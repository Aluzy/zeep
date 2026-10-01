---
lot: J5-S2
role: controle
date: 2026-10-01
changeset: agents/changesets/J5-S2.jsonl
elements: ["indice-de-reparabilite"]
---

# Contrôle du lot J5-S2 — passe 3

1 fiche(s), 25 opération(s) du rédacteur (changeset non encore appliqué).

## Consignes du contrôleur

Tu es le **contrôleur** du lot J5-S2. Tu n'as pas participé à la rédaction et tu ne la vois qu'à
travers ce document : les justifications du rédacteur sont volontairement absentes. Tu vérifies
chaque fiche contre les **12 critères** de `docs/grille-relecture.md` (lis-la en entier d'abord).

1. **Ouvre chaque URL de source** et vérifie qu'elle appuie la définition. Une source que tu ne
   peux pas ouvrir, imprécise (page d'accueil) ou qui n'appuie pas l'affirmation = critère 8 en échec.
2. Une fiche est **conforme** si les 12 critères passent. Dans `agents/changesets/J5-S2-controle.jsonl`, remplace alors
   `"__A_REMPLIR__"` de `new` par
   `{"date": "2026-10-01", "par": "agent-controleur-J5-S2", "statut": "relu-ia"}` et `why` par
   « Relue selon la grille (12 critères) ».
3. Une fiche **refusée** : supprime sa ligne dans `agents/changesets/J5-S2-controle.jsonl`, et note les critères en échec. Tu ne
   réécris pas la fiche : le rédacteur la corrige (nouvelle passe de contrôle) ou la retire du lot.
   Si le défaut porte sur une fiche hors lot, ajoute-la à `agents/donnees/signalements.json`.
4. Écris tes verdicts dans la section « Relecture (rempli par le contrôleur) » de
   `agents/rapports/J5-S2.md`, une ligne par fiche : critères en échec, décision.
5. Vérifie : `python3 scripts/apply_changeset.py agents/changesets/J5-S2.jsonl agents/changesets/J5-S2-controle.jsonl --dry-run`.
   Tu ne poses **jamais** `"statut": "valide"` (réservé à Alexandre).


## Fiches à contrôler

### 1. Indice de réparabilité — `indice-de-reparabilite`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Version simple — avant** (18 mots) :
> Cette note dit si un appareil sera facile à réparer. Plus elle est haute, plus l'objet durera longtemps.

**Version simple — après** (27 mots) :
> Cette note sur 10 dit si un appareil, comme un téléphone ou un aspirateur, sera facile à réparer. Plus elle est haute, plus la réparation est facile.

**Sources après** (à ouvrir une par une) :
- [Ministère de l'Économie — Tout savoir sur l'indice de réparabilité](https://www.economie.gouv.fr/particuliers/mes-droits-conso/bien-consommer/tout-savoir-sur-lindice-de-reparabilite) — type `reference`
- [Ministère de la Transition écologique — Durée de vie des produits](https://www.ecologie.gouv.fr/politiques-publiques/duree-vie-produits) — type `reference`
- [ADEME — Acheter des appareils électriques et électroniques faits pour durer](https://agirpourlatransition.ademe.fr/particuliers/mieux-consommer/electromenager/appareils-electriques-electroniques-durables) — type `reference`

**Fiches liées après** : `composant-electronique`, `eco-conception`, `obsolescence-programmee`, `recyclage-des-dechets-electroniques-deee`

```
fiche : indice-de-reparabilite
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```
