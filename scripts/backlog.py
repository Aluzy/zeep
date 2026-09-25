"""Backlog unifié du contenu Zeep : toutes les files de travail, dans l'ordre de priorité.

Module lu par scripts/prochain_lot.py (génération des missions) et scripts/etat_projet.py
(tableau de bord). Il ne décrit que du travail DÉDUIT du dépôt : une fiche sort de sa file
dès que le défaut qui l'y a placée est corrigé, sans que personne ait à tenir une liste.

Files, par ordre de priorité (une fiche n'apparaît que dans la première qui la contient) :

  vs-avant-lycee  notions vues avant le lycée (C1-C4) sans version simple — public prioritaire ;
  securite        fiches liées au secteur sans rappel de sécurité, définitions en HTML,
                  signalements de gravité haute (agents/donnees/signalements.json) ;
  niveaux         entrées périmées de la TABLE de agents/outils/mapping_niveau.py
                  (le lot complète la TABLE, puis lance mapping_niveau.py --lot) ;
  reecriture      définitions hors 25-60 mots, sources imprécises ou de type non admis,
                  version simple hors bornes, signalements de gravité moyenne (par domaine) ;
  creation        lexique attendu sans fiche, puis termes de programme sans fiche.

Principe « une fiche = une passe complète » : chaque élément porte TOUTES les règles que
la fiche enfreint, pas seulement celle qui l'a fait entrer dans sa file.
"""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import dette
from audit_couverture import couvert, index_des_formes
from zeeplib import (AGENTS_DIR, MISSIONS_DIR, RAPPORTS_DIR, load_lexique, lire_entete,
                     normaliser, slugify)

SIGNALEMENTS_FILE = AGENTS_DIR / "donnees" / "signalements.json"
MAPPING_NIVEAU = AGENTS_DIR / "outils" / "mapping_niveau.py"

FILES = {
    "vs-avant-lycee": "Version simple manquante (notions vues avant le lycée)",
    "securite": "Sécurité 230 V, HTML, signalements graves",
    "niveaux": "TABLE des niveaux périmée (mapping_niveau.py)",
    "reecriture": "Réécriture : définition, sources, version simple",
    "creation": "Création : lexique attendu, puis termes de programme",
}
# Nature du travail : "fiche" (changeset de set), "table" (code de mapping_niveau.py),
# "creation" (changeset de create).
NATURE = {"vs-avant-lycee": "fiche", "securite": "fiche", "niveaux": "table",
          "reecriture": "fiche", "creation": "creation"}

REGLES_REECRITURE = ("definition_longueur", "source_url_racine", "source_type_hors_liste",
                     "version_simple_longueur", "source_sans_url")


def _mapping_niveau():
    spec = importlib.util.spec_from_file_location("mapping_niveau", MAPPING_NIVEAU)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def signalements() -> list[dict]:
    if not SIGNALEMENTS_FILE.exists():
        return []
    return json.loads(SIGNALEMENTS_FILE.read_text(encoding="utf-8")).get("signalements", [])


def signalement_ouvert(sig: dict, fiche: dict | None) -> bool:
    """Un signalement est clos quand la fiche a été relue par un contrôleur
    indépendant depuis, ou validée par Alexandre."""
    if fiche is None:
        return False
    relec = fiche.get("relecture") or {}
    if relec.get("statut") == "valide":
        return False
    independante = relec.get("statut") == "relu-ia" and "controleur" in str(relec.get("par", ""))
    return not (independante and str(relec.get("date", "")) >= sig.get("date", ""))


def lots_en_cours() -> dict[str, str]:
    """Élément (slug ou terme) -> lot, pour les missions de rédaction sans rapport."""
    pris: dict[str, str] = {}
    if not MISSIONS_DIR.exists():
        return pris
    for chemin in sorted(MISSIONS_DIR.glob("*.md")):
        entete = lire_entete(chemin) or {}
        lot = entete.get("lot")
        if entete.get("role") != "redaction" or not lot:
            continue
        if (RAPPORTS_DIR / f"{lot}.md").exists():
            continue
        for cle in entete.get("elements") or []:
            pris.setdefault(cle, lot)
    return pris


def _item_fiche(slug: str, fiche: dict, defauts: dict[str, set[str]], motifs_sup: list[str]) -> dict:
    regles = [r for r in dette.REGLES if slug in defauts[r]]
    return {
        "cle": slug, "slug": slug, "terme": fiche.get("term", slug),
        "domaine": (fiche.get("domains") or ["?"])[0],
        "regles": regles,
        "motifs": [dette.REGLES[r] for r in regles] + motifs_sup,
    }


def construire(wiki: dict, exclure_en_cours: bool = True) -> dict[str, list[dict]]:
    """File -> éléments, dans l'ordre de priorité. Chaque élément :
    {cle, slug (None pour une création), terme, domaine, regles, motifs}."""
    defauts = dette.defauts(wiki)
    sig_ouverts = [s for s in signalements() if signalement_ouvert(s, wiki.get(s["slug"]))]
    sig_par_slug: dict[str, list[dict]] = {}
    for s in sig_ouverts:
        sig_par_slug.setdefault(s["slug"], []).append(s)

    def motifs_sig(slug: str) -> list[str]:
        return [f"Signalement {s['rapport']} ({s['gravite']}) : {s['motif']}" for s in sig_par_slug.get(slug, [])]

    files: dict[str, list[dict]] = {nom: [] for nom in FILES}
    vus: set[str] = set()

    def ajouter_fiches(nom: str, slugs: set[str], tri=lambda s: s) -> None:
        for slug in sorted(slugs - vus, key=tri):
            files[nom].append(_item_fiche(slug, wiki[slug], defauts, motifs_sig(slug)))
            vus.add(slug)

    ajouter_fiches("vs-avant-lycee", defauts["version_simple_manquante_avant_lycee"])
    graves = {s["slug"] for s in sig_ouverts if s.get("gravite") == "haute"}
    ajouter_fiches("securite", defauts["securite_230v_absente"] | defauts["definition_html"] | graves)

    mn = _mapping_niveau()
    etat = mn.analyser()
    for terme, lignes, slug in etat["perimees"]:
        files["niveaux"].append({
            "cle": f"TABLE:{terme}", "slug": slug, "terme": terme,
            "domaine": (wiki.get(slug, {}).get("domains") or ["?"])[0], "regles": [],
            "motifs": [f"TABLE périmée : « {terme} » ({lignes}) est rejeté alors que la fiche « {slug} » existe"],
        })

    a_reecrire = set().union(*(defauts[r] for r in REGLES_REECRITURE))
    a_reecrire |= {s["slug"] for s in sig_ouverts}
    ajouter_fiches("reecriture", a_reecrire,
                   tri=lambda s: ((wiki[s].get("domains") or ["?"])[0], s))

    # --- créations : lexique attendu, puis programmes -------------------------------
    index = index_des_formes(wiki)
    deja: set[str] = set()
    for code, termes in sorted((load_lexique().get("attendu") or {}).items()):
        for terme in termes:
            forme = normaliser(terme)
            if couvert(forme, index) or forme in deja:
                continue
            deja.add(forme)
            files["creation"].append({
                "cle": terme, "slug": None, "slugPrevu": slugify(terme), "terme": terme,
                "domaine": code, "regles": [],
                "motifs": [f"Lexique attendu (domaine {code}) sans fiche"],
            })
    for entree in etat["backlog"]:
        forme = normaliser(entree["terme"])
        if couvert(forme, index) or forme in deja:
            continue
        deja.add(forme)
        files["creation"].append({
            "cle": entree["terme"], "slug": None, "slugPrevu": slugify(entree["terme"]),
            "terme": entree["terme"], "domaine": "?", "regles": [],
            "motifs": [f"Terme de programme sans fiche (matrice {', '.join(entree['lignes'])})"
                       + (f" — {entree['note']}" if entree["note"] else "")],
        })

    if exclure_en_cours:
        pris = lots_en_cours()
        for nom in files:
            files[nom] = [x for x in files[nom] if x["cle"] not in pris]
    return files
