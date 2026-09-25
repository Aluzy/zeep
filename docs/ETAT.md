# État du projet Zeep

> Généré par `python3 scripts/etat_projet.py` — ne pas modifier à la main.

## Indicateurs de qualité

| Indicateur | Valeur |
|---|---|
| Fiches | 387 |
| Définitions de 25 à 60 mots | 204/387 (53 %) |
| Version simple, notions vues avant le lycée | 7/28 (25 %) |
| Version simple, toutes fiches | 187/387 (48 %) |
| Avec niveau scolaire | 79/387 (20 %) |
| Avec au moins une source précise (URL non racine) | 27/387 (7 %) |
| Relues par un contrôleur indépendant | 0/387 (0 %) |
| Validées par Alexandre | 0/387 (0 %) |
| Fiches secteur sans rappel de sécurité | 24 |

## Dette éditoriale (cliquet)

| Règle | Fiches en défaut | Base tolérée |
|---|---:|---:|
| Définition hors 25-60 mots (`definition_longueur`) | 183 | 183 |
| Balise HTML dans la définition (`definition_html`) | 3 | 3 |
| Notion vue avant le lycée (C1-C4) sans version simple (`version_simple_manquante_avant_lycee`) | 21 | 21 |
| Version simple hors 12-35 mots (`version_simple_longueur`) | 1 | 1 |
| Fiche liée au secteur sans rappel de sécurité (`securite_230v_absente`) | 24 | 24 |
| Source sans URL (`source_sans_url`) | 0 | 0 |
| Source pointant vers une page d'accueil (invérifiable) (`source_url_racine`) | 180 | 180 |
| Type de source hors liste (programme|reference|norme|manuel) (`source_type_hors_liste`) | 86 | 86 |
| « relu-ia » posé par un autre agent que le contrôleur (`relecture_non_independante`) | 197 | 197 |

## Backlog (ordre de priorité)

Lot suivant : `python3 scripts/prochain_lot.py --lot <LOT> [--file <file>] [--taille 20]`.

| File | Éléments | Premiers éléments |
|---|---:|---|
| `vs-avant-lycee` — Version simple manquante (notions vues avant le lycée) | 0 | — |
| `securite` — Sécurité 230 V, HTML, signalements graves | 31 | `alimentation-electrique`, `cablage-electrique`, `compteur-electrique`, `consommation-electrique`, `court-circuit`, `disjoncteur`, `domotique`, `electrocution` … |
| `niveaux` — TABLE des niveaux périmée (mapping_niveau.py) | 22 | `TABLE:Chaîne d'énergie`, `TABLE:asservissement`, `TABLE:caractéristique tension-courant`, `TABLE:chaîne d'information`, `TABLE:chaîne d'énergie`, `TABLE:constante de temps`, `TABLE:dipôle`, `TABLE:détecteur` … |
| `reecriture` — Réécriture : définition, sources, version simple | 315 | `ampere`, `amperemetre`, `atome`, `champ-electrique`, `champ-magnetique`, `charge-electrique`, `conductivite-electrique`, `coulomb` … |
| `creation` — Création : lexique attendu, puis termes de programme | 98 | `Admittance`, `Équations de Maxwell`, `Loi de Biot-Savart`, `Diagramme de Fresnel`, `Effet de peau`, `Ohm-mètre`, `Interconnexion européenne`, `Courbe de charge` … |

## Lots

| Lot | Titre | Date | Statut | Contrôleur | Fiches créées / modifiées |
|---|---|---|---|---|---|
| B1 | Les grandeurs de base | 2026-09-14 | termine | aucun | 0 / 0 |
| B2 | Sécurité et installation domestique | 2026-09-14 | termine | aucun | 0 / 0 |
| B3 | Le réseau : transport et distribution | 2026-09-14 | termine | aucun | 0 / 0 |
| B4 | Produire, stocker, facturer | 2026-09-14 | termine | aucun | 0 / 0 |
| B5 | Électronique analogique | 2026-09-14 | termine | aucun | 0 / 0 |
| B6 | Du silicium au calcul | 2026-09-14 | termine | aucun | 0 / 0 |
| B7 | Usages du quotidien : route, maison, lumière | 2026-09-15 | termine | aucun | 0 / 0 |
| J1-L2 | Robustesse du site | 2026-09-11 | termine | aucun | 0 / 0 |
| J1-L3 | Corrections éditoriales urgentes et grille de relecture | 2026-09-12 | termine | aucun | 0 / 0 |
| J2-L1 | Affichage du niveau scolaire, de la version simple et des sources | 2026-09-12 | termine | aucun | 0 / 0 |
| J2-L2 | Correspondance matrice curriculaire → fiches du wiki | 2026-09-12 | termine | aucun | 0 / 0 |
| J2-L4 | Lot 1 de nouvelles fiches : notions du tronc commun | 2026-09-12 | termine | aucun | 0 / 0 |
| J2-L5 | Liens retour : articles et projets qui citent une fiche | 2026-09-12 | termine | aucun | 0 / 0 |
| J3-L1 | Couverture du glossaire : outillage + 180 fiches | 2026-09-13 | termine | aucun | 0 / 0 |
| J4-CHAINE | Chaîne de production du contenu : backlog, missions, contrôle, validation, tableau de bord | 2026-09-25 | termine | aucun | 0 / 0 |
| J4-L0 | Cliquet de dette éditoriale, mapping des niveaux incrémental, modèle de rapport structuré | 2026-09-25 | termine | aucun | 0 / 0 |
| chantier-A-4-5 | Date, temps de lecture et sommaire de blog | 2026-09-13 | termine | aucun | 0 / 0 |
| chantier-A-6 | Liens contextuels dans les définitions du wiki | 2026-09-13 | termine | aucun | 0 / 0 |

## En cours

Missions sans rapport :
- `J4-L1.md` — redaction, 21 élément(s), file « vs-avant-lycee »

Brouillons de changeset :
- `J4-L1.jsonl` — 74 opération(s) sur 74 à remplir

## Lacunes remontées par les rapports

Notions sans fiche, absentes de `src/data/lexique-attendu.json`. Décision éditoriale : les ajouter à `attendu` (elles entrent alors dans la file `creation`) ou à `horsPerimetre` avec leur raison.

| Terme | Domaine | Vu dans |
|---|---|---|
| Récepteur électrique | A | J2-L4 (J2-L2 backlog) |
| Résistance interne | A | J2-L4 (J2-L2 backlog) |
| Courbe de charge d'une batterie | D | B7 (recharger-une-voiture-electrique) |
| Diagnostic électrique obligatoire | E | B2 (B2) |
| Disjoncteur de branchement | E | B2 (B2) |
| Règles de sécurité électrique | E | J2-L4 (J2-L2 backlog) |
| Repérage du tableau électrique | E | B2 (B2) |
| Schéma TT | E | B2 (B2) |
| Chaîne de puissance | F | J2-L4 (J2-L2 backlog) |
| KNX | H | B7 (B7) |
| Lampe | I | J2-L4 (J2-L2 backlog) |
| Signal électrique | K | J2-L4 (J2-L2 backlog) |
| Fonderie de semi-conducteurs | N | B6 (B6 article 1) |
| Porteur de charge majoritaire | N | B6 (B6 article 2) |
| Salle blanche | N | B6 (B6 article 1) |
| Zone de déplétion | N | B6 (B6 article 2) |
| Chaîne d'acquisition | S | J2-L4 (J2-L2 backlog) |
| George Boole | X | B6 (B6 article 3) |
| Guerre des courants | X | B1 (B1 article 2) |

## Décisions humaines remontées par les rapports

Suivi : issues GitHub étiquetées `decision`.

- **J1-L3** — Doublons processeur-cpu / microprocesseur, efficacite-energetique / rendement-energetique, conductivite-electrique / resistivite : fusionner ou différencier ?
- **J1-L3** — Format « Vu côté électricité / électronique » des fiches court-circuit, domotique, redresseur : décision de gabarit.
- **J2-L2** — Lois de Kirchhoff : première apparition en C4 ou en 2GT ?
- **J2-L4** — Correctif de slugify pour la ligature « œ » (point d'attention n° 1 du rapport).
- **J3-L1** — Doublons Tension électrique / Voltage, Intensité électrique / Ampérage, Court-circuit / Court-jus : à arbitrer.
- **J4-CHAINE** — Accès réseau des agents : l'environnement cloud utilisé pour ce lot bloque education.gouv.fr, eduscol.education.fr, electropedia.org et inrs.fr. Sans ces domaines autorisés, aucun lot de contenu ne peut respecter la règle « chaque source est ouverte avant d'être citée ».
- **J4-CHAINE** — Source « programme » automatique pour les fiches qui reçoivent un niveau : la matrice ne donne que la référence du BO (« BO n°24 du 11-6-2026 »), sans URL ; il faut d'abord une table référence BO -> URL du texte, vérifiée à la main.
- **J4-CHAINE** — Lacunes remontées par les anciens rapports (19, voir docs/ETAT.md) : les ajouter à lexique-attendu.json (attendu ou horsPerimetre) ?
- **J4-CHAINE** — Programmer un lot hebdomadaire automatique (backlog -> rédaction -> contrôle -> PR) une fois l'accès aux sources réglé ?
- **J4-L0** — Type de source « officiel » (86 fiches) : l'accepter (l'ajouter à TYPES_SOURCE dans scripts/dette.py et à AGENTS.md) ou le convertir en « reference » / « programme » ?
- **J4-L0** — Relecture jugée indépendante quand « par » contient « controleur » : convention à confirmer.
- **J4-L0** — Détection « secteur 230 V » par mots-clés (src/data/dette.json) : trier les 24 fiches signalées, exempter les faux positifs avec leur raison.

## Signalements de fiches douteuses

24 ouvert(s) sur 24 (`agents/donnees/signalements.json`) ; ils sont intégrés aux files `securite` et `reecriture`.
