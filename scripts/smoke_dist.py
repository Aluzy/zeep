#!/usr/bin/env python3
"""Test de fumée sur le site construit (dossier dist/), lancé en CI après `npm run build`.

Évite la panne du 11/09 (définitions invisibles sur toutes les fiches) :
- chaque fiche wiki a une page générée avec un bloc .definition non vide ;
- chaque lien interne (href commençant par /zeep/) pointe vers une page existante.

    python3 scripts/smoke_dist.py [--base /zeep]
"""
from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path

from zeeplib import ROOT, load_wiki

DIST = ROOT / "dist"


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []
        self.depth = 0
        self.definition = ""

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])
        if self.depth:
            self.depth += 1
        elif tag == "div" and "definition" in (a.get("class") or "").split():
            self.depth = 1

    def handle_endtag(self, tag):
        if self.depth:
            self.depth -= 1

    def handle_data(self, data):
        if self.depth:
            self.definition += data


def main() -> int:
    base = "/zeep"
    if "--base" in sys.argv:
        base = sys.argv[sys.argv.index("--base") + 1].rstrip("/")
    if not DIST.exists():
        print("ERREUR dist/ absent : lancer npm run build d'abord")
        return 1
    errors: list[str] = []
    for slug in load_wiki():
        page = DIST / "wiki" / slug / "index.html"
        if not page.exists():
            errors.append(f"page manquante : wiki/{slug}/")
            continue
        p = PageParser()
        p.feed(page.read_text(encoding="utf-8"))
        if len(p.definition.strip()) < 20:
            errors.append(f"définition vide ou tronquée sur wiki/{slug}/")
    pages = list(DIST.rglob("*.html"))
    for page in pages:
        p = PageParser()
        p.feed(page.read_text(encoding="utf-8"))
        for href in p.links:
            if not href.startswith(base + "/"):
                continue
            path = re.split(r"[?#]", href[len(base):])[0].lstrip("/")
            target = DIST / path
            if not (target.is_file() or (target / "index.html").is_file()):
                errors.append(f"lien interne cassé {href} dans {page.relative_to(DIST)}")
    for e in sorted(set(errors)):
        print(f"ERREUR  {e}")
    print(f"{len(pages)} pages vérifiées, {len(set(errors))} erreur(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
