---
lot: J4-L3
role: controle
date: 2026-09-25
changeset: agents/changesets/J4-L3.jsonl
elements: ["neutre", "panneau-photovoltaique", "parafoudre", "prise-de-terre", "redresseur", "regime-de-neutre", "schema-electrique", "tableau-electrique", "triphase", "valeur-crete", "valeur-efficace"]
---

# Contrôle du lot J4-L3 — passe 2

11 fiche(s), 85 opération(s) du rédacteur (changeset non encore appliqué).

## Consignes du contrôleur

Tu es le **contrôleur** du lot J4-L3. Tu n'as pas participé à la rédaction et tu ne la vois qu'à
travers ce document : les justifications du rédacteur sont volontairement absentes. Tu vérifies
chaque fiche contre les **12 critères** de `docs/grille-relecture.md` (lis-la en entier d'abord).

1. **Ouvre chaque URL de source** et vérifie qu'elle appuie la définition. Une source que tu ne
   peux pas ouvrir, imprécise (page d'accueil) ou qui n'appuie pas l'affirmation = critère 8 en échec.
2. Une fiche est **conforme** si les 12 critères passent. Dans `agents/changesets/J4-L3-controle.jsonl`, remplace alors
   `"__A_REMPLIR__"` de `new` par
   `{"date": "2026-09-25", "par": "agent-controleur-J4-L3", "statut": "relu-ia"}` et `why` par
   « Relue selon la grille (12 critères) ».
3. Une fiche **refusée** : supprime sa ligne dans `agents/changesets/J4-L3-controle.jsonl`, et note les critères en échec. Tu ne
   réécris pas la fiche : le rédacteur la corrige (nouvelle passe de contrôle) ou la retire du lot.
   Si le défaut porte sur une fiche hors lot, ajoute-la à `agents/donnees/signalements.json`.
4. Écris tes verdicts dans la section « Relecture (rempli par le contrôleur) » de
   `agents/rapports/J4-L3.md`, une ligne par fiche : critères en échec, décision.
5. Vérifie : `python3 scripts/apply_changeset.py agents/changesets/J4-L3.jsonl agents/changesets/J4-L3-controle.jsonl --dry-run`.
   Tu ne poses **jamais** `"statut": "valide"` (réservé à Alexandre).


## Fiches à contrôler

### 1. Neutre — `neutre`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (19 mots) :
> Conducteur d'un circuit électrique qui ramène le courant électrique vers la source, complétant le circuit avec la phase électrique.

**Définition — après** (58 mots) :
> Conducteur qui, avec la ou les phases, alimente les appareils en courant alternatif : en monophasé, les 230 V s'établissent entre la phase et le neutre. Selon le schéma de liaison à la terre, il est relié ou non à la terre ; il peut être sous tension en cas de défaut : toute intervention relève d'un électricien.

**Synonymes** : — → **conducteur de neutre**

**Sources après** (à ouvrir une par une) :
- [INRS, brochure ED 6345 « L'électricité », p. 12 : conducteurs repérés par couleurs, non interchangeables ; installations domestiques en 230 V](https://www.inrs.fr/dam/inrs/CataloguePapier/ED/TI-ED-6345.pdf#page=12) — type `reference`
- [INRS, brochure ED 6345 « L'électricité », p. 31 : cas où le neutre n'est pas relié directement à la terre](https://www.inrs.fr/dam/inrs/CataloguePapier/ED/TI-ED-6345.pdf#page=31) — type `reference`
- [INRS, dossier Risques électriques, « Prévention du risque électrique » (surintensités, schémas de liaison à la terre, NF C 15-100)](https://www.inrs.fr/risques/electriques/prevention-risque-electrique.html) — type `reference`

**Fiches liées après** : `circuit-electrique`, `courant-alternatif` (nouveau), `courant-electrique`, `electricien` (nouveau), `harmoniques`, `installation-electrique` (nouveau), `mise-a-la-terre` (nouveau), `monophase`, `phase-electrique`, `prise-de-courant` (nouveau), `regime-de-neutre`, `tension-electrique` (nouveau), `triphase`

```
fiche : neutre
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 2. Panneau photovoltaïque — `panneau-photovoltaique`

- Niveau scolaire : TG (cycles TG)
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (18 mots) :
> Dispositif composé de cellules qui convertit directement la lumière du soleil en courant continu, une forme d'énergie renouvelable.

**Définition — après** (50 mots) :
> Assemblage de cellules photovoltaïques qui convertit directement une partie de l'énergie lumineuse reçue du Soleil en énergie électrique, fournie sous forme de courant continu. Ce courant varie avec l'éclairement et la température ; un onduleur le transforme en courant alternatif pour l'utiliser dans un bâtiment ou l'injecter sur le réseau.

**Version simple — avant** (0 mots) :
_(vide)_

**Version simple — après** (31 mots) :
> Un panneau photovoltaïque transforme la lumière du Soleil en électricité. Sur un toit ou sur une calculatrice, il fonctionne dès qu'il est éclairé, et produit plus quand la lumière est forte.

**Sources après** (à ouvrir une par une) :
- [INRS, brochure ED 6345 « L'électricité », p. 11 : « Générateurs photovoltaïques » (cellules assemblées en panneaux, courant continu variant avec l'éclairement et la température)](https://www.inrs.fr/dam/inrs/CataloguePapier/ED/TI-ED-6345.pdf#page=11) — type `reference`

**Fiches liées après** : `autoconsommation`, `courant-alternatif` (nouveau), `courant-continu`, `effet-photoelectrique`, `energie-electrique` (nouveau), `energie-renouvelable`, `facteur-de-charge`, `generateur-electrique`, `onduleur`, `reseau-electrique` (nouveau), `watt-crete`

```
fiche : panneau-photovoltaique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 3. Parafoudre — `parafoudre`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (28 mots) :
> Dispositif installé dans un tableau électrique qui écoule vers la terre les surtensions dues à la foudre ou aux manœuvres du réseau. Il protège les équipements électroniques sensibles.

**Définition — après** (54 mots) :
> Dispositif qui protège une installation et les appareils qui y sont branchés contre les surtensions dues à la foudre ou à d'autres surtensions dangereuses, en les dérivant vers la terre. Placé dans le tableau électrique, il est obligatoire dans certains cas fixés par la norme NF C 15-100 ; sa pose relève d'un électricien.

**Synonymes** : SPD, parafoudre, protection contre la foudre → **SPD**

**Sources après** (à ouvrir une par une) :
- [Dictionnaire de français Larousse, article « parafoudre »](https://www.larousse.fr/dictionnaires/francais/parafoudre/57893) — type `reference`
- [INRS, brochure ED 6345 « L'électricité », p. 31 : « Parafoudres » : conditions de mise en œuvre selon la NF C 15-100](https://www.inrs.fr/dam/inrs/CataloguePapier/ED/TI-ED-6345.pdf#page=31) — type `reference`

**Fiches liées après** : `electricien` (nouveau), `installation-electrique`, `mise-a-la-terre`, `norme-electrique-nf-c-15-100` (nouveau), `prise-de-terre`, `tableau-electrique`, `varistance`

```
fiche : parafoudre
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 4. Prise de terre — `prise-de-terre`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (14 mots) :
> Dispositif enfoui dans le sol assurant la mise à la terre d'une installation électrique.

**Définition — après** (47 mots) :
> Ensemble de conducteurs enterrés qui assure le contact électrique entre une installation et le sol, afin d'écouler vers la terre les courants dus à un défaut d'isolement. Pour une maison, sa résistance ne doit pas dépasser 100 Ω ; sa réalisation et sa vérification relèvent d'un électricien.

**Sources après** (à ouvrir une par une) :
- [INRS, brochure ED 6345 « L'électricité », p. 27 : valeur de la prise de terre d'une maison (100 Ω au plus) et conducteur de protection](https://www.inrs.fr/dam/inrs/CataloguePapier/ED/TI-ED-6345.pdf#page=27) — type `reference`
- [Dictionnaire de français Larousse, article « terre »](https://www.larousse.fr/dictionnaires/francais/terre/77443) — type `reference`

**Fiches liées après** : `defaut-d-isolement` (nouveau), `electricien` (nouveau), `installation-electrique`, `mise-a-la-terre`, `parafoudre`, `regime-de-neutre`, `resistance-electrique` (nouveau)

```
fiche : prise-de-terre
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 5. Redresseur — `redresseur`

- Niveau scolaire : STI2D (cycles STI2D)
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (39 mots) :
> <strong>Vu côté électricité :</strong> Dispositif électronique qui convertit un courant alternatif en courant continu.<br><br><strong>Vu côté électronique :</strong> Circuit électronique, souvent construit à partir de diodes, qui convertit un signal analogique alternatif en signal continu au sein d'une alimentation électronique.

**Définition — après** (51 mots) :
> Montage qui convertit un courant alternatif, dont le sens s'inverse sans cesse, en un courant qui circule toujours dans le même sens, grâce à des composants comme les diodes, souvent montées en pont. On le trouve dans les chargeurs et les alimentations électroniques, où un condensateur lisse ensuite la tension obtenue.

**Synonymes** : — → **convertisseur alternatif-continu, AC/DC**

**Sources après** (à ouvrir une par une) :
- [Dictionnaire de français Larousse, article « redresseur »](https://www.larousse.fr/dictionnaires/francais/redresseur/67354) — type `reference`

**Fiches liées après** : `alimentation-electronique`, `condensateur` (nouveau), `courant-alternatif`, `courant-continu`, `diode`, `diode-schottky`, `electronique`, `pont-de-diodes`, `signal-analogique`, `tension-electrique` (nouveau)

```
fiche : redresseur
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 6. Régime de neutre — `regime-de-neutre`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (34 mots) :
> Manière dont le neutre de l'alimentation et les masses de l'installation sont reliés à la terre. Les régimes TT, TN et IT déterminent le comportement en cas de défaut et les protections à installer.

**Définition — après** (60 mots) :
> Manière dont le neutre de l'alimentation et les masses de l'installation, c'est-à-dire les parties métalliques accessibles des appareils, sont reliés ou non à la terre ; on le désigne par deux lettres : TT, TN ou IT. Il fixe ce qui se passe lors d'un défaut d'isolement et les protections à prévoir ; sa mise en œuvre relève d'un électricien.

**Version simple — avant** (21 mots) :
> Selon la façon dont l'installation est reliée à la terre, un défaut ne réagit pas pareil. Chaque cas a ses protections.

**Version simple — après** (30 mots) :
> Il existe plusieurs façons de relier une installation électrique à la terre. Chacune décide de ce qui se passe quand un appareil a un défaut, et des protections à prévoir.

**Synonymes** : IT, TN, TT, regime de neutre, schema des liaisons a la terre → **schéma de liaison à la terre, régime du neutre**

**Sources après** (à ouvrir une par une) :
- [INRS, dossier Risques électriques, « Prévention du risque électrique » (surintensités, schémas de liaison à la terre, NF C 15-100)](https://www.inrs.fr/risques/electriques/prevention-risque-electrique.html) — type `reference`
- [INRS, brochure ED 6345 « L'électricité », p. 18 : le courant de défaut dépend du schéma des liaisons à la terre (TT, TN, IT) ; renvoi à la NF C 15-100](https://www.inrs.fr/dam/inrs/CataloguePapier/ED/TI-ED-6345.pdf#page=18) — type `reference`

**Fiches liées après** : `classe-d-isolation`, `defaut-d-isolement` (nouveau), `disjoncteur-differentiel`, `electricien` (nouveau), `installation-electrique`, `mise-a-la-terre`, `neutre`, `prise-de-terre`

```
fiche : regime-de-neutre
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 7. Schéma électrique — `schema-electrique`

- Niveau scolaire : 1G (cycles 1G)
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (15 mots) :
> Représentation graphique d'un circuit électrique montrant les liaisons entre les différents composants d'une installation électrique.

**Définition — après** (48 mots) :
> Représentation d'un circuit électrique à l'aide de symboles normalisés reliés par des traits qui figurent les conducteurs. Il permet de comprendre le fonctionnement du circuit, de le réaliser ou de le dépanner ; dès l'école élémentaire, les élèves passent d'un montage réel à son schéma normalisé, et inversement.

**Version simple — avant** (0 mots) :
_(vide)_

**Version simple — après** (34 mots) :
> Un schéma électrique est un dessin qui représente un circuit avec des symboles simples : un rond marqué d'une croix pour la lampe, des traits pour les fils. Il aide à construire le circuit.

**Synonymes** : — → **schéma normalisé**

**Sources après** (à ouvrir une par une) :
- [Programme de sciences et technologie du cycle 3 (annexe 2 de l'arrêté du 5 juin 2026), p. 7 : l'élève compare son schéma de circuit à un schéma normalisé](https://www.education.gouv.fr/sites/default/files/document/annexe-2-programme-de-sciences-et-technologie-du-cycle-3-519023.pdf#page=7) — type `programme`
- [Programme de sciences et technologie du cycle 3 (annexe 2 de l'arrêté du 5 juin 2026), p. 9 : représentation schématique normalisée du circuit réalisé](https://www.education.gouv.fr/sites/default/files/document/annexe-2-programme-de-sciences-et-technologie-du-cycle-3-519023.pdf#page=9) — type `programme`

**Fiches liées après** : `circuit-electrique`, `conception-assistee-par-ordinateur-electronique`, `conducteur-electrique` (nouveau), `installation-electrique`, `schema-unifilaire`

```
fiche : schema-electrique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 8. Tableau électrique — `tableau-electrique`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (17 mots) :
> Ensemble centralisant les disjoncteurs et fusibles d'une installation électrique, permettant de répartir et protéger les circuits électriques.

**Définition — après** (49 mots) :
> Coffret qui regroupe les appareils de commande et de protection d'une installation : dispositifs différentiels, disjoncteurs ou fusibles de chaque circuit. Il répartit l'énergie entre les circuits et permet de les couper séparément. Le déclenchement d'une protection signale un défaut : toute intervention dans le tableau relève d'un électricien.

**Synonymes** : — → **tableau de répartition**

**Sources après** (à ouvrir une par une) :
- [Dictionnaire de français Larousse, article « tableau »](https://www.larousse.fr/dictionnaires/francais/tableau/76304) — type `reference`
- [INRS, dossier Risques électriques, « Prévention du risque électrique » (surintensités, schémas de liaison à la terre, NF C 15-100)](https://www.inrs.fr/risques/electriques/prevention-risque-electrique.html) — type `reference`
- [INRS, brochure ED 6344 « Électricité : 10 règles élémentaires de sécurité » (2019), p. 6 : « Ne pas bricoler » : l'électricien est un professionnel qualifié ; ne pas introduire de fils dans une prise](https://www.inrs.fr/dam/inrs/CataloguePapier/ED/TI-ED-6344.pdf#page=6) — type `reference`

**Fiches liées après** : `cablage-electrique`, `consignation-electrique`, `contacteur`, `disjoncteur`, `disjoncteur-differentiel`, `electricien` (nouveau), `fusible` (nouveau), `installation-electrique`, `parafoudre`, `schema-unifilaire`, `sectionneur`

```
fiche : tableau-electrique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 9. Triphasé — `triphase`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (33 mots) :
> Distribution électrique composée de trois phases décalées d'un tiers de période, avec ou sans neutre. Elle permet de transporter plus de puissance avec moins de cuivre et fait tourner directement les moteurs asynchrones.

**Définition — après** (53 mots) :
> Système de distribution en courant alternatif à trois phases dont les tensions sont décalées d'un tiers de période, avec ou sans neutre : en France, 230 V entre une phase et le neutre et 400 V entre deux phases. Il alimente notamment les moteurs de forte puissance ; toute intervention relève d'un électricien.

**Sources après** (à ouvrir une par une) :
- [INRS, brochure ED 6345 « L'électricité », p. 42 : tensions nominales en monophasé 230 V et en triphasé 230/400 V, exprimées en valeurs efficaces](https://www.inrs.fr/dam/inrs/CataloguePapier/ED/TI-ED-6345.pdf#page=42) — type `reference`
- [INRS, dossier Risques électriques, « Principes généraux sur l'électricité » (tensions 230 V et 400/230 V, moteur triphasé)](https://www.inrs.fr/risques/electriques/principes-generaux-electricite.html) — type `reference`

**Fiches liées après** : `courant-alternatif` (nouveau), `electricien` (nouveau), `monophase`, `moteur-asynchrone`, `neutre`, `periode` (nouveau), `phase-electrique`, `puissance-electrique` (nouveau), `reseau-de-distribution`, `tension-electrique` (nouveau)

```
fiche : triphase
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 10. Valeur crête — `valeur-crete`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (36 mots) :
> Valeur maximale atteinte par un signal alternatif au cours d'une période. Pour une sinusoïde, elle vaut environ une fois et demie la valeur efficace : les 230 volts du réseau culminent à plus de 320 volts.

**Définition — après** (48 mots) :
> Valeur maximale atteinte par une grandeur périodique, comme une tension ou un courant alternatif, au cours d'une période. Pour une sinusoïde, elle vaut environ 1,41 fois la valeur efficace : les 230 V du réseau correspondent à une tension crête d'environ 325 V, d'où le danger d'y toucher.

**Version simple — avant** (25 mots) :
> La valeur crête est le point le plus haut atteint par le signal. Elle est plus grande que la valeur qu'affiche un appareil de mesure.

**Version simple — après** (31 mots) :
> La valeur crête est le point le plus haut atteint par une tension qui change sans cesse. Pour le réseau, elle dépasse 320 volts, bien plus que les 230 volts annoncés.

**Synonymes** : Vpp, amplitude, valeur crete, valeur crete a crete → **amplitude, valeur maximale**

**Sources après** (à ouvrir une par une) :
- [Dictionnaire de français Larousse, article « crête »](https://www.larousse.fr/dictionnaires/francais/cr%C3%AAte/20420) — type `reference`
- [INRS, brochure ED 6345 « L'électricité », p. 42 : tensions nominales en monophasé 230 V et en triphasé 230/400 V, exprimées en valeurs efficaces](https://www.inrs.fr/dam/inrs/CataloguePapier/ED/TI-ED-6345.pdf#page=42) — type `reference`

**Fiches liées après** : `courant-alternatif`, `oscilloscope`, `periode` (nouveau), `signal-analogique`, `tension-electrique` (nouveau), `valeur-efficace`

```
fiche : valeur-crete
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 11. Valeur efficace — `valeur-efficace`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (31 mots) :
> Valeur d'un signal alternatif qui produirait le même échauffement qu'un courant continu de même valeur. C'est elle qu'affichent les multimètres et qui est désignée par les 230 volts du réseau domestique.

**Définition — après** (53 mots) :
> Valeur de la tension ou du courant continu qui produirait, dans une même résistance et pendant la même durée, le même échauffement que la tension ou le courant alternatif considéré. C'est elle qu'affichent les multimètres et que désignent les 230 volts du réseau domestique, une tension dangereuse à laquelle on ne touche jamais.

**Sources après** (à ouvrir une par une) :
- [INRS, brochure ED 6345 « L'électricité », p. 42 : tensions nominales en monophasé 230 V et en triphasé 230/400 V, exprimées en valeurs efficaces](https://www.inrs.fr/dam/inrs/CataloguePapier/ED/TI-ED-6345.pdf#page=42) — type `reference`

**Fiches liées après** : `courant-alternatif`, `courant-continu` (nouveau), `effet-joule`, `multimetre`, `resistance-electrique` (nouveau), `tension-electrique`, `valeur-crete`

```
fiche : valeur-efficace
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```
