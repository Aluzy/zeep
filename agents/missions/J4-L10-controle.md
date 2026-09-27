---
lot: J4-L10
role: controle
date: 2026-09-27
changeset: agents/changesets/J4-L10.jsonl
elements: ["amplificateur-operationnel", "bande-passante", "bobine-inductance", "bouton-poussoir", "circuit-analogique", "circuit-rc", "circuit-rl", "circuit-rlc", "composant-electronique", "condensateur", "diagramme-de-bode", "diode", "diode-electroluminescente-led", "diode-schottky", "diode-zener", "electronique", "filtre-electronique", "filtre-passe-bande", "filtre-passe-bas", "filtre-passe-haut"]
---

# Contrôle du lot J4-L10

20 fiche(s), 39 opération(s) du rédacteur (changeset non encore appliqué).

## Consignes du contrôleur

Tu es le **contrôleur** du lot J4-L10. Tu n'as pas participé à la rédaction et tu ne la vois qu'à
travers ce document : les justifications du rédacteur sont volontairement absentes. Tu vérifies
chaque fiche contre les **12 critères** de `docs/grille-relecture.md` (lis-la en entier d'abord).

1. **Ouvre chaque URL de source** et vérifie qu'elle appuie la définition. Une source que tu ne
   peux pas ouvrir, imprécise (page d'accueil) ou qui n'appuie pas l'affirmation = critère 8 en échec.
2. Une fiche est **conforme** si les 12 critères passent. Dans `agents/changesets/J4-L10-controle.jsonl`, remplace alors
   `"__A_REMPLIR__"` de `new` par
   `{"date": "2026-09-27", "par": "agent-controleur-J4-L10", "statut": "relu-ia"}` et `why` par
   « Relue selon la grille (12 critères) ».
3. Une fiche **refusée** : supprime sa ligne dans `agents/changesets/J4-L10-controle.jsonl`, et note les critères en échec. Tu ne
   réécris pas la fiche : le rédacteur la corrige (nouvelle passe de contrôle) ou la retire du lot.
   Si le défaut porte sur une fiche hors lot, ajoute-la à `agents/donnees/signalements.json`.
4. Écris tes verdicts dans la section « Relecture (rempli par le contrôleur) » de
   `agents/rapports/J4-L10.md`, une ligne par fiche : critères en échec, décision.
5. Vérifie : `python3 scripts/apply_changeset.py agents/changesets/J4-L10.jsonl agents/changesets/J4-L10-controle.jsonl --dry-run`.
   Tu ne poses **jamais** `"statut": "valide"` (réservé à Alexandre).


## Fiches à contrôler

### 1. Amplificateur opérationnel — `amplificateur-operationnel`

- Niveau scolaire : STI2D (cycles STI2D)
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (21 mots) :
> Circuit intégré analogique qui amplifie la différence entre deux signaux d'entrée, largement utilisé dans les filtres électroniques et les amplificateurs audio.

**Définition — après** (37 mots) :
> Circuit intégré analogique à deux entrées et une sortie, qui amplifie fortement la différence entre ses deux signaux d'entrée. Associé à des résistances ou à des condensateurs, il réalise des amplificateurs, des filtres électroniques ou des oscillateurs.

**Synonymes** : AOP, ampli op, amplificateur operationnel → **ALI, AOP, ampli op, amplificateur lineaire integre, amplificateur operationnel**

**Sources après** (à ouvrir une par une) :
- [IUT en Ligne — Hugues Ott, Amplificateur opérationnel (A.O)](https://www.iutenligne.net/rsc/rsc-public/electricite/ott/bases_de_l_electronique_analogique/6/aop.pdf) — type `manuel`

**Fiches liées après** : `amplificateur-audio`, `circuit-integre`, `condensateur` (nouveau), `distorsion`, `gain-electronique`, `oscillateur` (nouveau), `resistance` (nouveau), `signal-analogique`

```
fiche : amplificateur-operationnel
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 2. Bande passante — `bande-passante`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [IUT en Ligne — Pierre Le Bars, Filtres actifs](https://www.iutenligne.net/rsc/rsc-public/electronique/le-bars/analog/filtres.pdf) — type `manuel`

**Fiches liées après** : `amplificateur-audio`, `analyseur-de-spectre`, `antenne`, `decibel`, `filtre-passe-bande`, `frequence-de-coupure`, `signal-audio`, `theoreme-de-shannon`

```
fiche : bande-passante
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 3. Bobine (inductance) — `bobine-inductance`

- Niveau scolaire : 1-TG (cycles 1-TG)
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (23 mots) :
> Composant électronique constitué d'un enroulement de fil qui s'oppose aux variations du courant, utilisé dans les filtres électroniques et les alimentations à découpage.

**Définition — après** (36 mots) :
> Composant électronique constitué d'un enroulement de fil conducteur qui s'oppose aux variations du courant en emmagasinant de l'énergie dans un champ magnétique. Elle intervient dans les filtres électroniques, les alimentations à découpage et les circuits RL.

**Sources après** (à ouvrir une par une) :
- [Larousse — bobine d'inductance](https://www.larousse.fr/dictionnaires/francais/bobine/9955#168854) — type `reference`

**Fiches liées après** : `champ-magnetique` (nouveau), `circuit-rl`, `composant-electronique`, `dephasage`, `electronique`, `hacheur`, `haut-parleur`, `henry`, `impedance`, `loi-de-lenz`, `puissance-reactive`, `reactance`, `regime-transitoire`, `weber`

```
fiche : bobine-inductance
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 4. Bouton poussoir — `bouton-poussoir`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [Larousse — bouton-poussoir](https://www.larousse.fr/dictionnaires/francais/bouton-poussoir/10778) — type `reference`

**Fiches liées après** : `carte-arduino`, `circuit-logique`, `gpio`, `interrupteur`, `resistance`

```
fiche : bouton-poussoir
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 5. Circuit analogique — `circuit-analogique`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (18 mots) :
> Circuit électronique qui traite des signaux analogiques dont l'amplitude varie de façon continue, par opposition au circuit numérique.

**Définition — après** (39 mots) :
> Circuit électronique qui traite des signaux analogiques, dont l'amplitude varie de façon continue dans le temps, par opposition au circuit numérique qui ne connaît que des états binaires. Un amplificateur ou un filtre électronique en sont des exemples courants.

**Sources après** (à ouvrir une par une) :
- [IUT en Ligne — Signal analogique, signal numérique](https://www.iutenligne.net/rsc/rsc-public/telecommunications/berthet/module-signaux-systeme/AnalogiqueNumerique/index.html) — type `manuel`

**Fiches liées après** : `circuit-numerique`, `electronique`, `filtre-electronique` (nouveau), `simulation-spice`

```
fiche : circuit-analogique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 6. Circuit RC — `circuit-rc`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [Programme de physique-chimie de terminale générale (BO spécial n°1 du 22/01/2019)](https://www.education.gouv.fr/sites/default/files/document/Programme%20de%20physique-chimie%20de%20terminale%20g%C3%A9n%C3%A9rale-253485.pdf) — type `programme`

**Fiches liées après** : `circuit-rlc`, `condensateur`, `constante-de-temps`, `filtre-passe-bas`, `filtre-passe-haut`, `regime-transitoire`, `resistance`

```
fiche : circuit-rc
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 7. Circuit RL — `circuit-rl`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [IUT en Ligne — Hugues Ott, Résonance d'intensité (circuit RLC série)](https://www.iutenligne.net/rsc/rsc-public/electricite/ott/bases_de_l_electronique_analogique/4/rlc_serie.pdf) — type `manuel`

**Fiches liées après** : `bobine-inductance`, `circuit-rlc`, `constante-de-temps`, `regime-transitoire`, `resistance`

```
fiche : circuit-rl
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 8. Circuit RLC — `circuit-rlc`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [IUT en Ligne — Hugues Ott, Résonance d'intensité (circuit RLC série)](https://www.iutenligne.net/rsc/rsc-public/electricite/ott/bases_de_l_electronique_analogique/4/rlc_serie.pdf) — type `manuel`

**Fiches liées après** : `circuit-rc`, `circuit-rl`, `filtre-passe-bande`, `recepteur-radiofrequence`, `resonance`

```
fiche : circuit-rlc
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 9. Composant électronique — `composant-electronique`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (21 mots) :
> Élément de base, comme une résistance, un condensateur ou un transistor, assemblé sur un circuit imprimé pour constituer un circuit électronique.

**Définition — après** (41 mots) :
> Élément de base d'un circuit électronique, comme une résistance, un condensateur, une diode ou un transistor, assemblé sur un circuit imprimé. On distingue les composants passifs, qui ne font que consommer ou stocker de l'énergie, des composants actifs comme les transistors.

**Sources après** (à ouvrir une par une) :
- [Larousse — composant](https://www.larousse.fr/dictionnaires/francais/composant/17735) — type `reference`

**Fiches liées après** : `actionneur`, `bobine-inductance`, `capteur`, `circuit-imprime-pcb`, `code-couleur-des-resistances`, `condensateur`, `datasheet-fiche-technique`, `decharge-electrostatique`, `diode`, `dissipateur-thermique`, `electronique`, `indice-de-reparabilite`, `montage-en-surface`, `recyclage-des-dechets-electroniques-deee`, `refusion`, `resistance`, `terres-rares`, `transistor`

```
fiche : composant-electronique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 10. Condensateur — `condensateur`

- Niveau scolaire : 1-TG (cycles 1-TG, TG, STI2D)
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (20 mots) :
> Composant électronique qui stocke une charge électrique entre deux armatures, utilisé notamment dans les filtres électroniques et les alimentations électroniques.

**Définition — après** (36 mots) :
> Composant électronique formé de deux conducteurs, appelés armatures, séparés par un isolant ; il stocke une charge électrique proportionnelle à la tension appliquée entre ses bornes. Il équipe notamment les filtres électroniques et les alimentations électroniques.

**Sources après** (à ouvrir une par une) :
- [Larousse — condensateur](https://www.larousse.fr/dictionnaires/francais/condensateur/18000) — type `reference`
- [Programme de physique-chimie de terminale générale (BO spécial n°1 du 22/01/2019)](https://www.education.gouv.fr/sites/default/files/document/Programme%20de%20physique-chimie%20de%20terminale%20g%C3%A9n%C3%A9rale-253485.pdf) — type `programme`

**Fiches liées après** : `amplificateur-operationnel` (nouveau), `circuit-rc`, `composant-electronique`, `constante-de-temps`, `dephasage`, `dielectrique`, `electronique`, `facteur-de-puissance`, `farad`, `impedance`, `microphone`, `puissance-reactive`, `reactance`, `redresseur`, `regime-transitoire`, `supercondensateur`

```
fiche : condensateur
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 11. Diagramme de Bode — `diagramme-de-bode`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [IUT en Ligne — Pierre Le Bars, Filtres actifs](https://www.iutenligne.net/rsc/rsc-public/electronique/le-bars/analog/filtres.pdf) — type `manuel`

**Fiches liées après** : `decibel`, `dephasage`, `filtre-electronique`, `frequence-de-coupure`, `gain-electronique`, `simulation-spice`

```
fiche : diagramme-de-bode
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 12. Diode — `diode`

- Niveau scolaire : 1-TG (cycles 1-TG)
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (21 mots) :
> Composant électronique semi-conducteur qui ne laisse passer le courant que dans un seul sens, utilisé notamment dans les circuits de redresseur.

**Définition — après** (39 mots) :
> Composant électronique à semi-conducteur, formé d'une jonction entre une région dopée P et une région dopée N, qui ne laisse passer le courant que dans un seul sens. On l'utilise notamment dans les circuits redresseurs et les diodes électroluminescentes.

**Sources après** (à ouvrir une par une) :
- [Larousse — diode](https://www.larousse.fr/dictionnaires/francais/diode/25662) — type `reference`
- [IUT en Ligne — Constitution de la diode à jonction PN](https://www.iutenligne.net/rsc/rsc-public/electricite/marty/ELPU/fichiers/Chap1_1/Diode.htm) — type `manuel`

**Fiches liées après** : `caracteristique-tension-courant`, `composant-electronique`, `diode-electroluminescente-led`, `diode-schottky`, `diode-zener`, `electronique`, `jonction-pn`, `photodiode`, `pont-de-diodes`, `redresseur`, `semi-conducteur`, `tension-de-seuil`

```
fiche : diode
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 13. Diode électroluminescente (LED) — `diode-electroluminescente-led`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (24 mots) :
> Diode qui émet de la lumière lorsqu'elle est traversée par un courant électrique, largement utilisée en éclairage et sur les cartes électroniques comme voyant.

**Définition — après** (36 mots) :
> Diode qui émet de la lumière, dont la couleur dépend du semi-conducteur utilisé, lorsqu'un courant la traverse dans le sens passant. Elle consomme peu d'énergie et sert de voyant sur les cartes électroniques, ou pour l'éclairage.

**Sources après** (à ouvrir une par une) :
- [Larousse — diode électroluminescente (DEL)](https://www.larousse.fr/dictionnaires/francais/diode/25662#752629) — type `reference`

**Fiches liées après** : `diode`, `optocoupleur`, `semi-conducteur` (nouveau)

```
fiche : diode-electroluminescente-led
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 14. Diode Schottky — `diode-schottky`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [Larousse — Schottky (diode)](https://www.larousse.fr/dictionnaires/francais/diode_Schottky/71441) — type `reference`

**Fiches liées après** : `alimentation-a-decoupage`, `diode`, `redresseur`, `semi-conducteur`, `tension-de-seuil`

```
fiche : diode-schottky
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 15. Diode Zener — `diode-zener`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [Larousse — Zener (diode de)](https://www.larousse.fr/dictionnaires/francais/diode_de_Zener/83085) — type `reference`

**Fiches liées après** : `diode`, `regulateur-de-tension`, `semi-conducteur`, `tension-de-seuil`

```
fiche : diode-zener
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 16. Électronique — `electronique`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (21 mots) :
> Discipline scientifique et technique qui étudie et exploite les composants électroniques pour traiter, amplifier ou transformer des signaux analogiques et numériques.

**Définition — après** (38 mots) :
> Discipline scientifique et technique qui étudie et exploite les variations de grandeurs électriques, comme les courants et les tensions, pour capter, transmettre et exploiter de l'information. Elle regroupe les composants électroniques, les circuits analogiques et les circuits numériques.

**Sources après** (à ouvrir une par une) :
- [Larousse — électronique](https://www.larousse.fr/dictionnaires/francais/%C3%A9lectronique/28301#28164) — type `reference`

**Fiches liées après** : `actionneur`, `alimentation-a-decoupage`, `alimentation-electronique`, `amplificateur-audio`, `batterie-lithium-ion`, `bobine-inductance`, `boitier-electronique`, `bruit-electronique`, `capteur`, `capteur-de-pression`, `capteur-de-temperature`, `carte-arduino`, `carte-mere`, `carte-raspberry-pi`, `circuit-analogique`, `circuit-imprime-pcb`, `circuit-integre`, `circuit-numerique`, `compatibilite-electromagnetique-cem`, `composant-electronique`, `condensateur`, `court-circuit`, `datasheet-fiche-technique`, `diode`, `dissipateur-thermique`, `domotique`, `electronique-de-puissance`, `emetteur-radiofrequence`, `fer-a-souder`, `filtre-electronique`, `filtre-passe-bande`, `filtre-passe-bas`, `filtre-passe-haut`, `impedance`, `interference-electromagnetique`, `memoire-morte-rom`, `memoire-vive-ram`, `mosfet`, `oscillateur`, `plaque-d-essai-breadboard`, `porte-logique`, `prototypage-electronique`, `recepteur-radiofrequence`, `recyclage-des-dechets-electroniques-deee`, `redresseur`, `regulateur-de-tension`, `resistance`, `robotique`, `silicium`, `thyristor`, `transistor`, `usb`, `ventilateur-de-refroidissement`

```
fiche : electronique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 17. Filtre électronique — `filtre-electronique`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (21 mots) :
> Circuit électronique, composé de résistances, de condensateurs ou de bobines, qui sélectionne certaines fréquences d'un signal analogique et en atténue d'autres.

**Définition — après** (36 mots) :
> Circuit électronique, composé de résistances, de condensateurs ou de bobines, qui laisse passer certaines fréquences d'un signal et atténue les autres. On distingue notamment les filtres passe-bas, passe-haut et passe-bande selon la plage de fréquences conservée.

**Sources après** (à ouvrir une par une) :
- [Larousse — filtre électrique](https://www.larousse.fr/dictionnaires/francais/filtre/33777#10954736) — type `reference`
- [IUT en Ligne — Pierre Le Bars, Filtres actifs](https://www.iutenligne.net/rsc/rsc-public/electronique/le-bars/analog/filtres.pdf) — type `manuel`

**Fiches liées après** : `bruit-electronique`, `circuit-analogique` (nouveau), `decibel`, `diagramme-de-bode`, `electronique`, `filtre-passe-bande`, `filtre-passe-bas`, `filtre-passe-haut`, `frequence-de-coupure`, `generateur-de-fonctions`, `harmoniques`, `signal-analogique`

```
fiche : filtre-electronique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 18. Filtre passe-bande — `filtre-passe-bande`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (19 mots) :
> Filtre électronique qui ne laisse passer qu'une plage de fréquences comprise entre un filtre passe-bas et un filtre passe-haut.

**Définition — après** (35 mots) :
> Filtre électronique qui ne laisse passer qu'une plage de fréquences comprise entre une fréquence de coupure basse et une fréquence de coupure haute, en atténuant tout ce qui se trouve hors de cette bande passante.

**Sources après** (à ouvrir une par une) :
- [IUT en Ligne — Pierre Le Bars, Filtres actifs](https://www.iutenligne.net/rsc/rsc-public/electronique/le-bars/analog/filtres.pdf) — type `manuel`

**Fiches liées après** : `bande-passante`, `circuit-rlc`, `electronique`, `filtre-electronique`, `filtre-passe-bas`, `filtre-passe-haut`, `resonance`

```
fiche : filtre-passe-bande
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 19. Filtre passe-bas — `filtre-passe-bas`

- Niveau scolaire : STI2D (cycles STI2D)
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (19 mots) :
> Filtre électronique qui laisse passer les basses fréquences d'un signal et atténue les fréquences supérieures à un seuil donné.

**Définition — après** (33 mots) :
> Filtre électronique qui laisse passer les basses fréquences d'un signal et atténue celles supérieures à sa fréquence de coupure. Le circuit RC est l'exemple le plus simple de filtre passe-bas du premier ordre.

**Sources après** (à ouvrir une par une) :
- [IUT en Ligne — Pierre Le Bars, Filtres actifs](https://www.iutenligne.net/rsc/rsc-public/electronique/le-bars/analog/filtres.pdf) — type `manuel`

**Fiches liées après** : `circuit-rc`, `electronique`, `filtre-electronique`, `filtre-passe-bande`, `frequence-de-coupure`, `theoreme-de-shannon`

```
fiche : filtre-passe-bas
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 20. Filtre passe-haut — `filtre-passe-haut`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (19 mots) :
> Filtre électronique qui laisse passer les hautes fréquences d'un signal et atténue les fréquences inférieures à un seuil donné.

**Définition — après** (28 mots) :
> Filtre électronique qui laisse passer les hautes fréquences d'un signal et atténue celles inférieures à sa fréquence de coupure, utilisé par exemple pour éliminer une composante continue parasite.

**Sources après** (à ouvrir une par une) :
- [IUT en Ligne — Pierre Le Bars, Filtres actifs](https://www.iutenligne.net/rsc/rsc-public/electronique/le-bars/analog/filtres.pdf) — type `manuel`

**Fiches liées après** : `circuit-rc`, `electronique`, `filtre-electronique`, `filtre-passe-bande`, `frequence-de-coupure`

```
fiche : filtre-passe-haut
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```
