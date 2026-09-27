---
lot: J4-L5
role: controle
date: 2026-09-27
changeset: agents/changesets/J4-L5.jsonl
elements: ["asservissement", "constante-de-temps", "echantillonnage", "energie-electrique", "loi-de-coulomb", "mix-energetique", "quantification", "regime-transitoire", "stockage-d-energie", "supercondensateur"]
---

# Contrôle du lot J4-L5

10 fiche(s), 10 opération(s) du rédacteur (changeset non encore appliqué).

## Consignes du contrôleur

Tu es le **contrôleur** du lot J4-L5. Tu n'as pas participé à la rédaction et tu ne la vois qu'à
travers ce document : les justifications du rédacteur sont volontairement absentes. Tu vérifies
chaque fiche contre les **12 critères** de `docs/grille-relecture.md` (lis-la en entier d'abord).

1. **Ouvre chaque URL de source** et vérifie qu'elle appuie la définition. Une source que tu ne
   peux pas ouvrir, imprécise (page d'accueil) ou qui n'appuie pas l'affirmation = critère 8 en échec.
2. Une fiche est **conforme** si les 12 critères passent. Dans `agents/changesets/J4-L5-controle.jsonl`, remplace alors
   `"__A_REMPLIR__"` de `new` par
   `{"date": "2026-09-27", "par": "agent-controleur-J4-L5", "statut": "relu-ia"}` et `why` par
   « Relue selon la grille (12 critères) ».
3. Une fiche **refusée** : supprime sa ligne dans `agents/changesets/J4-L5-controle.jsonl`, et note les critères en échec. Tu ne
   réécris pas la fiche : le rédacteur la corrige (nouvelle passe de contrôle) ou la retire du lot.
   Si le défaut porte sur une fiche hors lot, ajoute-la à `agents/donnees/signalements.json`.
4. Écris tes verdicts dans la section « Relecture (rempli par le contrôleur) » de
   `agents/rapports/J4-L5.md`, une ligne par fiche : critères en échec, décision.
5. Vérifie : `python3 scripts/apply_changeset.py agents/changesets/J4-L5.jsonl agents/changesets/J4-L5-controle.jsonl --dry-run`.
   Tu ne poses **jamais** `"statut": "valide"` (réservé à Alexandre).


## Fiches à contrôler

### 1. Asservissement — `asservissement`

- Niveau scolaire : BACPRO (cycles BACPRO, STI2D)
- Règles automatiques encore enfreintes : ⚠ Source pointant vers une page d'accueil (invérifiable); ⚠ Type de source hors liste (programme|reference|norme|manuel); ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [Éduscol — ressources d'accompagnement des programmes](https://eduscol.education.fr/) — type `officiel`
- [IEC Electropedia — vocabulaire électrotechnique international](https://www.electropedia.org/) — type `reference`
- [Programme STI2D, enseignement technologique transversal (arrêté du 17 janvier 2019, modifié le 19 juillet 2019), « Comportement des systèmes régulés ou asservis », p. 35](https://www.snes.edu/IMG/pdf/arrete_sti2d_ensemble.pdf#page=35) — type `programme`

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
- Règles automatiques encore enfreintes : ⚠ Source pointant vers une page d'accueil (invérifiable); ⚠ Type de source hors liste (programme|reference|norme|manuel); ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [Éduscol — ressources d'accompagnement des programmes](https://eduscol.education.fr/) — type `officiel`
- [Programme de physique-chimie de terminale générale, enseignement de spécialité (BO spécial n° 8 du 25 juillet 2019), « Modèle du circuit RC série », p. 20](https://www.education.gouv.fr/sites/default/files/document/Programme%20de%20physique-chimie%20de%20terminale%20g%C3%A9n%C3%A9rale-253485.pdf#page=20) — type `programme`

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
- Règles automatiques encore enfreintes : ⚠ Définition hors 25-60 mots; ⚠ Source pointant vers une page d'accueil (invérifiable); ⚠ Type de source hors liste (programme|reference|norme|manuel); ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [Éduscol — ressources d'accompagnement des programmes](https://eduscol.education.fr/) — type `officiel`
- [Programme STI2D, enseignement technologique transversal (arrêté du 17 janvier 2019, modifié le 19 juillet 2019), « Conversion Analogique/Numérique (CAN) », p. 26](https://www.snes.edu/IMG/pdf/arrete_sti2d_ensemble.pdf#page=26) — type `programme`

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

### 4. Énergie électrique — `energie-electrique`

- Niveau scolaire : C2 (cycles C2, TG) — version simple obligatoire
- Règles automatiques encore enfreintes : ⚠ Source pointant vers une page d'accueil (invérifiable); ⚠ Type de source hors liste (programme|reference|norme|manuel); ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [Éduscol — ressources d'accompagnement des programmes](https://eduscol.education.fr/) — type `officiel`
- [IEC Electropedia — vocabulaire électrotechnique international](https://www.electropedia.org/) — type `reference`
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

### 5. Loi de Coulomb — `loi-de-coulomb`

- Niveau scolaire : 1G (cycles 1G)
- Règles automatiques encore enfreintes : ⚠ Source pointant vers une page d'accueil (invérifiable); ⚠ Type de source hors liste (programme|reference|norme|manuel); ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [Éduscol — ressources d'accompagnement des programmes](https://eduscol.education.fr/) — type `officiel`
- [IEC Electropedia — vocabulaire électrotechnique international](https://www.electropedia.org/) — type `reference`
- [Programme d'enseignement de spécialité de physique-chimie de première (BO spécial n° 1 du 22 janvier 2019), « Charge électrique, interaction électrostatique […] Loi de Coulomb », p. 498](https://www.pedagogie.ac-aix-marseille.fr/upload/docs/application/pdf/2019-01/bo_n1_22_janvier_2019.pdf#page=498) — type `programme`

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

### 6. Mix énergétique — `mix-energetique`

- Niveau scolaire : STI2D (cycles STI2D)
- Règles automatiques encore enfreintes : ⚠ Définition hors 25-60 mots; ⚠ Source pointant vers une page d'accueil (invérifiable); ⚠ Type de source hors liste (programme|reference|norme|manuel); ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [RTE — le réseau de transport d'électricité](https://www.rte-france.com/) — type `officiel`
- [ADEME — énergie, climat et économie circulaire](https://www.ademe.fr/) — type `officiel`
- [Programme STI2D, enseignement technologique transversal (arrêté du 17 janvier 2019, modifié le 19 juillet 2019), « mix énergétique », p. 39](https://www.snes.edu/IMG/pdf/arrete_sti2d_ensemble.pdf#page=39) — type `programme`

**Fiches liées après** : `centrale-nucleaire`, `empreinte-carbone-de-l-electricite`, `energie-fossile`, `energie-renouvelable`, `production-d-electricite`

```
fiche : mix-energetique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 7. Quantification — `quantification`

- Niveau scolaire : STI2D (cycles STI2D)
- Règles automatiques encore enfreintes : ⚠ Source pointant vers une page d'accueil (invérifiable); ⚠ Type de source hors liste (programme|reference|norme|manuel); ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [Éduscol — ressources d'accompagnement des programmes](https://eduscol.education.fr/) — type `officiel`
- [Programme STI2D, enseignement technologique transversal (arrêté du 17 janvier 2019, modifié le 19 juillet 2019), « Conversion Analogique/Numérique (CAN) », p. 26](https://www.snes.edu/IMG/pdf/arrete_sti2d_ensemble.pdf#page=26) — type `programme`

**Fiches liées après** : `bit`, `bruit-electronique`, `convertisseur-analogique-numerique-can`, `echantillonnage`, `signal-numerique`

```
fiche : quantification
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 8. Régime transitoire — `regime-transitoire`

- Niveau scolaire : TG (cycles TG)
- Règles automatiques encore enfreintes : ⚠ Source pointant vers une page d'accueil (invérifiable); ⚠ Type de source hors liste (programme|reference|norme|manuel); ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [Éduscol — ressources d'accompagnement des programmes](https://eduscol.education.fr/) — type `officiel`
- [Programme de physique-chimie de terminale générale, enseignement de spécialité (BO spécial n° 8 du 25 juillet 2019), « Modèle du circuit RC série […] temps caractéristique », p. 20](https://www.education.gouv.fr/sites/default/files/document/Programme%20de%20physique-chimie%20de%20terminale%20g%C3%A9n%C3%A9rale-253485.pdf#page=20) — type `programme`

**Fiches liées après** : `bobine-inductance`, `circuit-rc`, `circuit-rl`, `condensateur`, `constante-de-temps`

```
fiche : regime-transitoire
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 9. Stockage d'énergie — `stockage-d-energie`

- Niveau scolaire : 1-TG (cycles 1-TG)
- Règles automatiques encore enfreintes : ⚠ Source pointant vers une page d'accueil (invérifiable); ⚠ Type de source hors liste (programme|reference|norme|manuel); ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [ADEME — énergie, climat et économie circulaire](https://www.ademe.fr/) — type `officiel`
- [RTE — le réseau de transport d'électricité](https://www.rte-france.com/) — type `officiel`
- [Programme de sciences de l'ingénieur, cycle terminal, enseignement de spécialité (arrêté du 17 janvier 2019, applicable 2019 en 1ère et 2020 en terminale), « Stockage de l'énergie », p. 10](https://www.snes.edu/wp-content/uploads/cycle_terminal_sciences_ingenieur_specialite_voie_generale_1023828.pdf#page=10) — type `programme`

**Fiches liées après** : `accumulateur`, `autoconsommation`, `batterie`, `batterie-de-traction`, `energie-renouvelable`, `hydrogene`, `pile-a-combustible`, `reseau-electrique`, `station-de-transfert-d-energie-par-pompage`, `supercondensateur`

```
fiche : stockage-d-energie
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 10. Supercondensateur — `supercondensateur`

- Niveau scolaire : STI2D (cycles STI2D)
- Règles automatiques encore enfreintes : ⚠ Source pointant vers une page d'accueil (invérifiable); ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [IEC Electropedia — vocabulaire électrotechnique international](https://www.electropedia.org/) — type `reference`
- [Programme STI2D, enseignement technologique transversal (arrêté du 17 janvier 2019, modifié le 19 juillet 2019), « Stockage électrostatique », p. 44](https://www.snes.edu/IMG/pdf/arrete_sti2d_ensemble.pdf#page=44) — type `programme`

**Fiches liées après** : `accumulateur`, `batterie`, `condensateur`, `farad`, `freinage-regeneratif`, `stockage-d-energie`

```
fiche : supercondensateur
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```
