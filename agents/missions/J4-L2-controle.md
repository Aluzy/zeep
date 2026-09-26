---
lot: J4-L2
role: controle
date: 2026-09-25
changeset: agents/changesets/J4-L2.jsonl
elements: ["alimentation-electrique", "cablage-electrique", "compteur-electrique", "consommation-electrique", "court-circuit", "disjoncteur", "domotique", "electrocution", "fiche-electrique", "harmoniques", "impedance", "installation-electrique", "luminaire", "mise-a-la-terre", "modulation", "monophase"]
---

# Contrôle du lot J4-L2

16 fiche(s), 72 opération(s) du rédacteur (changeset non encore appliqué).

## Consignes du contrôleur

Tu es le **contrôleur** du lot J4-L2. Tu n'as pas participé à la rédaction et tu ne la vois qu'à
travers ce document : les justifications du rédacteur sont volontairement absentes. Tu vérifies
chaque fiche contre les **12 critères** de `docs/grille-relecture.md` (lis-la en entier d'abord).

1. **Ouvre chaque URL de source** et vérifie qu'elle appuie la définition. Une source que tu ne
   peux pas ouvrir, imprécise (page d'accueil) ou qui n'appuie pas l'affirmation = critère 8 en échec.
2. Une fiche est **conforme** si les 12 critères passent. Dans `agents/changesets/J4-L2-controle.jsonl`, remplace alors
   `"__A_REMPLIR__"` de `new` par
   `{"date": "2026-09-25", "par": "agent-controleur-J4-L2", "statut": "relu-ia"}` et `why` par
   « Relue selon la grille (12 critères) ».
3. Une fiche **refusée** : supprime sa ligne dans `agents/changesets/J4-L2-controle.jsonl`, et note les critères en échec. Tu ne
   réécris pas la fiche : le rédacteur la corrige (nouvelle passe de contrôle) ou la retire du lot.
   Si le défaut porte sur une fiche hors lot, ajoute-la à `agents/donnees/signalements.json`.
4. Écris tes verdicts dans la section « Relecture (rempli par le contrôleur) » de
   `agents/rapports/J4-L2.md`, une ligne par fiche : critères en échec, décision.
5. Vérifie : `python3 scripts/apply_changeset.py agents/changesets/J4-L2.jsonl agents/changesets/J4-L2-controle.jsonl --dry-run`.
   Tu ne poses **jamais** `"statut": "valide"` (réservé à Alexandre).


## Fiches à contrôler

### 1. Alimentation électrique — `alimentation-electrique`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (13 mots) :
> Fourniture de courant électrique à un appareil, une installation électrique ou un bâtiment.

**Définition — après** (44 mots) :
> Fourniture de l'énergie électrique nécessaire au fonctionnement d'un appareil, ou dispositif qui assure cette fourniture : réseau de distribution, batterie, bloc qui adapte la tension. L'alimentation par le secteur, en 230 V, est dangereuse : son raccordement ou sa réparation reviennent à un électricien.

**Synonymes** : — → **alimentation**

**Sources après** (à ouvrir une par une) :
- [Dictionnaire de français Larousse, article « alimentation »](https://www.larousse.fr/dictionnaires/francais/alimentation/2276) — type `reference`
- [INRS, brochure ED 6344 « Électricité : 10 règles élémentaires de sécurité » (2019), p. 4 : 230 V aux prises des particuliers, tensions au-delà de 50 V potentiellement mortelles](https://www.inrs.fr/dam/inrs/CataloguePapier/ED/TI-ED-6344.pdf#page=4) — type `reference`
- [INRS, brochure ED 6344 « Électricité : 10 règles élémentaires de sécurité » (2019), p. 6 : « Ne pas bricoler » : l'électricien est un professionnel qualifié ; fiche cassée à faire remplacer](https://www.inrs.fr/dam/inrs/CataloguePapier/ED/TI-ED-6344.pdf#page=6) — type `reference`

**Fiches liées après** : `batterie` (nouveau), `chaine-d-energie`, `courant-electrique`, `court-jus`, `electricien` (nouveau), `electrification`, `energie-electrique` (nouveau), `installation-electrique`, `reseau-de-distribution` (nouveau), `tension-electrique` (nouveau), `varistance`

```
fiche : alimentation-electrique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 2. Câblage électrique — `cablage-electrique`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (20 mots) :
> Ensemble des câbles électriques et fils électriques posés dans un bâtiment pour relier le tableau électrique aux différents points d'utilisation.

**Définition — après** (50 mots) :
> Ensemble des câbles et fils électriques qui relient, dans un bâtiment ou un appareil, la source d'énergie aux points d'utilisation, par exemple du tableau électrique aux prises et aux luminaires ; désigne aussi l'opération de pose et de raccordement. Le câblage d'un logement se fait hors tension, par un électricien.

**Synonymes** : — → **câblage**

**Sources après** (à ouvrir une par une) :
- [Dictionnaire de français Larousse, article « câblage »](https://www.larousse.fr/dictionnaires/francais/c%C3%A2blage/11883) — type `reference`
- [INRS, brochure ED 6344 « Électricité : 10 règles élémentaires de sécurité » (2019), p. 6 : « Ne pas bricoler » : l'électricien est un professionnel qualifié ; fiche cassée à faire remplacer](https://www.inrs.fr/dam/inrs/CataloguePapier/ED/TI-ED-6344.pdf#page=6) — type `reference`

**Fiches liées après** : `cable-electrique` (nouveau), `connecteur-electrique`, `electricien` (nouveau), `fil-electrique`, `gaine-thermoretractable`, `installation-electrique`, `luminaire` (nouveau), `prise-de-courant` (nouveau), `tableau-electrique`

```
fiche : cablage-electrique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 3. Compteur électrique — `compteur-electrique`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (21 mots) :
> Appareil qui mesure la consommation électrique d'un logement ou d'un bâtiment, exprimée en kilowattheures, servant de base à la facture d'électricité.

**Définition — après** (50 mots) :
> Appareil qui mesure l'énergie électrique consommée par un logement ou un bâtiment, en kilowattheures. La différence entre deux relevés de son index donne la consommation qui sert à établir la facture d'électricité. Il est installé et géré par le gestionnaire du réseau de distribution : on n'y intervient pas soi-même.

**Synonymes** : — → **compteur d'électricité**

**Sources après** (à ouvrir une par une) :
- [Enedis, FAQ « Comment lire l'index du compteur électrique ? »](https://www.enedis.fr/faq/compteur-electrique/comment-lire-lindex-du-compteur-electrique) — type `reference`
- [Enedis, FAQ « Comment brancher un compteur électrique monophasé ? »](https://www.enedis.fr/faq/compteur-electrique/comment-brancher-un-compteur-electrique-monophase) — type `reference`
- [Dictionnaire de français Larousse, article « compteur »](https://www.larousse.fr/dictionnaires/francais/compteur/17821) — type `reference`

**Fiches liées après** : `compteur-linky`, `consommation-electrique`, `electricite`, `energie-electrique` (nouveau), `facture-d-electricite`, `kilowattheure` (nouveau), `puissance-active`, `puissance-souscrite`, `reseau-de-distribution` (nouveau)

```
fiche : compteur-electrique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 4. Consommation électrique — `consommation-electrique`

- Niveau scolaire : 2GT (cycles 2GT)
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (19 mots) :
> Quantité d'énergie électrique utilisée par un appareil, un logement ou une entreprise, mesurée par le compteur électrique en kilowattheures.

**Définition — après** (51 mots) :
> Quantité d'énergie électrique utilisée par un appareil, un foyer ou une entreprise pendant une durée donnée, exprimée en kilowattheures. Elle se lit sur le compteur électrique : la différence entre deux index relevés donne l'énergie consommée entre ces deux dates. Elle ne se confond pas avec la puissance, exprimée en watts.

**Synonymes** : — → **consommation d'électricité**

**Sources après** (à ouvrir une par une) :
- [Programme du cycle 4 en vigueur à la rentrée 2020 (d'après le BOEN n° 31 du 30 juillet 2020), p. 103 : « Conduire un calcul de consommation d'énergie électrique relatif à une situation de la vie courante »](https://eduscol.education.gouv.fr/sites/default/files/document/programme-d-enseignement-du-cycle-4-67722.pdf#page=103) — type `programme`
- [Enedis, FAQ « Comment lire l'index du compteur électrique ? »](https://www.enedis.fr/faq/compteur-electrique/comment-lire-lindex-du-compteur-electrique) — type `reference`
- [Dictionnaire de français Larousse, article « consommation »](https://www.larousse.fr/dictionnaires/francais/consommation/18427) — type `reference`

**Fiches liées après** : `ampoule-led`, `compteur-electrique`, `compteur-linky`, `delestage`, `economie-d-energie`, `energie-electrique`, `facture-d-electricite`, `heures-creuses`, `kilowattheure` (nouveau), `puissance-electrique` (nouveau), `reseau-intelligent-smart-grid`

```
fiche : consommation-electrique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 5. Court-circuit — `court-circuit`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (48 mots) :
> <strong>Vu côté électricité :</strong> Contact accidentel entre deux conducteurs électriques de potentiels différents, provoquant une intensité électrique excessive pouvant déclencher un disjoncteur ou un fusible.<br><br><strong>Vu côté électronique :</strong> Contact accidentel entre deux points d'un circuit électronique de potentiels différents, provoquant un courant excessif pouvant endommager les composants électroniques.

**Définition — après** (53 mots) :
> Liaison accidentelle, de résistance presque nulle, entre deux points d'un circuit qui devraient être à des tensions différentes, par exemple les deux bornes d'une pile ou deux conducteurs d'un câble abîmé. L'intensité devient alors très grande et peut provoquer échauffement, incendie ou destruction des composants ; fusibles et disjoncteurs coupent alors le circuit.

**Sources après** (à ouvrir une par une) :
- [INRS, dossier Risques électriques, « Prévention du risque électrique » (surintensités, mise à la terre des masses, NF C 15-100)](https://www.inrs.fr/risques/electriques/prevention-risque-electrique.html) — type `reference`
- [Dictionnaire de français Larousse, article « court-circuit »](https://www.larousse.fr/dictionnaires/francais/court-circuit/19961) — type `reference`

**Fiches liées après** : `arc-electrique`, `cable-electrique` (nouveau), `court-jus`, `disjoncteur`, `electronique`, `fusible`, `intensite-electrique`, `pile-electrique` (nouveau), `tension-electrique` (nouveau)

```
fiche : court-circuit
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 6. Disjoncteur — `disjoncteur`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (24 mots) :
> Dispositif de protection d'un circuit électrique qui coupe automatiquement le courant électrique en cas de court-circuit ou de surcharge, installé dans le tableau électrique.

**Définition — après** (56 mots) :
> Appareil de protection qui ouvre automatiquement un circuit électrique lorsque l'intensité dépasse une valeur fixée pendant un temps donné, en cas de surcharge ou de court-circuit ; on le réarme ensuite à la main. Placé dans le tableau électrique, il protège les câbles contre l'échauffement. S'il se déclenche souvent, il faut faire appel à un électricien.

**Sources après** (à ouvrir une par une) :
- [INRS, dossier Risques électriques, « Prévention du risque électrique » (surintensités, mise à la terre des masses, NF C 15-100)](https://www.inrs.fr/risques/electriques/prevention-risque-electrique.html) — type `reference`
- [Dictionnaire de français Larousse, article « disjoncteur »](https://www.larousse.fr/dictionnaires/francais/disjoncteur/25911) — type `reference`

**Fiches liées après** : `arc-electrique`, `circuit-electrique`, `courant-electrique`, `court-circuit`, `court-jus`, `disjoncteur-differentiel`, `electricien` (nouveau), `intensite-electrique` (nouveau), `puissance-souscrite`, `schema-unifilaire`, `section-de-cable`, `sectionneur`, `tableau-electrique`

```
fiche : disjoncteur
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 7. Domotique — `domotique`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (43 mots) :
> <strong>Vu côté électricité :</strong> Ensemble des technologies qui automatisent et pilotent à distance les équipements électriques d'un logement, comme l'éclairage.<br><br><strong>Vu côté électronique :</strong> Ensemble des technologies d'électronique embarquée qui automatisent et pilotent à distance les équipements d'un logement, souvent via un objet connecté.

**Définition — après** (48 mots) :
> Ensemble des techniques qui automatisent et commandent à distance les équipements d'un bâtiment, comme l'éclairage, le chauffage, les volets ou l'alarme, grâce à des capteurs, des actionneurs et des objets connectés reliés par un réseau. Son installation sur les circuits en 230 V est confiée à un électricien.

**Synonymes** : — → **maison connectée**

**Sources après** (à ouvrir une par une) :
- [Dictionnaire de français Larousse, article « domotique »](https://www.larousse.fr/dictionnaires/francais/domotique/26402) — type `reference`

**Fiches liées après** : `actionneur` (nouveau), `capteur` (nouveau), `detecteur`, `detecteur-de-presence`, `eclairage`, `electricien` (nouveau), `electronique`, `electronique-embarquee`, `mqtt`, `objet-connecte-iot`, `reseau-maille`, `scenario-domotique`, `thermostat-connecte`, `volet-roulant-motorise`, `zigbee`

```
fiche : domotique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 8. Électrocution — `electrocution`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (28 mots) :
> Électrisation entraînant la mort de la personne. Le risque devient majeur dès quelques dizaines de milliampères traversant la cage thoracique, bien en deçà du courant d'un appareil ménager.

**Définition — après** (47 mots) :
> Électrisation qui entraîne la mort de la personne traversée par le courant électrique. Un courant alternatif de quelques dizaines de milliampères passant par le cœur pendant une seconde peut suffire, bien moins que celui d'un appareil ménager : toute tension supérieure à 50 V est potentiellement mortelle.

**Sources après** (à ouvrir une par une) :
- [INRS, dossier Risques électriques, « Accidents d'origine électrique » (électrisation, électrocution, effets du courant)](https://www.inrs.fr/risques/electriques/accidents-origine-electrique.html) — type `reference`
- [INRS, brochure ED 6344 « Électricité : 10 règles élémentaires de sécurité » (2019), p. 4 : 230 V aux prises des particuliers, tensions au-delà de 50 V potentiellement mortelles](https://www.inrs.fr/dam/inrs/CataloguePapier/ED/TI-ED-6344.pdf#page=4) — type `reference`
- [Dictionnaire de français Larousse, article « électrocution »](https://www.larousse.fr/dictionnaires/francais/%C3%A9lectrocution_n_f_/28237) — type `reference`

**Fiches liées après** : `courant-electrique`, `disjoncteur-differentiel`, `electrisation`, `habilitation-electrique`, `mise-a-la-terre`

```
fiche : electrocution
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 9. Fiche électrique — `fiche-electrique`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (18 mots) :
> Élément mobile équipé de broches, connecté à un appareil, destiné à être inséré dans une prise de courant.

**Définition — après** (50 mots) :
> Partie mâle d'un raccordement, fixée au bout du cordon d'un appareil, dont les broches s'enfoncent dans une prise de courant pour l'alimenter. Pour débrancher, on tire sur la fiche et non sur le câble ; une fiche cassée se remplace par un modèle normalisé et ne se répare jamais soi-même.

**Synonymes** : — → **prise mâle**

**Sources après** (à ouvrir une par une) :
- [INRS, brochure ED 6344 « Électricité : 10 règles élémentaires de sécurité » (2019), p. 6 : « Ne pas bricoler » : l'électricien est un professionnel qualifié ; fiche cassée à faire remplacer](https://www.inrs.fr/dam/inrs/CataloguePapier/ED/TI-ED-6344.pdf#page=6) — type `reference`
- [INRS, brochure ED 6344 « Électricité : 10 règles élémentaires de sécurité » (2019), p. 8 : « Ne pas tirer sur le câble d'alimentation […] mais sur sa fiche d'alimentation »](https://www.inrs.fr/dam/inrs/CataloguePapier/ED/TI-ED-6344.pdf#page=8) — type `reference`

**Fiches liées après** : `cable-electrique` (nouveau), `connecteur-electrique`, `prise-de-courant`

```
fiche : fiche-electrique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 10. Harmoniques — `harmoniques`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (31 mots) :
> Composantes d'un signal dont les fréquences sont des multiples de la fréquence fondamentale. Injectées par les appareils à découpage, elles déforment la tension du réseau et échauffent les conducteurs de neutre.

**Définition — après** (53 mots) :
> Composantes d'un courant ou d'une tension dont les fréquences sont des multiples entiers de la fréquence fondamentale, 50 Hz sur le réseau. Produites notamment par les alimentations à découpage, elles déforment la tension et échauffent les conducteurs de neutre ; leur mesure sur une installation sous tension est réservée à un professionnel qualifié.

**Sources après** (à ouvrir une par une) :
- [Dictionnaire de français Larousse, article « harmonique »](https://www.larousse.fr/dictionnaires/francais/harmonique/39116) — type `reference`

**Fiches liées après** : `alimentation-a-decoupage`, `analyseur-de-spectre`, `compatibilite-electromagnetique-cem`, `courant-alternatif`, `distorsion`, `filtre-electronique`, `frequence-electrique` (nouveau), `neutre`

```
fiche : harmoniques
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 11. Impédance — `impedance`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (17 mots) :
> Grandeur qui caractérise l'opposition d'un circuit électronique au passage d'un signal analogique, combinant résistance, condensateur et bobine.

**Définition — après** (48 mots) :
> Grandeur qui caractérise l'opposition d'un dipôle au passage d'un courant alternatif : en régime sinusoïdal, c'est le rapport de l'amplitude de la tension à ses bornes à celle du courant qui le traverse. Exprimée en ohms, elle combine la résistance et la réactance, qui dépend de la fréquence.

**Sources après** (à ouvrir une par une) :
- [Dictionnaire de français Larousse, article « impédance »](https://www.larousse.fr/dictionnaires/francais/imp%C3%A9dance/41833) — type `reference`

**Fiches liées après** : `bobine-inductance`, `condensateur`, `courant-alternatif` (nouveau), `dephasage`, `dipole` (nouveau), `electronique`, `haut-parleur`, `henry`, `ohm` (nouveau), `reactance`, `resistance`, `resistance-electrique` (nouveau), `signal-analogique`

```
fiche : impedance
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 12. Installation électrique — `installation-electrique`

- Niveau scolaire : CAP (cycles CAP)
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (22 mots) :
> Ensemble des équipements, comme le tableau électrique, le câblage électrique et les prises de courant, permettant de distribuer l'électricité dans un bâtiment.

**Définition — après** (46 mots) :
> Ensemble des matériels électriques d'un bâtiment qui distribuent l'énergie depuis le point de livraison jusqu'aux appareils : tableau électrique, protections, câblage, prises de courant et points d'éclairage. Elle doit respecter la norme NF C 15-100 ; toute intervention s'y fait hors tension et relève d'un électricien.

**Sources après** (à ouvrir une par une) :
- [INRS, dossier Risques électriques, « Prévention du risque électrique » (surintensités, mise à la terre des masses, NF C 15-100)](https://www.inrs.fr/risques/electriques/prevention-risque-electrique.html) — type `reference`
- [INRS, brochure ED 6344 « Électricité : 10 règles élémentaires de sécurité » (2019), p. 6 : « Ne pas bricoler » : l'électricien est un professionnel qualifié ; fiche cassée à faire remplacer](https://www.inrs.fr/dam/inrs/CataloguePapier/ED/TI-ED-6344.pdf#page=6) — type `reference`
- [Dictionnaire de français Larousse, article « installation »](https://www.larousse.fr/dictionnaires/francais/installation/43409) — type `reference`

**Fiches liées après** : `alimentation-electrique`, `borne-de-recharge`, `cablage-electrique`, `chute-de-tension`, `controleur-d-isolement`, `electricien`, `electricite`, `habilitation-electrique`, `indice-de-protection-ip`, `kilowatt`, `luminaire`, `mise-a-la-terre`, `monophase`, `norme-electrique-nf-c-15-100`, `parafoudre`, `prise-de-courant`, `prise-de-terre`, `regime-de-neutre`, `schema-electrique`, `schema-unifilaire`, `section-de-cable`, `tableau-electrique`, `tres-basse-tension-de-securite`, `volet-roulant-motorise`

```
fiche : installation-electrique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 13. Luminaire — `luminaire`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (15 mots) :
> Appareil d'éclairage qui reçoit, supporte et protège une ou plusieurs ampoules raccordées à l'installation électrique.

**Définition — après** (48 mots) :
> Appareil d'éclairage qui reçoit une ou plusieurs lampes, les alimente et répartit, filtre ou oriente leur lumière, comme un plafonnier, une applique ou un lampadaire. Lorsqu'il est raccordé en fixe à l'installation électrique, sa pose ou son remplacement se fait circuit coupé au tableau et relève d'un électricien.

**Synonymes** : — → **appareil d'éclairage**

**Sources après** (à ouvrir une par une) :
- [Dictionnaire de français Larousse, article « luminaire »](https://www.larousse.fr/dictionnaires/francais/luminaire/48046) — type `reference`
- [INRS, brochure ED 6344 « Électricité : 10 règles élémentaires de sécurité » (2019), p. 6 : « Ne pas bricoler » : l'électricien est un professionnel qualifié ; fiche cassée à faire remplacer](https://www.inrs.fr/dam/inrs/CataloguePapier/ED/TI-ED-6344.pdf#page=6) — type `reference`

**Fiches liées après** : `cablage-electrique` (nouveau), `eclairage`, `electricien` (nouveau), `gradateur`, `indice-de-protection-ip`, `installation-electrique`, `lumen`, `lux`

```
fiche : luminaire
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 14. Mise à la terre — `mise-a-la-terre`

- Niveau scolaire : BACPRO (cycles BACPRO)
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (22 mots) :
> Connexion électrique reliant les masses métalliques d'une installation électrique au sol via une prise de terre, afin d'assurer la sécurité des personnes.

**Définition — après** (52 mots) :
> Liaison qui relie les parties métalliques accessibles d'une installation et des appareils, appelées masses, à la terre par un conducteur de protection et une prise de terre. En cas de défaut d'isolement, le courant de fuite s'écoule par la terre et le dispositif différentiel coupe l'alimentation ; sa réalisation relève d'un électricien.

**Sources après** (à ouvrir une par une) :
- [INRS, dossier Risques électriques, « Prévention du risque électrique » (surintensités, mise à la terre des masses, NF C 15-100)](https://www.inrs.fr/risques/electriques/prevention-risque-electrique.html) — type `reference`
- [INRS, dossier Risques électriques, glossaire (masse, terre, contact indirect)](https://www.inrs.fr/risques/electriques/glossaire.html) — type `reference`
- [Dictionnaire de français Larousse, article « terre »](https://www.larousse.fr/dictionnaires/francais/terre/77443) — type `reference`

**Fiches liées après** : `classe-d-isolation`, `consignation-electrique`, `courant-de-fuite`, `defaut-d-isolement`, `disjoncteur-differentiel`, `electricien` (nouveau), `electrisation`, `electrocution`, `installation-electrique`, `parafoudre`, `prise-de-terre`, `regime-de-neutre`

```
fiche : mise-a-la-terre
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 15. Modulation — `modulation`

- Niveau scolaire : TG (cycles TG)
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (27 mots) :
> Technique consistant à faire varier une caractéristique d'un signal, souvent porté par une fréquence de commutation, pour y transmettre une information, utilisée notamment par un émetteur radiofréquence.

**Définition — après** (48 mots) :
> Procédé qui fait varier une caractéristique d'une onde porteuse, son amplitude, sa fréquence ou sa phase, au rythme d'un signal à transmettre, comme la voix ou des données. Il place ce signal dans la bande de fréquences adaptée à sa transmission, par exemple en radio AM ou FM.

**Sources après** (à ouvrir une par une) :
- [Dictionnaire de français Larousse, article « modulation »](https://www.larousse.fr/dictionnaires/francais/modulation/51977) — type `reference`

**Fiches liées après** : `emetteur-radiofrequence`

```
fiche : modulation
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 16. Monophasé — `monophase`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (28 mots) :
> Distribution électrique alimentée par une seule phase et un neutre, avec une tension de 230 volts en France. C'est le raccordement habituel des logements et des petits appareils.

**Définition — après** (42 mots) :
> Mode de distribution en courant alternatif qui utilise une seule phase et le neutre, entre lesquels la tension vaut 230 V en France. C'est le raccordement habituel des logements ; ces conducteurs sont dangereux, et toute intervention sur eux relève d'un électricien.

**Sources après** (à ouvrir une par une) :
- [Dictionnaire de français Larousse, article « monophasé »](https://www.larousse.fr/dictionnaires/francais/monophas%C3%A9/52374) — type `reference`
- [INRS, dossier Risques électriques, « Principes généraux sur l'électricité » (tensions 230 V et 400/230 V)](https://www.inrs.fr/risques/electriques/principes-generaux-electricite.html) — type `reference`
- [INRS, brochure ED 6344 « Électricité : 10 règles élémentaires de sécurité » (2019), p. 4 : 230 V aux prises des particuliers, tensions au-delà de 50 V potentiellement mortelles](https://www.inrs.fr/dam/inrs/CataloguePapier/ED/TI-ED-6344.pdf#page=4) — type `reference`

**Fiches liées après** : `courant-alternatif` (nouveau), `electricien` (nouveau), `installation-electrique`, `neutre`, `phase-electrique`, `tension-electrique`, `triphase`

```
fiche : monophase
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```
