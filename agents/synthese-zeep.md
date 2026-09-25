# Synthèse des rapports — projet Zeep

Sep 25, 2026 · @Alexandre

## Vue d'ensemble

Zeep est un wiki + blog + projets DIY sur l'électricité et l'électronique, en français, destiné en priorité au public scolaire (CE1 à la terminale, parents, enseignants). Le dépôt GitHub est la source de vérité du contenu ; le site est un Astro 4 statique déployé sur GitHub Pages. Un ensemble d'agents IA y travaillent par lots, chacun documenté par un rapport dans `agents/rapports/`.

Cette synthèse couvre les 15 rapports de lot du dossier, produits entre le 11 et le 20 septembre 2026, plus la fiche de cadrage de la série blog B1–B10 :

| Vague | Lots | Objet |
| --- | --- | --- |
| Jour 1 | J1-L2, J1-L3 | Robustesse technique du site, corrections éditoriales urgentes, grille de relecture |
| Jour 2 | J2-L1, J2-L2, J2-L4, J2-L5 | Affichage des niveaux scolaires, correspondance avec la matrice curriculaire, 10 nouvelles fiches, liens retour blog/DIY → wiki |
| Jour 3 | J3-L1 (+ L2, L3) | Audit et comblement massif de la couverture du glossaire (+87 % de fiches) |
| Chantier A | étapes 4-5, étape 6 | Date/temps de lecture/sommaire sur le blog, liens contextuels dans les définitions du wiki |
| Série blog | B1 à B10 (série complète) | 40 articles publiés (vérifié sur le site) ; rapports de lot manquants pour B8, B9, B10 |

**État du dépôt à l'issue des lots couverts** : 387 fiches wiki et 44 articles de blog, confirmés sur le site en production (aluzy.github.io/zeep) le 25/09/2026. Le blog est passé de 7 articles à 44 : les 40 articles de la série B1–B10 (série désormais complète, vérifiée sur le site) plus les 4 articles antérieurs à la série.

## Jour 1 — fondations

### J1-L2 — Robustesse du site

Un script `rename_slug.py` a été écrit pour renommer proprement un slug (fiche wiki + tous ses liens croisés dans le wiki, le blog et les projets DIY) et appliqué à 5 fiches pour uniformiser la convention de slug (ex. `plaque-d-essai-breadboard`). Les gabarits Astro ont été durcis : un lien wiki cassé fait désormais échouer le build au lieu d'être silencieusement ignoré, les éléments provisoires ("illustration à venir", liens vidéo vides) sont masqués plutôt qu'affichés en placeholder, et les compteurs de la page d'accueil (nombre de fiches, de domaines) sont devenus dynamiques au lieu d'être écrits en dur. Le README a été réécrit. Validation avant/après : 13 erreurs → 0.

### J1-L3 — Corrections éditoriales urgentes et grille de relecture

Lot repris après l'interruption d'un premier agent : son changeset (7 fiches sensibles — court-jus, électricité, voltage, ampérage, résistance, triac, mosfet) a été relu de façon critique, corrigé (une confusion électricité/énergie notamment) et complété de sources vérifiées. Une **grille de relecture à 12 critères** (`docs/grille-relecture.md`) a été produite pour outiller les lots suivants. Le balayage des 197 fiches existantes a repéré **20 fiches douteuses** (confusions électricité/énergie, circularités, absence de rappel de sécurité sur des fiches 230 V) signées mais non corrigées — matière pour un futur lot. Constat le plus large : **184 fiches sur 197 faisaient moins de 25 mots**, ce qui a montré que la règle éditoriale était en fait un chantier de réécriture quasi complet, pas un simple garde-fou.

## Jour 2 — niveaux scolaires, nouvelles fiches, maillage

### J2-L1 — Affichage des nouveaux champs

Pose l'affichage (gabarits + styles) des champs `niveau`, `versionSimple`, `sources` et `relecture` sur la fiche wiki — quatre blocs entièrement conditionnels, car au moment du lot aucune fiche ne les portait encore. Les filtres de domaine de l'index wiki n'affichent plus que les domaines peuplés.

### J2-L2 — Correspondance matrice curriculaire → fiches

Rapprochement méthodique des 251 termes de la matrice des programmes scolaires avec les 197 fiches existantes : **69 fiches** reçoivent un niveau scolaire justifié (`premièreApparition`, ligne de matrice à l'appui), **155 termes** de programme restent sans fiche correspondante — dont 72 identifiés comme un véritable backlog de rédaction (loi d'Ohm, effet Joule, dipôle, oscilloscope, lois de Kirchhoff, etc.), classure de priorité haute/moyenne.

### J2-L4 — 10 nouvelles fiches du tronc commun

Rédaction de 10 fiches parmi les termes « priorité haute » repérés par J2-L2 : loi d'Ohm, dipôle, loi des nœuds, loi des mailles, chaîne d'énergie, chaîne d'information, effet Joule, oscilloscope, détecteur, caractéristique tension-courant. Chacune sourcée, rattachée à la matrice, et auto-contrôlée contre les 12 critères de la grille de relecture (toutes « conformes », deux avec réserve signalée).

### J2-L5 — Liens retour (backlinks)

Le maillage n'allait que dans un sens (article/projet → fiche). Un index inversé (`src/lib/backlinks.ts`) ajoute sur chaque fiche wiki deux blocs « Articles qui en parlent » et « Projets qui l'utilisent », calculés au build à partir des `related` existants — 23 fiches sur 197 en bénéficiaient à l'issue du lot, faute d'un blog encore fourni.

## Jour 3 — audit et comblement de la couverture (le lot le plus structurant)

Le glossaire avait franchi 200 fiches sans page pour le farad, le coulomb, le henry, le hertz ni le joule, alors que les fiches Condensateur, Charge électrique, Bobine et Fréquence existaient déjà. Ce lot diagnostique **six causes structurelles** à ce phénomène (taxonomie utilisée comme étiquette et non comme cible, mapping matrice → fiche à sens unique, règles éditoriales qui évitent de nommer les unités, découverte de liens purement endogène, validation qui contrôle la conformité mais jamais la couverture, absence de champ de synonymes) et les ferme une par une.

**Outillage créé** : `scripts/audit_couverture.py` (audite les termes de programme sans fiche, l'effectif par domaine face à un plancher, le lexique de référence, la qualité du maillage), `src/data/couverture.json` (planchers par domaine), `src/data/lexique-attendu.json` (261 entrées de vocabulaire attendu), et un nouveau champ `synonymes` sur chaque fiche. Cet audit tourne désormais en CI, avant le build.

**Contenu produit** : **180 fiches nouvelles** (unités SI, lois et théorèmes, régime alternatif, composants, semi-conducteurs, logique numérique, embarqué et protocoles, sécurité électrique, mesure, énergie et réseau, et les cinq domaines jusque-là quasi vides — mobilité, domotique, audio, éco-conception, histoire/métiers) et **50 fiches existantes** enrichies de synonymes.

**Bilan chiffré** : 207 → 387 fiches (+87 %), 984 → 2 546 liens (+159 %), les 24 domaines de la taxonomie sont désormais tous au-dessus de leur plancher.

**Point de vigilance majeur** : les 180 fiches sont toutes en statut `relu-ia`, jamais `valide` (seul Alexandre peut poser ce statut) ; priorité de relecture humaine suggérée sur les fiches de sécurité (électrisation, électrocution, habilitation, consignation, différentiel, régimes de neutre).

## Chantier A — expérience de lecture

### Étapes 4-5 — Date, temps de lecture, sommaire de blog

Ajout d'un champ `date` au schéma du blog (renseigné sur les 7 articles existants, en partie deviné depuis l'historique Git faute de date de publication fiable — signalé pour confirmation). Affichage en tête d'article de la date et d'un temps de lecture estimé, plus un sommaire latéral généré depuis les titres, avec mise en surbrillance de la section lue (via `IntersectionObserver`, dégradation silencieuse si l'API est absente) et passage en bloc statique sur mobile.

### Étape 6 — Liens contextuels dans les définitions du wiki

Les mots d'une définition de fiche wiki qui désignent une notion traitée par un article de blog deviennent cliquables, calculés au rendu (le JSON des fiches n'est jamais touché). Règle de prudence assumée : en cas de doute (formes tronquées, ambiguïté entre deux fiches, mot de moins de 4 lettres), **pas de lien** plutôt qu'un lien hasardeux. À l'issue du lot : 121 liens sur 88 des 207 fiches d'alors — un vocabulaire liable encore restreint (31 termes) faute d'un blog suffisamment fourni, appelé à grossir avec la série B1–B10.

## Série blog B1–B10

Cadrée le 13/09/2026 : 10 lots de 4 articles (40 au total, dont 3 réécritures d'articles existants trop courts), un agent par lot, pour couvrir les 24 domaines de la taxonomie et faire passer le nombre de fiches wiki citées par un article de 33 à environ 250. Contrat de sortie strict par article : 800–1300 mots, 6 à 12 fiches wiki en `related` (le sujet en premier, l'ordre a un effet réel sur les liens du wiki), au moins 2 sources réellement ouvertes et lues, vocabulaire officiel (« tension » pas « voltage »), rappel de sécurité systématique sur tout sujet 230 V, aucune formule mathématique, aucune fiche wiki modifiée.

**Les 10 lots sont livrés** (40 articles, vérifié sur le site en production) :

| Lot | Thème | Domaine(s) |
| --- | --- | --- |
| B1 | Les grandeurs de base (tension, courant alternatif, multimètre, unités) | A, X |
| B2 | Sécurité et installation domestique (différentiel, terre, tableau, section de câble) | E |
| B3 | Le réseau : transport et distribution (THT, mono/triphasé, 50 Hz, poste source) | C |
| B4 | Produire, stocker, facturer (mix électrique, STEP, photovoltaïque, facture) | B, D, J |
| B5 | Électronique analogique (pont diviseur, condensateur, audio, diodes) | K, T |
| B6 | Du silicium au calcul (circuit intégré, jonction PN, portes logiques, binaire) | N, L |
| B7 | Usages du quotidien (recharge VE, freinage régénératif, éclairage LED, domotique) | G, H, I |
| B8 | Puissance, moteurs, automatismes (PWM, choix d'un moteur, variateur, asservissement) | M, F, P |
| B9 | Embarqué, objets connectés et radio (Arduino/Raspberry/ESP32, I2C/SPI/UART, LoRa/Zigbee/Wi-Fi) | O, Q, R |
| B10 | Atelier : fabriquer, mesurer, faire durer (prototypage, instruments de mesure, CEM, obsolescence) | V, S, U, W |

Tous ces lots affichent **0 erreur** de validation et **0 fiche wiki modifiée**, avec des sources systématiquement ouvertes et lues avant citation. Chaque rapport signale, sans les créer (hors périmètre), les notions rencontrées en rédigeant mais encore sans fiche wiki — matière pour un futur lot de contenu.

**Anomalie constatée** : les articles des lots B8, B9 et B10 sont bien publiés (vérifié sur le site et dans les fichiers du dépôt), mais **aucun rapport de lot** `agents/rapports/B8.md`, `B9.md` ou `B10.md` n'existe dans le dépôt — seuls B1 à B7 en ont un. Sources, points d'attention et notions manquantes signalées pour ces trois lots restent donc introuvables. À vérifier : rapports écrits mais non commités, ou lots livrés sans rapport.

## Décisions à trancher par Alexandre

| Sujet | Détail | Origine |
| --- | --- | --- |
| Fiche « Court-jus » | La définition dit désormais qu'un court-jus n'est pas une panne de courant, mais le titre affiché reste « Court-jus (panne de courant) » : la fiche se contredit. Renommer (impossible par changeset, casse l'URL) ou fusionner avec `court-circuit` ? | J1-L3 — signalé comme le point le plus urgent |
| Doublons éditoriaux | *Tension électrique*/*Voltage*, *Intensité électrique*/*Ampérage*, *Court-circuit*/*Court-jus* : deux fiches proches, renommage interdit hors mission dédiée | J3-L1 |
| Statut de relecture | `validate_content.py` ne compte comme « relues » que le statut `relu`, alors qu'AGENTS.md et les agents utilisent `relu-ia`/`valide` : incohérence à aligner | J1-L2, J1-L3 |
| Bornes de la version simple | Fiche de mission : 8–60 mots ; AGENTS.md §3 : 12–35 mots. Écart volontaire (script en garde-fou large, grille en règle stricte) à trancher | J2-L1 |
| Ligature « œ » dans les slugs | `slugify` casse la ligature (« nœuds » → slug illisible) ; correctif proposé dans `zeeplib.py` pour permettre plus tard de retypographier « Loi des nœuds » sans casser l'URL | J2-L4 |
| Première apparition des lois de Kirchhoff | Classées en C4 (cycle 4) plutôt qu'en 2de GT comme suggéré initialement : à confirmer, sinon retirer la version simple des deux fiches concernées | J2-L4 |
| Priorité de relecture humaine | 180 fiches créées en J3 sont en `relu-ia`, jamais `valide` ; les fiches de sécurité (électrisation, habilitation, différentiel…) sont à relire en priorité | J3-L1 |
| 20 fiches douteuses non corrigées | Confusions électricité/énergie, circularités (`conductivite-electrique`↔`resistivite`), fiches 230 V sans rappel de sécurité | J1-L3 (liste détaillée dans le rapport) |

## Chantiers restants

- **Série blog** : la série est en fait complète (40 articles publiés, vérifié sur le site) ; il manque seulement les rapports de lot B8, B9 et B10 dans le dépôt, à retrouver ou reconstituer.
- **J4 — niveaux scolaires** : rattacher les 180 fiches créées en J3 à la matrice curriculaire, et traiter les 149 termes de programme encore sans fiche.
- **J5 — version simple et sources** : 200 fiches sans version simple (couverture 48 %, cible 60 %) et 190 sans source (51 %, cible 90 %).
- **J6 — maillage** : 17 fiches avec moins de 3 liens.
- **Lexique restant** : 47 entrées attendues encore à écrire (Admittance, Maxwell, Biot-Savart, ainsi que des fiches biographiques — Volta, Ampère, Faraday, Tesla, Edison — repérées comme lacune dès le lot B1).
- **Affichage** : le niveau scolaire n'est visible que sur la fiche elle-même, pas encore sur l'index ni via un filtre par niveau ; les liens contextuels du chantier A pourraient s'étendre à la version simple des fiches.
- **Doublons conceptuels** à arbitrer (hors renommage) : `processeur-cpu`/`microprocesseur`, `efficacite-energetique`/`rendement-energetique`, `conductivite-electrique`/`resistivite`.
- **CI** : intégrer `verifie_liens_retour.py` (J2-L5) à la CI existante.
- **Projets DIY** : seulement 3 à ce jour, alors que plusieurs articles de la série blog (B5, B9, B10) appelleraient naturellement un projet associé — à planifier comme série distincte.
