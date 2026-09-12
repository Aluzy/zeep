"""Fonctions partagées par les scripts de contenu Zeep (stdlib uniquement)."""
from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "src" / "content" / "wiki"
BLOG_DIR = ROOT / "src" / "content" / "blog"
DIY_DIR = ROOT / "src" / "content" / "diy"
TAXONOMY_FILE = ROOT / "src" / "data" / "taxonomy.json"

LIGATURES = {"œ": "oe", "æ": "ae", "ﬁ": "fi"}  # non décomposées par NFKD

SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def slugify(term: str) -> str:
    """Convention des slugs (décidée le 11/09) : minuscules, accents retirés,
    tout caractère non alphanumérique (espace, apostrophe, parenthèse) -> tiret.
    "Facture d'électricité" -> "facture-d-electricite" ; "Loi d'Ohm" -> "loi-d-ohm".
    (L'ancienne convention supprimait l'apostrophe sans la remplacer par un tiret ;
    les fiches concernées ont été renommées avec scripts/rename_slug.py.)"""
    s = term.lower()
    for lig, rempl in LIGATURES.items():
        s = s.replace(lig, rempl)
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def load_json(path: Path):
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def dump_json(path: Path, data) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def load_wiki() -> dict[str, dict]:
    return {p.stem: load_json(p) for p in sorted(WIKI_DIR.glob("*.json"))}


def load_taxonomy() -> dict[str, str]:
    return load_json(TAXONOMY_FILE)


def read_frontmatter(path: Path) -> tuple[dict, str]:
    """Frontmatter minimal (clé: valeur JSON ou chaîne) — suffisant pour nos .md."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}, text
    _, fm, body = text.split("---", 2)
    data = {}
    for line in fm.strip().splitlines():
        if ":" not in line:
            continue
        key, raw = line.split(":", 1)
        raw = raw.strip()
        try:
            data[key.strip()] = json.loads(raw)
        except json.JSONDecodeError:
            data[key.strip()] = raw.strip('"')
    return data, body
