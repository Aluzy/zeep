# État du projet Zeep

> Généré par `python3 scripts/etat_projet.py` — ne pas modifier à la main.

## Indicateurs de qualité

| Indicateur | Valeur |
|---|---|
| Fiches | 387 |
| Définitions de 25 à 60 mots | 296/387 (76 %) |
| Version simple, notions vues avant le lycée | 29/29 (100 %) |
| Version simple, toutes fiches | 211/387 (55 %) |
| Avec niveau scolaire | 89/387 (23 %) |
| Avec au moins une source précise (URL non racine) | 203/387 (52 %) |
| Relues par un contrôleur indépendant | 154/387 (40 %) |
| Validées par Alexandre | 31/387 (8 %) |
| Fiches secteur sans rappel de sécurité | 0 |

## Dette éditoriale (cliquet)

| Règle | Fiches en défaut | Base tolérée |
|---|---:|---:|
| Définition hors 25-60 mots (`definition_longueur`) | 91 | 91 |
| Balise HTML dans la définition (`definition_html`) | 0 | 0 |
| Notion vue avant le lycée (C1-C4) sans version simple (`version_simple_manquante_avant_lycee`) | 0 | 0 |
| Version simple hors 12-35 mots (`version_simple_longueur`) | 1 | 1 |
| Fiche liée au secteur sans rappel de sécurité (`securite_230v_absente`) | 0 | 0 |
| Source sans URL (`source_sans_url`) | 0 | 0 |
| Source pointant vers une page d'accueil (invérifiable) (`source_url_racine`) | 104 | 104 |
| Type de source hors liste (programme|reference|norme|manuel) (`source_type_hors_liste`) | 38 | 38 |
| « relu-ia » posé par un autre agent que le contrôleur (`relecture_non_independante`) | 111 | 111 |

## Backlog (ordre de priorité)

Lot suivant : `python3 scripts/prochain_lot.py --lot <LOT> [--file <file>] [--taille 20]`.

| File | Éléments | Premiers éléments |
|---|---:|---|
| `vs-avant-lycee` — Version simple manquante (notions vues avant le lycée) | 0 | — |
| `securite` — Sécurité 230 V, HTML, signalements graves | 0 | — |
| `niveaux` — TABLE des niveaux périmée (mapping_niveau.py) | 0 | — |
| `reecriture` — Réécriture : définition, sources, version simple | 182 | `chute-de-tension`, `electrification`, `ligne-basse-tension`, `ligne-haute-tension`, `ligne-moyenne-tension`, `poste-de-transformation`, `reseau-de-distribution`, `reseau-de-transport` … |
| `creation` — Création : lexique attendu, puis termes de programme | 95 | `Admittance`, `Équations de Maxwell`, `Loi de Biot-Savart`, `Diagramme de Fresnel`, `Effet de peau`, `Interconnexion européenne`, `Courbe de charge`, `Sélectivité` … |

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
| J4-L1 | Versions simples des notions des cycles 2 à 4 (21 fiches) | 2026-09-25 | termine | agent-controleur-J4-L1 | 0 / 21 |
| J4-L10 | Réécriture, domaine K (électronique analogique) — 20 des 30 fiches, partie 1/2 | 2026-09-27 | termine | agent-controleur-J4-L10 | 0 / 20 |
| J4-L11 | Réécriture, domaine K (électronique analogique) — 10 dernières fiches, partie 2/2 (fin du domaine K) | 2026-09-27 | termine | agent-controleur-J4-L11 | 0 / 11 |
| J4-L2 | Sécurité 230 V, définitions en HTML et signalements graves (16 fiches, partie 1 de la file « securite ») | 2026-09-25 | termine | agent-controleur-J4-L2 | 0 / 16 |
| J4-L3 | Sécurité 230 V et signalements graves (15 fiches, partie 2 de la file « securite ») | 2026-09-25 | termine | agent-controleur-J4-L3 | 0 / 15 |
| J4-L4 | TABLE des niveaux périmée : 22 entrées corrigées (mapping_niveau.py) | 2026-09-26 | termine | agent-controleur-J4-L4 | 0 / 10 |
| J4-L5 | Source « programme » pour les 10 fiches qui ont reçu un niveau en J4-L4 | 2026-09-27 | termine | agent-controleur-J4-L5 | 0 / 10 |
| J4-L6 | Réécriture, domaine A (électricité — fondamentaux et physique), 20 fiches | 2026-09-27 | termine | agent-controleur-J4-L6 | 0 / 24 |
| J4-L7 | Réécriture, domaine A (électricité — fondamentaux et physique), 20 fiches | 2026-09-27 | termine | agent-controleur-J4-L7 | 0 / 21 |
| J4-L8 | Réécriture, domaine A (électricité — fondamentaux et physique), 16 fiches — fin du domaine A | 2026-09-27 | termine | agent-controleur-J4-L8 | 0 / 16 |
| J4-L9 | Réécriture, domaine B (production d'électricité) — 20 fiches, domaine B complet | 2026-09-27 | termine | agent-controleur-J4-L9 | 0 / 20 |
| J5-S1 | Réécriture : sources précises de Batterie de traction | 2026-10-01 | termine | agent-controleur-J5-S1 | 0 / 1 |
| J5-S2 | Réécriture : sources précises (ADEME, RTE, Enedis...) pour 13 fiches | 2026-10-01 | termine | agent-controleur-J5-S2 | 0 / 13 |
| J5-S3 | Réécriture : sources précises (compteur Linky, délestage, heures creuses, puissance souscrite) | 2026-10-01 | termine | agent-controleur-J5-S3 | 0 / 4 |
| chantier-A-4-5 | Date, temps de lecture et sommaire de blog | 2026-09-13 | termine | aucun | 0 / 0 |
| chantier-A-6 | Liens contextuels dans les définitions du wiki | 2026-09-13 | termine | aucun | 0 / 0 |

## En cours

Missions des lots non intégrés au wiki :
- `J4-L5-controle.md` — controle, 10 élément(s)
- `J4-L5.md` — redaction, 10 élément(s), file « aucune (complément ponctuel demandé par Alexandre, hors backlog automatisé) »

Brouillons de changeset :
- aucun

## Lacunes remontées par les rapports

Notions sans fiche, absentes de `src/data/lexique-attendu.json`. Décision éditoriale : les ajouter à `attendu` (elles entrent alors dans la file `creation`) ou à `horsPerimetre` avec leur raison.

| Terme | Domaine | Vu dans |
|---|---|---|
| flux magnétique | A | J4-L7 (induction-electromagnetique, weber) |
| Potentiel électrique | A | J4-L1 (tension-electrique (notion retirée de la définition faute de fiche)) |
| Récepteur électrique | A | J2-L4 (J2-L2 backlog); J4-L1 (circuit-electrique (mot du programme de cycle 2 évité faute de fiche)) |
| Résistance interne | A | J2-L4 (J2-L2 backlog) |
| Courbe de charge d'une batterie | D | B7 (recharger-une-voiture-electrique) |
| système de gestion de batterie (BMS) | D | J5-S1 (batterie-de-traction) |
| Diagnostic électrique obligatoire | E | B2 (B2) |
| Disjoncteur de branchement | E | B2 (B2) |
| Masse (électricité) | E | J4-L2 (mise-a-la-terre (expliqué dans la définition faute de fiche)) |
| Règles de sécurité électrique | E | J2-L4 (J2-L2 backlog) |
| Repérage du tableau électrique | E | B2 (B2) |
| Schéma TT | E | B2 (B2) |
| Surcharge | E | J4-L2 (disjoncteur) |
| Surtension | E | J4-L3 (parafoudre) |
| Chaîne de puissance | F | J2-L4 (J2-L2 backlog) |
| KNX | H | B7 (B7) |
| Lampe | I | J2-L4 (J2-L2 backlog); J4-L1 (circuit-electrique, circuit-ferme, interrupteur) |
| Signal électrique | K | J2-L4 (J2-L2 backlog) |
| Fonderie de semi-conducteurs | N | B6 (B6 article 1) |
| Porteur de charge majoritaire | N | B6 (B6 article 2) |
| Salle blanche | N | B6 (B6 article 1) |
| Zone de déplétion | N | B6 (B6 article 2) |
| Onde porteuse | R | J4-L2 (modulation) |
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
- **J4-L1** — Le mot « relais » a été retiré de la définition d'actionneur : le programme de technologie de 2024 range le relais dans la chaîne d'énergie (distribuer), pas parmi les actionneurs. La fiche relais-electronique le présente encore comme un actionneur : à trancher.
- **J4-L10** — 8 opérations « synonymes » du brouillon (circuit-analogique, composant-electronique, diode, electronique, filtre-electronique, filtre-passe-bande, filtre-passe-bas, filtre-passe-haut) retirées du changeset : aucune forme équivalente réelle trouvée pour ces termes, décision seul de ne rien fabriquer (AGENTS.md §3 point 8).
- **J4-L10** — public.iutenligne.net et www.iutenligne.net (sous-domaines du même site) répondent de façon intermittente depuis cet environnement (« Connection reset by peer » sur certaines requêtes, 200 à la requête suivante) — 6 sources du lot en dépendent ; contenu vérifié à chaque fois qu'une réponse est obtenue, mais l'accès n'est pas garanti à 100 %, contrairement à Larousse et education.gouv.fr qui ont répondu de façon stable.
- **J4-L11** — 3 opérations « synonymes » du brouillon retirées (gain-electronique, relais-electronique, transistor) : aucune forme équivalente réelle trouvée (« gain » et « relais » seuls sont trop ambigus dans le dictionnaire pour servir de synonymes sans introduire de fausses correspondances ; « transistor » n'a pas d'abréviation d'usage) — décision seule de ne rien fabriquer (AGENTS.md §3 point 8).
- **J4-L11** — potentiometre, relais-electronique et « relais » (Larousse) n'offrent pas d'ancre par sens (contrairement à diode/Zener/Schottky/DEL en J4-L10, qui avaient des « Locutions » ancrées) : la page cite plusieurs sens sans identifiant séparé pour chacun. URL de la page + numéro de sens précisé dans « Sources réellement ouvertes » ci-dessous, comme pour la fiche `diode` en J4-L10 (sens 2, sans ancre).
- **J4-L2** — consommation-electrique : le programme de cycle 4 (p. 103) demande un calcul de consommation d'énergie électrique, mais la matrice ne cite la notion qu'au lycée (M016, M019) : niveau 2GT à revoir avec la décision sur la « première apparition » (issue « Définition de première apparition »).
- **J4-L2** — Format « Vu côté électricité / Vu côté électronique » (court-circuit, domotique) : remplacé par une définition unique ; à confirmer (redresseur, traité en J4-L3, suivra la même règle).
- **J4-L3** — Niveaux en retard sur les programmes : panneau-photovoltaique (éléments photovoltaïques en 6e, programme de cycle 3 de 2026) et schema-electrique (schéma normalisé dès le cycle 3) sont au niveau lycée faute de ligne dans la matrice ; triphase n'a pas de niveau car l'entrée « monophasé/triphasé » de la TABLE de mapping_niveau.py est rejetée alors que les fiches existent. À traiter avec le lot « niveaux » et la décision sur la « première apparition ».
- **J4-L3** — valeur-efficace : aucune source de référence ouverte ne donne la définition par l'échauffement équivalent (la ressource Éduscol trouvée l'assimile à tort à la valeur moyenne) ; la phrase existante, exacte, est conservée et seule la partie « 230 V = valeur efficace » est sourcée (INRS ED 6345). Une source de référence (manuel, norme) reste à ajouter.
- **J4-L4** — Écart loi-des-mailles / loi-des-noeuds : niveau actuel C4 (matriceIds M009, M014, M033, M034, posé par J2-L2), la TABLE recalculée à partir de la seule ligne M014 (« Loi des mailles et des nœuds ») donne 2GT. Rejoint l'issue « Définition de première apparition » (Lois de Kirchhoff C4 ou 2GT ?, Aluzy/zeep#27) : la ligne M009 ne cite les lois qu'au travers du terme combiné « loi des nœuds/mailles », resté rejeté (aucune fiche « lois de Kirchhoff »), donc non compté par le calcul actuel. Trancher revient à décider si on relie ce terme combiné aux deux fiches (auquel cas C4 est confirmé) ou si on laisse la TABLE recalculée l'emporter (2GT).
- **J4-L4** — Écarts caracteristique-tension-courant, chaine-d-energie, chaine-d-information, dipole : même niveau (premiereApparition inchangé) mais matriceIds enrichis par ce lot (le calcul relie maintenant plus de lignes de la matrice au même terme). Aucune contradiction : à absorber en relançant mapping_niveau.py sans --lot pour information, aucune décision requise.
- **J4-L5** — arrete_sti2d_ensemble.pdf et le programme SI utilisés dans ce lot sont hébergés sur snes.edu (miroir syndical), les pages education.gouv.fr/bo/19/SpecialN correspondantes étant bloquées (403) depuis cet environnement. Contenu vérifié conforme, mais à remplacer par une source officielle directe si l'accès s'améliore.
- **J4-L5** — loi-de-coulomb cite un miroir académique (ac-aix-marseille.fr) pour le même motif (BO spécial n°1 du 22 janvier 2019 inaccessible en direct).
- **J4-L6** — conductivite-electrique : aucune entrée de dictionnaire ou de programme ne définit spécifiquement la « conductivité électrique » (Larousse ne définit que la « conductibilité », notion générale chaleur/électricité) ; la source retenue est donc générale, à améliorer si une source plus précise (norme, manuel de physique) est trouvée.
- **J4-L6** — resistivite (hors lot) : le signalement J1-L3 §2 n°13 portait sur une circularité mutuelle entre conductivite-electrique et resistivite ; seule la première est corrigée dans ce lot (resistivite n'est pas dans les 20 éléments) — à traiter par un prochain lot de la file « reecriture ».
- **J4-L7** — pont-diviseur-de-courant et pont-diviseur-de-tension : aucun document officiel (programme, norme) définissant précisément ces deux montages n'a été trouvé accessible ; la source retenue est un cours d'électricité de l'IUT en ligne (plateforme nationale du réseau des IUT, type « manuel »), qui donne les formules mais pas une définition rédigée du montage lui-même — à améliorer si une source de programme plus précise est trouvée.
- **J4-L7** — conductivite-electrique/resistivite (hors lot, rappel J4-L6) : signalement J1-L3 §2 n°13 encore ouvert, aucune des deux fiches n'est dans ce lot.
- **J4-L8** — theoreme-de-millman/norton/superposition/thevenin : comme pour pont-diviseur-de-tension/courant en J4-L7, aucun document de programme officiel précis n'a été trouvé pour ces quatre théorèmes ; source retenue : le chapitre 7 du même cours de l'IUT en ligne (M. Piou), qui les énonce formellement (type « manuel »).
- **J4-L8** — resistivite/conductivite-electrique : signalement J1-L3 §2 n°13 refermé par ce lot (retiré de agents/donnees/signalements.json) — voir détail ci-dessous, décision prise seul, à confirmer par relecture indépendante ou Alexandre.
- **J4-L9** — alternateur/production-d-electricite : signalements J1-L3 §2 n°8 et n°10 retirés de agents/donnees/signalements.json par ce lot (motif exact — confusion énergie/courant — complètement levé par la nouvelle définition) ; retrait confirmé par le contrôleur indépendant agent-controleur-J4-L9.
- **J4-L9** — Type « manuel » pour connaissancedesenergies.org (11 sources) : le contrôleur note que le site est édité par Selectra SAS (entreprise commerciale de comparaison de fournisseurs d'énergie, comité scientifique depuis fin 2024), pas un organisme de référence institutionnel au sens strict d'AGENTS.md §3. Contenu cité vérifié factuel et conforme par le contrôleur, mais décision humaine à prendre sur son usage récurrent comme source de type « manuel ».
- **J5-S1** — Accepter FranceTerme (culture.fr, Journal officiel) comme source de type reference, hors liste de conversion décidée.
- **J5-S1** — Définition modifiée alors que la mission ne demandait que les sources : retrait de la mention du refroidissement, faute de source ouverte.
- **J5-S2** — Les domaines ecologie.gouv.fr, economie.gouv.fr et cea.fr ne figurent pas dans la table de conversion décidée : ils ont été typés « reference » (organismes publics) ; à confirmer.
- **J5-S2** — Légifrance (article L441-2 du code de la consommation, obsolescence programmée) renvoie 403 à l'ouverture : aucune source de type « norme » n'a pu être citée pour cette fiche.
- **J5-S3** — Accepter des sources Enedis (type reference) pour délestage, faute de page RTE précise ouverte ?
- **J5-S3** — Compteur Linky : la mention « pilotage du réseau » n'est appuyée qu'indirectement ; la garder ou la reformuler ?
- **J5-S3** — Puissance souscrite : « se paie par un abonnement plus élevé » n'est confirmé par aucune page ouverte ; garder ou retirer ?

## Signalements de fiches douteuses

6 ouvert(s) sur 23 (`agents/donnees/signalements.json`) ; ils sont intégrés aux files `securite` et `reecriture`.
