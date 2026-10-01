---
lot: J5-S5
role: controle
date: 2026-10-01
changeset: agents/changesets/J5-S5.jsonl
elements: ["constante-de-temps"]
---

# Contrôle du lot J5-S5 — passe 4

1 fiche(s), 53 opération(s) du rédacteur (changeset non encore appliqué).

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

### 1. Constante de temps — `constante-de-temps`

- Niveau scolaire : TG (cycles TG)
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (30 mots) :
> Durée caractéristique de la charge ou de la décharge d'un circuit contenant un condensateur ou une bobine. Au bout de cinq constantes de temps, le régime est considéré comme établi.

**Définition — après** (42 mots) :
> Durée caractéristique de la charge ou de la décharge d'un condensateur dans un circuit RC : au bout de cette durée, l'écart entre la tension aux bornes du condensateur et sa valeur finale a été divisé par le nombre e, environ 2,7.

**Version simple — avant** (22 mots) :
> C'est le temps que met un condensateur à se remplir ou à se vider en grande partie. Il dépend des composants choisis.

**Version simple — après** (33 mots) :
> C'est le temps que met un condensateur à se remplir ou à se vider en grande partie, comme le temps qu'il faut à un thé chaud pour refroidir. Il dépend des composants choisis.

**Sources après** (à ouvrir une par une) :
- [Programme de physique-chimie de terminale générale, enseignement de spécialité, « Modèle du circuit RC série »](https://www.education.gouv.fr/sites/default/files/document/Programme%20de%20physique-chimie%20de%20terminale%20g%C3%A9n%C3%A9rale-253485.pdf) — type `programme`
- [IEC 60050 (Electropedia), IEV 103-05-26 « time constant »](https://www.electropedia.org/iev/iev.nsf/IEVref_xref/en:103-05-26) — type `reference`

**Fiches liées après** : `bobine-inductance` (nouveau), `circuit-rc`, `circuit-rl`, `condensateur`, `regime-transitoire`, `tension-electrique` (nouveau)

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
