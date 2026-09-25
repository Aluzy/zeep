#!/usr/bin/env python3
"""Tableau de bord du projet, généré depuis le dépôt : docs/ETAT.md.

    python3 scripts/etat_projet.py               # (ré)écrit docs/ETAT.md
    python3 scripts/etat_projet.py --stdout      # affiche sans écrire (résumé de la CI)
    python3 scripts/etat_projet.py --verifier    # contrôle l'en-tête des rapports (CI) : code 1 si défaut

Remplace la synthèse écrite à la main (agents/rapports/synthese-zeep.md), qui se périmait dès
qu'elle était écrite. Tout ce qui figure ici est recalculé :
  - indicateurs de qualité (scripts/dette.py) et dette par règle (actuel / base du cliquet) ;
  - taille de chaque file du backlog (scripts/backlog.py) et ses premiers éléments ;
  - lots terminés et missions en cours (en-têtes des rapports et des missions) ;
  - brouillons de changeset encore à remplir ;
  - lacunes remontées par les rapports, sans fiche et absentes de src/data/lexique-attendu.json :
    à ajouter au lexique (ou à « horsPerimetre » avec sa raison) — décision éditoriale ;
  - décisions humaines ouvertes (rapports), signalements de fiches douteuses encore ouverts.

Le fichier ne contient pas de date : il ne change que si l'état du projet change.
Lot type : régénérer docs/ETAT.md dans le même commit que le rapport de lot.
"""
from __future__ import annotations

import sys

import backlog
import dette
from audit_couverture import couvert, index_des_formes
from zeeplib import (CHANGESETS_DIR, MISSIONS_DIR, RAPPORTS_DIR, ROOT, contient_a_remplir,
                     lire_changeset, lire_entete, load_lexique, load_wiki, normaliser)

ETAT_FILE = ROOT / "docs" / "ETAT.md"
# Fichiers de agents/rapports/ qui ne sont pas des rapports de lot.
HORS_RAPPORTS = {"TEMPLATE.md", "synthese-zeep.md"}
CLES_OBLIGATOIRES = ("lot", "titre", "date", "statut", "redacteur", "controleur")
STATUTS = ("termine", "partiel", "bloque")
APERCU_FILE = 8


def rapports() -> list[tuple[str, dict | None]]:
    out = []
    for chemin in sorted(RAPPORTS_DIR.glob("*.md")):
        if chemin.name in HORS_RAPPORTS or chemin.stem.endswith("-apercu"):
            continue
        out.append((chemin.name, lire_entete(chemin)))
    return out


def verifier_rapports() -> list[str]:
    erreurs = []
    for nom, entete in rapports():
        if entete is None:
            erreurs.append(f"agents/rapports/{nom} : en-tête absent (voir agents/rapports/TEMPLATE.md)")
            continue
        manquantes = [c for c in CLES_OBLIGATOIRES if not entete.get(c)]
        if manquantes:
            erreurs.append(f"agents/rapports/{nom} : clé(s) manquante(s) {', '.join(manquantes)}")
        if entete.get("lot") and f"{entete['lot']}.md" != nom:
            erreurs.append(f"agents/rapports/{nom} : « lot: {entete['lot']} » ne correspond pas au nom du fichier")
        if entete.get("statut") and entete["statut"] not in STATUTS:
            erreurs.append(f"agents/rapports/{nom} : statut « {entete['statut']} » (attendus : {', '.join(STATUTS)})")
        for cle in ("changesets", "fiches_creees", "fiches_modifiees", "lacunes", "decisions_humaines"):
            if cle in entete and not isinstance(entete[cle], list):
                erreurs.append(f"agents/rapports/{nom} : « {cle} » doit être une liste JSON")
        for lac in entete.get("lacunes") or []:
            if not isinstance(lac, dict) or not lac.get("terme"):
                erreurs.append(f"agents/rapports/{nom} : lacune mal formée {lac!r} "
                               '(attendu {"terme": …, "domaine": …, "vu_dans": …})')
    return erreurs


def cellule(v) -> str:
    return str(v if v not in (None, "") else "—").replace("|", "\\|")


def generer(wiki: dict) -> str:
    lignes = ["# État du projet Zeep", "",
              "> Généré par `python3 scripts/etat_projet.py` — ne pas modifier à la main.", ""]

    # --- indicateurs --------------------------------------------------------------------
    lignes += ["## Indicateurs de qualité", "", "| Indicateur | Valeur |", "|---|---|"]
    lignes += [f"| {k} | {v} |" for k, v in dette.indicateurs(wiki)]
    lignes.append("")

    config = dette.charger_config()
    base = config.get("base", {})
    actuels = dette.defauts(wiki, config)
    lignes += ["## Dette éditoriale (cliquet)", "",
               "| Règle | Fiches en défaut | Base tolérée |", "|---|---:|---:|"]
    for regle, libelle in dette.REGLES.items():
        lignes.append(f"| {libelle} (`{regle}`) | {len(actuels[regle])} | {len(base.get(regle, []))} |")
    lignes.append("")

    # --- backlog ------------------------------------------------------------------------
    files = backlog.construire(wiki)
    lignes += ["## Backlog (ordre de priorité)", "",
               "Lot suivant : `python3 scripts/prochain_lot.py --lot <LOT> [--file <file>] [--taille 20]`.", "",
               "| File | Éléments | Premiers éléments |", "|---|---:|---|"]
    for nom, items in files.items():
        premiers = ", ".join(f"`{x['cle']}`" for x in items[:APERCU_FILE]) + (" …" if len(items) > APERCU_FILE else "")
        lignes.append(f"| `{nom}` — {backlog.FILES[nom]} | {len(items)} | {premiers or '—'} |")
    lignes.append("")

    # --- lots ---------------------------------------------------------------------------
    lignes += ["## Lots", "", "| Lot | Titre | Date | Statut | Contrôleur | Fiches créées / modifiées |",
               "|---|---|---|---|---|---|"]
    entetes = []
    for nom, e in rapports():
        if e is None:
            lignes.append(f"| {nom[:-3]} | _en-tête absent_ | | | | |")
            continue
        entetes.append(e)
        lignes.append(f"| {cellule(e.get('lot'))} | {cellule(e.get('titre'))} | {cellule(e.get('date'))} "
                      f"| {cellule(e.get('statut'))} | {cellule(e.get('controleur'))} "
                      f"| {len(e.get('fiches_creees') or [])} / {len(e.get('fiches_modifiees') or [])} |")
    lignes.append("")

    en_cours = []
    lots_ouverts = set(backlog.lots_en_cours(wiki).values())
    for chemin in sorted(MISSIONS_DIR.glob("*.md")) if MISSIONS_DIR.exists() else []:
        e = lire_entete(chemin) or {}
        if e.get("role") in ("redaction", "controle") and e.get("lot") in lots_ouverts:
            en_cours.append(f"- `{chemin.name}` — {e.get('role')}, {len(e.get('elements') or [])} élément(s)"
                            + (f", file « {e['file']} »" if e.get("file") else ""))
    brouillons = []
    for chemin in sorted(CHANGESETS_DIR.glob("*.jsonl")):
        ops = lire_changeset(chemin)
        reste = sum(1 for o in ops if contient_a_remplir(o))
        if reste:
            brouillons.append(f"- `{chemin.name}` — {reste} opération(s) sur {len(ops)} à remplir")
    lignes += ["## En cours", "", "Missions des lots non intégrés au wiki :", *(en_cours or ["- aucune"]), "",
               "Brouillons de changeset :", *(brouillons or ["- aucun"]), ""]

    # --- lacunes remontées --------------------------------------------------------------
    lexique = load_lexique()
    connus = {normaliser(t) for termes in (lexique.get("attendu") or {}).values() for t in termes}
    connus |= {normaliser(t) for t in (lexique.get("horsPerimetre") or {}) if not t.startswith("_")}
    index = index_des_formes(wiki)
    lacunes: dict[str, dict] = {}
    for e in entetes:
        for lac in e.get("lacunes") or []:
            forme = normaliser(lac.get("terme", ""))
            if not forme or forme in connus or couvert(forme, index):
                continue
            entree = lacunes.setdefault(forme, {"terme": lac["terme"], "domaine": lac.get("domaine", "?"), "lots": []})
            entree["lots"].append(f"{e.get('lot')} ({lac.get('vu_dans', '?')})")
    lignes += ["## Lacunes remontées par les rapports", "",
               "Notions sans fiche, absentes de `src/data/lexique-attendu.json`. Décision éditoriale : "
               "les ajouter à `attendu` (elles entrent alors dans la file `creation`) ou à `horsPerimetre` "
               "avec leur raison.", ""]
    if lacunes:
        lignes += ["| Terme | Domaine | Vu dans |", "|---|---|---|"]
        lignes += [f"| {cellule(v['terme'])} | {cellule(v['domaine'])} | {cellule('; '.join(v['lots']))} |"
                   for v in sorted(lacunes.values(), key=lambda x: (x["domaine"], normaliser(x["terme"])))]
    else:
        lignes.append("Aucune.")
    lignes.append("")

    # --- décisions et signalements ------------------------------------------------------
    decisions = [(e.get("lot"), d) for e in entetes for d in e.get("decisions_humaines") or []]
    lignes += ["## Décisions humaines remontées par les rapports", "",
               "Suivi : issues GitHub étiquetées `decision`.", ""]
    lignes += [f"- **{lot}** — {d}" for lot, d in decisions] or ["Aucune."]
    lignes.append("")
    ouverts = [s for s in backlog.signalements() if backlog.signalement_ouvert(s, wiki.get(s["slug"]))]
    lignes += ["## Signalements de fiches douteuses", "",
               f"{len(ouverts)} ouvert(s) sur {len(backlog.signalements())} "
               "(`agents/donnees/signalements.json`) ; ils sont intégrés aux files `securite` et `reecriture`.", ""]
    return "\n".join(lignes).rstrip() + "\n"


def main() -> int:
    if "--verifier" in sys.argv:
        erreurs = verifier_rapports()
        for e in erreurs:
            print(f"ERREUR  {e}")
        print(f"En-têtes des rapports : {len(erreurs)} erreur(s)")
        return 1 if erreurs else 0
    texte = generer(load_wiki())
    if "--stdout" in sys.argv:
        print(texte)
        return 0
    ETAT_FILE.parent.mkdir(parents=True, exist_ok=True)
    ETAT_FILE.write_text(texte, encoding="utf-8")
    print(f"{ETAT_FILE.relative_to(ROOT)} écrit.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
