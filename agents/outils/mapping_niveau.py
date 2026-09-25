#!/usr/bin/env python3
"""J2-L2 — rattache les fiches du wiki aux niveaux scolaires de la matrice v2.

    python3 agents/outils/mapping_niveau.py --verifier      # contrôles seuls, rien n'est écrit (CI)
    python3 agents/outils/mapping_niveau.py                 # régénère le rapport CSV seul
    python3 agents/outils/mapping_niveau.py --lot J4-L1     # + changeset des niveaux manquants

Depuis le 25/09/2026 le script est INCRÉMENTAL : il a d'abord servi une seule fois (lot J2-L2,
197 fiches), puis s'arrêtait dès qu'une fiche avait déjà un niveau. Il peut maintenant être
relancé à chaque lot :
  - une fiche qui a déjà le niveau calculé est ignorée ;
  - une fiche qui a un niveau DIFFÉRENT est signalée (« écart »), jamais écrasée ;
  - une fiche rattachable sans niveau reçoit une opération dans agents/changesets/<LOT>.jsonl ;
  - un terme rejeté faute de fiche (« rejet ») alors qu'une fiche porte désormais ce terme ou
    ce synonyme est signalé comme TABLE PÉRIMÉE : c'est l'entrée du lot de mise à jour des
    niveaux (compléter la TABLE, puis relancer avec --lot).
Le changeset historique agents/changesets/J2-L2.jsonl n'est jamais réécrit.

Principe
--------
1. Le script lit la matrice curriculaire (snapshot commité dans agents/donnees/) et
   en extrait, pour chaque ligne, les « termes de programme » : la notion normalisée
   et chaque item du vocabulaire associé (découpage sur les virgules hors parenthèses).
2. Chaque terme distinct est cherché dans la TABLE DE CORRESPONDANCE ci-dessous,
   écrite et justifiée à la main. Un terme y renvoie soit vers une ou plusieurs
   fiches du wiki, soit vers un rejet explicite (aucune fiche ne correspond).
3. Pour chaque fiche rattachée, le script agrège les lignes de matrice qui la
   justifient et en déduit `niveau` : premiereApparition, cycles, familles, matriceIds.
4. Sorties : agents/rapports/J2-L2-correspondances.csv (toujours) et, avec --lot,
   agents/changesets/<LOT>.jsonl (seulement les niveaux manquants).

Garde-fous (le script s'arrête en erreur) :
  - un terme présent dans la matrice et absent de la TABLE  -> couverture incomplète ;
  - une entrée de la TABLE qui n'apparaît dans aucune ligne -> table périmée ;
  - un slug cité qui n'existe pas dans src/content/wiki     -> faute de frappe ;
  - une fiche rattachée sans aucun matriceId                -> justification manquante.

Règle de rejet : on ne force jamais un rattachement douteux. Une fiche sans
correspondance claire reste sans `niveau` (cas normal des notions hors programme).
Les lignes de la famille FAM19 (constats d'absence de notion) sont ignorées.
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
import unicodedata
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RACINE / "scripts"))
from zeeplib import formes_d_une_fiche, normaliser  # noqa: E402
MATRICE = RACINE / "agents" / "donnees" / "matrice-electricite-electronique-v2.csv"
WIKI = RACINE / "src" / "content" / "wiki"
CHANGESETS = RACINE / "agents" / "changesets"
RAPPORT_CSV = RACINE / "agents" / "rapports" / "J2-L2-correspondances.csv"
LOT_HISTORIQUE = "J2-L2"  # changeset d'origine : jamais réécrit

# Précocité des niveaux. C1 < C2 < C3 < C4 < 2GT < 1G < 1-TG < TG, puis les voies.
# 1-TG (première + terminale spé SI) commence en première : il se place juste
# après 1G et avant TG. Les voies ne servent qu'aux notions qui n'apparaissent
# nulle part ailleurs ; entre elles, CAP (2 ans après la 3e) précède le bac pro
# (3 ans après la 3e), lui-même retenu avant STI2D dont le programme commence en
# première. Cet ordre ne sert qu'à choisir `premiereApparition`.
RANG = {"C1": 1, "C2": 2, "C3": 3, "C4": 4, "2GT": 5, "1G": 6, "1-TG": 7, "TG": 8,
        "CAP": 9, "BACPRO": 10, "STI2D": 11}

# --------------------------------------------------------------------------------------
# TABLE DE CORRESPONDANCE  terme de programme -> fiches du wiki
#
# Clé      : le terme tel qu'il figure dans la matrice (notion normalisée ou item du
#            vocabulaire associé). Suffixe « |Mxxx » quand un même mot doit être
#            traité différemment selon la ligne (ex. « résistance » grandeur / composant).
# Valeur   : (slugs, type, confiance, backlog, note)
#   type      : direct   — le terme est le libellé de la fiche ;
#               variante — même notion, orthographe/pluriel/abréviation différents ;
#               compose  — libellé composé qui recouvre plusieurs fiches ;
#               sens     — rapprochement par le sens, justifié dans la note ;
#               rejet    — aucune fiche ne correspond : on ne rattache rien.
#   confiance : haute | moyenne | basse (les « basse » sont listées dans le rapport
#               pour arbitrage humain) ; vide pour un rejet.
#   backlog   : True si le terme désigne une notion du programme qui MÉRITE une fiche
#               (alimente le backlog de rédaction J2-L4 / J3) ; False si le rejet tient
#               au hors-périmètre ou au fait que la ligne est déjà couverte autrement.
# --------------------------------------------------------------------------------------
TABLE: dict[str, tuple[list[str], str, str, bool, str]] = {
    # --- M002 / M003 / M007 : circuit à une boucle (cycles 2 et 3) -----------------
    "Circuit électrique à une boucle": (["circuit-electrique"], "sens", "haute", False,
        "La notion du programme est le circuit électrique lui-même."),
    "Objets et circuits électriques simples": (["circuit-electrique"], "sens", "haute", False,
        "Idem : circuit électrique simple."),
    "Circuit électrique simple à une boucle": (["circuit-electrique"], "sens", "haute", False,
        "Idem."),
    "circuit électrique": (["circuit-electrique"], "direct", "haute", False, ""),
    "générateur": (["generateur-electrique"], "variante", "haute", False,
        "« Générateur » du circuit scolaire = fiche Générateur électrique."),
    "pile": (["pile-electrique"], "variante", "haute", False, ""),
    "pile électrique": (["pile-electrique"], "direct", "haute", False, ""),
    "interrupteur": (["interrupteur"], "direct", "haute", False, ""),
    "ampoule": ([], "rejet", "", True,
        "Pas de fiche générique « lampe / ampoule » ; ampoule-led est un type particulier."),
    "récepteur": ([], "rejet", "", True,
        "« Récepteur » au sens du dipôle qui consomme l'énergie ; la fiche voisine "
        "recepteur-radiofrequence a un tout autre sens."),
    "circuit ouvert/fermé": (["circuit-ouvert", "circuit-ferme"], "compose", "haute", False,
        "Libellé composé recouvrant deux fiches."),
    "circuit fermé/ouvert": (["circuit-ferme", "circuit-ouvert"], "compose", "haute", False,
        "Libellé composé recouvrant deux fiches."),
    "matériau conducteur/isolant": (["conducteur-electrique", "isolant-electrique"], "compose",
        "haute", False, "Libellé composé recouvrant deux fiches."),
    "câbles": (["cable-electrique"], "variante", "haute", False, "Pluriel."),
    "câbles conducteurs": (["cable-electrique"], "variante", "haute", False, ""),
    "objet technique": ([], "rejet", "", False, "Notion de technologie, hors périmètre du wiki."),
    "règles de sécurité": ([], "rejet", "", True,
        "Pas de fiche « sécurité électrique » ; notion pourtant attendue dès le cycle 2."),

    # --- M004 / M005 : objets techniques et source d'énergie (cycle 2) --------------
    "Objets techniques et source d'énergie": ([], "rejet", "", False,
        "Notion de technologie générale, sans fiche correspondante."),
    "Objets techniques utilisant une source d'énergie électrique": ([], "rejet", "", False,
        "Idem ; le vocabulaire de la ligne porte les rattachements."),
    "besoin": ([], "rejet", "", False, "Vocabulaire de technologie, hors périmètre."),
    "énergie électrique": ([], "rejet", "", True,
        "Aucune fiche « énergie électrique ». Ne PAS rattacher à la fiche « électricité » : "
        "AGENTS.md §3 interdit de confondre électricité et énergie."),
    "maquette": ([], "rejet", "", False, "Hors périmètre."),
    "assistance électrique": ([], "rejet", "", False, "Exemple d'application, hors périmètre."),

    # --- M006 : dispositifs numériques (cycle 2) ------------------------------------
    "Dispositifs numériques": ([], "rejet", "", False, "Libellé générique ; vocabulaire traité ligne à ligne."),
    "processeur": (["processeur-cpu"], "variante", "haute", False, ""),
    "ordinateur": ([], "rejet", "", False, "Hors périmètre électricité/électronique du wiki."),
    "numérique": ([], "rejet", "", False,
        "Adjectif trop générique ; les fiches signal-numerique et circuit-numerique ont un sens précis."),

    # --- M009 / M014 / M034 / M072 : grandeurs et lois (cycle 4 -> bac pro) ----------
    "Circuits électriques et lois de l'électricité": (["circuit-electrique"], "sens", "haute", False, ""),
    "Circuit électrique : grandeurs flux/effort": (["circuit-electrique"], "sens", "haute", False, ""),
    "Loi des mailles et des nœuds": ([], "rejet", "", True, "Aucune fiche sur les lois de Kirchhoff."),
    "Grandeurs électriques en régime établi": ([], "rejet", "", False,
        "Libellé chapeau ; le vocabulaire de la ligne porte les rattachements."),
    "tension": (["tension-electrique"], "variante", "haute", False, ""),
    "intensité": (["intensite-electrique"], "variante", "haute", False, ""),
    "courant": (["courant-electrique"], "variante", "haute", False, ""),
    "courant électrique": (["courant-electrique"], "direct", "haute", False, ""),
    "puissance électrique": (["puissance-electrique"], "direct", "haute", False, ""),
    "puissance": (["puissance-electrique"], "variante", "haute", False, ""),
    "fréquence": (["frequence-electrique"], "variante", "haute", False,
        "Ligne M072 : fréquence du réseau alternatif."),
    "résistance|M009": (["resistance-electrique"], "variante", "haute", False,
        "Cycle 4 : « tension, intensité, résistance » désigne la GRANDEUR."),
    "résistance|M033": (["resistance"], "direct", "haute", False,
        "Spé SI : liste de COMPOSANTS (résistance, inductance, condensateur, diode, transistor)."),
    "dipôle ohmique": (["resistance"], "sens", "moyenne", False,
        "Le dipôle ohmique est le conducteur ohmique modélisant la résistance (cf. définition de la fiche)."),
    "dipôle": ([], "rejet", "", True, "Aucune fiche « dipôle »."),
    "loi d'Ohm": ([], "rejet", "", True, "Aucune fiche « loi d'Ohm » alors que la notion est centrale au cycle 4."),
    "loi des nœuds/mailles": ([], "rejet", "", True, "Aucune fiche sur les lois de Kirchhoff."),
    "loi des mailles": ([], "rejet", "", True, "Aucune fiche."),
    "loi des nœuds": ([], "rejet", "", True, "Aucune fiche."),
    "lois de Kirchhoff": ([], "rejet", "", True, "Aucune fiche."),
    "lois de comportement": ([], "rejet", "", False, "Vocabulaire de modélisation SI, hors périmètre."),
    "régime continu/monophasé/triphasé": (["courant-continu"], "sens", "moyenne", True,
        "Seul le régime continu a une fiche ; monophasé et triphasé n'en ont pas (backlog)."),
    "monophasé/triphasé": ([], "rejet", "", True, "Aucune fiche monophasé/triphasé."),
    "courants faibles/forts": ([], "rejet", "", False, "Vocabulaire de chantier, sans fiche."),
    "effet thermique/magnétique/chimique": ([], "rejet", "", True,
        "Effets du courant : aucune fiche dédiée (voir aussi « effet Joule »)."),
    "Courant électrique et ses effets": ([], "rejet", "", False, "Libellé chapeau, couvert par le vocabulaire."),

    # --- M010 : signal électrique (cycle 4) -----------------------------------------
    "Signal électrique, vecteur d'information": ([], "rejet", "", True,
        "Pas de fiche générique « signal électrique » ; seules signal-analogique et "
        "signal-numerique existent et ne recouvrent pas la notion du cycle 4."),
    "signal": ([], "rejet", "", True, "Idem."),
    "signal électrique": ([], "rejet", "", True, "Idem."),
    "information": ([], "rejet", "", False, "Trop générique."),

    # --- M011 / M036 / M039 / M048 / M050 / M051 / M061 : chaînes d'énergie ----------
    "Chaîne d'énergie": ([], "rejet", "", True, "Aucune fiche « chaîne d'énergie » (notion pivot du cycle 4)."),
    "chaîne d'énergie": ([], "rejet", "", True, "Idem."),
    "chaîne de l'énergie": ([], "rejet", "", True, "Idem."),
    "Chaîne de puissance": ([], "rejet", "", True, "Aucune fiche « chaîne de puissance »."),
    "Chaîne de puissance et réversibilité": ([], "rejet", "", True, "Idem."),
    "Chaîne de puissance approfondie": ([], "rejet", "", True, "Idem."),
    "chaîne de puissance": ([], "rejet", "", True, "Idem."),
    "Conception d'une chaîne d'énergie": ([], "rejet", "", False, "Activité de conception, pas une notion à définir."),
    "Simulation énergétique multi-physique": ([], "rejet", "", False, "Activité de simulation, hors périmètre."),
    "simulation multi-physique": ([], "rejet", "", False, "Hors périmètre."),
    "Circuits électriques et chaîne de l'énergie": ([], "rejet", "", False, "Couvert par le vocabulaire de la ligne."),
    "grandeur d'effort": ([], "rejet", "", False, "Vocabulaire de modélisation SI."),
    "grandeur de flux": ([], "rejet", "", False, "Vocabulaire de modélisation SI."),
    "stockage d'énergie": ([], "rejet", "", True,
        "Aucune fiche « stockage d'énergie » ; ne pas l'assimiler à batterie ou accumulateur."),
    "alimentation → action": ([], "rejet", "", False, "Blocs fonctionnels de la chaîne d'énergie, pas une notion."),
    "conversion": ([], "rejet", "", False, "Terme générique de la chaîne de puissance."),
    "adaptation": ([], "rejet", "", False, "Terme générique de la chaîne de puissance."),
    "production/transformation d'énergie": (["production-d-electricite"], "sens", "moyenne", False,
        "Volet « production » de la chaîne de puissance STI2D."),
    "Système de gestion et performance énergétique": ([], "rejet", "", False, "Couvert par le vocabulaire."),
    "système de gestion": ([], "rejet", "", False, "Terme générique, sans fiche."),
    "performance énergétique": (["efficacite-energetique"], "sens", "haute", False,
        "La performance énergétique d'un système est traitée par la fiche Efficacité énergétique."),
    "paramétrage": ([], "rejet", "", False, "Activité, hors périmètre."),
    "programmation": ([], "rejet", "", False, "Informatique, hors périmètre du wiki élec."),
    "cahier des charges énergétique": ([], "rejet", "", False, "Hors périmètre."),

    # --- M012 / M015 / M017 / M024 / M037 / M041 / M057 / M071 : chaîne d'information -
    "Chaîne d'information, capteurs et actionneurs": ([], "rejet", "", False, "Couvert par le vocabulaire."),
    "Chaîne d'acquisition": ([], "rejet", "", True, "Aucune fiche « chaîne d'acquisition »."),
    "Chaîne d'information et conditionnement": ([], "rejet", "", False, "Couvert par le vocabulaire."),
    "Chaîne d'information et architecture associée": ([], "rejet", "", False, "Couvert par le vocabulaire."),
    "Simulation du comportement informationnel": ([], "rejet", "", False, "Activité de simulation, hors périmètre."),
    "chaîne d'information": ([], "rejet", "", True, "Aucune fiche « chaîne d'information » (notion pivot du cycle 4)."),
    "chaîne d'acquisition": ([], "rejet", "", True, "Aucune fiche."),
    "simulation informationnelle": ([], "rejet", "", False, "Hors périmètre."),
    "acquisition": ([], "rejet", "", False, "Terme générique ; voir « chaîne d'acquisition »."),
    "restitution de l'information": ([], "rejet", "", False, "Terme générique, sans fiche."),
    "acquisition de données": ([], "rejet", "", True, "Aucune fiche ; notion des programmes 2de GT et STI2D."),
    "capteur": (["capteur"], "direct", "haute", False, ""),
    "Capteurs, actionneurs, IHM": ([], "rejet", "", False, "Couvert par le vocabulaire."),
    "Capteur associé à un microcontrôleur": ([], "rejet", "", False, "Couvert par le vocabulaire."),
    "Capteurs et détecteurs": ([], "rejet", "", False, "Couvert par le vocabulaire."),
    "actionneur": (["actionneur"], "direct", "haute", False, ""),
    "commande d'actionneur": (["actionneur"], "sens", "moyenne", False,
        "Commander un actionneur : rattaché à la fiche Actionneur."),
    "Commande d'actionneur et acquisition de données": ([], "rejet", "", False, "Couvert par le vocabulaire."),
    "capteur/actionneur/interface": (["capteur", "actionneur"], "compose", "haute", False,
        "Libellé composé ; « interface » n'a pas de fiche."),
    "codeur": ([], "rejet", "", True, "Aucune fiche « codeur »."),
    "détecteur": ([], "rejet", "", True,
        "Aucune fiche « détecteur » ; ne pas l'assimiler à « capteur » (un détecteur est tout-ou-rien)."),
    "signal analogique/numérique": (["signal-analogique", "signal-numerique"], "compose", "haute", False,
        "Libellé composé recouvrant deux fiches."),
    "signal numérique": (["signal-numerique"], "direct", "haute", False, ""),
    "IHM": ([], "rejet", "", True, "Aucune fiche « interface homme-machine »."),
    "ports d'entrée/sortie": ([], "rejet", "", True, "Aucune fiche « entrées/sorties »."),
    "amplification": ([], "rejet", "", True,
        "Aucune fiche générique « amplificateur » ; les fiches existantes sont spécialisées "
        "(audio, opérationnel) et gain-electronique ne traite que le gain."),
    "amplificateur linéaire intégré": (["amplificateur-operationnel"], "sens", "haute", False,
        "ALI est le nom des programmes pour l'amplificateur opérationnel."),
    "filtrage passe-bas": (["filtre-passe-bas"], "variante", "haute", False, ""),

    # --- M013 / M043 / M058 : systèmes embarqués et microcontrôleurs -----------------
    "Systèmes embarqués, microcontrôleurs, réseaux informatiques": ([], "rejet", "", False,
        "Couvert par le vocabulaire."),
    "Cartes microcontrôleur et objets connectés": ([], "rejet", "", True,
        "Aucune fiche générique « carte à microcontrôleur » ; carte-arduino est une carte "
        "particulière, non citée par les programmes."),
    "Cartes microcontrôleur et IHM": ([], "rejet", "", True, "Idem."),
    "systèmes embarqués": (["electronique-embarquee"], "sens", "haute", False,
        "La fiche Électronique embarquée définit les systèmes embarqués."),
    "système embarqué": (["electronique-embarquee"], "sens", "haute", False, "Idem, au singulier."),
    "microcontrôleur": (["microcontroleur"], "direct", "haute", False, ""),
    "microprocesseur": (["microprocesseur"], "direct", "haute", False, ""),
    "nano-ordinateur": (["carte-raspberry-pi"], "sens", "moyenne", False,
        "Le nano-ordinateur des programmes STI2D correspond à la carte Raspberry Pi "
        "(carte à microprocesseur exécutant un système d'exploitation)."),
    "protocole": (["protocole-de-communication"], "variante", "haute", False, ""),
    "réseau local": ([], "rejet", "", True, "Aucune fiche « réseau informatique / réseau local »."),
    "Architecture matérielle et logicielle": ([], "rejet", "", False, "Informatique, hors périmètre."),
    "architecture matérielle/logicielle": ([], "rejet", "", False, "Informatique, hors périmètre."),
    "Algorithme et programmation": ([], "rejet", "", False, "Informatique, hors périmètre."),
    "algorithme": ([], "rejet", "", False, "Informatique, hors périmètre."),

    # --- M016 : servomoteurs et électronique de puissance (2de GT) -------------------
    "Servomoteurs et électronique de puissance": ([], "rejet", "", False, "Couvert par le vocabulaire."),
    "servomoteur électrique": (["servomoteur"], "variante", "haute", False, ""),
    "électronique de puissance": (["electronique-de-puissance"], "direct", "haute", False, ""),
    "Électronique de puissance, moteurs et transformateurs": ([], "rejet", "", False,
        "Couvert par le vocabulaire."),
    "consommation électrique": (["consommation-electrique"], "direct", "haute", False, ""),

    # --- M018 : capteur photographique (2de GT) --------------------------------------
    "Capteur photographique (CCD)": (["capteur-optique"], "sens", "moyenne", False,
        "Un capteur CCD est un capteur optique (la fiche cite photodiode et phototransistor)."),
    "capteur CCD": (["capteur-optique"], "sens", "moyenne", False, "Idem."),
    "photosite": ([], "rejet", "", False, "Détail de constitution d'un capteur d'image, hors périmètre."),
    "résolution du capteur": ([], "rejet", "", False, "Caractéristique, pas une notion du wiki."),

    # --- M019 : centres de données (2de GT) ------------------------------------------
    "Consommation électrique des centres de données": ([], "rejet", "", False, "Couvert par le vocabulaire."),
    "centre de données": ([], "rejet", "", False, "Hors périmètre (informatique)."),
    "refroidissement": ([], "rejet", "", False,
        "Refroidissement d'un centre de données ; ventilateur-de-refroidissement et "
        "dissipateur-thermique sont des composants, pas la notion visée."),

    # --- M020 / M021 / M022 / M031 : mesure et instrumentation -----------------------
    "Caractéristique tension-courant et capteurs": ([], "rejet", "", False, "Couvert par le vocabulaire."),
    "Instrumentation électrique de laboratoire": ([], "rejet", "", False, "Couvert par le vocabulaire."),
    "Instrumentation électrique": ([], "rejet", "", False, "Couvert par le vocabulaire."),
    "Incertitude de mesure électrique": ([], "rejet", "", False, "Métrologie générale, hors périmètre."),
    "multimètre": (["multimetre"], "direct", "haute", False, ""),
    "oscilloscope": ([], "rejet", "", True,
        "Aucune fiche « oscilloscope » alors que l'appareil est au programme de 2de GT."),
    "caractéristique tension-courant": ([], "rejet", "", True,
        "Aucune fiche « caractéristique courant-tension »."),
    "caractéristique": ([], "rejet", "", True, "Idem (ligne M029)."),
    "courbe d'étalonnage": ([], "rejet", "", False, "Méthode expérimentale, hors périmètre."),
    "interface d'acquisition": ([], "rejet", "", True, "Aucune fiche ; voir « chaîne d'acquisition »."),
    "interface de mesure": ([], "rejet", "", True, "Idem."),
    "incertitude": ([], "rejet", "", False, "Métrologie générale, hors périmètre."),
    "chiffres significatifs": ([], "rejet", "", False, "Mathématiques, hors périmètre."),
    "schéma normalisé": (["schema-electrique"], "sens", "haute", False,
        "Le schéma normalisé d'un circuit est le schéma électrique."),

    # --- M025 / M048 / M066 : production d'électricité -------------------------------
    "Méthodes de production d'énergie électrique": (["production-d-electricite"], "sens", "haute", False, ""),
    "Moyens de production d'électricité": (["production-d-electricite"], "sens", "haute", False, ""),
    "production": (["production-d-electricite"], "sens", "haute", False,
        "Volet « production » du champ d'intervention CAP / bac pro."),
    "conversion électrochimique": ([], "rejet", "", True,
        "Aucune fiche sur la conversion électrochimique ; les fiches pile/batterie ne la définissent pas."),
    "dynamo": (["dynamo"], "direct", "haute", False, ""),
    "panneau photovoltaïque": (["panneau-photovoltaique"], "direct", "haute", False, ""),
    "pile à hydrogène": ([], "rejet", "", True, "Aucune fiche « pile à combustible / à hydrogène »."),
    "centrale électrique": (["centrale-electrique"], "direct", "haute", False, ""),
    "production centralisée/décentralisée": ([], "rejet", "", True,
        "Aucune fiche sur la production centralisée/décentralisée."),

    # --- M026 / M027 / M045 / M053 / M060 / M064 / M065 : transport et distribution ---
    "Effet Joule et optimisation du transport": ([], "rejet", "", False, "Couvert par le vocabulaire."),
    "effet Joule": ([], "rejet", "", True,
        "Aucune fiche « effet Joule » alors que la notion est au programme (terminale, spé PC)."),
    "transport de l'électricité": (["reseau-de-transport"], "sens", "haute", False,
        "Le transport de l'électricité est assuré par le réseau de transport."),
    "transport": (["reseau-de-transport"], "sens", "haute", False, "Idem (champ d'intervention CAP / bac pro)."),
    "Réseau de distribution électrique": (["reseau-de-distribution"], "direct", "haute", False, ""),
    "réseau de distribution": (["reseau-de-distribution"], "direct", "haute", False, ""),
    "réseau de distribution électrique": (["reseau-de-distribution"], "direct", "haute", False, ""),
    "distribution": (["reseau-de-distribution"], "sens", "haute", False, "Idem (champ d'intervention CAP / bac pro)."),
    "Réseau de transport et de distribution": (["reseau-de-transport", "reseau-de-distribution"],
        "compose", "haute", False, "Libellé composé recouvrant deux fiches."),
    "Réseaux électriques alternatifs/continus (approfondi)": ([], "rejet", "", False, "Couvert par le vocabulaire."),
    "Architecture des réseaux de distribution": ([], "rejet", "", False, "Couvert par le vocabulaire."),
    "Champ d'intervention sur les installations électriques": (["installation-electrique"], "sens", "haute", False,
        "Le champ d'intervention du CAP porte sur les installations électriques."),
    "Champ d'intervention RAP": ([], "rejet", "", False,
        "Libellé administratif (référentiel d'activités professionnelles) ; couvert par le vocabulaire."),
    "alternatif/continu": (["courant-alternatif", "courant-continu"], "compose", "haute", False,
        "Libellé composé recouvrant deux fiches."),
    "transformation de l'énergie électrique": (["poste-de-transformation"], "sens", "basse", False,
        "CONFIANCE BASSE : dans le champ production/transport/distribution/transformation, "
        "« transformation » désigne les postes de transformation, mais le terme peut aussi "
        "viser la conversion d'énergie en général. À trancher."),
    "réseaux de communication (cuivre, fibre optique, sans fil)": ([], "rejet", "", True,
        "Aucune fiche « fibre optique » ni « réseau de communication » ; sans-fil couvert par wi-fi seulement."),
    "smartgrid": (["reseau-intelligent-smart-grid"], "variante", "haute", False, ""),
    "pertes": ([], "rejet", "", True, "Pertes en ligne : aucune fiche (voir « effet Joule »)."),
    "mix énergétique": ([], "rejet", "", True, "Aucune fiche « mix énergétique »."),

    # --- M028 : électrostatique (1re spé PC) -----------------------------------------
    "Charge électrique et champ électrostatique": ([], "rejet", "", False, "Couvert par le vocabulaire."),
    "charge électrique": (["charge-electrique"], "direct", "haute", False, ""),
    "interaction électrostatique": (["electrostatique"], "sens", "haute", False,
        "La fiche Électrostatique traite les charges au repos et leurs interactions."),
    "champ électrostatique": (["champ-electrique"], "sens", "haute", False,
        "Le champ électrostatique est le champ électrique créé par des charges au repos."),
    "loi de Coulomb": ([], "rejet", "", True, "Aucune fiche « loi de Coulomb »."),
    "ligne de champ": ([], "rejet", "", True, "Aucune fiche « ligne de champ »."),

    # --- M029 / M030 : source de tension, puissance, rendement (1re spé PC) ----------
    "Source réelle de tension": ([], "rejet", "", False, "Couvert par le vocabulaire identique de la ligne."),
    "Puissance, énergie et rendement": ([], "rejet", "", False, "Couvert par le vocabulaire."),
    "source réelle de tension": (["generateur-electrique"], "sens", "moyenne", False,
        "Modèle du générateur réel (f.é.m. + résistance interne) : rattaché à Générateur électrique."),
    "résistance interne": ([], "rejet", "", True, "Aucune fiche « résistance interne »."),
    "débit de charges": ([], "rejet", "", False,
        "Définition de l'intensité, déjà portée par le terme « intensité » de la même ligne."),
    "énergie": ([], "rejet", "", True,
        "Aucune fiche « énergie » ; ne pas confondre avec puissance (AGENTS.md §3)."),
    "rendement": (["rendement-energetique"], "variante", "haute", False, ""),
    "convertisseur": ([], "rejet", "", True,
        "« Convertisseur » au sens d'un convertisseur d'énergie ; les fiches convertisseur-* "
        "du wiki traitent du signal ou de la fréquence."),

    # --- M032 / M046 / M052 : condensateurs et stockage ------------------------------
    "Dipôle RC et condensateur": ([], "rejet", "", False, "Couvert par le vocabulaire."),
    "Stockage électrostatique": ([], "rejet", "", False, "Couvert par le vocabulaire."),
    "Convertisseurs et stockeurs d'énergie": ([], "rejet", "", False, "Couvert par le vocabulaire."),
    "condensateur": (["condensateur"], "direct", "haute", False, ""),
    "dipôle RC": ([], "rejet", "", True, "Aucune fiche « circuit RC »."),
    "constante de temps": ([], "rejet", "", True, "Aucune fiche « constante de temps »."),
    "régime transitoire": ([], "rejet", "", True, "Aucune fiche « régime transitoire »."),
    "supercondensateur": ([], "rejet", "", True, "Aucune fiche « supercondensateur »."),
    "diagramme de Ragone": ([], "rejet", "", False, "Outil de comparaison, hors périmètre."),
    "modulateur": ([], "rejet", "", False,
        "Bloc fonctionnel de la chaîne de puissance ; voir « modulation de puissance »."),

    # --- M033 : électrocinétique (spé SI) --------------------------------------------
    "Électrocinétique complète": ([], "rejet", "", False, "Libellé chapeau ; couvert par le vocabulaire."),
    "inductance": (["bobine-inductance"], "variante", "haute", False, ""),
    "diode": (["diode"], "direct", "haute", False, ""),
    "transistor": (["transistor"], "direct", "haute", False, ""),
    "source alternative": (["courant-alternatif"], "sens", "moyenne", False,
        "Source de tension alternative : rattachée à la fiche Courant alternatif, faute de fiche « tension alternative »."),

    # --- M035 : modulation (terminale spé SI) ----------------------------------------
    "Modulation/démodulation numérique": ([], "rejet", "", False, "Couvert par le vocabulaire."),
    "modulation/démodulation": (["modulation"], "variante", "haute", False,
        "La fiche Modulation traite la transmission d'information par un signal."),
    "internet des objets": (["objet-connecte-iot"], "sens", "haute", False,
        "L'internet des objets est traité par la fiche Objet connecté (IoT)."),

    # --- M038 / M047 / M070 : asservissement et régulation ---------------------------
    "Systèmes asservis linéaires": ([], "rejet", "", True, "Aucune fiche « système asservi »."),
    "Boucle de régulation/asservissement": ([], "rejet", "", True, "Idem."),
    "Automatismes et asservissement": ([], "rejet", "", True, "Idem."),
    "système asservi": ([], "rejet", "", True, "Aucune fiche."),
    "asservissement": ([], "rejet", "", True, "Aucune fiche."),
    "régulation": ([], "rejet", "", True,
        "Aucune fiche « régulation » ; regulateur-de-tension désigne un composant, pas la boucle de régulation."),
    "automatisme": ([], "rejet", "", True, "Aucune fiche « automatisme »."),
    "comparateur": ([], "rejet", "", True, "Aucune fiche « comparateur »."),
    "correcteur proportionnel": ([], "rejet", "", True, "Aucune fiche « correcteur »."),
    "erreur statique": ([], "rejet", "", False, "Grandeur d'automatique, hors périmètre v1."),
    "point de fonctionnement": ([], "rejet", "", True, "Aucune fiche « point de fonctionnement »."),

    # --- M039 / M040 : modulation de l'énergie (STI2D) -------------------------------
    "Modulation électrique commandée": ([], "rejet", "", False, "Couvert par le vocabulaire."),
    "modulation": (["electronique-de-puissance"], "sens", "moyenne", False,
        "Ligne M039 : « modulation » de l'ÉNERGIE dans la chaîne de puissance ; la fiche "
        "Modulation traite du signal et ne convient pas ici."),
    "modulation de puissance": (["electronique-de-puissance"], "sens", "moyenne", False, "Idem."),
    "AC/DC": (["redresseur"], "sens", "haute", False, "La conversion AC/DC est le redressement."),
    "DC/AC": (["onduleur"], "sens", "haute", False, "La conversion DC/AC est l'onduleur."),
    "DC/DC": ([], "rejet", "", True,
        "Aucune fiche « hacheur / convertisseur DC-DC » ; alimentation-a-decoupage en est une "
        "application, pas la notion."),

    # --- M042 / M058 : conversion analogique-numérique -------------------------------
    "Conversion analogique-numérique (CAN)": (["convertisseur-analogique-numerique-can"], "sens", "haute", False, ""),
    "CAN": (["convertisseur-analogique-numerique-can"], "variante", "haute", False,
        "Abréviation du programme ; à ne pas confondre avec le bus CAN (ligne M044)."),
    "résolution": ([], "rejet", "", True, "Caractéristique du convertisseur, sans fiche propre."),
    "quantum": ([], "rejet", "", True, "Caractéristique du convertisseur, sans fiche propre."),
    "échantillonnage": ([], "rejet", "", True, "Aucune fiche « échantillonnage »."),

    # --- M044 / M059 / M069 : bus et communication -----------------------------------
    "Bus de communication et transmission sans fil": ([], "rejet", "", False, "Couvert par le vocabulaire."),
    "Réseaux et bus de communication (approfondi)": ([], "rejet", "", False, "Couvert par le vocabulaire."),
    "Réseaux VDI et bus de données": ([], "rejet", "", False, "Couvert par le vocabulaire."),
    "bus de données": (["bus-de-donnees"], "direct", "haute", False, ""),
    "bus de terrain": (["bus-de-donnees"], "sens", "moyenne", False,
        "Un bus de terrain est un bus de données industriel ; aucune fiche dédiée."),
    "bus KNX/CAN/I²C/SPI": (["bus-i2c", "bus-spi"], "compose", "haute", False,
        "Libellé composé : I²C et SPI ont une fiche ; KNX et CAN n'en ont pas (backlog)."),
    "WiFi": (["wi-fi"], "variante", "haute", False, ""),
    "Bluetooth": (["bluetooth"], "direct", "haute", False, ""),
    "routeur": ([], "rejet", "", True, "Aucune fiche « routeur »."),
    "VDI": ([], "rejet", "", True, "Aucune fiche « VDI (voix-données-images) »."),

    # --- M060 / M063 / M068 : machines, conversion (CAP / bac pro) -------------------
    "moteur à courant alternatif": (["moteur-electrique"], "sens", "haute", False,
        "Aucune fiche « moteur asynchrone » ; rattaché à la fiche générale Moteur électrique."),
    "machine électromagnétique": (["moteur-electrique"], "sens", "moyenne", False,
        "Machine électromagnétique (moteur ou génératrice) : la fiche la plus proche est Moteur électrique."),
    "transformateur": (["transformateur"], "direct", "haute", False, ""),
    "variateur": (["convertisseur-de-frequence"], "sens", "moyenne", False,
        "Un variateur de vitesse pour moteur alternatif est un convertisseur de fréquence "
        "(cf. définition de la fiche)."),
    "compatibilité électromagnétique": (["compatibilite-electromagnetique-cem"], "direct", "haute", False, ""),
    "Conversion et modulation de l'énergie électrique": ([], "rejet", "", False, "Couvert par le vocabulaire."),

    # --- M067 : protection des personnes (bac pro) -----------------------------------
    "Protection des personnes et des biens": ([], "rejet", "", False, "Couvert par le vocabulaire."),
    "schéma de liaison à la terre": (["mise-a-la-terre"], "sens", "haute", False,
        "Le schéma de liaison à la terre (régime de neutre) repose sur la mise à la terre."),
    "pré-actionneur": ([], "rejet", "", True, "Aucune fiche « préactionneur »."),
    "protection des personnes": ([], "rejet", "", True,
        "Aucune fiche « protection des personnes » ; les fiches disjoncteur/fusible ne couvrent "
        "pas la notion (pas de fiche différentiel ni habilitation)."),
}


def sans_accent(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def cle_normalisee(s: str) -> str:
    """Clé de comparaison : minuscules, sans accents, espaces normalisés."""
    return " ".join(sans_accent(s).lower().replace(" ", " ").split())


def decouper_vocabulaire(cellule: str) -> list[str]:
    """Découpe « Vocabulaire associé » sur les virgules situées hors parenthèses."""
    items, profondeur, courant = [], 0, ""
    for ch in cellule:
        if ch == "(":
            profondeur += 1
        elif ch == ")":
            profondeur -= 1
        if ch == "," and profondeur == 0:
            items.append(courant.strip())
            courant = ""
        else:
            courant += ch
    items.append(courant.strip())
    return [x for x in items if x and x != "—"]


def lire_matrice(chemin: Path) -> list[dict]:
    with chemin.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def occurrences(lignes: list[dict]) -> dict[str, dict]:
    """terme -> {'label':…, 'origine':'notion'|'vocabulaire', 'ids':[…]} (FAM19 exclue)."""
    occ: dict[str, dict] = {}
    for ligne in lignes:
        if ligne["ID_Famille"] == "FAM19":
            continue
        termes = [("notion", ligne["Notion (normalisée)"].strip())]
        termes += [("vocabulaire", v) for v in decouper_vocabulaire(ligne["Vocabulaire associé"])]
        for origine, label in termes:
            if not label:
                continue
            # Une clé « terme|Mxxx » l'emporte sur la clé générique (désambiguïsation).
            specifique = f"{label}|{ligne['ID_Ligne']}"
            cle = specifique if specifique in TABLE else label
            entree = occ.setdefault(cle, {"label": label, "origine": origine, "ids": []})
            if ligne["ID_Ligne"] not in entree["ids"]:
                entree["ids"].append(ligne["ID_Ligne"])
    return occ


def verifier(occ: dict[str, dict], slugs_wiki: set[str]) -> None:
    manquants = sorted(k for k in occ if k not in TABLE)
    if manquants:
        raise SystemExit("Termes de la matrice absents de la TABLE :\n  - " + "\n  - ".join(manquants))
    inutiles = sorted(k for k in TABLE if k not in occ)
    if inutiles:
        raise SystemExit("Entrées de la TABLE introuvables dans la matrice :\n  - " + "\n  - ".join(inutiles))
    inconnus = sorted({s for v in TABLE.values() for s in v[0]} - slugs_wiki)
    if inconnus:
        raise SystemExit("Slugs cités mais inexistants dans src/content/wiki :\n  - " + "\n  - ".join(inconnus))


def construire(occ: dict[str, dict], lignes: list[dict]) -> dict[str, dict]:
    """slug -> {matriceIds, cycles, familles, termes}."""
    par_id = {l["ID_Ligne"]: l for l in lignes}
    fiches: dict[str, dict] = {}
    for cle, info in occ.items():
        slugs, type_corr, _conf, _bl, _note = TABLE[cle]
        for slug in slugs:
            f = fiches.setdefault(slug, {"matriceIds": set(), "cycles": set(),
                                         "familles": set(), "termes": []})
            f["matriceIds"].update(info["ids"])
            f["termes"].append((info["label"], type_corr, info["ids"]))
            for mid in info["ids"]:
                f["cycles"].add(par_id[mid]["Cycle_scolaire_normalise"])
                f["familles"].add(par_id[mid]["ID_Famille"])
    for slug, f in fiches.items():
        if not f["matriceIds"]:
            raise SystemExit(f"{slug} : rattachement sans ligne de matrice (interdit).")
        inconnus = f["cycles"] - set(RANG)
        if inconnus:
            raise SystemExit(f"{slug} : niveau(x) hors référentiel {sorted(inconnus)}")
    return fiches


def niveau(f: dict) -> dict:
    cycles = sorted(f["cycles"], key=lambda c: RANG[c])
    return {
        "premiereApparition": cycles[0],
        "cycles": cycles,
        "familles": sorted(f["familles"]),
        "matriceIds": sorted(f["matriceIds"]),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--matrice", type=Path, default=MATRICE)
    ap.add_argument("--verifier", action="store_true", help="contrôles seuls, aucune écriture")
    ap.add_argument("--lot", help="écrit agents/changesets/<LOT>.jsonl avec les niveaux manquants")
    args = ap.parse_args()
    if args.lot == LOT_HISTORIQUE:
        raise SystemExit(f"{LOT_HISTORIQUE}.jsonl est le changeset historique : choisir un autre nom de lot.")

    lignes = lire_matrice(args.matrice)
    fiches_wiki = {p.stem: json.loads(p.read_text(encoding="utf-8")) for p in sorted(WIKI.glob("*.json"))}
    occ = occurrences(lignes)
    verifier(occ, set(fiches_wiki))
    fiches = construire(occ, lignes)

    # --- niveaux : à poser, déjà posés, en écart -------------------------------------
    ops, deja, ecarts = [], [], []
    for slug in sorted(fiches):
        n = niveau(fiches[slug])
        actuel = fiches_wiki[slug].get("niveau")
        if actuel == n:
            deja.append(slug)
            continue
        if actuel is not None:
            ecarts.append((slug, actuel.get("premiereApparition"), n["premiereApparition"]))
            continue
        termes = fiches[slug]["termes"]
        detail = " ; ".join(f"« {t} » ({', '.join(ids)})" for t, _typ, ids in sorted(termes))
        ops.append({
            "op": "set", "lot": args.lot or "?", "slug": slug, "field": "niveau", "old": None, "new": n,
            "why": f"Matrice curriculaire v2 : {detail}. Première apparition : {n['premiereApparition']}.",
        })

    # --- table périmée : un rejet que le corpus couvre désormais ----------------------
    formes = {}
    for slug, fiche in fiches_wiki.items():
        for forme in formes_d_une_fiche(fiche):
            formes.setdefault(forme, slug)
    perimees = []
    for cle, info in occ.items():
        slugs, type_corr, _c, _b, _n = TABLE[cle]
        if type_corr == "rejet":
            slug = formes.get(normaliser(info["label"]))
            if slug:
                perimees.append((info["label"], ", ".join(info["ids"]), slug))

    # --- rapport CSV -----------------------------------------------------------------
    rows = []
    for cle, info in occ.items():
        slugs, type_corr, conf, backlog, note = TABLE[cle]
        ids = ", ".join(info["ids"])
        if slugs:
            for slug in slugs:
                rows.append([info["label"], info["origine"], ids, slug, type_corr, conf, note])
        else:
            rows.append([info["label"], info["origine"], ids, "non rattaché", "rejet",
                         "backlog" if backlog else "hors périmètre", note])
    rows.sort(key=lambda r: (r[2], cle_normalisee(r[0]), r[3]))

    print(f"Termes de programme : {len(occ)} — fiches rattachées : {len(fiches)} / {len(fiches_wiki)}")
    print(f"Niveau déjà à jour : {len(deja)} — à poser : {len(ops)} — en écart : {len(ecarts)}")
    for slug, a, b in ecarts:
        print(f"  ÉCART        {slug} : niveau actuel {a}, la TABLE donne {b} (non modifié)")
    if perimees:
        print(f"TABLE périmée : {len(perimees)} terme(s) rejeté(s) alors qu'une fiche les couvre désormais")
        for label, ids, slug in sorted(perimees):
            print(f"  PÉRIMÉ       « {label} » ({ids}) -> fiche existante « {slug} »")
    couverts = {label for label, _ids, _slug in perimees}
    backlog = [occ[k]["label"] for k in occ
               if not TABLE[k][0] and TABLE[k][3] and occ[k]["label"] not in couverts]
    print(f"Termes de programme encore sans fiche (backlog) : {len(backlog)}")

    if args.verifier:
        # Bloquant en CI : seulement la cohérence de la TABLE (contrôlée plus haut).
        # Écarts et table périmée sont du travail à planifier, pas des erreurs.
        print("OK : TABLE cohérente avec la matrice et le wiki.")
        return 0

    RAPPORT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with RAPPORT_CSV.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(["Terme de programme", "Origine", "Lignes de matrice", "Slug retenu",
                    "Type de correspondance", "Confiance", "Commentaire"])
        w.writerows(rows)
    print(f"{RAPPORT_CSV.relative_to(RACINE)} : {len(rows)} ligne(s)")

    if args.lot:
        if not ops:
            print("Aucun niveau à poser : pas de changeset écrit.")
            return 0
        chemin = CHANGESETS / f"{args.lot}.jsonl"
        if chemin.exists():
            raise SystemExit(f"{chemin.relative_to(RACINE)} existe déjà : choisir un autre nom de lot.")
        chemin.write_text("".join(json.dumps(o, ensure_ascii=False) + "\n" for o in ops), encoding="utf-8")
        print(f"{chemin.relative_to(RACINE)} : {len(ops)} opération(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
