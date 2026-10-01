---
lot: J5-S5
role: controle
date: 2026-10-01
changeset: agents/changesets/J5-S5.jsonl
elements: ["asservissement", "constante-de-temps", "echantillonnage", "algebre-de-boole", "bit", "bande-interdite", "dopage", "jonction-pn", "loi-de-coulomb", "machine-a-etats", "bras-robotise", "histoire-de-l-electricite", "moteur-a-courant-continu", "moteur-asynchrone"]
---

# Contrôle du lot J5-S5

14 fiche(s), 45 opération(s) du rédacteur (changeset non encore appliqué).

## Consignes du contrôleur

Tu es le **contrôleur** du lot J5-S5. Tu n'as pas participé à la rédaction et tu ne la vois qu'à
travers ce document : les justifications du rédacteur sont volontairement absentes. Tu vérifies
chaque fiche contre les **12 critères** de `docs/grille-relecture.md` (lis-la en entier d'abord).

1. **Ouvre chaque URL de source** et vérifie qu'elle appuie la définition. Une source que tu ne
   peux pas ouvrir, imprécise (page d'accueil) ou qui n'appuie pas l'affirmation = critère 8 en échec.
2. Une fiche est **conforme** si les 12 critères passent. Dans `agents/changesets/J5-S5-controle.jsonl`, remplace alors
   `"__A_REMPLIR__"` de `new` par
   `{"date": "2026-10-01", "par": "agent-controleur-J5-S5", "statut": "relu-ia"}` et `why` par
   « Relue selon la grille (12 critères) ».
3. Une fiche **refusée** : supprime sa ligne dans `agents/changesets/J5-S5-controle.jsonl`, et note les critères en échec. Tu ne
   réécris pas la fiche : le rédacteur la corrige (nouvelle passe de contrôle) ou la retire du lot.
   Si le défaut porte sur une fiche hors lot, ajoute-la à `agents/donnees/signalements.json`.
4. Écris tes verdicts dans la section « Relecture (rempli par le contrôleur) » de
   `agents/rapports/J5-S5.md`, une ligne par fiche : critères en échec, décision.
5. Vérifie : `python3 scripts/apply_changeset.py agents/changesets/J5-S5.jsonl agents/changesets/J5-S5-controle.jsonl --dry-run`.
   Tu ne poses **jamais** `"statut": "valide"` (réservé à Alexandre).


## Fiches à contrôler

### 1. Asservissement — `asservissement`

- Niveau scolaire : BACPRO (cycles BACPRO, STI2D)
- Règles automatiques encore enfreintes : aucune

**Sources après** (à ouvrir une par une) :
- [Programme STI2D, enseignement technologique transversal (arrêté du 17 janvier 2019, modifié le 19 juillet 2019), « Représentation d'une boucle de régulation ou d'asservissement »](https://www.snes.edu/IMG/pdf/arrete_sti2d_ensemble.pdf) — type `programme`

**Fiches liées après** : `actionneur`, `automate-programmable`, `bras-robotise`, `capteur`, `codeur-rotatif`, `drone`, `machine-a-etats`, `robotique`, `servomoteur`

```
fiche : asservissement
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 2. Constante de temps — `constante-de-temps`

- Niveau scolaire : TG (cycles TG)
- Règles automatiques encore enfreintes : aucune

**Version simple — avant** (22 mots) :
> C'est le temps que met un condensateur à se remplir ou à se vider en grande partie. Il dépend des composants choisis.

**Version simple — après** (33 mots) :
> C'est le temps que met un condensateur à se remplir ou à se vider en grande partie, comme le temps qu'il faut à un thé chaud pour refroidir. Il dépend des composants choisis.

**Sources après** (à ouvrir une par une) :
- [Programme de physique-chimie de terminale générale, enseignement de spécialité, « Modèle du circuit RC série »](https://www.education.gouv.fr/sites/default/files/document/Programme%20de%20physique-chimie%20de%20terminale%20g%C3%A9n%C3%A9rale-253485.pdf) — type `programme`

**Fiches liées après** : `circuit-rc`, `circuit-rl`, `condensateur`, `regime-transitoire`

```
fiche : constante-de-temps
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 3. Échantillonnage — `echantillonnage`

- Niveau scolaire : STI2D (cycles STI2D)
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (24 mots) :
> Opération qui relève la valeur d'un signal analogique à intervalles réguliers pour le convertir en nombres. Sa fréquence détermine la fidélité de la numérisation.

**Définition — après** (33 mots) :
> Opération qui relève la valeur d'un signal analogique à intervalles de temps réguliers pour la convertir en nombres. Le nombre de relevés par seconde, appelé fréquence d'échantillonnage, détermine la fidélité de la numérisation.

**Sources après** (à ouvrir une par une) :
- [Programme STI2D, enseignement technologique transversal (arrêté du 17 janvier 2019, modifié le 19 juillet 2019), « Conversion Analogique/Numérique (CAN) »](https://www.snes.edu/IMG/pdf/arrete_sti2d_ensemble.pdf) — type `programme`

**Fiches liées après** : `convertisseur-analogique-numerique-can`, `quantification`, `signal-analogique`, `signal-numerique`, `theoreme-de-shannon`

```
fiche : echantillonnage
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 4. Algèbre de Boole — `algebre-de-boole`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (32 mots) :
> Système de calcul sur des variables ne prenant que deux valeurs, vrai ou faux. Il fournit les règles qui permettent de simplifier un circuit logique avant de le réaliser avec des portes.

**Définition — après** (36 mots) :
> Système de calcul sur des variables ne prenant que deux valeurs, vrai ou faux, notées 1 et 0, avec des opérateurs comme ET, OU et NON. Les circuits logiques réalisent ces calculs à l'aide de portes.

**Version simple — avant** (20 mots) :
> C'est une façon de calculer avec seulement deux réponses possibles : oui ou non. Les ordinateurs raisonnent uniquement comme cela.

**Version simple — après** (27 mots) :
> C'est une façon de calculer avec seulement deux réponses : oui ou non. Par exemple, on sort jouer s'il fait beau ET si les devoirs sont finis.

**Sources après** (à ouvrir une par une) :
- [Programme de numérique et sciences informatiques de première générale, « Représentation des données : types et valeurs de base » (valeurs et opérateurs booléens)](https://eduscol.education.fr/document/30007/download) — type `programme`

**Fiches liées après** : `bit`, `circuit-logique`, `porte-logique`, `porte-ou-exclusif`, `signal-numerique`, `table-de-verite`

```
fiche : algebre-de-boole
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 5. Bit — `bit`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (32 mots) :
> Plus petite quantité d'information manipulée par un système numérique, qui ne peut valoir que zéro ou un. Un bit correspond physiquement à une tension basse ou haute sur une piste de circuit.

**Définition — après** (33 mots) :
> Plus petite unité d'information manipulée par une machine informatique, qui ne peut valoir que 0 ou 1. Les nombres entiers ou les caractères d'un texte y sont représentés par des suites de bits.

**Version simple — avant** (23 mots) :
> Un bit est la plus petite information possible : zéro ou un. Tout ce que fait un ordinateur est fabriqué avec des bits.

**Version simple — après** (31 mots) :
> Un bit est la plus petite information possible : 0 ou 1, comme une lampe éteinte ou allumée. Les photos et la musique d'un téléphone sont enregistrées avec énormément de bits.

**Sources après** (à ouvrir une par une) :
- [Programme de numérique et sciences informatiques de première générale, « Représentation des données : types et valeurs de base »](https://eduscol.education.fr/document/30007/download) — type `programme`

**Fiches liées après** : `algebre-de-boole`, `circuit-numerique`, `octet`, `quantification`, `registre-a-decalage`, `signal-numerique`, `systeme-binaire`, `systeme-hexadecimal`

```
fiche : bit
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 6. Bande interdite — `bande-interdite`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (33 mots) :
> Écart d'énergie que doit franchir un électron pour devenir libre dans un matériau. Très grand dans un isolant, nul dans un métal, il est modéré dans un semi-conducteur, ce qui rend celui-ci commandable.

**Définition — après** (31 mots) :
> Écart d'énergie qu'un électron doit franchir pour devenir libre de se déplacer dans un matériau. Grand dans un isolant, négligeable ou nul dans un métal, il est intermédiaire dans un semi-conducteur.

**Version simple — avant** (22 mots) :
> C'est la marche que doit franchir un électron pour se libérer. Trop haute, le matériau isole ; trop basse, il conduit toujours.

**Version simple — après** (31 mots) :
> C'est comme une marche d'escalier qu'un électron doit monter pour pouvoir se déplacer : très haute dans le plastique, qui isole, et presque absente dans le cuivre des fils, qui conduit.

**Sources après** (à ouvrir une par une) :
- [IEC 60050 (Electropedia), IEV 113-06-16 « gap energy » (énergie de bande interdite)](https://electropedia.org/iev/iev.nsf/17127c61f2426ed8c1257cb5003c9bec/690670e98b0338ccc1257e6e00293294) — type `reference`
- [Futura-Sciences, définition « Gap »](https://www.futura-sciences.com/sciences/definitions/physique-gap-5120/) — type `reference`

**Fiches liées après** : `conducteur-electrique`, `effet-photoelectrique`, `electron` (nouveau), `isolant-electrique`, `semi-conducteur`, `silicium`

```
fiche : bande-interdite
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 7. Dopage — `dopage`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (26 mots) :
> Introduction contrôlée d'impuretés dans un cristal semi-conducteur afin d'y ajouter des électrons libres ou des trous. C'est le dopage qui rend le silicium exploitable en électronique.

**Définition — après** (38 mots) :
> Introduction volontaire d'impuretés dans un cristal semi-conducteur afin de modifier sa conductivité électrique, en y ajoutant des électrons libres (dopage N) ou des trous (dopage P). Associer une région P et une région N forme une jonction PN.

**Version simple — avant** (15 mots) :
> On ajoute volontairement quelques atomes différents dans le silicium pour qu'il conduise mieux le courant.

**Version simple — après** (30 mots) :
> On ajoute volontairement quelques atomes d'un autre élément dans le silicium pour changer la façon dont il conduit le courant, comme une pincée de sel change le goût d'une soupe.

**Sources après** (à ouvrir une par une) :
- [Encyclopaedia Britannica, « Dopant »](https://www.britannica.com/print/article/169306) — type `reference`
- [IEC 60050 (Electropedia), IEV 521-02-04 « impurity » (impureté)](https://electropedia.org/iev/iev.nsf/17127c61f2426ed8c1257cb5003c9bec/392df7f5737c54bec125727c00311fa3) — type `reference`

**Fiches liées après** : `conductivite-electrique` (nouveau), `electron`, `jonction-pn`, `semi-conducteur`, `silicium`, `trou-electronique`

```
fiche : dopage
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 8. Jonction PN — `jonction-pn`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (35 mots) :
> Zone de contact entre une région de semi-conducteur dopée positivement et une région dopée négativement. Elle ne laisse passer le courant que dans un sens et constitue le cœur de la diode et du transistor.

**Définition — après** (38 mots) :
> Zone de transition entre une région de semi-conducteur dopée P et une région dopée N. Elle laisse passer facilement le courant dans un sens et très peu dans l'autre : c'est le principe de base de la diode.

**Version simple — avant** (18 mots) :
> En collant deux morceaux de silicium traités différemment, on obtient un passage à sens unique pour le courant.

**Version simple — après** (32 mots) :
> C'est la frontière entre deux parties d'un matériau préparées différemment : le courant y passe facilement dans un sens, presque pas dans l'autre, comme l'air dans la valve d'un pneu de vélo.

**Sources après** (à ouvrir une par une) :
- [IEC 60050 (Electropedia), IEV 521-02-72 « junction » (jonction)](https://electropedia.org/iev/iev.nsf/17127c61f2426ed8c1257cb5003c9bec/977896b8fdbaa993c125727c00312274) — type `reference`
- [IEC 60050 (Electropedia), IEV 521-05-03 « forward direction (of a PN junction) »](https://electropedia.org/iev/iev.nsf/17127c61f2426ed8c1257cb5003c9bec/dd9f2c6cfb7c5cccc125727c003126b4) — type `reference`
- [Energy Education (Université de Calgary), « P-n junction »](https://energyeducation.ca/encyclopedia/P-n_junction) — type `reference`

**Fiches liées après** : `diode`, `dopage`, `semi-conducteur`, `silicium`, `transistor`, `trou-electronique`

```
fiche : jonction-pn
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 9. Loi de Coulomb — `loi-de-coulomb`

- Niveau scolaire : 1G (cycles 1G)
- Règles automatiques encore enfreintes : aucune

**Version simple — avant** (25 mots) :
> Deux objets chargés se repoussent s'ils portent la même charge, et s'attirent sinon. Plus ils sont loin l'un de l'autre, plus cet effet devient faible.

**Version simple — après** (33 mots) :
> Deux objets chargés d'électricité se repoussent si leurs charges sont de même signe et s'attirent sinon : deux ballons frottés de la même façon s'écartent l'un de l'autre. L'effet faiblit avec la distance.

**Sources après** (à ouvrir une par une) :
- [Programme d'enseignement de spécialité de physique-chimie de première générale, « Interactions fondamentales et introduction à la notion de champ » (loi de Coulomb)](https://www.snes.edu/IMG/pdf/physique_spe_annexe_1eg_bo.pdf) — type `programme`
- [IEC 60050 (Electropedia), IEV 121-11-02 « Coulomb law » (loi de Coulomb)](https://electropedia.org/iev/iev.nsf/IEVref_xref/en:121-11-02) — type `reference`
- [Royal Institution, activité « Static magic »](https://www.rigb.org/learning/activities-and-resources/static-magic) — type `reference`

**Fiches liées après** : `champ-electrique`, `charge-electrique`, `coulomb`, `electron`, `electrostatique`

```
fiche : loi-de-coulomb
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 10. Machine à états — `machine-a-etats`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (29 mots) :
> Modèle de comportement dans lequel un système passe d'un état à un autre selon les événements reçus. Il structure la programmation des automatismes et la conception des circuits séquentiels.

**Définition — après** (41 mots) :
> Modèle de comportement dans lequel un système passe d'un état à un autre selon les événements reçus, chaque transition étant décrite par un graphe ou une table. Il sert à décrire le fonctionnement des automatismes et des circuits logiques à mémoire.

**Version simple — avant** (23 mots) :
> On décrit une machine par les situations où elle peut se trouver et par ce qui la fait passer de l'une à l'autre.

**Version simple — après** (29 mots) :
> On décrit une machine par les situations où elle peut être et ce qui la fait changer, comme un feu qui passe du vert à l'orange puis au rouge.

**Sources après** (à ouvrir une par une) :
- [IEC 60050 (Electropedia), IEV 351-53-06 « state graph » (graphe d'états)](https://electropedia.org/iev/iev.nsf/17127c61f2426ed8c1257cb5003c9bec/f124e1bdd76bca6ac1257b6d004347c6) — type `reference`
- [IEC 60050 (Electropedia), IEV 351-53-02 « state transition table »](https://electropedia.org/iev/iev.nsf/17127c61f2426ed8c1257cb5003c9bec/46ab73796eb80bfdc1257b6d0043472b) — type `reference`
- [Programme STI2D, enseignement technologique transversal (arrêté du 17 janvier 2019, modifié le 19 juillet 2019), « Diagramme d'états, d'activités »](https://www.snes.edu/IMG/pdf/arrete_sti2d_ensemble.pdf) — type `programme`

**Fiches liées après** : `asservissement`, `automate-programmable`, `bascule-flip-flop` (nouveau), `circuit-logique`, `fpga`, `microcontroleur`, `robotique`, `scenario-domotique`

```
fiche : machine-a-etats
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 11. Bras robotisé — `bras-robotise`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (27 mots) :
> Ensemble de segments articulés mus par des moteurs asservis, capable de positionner un outil dans l'espace. Chaque axe possède son codeur, et le calculateur coordonne leurs mouvements.

**Définition — après** (37 mots) :
> Structure mécanique articulée, par exemple à six axes, capable de positionner et d'orienter avec précision un outil porté à son extrémité. Un calculateur, placé dans une armoire de commande, convertit les consignes reçues en mouvements des axes.

**Version simple — avant** (21 mots) :
> C'est un bras mécanique commandé par des moteurs. Chaque articulation sait où elle se trouve, ce qui permet des gestes précis.

**Version simple — après** (27 mots) :
> C'est un bras mécanique qui bouge à plusieurs articulations, comme ton épaule, ton coude et ton poignet, et qu'un ordinateur commande pour placer un outil avec précision.

**Sources après** (à ouvrir une par une) :
- [Éduscol STI, « Le robot industriel FANUC M20i A » (support d'étude)](https://sti.eduscol.education.fr/print/8225) — type `reference`

**Fiches liées après** : `actionneur`, `asservissement`, `automate-programmable`, `codeur-rotatif`, `moteur-pas-a-pas`, `robotique`, `servomoteur`

```
fiche : bras-robotise
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 12. Histoire de l'électricité — `histoire-de-l-electricite`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (30 mots) :
> Parcours allant des premières observations d'électricité statique aux réseaux mondiaux actuels, en passant par la pile de Volta, l'induction de Faraday et l'éclairage urbain de la fin du dix-neuvième siècle.

**Définition — après** (42 mots) :
> Parcours allant des premières observations d'électricité statique, comme l'ambre frotté qui attire de petits objets, aux réseaux électriques actuels, en passant par la pile de Volta, l'induction électromagnétique découverte par Faraday et la lampe à incandescence de la fin du dix-neuvième siècle.

**Version simple — avant** (21 mots) :
> L'électricité a d'abord été une curiosité, avant de devenir en deux siècles ce qui fait fonctionner presque tout autour de nous.

**Version simple — après** (30 mots) :
> Il y a très longtemps, on a remarqué que l'ambre frotté attire de petits objets ; en deux siècles, l'électricité est devenue ce qui allume les lampes de nos maisons.

**Sources après** (à ouvrir une par une) :
- [Encyclopédie de l'énergie, N. Hadjsaïd et J.-C. Sabonnadière, « Histoire de l'électricité : de Thalès à la consommation du 21e siècle » (2015)](https://encyclopedie-energie.org/wp-content/uploads/2018/09/art026_Hadjsaid-Nourredine_Sabonnadiere-JeanClaude_Histoire-electricite-de-Thales-a-consommation-21e-siecle.pdf) — type `reference`

**Fiches liées après** : `eclairage`, `electricite`, `electrification`, `electrostatique` (nouveau), `induction-electromagnetique`, `pile-electrique`, `reseau-electrique` (nouveau)

```
fiche : histoire-de-l-electricite
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 13. Moteur à courant continu — `moteur-a-courant-continu`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (36 mots) :
> Moteur alimenté en continu dont la vitesse se règle simplement en agissant sur la tension. Son collecteur à balais s'use, ce qui limite sa durée de vie mais en fait un moteur très facile à piloter.

**Définition — après** (41 mots) :
> Moteur alimenté en courant continu dont le bobinage tournant est relié à l'alimentation par des contacts frottants, le collecteur et les balais, qui demandent un entretien régulier. Sa vitesse augmente avec la tension d'alimentation, ce qui permet de la régler simplement.

**Version simple — avant** (22 mots) :
> C'est le moteur des jouets et des petits robots : il tourne plus ou moins vite selon la tension qu'on lui donne.

**Version simple — après** (23 mots) :
> On le trouve par exemple dans des jouets à piles : il tourne plus ou moins vite selon la tension qu'on lui donne.

**Sources après** (à ouvrir une par une) :
- [IEC 60050 (Electropedia), IEV 411-31-05 « direct current machine » (machine à courant continu)](https://electropedia.org/iev/iev.nsf/17127c61f2426ed8c1257cb5003c9bec/0e2613943fead07bc12571ef0047f45d) — type `reference`
- [Schneider Electric, Cahier technique n° 207 « Les moteurs électriques… pour mieux les piloter et les protéger » (hébergé par Éduscol STI)](https://sti.eduscol.education.fr/sites/eduscol.education.fr.sti/files/ressources/techniques/690/690-ct207-moteurs-elec.pdf) — type `reference`
- [HPC, documentation technique « Moteurs à courant continu »](https://shop.hpceurope.com/docTech/fr/TechMoteurDC%2Epdf) — type `reference`

**Fiches liées après** : `courant-continu` (nouveau), `hacheur`, `modulation-de-largeur-d-impulsion-pwm`, `moteur-brushless`, `moteur-electrique`, `robotique`

```
fiche : moteur-a-courant-continu
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 14. Moteur asynchrone — `moteur-asynchrone`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (30 mots) :
> Moteur alimenté en triphasé dont le rotor tourne légèrement moins vite que le champ magnétique tournant du stator. Robuste et sans balais, il équipe la grande majorité des machines industrielles.

**Définition — après** (43 mots) :
> Moteur à courant alternatif, monophasé ou triphasé, dont la partie tournante, le rotor, tourne moins vite que le champ magnétique tournant créé par la partie fixe, le stator. Robuste et simple d'entretien, sa version triphasée à cage est la plus utilisée dans l'industrie.

**Version simple — avant** (19 mots) :
> C'est le moteur le plus courant dans les usines. Il est solide, simple, et fonctionne avec du courant triphasé.

**Version simple — après** (26 mots) :
> C'est l'un des moteurs les plus utilisés dans les usines. Solide et simple à entretenir, il fait tourner par exemple des pompes ou de grands ventilateurs.

**Sources après** (à ouvrir une par une) :
- [IEC 60050 (Electropedia), IEV 411-31-09 « asynchronous machine » (machine asynchrone)](https://electropedia.org/iev/iev.nsf/IEVref_xref/en:411-31-09) — type `reference`
- [Schneider Electric, Cahier technique n° 207 « Les moteurs électriques… pour mieux les piloter et les protéger » (hébergé par Éduscol STI)](https://sti.eduscol.education.fr/sites/eduscol.education.fr.sti/files/ressources/techniques/690/690-ct207-moteurs-elec.pdf) — type `reference`

**Fiches liées après** : `champ-magnetique`, `contacteur`, `convertisseur-de-frequence`, `courant-alternatif` (nouveau), `monophase` (nouveau), `moteur-electrique`, `moteur-synchrone`, `triphase`

```
fiche : moteur-asynchrone
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```
