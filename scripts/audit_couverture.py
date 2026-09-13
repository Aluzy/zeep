#!/usr/bin/env python3
"""Audit de COUVERTURE du glossaire Zeep : ce qui manque, pas ce qui est faux.

    python3 scripts/audit_couverture.py              # rapport complet
    python3 scripts/audit_couverture.py --ci         # + code de sortie 1 si blocage
    python3 scripts/audit_couverture.py --backlog J4 # écrit un squelette de changeset

Pourquoi ce script existe
-------------------------
validate_content.py vérifie la conformité de ce qui est écrit : schéma, slugs,
réciprocité des liens. Un glossaire à moitié rempli mais parfaitement cohérent
passe donc tous les contrôles au vert. C'est ce qui s'est produit : le corpus a
été amorcé à partir de quelques listes génériques (`sourceDomain`), la taxonomie
à 24 domaines n'a servi qu'à étiqueter après coup, et le rapprochement avec la
matrice curriculaire n'a été fait que dans le sens matrice -> fiche. Résultat :
des domaines entiers quasi vides et aucune fiche pour le farad, le coulomb, le
henry, le hertz ou le joule — alors que les fiches Condensateur, Charge
électrique, Bobine et Fréquence existaient déjà.

Les quatre audits ci-dessous ferment chacun une de ces portes.

  1. Programmes   : termes de la matrice curriculaire sans fiche (sens inverse
                    du mapping du lot J2, celui qui n'avait jamais été exploité).
  2. Domaines     : effectif de chaque domaine face au plancher de couverture.json.
  3. Lexique      : entrées de lexique-attendu.json sans fiche. Une entrée déjà
                    citée dans une définition existante est « citée mais absente »,
                    c'est-à-dire le cas farad : priorité maximale.
  4. Qualité      : fiches trop peu maillées, sans version simple ou sans source.

Le rapprochement se fait sur la forme normalisée du terme ET de ses synonymes :
une fiche « Modulation de largeur d'impulsion (PWM) » couvre donc « PWM » et
« MLI » si ces formes sont déclarées dans son champ `synonymes`.
"""
from __future__ import annotations

import csv
import json
import sys
from collections import Counter
from pathlib import Path

from zeeplib import (MATRICE_FILE, formes_d_une_fiche, load_couverture,
                     load_lexique, load_taxonomy, load_wiki, normaliser,
                     slugify)

# Colonnes de la matrice curriculaire qui portent du vocabulaire à couvrir.
COLONNES_MATRICE = ("Notion (normalisée)", "Vocabulaire associé")
# Séparateurs employés dans la colonne « Vocabulaire associé ».
SEPARATEURS = (";", "|", ",")
# En dessous de cette longueur, un terme isolé n'est pas exploitable.
LONGUEUR_MIN = 3
# Au-delà, la colonne « Vocabulaire associé » donne une phrase de programme
# (« architecture matérielle et logicielle »), pas un terme de glossaire.
MOTS_MAX = 4
# Formulations de la matrice qui décrivent une absence ou un attendu pédagogique,
# et qui ne désignent donc aucune notion à définir.
DEBUTS_IGNORES = ("absence", "pas de", "aucun", "cahier des charges", "attendu")
# Mots vides : un « terme » qui s'y réduit n'apporte rien.
MOTS_VIDES = {"le", "la", "les", "de", "des", "du", "et", "ou", "un", "une",
              "en", "au", "aux", "a", "d", "l", "son", "sa", "ses", "besoin",
              "notion", "notions", "etude", "exemple", "exemples"}


def singulier(forme: str) -> str:
    """Forme comparable au pluriel près : « capteurs » et « capteur » se valent."""
    mots = []
    for mot in forme.split():
        if len(mot) > 3 and mot[-1] in "sx":
            mot = mot[:-1]
        mots.append(mot)
    return " ".join(mots)


def index_des_formes(wiki: dict) -> dict[str, str]:
    """Forme normalisée -> slug de la fiche qui la couvre (terme ou synonyme).

    Chaque forme est indexée telle quelle ET au singulier, sans quoi le simple
    pluriel d'un terme de programme ressortirait comme une lacune.
    """
    index: dict[str, str] = {}
    for slug, fiche in wiki.items():
        for forme in formes_d_une_fiche(fiche):
            index.setdefault(forme, slug)
            index.setdefault(singulier(forme), slug)
    return index


def couvert(forme: str, index: dict[str, str]) -> bool:
    return forme in index or singulier(forme) in index


def exploitable(forme: str) -> bool:
    """Écarte les formulations de programme qui ne désignent pas une notion."""
    if len(forme) < LONGUEUR_MIN:
        return False
    mots = forme.split()
    if len(mots) > MOTS_MAX:
        return False
    if forme.startswith(DEBUTS_IGNORES):
        return False
    return any(m not in MOTS_VIDES for m in mots)


def termes_de_la_matrice() -> dict[str, list[str]]:
    """Terme normalisé -> identifiants de lignes de la matrice qui le citent."""
    if not MATRICE_FILE.exists():
        return {}
    trouves: dict[str, list[str]] = {}
    with MATRICE_FILE.open(encoding="utf-8", newline="") as f:
        for ligne in csv.DictReader(f):
            ident = (ligne.get("ID_Ligne") or "?").strip()
            for colonne in COLONNES_MATRICE:
                brut = (ligne.get(colonne) or "").strip()
                if not brut:
                    continue
                morceaux = [brut]
                for sep in SEPARATEURS:
                    morceaux = [m for bloc in morceaux for m in bloc.split(sep)]
                for morceau in morceaux:
                    forme = normaliser(morceau)
                    if not exploitable(forme):
                        continue
                    trouves.setdefault(forme, [])
                    if ident not in trouves[forme]:
                        trouves[forme].append(ident)
    return trouves


def citations_dans_le_corpus(wiki: dict, formes: list[str]) -> dict[str, int]:
    """Combien de définitions existantes emploient déjà telle forme absente.

    C'est le détecteur d'orphelins : un mot que le corpus utilise couramment
    sans lui consacrer de fiche est une lacune que personne ne voit passer.
    """
    textes = [
        normaliser(" ".join([
            fiche.get("definition", ""),
            fiche.get("versionSimple") or "",
        ]))
        for fiche in wiki.values()
    ]
    compte: dict[str, int] = {}
    for forme in formes:
        if len(forme) < 4:
            continue
        n = sum(1 for t in textes if forme in t)
        if n:
            compte[forme] = n
    return compte


def main() -> int:
    ci = "--ci" in sys.argv
    backlog = None
    if "--backlog" in sys.argv:
        i = sys.argv.index("--backlog")
        backlog = sys.argv[i + 1] if len(sys.argv) > i + 1 else "BACKLOG"

    wiki = load_wiki()
    taxonomy = load_taxonomy()
    couverture = load_couverture()
    lexique = load_lexique()
    index = index_des_formes(wiki)
    bloquants = 0

    print(f"Fiches wiki : {len(wiki)} — formes reconnues : {len(index)}\n")

    # ------------------------------------------------------------ 1. Programmes
    print("1. PROGRAMMES — termes de la matrice curriculaire sans fiche")
    matrice = termes_de_la_matrice()
    if not matrice:
        print("   (matrice introuvable : audit ignoré)")
        orphelins_matrice: list[str] = []
    else:
        orphelins_matrice = sorted(f for f in matrice if not couvert(f, index))
        print(f"   {len(matrice) - len(orphelins_matrice)}/{len(matrice)} formes couvertes")
        for forme in orphelins_matrice[:40]:
            print(f"   MANQUE  {forme}  (lignes {', '.join(matrice[forme][:4])})")
        if len(orphelins_matrice) > 40:
            print(f"   … et {len(orphelins_matrice) - 40} autres")
    print()

    # -------------------------------------------------------------- 2. Domaines
    print("2. DOMAINES — effectif face au plancher de couverture.json")
    planchers = couverture.get("plancherParDomaine", {})
    effectifs = Counter(x for d in wiki.values() for x in d.get("domains", []))
    sous_plancher = []
    for code in sorted(taxonomy):
        n, seuil = effectifs.get(code, 0), int(planchers.get(code, 0))
        etat = "OK  " if n >= seuil else "SOUS"
        if n < seuil:
            sous_plancher.append(code)
            bloquants += 1
        print(f"   {etat} {code} {taxonomy[code][:44]:<44} {n:>3} / {seuil}")
    print()

    # --------------------------------------------------------------- 3. Lexique
    print("3. LEXIQUE DE RÉFÉRENCE — entrées attendues sans fiche")
    attendu = lexique.get("attendu", {})
    manquants: dict[str, list[str]] = {}
    for code, termes in sorted(attendu.items()):
        absents = [t for t in termes if not couvert(normaliser(t), index)]
        if absents:
            manquants[code] = absents
    tous_absents = sorted({t for v in manquants.values() for t in v})
    cites = citations_dans_le_corpus(wiki, [normaliser(t) for t in tous_absents])
    prioritaires = sorted(
        (t for t in tous_absents if normaliser(t) in cites),
        key=lambda t: (-cites[normaliser(t)], t),
    )
    total_attendu = sum(len(v) for v in attendu.values())
    print(f"   {total_attendu - len(tous_absents)}/{total_attendu} entrées couvertes")
    if prioritaires:
        print("   --- cités dans des définitions existantes mais sans fiche (priorité 1) ---")
        for t in prioritaires:
            print(f"   MANQUE  {t}  (cité dans {cites[normaliser(t)]} fiche(s))")
        bloquants += len(prioritaires)
    for code, absents in manquants.items():
        restants = [t for t in absents if t not in prioritaires]
        if restants:
            print(f"   {code} : " + ", ".join(restants))
    print()

    # --------------------------------------------------------------- 4. Qualité
    print("4. QUALITÉ — maillage, version simple, sources")
    q = couverture.get("qualite", {})
    lmin = int(q.get("liensMinimum", 3))
    faibles = sorted(s for s, d in wiki.items() if len(d.get("related", [])) < lmin)
    sans_simple = [s for s, d in wiki.items() if not d.get("versionSimple")]
    sans_source = [s for s, d in wiki.items() if not d.get("sources")]
    sans_syn = [s for s, d in wiki.items() if not d.get("synonymes")]
    print(f"   Moins de {lmin} liens        : {len(faibles)} fiche(s)")
    if faibles:
        print("      " + ", ".join(faibles[:25]) + (" …" if len(faibles) > 25 else ""))
    for libelle, lot, cible in (
        ("Sans version simple", sans_simple, float(q.get("partVersionSimpleCible", 0))),
        ("Sans source", sans_source, float(q.get("partSourcesCible", 0))),
    ):
        part = 1 - len(lot) / len(wiki) if wiki else 0
        etat = "OK" if part >= cible else "SOUS"
        print(f"   {libelle:<22} : {len(lot)} fiche(s) — couverture {part:.0%} (cible {cible:.0%}) [{etat}]")
    print(f"   Sans synonymes         : {len(sans_syn)} fiche(s)")
    print()

    # -------------------------------------------------- squelette de changeset
    if backlog:
        chemin = Path("agents/changesets") / f"{backlog}-backlog.jsonl"
        chemin.parent.mkdir(parents=True, exist_ok=True)
        lignes = []
        for code, absents in sorted(manquants.items()):
            for terme in absents:
                lignes.append(json.dumps({
                    "op": "create", "lot": backlog,
                    "data": {
                        "term": terme, "domains": [code], "definition": "À RÉDIGER",
                        "versionSimple": None, "synonymes": [], "related": [],
                        "sources": [], "relecture": None,
                    },
                    "_slugPrevu": slugify(terme),
                    "why": f"Entrée du lexique de référence sans fiche (audit de couverture, domaine {code}).",
                }, ensure_ascii=False))
        chemin.write_text("\n".join(lignes) + "\n", encoding="utf-8")
        print(f"Squelette de changeset écrit : {chemin} ({len(lignes)} création(s) à rédiger)")
        print("Les définitions valent « À RÉDIGER » : le fichier n'est PAS applicable tel quel.\n")

    # ------------------------------------------------------------------ verdict
    print(f"Bilan : {len(orphelins_matrice)} terme(s) de programme sans fiche, "
          f"{len(sous_plancher)} domaine(s) sous plancher, "
          f"{len(tous_absents)} entrée(s) de lexique à écrire "
          f"(dont {len(prioritaires)} déjà citée(s) dans le corpus).")
    if ci and bloquants:
        print(f"\nÉCHEC : {bloquants} point(s) bloquant(s) — domaine sous plancher "
              "ou terme cité sans fiche.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
