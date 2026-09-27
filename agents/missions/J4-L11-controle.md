---
lot: J4-L11
role: controle
date: 2026-09-27
changeset: agents/changesets/J4-L11.jsonl
elements: ["frequence-de-coupure", "gain-electronique", "optocoupleur", "potentiometre", "quartz-resonateur", "relais-electronique", "rheostat", "tension-de-seuil", "transistor", "transistor-bipolaire"]
---

# Contrôle du lot J4-L11

10 fiche(s), 19 opération(s) du rédacteur (changeset non encore appliqué).

## Consignes du contrôleur

Tu es le **contrôleur** du lot J4-L11. Tu n'as pas participé à la rédaction et tu ne la vois qu'à
travers ce document : les justifications du rédacteur sont volontairement absentes. Tu vérifies
chaque fiche contre les **12 critères** de `docs/grille-relecture.md` (lis-la en entier d'abord).

1. **Ouvre chaque URL de source** et vérifie qu'elle appuie la définition. Une source que tu ne
   peux pas ouvrir, imprécise (page d'accueil) ou qui n'appuie pas l'affirmation = critère 8 en échec.
2. Une fiche est **conforme** si les 12 critères passent. Dans `agents/changesets/J4-L11-controle.jsonl`, remplace alors
   `"__A_REMPLIR__"` de `new` par
   `{"date": "2026-09-27", "par": "agent-controleur-J4-L11", "statut": "relu-ia"}` et `why` par
   « Relue selon la grille (12 critères) ».
3. Une fiche **refusée** : supprime sa ligne dans `agents/changesets/J4-L11-controle.jsonl`, et note les critères en échec. Tu ne
   réécris pas la fiche : le rédacteur la corrige (nouvelle passe de contrôle) ou la retire du lot.
   Si le défaut porte sur une fiche hors lot, ajoute-la à `agents/donnees/signalements.json`.
4. Écris tes verdicts dans la section « Relecture (rempli par le contrôleur) » de
   `agents/rapports/J4-L11.md`, une ligne par fiche : critères en échec, décision.
5. Vérifie : `python3 scripts/apply_changeset.py agents/changesets/J4-L11.jsonl agents/changesets/J4-L11-controle.jsonl --dry-run`.
   Tu ne poses **jamais** `"statut": "valide"` (réservé à Alexandre).


## Fiches à contrôler

### 1. Fréquence de coupure — `frequence-de-coupure`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [IUT en Ligne — Les filtres analogiques (Le Bars)](https://www.iutenligne.net/rsc/rsc-public/electronique/le-bars/analog/filtres.pdf) — type `manuel`

**Fiches liées après** : `bande-passante`, `decibel`, `diagramme-de-bode`, `filtre-electronique`, `filtre-passe-bas`, `filtre-passe-haut`

```
fiche : frequence-de-coupure
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 2. Gain (électronique) — `gain-electronique`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (20 mots) :
> Rapport entre l'amplitude d'un signal en sortie et en entrée d'un circuit, notamment d'un amplificateur opérationnel ou d'un amplificateur audio.

**Définition — après** (36 mots) :
> Rapport entre l'amplitude d'un signal en sortie et en entrée d'un circuit, notamment d'un amplificateur opérationnel ou d'un amplificateur audio. Il s'exprime souvent en décibels et caractérise l'amplification apportée par le circuit à un signal électrique.

**Sources après** (à ouvrir une par une) :
- [IUT en Ligne — L'amplificateur opérationnel (Ott)](https://www.iutenligne.net/rsc/rsc-public/electricite/ott/bases_de_l_electronique_analogique/6/aop.pdf) — type `manuel`

**Fiches liées après** : `amplificateur-audio`, `amplificateur-operationnel`, `decibel`, `diagramme-de-bode`, `distorsion`

```
fiche : gain-electronique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 3. Optocoupleur — `optocoupleur`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [Larousse — photocoupleur](https://www.larousse.fr/dictionnaires/francais/photocoupleur/60427) — type `reference`

**Fiches liées après** : `diode-electroluminescente-led`, `electronique-de-puissance`, `phototransistor`, `relais-electronique`, `relais-statique`

```
fiche : optocoupleur
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 4. Potentiomètre — `potentiometre`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [Larousse — potentiomètre](https://www.larousse.fr/dictionnaires/francais/potentiom%C3%A8tre/63001) — type `reference`

**Fiches liées après** : `carte-arduino`, `pont-diviseur-de-tension`, `resistance`, `rheostat`, `tension-electrique`

```
fiche : potentiometre
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 5. Quartz (résonateur) — `quartz-resonateur`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (20 mots) :
> Composant qui vibre à une fréquence précise sous l'effet d'une tension, utilisé pour stabiliser un oscillateur dans un circuit numérique.

**Définition — après** (37 mots) :
> Composant qui vibre à une fréquence précise et stable sous l'effet d'une tension, grâce à la piézoélectricité du cristal de quartz qui le compose. Il stabilise la fréquence d'un oscillateur, par exemple pour cadencer un circuit numérique.

**Sources après** (à ouvrir une par une) :
- [Larousse — quartz](https://www.larousse.fr/dictionnaires/francais/quartz/64798) — type `reference`

**Fiches liées après** : `circuit-numerique`, `oscillateur`, `piezoelectricite`, `resonance`, `signal-d-horloge`

```
fiche : quartz-resonateur
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 6. Relais électronique — `relais-electronique`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (23 mots) :
> Actionneur qui utilise un signal de faible puissance pour commander un circuit de plus forte puissance, jouant un rôle proche d'un interrupteur commandé.

**Définition — après** (34 mots) :
> Actionneur qui utilise un signal de commande de faible puissance pour établir ou couper un circuit de plus forte puissance, par un mécanisme électromécanique ou par des composants électroniques comme dans un relais statique.

**Sources après** (à ouvrir une par une) :
- [Larousse — relais](https://www.larousse.fr/dictionnaires/francais/relais/67074) — type `reference`

**Fiches liées après** : `actionneur`, `contacteur`, `optocoupleur`, `relais-statique`

```
fiche : relais-electronique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 7. Rhéostat — `rheostat`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [Larousse — rhéostat](https://www.larousse.fr/dictionnaires/francais/rh%C3%A9ostat/69233) — type `reference`

**Fiches liées après** : `courant-electrique`, `moteur-electrique`, `potentiometre`, `resistance`

```
fiche : rheostat
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 8. Tension de seuil — `tension-de-seuil`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (20 mots) :
> Valeur de tension à partir de laquelle un composant comme une diode ou un transistor commence à conduire le courant.

**Définition — après** (42 mots) :
> Valeur de tension à partir de laquelle un composant comme une diode ou un transistor commence à conduire le courant ; en dessous, il se comporte comme un interrupteur ouvert. Notée Vth, elle vaut environ 0,7 V pour une diode au silicium.

**Synonymes** : — → **Vth**

**Sources après** (à ouvrir une par une) :
- [IUT en Ligne — La diode à jonction PN (Marty)](https://www.iutenligne.net/rsc/rsc-public/electricite/marty/ELPU/fichiers/Chap1_1/Diode.htm) — type `manuel`

**Fiches liées après** : `diode`, `diode-schottky`, `diode-zener`, `interrupteur` (nouveau), `transistor`

```
fiche : tension-de-seuil
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 9. Transistor — `transistor`

- Niveau scolaire : 1-TG (cycles 1-TG)
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (19 mots) :
> Composant électronique semi-conducteur à trois électrodes qui amplifie ou commute un signal électrique, brique de base des circuits intégrés.

**Définition — après** (41 mots) :
> Composant électronique semi-conducteur à trois électrodes qui amplifie ou commute un signal électrique à partir d'un courant ou d'une tension de commande. Bipolaire ou à effet de champ, il est la brique de base des circuits intégrés, des amplificateurs aux processeurs.

**Sources après** (à ouvrir une par une) :
- [Larousse — transistor](https://www.larousse.fr/dictionnaires/francais/transistor/78188) — type `reference`
- [Programme de sciences de l'ingénieur, cycle terminal, voie générale (BO spécial n°1 du 22/01/2019)](https://www.pedagogie.ac-aix-marseille.fr/upload/docs/application/pdf/2019-01/bo_n1_22_janvier_2019.pdf#page=516) — type `programme`

**Fiches liées après** : `alimentation-a-decoupage`, `amplificateur-audio`, `composant-electronique`, `dissipateur-thermique`, `electronique`, `frequence-de-commutation`, `jonction-pn`, `mosfet`, `phototransistor`, `semi-conducteur`, `tension-de-seuil`, `transistor-a-effet-de-champ-fet`, `transistor-bipolaire`

```
fiche : transistor
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 10. Transistor bipolaire — `transistor-bipolaire`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (21 mots) :
> Type de transistor commandé par un courant appliqué sur sa base, utilisé pour l'amplification ou la commutation dans les circuits analogiques.

**Définition — après** (46 mots) :
> Type de transistor à trois électrodes (base, émetteur, collecteur) commandé par un faible courant appliqué sur sa base, qui contrôle un courant plus important entre émetteur et collecteur. Il existe en deux polarités, NPN et PNP, utilisées pour l'amplification ou la commutation dans les circuits analogiques.

**Synonymes** : — → **BJT**

**Sources après** (à ouvrir une par une) :
- [Le transistor bipolaire — P. Masson, École Polytechnique Universitaire de Nice Sophia-Antipolis (Polytech, Université Côte d'Azur)](https://users.polytech.unice.fr/~pmasson/Enseignement/Bipolaire%20Cours%20-%20Projection%20-%20MASSON.pdf) — type `manuel`

**Fiches liées après** : `transistor`, `transistor-igbt`

```
fiche : transistor-bipolaire
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```
