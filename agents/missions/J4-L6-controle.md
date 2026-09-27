---
lot: J4-L6
role: controle
date: 2026-09-27
changeset: agents/changesets/J4-L6.jsonl
elements: ["ampere", "amperemetre", "atome", "champ-electrique", "champ-magnetique", "charge-electrique", "conductivite-electrique", "coulomb", "courant-alternatif", "courant-continu", "courant-electrique", "decibel", "dephasage", "dipole", "electromagnetisme", "electron", "electrostatique", "energie-electrique", "effet-photoelectrique", "electrolyse"]
---

# Contrôle du lot J4-L6

20 fiche(s), 41 opération(s) du rédacteur (changeset non encore appliqué).

## Consignes du contrôleur

Tu es le **contrôleur** du lot J4-L6. Tu n'as pas participé à la rédaction et tu ne la vois qu'à
travers ce document : les justifications du rédacteur sont volontairement absentes. Tu vérifies
chaque fiche contre les **12 critères** de `docs/grille-relecture.md` (lis-la en entier d'abord).

1. **Ouvre chaque URL de source** et vérifie qu'elle appuie la définition. Une source que tu ne
   peux pas ouvrir, imprécise (page d'accueil) ou qui n'appuie pas l'affirmation = critère 8 en échec.
2. Une fiche est **conforme** si les 12 critères passent. Dans `agents/changesets/J4-L6-controle.jsonl`, remplace alors
   `"__A_REMPLIR__"` de `new` par
   `{"date": "2026-09-27", "par": "agent-controleur-J4-L6", "statut": "relu-ia"}` et `why` par
   « Relue selon la grille (12 critères) ».
3. Une fiche **refusée** : supprime sa ligne dans `agents/changesets/J4-L6-controle.jsonl`, et note les critères en échec. Tu ne
   réécris pas la fiche : le rédacteur la corrige (nouvelle passe de contrôle) ou la retire du lot.
   Si le défaut porte sur une fiche hors lot, ajoute-la à `agents/donnees/signalements.json`.
4. Écris tes verdicts dans la section « Relecture (rempli par le contrôleur) » de
   `agents/rapports/J4-L6.md`, une ligne par fiche : critères en échec, décision.
5. Vérifie : `python3 scripts/apply_changeset.py agents/changesets/J4-L6.jsonl agents/changesets/J4-L6-controle.jsonl --dry-run`.
   Tu ne poses **jamais** `"statut": "valide"` (réservé à Alexandre).


## Fiches à contrôler

### 1. Ampère — `ampere`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (12 mots) :
> Unité de mesure de l'intensité électrique dans le Système international, symbole A.

**Définition — après** (38 mots) :
> Unité de mesure de l'intensité électrique dans le Système international, de symbole A. Un courant électrique d'un ampère transporte, en une seconde, une charge électrique d'un coulomb ; c'est l'une des sept unités de base du Système international.

**Sources après** (à ouvrir une par une) :
- [Larousse, « ampère »](https://www.larousse.fr/dictionnaires/francais/amp%C3%A8re/3038) — type `reference`

**Fiches liées après** : `amperage`, `ampere-heure`, `charge-electrique` (nouveau), `coulomb`, `courant-electrique` (nouveau), `intensite-electrique`

```
fiche : ampere
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 2. Ampèremètre — `amperemetre`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (14 mots) :
> Instrument de mesure de l'intensité électrique circulant dans un conducteur électrique, exprimée en ampères.

**Définition — après** (35 mots) :
> Instrument de mesure de l'intensité du courant électrique dans un circuit, exprimée en ampères. Il se branche en série dans le circuit, de façon à être traversé par le même courant que le composant étudié.

**Sources après** (à ouvrir une par une) :
- [Larousse, « ampèremètre »](https://www.larousse.fr/dictionnaires/francais/amp%C3%A8rem%C3%A8tre/3040) — type `reference`

**Fiches liées après** : `amperage`, `circuit-electrique` (nouveau), `conducteur-electrique`, `courant-electrique` (nouveau), `intensite-electrique`, `loi-des-noeuds`, `multimetre`, `pince-amperemetrique`

```
fiche : amperemetre
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 3. Atome — `atome`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [Programme du cycle 4 (BOEN n° 31 du 30 juillet 2020), thème « Organisation et transformations de la matière », p. 100 (constituants de l'atome, structure interne du noyau, électrons)](https://eduscol.education.gouv.fr/sites/default/files/document/programme-d-enseignement-du-cycle-4-67722.pdf#page=100) — type `programme`

**Fiches liées après** : `charge-electrique`, `conducteur-electrique`, `electron`, `ion`, `isolant-electrique`

```
fiche : atome
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 4. Champ électrique — `champ-electrique`

- Niveau scolaire : 1G (cycles 1G)
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (18 mots) :
> Région de l'espace dans laquelle une charge électrique subit une force, créée par la présence d'autres charges électriques.

**Définition — après** (39 mots) :
> Région de l'espace où une charge électrique immobile ou en mouvement subit une force électrique, engendrée par la présence d'autres charges électriques. Il se représente par un vecteur en tout point, dont l'intensité se mesure en volts par mètre.

**Sources après** (à ouvrir une par une) :
- [Programme de physique-chimie de première générale, enseignement de spécialité (BO spécial n° 1 du 22 janvier 2019), partie « Mouvement et interactions », p. 499 (force et champ électrostatiques)](https://www.pedagogie.ac-aix-marseille.fr/upload/docs/application/pdf/2019-01/bo_n1_22_janvier_2019.pdf#page=499) — type `programme`
- [Larousse, « champ électrique »](https://www.larousse.fr/dictionnaires/francais/champ/14557#152185) — type `reference`

**Fiches liées après** : `charge-electrique`, `dielectrique`, `electromagnetisme`, `electrostatique`, `loi-de-coulomb`

```
fiche : champ-electrique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 5. Champ magnétique — `champ-magnetique`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (21 mots) :
> Région de l'espace dans laquelle un aimant ou un courant électrique exerce une force sur d'autres aimants ou charges en mouvement.

**Définition — après** (39 mots) :
> Région de l'espace où un aimant ou un courant électrique exerce une force sur d'autres aimants, sur des charges électriques en mouvement ou sur d'autres courants électriques. Il se représente par un vecteur, dont l'intensité se mesure en teslas.

**Sources après** (à ouvrir une par une) :
- [Larousse, « champ magnétique »](https://www.larousse.fr/dictionnaires/francais/champ/14557#152187) — type `reference`

**Fiches liées après** : `charge-electrique` (nouveau), `courant-electrique`, `effet-hall`, `electromagnetisme`, `haut-parleur`, `induction-electromagnetique`, `loi-de-lenz`, `moteur-asynchrone`, `pince-amperemetrique`, `supraconductivite`, `tesla`, `weber`

```
fiche : champ-magnetique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 6. Charge électrique — `charge-electrique`

- Niveau scolaire : 1G (cycles 1G)
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (24 mots) :
> Propriété fondamentale de la matière, portée notamment par l'électron, qui est à l'origine des phénomènes électriques comme le courant électrique et le champ électrique.

**Définition — après** (38 mots) :
> Propriété fondamentale de la matière, portée notamment par l'électron, qui est à l'origine du courant électrique et du champ électrique. Elle s'exprime en coulombs et peut être positive ou négative selon le sens des charges qui la portent.

**Sources après** (à ouvrir une par une) :
- [Larousse, « charge électrique »](https://www.larousse.fr/dictionnaires/francais/charge/14743#152373) — type `reference`

**Fiches liées après** : `ampere` (nouveau), `atome`, `champ-electrique`, `champ-magnetique` (nouveau), `conducteur-electrique`, `coulomb`, `courant-electrique`, `decharge-electrostatique`, `electricite`, `electron`, `farad`, `intensite-electrique`, `ion`, `isolant-electrique`, `loi-de-coulomb`, `loi-des-noeuds`, `tension-electrique`, `trou-electronique`

```
fiche : charge-electrique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 7. Conductivité électrique — `conductivite-electrique`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (13 mots) :
> Aptitude d'un matériau à laisser circuler le courant électrique, inverse de la résistivité.

**Définition — après** (41 mots) :
> Grandeur physique qui caractérise l'aptitude d'un matériau à laisser passer le courant électrique sous l'effet d'une tension : plus elle est élevée, plus le matériau conduit facilement le courant. Elle s'exprime en siemens par mètre et vaut l'inverse de la résistivité.

**Sources après** (à ouvrir une par une) :
- [Larousse, « conductibilité »](https://www.larousse.fr/dictionnaires/francais/conductibilit%C3%A9/18036) — type `reference`

**Fiches liées après** : `courant-electrique`, `resistivite`, `siemens`, `tension-electrique` (nouveau), `theoreme-de-millman`

```
fiche : conductivite-electrique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 8. Coulomb — `coulomb`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [BIPM, « Le Système international d'unités » (9e édition, version française, 2019), p. 14 (relation C = A·s)](https://www.bipm.org/documents/20126/41483022/SI-Brochure-9-FR.pdf#page=14) — type `norme`
- [Larousse, « coulomb »](https://www.larousse.fr/dictionnaires/francais/coulomb/19779) — type `reference`

**Fiches liées après** : `ampere`, `charge-electrique`, `courant-electrique`, `electron`, `farad`, `loi-de-coulomb`

```
fiche : coulomb
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 9. Courant alternatif — `courant-alternatif`

- Niveau scolaire : 1-TG (cycles 1-TG, STI2D)
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (19 mots) :
> Courant électrique dont le sens et l'intensité varient périodiquement, caractérisé par sa fréquence électrique, utilisé sur le réseau électrique.

**Définition — après** (35 mots) :
> Courant électrique dont l'intensité varie périodiquement dans le temps et change de sens, à la différence du courant continu. Sur le réseau électrique français, il varie de façon sinusoïdale à la fréquence de 50 hertz.

**Sources après** (à ouvrir une par une) :
- [Larousse, « alternatif »](https://www.larousse.fr/dictionnaires/francais/alternatif/2566) — type `reference`

**Fiches liées après** : `alternateur`, `borne-de-recharge`, `convertisseur-de-frequence`, `courant-continu` (nouveau), `courant-electrique`, `dephasage`, `electrocution`, `frequence-electrique`, `harmoniques`, `hertz`, `impedance`, `monophase`, `neutre`, `onduleur`, `panneau-photovoltaique`, `periode`, `phase-electrique`, `pont-de-diodes`, `redresseur`, `reseau-electrique`, `transformateur`, `triac`, `triphase`, `valeur-crete`, `valeur-efficace`

```
fiche : courant-alternatif
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 10. Courant continu — `courant-continu`

- Niveau scolaire : BACPRO (cycles BACPRO, STI2D)
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (17 mots) :
> Courant électrique circulant toujours dans le même sens, produit notamment par une batterie ou un panneau photovoltaïque.

**Définition — après** (31 mots) :
> Courant électrique dont l'intensité garde toujours le même sens, produit notamment par une batterie, un panneau photovoltaïque ou une dynamo, à la différence du courant alternatif utilisé sur le réseau électrique.

**Sources après** (à ouvrir une par une) :
- [Larousse, « continu »](https://www.larousse.fr/dictionnaires/francais/continu/18615) — type `reference`

**Fiches liées après** : `batterie`, `borne-de-recharge`, `courant-alternatif` (nouveau), `courant-electrique`, `dynamo`, `electrolyse`, `onduleur`, `panneau-photovoltaique`, `pont-de-diodes`, `puissance-electrique`, `redresseur`, `reseau-electrique` (nouveau), `valeur-efficace`

```
fiche : courant-continu
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 11. Courant électrique — `courant-electrique`

- Niveau scolaire : 1G (cycles 1G, CAP, BACPRO)
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (18 mots) :
> Déplacement ordonné de charges électriques dans un conducteur électrique, mesuré en ampères et caractérisé par son intensité électrique.

**Définition — après** (48 mots) :
> Déplacement d'ensemble de charges électriques, notamment des électrons, dans un conducteur électrique. Son intensité, exprimée en ampères, mesure le débit de charge qui traverse une section du conducteur chaque seconde ; il peut être continu ou alternatif selon que ce déplacement garde ou non toujours le même sens.

**Sources après** (à ouvrir une par une) :
- [Larousse, « courant (électrique) »](https://www.larousse.fr/dictionnaires/francais/courant/19881#154173) — type `reference`

**Fiches liées après** : `accumulateur`, `alimentation-electrique`, `ampere` (nouveau), `amperemetre` (nouveau), `cable-electrique`, `champ-magnetique`, `charge-electrique`, `circuit-electrique`, `circuit-ferme`, `circuit-ouvert`, `conducteur-electrique`, `conductivite-electrique`, `coulomb`, `courant-alternatif`, `courant-continu`, `disjoncteur`, `electricite`, `electrisation`, `electrocution`, `electromagnetisme`, `electron`, `generateur-electrique`, `intensite-electrique`, `interrupteur`, `isolant-electrique`, `loi-des-noeuds`, `neutre`, `phase-electrique`, `pont-diviseur-de-courant`, `production-d-electricite`, `resistance-electrique`, `resistivite`, `rheostat`, `tension-electrique`, `theoreme-de-norton`

```
fiche : courant-electrique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 12. Décibel — `decibel`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [Larousse, « décibel »](https://www.larousse.fr/dictionnaires/francais/d%C3%A9cibel/22175) — type `reference`

**Fiches liées après** : `amplificateur-audio`, `bande-passante`, `diagramme-de-bode`, `filtre-electronique`, `frequence-de-coupure`, `gain-electronique`

```
fiche : decibel
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 13. Déphasage — `dephasage`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [Larousse, « déphasage »](https://www.larousse.fr/dictionnaires/francais/d%C3%A9phasage/23764) — type `reference`

**Fiches liées après** : `bobine-inductance`, `condensateur`, `courant-alternatif`, `diagramme-de-bode`, `facteur-de-puissance`, `impedance`, `modulation`

```
fiche : dephasage
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 14. Dipôle — `dipole`

- Niveau scolaire : C4 (cycles C4, 2GT, 1G) — version simple obligatoire
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (63 mots) :
> Composant ou portion de circuit relié au reste du montage par deux bornes, caractérisé par la tension entre ces bornes et l'intensité du courant qui le traverse. Il est dit actif quand il peut fournir de l'énergie au circuit, comme une pile — sa caractéristique ne passe pas par l'origine —, et passif dans le cas contraire, comme une résistance ou une lampe.

**Définition — après** (54 mots) :
> Composant ou portion de circuit relié au reste du montage par deux bornes, caractérisé par la tension entre ces bornes et l'intensité du courant qui le traverse. Il est dit actif quand il peut fournir de l'énergie au circuit, comme une pile, et passif dans le cas contraire, comme une résistance ou une lampe.

**Sources après** (à ouvrir une par une) :
- [Éduscol, « Aide à la construction d'une progression en physique-chimie au cycle 4 »](https://eduscol.education.fr/document/17731/download) — type `programme`
- [Éduscol, « L'électricité dans les programmes » (juillet 2019), physique-chimie de seconde générale et technologique et de première générale](https://eduscol.education.fr/document/22873/download) — type `programme`
- [Programme de physique-chimie de première générale (BO spécial n° 1 du 22 janvier 2019), partie « Aspects énergétiques des phénomènes électriques »](https://eduscol.education.gouv.fr/sites/default/files/document/spe635annexe1063432pdf-82266.pdf) — type `programme`

**Fiches liées après** : `caracteristique-tension-courant`, `circuit-electrique`, `generateur-electrique`, `impedance`, `intensite-electrique`, `loi-d-ohm`, `loi-des-mailles`, `loi-des-noeuds`, `resistance`, `resistance-electrique`, `tension-electrique`, `theoreme-de-thevenin`

```
fiche : dipole
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 15. Électromagnétisme — `electromagnetisme`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (19 mots) :
> Branche de la physique qui étudie les relations entre le champ électrique, le champ magnétique et le courant électrique.

**Définition — après** (38 mots) :
> Branche de la physique qui étudie les relations entre l'électricité et le magnétisme, en particulier la façon dont un courant électrique produit un champ magnétique et dont un champ magnétique variable produit à son tour un courant électrique.

**Sources après** (à ouvrir une par une) :
- [Larousse, « électromagnétisme »](https://www.larousse.fr/dictionnaires/francais/%C3%A9lectromagn%C3%A9tisme/28277) — type `reference`

**Fiches liées après** : `champ-electrique`, `champ-magnetique`, `courant-electrique`, `electricite` (nouveau), `tesla`

```
fiche : electromagnetisme
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 16. Électron — `electron`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (15 mots) :
> Particule élémentaire chargée négativement dont le déplacement dans un conducteur électrique constitue le courant électrique.

**Définition — après** (35 mots) :
> Particule élémentaire portant la plus petite charge électrique négative connue, présente dans le nuage qui entoure le noyau de tout atome. Son déplacement d'ensemble dans un conducteur électrique, comme un métal, constitue le courant électrique.

**Sources après** (à ouvrir une par une) :
- [Larousse, « électron »](https://www.larousse.fr/dictionnaires/francais/%C3%A9lectron/28295) — type `reference`

**Fiches liées après** : `atome`, `charge-electrique`, `conducteur-electrique`, `coulomb`, `courant-electrique`, `dopage`, `effet-photoelectrique`, `ion`, `loi-de-coulomb`, `trou-electronique`

```
fiche : electron
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 17. Électrostatique — `electrostatique`

- Niveau scolaire : 1G (cycles 1G)
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (17 mots) :
> Branche de la physique qui étudie les charges électriques au repos et le champ électrique qu'elles produisent.

**Définition — après** (34 mots) :
> Branche de la physique qui étudie les charges électriques immobiles, la force électrostatique qu'elles exercent les unes sur les autres et le champ électrique qu'elles produisent autour d'elles, décrit par la loi de Coulomb.

**Sources après** (à ouvrir une par une) :
- [Programme de physique-chimie de première générale, enseignement de spécialité (BO spécial n° 1 du 22 janvier 2019), partie « Mouvement et interactions », p. 499 (force et champ électrostatiques)](https://www.pedagogie.ac-aix-marseille.fr/upload/docs/application/pdf/2019-01/bo_n1_22_janvier_2019.pdf#page=499) — type `programme`
- [Larousse, « électrostatique »](https://www.larousse.fr/dictionnaires/francais/%C3%A9lectrostatique/28341) — type `reference`

**Fiches liées après** : `champ-electrique`, `decharge-electrostatique`, `loi-de-coulomb`

```
fiche : electrostatique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 18. Énergie électrique — `energie-electrique`

- Niveau scolaire : C2 (cycles C2, TG) — version simple obligatoire
- Règles automatiques encore enfreintes : aucune

**Sources après** (à ouvrir une par une) :
- [Programme de sciences et technologie du cycle 2 (annexe 1 de l'arrêté du 5 juin 2026, BO n° 24 du 11 juin 2026), « source d'énergie électrique », p. 11](https://www.education.gouv.fr/sites/default/files/document/annexe-1-programme-de-sciences-et-technologie-du-cycle-2-519020.pdf#page=11) — type `programme`

**Fiches liées après** : `alimentation-electrique`, `cable-electrique`, `compteur-electrique`, `consommation-electrique`, `facture-d-electricite`, `generateur-electrique`, `joule`, `kilowattheure`, `panneau-photovoltaique`, `puissance-electrique`

```
fiche : energie-electrique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 19. Effet photoélectrique — `effet-photoelectrique`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [Larousse, « effet photoélectrique »](https://www.larousse.fr/dictionnaires/francais/photo%C3%A9lectrique/60435#174496) — type `reference`

**Fiches liées après** : `bande-interdite`, `capteur-optique`, `electron`, `panneau-photovoltaique`, `photodiode`, `semi-conducteur`

```
fiche : effet-photoelectrique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 20. Électrolyse — `electrolyse`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [Larousse, « électrolyse »](https://www.larousse.fr/dictionnaires/francais/%C3%A9lectrolyse/28270) — type `reference`

**Fiches liées après** : `conducteur-electrique`, `courant-continu`, `hydrogene`, `ion`

```
fiche : electrolyse
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```
