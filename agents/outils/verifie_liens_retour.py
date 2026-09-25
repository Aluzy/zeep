#!/usr/bin/env python3
"""Contrôle de l'index inverse des liens retour (lot J2-L5) — stdlib uniquement.

    python3 agents/outils/verifie_liens_retour.py [--json]

Le site affiche sur chaque fiche wiki les articles et projets qui la citent
(`src/lib/backlinks.ts`). Le build Astro n'étant pas lançable dans l'environnement
des agents (pas de `npm install`), ce script vérifie la logique sans Astro :

1. il reconstruit l'index inverse depuis `src/content/` (implémentation Python
   indépendante de celle du site) ;
2. il compare les attendus connus (par exemple : `carte-arduino` est citée par
   l'article Arduino/Raspberry/ESP32 **et** par le projet clignotant LED) ;
3. si Node sait retirer les types TypeScript (`--experimental-strip-types`,
   Node >= 22.6), il exécute le **vrai** `buildBacklinkIndex` de
   `src/lib/backlinks.ts` sur les mêmes données et exige un résultat identique ;
4. il vérifie que le garde-fou lève bien une erreur sur un slug de fiche inexistant.

Code de sortie : 0 si tout passe, 1 sinon.
"""
from __future__ import annotations

import json
import subprocess
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from zeeplib import BLOG_DIR, DIY_DIR, load_json, load_wiki, read_frontmatter  # noqa: E402

NODE_WRAPPER = Path(__file__).resolve().parent / "liens_retour_node.mjs"

# Témoins écrits à la main depuis src/content/ (3 articles, 3 projets au 12/09).
# Le contenu grandit à chaque lot de blog : un témoin exige que ces liens retour
# SOIENT présents (inclusion), il ne fige pas la liste complète. Les décomptes
# globaux et la liste des fiches « sans lien » figés au 12/09 ont été retirés le
# 25/09/2026 : ils cassaient dès le premier article publié.
ATTENDUS = {
    "carte-arduino": {
        "articles": ["arduino-vs-raspberry-vs-esp32"],
        "projets": ["clignotant-led-arduino"],
    },
    "objet-connecte-iot": {
        "articles": ["arduino-vs-raspberry-vs-esp32"],
        "projets": ["station-meteo-connectee"],
    },
    "facture-d-electricite": {
        "articles": ["comprendre-facture-electricite"],
        "projets": [],
    },
    "soudure-electronique": {
        "articles": [],
        "projets": ["pcb-personnalise-kicad"],
    },
}


def lire_articles() -> list[dict]:
    """Les entrées de la collection `blog` telles qu'Astro les fournit."""
    entrees = []
    for path in sorted(BLOG_DIR.glob("*.md")):
        fm, _ = read_frontmatter(path)
        entrees.append(
            {
                "slug": path.stem,  # Astro dérive le slug du nom de fichier
                "data": {"title": fm.get("title", ""), "related": fm.get("related") or []},
            }
        )
    return entrees


def lire_projets() -> list[dict]:
    """Les entrées de la collection `diy`."""
    entrees = []
    for path in sorted(DIY_DIR.glob("*.json")):
        d = load_json(path)
        entrees.append(
            {
                "data": {
                    "slug": d.get("slug", ""),
                    "title": d.get("title", ""),
                    "level": d.get("level", ""),
                    "duration": d.get("duration", ""),
                    "related": d.get("related") or [],
                }
            }
        )
    return entrees


def index_python(articles: list[dict], projets: list[dict], slugs_wiki: set[str]) -> dict:
    """Même contrat que buildBacklinkIndex : tri par titre, doublons ignorés,
    slug inconnu = erreur."""
    index: dict[str, dict] = {}

    def entree(slug: str) -> dict:
        return index.setdefault(slug, {"articles": [], "projets": []})

    for a in articles:
        vus: set[str] = set()
        for cible in a["data"]["related"]:
            if cible not in slugs_wiki:
                raise ValueError(
                    f"Fiche wiki introuvable « {cible} » référencée par l'article de blog {a['slug']}"
                )
            if cible in vus:
                continue
            # rang = position de la fiche parmi les cibles distinctes de l'article
            entree(cible)["articles"].append(
                {"slug": a["slug"], "titre": a["data"]["title"], "rang": len(vus)}
            )
            vus.add(cible)

    for p in projets:
        vus = set()
        for cible in p["data"]["related"]:
            if cible not in slugs_wiki:
                raise ValueError(
                    f"Fiche wiki introuvable « {cible} » référencée par le projet DIY {p['data']['slug']}"
                )
            if cible in vus:
                continue
            vus.add(cible)
            entree(cible)["projets"].append(
                {
                    "slug": p["data"]["slug"],
                    "titre": p["data"]["title"],
                    "niveau": p["data"]["level"],
                    "duree": (p["data"]["duration"] or "").strip(),
                }
            )

    for liens in index.values():
        # Approximation de localeCompare(…, "fr") : accents et casse ignorés,
        # puis la forme exacte pour départager.
        liens["articles"].sort(key=cle_titre)
        liens["projets"].sort(key=cle_titre)
    return index


def cle_titre(x: dict) -> tuple[str, str]:
    t = x["titre"]
    sans = "".join(c for c in unicodedata.normalize("NFKD", t) if not unicodedata.combining(c))
    return ("".join(c for c in sans.casefold() if c.isalnum() or c.isspace()), t)


def index_node(articles: list[dict], projets: list[dict], slugs_wiki: list[str]) -> dict | None:
    """Exécute src/lib/backlinks.ts via Node. None si Node ne sait pas le faire."""
    entree = json.dumps({"articles": articles, "projets": projets, "slugsWiki": slugs_wiki})
    try:
        r = subprocess.run(
            ["node", "--experimental-strip-types", "--no-warnings", str(NODE_WRAPPER)],
            input=entree, capture_output=True, text=True, timeout=60,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        print(f"NOTE  Node indisponible ({exc}) : comparaison avec le code du site ignorée.")
        return None
    if r.returncode != 0 or not r.stdout.strip():
        print(f"NOTE  Node n'a pas pu exécuter le .ts : comparaison ignorée.\n{r.stderr.strip()[:400]}")
        return None
    return json.loads(r.stdout)


def main() -> int:
    erreurs: list[str] = []
    wiki = load_wiki()
    slugs = set(wiki)
    articles = lire_articles()
    projets = lire_projets()

    attendu = index_python(articles, projets, slugs)

    # 1. Aucune entrée vide (un bloc vide ne doit jamais être affiché).
    for slug, liens in attendu.items():
        if not liens["articles"] and not liens["projets"]:
            erreurs.append(f"entrée vide dans l'index pour {slug}")

    # 2. Attendus écrits à la main.
    for slug, att in ATTENDUS.items():
        if slug not in slugs:
            erreurs.append(f"fiche attendue absente du wiki : {slug}")
            continue
        liens = attendu.get(slug, {"articles": [], "projets": []})
        obtenu_a = {x["slug"] for x in liens["articles"]}
        obtenu_p = {x["slug"] for x in liens["projets"]}
        for manque in sorted(set(att["articles"]) - obtenu_a):
            erreurs.append(f"{slug} : l'article {manque} devrait apparaître en lien retour")
        for manque in sorted(set(att["projets"]) - obtenu_p):
            erreurs.append(f"{slug} : le projet {manque} devrait apparaître en lien retour")

    # 3. Niveau et durée des projets renseignés (affichés sur la fiche).
    for slug, liens in attendu.items():
        for p in liens["projets"]:
            if p["niveau"] not in ("debutant", "intermediaire", "avance"):
                erreurs.append(f"{slug} : niveau de projet inconnu « {p['niveau']} »")
            if not p["duree"]:
                print(f"NOTE  {p['slug']} n'a pas de durée : la puce affichera le titre seul.")

    # 4. Le vrai code du site doit donner exactement le même index.
    res = index_node(articles, projets, sorted(slugs))
    if res is not None:
        if not res.get("ok"):
            erreurs.append(f"buildBacklinkIndex a échoué sur le contenu réel : {res.get('erreur')}")
        elif res["index"] != attendu:
            manquants = sorted(set(attendu) - set(res["index"]))
            surplus = sorted(set(res["index"]) - set(attendu))
            differents = sorted(s for s in set(attendu) & set(res["index"]) if attendu[s] != res["index"][s])
            erreurs.append(
                "index TypeScript ≠ index Python "
                f"(manquants={manquants}, en trop={surplus}, différents={differents})"
            )
        else:
            print("OK    src/lib/backlinks.ts donne le même index que la reconstruction Python.")

        # 5. Garde-fou : un slug inexistant doit faire échouer le build.
        faux = [{"slug": "essai", "data": {"title": "Essai", "related": ["fiche-qui-nexiste-pas"]}}]
        res2 = index_node(faux, [], sorted(slugs))
        if res2 is None or res2.get("ok") or "fiche-qui-nexiste-pas" not in str(res2.get("erreur", "")):
            erreurs.append("un slug de fiche inexistant n'a pas levé d'erreur explicite")
        else:
            print(f"OK    garde-fou : {res2['erreur']}")

    if "--json" in sys.argv:
        print(json.dumps(attendu, ensure_ascii=False, indent=2))
    else:
        for slug in sorted(attendu):
            liens = attendu[slug]
            a = ", ".join(x["slug"] for x in liens["articles"]) or "—"
            p = ", ".join(x["slug"] for x in liens["projets"]) or "—"
            print(f"  {slug:32} articles: {a:34} projets: {p}")

    for e in erreurs:
        print(f"ERREUR  {e}")
    print(
        f"{len(attendu)} fiche(s) sur {len(wiki)} reçoivent des liens retour "
        f"— {len(erreurs)} erreur(s)"
    )
    return 1 if erreurs else 0


if __name__ == "__main__":
    sys.exit(main())
