---
lot: J4-L1
role: controle
date: 2026-09-25
changeset: agents/changesets/J4-L1.jsonl
elements: ["protocole-de-communication"]
---

# Contrôle du lot J4-L1 — passe 3

1 fiche(s), 99 opération(s) du rédacteur (changeset non encore appliqué).

## Consignes du contrôleur

Tu es le **contrôleur** du lot J4-L1. Tu n'as pas participé à la rédaction et tu ne la vois qu'à
travers ce document : les justifications du rédacteur sont volontairement absentes. Tu vérifies
chaque fiche contre les **12 critères** de `docs/grille-relecture.md` (lis-la en entier d'abord).

1. **Ouvre chaque URL de source** et vérifie qu'elle appuie la définition. Une source que tu ne
   peux pas ouvrir, imprécise (page d'accueil) ou qui n'appuie pas l'affirmation = critère 8 en échec.
2. Une fiche est **conforme** si les 12 critères passent. Dans `agents/changesets/J4-L1-controle.jsonl`, remplace alors
   `"__A_REMPLIR__"` de `new` par
   `{"date": "2026-09-25", "par": "agent-controleur-J4-L1", "statut": "relu-ia"}` et `why` par
   « Relue selon la grille (12 critères) ».
3. Une fiche **refusée** : supprime sa ligne dans `agents/changesets/J4-L1-controle.jsonl`, et note les critères en échec. Tu ne
   réécris pas la fiche : le rédacteur la corrige (nouvelle passe de contrôle) ou la retire du lot.
   Si le défaut porte sur une fiche hors lot, ajoute-la à `agents/donnees/signalements.json`.
4. Écris tes verdicts dans la section « Relecture (rempli par le contrôleur) » de
   `agents/rapports/J4-L1.md`, une ligne par fiche : critères en échec, décision.
5. Vérifie : `python3 scripts/apply_changeset.py agents/changesets/J4-L1.jsonl agents/changesets/J4-L1-controle.jsonl --dry-run`.
   Tu ne poses **jamais** `"statut": "valide"` (réservé à Alexandre).


## Fiches à contrôler

### 1. Protocole de communication — `protocole-de-communication`

- Niveau scolaire : C4 (cycles C4) — version simple obligatoire
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (25 mots) :
> Ensemble de règles définissant l'échange de données sur un bus de données ou une interface série, comme le bus I2C, le bus SPI ou l'USB.

**Définition — après** (50 mots) :
> Ensemble de règles communes qui fixent comment des appareils échangent des données : format des messages, ordre des échanges, détection des erreurs. Il en existe pour les liaisons entre composants, comme le bus I2C, ou entre appareils, comme l'USB, et pour les réseaux, comme Internet, le Wi-Fi ou le Bluetooth.

**Version simple — avant** (0 mots) :
_(vide)_

**Version simple — après** (31 mots) :
> Un protocole, ce sont les règles que deux appareils suivent pour se comprendre, comme une langue commune. Grâce à lui, une manette sans fil peut parler à une console de jeu.

**Synonymes** : — → **protocole**

**Sources après** (à ouvrir une par une) :
- [Programme du cycle 4 en vigueur à la rentrée 2020 (d'après le BOEN n° 31 du 30 juillet 2020), p. 124 : technologie, « Comprendre le fonctionnement d'un réseau informatique » (notion de protocole, routage, Internet)](https://eduscol.education.gouv.fr/sites/default/files/document/programme-d-enseignement-du-cycle-4-67722.pdf#page=124) — type `programme`
- [Dictionnaire de français Larousse, article « protocole »](https://www.larousse.fr/dictionnaires/francais/protocole/64577) — type `reference`

**Fiches liées après** : `bluetooth`, `bus-can`, `bus-de-donnees`, `bus-i2c`, `bus-spi`, `ethernet`, `interface-serie-uart`, `modbus`, `mqtt`, `reseau-maille`, `rs-485`, `usb`, `wi-fi`

```
fiche : protocole-de-communication
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```
