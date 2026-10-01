---
lot: J5-S6
role: controle
date: 2026-10-01
changeset: agents/changesets/J5-S6.jsonl
elements: ["porte-non-et", "porte-non-ou", "technicien-de-maintenance"]
---

# Contrôle du lot J5-S6 — passe 2

3 fiche(s), 53 opération(s) du rédacteur (changeset non encore appliqué).

## Consignes du contrôleur

Tu es le **contrôleur** du lot J5-S6. Tu n'as pas participé à la rédaction et tu ne la vois qu'à
travers ce document : les justifications du rédacteur sont volontairement absentes. Tu vérifies
chaque fiche contre les **12 critères** de `docs/grille-relecture.md` (lis-la en entier d'abord).

1. **Ouvre chaque URL de source** et vérifie qu'elle appuie la définition. Une source que tu ne
   peux pas ouvrir, imprécise (page d'accueil) ou qui n'appuie pas l'affirmation = critère 8 en échec.
2. Une fiche est **conforme** si les 12 critères passent. Dans `agents/changesets/J5-S6-controle.jsonl`, remplace alors
   `"__A_REMPLIR__"` de `new` par
   `{"date": "2026-10-01", "par": "agent-controleur-J5-S6", "statut": "relu-ia"}` et `why` par
   « Relue selon la grille (12 critères) ».
3. Une fiche **refusée** : supprime sa ligne dans `agents/changesets/J5-S6-controle.jsonl`, et note les critères en échec. Tu ne
   réécris pas la fiche : le rédacteur la corrige (nouvelle passe de contrôle) ou la retire du lot.
   Si le défaut porte sur une fiche hors lot, ajoute-la à `agents/donnees/signalements.json`.
4. Écris tes verdicts dans la section « Relecture (rempli par le contrôleur) » de
   `agents/rapports/J5-S6.md`, une ligne par fiche : critères en échec, décision.
5. Vérifie : `python3 scripts/apply_changeset.py agents/changesets/J5-S6.jsonl agents/changesets/J5-S6-controle.jsonl --dry-run`.
   Tu ne poses **jamais** `"statut": "valide"` (réservé à Alexandre).


## Fiches à contrôler

### 1. Porte NON-ET — `porte-non-et`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Version simple — avant** (20 mots) :
> Cette porte répond non seulement quand toutes ses entrées disent oui. Avec elle seule, on peut fabriquer toutes les autres.

**Version simple — après** (31 mots) :
> Cette porte répond « non » seulement quand toutes ses entrées disent « oui », comme une lampe qui reste allumée sauf si l'on appuie sur deux boutons à la fois.

**Sources après** (à ouvrir une par une) :
- [Eric Cariou (Université de Pau et des Pays de l'Adour), cours d'architecture des ordinateurs, « Circuits logiques »](https://lab-sticc.univ-brest.fr/~ecariou/cours/archi/cours-3-circuits-logiques.pdf) — type `manuel`

**Fiches liées après** : `circuit-logique`, `porte-et-and`, `porte-logique`, `porte-non-not`, `table-de-verite`

```
fiche : porte-non-et
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 2. Porte NON-OU — `porte-non-ou`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Version simple — avant** (11 mots) :
> Cette porte répond oui seulement quand aucune entrée ne dit oui.

**Version simple — après** (32 mots) :
> Cette porte répond « oui » seulement quand aucune de ses entrées ne dit « oui », comme une lampe qui s'éteint dès qu'on appuie sur au moins un des deux boutons.

**Sources après** (à ouvrir une par une) :
- [Eric Cariou (Université de Pau et des Pays de l'Adour), cours d'architecture des ordinateurs, « Circuits logiques »](https://lab-sticc.univ-brest.fr/~ecariou/cours/archi/cours-3-circuits-logiques.pdf) — type `manuel`

**Fiches liées après** : `circuit-logique`, `porte-logique`, `porte-non-not`, `porte-ou-or`, `table-de-verite`

```
fiche : porte-non-ou
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 3. Technicien de maintenance — `technicien-de-maintenance`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (29 mots) :
> Professionnel chargé de prévenir et de réparer les pannes des équipements électriques et automatisés. Il diagnostique à l'aide d'appareils de mesure et intervient dans le cadre d'une habilitation électrique.

**Définition — après** (48 mots) :
> Professionnel qui contrôle, surveille et entretient des équipements industriels, notamment électriques et automatisés, pour prévenir les pannes, et qui organise leur réparation quand elles surviennent. Il établit un diagnostic à l'aide de tests et de mesures et doit être habilité pour intervenir sur ou près d'une installation électrique.

**Version simple — avant** (16 mots) :
> Ce métier consiste à entretenir les machines et à trouver l'origine des pannes pour les réparer.

**Version simple — après** (28 mots) :
> Ce métier consiste à entretenir les machines, par exemple dans une usine ou un centre de tri des déchets, et à trouver l'origine des pannes pour les réparer.

**Sources après** (à ouvrir une par une) :
- [Onisep, fiche métier « Technicien / Technicienne de maintenance industrielle », version PDF complète](https://www.onisep.fr/ressources/univers-metier/metiers/technicien-technicienne-de-maintenance-industrielle/pdf) — type `reference`
- [Onisep, fiche métier « Technicien / Technicienne de maintenance industrielle »](https://www.onisep.fr/ressources/univers-metier/metiers/technicien-technicienne-de-maintenance-industrielle) — type `reference`
- [INRS, Risques électriques — Réglementation et prévention du risque électrique (habilitation)](https://www.inrs.fr/risques/electriques/reglementation-prevention-risque-electrique.html) — type `reference`

**Fiches liées après** : `automate-programmable`, `consignation-electrique`, `electricien`, `habilitation-electrique`, `installation-electrique` (nouveau), `multimetre`

```
fiche : technicien-de-maintenance
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```
