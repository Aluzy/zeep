#!/usr/bin/env python3
"""Applique un changeset de contenu wiki (format JSONL) de façon déterministe.

Les agents de contenu ne modifient JAMAIS les fiches JSON à la main : ils
écrivent un changeset dans agents/changesets/, puis l'intégrateur l'applique.
Plusieurs agents peuvent ainsi travailler en parallèle sur les mêmes fiches
sans conflit Git, et chaque modification garde sa justification.

    python3 scripts/apply_changeset.py agents/changesets/J1-L3.jsonl --dry-run
    python3 scripts/apply_changeset.py agents/changesets/J1-L3.jsonl

Une opération par ligne (objet JSON). Champs communs : "op", "lot", "why".

  {"op":"set","slug":"voltage","field":"definition","old":"<valeur actuelle>","new":"...","why":"...","sources":[...]}
      Remplace un champ. "old" doit être identique à la valeur actuelle
      (protection contre les modifications concurrentes). Champs autorisés :
      definition, versionSimple, domains, pillar, niveau, sources, relecture,
      synonymes. Pour un champ encore absent de la fiche, "old" vaut null.

  {"op":"create","data":{"term":"Loi d'Ohm","domains":["A"],"definition":"...","related":["tension-electrique"], ...},"why":"..."}
      Crée une fiche. slug calculé depuis term ; les liens sont rendus réciproques.

  {"op":"link","a":"loi-dohm","b":"resistance-electrique","why":"..."}
  {"op":"unlink","a":"...","b":"...","why":"..."}

Renommer ou supprimer une fiche n'est pas autorisé par changeset (casse les URLs) :
à signaler dans le rapport de lot pour décision humaine.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from zeeplib import WIKI_DIR, dump_json, load_wiki, slugify

SETTABLE = {"definition", "versionSimple", "domains", "pillar", "niveau", "sources", "relecture", "synonymes"}
CREATE_DEFAULTS = {"sourceDomain": [], "merged": False, "pillar": False, "illustration": None,
                   "related": [], "synonymes": []}


class ChangesetError(Exception):
    pass


def add_link(wiki: dict, a: str, b: str) -> bool:
    if a == b:
        raise ChangesetError(f"lien d'une fiche vers elle-même : {a}")
    for x in (a, b):
        if x not in wiki:
            raise ChangesetError(f"fiche inexistante : {x}")
    changed = False
    for x, y in ((a, b), (b, a)):
        if y not in wiki[x]["related"]:
            wiki[x]["related"] = sorted(wiki[x]["related"] + [y])
            changed = True
    return changed


def apply(ops: list[dict], wiki: dict) -> tuple[set[str], list[str]]:
    touched: set[str] = set()
    log: list[str] = []
    for i, op in enumerate(ops, 1):
        kind = op.get("op")
        if not op.get("why"):
            raise ChangesetError(f"ligne {i} : justification « why » manquante")
        if kind == "set":
            slug, field = op.get("slug"), op.get("field")
            if slug not in wiki:
                raise ChangesetError(f"ligne {i} : fiche inexistante « {slug} »")
            if field not in SETTABLE:
                raise ChangesetError(f"ligne {i} : champ « {field} » non modifiable par changeset")
            current = wiki[slug].get(field)
            if "old" not in op:
                raise ChangesetError(f"ligne {i} : « old » manquant")
            if current != op["old"]:
                raise ChangesetError(f"ligne {i} : « old » ne correspond pas à la valeur actuelle de {slug}.{field}")
            wiki[slug][field] = op["new"]
            touched.add(slug)
            log.append(f"set     {slug}.{field}")
        elif kind == "create":
            data = dict(CREATE_DEFAULTS, **op.get("data", {}))
            if not data.get("term") or not data.get("definition") or not data.get("domains"):
                raise ChangesetError(f"ligne {i} : create exige term, definition et domains")
            slug = slugify(data["term"])
            if "slug" in data and data["slug"] != slug:
                raise ChangesetError(f"ligne {i} : slug « {data['slug']} » ≠ convention « {slug} »")
            if slug in wiki:
                raise ChangesetError(f"ligne {i} : la fiche « {slug} » existe déjà")
            related = data.pop("related")
            data["slug"] = slug
            data["related"] = []
            wiki[slug] = data
            for r in related:
                add_link(wiki, slug, r)
                touched.add(r)
            touched.add(slug)
            log.append(f"create  {slug} ({len(related)} liens)")
        elif kind == "link":
            if add_link(wiki, op.get("a"), op.get("b")):
                touched.update({op["a"], op["b"]})
            log.append(f"link    {op.get('a')} <-> {op.get('b')}")
        elif kind == "unlink":
            a, b = op.get("a"), op.get("b")
            for x, y in ((a, b), (b, a)):
                if x not in wiki:
                    raise ChangesetError(f"ligne {i} : fiche inexistante « {x} »")
                if y in wiki[x]["related"]:
                    wiki[x]["related"].remove(y)
                    touched.add(x)
            log.append(f"unlink  {a} <-> {b}")
        else:
            raise ChangesetError(f"ligne {i} : opération inconnue « {kind} »")
    return touched, log


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        return 2
    dry = "--dry-run" in sys.argv
    wiki = load_wiki()
    all_touched: set[str] = set()
    for path in args:
        ops = []
        for n, line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
            if line.strip():
                try:
                    ops.append(json.loads(line))
                except json.JSONDecodeError as e:
                    print(f"ERREUR {path}:{n} JSON invalide : {e}")
                    return 1
        try:
            touched, log = apply(ops, wiki)
        except ChangesetError as e:
            print(f"ERREUR {path} : {e}  — rien n'a été écrit.")
            return 1
        print(f"{path} : {len(ops)} opération(s), {len(touched)} fiche(s) touchée(s)")
        for entry in log:
            print(f"  {entry}")
        all_touched |= touched
    if dry:
        print("\n(dry-run : aucun fichier modifié)")
        return 0
    for slug in sorted(all_touched):
        dump_json(WIKI_DIR / f"{slug}.json", wiki[slug])
    print(f"\n{len(all_touched)} fichier(s) écrit(s). Lancer ensuite scripts/validate_content.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
