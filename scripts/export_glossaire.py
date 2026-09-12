#!/usr/bin/env python3
"""Export tableur du glossaire (le dépôt fait foi ; l'export sert à la consultation).

    python3 scripts/export_glossaire.py sortie.csv
"""
from __future__ import annotations

import csv
import sys

from zeeplib import load_taxonomy, load_wiki

COLUMNS = ["Terme", "Slug", "Domaines", "Niveau (1re apparition)", "Définition",
           "Version simple", "Nb de liens", "Termes liés", "Relecture", "Sources"]


def main() -> int:
    out = sys.argv[1] if len(sys.argv) > 1 else "glossaire-export.csv"
    wiki, tax = load_wiki(), load_taxonomy()
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(COLUMNS)
        for slug, d in sorted(wiki.items(), key=lambda kv: kv[1]["term"].lower()):
            niveau = (d.get("niveau") or {}).get("premiereApparition", "")
            relec = d.get("relecture") or {}
            w.writerow([
                d["term"], slug,
                " | ".join(f"{x} {tax.get(x, '')}" for x in d["domains"]),
                niveau,
                d["definition"].replace("<br><br>", " / ").replace("<strong>", "").replace("</strong>", ""),
                d.get("versionSimple") or "",
                len(d["related"]),
                " | ".join(wiki[r]["term"] for r in d["related"] if r in wiki),
                f"{relec.get('statut', '')} {relec.get('date', '')}".strip(),
                " | ".join(s.get("titre", "") for s in d.get("sources", [])),
            ])
    print(f"{len(wiki)} fiches exportées vers {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
