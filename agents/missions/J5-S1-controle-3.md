---
lot: J5-S1
role: controle
date: 2026-10-01
changeset: agents/changesets/J5-S1.jsonl
elements: ["batterie-de-traction"]
---

# Contrôle du lot J5-S1 — passe 3

1 fiche(s), 4 opération(s) du rédacteur (changeset non encore appliqué).

## Consignes du contrôleur

Tu es le **contrôleur** du lot J5-S1. Tu n'as pas participé à la rédaction et tu ne la vois qu'à
travers ce document : les justifications du rédacteur sont volontairement absentes. Tu vérifies
chaque fiche contre les **12 critères** de `docs/grille-relecture.md` (lis-la en entier d'abord).

1. **Ouvre chaque URL de source** et vérifie qu'elle appuie la définition. Une source que tu ne
   peux pas ouvrir, imprécise (page d'accueil) ou qui n'appuie pas l'affirmation = critère 8 en échec.
2. Une fiche est **conforme** si les 12 critères passent. Dans `agents/changesets/J5-S1-controle.jsonl`, remplace alors
   `"__A_REMPLIR__"` de `new` par
   `{"date": "2026-10-01", "par": "agent-controleur-J5-S1", "statut": "relu-ia"}` et `why` par
   « Relue selon la grille (12 critères) ».
3. Une fiche **refusée** : supprime sa ligne dans `agents/changesets/J5-S1-controle.jsonl`, et note les critères en échec. Tu ne
   réécris pas la fiche : le rédacteur la corrige (nouvelle passe de contrôle) ou la retire du lot.
   Si le défaut porte sur une fiche hors lot, ajoute-la à `agents/donnees/signalements.json`.
4. Écris tes verdicts dans la section « Relecture (rempli par le contrôleur) » de
   `agents/rapports/J5-S1.md`, une ligne par fiche : critères en échec, décision.
5. Vérifie : `python3 scripts/apply_changeset.py agents/changesets/J5-S1.jsonl agents/changesets/J5-S1-controle.jsonl --dry-run`.
   Tu ne poses **jamais** `"statut": "valide"` (réservé à Alexandre).


## Fiches à contrôler

### 1. Batterie de traction — `batterie-de-traction`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (26 mots) :
> Assemblage de nombreuses cellules lithium-ion, de leur système de refroidissement et de leur électronique de surveillance, qui alimente un véhicule électrique. Sa capacité fixe l'autonomie disponible.

**Définition — après** (49 mots) :
> Batterie d'accumulateurs rechargeable qui alimente le moteur électrique d'un véhicule. Elle regroupe le plus souvent de nombreuses cellules lithium-ion associées en série et en parallèle, surveillées par un système de gestion de batterie. Sa capacité, en kilowattheures, est l'énergie stockée : avec la consommation du véhicule, elle fixe l'autonomie.

**Sources après** (à ouvrir une par une) :
- [FranceTerme (Journal officiel du 12/12/2024) — batterie de traction](https://www.culture.fr/franceterme/france_terme_rtf?num=BATT5) — type `reference`
- [ADEME — Avis sur le véhicule électrique : une batterie de taille raisonnable (12/10/2022)](https://www.ademe.fr/presse/communique-national/mondial-de-lautomobile-lademe-publie-son-avis-sur-le-vehicule-electrique-une-batterie-de-taille-raisonnable-assure-une-pertinence-climatique-et-economique/) — type `reference`
- [INRS / Carsat Hauts-de-France — Batteries au lithium : panorama des technologies et des utilisations (22/11/2022)](https://www.inrs.fr/dam/inrs/PDF/Actes-et-comptes-rendus/2022-11-22-JT%20Lithium/1-Le-Minor.pdf) — type `reference`

**Fiches liées après** : `accumulateur`, `ampere-heure`, `batterie-lithium-ion`, `borne-de-recharge`, `freinage-regeneratif`, `kilowattheure` (nouveau), `moteur-electrique` (nouveau), `stockage-d-energie`, `vehicule-electrique`

```
fiche : batterie-de-traction
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```
