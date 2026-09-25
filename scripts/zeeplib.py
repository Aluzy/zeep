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
COUVERTURE_FILE = ROOT / "src" / "data" / "couverture.json"
LEXIQUE_FILE = ROOT / "src" / "data" / "lexique-attendu.json"
MATRICE_FILE = ROOT / "agents" / "donnees" / "matrice-electricite-electronique-v2.csv"

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


def normaliser(texte: str) -> str:
    """Forme comparable d'un terme : minuscules, sans accents, ponctuation et
    espaces réduits à une espace simple. « Loi d'Ohm », « loi d ohm » et
    « LOI D’OHM » donnent la même forme. Sert au rapprochement avec la matrice
    curriculaire, au lexique attendu et au contrôle d'ambiguïté des synonymes."""
    s = texte.lower()
    for lig, rempl in LIGATURES.items():
        s = s.replace(lig, rempl)
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return " ".join(re.sub(r"[^a-z0-9]+", " ", s).split())


def formes_d_une_fiche(fiche: dict) -> set[str]:
    """Toutes les façons de nommer une fiche : son terme et ses synonymes."""
    formes = {normaliser(fiche.get("term", ""))}
    formes.update(normaliser(x) for x in fiche.get("synonymes") or [])
    return {f for f in formes if f}


def load_json(path: Path):
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def dump_json(path: Path, data) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def load_wiki() -> dict[str, dict]:
    return {p.stem: load_json(p) for p in sorted(WIKI_DIR.glob("*.json"))}


def load_taxonomy() -> dict[str, str]:
    return load_json(TAXONOMY_FILE)


def load_couverture() -> dict:
    """Objectifs de couverture (planchers par domaine). Absent = aucun objectif."""
    return load_json(COUVERTURE_FILE) if COUVERTURE_FILE.exists() else {}


def load_lexique() -> dict:
    """Lexique de référence attendu : ce que le glossaire DEVRAIT contenir."""
    return load_json(LEXIQUE_FILE) if LEXIQUE_FILE.exists() else {}


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


# --- Chaîne de production (lots, missions, rapports) ---------------------------------
AGENTS_DIR = ROOT / "agents"
CHANGESETS_DIR = AGENTS_DIR / "changesets"
MISSIONS_DIR = AGENTS_DIR / "missions"
RAPPORTS_DIR = AGENTS_DIR / "rapports"

# Valeur à remplacer dans un brouillon de changeset (refusée par apply_changeset.py).
A_REMPLIR = "__A_REMPLIR__"


def contient_a_remplir(valeur) -> bool:
    """Vrai si la valeur (ou l'un de ses éléments, à toute profondeur) vaut A_REMPLIR."""
    if isinstance(valeur, str):
        return A_REMPLIR in valeur
    if isinstance(valeur, dict):
        return any(contient_a_remplir(v) for v in valeur.values())
    if isinstance(valeur, list):
        return any(contient_a_remplir(v) for v in valeur)
    return False


def _valeur_entete(brut: str):
    """Valeur d'une ligne d'en-tête : JSON si possible (listes, objets, nombres),
    sinon chaîne. Un commentaire « # … » en fin de ligne est ignoré."""
    brut = brut.strip()
    try:
        return json.loads(brut)
    except json.JSONDecodeError:
        pass
    # Commentaire final : on essaie chaque « # » précédé d'une espace, de la droite vers la gauche.
    positions = [m.start() for m in re.finditer(r"\s#", brut)]
    for pos in positions:
        avant = brut[:pos].strip()
        try:
            return json.loads(avant)
        except json.JSONDecodeError:
            continue
    if positions:
        brut = brut[:positions[0]].strip()
    return brut.strip('"')


def lire_entete(path: Path) -> dict | None:
    """En-tête « --- clé: valeur --- » d'un rapport ou d'une mission (stdlib seule, pas de YAML).

    Les valeurs complexes s'écrivent en JSON (clés entre guillemets) :
        lacunes: [{"terme": "Farad", "domaine": "A", "vu_dans": "condensateur"}]
    Renvoie None si le fichier n'a pas d'en-tête (anciens rapports)."""
    texte = path.read_text(encoding="utf-8")
    if not texte.startswith("---"):
        return None
    fin = texte.find("\n---", 3)
    if fin < 0:
        return None
    entete = {}
    for ligne in texte[3:fin].splitlines():
        if not ligne.strip() or ligne.lstrip().startswith("#") or ":" not in ligne:
            continue
        cle, brut = ligne.split(":", 1)
        entete[cle.strip()] = _valeur_entete(brut)
    return entete


def lire_changeset(path: Path) -> list[dict]:
    """Opérations d'un changeset JSONL (lignes vides ignorées)."""
    return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]


def ecrire_changeset(path: Path, ops: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(o, ensure_ascii=False) + "\n" for o in ops), encoding="utf-8")


def slugs_du_changeset(ops: list[dict]) -> list[str]:
    """Fiches traitées par un changeset (« set » et « create »), dans l'ordre, sans les
    fiches seulement touchées par un lien."""
    slugs: list[str] = []
    for o in ops:
        if o.get("op") == "set":
            s = o.get("slug")
        elif o.get("op") == "create":
            s = slugify((o.get("data") or {}).get("term", ""))
        else:
            continue
        if s and s not in slugs:
            slugs.append(s)
    return slugs
