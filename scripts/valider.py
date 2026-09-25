#!/usr/bin/env python3
"""Validation humaine d'un lot, fiche par fiche : aperçu lisible puis changeset de validation.

    python3 scripts/valider.py J4-L1 --apercu               # agents/validations/J4-L1.md
    python3 scripts/valider.py J4-L1 [--sauf slug1,slug2]   # agents/changesets/J4-L1-validation.jsonl

SEUL ALEXANDRE lance la seconde commande, ou demande explicitement qu'on la lance pour lui
(AGENTS.md §3) : elle pose "statut": "valide" sur les fiches du lot.

Aperçu : pour chaque fiche du lot (changeset agents/changesets/<LOT>.jsonl), l'avant / après
de chaque champ modifié, les sources cliquables et l'état de la relecture. Le fichier Markdown
se lit directement sur GitHub, dans la pull request du lot.

Validation : une opération « relecture » par fiche, sauf celles listées dans --sauf. Seules les
fiches relues par un contrôleur indépendant (« relu-ia », par contenant « controleur ») peuvent
être validées ; les autres sont écartées et listées. Les deux changesets du lot (rédaction et
contrôle) doivent donc avoir été appliqués avant.
"""
from __future__ import annotations

import argparse
import datetime as dt
import sys

from apply_changeset import ChangesetError, avant_apres
from zeeplib import (AGENTS_DIR, CHANGESETS_DIR, ROOT, ecrire_changeset, lire_changeset, load_wiki,
                     slugs_du_changeset)

VALIDATIONS_DIR = AGENTS_DIR / "validations"
VALIDEUR = "Alexandre"


def relu_independamment(fiche: dict) -> bool:
    r = fiche.get("relecture") or {}
    return r.get("statut") == "relu-ia" and "controleur" in str(r.get("par", ""))


def texte(v) -> str:
    if v is None or v == [] or v == "":
        return "_(vide)_"
    if isinstance(v, list):
        v = ", ".join(str(x) for x in v)
    return str(v).replace("|", "\\|").replace("\n", " ")


def sources_md(sources) -> str:
    if not sources:
        return "_(aucune)_"
    return "<br>".join(f"[{s.get('titre')}]({s.get('url')}) ({s.get('type')})" for s in sources)


def apercu(lot: str, ops: list[dict], wiki: dict) -> int:
    try:
        avant, apres, deja = avant_apres(ops, wiki)
    except ChangesetError as e:
        print(f"Le changeset du lot ne s'applique pas : {e}")
        return 1
    slugs = slugs_du_changeset(ops)
    lignes = [f"# Validation du lot {lot}", "",
              f"{len(slugs)} fiche(s). Changeset {'appliqué au dépôt' if deja else '**non encore appliqué**'}.",
              "", "Pour valider : `python3 scripts/valider.py " + lot + " [--sauf slug1,slug2]` "
              "(Alexandre uniquement).", ""]
    for i, s in enumerate(slugs, 1):
        a, b = avant.get(s), apres[s]
        relec = b.get("relecture") or {}
        etat = f"{relec.get('statut')} par {relec.get('par')} le {relec.get('date')}" if relec else "non relue"
        drapeau = "✅" if relu_independamment(b) else "⛔ pas de relecture indépendante"
        lignes += [f"## {i}. {b.get('term')} (`{s}`)", "",
                   f"Relecture : {etat} — {drapeau}", "",
                   "| Champ | Avant | Après |", "|---|---|---|"]
        for champ in ("definition", "versionSimple", "synonymes"):
            va, vb = (a or {}).get(champ), b.get(champ)
            if a is None or va != vb:
                lignes.append(f"| {champ} | {texte(va) if a else '_(création)_'} | {texte(vb)} |")
        if a is None or (a or {}).get("sources") != b.get("sources"):
            lignes.append(f"| sources | {sources_md((a or {}).get('sources')) if a else '_(création)_'} "
                          f"| {sources_md(b.get('sources'))} |")
        lignes.append("")
    VALIDATIONS_DIR.mkdir(parents=True, exist_ok=True)
    chemin = VALIDATIONS_DIR / f"{lot}.md"
    chemin.write_text("\n".join(lignes).rstrip() + "\n", encoding="utf-8")
    print(f"{chemin.relative_to(ROOT)} : {len(slugs)} fiche(s)")
    return 0


def valider(lot: str, ops: list[dict], wiki: dict, sauf: set[str]) -> int:
    sortie = CHANGESETS_DIR / f"{lot}-validation.jsonl"
    if sortie.exists():
        print(f"{sortie.relative_to(ROOT)} existe déjà.")
        return 1
    slugs = slugs_du_changeset(ops)
    inconnus = sauf - set(slugs)
    if inconnus:
        print(f"--sauf cite des fiches hors du lot : {', '.join(sorted(inconnus))}")
        return 1
    date = dt.date.today().isoformat()
    valides, ecartees = [], []
    for s in slugs:
        if s in sauf:
            continue
        fiche = wiki.get(s)
        if fiche is None or not relu_independamment(fiche):
            ecartees.append(s)
            continue
        valides.append({"op": "set", "lot": f"{lot}-validation", "slug": s, "field": "relecture",
                        "old": fiche.get("relecture"),
                        "new": {"date": date, "par": VALIDEUR, "statut": "valide"},
                        "why": f"Validation humaine du lot {lot} par {VALIDEUR}."})
    if ecartees:
        print("Écartées (pas de relecture indépendante appliquée au dépôt) : " + ", ".join(ecartees))
    if not valides:
        print("Aucune fiche à valider.")
        return 1
    ecrire_changeset(sortie, valides)
    print(f"{sortie.relative_to(ROOT)} : {len(valides)} fiche(s) validée(s)"
          + (f", {len(sauf)} exclue(s) par --sauf" if sauf else ""))
    print(f"Appliquer : python3 scripts/apply_changeset.py {sortie.relative_to(ROOT)}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("lot")
    ap.add_argument("--apercu", action="store_true", help="écrit l'aperçu Markdown, ne valide rien")
    ap.add_argument("--sauf", default="", help="slugs à ne pas valider, séparés par des virgules")
    args = ap.parse_args()
    source = CHANGESETS_DIR / f"{args.lot}.jsonl"
    if not source.exists():
        print(f"{source.relative_to(ROOT)} introuvable.")
        return 1
    ops = lire_changeset(source)
    wiki = load_wiki()
    if args.apercu:
        return apercu(args.lot, ops, wiki)
    return valider(args.lot, ops, wiki, {s.strip() for s in args.sauf.split(",") if s.strip()})


if __name__ == "__main__":
    sys.exit(main())
