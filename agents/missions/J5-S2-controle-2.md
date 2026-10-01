---
lot: J5-S2
role: controle
date: 2026-10-01
changeset: agents/changesets/J5-S2.jsonl
elements: ["borne-de-recharge", "hydrogene", "indice-de-reparabilite", "pile-a-combustible", "terres-rares", "thermostat-connecte"]
---

# Contrôle du lot J5-S2 — passe 2

6 fiche(s), 25 opération(s) du rédacteur (changeset non encore appliqué).

## Consignes du contrôleur

Tu es le **contrôleur** du lot J5-S2. Tu n'as pas participé à la rédaction et tu ne la vois qu'à
travers ce document : les justifications du rédacteur sont volontairement absentes. Tu vérifies
chaque fiche contre les **12 critères** de `docs/grille-relecture.md` (lis-la en entier d'abord).

1. **Ouvre chaque URL de source** et vérifie qu'elle appuie la définition. Une source que tu ne
   peux pas ouvrir, imprécise (page d'accueil) ou qui n'appuie pas l'affirmation = critère 8 en échec.
2. Une fiche est **conforme** si les 12 critères passent. Dans `agents/changesets/J5-S2-controle.jsonl`, remplace alors
   `"__A_REMPLIR__"` de `new` par
   `{"date": "2026-10-01", "par": "agent-controleur-J5-S2", "statut": "relu-ia"}` et `why` par
   « Relue selon la grille (12 critères) ».
3. Une fiche **refusée** : supprime sa ligne dans `agents/changesets/J5-S2-controle.jsonl`, et note les critères en échec. Tu ne
   réécris pas la fiche : le rédacteur la corrige (nouvelle passe de contrôle) ou la retire du lot.
   Si le défaut porte sur une fiche hors lot, ajoute-la à `agents/donnees/signalements.json`.
4. Écris tes verdicts dans la section « Relecture (rempli par le contrôleur) » de
   `agents/rapports/J5-S2.md`, une ligne par fiche : critères en échec, décision.
5. Vérifie : `python3 scripts/apply_changeset.py agents/changesets/J5-S2.jsonl agents/changesets/J5-S2-controle.jsonl --dry-run`.
   Tu ne poses **jamais** `"statut": "valide"` (réservé à Alexandre).


## Fiches à contrôler

### 1. Borne de recharge — `borne-de-recharge`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (30 mots) :
> Équipement qui délivre l'énergie à un véhicule électrique en dialoguant avec lui pour ajuster le courant. La recharge lente se fait en alternatif, la recharge rapide directement en courant continu.

**Définition — après** (43 mots) :
> Équipement raccordé à une alimentation électrique qui permet de recharger la batterie d'un véhicule électrique, avec une puissance allant de la recharge normale à la haute puissance. À domicile, son installation se confie à un professionnel qualifié : on n'y intervient pas soi-même.

**Sources après** (à ouvrir une par une) :
- [Ministère de la Transition écologique — Développer les bornes de recharge pour véhicules électriques](https://www.ecologie.gouv.fr/politiques-publiques/developper-bornes-recharge-vehicules-electriques) — type `reference`
- [Enedis — Guide pratique pour recharger sa voiture électrique](https://www.enedis.fr/sites/default/files/documents/pdf/guide-pratique-pour-recharger-sa-voiture-electrique.pdf) — type `reference`

**Fiches liées après** : `batterie-de-traction`, `courant-alternatif`, `courant-continu`, `installation-electrique`, `vehicule-electrique`

```
fiche : borne-de-recharge
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 2. Hydrogène — `hydrogene`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (32 mots) :
> Gaz produit par électrolyse de l'eau à partir d'électricité, stockable puis reconverti en courant dans une pile à combustible. Il offre un stockage de longue durée, au prix d'un rendement global modeste.

**Définition — après** (51 mots) :
> Gaz très léger qui sert de vecteur d'énergie : il permet de stocker et de transporter de l'énergie. On le produit surtout à partir de gaz naturel, ou par électrolyse de l'eau avec de l'électricité ; une pile à combustible peut ensuite en tirer de l'énergie électrique, avec des pertes importantes.

**Sources après** (à ouvrir une par une) :
- [RTE — Hydrogène vert : mythe ou réalité ?](https://www.rte-france.com/bases-electricite/production-electricite/hydrogene-vert-mythe-ou-realite) — type `reference`
- [ADEME — Favorisez les solutions hydrogène renouvelable et bas carbone](https://agirpourlatransition.ademe.fr/collectivites/favorisez-solutions-hydrogene-bas-carbone-renouvelable) — type `reference`
- [CEA — L'hydrogène (chapitre 3 : production)](https://www.cea.fr/comprendre/Pages/energies/renouvelables/hydrogene.aspx?Type=Chapitre&numero=3) — type `reference`
- [ADEME — Décarbonez avec l'hydrogène renouvelable et bas carbone](https://agirpourlatransition.ademe.fr/entreprises/conseils/transport-entreposage/transport-durable/hydrogene) — type `reference`

**Fiches liées après** : `electrolyse`, `energie-renouvelable`, `pile-a-combustible`, `stockage-d-energie`

```
fiche : hydrogene
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 3. Indice de réparabilité — `indice-de-reparabilite`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Version simple — avant** (18 mots) :
> Cette note dit si un appareil sera facile à réparer. Plus elle est haute, plus l'objet durera longtemps.

**Version simple — après** (24 mots) :
> Cette note sur 10 dit si un appareil sera facile à réparer. Plus elle est haute, plus il est facile de le faire réparer.

**Sources après** (à ouvrir une par une) :
- [Ministère de l'Économie — Tout savoir sur l'indice de réparabilité](https://www.economie.gouv.fr/particuliers/mes-droits-conso/bien-consommer/tout-savoir-sur-lindice-de-reparabilite) — type `reference`
- [Ministère de la Transition écologique — Durée de vie des produits](https://www.ecologie.gouv.fr/politiques-publiques/duree-vie-produits) — type `reference`
- [ADEME — Acheter des appareils électriques et électroniques faits pour durer](https://agirpourlatransition.ademe.fr/particuliers/mieux-consommer/electromenager/appareils-electriques-electroniques-durables) — type `reference`

**Fiches liées après** : `composant-electronique`, `eco-conception`, `obsolescence-programmee`, `recyclage-des-dechets-electroniques-deee`

```
fiche : indice-de-reparabilite
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 4. Pile à combustible — `pile-a-combustible`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (27 mots) :
> Générateur qui produit de l'électricité par réaction entre l'hydrogène et l'oxygène, en ne rejetant que de l'eau. Elle alimente certains véhicules lourds et des installations de secours.

**Définition — après** (33 mots) :
> Générateur qui produit de l'électricité par réaction entre l'hydrogène et l'oxygène, en dégageant de l'eau et de la chaleur. Elle alimente certains véhicules, notamment lourds, ainsi que des appareils portables et des bâtiments.

**Version simple — avant** (16 mots) :
> Cette pile fabrique de l'électricité à partir d'hydrogène et d'air, et ne rejette que de l'eau.

**Version simple — après** (20 mots) :
> Cette pile fabrique de l'électricité à partir d'hydrogène et d'air, et rejette seulement de l'eau et un peu de chaleur.

**Sources après** (à ouvrir une par une) :
- [CEA — L'hydrogène (chapitre 5 : la pile à combustible)](https://www.cea.fr/comprendre/Pages/energies/renouvelables/hydrogene.aspx?Type=Chapitre&numero=5) — type `reference`
- [ADEME — Favorisez les solutions hydrogène renouvelable et bas carbone](https://agirpourlatransition.ademe.fr/collectivites/favorisez-solutions-hydrogene-bas-carbone-renouvelable) — type `reference`
- [ADEME — Décarbonez avec l'hydrogène renouvelable et bas carbone](https://agirpourlatransition.ademe.fr/entreprises/conseils/transport-entreposage/transport-durable/hydrogene) — type `reference`

**Fiches liées après** : `hydrogene`, `pile-electrique`, `stockage-d-energie`, `vehicule-electrique`

```
fiche : pile-a-combustible
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 5. Terres rares — `terres-rares`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Version simple — avant** (19 mots) :
> Certains métaux rares sont indispensables aux aimants et aux composants. Les extraire pollue, et peu de pays en produisent.

**Version simple — après** (28 mots) :
> Ces métaux servent dans les aimants des moteurs et des éoliennes. Ils ne sont pas vraiment rares, mais presque tous viennent d'un seul pays et les extraire pollue.

**Sources après** (à ouvrir une par une) :
- [ADEME — Terres rares, énergies renouvelables et stockage d'énergies](https://librairie.ademe.fr/energies-renouvelables-reseaux-et-stockage/492-terres-rares-energies-renouvelables-et-stockage-d-energies.html) — type `reference`
- [ADEME — Avis : quels leviers pour une transition énergétique robuste face à la dépendance en matériaux ?](https://www.ademe.fr/presse/communique-national/avis-de-lademe-quels-leviers-pour-une-transition-energetique-robuste-face-a-la-dependance-en-materiaux/) — type `reference`

**Fiches liées après** : `composant-electronique`, `eco-conception`, `eolienne`, `moteur-electrique`, `moteur-synchrone`, `recyclage-des-dechets-electroniques-deee`

```
fiche : terres-rares
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 6. Thermostat connecté — `thermostat-connecte`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (28 mots) :
> Régulateur de chauffage programmable et pilotable à distance, qui adapte la consigne à la présence et aux habitudes des occupants. Il réduit la consommation sans dégrader le confort.

**Définition — après** (36 mots) :
> Régulateur de chauffage programmable et pilotable à distance depuis une application, qui commande la chaudière ou la pompe à chaleur pour atteindre la température voulue selon des programmes horaires. Il permet de réduire la consommation d'énergie.

**Version simple — avant** (19 mots) :
> Ce thermostat règle le chauffage tout seul selon les heures et la présence, et se commande depuis un téléphone.

**Version simple — après** (20 mots) :
> Ce thermostat allume et baisse le chauffage aux heures choisies, par exemple la nuit, et se commande depuis un téléphone.

**Sources après** (à ouvrir une par une) :
- [ADEME — Réduire sa facture de chauffage avec un thermostat programmable](https://agirpourlatransition.ademe.fr/particuliers/maison/economies-denergie/reduire-facture-chauffage-thermostat-programmable) — type `reference`

**Fiches liées après** : `capteur-de-temperature`, `domotique`, `economie-d-energie`, `objet-connecte-iot`, `scenario-domotique`

```
fiche : thermostat-connecte
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```
