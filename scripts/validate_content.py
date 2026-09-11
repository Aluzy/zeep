#!/usr/bin/env python3
"""Garde-fou du contenu Zeep. À lancer avant tout commit et en CI.

    python3 scripts/validate_content.py          # erreurs => code de sortie 1
    python3 scripts/validate_content.py --stats  # + statistiques de couverture

Vérifie : schéma des fiches wiki, slug = nom de fichier = slugify(term),
références (related, blog, DIY) existantes, réciprocité des liens wiki,
domaines connus, définitions non vides, doublons de termes, URLs vides.
"""
from __future__ import annotations

import sys
from collections import Counter

from zeeplib import (BLOG_DIR, DIY_DIR, SLUG_RE, load_json, load_taxonomy,
                     load_wiki, read_frontmatter, slugify)

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
    # Champs ajoutés au Jour 2 (optionnels tant que la migration n'est pas finie)
    "niveau": ((dict, type(None)), False),
    "versionSimple": ((str, type(None)), False),
    "sources": ((list,), False),
    "relecture": ((dict, type(None)), False),
}
NIVEAU_KEYS = {"premiereApparition", "cycles", "familles", "matriceIds"}
RELECTURE_KEYS = {"date", "par", "statut"}


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    wiki = load_wiki()
    taxonomy = load_taxonomy()

    terms = Counter(d.get("term", "").strip().lower() for d in wiki.values())
    for t, n in terms.items():
        if n > 1:
            errors.append(f"terme en double ({n}×) : {t}")

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
        niveau = d.get("niveau")
        if isinstance(niveau, dict) and not set(niveau) <= NIVEAU_KEYS:
            errors.append(f"{where} : clés inconnues dans niveau {set(niveau) - NIVEAU_KEYS}")
        relec = d.get("relecture")
        if isinstance(relec, dict) and not set(relec) <= RELECTURE_KEYS:
            errors.append(f"{where} : clés inconnues dans relecture {set(relec) - RELECTURE_KEYS}")
        for s in d.get("sources", []):
            if not isinstance(s, dict) or not s.get("titre"):
                errors.append(f"{where} : source invalide (objet avec au moins « titre » attendu)")

    for path in sorted(BLOG_DIR.glob("*.md")):
        fm, body = read_frontmatter(path)
        where = f"blog/{path.name}"
        for key in ("title", "domain", "excerpt"):
            if not fm.get(key):
                errors.append(f"{where} : frontmatter « {key} » manquant")
        if fm.get("domain") and fm["domain"] not in taxonomy:
            errors.append(f"{where} : domaine inconnu « {fm['domain']} »")
        for r in fm.get("related", []) or []:
            if r not in wiki:
                errors.append(f"{where} : lien vers une fiche inexistante « {r} »")
        words = len(body.split())
        if words < 600:
            warnings.append(f"{where} : article court ({words} mots, cible ≥ 800)")

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
        print(f"Avec version simple  : {sum(1 for d in wiki.values() if d.get('versionSimple'))}")
        print(f"Relues               : {sum(1 for d in wiki.values() if (d.get('relecture') or {}).get('statut') == 'relu')}")

    for w in warnings:
        print(f"AVERTISSEMENT  {w}")
    for e in errors:
        print(f"ERREUR         {e}")
    print(f"\n{len(errors)} erreur(s), {len(warnings)} avertissement(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
