---
lot: J5-S3
role: controle
date: 2026-10-01
changeset: agents/changesets/J5-S3.jsonl
elements: ["compteur-linky", "delestage", "heures-creuses", "puissance-souscrite"]
---

# Contrôle du lot J5-S3 — passe 2

4 fiche(s), 9 opération(s) du rédacteur (changeset non encore appliqué).

## Consignes du contrôleur

Tu es le **contrôleur** du lot J5-S3. Tu n'as pas participé à la rédaction et tu ne la vois qu'à
travers ce document : les justifications du rédacteur sont volontairement absentes. Tu vérifies
chaque fiche contre les **12 critères** de `docs/grille-relecture.md` (lis-la en entier d'abord).

1. **Ouvre chaque URL de source** et vérifie qu'elle appuie la définition. Une source que tu ne
   peux pas ouvrir, imprécise (page d'accueil) ou qui n'appuie pas l'affirmation = critère 8 en échec.
2. Une fiche est **conforme** si les 12 critères passent. Dans `agents/changesets/J5-S3-controle.jsonl`, remplace alors
   `"__A_REMPLIR__"` de `new` par
   `{"date": "2026-10-01", "par": "agent-controleur-J5-S3", "statut": "relu-ia"}` et `why` par
   « Relue selon la grille (12 critères) ».
3. Une fiche **refusée** : supprime sa ligne dans `agents/changesets/J5-S3-controle.jsonl`, et note les critères en échec. Tu ne
   réécris pas la fiche : le rédacteur la corrige (nouvelle passe de contrôle) ou la retire du lot.
   Si le défaut porte sur une fiche hors lot, ajoute-la à `agents/donnees/signalements.json`.
4. Écris tes verdicts dans la section « Relecture (rempli par le contrôleur) » de
   `agents/rapports/J5-S3.md`, une ligne par fiche : critères en échec, décision.
5. Vérifie : `python3 scripts/apply_changeset.py agents/changesets/J5-S3.jsonl agents/changesets/J5-S3-controle.jsonl --dry-run`.
   Tu ne poses **jamais** `"statut": "valide"` (réservé à Alexandre).


## Fiches à contrôler

### 1. Compteur Linky — `compteur-linky`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (31 mots) :
> Compteur électrique communicant déployé en France, qui relève la consommation à distance et transmet les données par courants porteurs. Il permet le suivi fin des usages et le pilotage du réseau.

**Définition — après** (44 mots) :
> Compteur électrique communicant déployé en France, qui relève la consommation à distance et transmet ses données par des signaux envoyés dans les câbles du réseau électrique. Il permet un suivi précis de la consommation réelle et facilite l'intégration de nouveaux usages sur le réseau.

**Sources après** (à ouvrir une par une) :
- [Enedis — Qu'est-ce que le compteur Linky ?](https://www.enedis.fr/faq/compteur-linky/quest-ce-que-le-compteur-linky) — type `reference`
- [Enedis — Comment communique le compteur Linky ?](https://www.enedis.fr/faq/compteur-linky/comment-communique-le-compteur-linky) — type `reference`
- [Enedis — Tout savoir sur Linky, le compteur adapté à la vie d'aujourd'hui](https://www.enedis.fr/tout-savoir-sur-linky-le-compteur-adapte-la-vie-daujourdhui) — type `reference`

**Fiches liées après** : `autoconsommation`, `compteur-electrique`, `consommation-electrique`, `facture-d-electricite`, `reseau-de-distribution`, `reseau-intelligent-smart-grid`

```
fiche : compteur-linky
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 2. Délestage — `delestage`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Version simple — avant** (19 mots) :
> Quand il n'y a pas assez d'électricité pour tout le monde, on coupe volontairement certains secteurs peu de temps.

**Version simple — après** (28 mots) :
> Quand tout le monde chauffe sa maison en même temps et que l'électricité produite ne suffit plus, on coupe le courant à tour de rôle dans certains quartiers.

**Synonymes** : coupure organisee, delestage, effacement → **coupure organisee, delestage**

**Sources après** (à ouvrir une par une) :
- [Enedis — Qu'est-ce que le délestage ?](https://www.enedis.fr/faq/glossaire/quest-ce-que-le-delestage) — type `reference`
- [Enedis — À quoi servent les délestages ou coupures temporaires ?](https://www.enedis.fr/faq/delestage/a-quoi-servent-les-delestages) — type `reference`

**Fiches liées après** : `consommation-electrique`, `frequence-electrique`, `heures-creuses`, `reseau-de-transport`, `reseau-electrique`

```
fiche : delestage
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 3. Heures creuses — `heures-creuses`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (26 mots) :
> Plages horaires durant lesquelles le kilowattheure est facturé moins cher, afin de déplacer la consommation hors des pointes. Elles commandent classiquement le chauffe-eau par un contacteur.

**Définition — après** (41 mots) :
> Périodes de la journée, huit heures au total, où le kilowattheure est facturé moins cher. Elles incitent à déplacer la consommation hors des heures de pointe, quand beaucoup d'appareils fonctionnent en même temps ; depuis 2025, une partie se situe l'après-midi.

**Sources après** (à ouvrir une par une) :
- [Enedis — Modification des heures creuses : comprendre ce qui change à partir du 1er novembre 2025](https://www.enedis.fr/magazine/modification-des-heures-creuses-comprendre-ce-qui-change-partir-du-1er-novembre-2025) — type `reference`
- [Enedis — Réforme des heures creuses pour accompagner les nouveaux usages](https://www.enedis.fr/presse/enedis-met-en-oeuvre-la-reforme-des-heures-creuses-pour-accompagner-les-nouveaux-usages-lies) — type `reference`

**Fiches liées après** : `consommation-electrique`, `contacteur`, `delestage`, `facture-d-electricite`, `kilowattheure`

```
fiche : heures-creuses
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 4. Puissance souscrite — `puissance-souscrite`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Version simple — avant** (19 mots) :
> C'est la quantité d'électricité que l'on peut utiliser en même temps. Si on la dépasse, le compteur coupe tout.

**Version simple — après** (32 mots) :
> C'est la puissance maximale que le compteur laisse utiliser en même temps. Si on allume le four, la bouilloire et le lave-linge ensemble, on peut dépasser la limite et le compteur coupe.

**Sources après** (à ouvrir une par une) :
- [Enedis — Pourquoi faut-il estimer la puissance d'un compteur électrique ?](https://www.enedis.fr/faq/compteur-electrique/pourquoi-faut-il-estimer-la-puissance-dun-compteur-electrique) — type `reference`
- [Enedis — Compteur Linky : quelle puissance choisir ?](https://www.enedis.fr/faq/compteur-linky/compteur-linky-quelle-puissance-choisir) — type `reference`

**Fiches liées après** : `compteur-electrique`, `disjoncteur`, `facture-d-electricite`, `fournisseur-d-electricite`, `voltampere`

```
fiche : puissance-souscrite
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```
