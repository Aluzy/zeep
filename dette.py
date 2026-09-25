#!/usr/bin/env python3
"""Dette éditoriale du wiki Zeep : les règles d'AGENTS.md que le corpus ne respecte pas encore.

    python3 scripts/dette.py                    # tableau : règle, fiches en défaut, base enregistrée
    python3 scripts/dette.py --detail REGLE     # liste des fiches en défaut pour une règle
    python3 scripts/dette.py --indicateurs      # tableau Markdown à coller dans un rapport de lot
    python3 scripts/dette.py --abaisser         # retire de la base les fiches corrigées (jamais d'ajout)
    python3 scripts/dette.py --initialiser      # (une seule fois) enregistre l'état actuel comme base

Pourquoi ce script existe
-------------------------
validate_content.py affichait « 0 erreur » alors que 182 définitions sur 387 sortaient de
la fourchette 25-60 mots, que 108 sources pointaient vers la page d'accueil d'Electropedia
et que 180 fiches étaient marquées « relu-ia » par l'agent qui les avait écrites. Les règles
existaient dans AGENTS.md, mais aucun script ne les vérifiait.

Rendre ces règles bloquantes d'un coup aurait mis la CI au rouge pour des centaines de
fiches. On applique donc un CLIQUET : src/data/dette.json enregistre, règle par règle, la
liste des fiches déjà en défaut. validate_content.py (donc la CI) échoue si une fiche qui
N'EST PAS dans cette liste enfreint la règle. La dette existante est tolérée, mais on ne
peut plus en ajouter. Chaque lot qui corrige des fiches lance ensuite `--abaisser`, et la
liste ne fait que raccourcir.

Ajouter une fiche à la base à la main revient à accepter une nouvelle dette : c'est une
décision humaine, visible dans la revue de la pull request.
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

from zeeplib import ROOT, load_wiki

DETTE_FILE = ROOT / "src" / "data" / "dette.json"

# --- Paramètres des règles (AGENTS.md §3) ----------------------------------------------
DEFINITION_MIN, DEFINITION_MAX = 25, 60
VERSION_SIMPLE_MIN, VERSION_SIMPLE_MAX = 12, 35
TYPES_SOURCE = ("programme", "reference", "norme", "manuel")
NIVEAUX_AVANT_LYCEE = ("C1", "C2", "C3", "C4")
HTML_RE = re.compile(r"</?[a-zA-Z][^>]*>")

# Libellés affichés (ordre = ordre d'affichage).
REGLES = {
    "definition_longueur": f"Définition hors {DEFINITION_MIN}-{DEFINITION_MAX} mots",
    "definition_html": "Balise HTML dans la définition",
    "version_simple_manquante_avant_lycee": "Notion vue avant le lycée (C1-C4) sans version simple",
    "version_simple_longueur": f"Version simple hors {VERSION_SIMPLE_MIN}-{VERSION_SIMPLE_MAX} mots",
    "securite_230v_absente": "Fiche liée au secteur sans rappel de sécurité",
    "source_sans_url": "Source sans URL",
    "source_url_racine": "Source pointant vers une page d'accueil (invérifiable)",
    "source_type_hors_liste": "Type de source hors liste (" + "|".join(TYPES_SOURCE) + ")",
    "relecture_non_independante": "« relu-ia » posé par un autre agent que le contrôleur",
}


def mots(texte: str | None) -> int:
    return len((texte or "").split())


def charger_config() -> dict:
    if not DETTE_FILE.exists():
        return {}
    return json.loads(DETTE_FILE.read_text(encoding="utf-8"))


def _texte(fiche: dict) -> str:
    return f"{fiche.get('definition') or ''} {fiche.get('versionSimple') or ''}"


def defauts(wiki: dict, config: dict | None = None) -> dict[str, set[str]]:
    """Règle -> ensemble des slugs en défaut, sur le corpus tel qu'il est."""
    config = charger_config() if config is None else config
    secu = config.get("securite230V", {})
    mots_cles = re.compile("|".join(secu.get("motsCles", [])) or r"(?!x)x", re.I)
    rappel = re.compile("|".join(secu.get("formulesRappel", [])) or r"(?!x)x", re.I)
    exemptees = set(secu.get("exemptees", {}))

    res: dict[str, set[str]] = {r: set() for r in REGLES}
    for slug, f in wiki.items():
        definition = f.get("definition") or ""
        if not DEFINITION_MIN <= mots(definition) <= DEFINITION_MAX:
            res["definition_longueur"].add(slug)
        if HTML_RE.search(definition):
            res["definition_html"].add(slug)

        vs = f.get("versionSimple")
        niveau = f.get("niveau") or {}
        if niveau.get("premiereApparition") in NIVEAUX_AVANT_LYCEE and not vs:
            res["version_simple_manquante_avant_lycee"].add(slug)
        if vs and not VERSION_SIMPLE_MIN <= mots(vs) <= VERSION_SIMPLE_MAX:
            res["version_simple_longueur"].add(slug)

        texte = _texte(f)
        if slug not in exemptees and mots_cles.search(texte) and not rappel.search(texte):
            res["securite_230v_absente"].add(slug)

        for s in f.get("sources") or []:
            url = str(s.get("url") or "").strip()
            if not url:
                res["source_sans_url"].add(slug)
            elif urlparse(url).path.strip("/") == "" and not urlparse(url).query:
                res["source_url_racine"].add(slug)
            if s.get("type") not in TYPES_SOURCE:
                res["source_type_hors_liste"].add(slug)

        relec = f.get("relecture") or {}
        if relec.get("statut") == "relu-ia" and "controleur" not in str(relec.get("par", "")):
            res["relecture_non_independante"].add(slug)
    return res


def verifier(wiki: dict) -> tuple[list[str], list[str]]:
    """(erreurs, notes) pour validate_content.py. Erreur = défaut hors de la base."""
    config = charger_config()
    if not config:
        return ([f"{DETTE_FILE.relative_to(ROOT)} absent : lancer scripts/dette.py --initialiser"], [])
    base = config.get("base", {})
    erreurs, notes = [], []
    for regle, slugs in defauts(wiki, config).items():
        tolere = set(base.get(regle, []))
        for slug in sorted(slugs - tolere):
            erreurs.append(f"wiki/{slug}.json : {REGLES[regle].lower()} (règle « {regle} », "
                           "nouvelle dette interdite : voir scripts/dette.py)")
        corriges = tolere - slugs
        if corriges:
            notes.append(f"dette « {regle} » : {len(corriges)} fiche(s) corrigée(s), "
                         "lancer scripts/dette.py --abaisser")
    return erreurs, notes


def indicateurs(wiki: dict) -> list[tuple[str, str]]:
    """Indicateurs de pilotage (à comparer avant/après un lot)."""
    n = len(wiki)
    d = defauts(wiki)

    def part(k: int, total: int) -> str:
        return f"{k}/{total} ({round(100 * k / total) if total else 0} %)"

    avant_lycee = [s for s, f in wiki.items()
                   if (f.get("niveau") or {}).get("premiereApparition") in NIVEAUX_AVANT_LYCEE]
    def precise(src: dict) -> bool:
        u = urlparse(str(src.get("url") or "").strip())
        return bool(u.netloc) and (u.path.strip("/") != "" or bool(u.query))

    sources_precises = [s for s, f in wiki.items() if any(precise(x) for x in f.get("sources") or [])]
    statuts = Counter((f.get("relecture") or {}).get("statut") for f in wiki.values())
    return [
        ("Fiches", str(n)),
        ("Définitions de 25 à 60 mots", part(n - len(d["definition_longueur"]), n)),
        ("Version simple, notions vues avant le lycée",
         part(len(avant_lycee) - len(d["version_simple_manquante_avant_lycee"]), len(avant_lycee))),
        ("Version simple, toutes fiches", part(sum(1 for f in wiki.values() if f.get("versionSimple")), n)),
        ("Avec niveau scolaire", part(sum(1 for f in wiki.values() if f.get("niveau")), n)),
        ("Avec au moins une source précise (URL non racine)", part(len(sources_precises), n)),
        ("Relues par un contrôleur indépendant",
         part(statuts.get("relu-ia", 0) - len(d["relecture_non_independante"]), n)),
        ("Validées par Alexandre", part(statuts.get("valide", 0), n)),
        ("Fiches secteur sans rappel de sécurité", str(len(d["securite_230v_absente"]))),
    ]


def ecrire(config: dict) -> None:
    DETTE_FILE.write_text(json.dumps(config, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    args = sys.argv[1:]
    wiki = load_wiki()
    config = charger_config()

    if "--initialiser" in args:
        if config.get("base") and "--force" not in args:
            print("Base déjà présente : --initialiser ne sert qu'une fois (ajouter --force pour écraser).")
            return 1
        config["base"] = {r: sorted(s) for r, s in defauts(wiki, config).items()}
        ecrire(config)
        print(f"{DETTE_FILE.relative_to(ROOT)} initialisé.")
        return 0

    actuels = defauts(wiki, config)
    base = config.get("base", {})

    if "--abaisser" in args:
        total = 0
        for regle in REGLES:
            avant = set(base.get(regle, []))
            apres = avant & actuels[regle]  # on retire les corrigées, on n'ajoute jamais
            total += len(avant) - len(apres)
            base[regle] = sorted(apres)
        config["base"] = base
        ecrire(config)
        print(f"Base abaissée : {total} fiche(s) retirée(s) de la dette.")
        return 0

    if "--detail" in args:
        i = args.index("--detail")
        regle = args[i + 1] if i + 1 < len(args) else ""
        if regle not in REGLES:
            print("Règles connues : " + ", ".join(REGLES))
            return 1
        tolere = set(base.get(regle, []))
        for slug in sorted(actuels[regle]):
            print(slug + ("" if slug in tolere else "   <- NOUVEAU (bloquant)"))
        return 0

    if "--indicateurs" in args:
        print("| Indicateur | Valeur |\n|---|---|")
        for k, v in indicateurs(wiki):
            print(f"| {k} | {v} |")
        return 0

    print(f"{'Règle':40} {'Actuel':>7} {'Base':>6}  Libellé")
    bloquant = False
    for regle, libelle in REGLES.items():
        nouveaux = actuels[regle] - set(base.get(regle, []))
        bloquant |= bool(nouveaux)
        drapeau = f"  +{len(nouveaux)} NOUVEAU" if nouveaux else ""
        print(f"{regle:40} {len(actuels[regle]):>7} {len(base.get(regle, [])):>6}  {libelle}{drapeau}")
    return 1 if bloquant else 0


if __name__ == "__main__":
    sys.exit(main())
