---
lot: J5-S5
role: controle
date: 2026-10-01
changeset: agents/changesets/J5-S5.jsonl
elements: ["asservissement", "constante-de-temps", "echantillonnage", "machine-a-etats", "moteur-a-courant-continu"]
---

# Contrôle du lot J5-S5 — passe 2

5 fiche(s), 49 opération(s) du rédacteur (changeset non encore appliqué).

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

**Version simple — avant** (21 mots) :
> Le système vérifie sans arrêt s'il fait bien ce qu'on lui a demandé, et se corrige tout seul quand il s'écarte.

**Version simple — après** (29 mots) :
> Le système vérifie sans arrêt s'il fait bien ce qu'on lui a demandé et se corrige tout seul, comme un four qui se remet à chauffer quand il refroidit.

**Sources après** (à ouvrir une par une) :
- [Arrêté fixant le programme des enseignements de spécialité des classes de première et terminale conduisant au baccalauréat technologique série STI2D (texte non daté, copie snes.edu), § 3.4.4 « Comportement des systèmes régulés ou asservis »](https://www.snes.edu/IMG/pdf/arrete_sti2d_ensemble.pdf) — type `programme`

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

**Fiches liées après** : `bobine-inductance` (nouveau), `circuit-rc`, `circuit-rl`, `condensateur`, `regime-transitoire`

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
- [IEC 60050 (Electropedia), IEV 704-23-02 « sampling (of a signal) » (échantillonnage)](https://electropedia.org/iev/iev.nsf/17127c61f2426ed8c1257cb5003c9bec/d368e0fa1011c472c1257245003c6d7e) — type `reference`
- [Arrêté fixant le programme des enseignements de spécialité des classes de première et terminale conduisant au baccalauréat technologique série STI2D (texte non daté, copie snes.edu), § 3.4.1 (signal « échantillonné »)](https://www.snes.edu/IMG/pdf/arrete_sti2d_ensemble.pdf) — type `programme`

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

### 4. Machine à états — `machine-a-etats`

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
- [Arrêté fixant le programme des enseignements de spécialité des classes de première et terminale conduisant au baccalauréat technologique série STI2D (texte non daté, copie snes.edu), § 3.4.2 « Description et simulation comportementale de l'information »](https://www.snes.edu/IMG/pdf/arrete_sti2d_ensemble.pdf) — type `programme`

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

### 5. Moteur à courant continu — `moteur-a-courant-continu`

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
- [HPC, « Moteur d'entraînement DC — Fiche technique » (tome 2, 2013)](https://shop.hpceurope.com/docTech/fr/TechMoteurDC%2Epdf) — type `reference`

**Fiches liées après** : `bobine-inductance` (nouveau), `courant-continu` (nouveau), `hacheur`, `modulation-de-largeur-d-impulsion-pwm`, `moteur-brushless`, `moteur-electrique`, `robotique`, `tension-electrique` (nouveau)

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
