---
lot: J4-L8
role: controle
date: 2026-09-27
changeset: agents/changesets/J4-L8.jsonl
elements: ["puissance-reactive", "reactance", "resistivite", "resonance", "siemens", "tesla", "theoreme-de-millman", "theoreme-de-norton", "theoreme-de-superposition", "theoreme-de-thevenin", "volt", "voltampere", "voltmetre", "watt", "wattmetre", "weber"]
---

# Contrôle du lot J4-L8

16 fiche(s), 22 opération(s) du rédacteur (changeset non encore appliqué).

## Consignes du contrôleur

Tu es le **contrôleur** du lot J4-L8. Tu n'as pas participé à la rédaction et tu ne la vois qu'à
travers ce document : les justifications du rédacteur sont volontairement absentes. Tu vérifies
chaque fiche contre les **12 critères** de `docs/grille-relecture.md` (lis-la en entier d'abord).

1. **Ouvre chaque URL de source** et vérifie qu'elle appuie la définition. Une source que tu ne
   peux pas ouvrir, imprécise (page d'accueil) ou qui n'appuie pas l'affirmation = critère 8 en échec.
2. Une fiche est **conforme** si les 12 critères passent. Dans `agents/changesets/J4-L8-controle.jsonl`, remplace alors
   `"__A_REMPLIR__"` de `new` par
   `{"date": "2026-09-27", "par": "agent-controleur-J4-L8", "statut": "relu-ia"}` et `why` par
   « Relue selon la grille (12 critères) ».
3. Une fiche **refusée** : supprime sa ligne dans `agents/changesets/J4-L8-controle.jsonl`, et note les critères en échec. Tu ne
   réécris pas la fiche : le rédacteur la corrige (nouvelle passe de contrôle) ou la retire du lot.
   Si le défaut porte sur une fiche hors lot, ajoute-la à `agents/donnees/signalements.json`.
4. Écris tes verdicts dans la section « Relecture (rempli par le contrôleur) » de
   `agents/rapports/J4-L8.md`, une ligne par fiche : critères en échec, décision.
5. Vérifie : `python3 scripts/apply_changeset.py agents/changesets/J4-L8.jsonl agents/changesets/J4-L8-controle.jsonl --dry-run`.
   Tu ne poses **jamais** `"statut": "valide"` (réservé à Alexandre).


## Fiches à contrôler

### 1. Puissance réactive — `puissance-reactive`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [Larousse — puissance réactive](https://www.larousse.fr/dictionnaires/francais/puissance/65022#165626) — type `reference`

**Fiches liées après** : `bobine-inductance`, `condensateur`, `facteur-de-puissance`, `puissance-active`, `puissance-apparente`

```
fiche : puissance-reactive
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 2. Réactance — `reactance`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [Larousse — réactance](https://www.larousse.fr/dictionnaires/francais/réactance/66789) — type `reference`

**Fiches liées après** : `bobine-inductance`, `condensateur`, `frequence-electrique`, `impedance`, `ohm`

```
fiche : reactance
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 3. Résistivité — `resistivite`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (19 mots) :
> Grandeur physique caractérisant la capacité d'un matériau à s'opposer au passage du courant électrique, inverse de la conductivité électrique.

**Définition — après** (37 mots) :
> Grandeur physique qui caractérise l'aptitude d'un matériau à s'opposer au passage du courant électrique : plus elle est élevée, plus ce matériau conduit difficilement le courant. Elle s'exprime en ohms-mètres et vaut l'inverse de la conductivité électrique.

**Synonymes** : — → **rho, ρ**

**Sources après** (à ouvrir une par une) :
- [Larousse — résistivité](https://www.larousse.fr/dictionnaires/francais/résistivité/68639) — type `reference`

**Fiches liées après** : `conductivite-electrique`, `courant-electrique`, `supraconductivite`

```
fiche : resistivite
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 4. Résonance — `resonance`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [Larousse — résonance (sens 4, Physique)](https://www.larousse.fr/dictionnaires/francais/résonance/68656) — type `reference`

**Fiches liées après** : `antenne`, `circuit-rlc`, `filtre-passe-bande`, `frequence-electrique`, `quartz-resonateur`

```
fiche : resonance
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 5. Siemens — `siemens`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [BIPM, « Le Système international d'unités » (9e édition, version française, 2019), tableau 4, p. 24](https://www.bipm.org/documents/20126/41483022/SI-Brochure-9-FR.pdf#page=24) — type `norme`
- [Larousse — siemens](https://www.larousse.fr/dictionnaires/francais/siemens/72652) — type `reference`

**Fiches liées après** : `conducteur-electrique`, `conductivite-electrique`, `ohm`, `resistance-electrique`

```
fiche : siemens
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 6. Tesla — `tesla`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [BIPM, « Le Système international d'unités » (9e édition, version française, 2019), tableau 4, p. 24](https://www.bipm.org/documents/20126/41483022/SI-Brochure-9-FR.pdf#page=24) — type `norme`
- [Larousse — tesla](https://www.larousse.fr/dictionnaires/francais/tesla/77490) — type `reference`

**Fiches liées après** : `champ-magnetique`, `effet-hall`, `electromagnetisme`, `induction-electromagnetique`, `weber`

```
fiche : tesla
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 7. Théorème de Millman — `theoreme-de-millman`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [IUT en ligne, « Analyse des signaux et des circuits électriques », chapitre 7 (M. Piou), exercice 6 « Théorème de Millman », p. 7](https://www.iutenligne.net/rsc/rsc-public/electronique/piou_fruitet_fortun/baselecpro/acquisition/pdf/DL-001051-04-07.01.00.pdf#page=9) — type `manuel`

**Fiches liées après** : `circuit-electrique`, `conductivite-electrique`, `loi-des-noeuds`, `tension-electrique`

```
fiche : theoreme-de-millman
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 8. Théorème de Norton — `theoreme-de-norton`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [IUT en ligne, « Analyse des signaux et des circuits électriques », chapitre 7 (M. Piou), §2.4 « Théorème de Norton », p. 4](https://www.iutenligne.net/rsc/rsc-public/electronique/piou_fruitet_fortun/baselecpro/acquisition/pdf/DL-001051-04-07.01.00.pdf#page=6) — type `manuel`

**Fiches liées après** : `circuit-electrique`, `courant-electrique`, `resistance-electrique`, `theoreme-de-thevenin`

```
fiche : theoreme-de-norton
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 9. Théorème de superposition — `theoreme-de-superposition`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [IUT en ligne, « Analyse des signaux et des circuits électriques », chapitre 7 (M. Piou), §2.2 « Théorème de superposition », p. 3](https://www.iutenligne.net/rsc/rsc-public/electronique/piou_fruitet_fortun/baselecpro/acquisition/pdf/DL-001051-04-07.01.00.pdf#page=5) — type `manuel`

**Fiches liées après** : `circuit-electrique`, `generateur-electrique`, `loi-des-mailles`, `loi-des-noeuds`

```
fiche : theoreme-de-superposition
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 10. Théorème de Thévenin — `theoreme-de-thevenin`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [IUT en ligne, « Analyse des signaux et des circuits électriques », chapitre 7 (M. Piou), §2.3 « Théorème de Thévenin », p. 4](https://www.iutenligne.net/rsc/rsc-public/electronique/piou_fruitet_fortun/baselecpro/acquisition/pdf/DL-001051-04-07.01.00.pdf#page=6) — type `manuel`

**Fiches liées après** : `circuit-electrique`, `dipole`, `generateur-electrique`, `resistance-electrique`, `theoreme-de-norton`

```
fiche : theoreme-de-thevenin
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 11. Volt — `volt`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (13 mots) :
> Unité de mesure de la tension électrique dans le Système international, symbole V.

**Définition — après** (39 mots) :
> Unité de mesure de la tension électrique dans le Système international, de symbole V. Un volt correspond à la tension aux bornes d'un conducteur parcouru par un courant d'un ampère, quand la puissance dissipée y est de un watt.

**Sources après** (à ouvrir une par une) :
- [BIPM, « Le Système international d'unités » (9e édition, version française, 2019), tableau 4, p. 24](https://www.bipm.org/documents/20126/41483022/SI-Brochure-9-FR.pdf#page=24) — type `norme`
- [Larousse — volt](https://www.larousse.fr/dictionnaires/francais/volt/82478) — type `reference`

**Fiches liées après** : `tension-electrique`, `voltage`

```
fiche : volt
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 12. Voltampère — `voltampere`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [Larousse — voltampère](https://www.larousse.fr/dictionnaires/francais/voltampère/82486) — type `reference`

**Fiches liées après** : `facteur-de-puissance`, `puissance-apparente`, `puissance-electrique`, `puissance-souscrite`, `transformateur`

```
fiche : voltampere
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 13. Voltmètre — `voltmetre`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (16 mots) :
> Instrument de mesure de la tension électrique entre deux points d'un circuit électrique, exprimée en volts.

**Définition — après** (31 mots) :
> Instrument qui mesure la tension électrique, exprimée en volts, entre deux points d'un circuit électrique ; il se branche en dérivation, aux bornes du dipôle dont on veut connaître la tension.

**Sources après** (à ouvrir une par une) :
- [Larousse — voltmètre](https://www.larousse.fr/dictionnaires/francais/voltmètre/82496) — type `reference`

**Fiches liées après** : `circuit-electrique`, `loi-des-mailles`, `multimetre`, `oscilloscope`, `tension-electrique`, `voltage`

```
fiche : voltmetre
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 14. Watt — `watt`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (15 mots) :
> Unité de mesure de la puissance électrique, correspondant à un joule d'énergie transféré par seconde.

**Définition — après** (32 mots) :
> Unité de mesure de la puissance, quelle que soit sa forme (électrique, mécanique, thermique...), dans le Système international, de symbole W. Un watt correspond à un transfert d'énergie d'un joule chaque seconde.

**Sources après** (à ouvrir une par une) :
- [BIPM, « Le Système international d'unités » (9e édition, version française, 2019), tableau 4, p. 24](https://www.bipm.org/documents/20126/41483022/SI-Brochure-9-FR.pdf#page=24) — type `norme`
- [Larousse — watt](https://www.larousse.fr/dictionnaires/francais/watt/82733) — type `reference`

**Fiches liées après** : `consommation-electrique`, `joule`, `puissance-active`, `puissance-electrique`, `watt-crete`

```
fiche : watt
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 15. Wattmètre — `wattmetre`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (17 mots) :
> Instrument de mesure de la puissance électrique consommée ou produite par un appareil ou un circuit électrique.

**Définition — après** (30 mots) :
> Instrument qui mesure la puissance électrique, exprimée en watts, consommée ou produite par un appareil ou un circuit électrique, à partir de la tension et de l'intensité qu'il mesure simultanément.

**Sources après** (à ouvrir une par une) :
- [Larousse — wattmètre](https://www.larousse.fr/dictionnaires/francais/wattmètre/82738) — type `reference`

**Fiches liées après** : `circuit-electrique`, `puissance-electrique`

```
fiche : wattmetre
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 16. Weber — `weber`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [BIPM, « Le Système international d'unités » (9e édition, version française, 2019), tableau 4, p. 24](https://www.bipm.org/documents/20126/41483022/SI-Brochure-9-FR.pdf#page=24) — type `norme`
- [Larousse — weber](https://www.larousse.fr/dictionnaires/francais/weber/82750) — type `reference`

**Fiches liées après** : `bobine-inductance`, `champ-magnetique`, `induction-electromagnetique`, `loi-de-faraday`, `tesla`

```
fiche : weber
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```
