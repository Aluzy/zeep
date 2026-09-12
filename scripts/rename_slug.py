#!/usr/bin/env python3
"""Renomme une fiche wiki et met à jour toutes les références à son slug.

    python3 scripts/rename_slug.py <ancien-slug> [--term "Nouveau terme"] [--dry-run]

Le nouveau slug est calculé par zeeplib.slugify(nouveau terme, ou terme actuel
si --term est absent). Le script :
  - renomme src/content/wiki/<ancien>.json en <nouveau>.json (git mv si le
    fichier est suivi par Git, sinon os.rename) et met à jour "slug" (et "term") ;
  - remplace l'ancien slug dans "related" de toutes les fiches wiki (l'ordre
    alphabétique est conservé s'il était respecté) ;
  - remplace l'ancien slug dans le frontmatter "related" des articles
    src/content/blog/*.md (tableau JSON sur une ligne ; le reste du fichier
    est préservé à l'identique) ;
  - remplace l'ancien slug dans "related" des projets src/content/diy/*.json
    (remplacement ciblé : la mise en forme du fichier est préservée).

Toutes les modifications sont calculées avant la première écriture : en cas
d'erreur (fiche absente, slug cible déjà pris, format non géré), rien n'est
modifié. Renommer une fiche casse son URL publique : ne le faire que si la
mission le demande (voir AGENTS.md).

Codes de sortie : 0 succès (ou rien à faire), 1 erreur, 2 arguments invalides.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

from zeeplib import (BLOG_DIR, DIY_DIR, ROOT, SLUG_RE, WIKI_DIR, dump_json,
                     load_wiki, slugify)


class RenameError(Exception):
    pass


def replace_in_list(items: list, old: str, new: str) -> list:
    return [new if x == old else x for x in items]


def replace_in_json_array(text: str, key: str, old: str, new: str) -> str:
    """Remplace "old" par "new" uniquement à l'intérieur du tableau `"key": [...]`
    (ou `key: [...]` pour un frontmatter). Retourne le texte modifié."""
    pattern = re.compile(r'((?<![\w-])"?' + re.escape(key) + r'"?\s*:\s*)\[([^\]]*)\]')
    token = re.compile(r'"' + re.escape(old) + r'"')

    def sub(m: re.Match) -> str:
        return m.group(1) + "[" + token.sub('"' + new + '"', m.group(2)) + "]"

    return pattern.sub(sub, text, count=1)


def plan_blog(path: Path, old: str, new: str) -> str | None:
    """Nouveau contenu de l'article, ou None s'il ne référence pas l'ancien slug."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        raise RenameError(f"blog/{path.name} : frontmatter non fermé")
    fm = text[:end]
    lines = fm.split("\n")
    idx = [i for i, line in enumerate(lines) if line.startswith("related:")]
    if not idx:
        return None
    i = idx[0]
    raw = lines[i].split(":", 1)[1].strip()
    try:
        related = json.loads(raw)
    except json.JSONDecodeError:
        # Liste YAML multiligne ou autre format : on refuse plutôt que d'oublier un lien.
        if old in raw or any(old in line for line in lines[i + 1:]):
            raise RenameError(f"blog/{path.name} : « related » n'est pas un tableau JSON sur une ligne (format non géré)")
        return None
    if not isinstance(related, list):
        raise RenameError(f"blog/{path.name} : « related » n'est pas un tableau")
    if old not in related:
        return None
    new_line = replace_in_json_array(lines[i], "related", old, new)
    check = json.loads(new_line.split(":", 1)[1].strip())
    if check != replace_in_list(related, old, new):
        raise RenameError(f"blog/{path.name} : remplacement ciblé impossible dans « related »")
    lines[i] = new_line
    return "\n".join(lines) + text[end:]


def plan_diy(path: Path, old: str, new: str) -> str | None:
    """Nouveau contenu du projet DIY, ou None s'il ne référence pas l'ancien slug."""
    text = path.read_text(encoding="utf-8")
    data = json.loads(text)
    related = data.get("related", [])
    if old not in related:
        return None
    expected = dict(data, related=replace_in_list(related, old, new))
    new_text = replace_in_json_array(text, "related", old, new)
    if json.loads(new_text) == expected:
        return new_text
    # Mise en forme inattendue : réécriture complète (contenu garanti identique).
    return json.dumps(expected, ensure_ascii=False, indent=2) + "\n"


def git_tracked(path: Path) -> bool:
    try:
        res = subprocess.run(["git", "-C", str(ROOT), "ls-files", "--error-unmatch", str(path)],
                             capture_output=True, text=True)
    except OSError:
        return False
    return res.returncode == 0


def show(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def move_file(src: Path, dst: Path) -> str:
    if git_tracked(src):
        res = subprocess.run(["git", "-C", str(ROOT), "mv", str(src), str(dst)], capture_output=True, text=True)
        if res.returncode == 0:
            return "git mv"
    os.rename(src, dst)
    return "os.rename"


def run(old: str, new_term: str | None, dry_run: bool) -> int:
    wiki = load_wiki()
    if old not in wiki:
        raise RenameError(f"fiche inexistante : src/content/wiki/{old}.json")
    entry = wiki[old]
    term = new_term if new_term is not None else entry.get("term", "")
    if new_term is not None and not new_term.strip():
        raise RenameError("--term ne peut pas être vide")
    new = slugify(term)
    if not SLUG_RE.match(new):
        raise RenameError(f"slug calculé invalide « {new} » pour le terme « {term} »")
    term_changed = new_term is not None and new_term != entry.get("term")

    if new == old and not term_changed:
        print(f"Rien à faire : « {old} » est déjà le slug de « {term} ».")
        return 0
    if new != old and (new in wiki or (WIKI_DIR / f"{new}.json").exists()):
        raise RenameError(f"le slug cible existe déjà : src/content/wiki/{new}.json")
    if term_changed:
        others = {d.get("term", "").strip().lower(): s for s, d in wiki.items() if s != old}
        if term.strip().lower() in others:
            raise RenameError(f"le terme « {term} » est déjà utilisé par la fiche « {others[term.strip().lower()]} »")

    # 1. Calcul de toutes les modifications (aucune écriture).
    entry_new = dict(entry)
    entry_new["slug"] = new
    if term_changed:
        entry_new["term"] = term
    wiki_updates: dict[str, dict] = {}
    if new != old:
        for slug, d in wiki.items():
            if slug == old:
                continue
            links = d.get("related", [])
            if old in links:
                was_sorted = links == sorted(links)
                rel2 = replace_in_list(links, old, new)
                wiki_updates[slug] = dict(d, related=sorted(rel2) if was_sorted else rel2)
    blog_updates: dict[Path, str] = {}
    diy_updates: dict[Path, str] = {}
    if new != old:
        for path in sorted(BLOG_DIR.glob("*.md")):
            content = plan_blog(path, old, new)
            if content is not None:
                blog_updates[path] = content
        for path in sorted(DIY_DIR.glob("*.json")):
            content = plan_diy(path, old, new)
            if content is not None:
                diy_updates[path] = content

    # 2. Compte rendu.
    prefix = "[dry-run] " if dry_run else ""
    if new != old:
        print(f"{prefix}fiche     {old} -> {new}" + (f" (terme : « {entry.get('term')} » -> « {term} »)" if term_changed else ""))
    else:
        print(f"{prefix}fiche     {old} : terme « {entry.get('term')} » -> « {term} » (slug inchangé)")
    for slug in sorted(wiki_updates):
        print(f"{prefix}wiki      src/content/wiki/{slug}.json (related)")
    for path in blog_updates:
        print(f"{prefix}blog      {show(path)} (related)")
    for path in diy_updates:
        print(f"{prefix}diy       {show(path)} (related)")
    total = 1 + len(wiki_updates) + len(blog_updates) + len(diy_updates)
    if dry_run:
        print(f"{prefix}{total} fichier(s) seraient modifiés ; rien n'a été écrit.")
        return 0

    # 3. Écriture.
    src, dst = WIKI_DIR / f"{old}.json", WIKI_DIR / f"{new}.json"
    if new != old:
        how = move_file(src, dst)
        print(f"renommage {show(src)} -> {show(dst)} ({how})")
    dump_json(dst, entry_new)
    for slug, d in wiki_updates.items():
        dump_json(WIKI_DIR / f"{slug}.json", d)
    for path, content in {**blog_updates, **diy_updates}.items():
        path.write_text(content, encoding="utf-8")
    print(f"{total} fichier(s) modifié(s). Lancer ensuite : python3 scripts/validate_content.py")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Renomme une fiche wiki et met à jour les références.")
    parser.add_argument("old_slug", help="slug actuel de la fiche (nom du fichier sans .json)")
    parser.add_argument("--term", help="nouveau terme (le slug est recalculé à partir de lui)")
    parser.add_argument("--dry-run", action="store_true", help="affiche les modifications sans rien écrire")
    args = parser.parse_args()
    try:
        return run(args.old_slug, args.term, args.dry_run)
    except RenameError as e:
        print(f"ERREUR  {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
