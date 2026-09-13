#!/usr/bin/env python3
"""Garde-fou du contenu Zeep. À lancer avant tout commit et en CI.

    python3 scripts/validate_content.py          # erreurs => code de sortie 1
    python3 scripts/validate_content.py --stats  # + statistiques de couverture

Vérifie : schéma des fiches wiki, slug = nom de fichier = slugify(term),
références (related, blog, DIY) existantes, réciprocité des liens wiki,
domaines connus, définitions non vides, doublons de termes, URLs vides,
synonymes non ambigus, et effectif plancher de chaque domaine.

Ce script contrôle la CONFORMITÉ de ce qui existe. Il ne dit pas ce qui manque :
c'est le rôle de scripts/audit_couverture.py, à lancer dans la foulée.
"""
from __future__ import annotations

import datetime
import re
import sys
from collections import Counter

from zeeplib import (BLOG_DIR, DIY_DIR, SLUG_RE, load_couverture, load_json,
                     load_taxonomy, load_wiki, normaliser, read_frontmatter,
                     slugify)

# Champs de fiche wiki : nom -> (types acceptés, obligatoire)
WIKI_FIELDS = {
    "term": ((str,), True),
    "slug": ((str,), True),
    "domains": ((list,), True),
    "sourceDomain": ((list,), True),
    "merged": ((bool,), True),
    "pillar": ((bool,), False),
    "illustration": ((str, type(None)), False),
    "definition": ((str,), True),
    "related": ((list,), True),
    "synonymes": ((list,), False),
    # Champs ajoutés au Jour 2 (optionnels tant que la migration n'est pas finie)
    "niveau": ((dict, type(None)), False),
    "versionSimple": ((str, type(None)), False),
    "sources": ((list,), False),
    "relecture": ((dict, type(None)), False),
}
NIVEAU_KEYS = {"premiereApparition", "cycles", "familles", "matriceIds"}
RELECTURE_KEYS = {"date", "par", "statut"}
# Codes de la colonne « Cycle_scolaire_normalise » de la matrice curriculaire.
# Même liste que NIVEAU_LABEL dans src/lib/helpers.ts : garder les deux synchronisées.
NIVEAUX = ["C1", "C2", "C3", "C4", "2GT", "1G", "TG", "1-TG", "STI2D", "CAP", "BACPRO"]
RELECTURE_STATUTS = ("relu-ia", "valide")
# Version simple : 1 à 2 phrases pour un élève de 8-11 ans (AGENTS.md §3).
# La borne haute reste large pour ne pas bloquer une reformulation en cours de lot.
VERSION_SIMPLE_MIN_MOTS = 8
VERSION_SIMPLE_MAX_MOTS = 60
# Date de publication des articles de blog : "AAAA-MM-JJ" (chaîne, cf. src/content/config.ts).
BLOG_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    wiki = load_wiki()
    taxonomy = load_taxonomy()

    terms = Counter(d.get("term", "").strip().lower() for d in wiki.values())
    for t, n in terms.items():
        if n > 1:
            errors.append(f"terme en double ({n}×) : {t}")

    autres_termes = {normaliser(d.get("term", "")): stem for stem, d in wiki.items()}

    for stem, d in wiki.items():
        where = f"wiki/{stem}.json"
        for key in d:
            if key not in WIKI_FIELDS:
                errors.append(f"{where} : champ inconnu « {key} » (ajouter au schéma d'abord)")
        for key, (types, required) in WIKI_FIELDS.items():
            if key not in d:
                if required:
                    errors.append(f"{where} : champ obligatoire manquant « {key} »")
                continue
            if not isinstance(d[key], types):
                errors.append(f"{where} : « {key} » a un type invalide")
        if d.get("slug") != stem:
            errors.append(f"{where} : slug « {d.get('slug')} » ≠ nom de fichier")
        if not SLUG_RE.match(stem):
            errors.append(f"{where} : slug mal formé")
        if isinstance(d.get("term"), str) and slugify(d["term"]) != stem:
            errors.append(f"{where} : slug attendu « {slugify(d['term'])} » pour le terme « {d['term']} »")
        if not str(d.get("definition", "")).strip():
            errors.append(f"{where} : définition vide")
        for dom in d.get("domains", []):
            if dom not in taxonomy:
                errors.append(f"{where} : domaine inconnu « {dom} »")
        if not d.get("domains"):
            errors.append(f"{where} : aucun domaine")
        rel = d.get("related", [])
        if len(rel) != len(set(rel)):
            errors.append(f"{where} : liens en double dans related")
        for r in rel:
            if r == stem:
                errors.append(f"{where} : se cite lui-même")
            elif r not in wiki:
                errors.append(f"{where} : lien vers une fiche inexistante « {r} »")
            elif stem not in wiki[r].get("related", []):
                errors.append(f"{where} : lien non réciproque avec « {r} »")
        if not rel:
            warnings.append(f"{where} : aucune fiche liée")
        syns = d.get("synonymes") or []
        formes_vues: set[str] = set()
        for syn in syns:
            if not isinstance(syn, str) or not syn.strip():
                errors.append(f"{where} : synonyme vide")
                continue
            forme = normaliser(syn)
            if forme in formes_vues:
                errors.append(f"{where} : synonyme en double « {syn} »")
            formes_vues.add(forme)
            if forme in autres_termes and autres_termes[forme] != stem:
                errors.append(
                    f"{where} : le synonyme « {syn} » est déjà le terme de la fiche "
                    f"« {autres_termes[forme]} » (ambiguïté de recherche)"
                )
        niveau = d.get("niveau")
        if isinstance(niveau, dict):
            if not set(niveau) <= NIVEAU_KEYS:
                errors.append(f"{where} : clés inconnues dans niveau {set(niveau) - NIVEAU_KEYS}")
            premiere = niveau.get("premiereApparition")
            if premiere is None:
                errors.append(f"{where} : niveau sans « premiereApparition »")
            elif premiere not in NIVEAUX:
                errors.append(
                    f"{where} : niveau « {premiere} » inconnu (attendus : {', '.join(NIVEAUX)})"
                )
        version_simple = d.get("versionSimple")
        if isinstance(version_simple, str):
            mots = len(version_simple.split())
            if not VERSION_SIMPLE_MIN_MOTS <= mots <= VERSION_SIMPLE_MAX_MOTS:
                errors.append(
                    f"{where} : version simple de {mots} mot(s) "
                    f"(attendu : {VERSION_SIMPLE_MIN_MOTS} à {VERSION_SIMPLE_MAX_MOTS} ; "
                    "mettre null s'il n'y en a pas)"
                )
        relec = d.get("relecture")
        if isinstance(relec, dict):
            if not set(relec) <= RELECTURE_KEYS:
                errors.append(f"{where} : clés inconnues dans relecture {set(relec) - RELECTURE_KEYS}")
            if relec.get("statut") not in RELECTURE_STATUTS:
                errors.append(
                    f"{where} : statut de relecture « {relec.get('statut')} » invalide "
                    f"(attendus : {', '.join(RELECTURE_STATUTS)})"
                )
        for s in d.get("sources", []):
            if not isinstance(s, dict) or not str(s.get("titre") or "").strip():
                errors.append(f"{where} : source invalide (objet avec au moins « titre » non vide attendu)")

    # Couverture par domaine : la taxonomie est une cible, pas une étiquette.
    couverture = load_couverture()
    effectifs = Counter(x for d in wiki.values() for x in d.get("domains", []))
    for code in sorted(taxonomy):
        seuil = int(couverture.get("plancherParDomaine", {}).get(code, 0))
        if effectifs.get(code, 0) < seuil:
            warnings.append(
                f"domaine {code} ({taxonomy[code]}) : {effectifs.get(code, 0)} fiche(s) "
                f"pour un plancher de {seuil} — voir scripts/audit_couverture.py"
            )

    for path in sorted(BLOG_DIR.glob("*.md")):
        fm, body = read_frontmatter(path)
        where = f"blog/{path.name}"
        for key in ("title", "domain", "excerpt", "date"):
            if not fm.get(key):
                errors.append(f"{where} : frontmatter « {key} » manquant")
        if fm.get("domain") and fm["domain"] not in taxonomy:
            errors.append(f"{where} : domaine inconnu « {fm['domain']} »")
        date = fm.get("date")
        if date is not None:
            if not isinstance(date, str) or not BLOG_DATE_RE.match(date):
                errors.append(f"{where} : date « {date} » attendue au format AAAA-MM-JJ")
            else:
                try:
                    datetime.date.fromisoformat(date)
                except ValueError:
                    errors.append(f"{where} : date « {date} » invalide")
        for r in fm.get("related", []) or []:
            if r not in wiki:
                errors.append(f"{where} : lien vers une fiche inexistante « {r} »")
        for s in fm.get("sources", []) or []:
            if not isinstance(s, dict) or not str(s.get("titre") or "").strip():
                errors.append(f"{where} : source invalide (objet avec au moins « titre » non vide attendu)")
        words = len(body.split())
        if words < 600:
            warnings.append(f"{where} : article court ({words} mots, cible ≥ 800)")
        if not fm.get("sources"):
            warnings.append(f"{where} : aucune source déclarée")

    for path in sorted(DIY_DIR.glob("*.json")):
        d = load_json(path)
        where = f"diy/{path.name}"
        if d.get("slug") != path.stem:
            errors.append(f"{where} : slug ≠ nom de fichier")
        for r in d.get("related", []):
            if r not in wiki:
                errors.append(f"{where} : lien vers une fiche inexistante « {r} »")
        if "notionsWiki" in d:
            errors.append(f"{where} : champ obsolète « notionsWiki » (utiliser related)")
        for v in d.get("videos", []):
            if not str(v.get("url", "")).strip():
                errors.append(f"{where} : vidéo sans URL (retirer l'entrée ou la renseigner)")
        for c in d.get("composants", []):
            for lien in c.get("liens", []):
                if not str(lien.get("url", "")).strip():
                    errors.append(f"{where} : lien d'achat sans URL pour « {c.get('nom')} »")

    if "--stats" in sys.argv:
        dom = Counter(x for d in wiki.values() for x in d.get("domains", []))
        print(f"Fiches wiki : {len(wiki)}")
        print(f"Liens wiki  : {sum(len(d.get('related', [])) for d in wiki.values())}")
        print("Fiches par domaine : " + ", ".join(f"{k}={dom.get(k, 0)}" for k in taxonomy))
        print(f"Avec niveau scolaire : {sum(1 for d in wiki.values() if d.get('niveau'))}")
        niv = Counter(
            (d.get("niveau") or {}).get("premiereApparition")
            for d in wiki.values()
            if isinstance(d.get("niveau"), dict)
        )
        autres = sorted(str(k) for k in niv if k is not None and k not in NIVEAUX)
        detail = ", ".join(f"{k}={niv.get(k, 0)}" for k in NIVEAUX + autres)
        print(f"Fiches par niveau    : {detail}")
        print(f"Avec version simple  : {sum(1 for d in wiki.values() if d.get('versionSimple'))}")
        print(f"Avec synonymes       : {sum(1 for d in wiki.values() if d.get('synonymes'))} "
              f"({sum(len(d.get('synonymes') or []) for d in wiki.values())} formes déclarées)")
        statuts = Counter((d.get("relecture") or {}).get("statut") for d in wiki.values())
        print(f"Relues               : {statuts.get('relu-ia', 0)} relu-ia, {statuts.get('valide', 0)} validées par Alexandre")

    for w in warnings:
        print(f"AVERTISSEMENT  {w}")
    for e in errors:
        print(f"ERREUR         {e}")
    print(f"\n{len(errors)} erreur(s), {len(warnings)} avertissement(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
