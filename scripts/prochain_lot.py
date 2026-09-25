#!/usr/bin/env python3
"""Chaîne de production du contenu : backlog unifié -> mission du rédacteur -> mission du contrôleur.

    python3 scripts/prochain_lot.py                                   # taille de chaque file du backlog
    python3 scripts/prochain_lot.py --lot J4-L1                       # lot suivant (première file non vide)
    python3 scripts/prochain_lot.py --lot J4-L2 --file securite --taille 20
    python3 scripts/prochain_lot.py --lot J4-L4 --file reecriture --domaine A
    python3 scripts/prochain_lot.py --controle J4-L1                  # mission du contrôleur (changeset rempli)

Rédaction (--lot) : écrit
  - agents/missions/<LOT>.md          pour chaque fiche : contenu actuel, règles enfreintes,
                                       fiches voisines, articles qui la citent ; consignes du lot ;
  - agents/changesets/<LOT>.jsonl     BROUILLON : une opération par champ à reprendre, avec
                                       « old » déjà recopié à l'identique et « new » / « why »
                                       valant "__A_REMPLIR__" (apply_changeset.py refuse le
                                       fichier tant qu'il en reste un).
Pour la file « niveaux », seul la mission est écrite : le travail porte sur la TABLE de
agents/outils/mapping_niveau.py, qui écrit ensuite le changeset (--lot).

Contrôle (--controle) : le changeset du rédacteur doit être rempli. Écrit
  - agents/missions/<LOT>-controle.md   avant / après par fiche, règles encore enfreintes,
                                         grille des 12 critères, format de sortie ;
  - agents/changesets/<LOT>-controle.jsonl  BROUILLON : une opération « relecture » par fiche.
    Le contrôleur remplace "__A_REMPLIR__" par {"date": …, "par": "agent-controleur-<LOT>",
    "statut": "relu-ia"} pour une fiche conforme, et SUPPRIME la ligne d'une fiche refusée.

Le contrôleur est un autre agent que le rédacteur, lancé sans le contexte de la rédaction :
sa mission ne contient pas les justifications (« why ») du rédacteur, il vérifie lui-même.

Une fiche d'une mission de rédaction pas encore intégrée (sans rapport, ou changeset pas encore
appliqué au wiki) est considérée « en cours » : elle n'est pas reproposée à un autre lot.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

import backlog
import dette
from apply_changeset import ChangesetError, avant_apres
from zeeplib import (A_REMPLIR, BLOG_DIR, CHANGESETS_DIR, MISSIONS_DIR, ROOT, contient_a_remplir,
                     ecrire_changeset, lire_changeset, load_taxonomy, load_wiki, read_frontmatter,
                     slugs_du_changeset)

TAILLE_DEFAUT = 20
NIVEAUX_AVANT_LYCEE = dette.NIVEAUX_AVANT_LYCEE
VOISINES_MAX = 8


def rel(p: Path) -> str:
    return str(p.relative_to(ROOT))


def mots(texte) -> int:
    return dette.mots(texte if isinstance(texte, str) else None)


def citations_blog() -> dict[str, list[str]]:
    """Slug de fiche -> titres des articles de blog qui la citent."""
    cites: dict[str, list[str]] = {}
    for chemin in sorted(BLOG_DIR.glob("*.md")):
        fm, _ = read_frontmatter(chemin)
        for slug in fm.get("related") or []:
            cites.setdefault(slug, []).append(f"{fm.get('title', chemin.stem)} (`{chemin.stem}`)")
    return cites


def entete(champs: dict) -> str:
    lignes = ["---"]
    for cle, val in champs.items():
        lignes.append(f"{cle}: {json.dumps(val, ensure_ascii=False) if not isinstance(val, str) else val}")
    lignes.append("---")
    return "\n".join(lignes)


def citer(texte: str | None) -> str:
    if not texte:
        return "_(vide)_"
    return "\n".join("> " + l for l in str(texte).splitlines())


def lister_sources(sources) -> str:
    if not sources:
        return "_(aucune)_"
    out = []
    for s in sources:
        url = s.get("url") or ""
        titre = s.get("titre") or "(sans titre)"
        lien = f"[{titre}]({url})" if url else f"{titre} — **sans URL**"
        out.append(f"- {lien} — type `{s.get('type')}`")
    return "\n".join(out)


def niveau_texte(fiche: dict) -> str:
    n = fiche.get("niveau") or {}
    if not n:
        return "aucun"
    return f"{n.get('premiereApparition')} (cycles {', '.join(n.get('cycles', []))})"


def avant_lycee(fiche: dict) -> bool:
    return (fiche.get("niveau") or {}).get("premiereApparition") in NIVEAUX_AVANT_LYCEE


# --------------------------------------------------------------------------- rédaction
def ops_brouillon(lot: str, item: dict, fiche: dict) -> list[dict]:
    """Opérations « set » à reprendre pour une passe complète sur la fiche."""
    regles = set(item["regles"])
    champs = []
    if regles & {"definition_longueur", "definition_html", "securite_230v_absente"} \
            or any(m.startswith("Signalement") for m in item["motifs"]):
        champs.append("definition")
    if (avant_lycee(fiche) and not fiche.get("versionSimple")) or "version_simple_longueur" in regles:
        champs.append("versionSimple")
    if not fiche.get("sources") or regles & {"source_url_racine", "source_type_hors_liste", "source_sans_url"}:
        champs.append("sources")
    if not fiche.get("synonymes"):
        champs.append("synonymes")
    return [{"op": "set", "lot": lot, "slug": item["slug"], "field": champ,
             "old": fiche.get(champ), "new": A_REMPLIR, "why": A_REMPLIR} for champ in champs]


def op_creation(lot: str, item: dict) -> dict:
    return {"op": "create", "lot": lot, "data": {
        "term": item["terme"],
        "domains": [item["domaine"]] if item["domaine"] != "?" else [A_REMPLIR],
        "definition": A_REMPLIR,
        "versionSimple": f"{A_REMPLIR} (ou null si la notion n'est pas vue avant le lycée)",
        "synonymes": A_REMPLIR, "related": A_REMPLIR, "sources": A_REMPLIR,
    }, "_slugPrevu": item["slugPrevu"], "why": A_REMPLIR}


CONSIGNES_REDACTION = """\
## Consignes (à lire avant la première fiche)

Tu es le **rédacteur** du lot {lot}. Règles complètes : `AGENTS.md` §3 et `docs/grille-relecture.md`.

1. **Une fiche = une passe complète.** Pour chaque fiche, reprends tous les champs du brouillon
   `{changeset}` : définition, version simple, sources, synonymes. Remplace chaque
   `"__A_REMPLIR__"` (dans `new` **et** dans `why`). Ne touche jamais à `old` : il est recopié à
   l'identique et protège contre les modifications concurrentes.
2. Un champ déjà conforme que tu ne modifies pas : **supprime sa ligne** et dis-le dans le rapport.
   Un champ absent du brouillon que tu dois reprendre : ajoute une ligne `set` en recopiant `old`
   depuis la fiche (valeur exacte, `null` si le champ est absent).
3. **Définition** : 1 à 3 phrases, 25 à 60 mots, texte brut, sans circularité ; tout terme technique
   a sa fiche et un lien (`{{"op": "link", "a": …, "b": …, "why": …}}`) — sinon l'expliquer ou le retirer.
   Vocabulaire officiel : « tension », « intensité » ; ne pas confondre électricité et énergie,
   courant et tension, puissance et énergie.
4. **Version simple** (obligatoire pour les notions vues avant le lycée) : 1 à 2 phrases, 12 à 35 mots,
   vocabulaire d'un élève de 8-11 ans, un exemple du quotidien, aucune formule. Toujours exacte.
5. **Sécurité** : toute fiche liée au secteur 230 V dit qu'on n'y intervient pas soi-même
   (formules reconnues : `src/data/dette.json`, clé `securite230V.formulesRappel`).
6. **Sources** : au moins une, `{{"titre", "url", "type"}}` avec `type` ∈ programme | reference | norme | manuel.
   URL **précise** (le document, jamais une page d'accueil) ; pour Electropedia, l'entrée IEC 60050 avec
   son numéro IEV. **Ouvre chaque URL** avant de la citer et note-la dans le rapport
   (« Sources réellement ouvertes »). Jamais Wikipédia comme source unique. Si tu ne peux pas ouvrir
   de source pour une fiche, **retire la fiche du lot** (supprime ses lignes) et signale-la.
7. **Synonymes** : abréviations, symboles, variantes (`PWM`, `LDR`, `kWh`) ; jamais le terme d'une autre fiche.
8. **Doute scientifique** : ne pas écrire ; garder l'ancien texte, supprimer la ligne, signaler au rapport.
9. Tu ne poses **jamais** de `relecture` : c'est le rôle du contrôleur (un autre agent).

## Avant de rendre

```bash
python3 scripts/apply_changeset.py {changeset} --dry-run      # doit passer (aucun __A_REMPLIR__)
cp -r . /tmp/zeep-essai && cd /tmp/zeep-essai                   # copie de travail
python3 scripts/apply_changeset.py {changeset}
python3 scripts/validate_content.py                             # 0 erreur
python3 scripts/audit_couverture.py --ci                        # code de sortie 0
python3 scripts/dette.py --indicateurs                          # colonne « Après » du rapport
```

Puis écris `agents/rapports/{lot}.md` d'après `agents/rapports/TEMPLATE.md` (en-tête compris,
valeurs complexes en JSON), et lance `python3 scripts/prochain_lot.py --controle {lot}` pour
préparer la mission du contrôleur. Commits : `{lot}: …`.
"""


def mission_redaction(lot: str, nom_file: str, items: list[dict], wiki: dict, ops: list[dict],
                      changeset: Path | None) -> str:
    taxo = load_taxonomy()
    cites = citations_blog()
    date = dt.date.today().isoformat()
    tete = entete({
        "lot": lot, "role": "redaction", "file": nom_file, "date": date,
        "changeset": rel(changeset) if changeset else "aucun (mapping_niveau.py --lot)",
        "elements": [x["cle"] for x in items],
    })
    parties = [tete, "", f"# Mission {lot} — {backlog.FILES[nom_file]}", "",
               f"Générée par `scripts/prochain_lot.py` le {date} : {len(items)} élément(s) de la file "
               f"« {nom_file} »" + (f", {len(ops)} opération(s) à remplir dans `{rel(changeset)}`." if changeset else "."),
               ""]
    if nom_file == "niveaux":
        parties += [CONSIGNES_NIVEAUX.format(lot=lot), ""]
    elif changeset:
        parties += [CONSIGNES_REDACTION.format(lot=lot, changeset=rel(changeset)), ""]
    parties += ["## Éléments du lot", ""]
    for i, item in enumerate(items, 1):
        if item["slug"] and item["slug"] in wiki and nom_file != "niveaux":
            parties.append(bloc_fiche(i, item, wiki, taxo, cites, ops))
        elif nom_file == "niveaux":
            parties.append(bloc_niveau(i, item, wiki))
        else:
            parties.append(bloc_creation(i, item, wiki, taxo))
    return "\n".join(parties).rstrip() + "\n"


def bloc_fiche(i: int, item: dict, wiki: dict, taxo: dict, cites: dict, ops: list[dict]) -> str:
    f = wiki[item["slug"]]
    champs = [o["field"] for o in ops if o.get("slug") == item["slug"]]
    voisines = []
    for r in (f.get("related") or [])[:VOISINES_MAX]:
        v = wiki.get(r, {})
        voisines.append(f"- **{v.get('term', r)}** (`{r}`) : {v.get('definition', '')}")
    reste = len(f.get("related") or []) - VOISINES_MAX
    if reste > 0:
        voisines.append(f"- … et {reste} autre(s) : " + ", ".join(f"`{r}`" for r in f["related"][VOISINES_MAX:]))
    domaines = ", ".join(f"{d} ({taxo.get(d, '?')})" for d in f.get("domains", []))
    return "\n".join([
        f"### {i}. {f.get('term')} — `{item['slug']}`",
        "",
        f"- Domaines : {domaines}",
        f"- Niveau scolaire : {niveau_texte(f)}" + (" — **version simple obligatoire**" if avant_lycee(f) else ""),
        f"- À reprendre : " + (", ".join(f"`{c}`" for c in champs) or "_(rien dans le brouillon)_"),
        "- Règles enfreintes :",
        *[f"  - {m}" for m in item["motifs"]],
        "",
        f"**Définition actuelle** ({mots(f.get('definition'))} mots) :",
        citer(f.get("definition")),
        "",
        f"**Version simple actuelle** ({mots(f.get('versionSimple'))} mots) :",
        citer(f.get("versionSimple")),
        "",
        f"**Synonymes** : {', '.join(f.get('synonymes') or []) or '_(aucun)_'}",
        "",
        "**Sources actuelles** :",
        lister_sources(f.get("sources")),
        "",
        "**Fiches liées** (vérifier que chaque terme technique employé y figure) :",
        *(voisines or ["_(aucune)_"]),
        "",
        "**Cité par les articles** : " + ("; ".join(cites.get(item["slug"], [])) or "_(aucun)_"),
        "",
    ])


def bloc_creation(i: int, item: dict, wiki: dict, taxo: dict) -> str:
    dom = item["domaine"]
    proches = [s for s, f in wiki.items() if dom in f.get("domains", [])][:12] if dom != "?" else []
    return "\n".join([
        f"### {i}. Créer « {item['terme']} » — slug prévu `{item['slugPrevu']}`",
        "",
        f"- Domaine : {dom} ({taxo.get(dom, 'à choisir dans src/data/taxonomy.json')})",
        *[f"- {m}" for m in item["motifs"]],
        "- Fiches du même domaine (candidates pour `related`) : "
        + (", ".join(f"`{s}`" for s in proches) or "_(à chercher)_"),
        "",
    ])


CONSIGNES_NIVEAUX = """\
## Consignes

Ce lot ne modifie aucune fiche à la main. Pour chaque entrée ci-dessous, la TABLE de
`agents/outils/mapping_niveau.py` rejette un terme de programme alors qu'une fiche le couvre
désormais.

1. Remplace le rejet par un rattachement (`direct`, `variante`, `compose` ou `sens`, avec sa
   confiance et une note qui le justifie) — ou garde le rejet en expliquant dans la note pourquoi
   la fiche ne correspond pas (dans ce cas, la marquer `backlog=False` si elle ne mérite pas de fiche).
2. `python3 agents/outils/mapping_niveau.py --verifier` doit passer.
3. `python3 agents/outils/mapping_niveau.py --lot {lot}` écrit `agents/changesets/{lot}.jsonl`
   (niveaux manquants seulement ; un niveau existant n'est jamais écrasé : les écarts sont affichés).
4. Tranche chaque écart signalé dans le rapport (décision humaine si le niveau change).
5. Rapport `agents/rapports/{lot}.md` d'après `TEMPLATE.md`. Le lot touche du code : pas de
   contrôle de fiche, mais la TABLE est relue par un autre agent (section « Relecture »).
"""


def bloc_niveau(i: int, item: dict, wiki: dict) -> str:
    f = wiki.get(item["slug"], {})
    return "\n".join([
        f"### {i}. « {item['terme']} » -> `{item['slug']}`",
        "",
        *[f"- {m}" for m in item["motifs"]],
        f"- Niveau actuel de la fiche : {niveau_texte(f)}",
        f"- Définition : {f.get('definition', '')}",
        "",
    ])


def generer_lot(args, wiki: dict) -> int:
    lot = args.lot
    mission = MISSIONS_DIR / f"{lot}.md"
    changeset = CHANGESETS_DIR / f"{lot}.jsonl"
    for chemin in (mission, changeset):
        if chemin.exists():
            print(f"{rel(chemin)} existe déjà : choisir un autre nom de lot.")
            return 1
    files = backlog.construire(wiki)
    nom = args.file or next((n for n, v in files.items() if v), None)
    if nom is None:
        print("Backlog vide : rien à produire.")
        return 0
    if nom not in files:
        print("Files connues : " + ", ".join(files))
        return 1
    items = files[nom]
    if args.domaine:
        items = [x for x in items if x["domaine"] == args.domaine]
    items = items[: args.taille]
    if not items:
        print(f"File « {nom} » vide" + (f" pour le domaine {args.domaine}" if args.domaine else "") + ".")
        return 1

    ops: list[dict] = []
    if backlog.NATURE[nom] == "fiche":
        for item in items:
            ops += ops_brouillon(lot, item, wiki[item["slug"]])
    elif backlog.NATURE[nom] == "creation":
        ops = [op_creation(lot, item) for item in items]
    if ops:
        ecrire_changeset(changeset, ops)
    MISSIONS_DIR.mkdir(parents=True, exist_ok=True)
    mission.write_text(mission_redaction(lot, nom, items, wiki, ops, changeset if ops else None),
                       encoding="utf-8")
    print(f"File « {nom} » : {len(items)} élément(s).")
    print(f"  {rel(mission)}")
    if ops:
        print(f"  {rel(changeset)} (brouillon, {len(ops)} opération(s) à remplir)")
    return 0


# ---------------------------------------------------------------------------- contrôle
GRILLE = [
    "exactitude scientifique", "pas de circularité", "vocabulaire officiel", "grandeurs non confondues",
    "format 25-60 mots, texte brut", "jargon relié (fiche + lien)", "sécurité 230 V",
    "sources ouvertes et précises", "version simple (8-11 ans, exemple, exacte)",
    "cohérence avec le niveau", "unités et symboles", "ton neutre, texte original",
]

CONSIGNES_CONTROLE = """\
## Consignes du contrôleur

Tu es le **contrôleur** du lot {lot}. Tu n'as pas participé à la rédaction et tu ne la vois qu'à
travers ce document : les justifications du rédacteur sont volontairement absentes. Tu vérifies
chaque fiche contre les **12 critères** de `docs/grille-relecture.md` (lis-la en entier d'abord).

1. **Ouvre chaque URL de source** et vérifie qu'elle appuie la définition. Une source que tu ne
   peux pas ouvrir, imprécise (page d'accueil) ou qui n'appuie pas l'affirmation = critère 8 en échec.
2. Une fiche est **conforme** si les 12 critères passent. Dans `{changeset}`, remplace alors
   `"__A_REMPLIR__"` de `new` par
   `{{"date": "{date}", "par": "agent-controleur-{lot}", "statut": "relu-ia"}}` et `why` par
   « Relue selon la grille (12 critères) ».
3. Une fiche **refusée** : supprime sa ligne dans `{changeset}`, et note les critères en échec. Tu ne
   réécris pas la fiche : le rédacteur la corrige (nouvelle passe de contrôle) ou la retire du lot.
   Si le défaut porte sur une fiche hors lot, ajoute-la à `agents/donnees/signalements.json`.
4. Écris tes verdicts dans la section « Relecture (rempli par le contrôleur) » de
   `agents/rapports/{lot}.md`, une ligne par fiche : critères en échec, décision.
5. Vérifie : `python3 scripts/apply_changeset.py agents/changesets/{lot}.jsonl {changeset} --dry-run`.
   Tu ne poses **jamais** `"statut": "valide"` (réservé à Alexandre).
"""


def generer_controle(lot: str, wiki: dict) -> int:
    source = CHANGESETS_DIR / f"{lot}.jsonl"
    brouillon = CHANGESETS_DIR / f"{lot}-controle.jsonl"
    if not source.exists():
        print(f"{rel(source)} introuvable.")
        return 1
    # Passes successives : une fiche refusée (ligne supprimée du brouillon) puis corrigée par
    # le rédacteur repasse au contrôle ; les verdicts déjà rendus sont conservés.
    passe = len(list(MISSIONS_DIR.glob(f"{lot}-controle*.md"))) + 1
    mission = MISSIONS_DIR / (f"{lot}-controle.md" if passe == 1 else f"{lot}-controle-{passe}.md")
    existants = lire_changeset(brouillon) if brouillon.exists() else []
    if any(contient_a_remplir(o) for o in existants):
        print(f"{rel(brouillon)} contient encore des « {A_REMPLIR} » : la passe de contrôle précédente n'est pas finie.")
        return 1
    ops = lire_changeset(source)
    if any(contient_a_remplir(o) for o in ops):
        print(f"{rel(source)} contient encore des « {A_REMPLIR} » : la rédaction n'est pas finie.")
        return 1
    if any(o.get("op") == "set" and o.get("field") == "relecture" for o in ops) \
            or any("relecture" in (o.get("data") or {}) for o in ops if o.get("op") == "create"):
        print("Le changeset du rédacteur pose une « relecture » : interdit (AGENTS.md §3). Retirer ces lignes.")
        return 1
    try:
        avant, apres, deja = avant_apres(ops, wiki)
    except ChangesetError as e:
        print(f"{rel(source)} ne s'applique pas : {e}")
        return 1

    decidees = {o.get("slug") for o in existants}
    slugs = [s for s in slugs_du_changeset(ops) if s not in decidees]
    if not slugs:
        print(f"Toutes les fiches du lot {lot} ont déjà un verdict dans {rel(brouillon)}.")
        return 0
    defauts_apres = dette.defauts({s: apres[s] for s in slugs})
    date = dt.date.today().isoformat()

    releve = existants + [{"op": "set", "lot": lot, "slug": s, "field": "relecture", "old": apres[s].get("relecture"),
               "new": A_REMPLIR, "why": A_REMPLIR} for s in slugs]
    parties = [entete({"lot": lot, "role": "controle", "date": date, "changeset": rel(source),
                       "elements": slugs}), "",
               f"# Contrôle du lot {lot}" + (f" — passe {passe}" if passe > 1 else ""), "",
               f"{len(slugs)} fiche(s), {len(ops)} opération(s) du rédacteur"
               + (" (changeset déjà appliqué au dépôt)." if deja else " (changeset non encore appliqué)."), "",
               CONSIGNES_CONTROLE.format(lot=lot, changeset=rel(brouillon), date=date), "",
               "## Fiches à contrôler", ""]
    for i, s in enumerate(slugs, 1):
        a, b = avant.get(s), apres[s]
        restantes = [dette.REGLES[r] for r in dette.REGLES if s in defauts_apres[r]]
        parties += [f"### {i}. {b.get('term')} — `{s}`" + (" (création)" if a is None else ""), "",
                    f"- Niveau scolaire : {niveau_texte(b)}"
                    + (" — version simple obligatoire" if avant_lycee(b) else ""),
                    "- Règles automatiques encore enfreintes : "
                    + ("; ".join(f"⚠ {r}" for r in restantes) if restantes else "aucune"), ""]
        for champ in ("definition", "versionSimple", "synonymes"):
            va, vb = (a or {}).get(champ), b.get(champ)
            if (a is not None and va == vb) or (not va and not vb):
                continue
            if champ == "synonymes":
                parties += [f"**Synonymes** : {', '.join(va or []) or '—'} → **{', '.join(vb or []) or '—'}**", ""]
                continue
            nom = "Définition" if champ == "definition" else "Version simple"
            if a is not None:
                parties += [f"**{nom} — avant** ({mots(va)} mots) :", citer(va), ""]
            parties += [f"**{nom} — après** ({mots(vb)} mots) :", citer(vb), ""]
        parties += ["**Sources après** (à ouvrir une par une) :", lister_sources(b.get("sources")), ""]
        nouveaux_liens = sorted(set(b.get("related") or []) - set((a or {}).get("related") or []))
        parties += ["**Fiches liées après** : " + ", ".join(
            f"`{r}`" + (" (nouveau)" if r in nouveaux_liens else "") for r in b.get("related") or []), ""]
        parties += ["```", f"fiche : {s}"]
        for k in range(6):
            g, d = GRILLE[k], GRILLE[k + 6]
            parties.append(f"{k + 1:>2} {g:<32}[ ]   {k + 7:>2} {d:<44}[ ]")
        parties += ["décision : conforme / refusée (n° des critères)", "```", ""]

    ecrire_changeset(brouillon, releve)
    mission.write_text("\n".join(parties).rstrip() + "\n", encoding="utf-8")
    print(f"  {rel(mission)}")
    print(f"  {rel(brouillon)} (brouillon, {len(releve) - len(existants)} relecture(s) à décider)")
    print("À confier à un AUTRE agent, sans le contexte de la rédaction.")
    return 0


# ------------------------------------------------------------------------------- main
def afficher_files(wiki: dict) -> int:
    files = backlog.construire(wiki)
    pris = backlog.lots_en_cours()
    print(f"{'File':16} {'Éléments':>8}  Libellé")
    for nom, items in files.items():
        print(f"{nom:16} {len(items):>8}  {backlog.FILES[nom]}")
    if pris:
        lots = sorted(set(pris.values()))
        print(f"\nEn cours (lots non intégrés au wiki) : {len(pris)} élément(s) dans {', '.join(lots)}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--lot", help="nom du lot de rédaction à générer (ex. J4-L1)")
    ap.add_argument("--file", choices=list(backlog.FILES), help="file du backlog (défaut : première non vide)")
    ap.add_argument("--taille", type=int, default=TAILLE_DEFAUT, help=f"éléments par lot (défaut {TAILLE_DEFAUT})")
    ap.add_argument("--domaine", help="limiter la file à un domaine de la taxonomie (ex. A)")
    ap.add_argument("--controle", metavar="LOT", help="génère la mission du contrôleur pour ce lot")
    args = ap.parse_args()
    wiki = load_wiki()
    if args.controle:
        return generer_controle(args.controle, wiki)
    if args.lot:
        return generer_lot(args, wiki)
    return afficher_files(wiki)


if __name__ == "__main__":
    sys.exit(main())
