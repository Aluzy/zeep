---
lot: J4-L9
role: controle
date: 2026-09-27
changeset: agents/changesets/J4-L9.jsonl
elements: ["alternateur", "barrage-hydroelectrique", "biomasse", "centrale-electrique", "centrale-eolienne", "centrale-hydraulique", "centrale-nucleaire", "centrale-solaire", "centrale-thermique", "cogeneration", "dynamo", "energie-fossile", "energie-maremotrice", "energie-renouvelable", "eolienne", "facteur-de-charge", "geothermie", "onduleur", "production-d-electricite", "watt-crete"]
---

# Contrôle du lot J4-L9

20 fiche(s), 47 opération(s) du rédacteur (changeset non encore appliqué).

## Consignes du contrôleur

Tu es le **contrôleur** du lot J4-L9. Tu n'as pas participé à la rédaction et tu ne la vois qu'à
travers ce document : les justifications du rédacteur sont volontairement absentes. Tu vérifies
chaque fiche contre les **12 critères** de `docs/grille-relecture.md` (lis-la en entier d'abord).

1. **Ouvre chaque URL de source** et vérifie qu'elle appuie la définition. Une source que tu ne
   peux pas ouvrir, imprécise (page d'accueil) ou qui n'appuie pas l'affirmation = critère 8 en échec.
2. Une fiche est **conforme** si les 12 critères passent. Dans `agents/changesets/J4-L9-controle.jsonl`, remplace alors
   `"__A_REMPLIR__"` de `new` par
   `{"date": "2026-09-27", "par": "agent-controleur-J4-L9", "statut": "relu-ia"}` et `why` par
   « Relue selon la grille (12 critères) ».
3. Une fiche **refusée** : supprime sa ligne dans `agents/changesets/J4-L9-controle.jsonl`, et note les critères en échec. Tu ne
   réécris pas la fiche : le rédacteur la corrige (nouvelle passe de contrôle) ou la retire du lot.
   Si le défaut porte sur une fiche hors lot, ajoute-la à `agents/donnees/signalements.json`.
4. Écris tes verdicts dans la section « Relecture (rempli par le contrôleur) » de
   `agents/rapports/J4-L9.md`, une ligne par fiche : critères en échec, décision.
5. Vérifie : `python3 scripts/apply_changeset.py agents/changesets/J4-L9.jsonl agents/changesets/J4-L9-controle.jsonl --dry-run`.
   Tu ne poses **jamais** `"statut": "valide"` (réservé à Alexandre).


## Fiches à contrôler

### 1. Alternateur — `alternateur`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (18 mots) :
> Machine électrique qui convertit l'énergie mécanique en courant alternatif, utilisée dans les centrales électriques pour la production d'électricité.

**Définition — après** (37 mots) :
> Générateur électrique qui convertit l'énergie mécanique d'un arbre entraîné en rotation, par exemple par une turbine, en énergie électrique fournie sous forme de courant alternatif, grâce au phénomène d'induction électromagnétique. Il équipe la plupart des centrales électriques.

**Sources après** (à ouvrir une par une) :
- [Dictionnaire de français Larousse, article « alternateur »](https://www.larousse.fr/dictionnaires/francais/alternateur/2565) — type `reference`

**Fiches liées après** : `barrage-hydroelectrique`, `centrale-electrique` (nouveau), `centrale-hydraulique` (nouveau), `centrale-nucleaire`, `centrale-thermique` (nouveau), `courant-alternatif`, `dynamo` (nouveau), `electricite`, `generateur-electrique`, `induction-electromagnetique`, `loi-de-faraday`, `production-d-electricite`, `turbine`

```
fiche : alternateur
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 2. Barrage hydroélectrique — `barrage-hydroelectrique`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (22 mots) :
> Ouvrage retenant l'eau d'un cours d'eau afin d'actionner une turbine reliée à un alternateur pour produire de l'électricité dans une centrale hydraulique.

**Définition — après** (34 mots) :
> Ouvrage qui retient l'eau d'un cours d'eau pour former une retenue et l'acheminer vers les turbines d'une centrale hydraulique ; en s'écoulant, l'eau actionne une turbine reliée à un alternateur qui produit de l'électricité.

**Sources après** (à ouvrir une par une) :
- [Connaissance des Énergies, fiche pédagogique « Hydroélectricité »](https://www.connaissancedesenergies.org/fiche-pedagogique/hydroelectricite) — type `manuel`

**Fiches liées après** : `alternateur`, `centrale-hydraulique`, `electricite`, `station-de-transfert-d-energie-par-pompage`, `turbine`

```
fiche : barrage-hydroelectrique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 3. Biomasse — `biomasse`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [Ministère de la Transition écologique, « Biomasse énergie »](https://www.ecologie.gouv.fr/politiques-publiques/biomasse-energie) — type `reference`

**Fiches liées après** : `centrale-thermique`, `cogeneration`, `energie-renouvelable`, `production-d-electricite`, `turbine`

```
fiche : biomasse
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 4. Centrale électrique — `centrale-electrique`

- Niveau scolaire : BACPRO (cycles BACPRO)
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (22 mots) :
> Installation industrielle qui assure la production d'électricité à partir d'une source d'énergie, comme le nucléaire, le thermique, l'hydraulique, le solaire ou l'éolien.

**Définition — après** (39 mots) :
> Installation industrielle qui convertit une énergie primaire — nucléaire, chimique dans un combustible fossile ou la biomasse, mécanique dans l'eau ou le vent, ou solaire — en énergie électrique, le plus souvent au moyen d'une turbine et d'un alternateur.

**Sources après** (à ouvrir une par une) :
- [Connaissance des Énergies, fiche pédagogique « Électricité »](https://www.connaissancedesenergies.org/fiche-pedagogique/electricite) — type `manuel`

**Fiches liées après** : `alternateur` (nouveau), `centrale-hydraulique`, `centrale-nucleaire`, `centrale-solaire`, `centrale-thermique`, `electricite`, `production-d-electricite`, `turbine` (nouveau)

```
fiche : centrale-electrique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 5. Centrale éolienne — `centrale-eolienne`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (12 mots) :
> Ensemble d'éoliennes qui produisent de l'électricité à partir de l'énergie du vent.

**Définition — après** (35 mots) :
> Ensemble de plusieurs éoliennes regroupées sur un même site et raccordées au réseau électrique, aussi appelé parc éolien. Chaque éolienne convertit l'énergie cinétique du vent en énergie mécanique, transformée en électricité par un générateur électrique.

**Synonymes** : — → **parc eolien**

**Sources après** (à ouvrir une par une) :
- [Ministère de la Transition écologique, « Éolien terrestre »](https://www.ecologie.gouv.fr/politiques-publiques/eolien-terrestre) — type `reference`

**Fiches liées après** : `electricite`, `eolienne` (nouveau), `generateur-electrique` (nouveau)

```
fiche : centrale-eolienne
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 6. Centrale hydraulique — `centrale-hydraulique`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (22 mots) :
> Centrale électrique qui produit de l'électricité en utilisant la force de l'eau, souvent au moyen d'un barrage hydroélectrique, pour entraîner une turbine.

**Définition — après** (38 mots) :
> Centrale électrique qui convertit l'énergie cinétique de l'eau, d'une rivière ou d'une retenue formée par un barrage hydroélectrique, en énergie électrique au moyen d'une turbine couplée à un alternateur ; c'est la première source d'électricité renouvelable en France.

**Synonymes** : — → **centrale hydroelectrique**

**Sources après** (à ouvrir une par une) :
- [Connaissance des Énergies, fiche pédagogique « Hydroélectricité »](https://www.connaissancedesenergies.org/fiche-pedagogique/hydroelectricite) — type `manuel`

**Fiches liées après** : `alternateur` (nouveau), `barrage-hydroelectrique`, `centrale-electrique`, `electricite`, `energie-maremotrice`, `station-de-transfert-d-energie-par-pompage`, `turbine`

```
fiche : centrale-hydraulique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 7. Centrale nucléaire — `centrale-nucleaire`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (22 mots) :
> Centrale électrique produisant de l'électricité grâce à la chaleur dégagée par une réaction de fission nucléaire, actionnant une turbine et un alternateur.

**Définition — après** (37 mots) :
> Centrale électrique dans laquelle la chaleur dégagée par une réaction de fission nucléaire en chaîne, contrôlée dans le cœur du réacteur, produit de la vapeur qui actionne une turbine couplée à un alternateur pour produire de l'électricité.

**Sources après** (à ouvrir une par une) :
- [Connaissance des Énergies, fiche pédagogique « Principes de fonctionnement d'un réacteur nucléaire »](https://www.connaissancedesenergies.org/fiche-pedagogique/principes-de-fonctionnement-dun-reacteur-nucleaire) — type `manuel`

**Fiches liées après** : `alternateur`, `centrale-electrique`, `electricite`, `mix-energetique`, `turbine`

```
fiche : centrale-nucleaire
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 8. Centrale solaire — `centrale-solaire`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (18 mots) :
> Centrale électrique qui produit de l'électricité à partir du rayonnement du soleil, notamment grâce à des panneaux photovoltaïques.

**Définition — après** (38 mots) :
> Centrale électrique qui produit de l'électricité à partir du rayonnement solaire, le plus souvent grâce à des panneaux photovoltaïques qui le convertissent directement en électricité, plus rarement en le concentrant pour produire de la chaleur puis de l'électricité.

**Sources après** (à ouvrir une par une) :
- [Connaissance des Énergies, fiche pédagogique « Solaire photovoltaïque »](https://www.connaissancedesenergies.org/fiche-pedagogique/solaire-photovoltaique) — type `manuel`

**Fiches liées après** : `centrale-electrique`, `electricite`, `watt-crete`

```
fiche : centrale-solaire
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 9. Centrale thermique — `centrale-thermique`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (19 mots) :
> Centrale électrique qui produit de l'électricité en brûlant une énergie fossile ou de la biomasse pour actionner une turbine.

**Définition — après** (39 mots) :
> Centrale électrique qui produit de l'électricité à partir d'une source de chaleur — le plus souvent en brûlant une énergie fossile ou de la biomasse — pour produire de la vapeur qui actionne une turbine couplée à un alternateur.

**Sources après** (à ouvrir une par une) :
- [Connaissance des Énergies, « Une centrale thermique utilise-t-elle toujours du combustible fossile ? »](https://www.connaissancedesenergies.org/idees-recues-energies/idee-recue-une-centrale-thermique-utilise-toujours-du-combustible-fossile) — type `manuel`

**Fiches liées après** : `alternateur` (nouveau), `biomasse`, `centrale-electrique`, `cogeneration`, `electricite`, `energie-fossile`, `geothermie`, `turbine`

```
fiche : centrale-thermique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 10. Cogénération — `cogeneration`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [Connaissance des Énergies, « Qu'est-ce que la cogénération ? »](https://www.connaissancedesenergies.org/questions-et-reponses-energies/quest-ce-que-la-cogeneration) — type `manuel`

**Fiches liées après** : `biomasse`, `centrale-thermique`, `efficacite-energetique`, `rendement-energetique`

```
fiche : cogeneration
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 11. Dynamo — `dynamo`

- Niveau scolaire : TG (cycles TG)
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (11 mots) :
> Générateur électrique produisant un courant continu à partir d'une rotation mécanique.

**Définition — après** (36 mots) :
> Générateur électrique qui convertit l'énergie mécanique d'une rotation en énergie électrique fournie sous forme de courant continu, par un principe d'induction électromagnétique proche de celui de l'alternateur ; elle équipait les vélos et les véhicules automobiles.

**Sources après** (à ouvrir une par une) :
- [Dictionnaire de français Larousse, article « dynamo »](https://www.larousse.fr/dictionnaires/francais/dynamo/27092) — type `reference`

**Fiches liées après** : `alternateur` (nouveau), `courant-continu`, `generateur-electrique`, `induction-electromagnetique` (nouveau), `loi-de-faraday`

```
fiche : dynamo
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 12. Énergie fossile — `energie-fossile`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (21 mots) :
> Source d'énergie issue de matières organiques fossilisées, comme le charbon, le pétrole ou le gaz, utilisée notamment dans les centrales thermiques.

**Définition — après** (39 mots) :
> Énergie stockée dans le sous-sol sous forme d'hydrocarbures issus de la sédimentation de matières organiques enfouies depuis des centaines de millions d'années, comme le charbon, le pétrole ou le gaz naturel ; elle n'est pas renouvelable à l'échelle humaine.

**Sources après** (à ouvrir une par une) :
- [Connaissance des Énergies, « Qu'est-ce qu'une énergie fossile ? »](https://www.connaissancedesenergies.org/questions-et-reponses-energies/quest-ce-quune-energie-fossile) — type `manuel`

**Fiches liées après** : `centrale-thermique`, `empreinte-carbone-de-l-electricite`, `mix-energetique`

```
fiche : energie-fossile
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 13. Énergie marémotrice — `energie-maremotrice`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [Ministère de la Transition écologique, « Énergies marines renouvelables (hors éolien en mer) »](https://www.ecologie.gouv.fr/politiques-publiques/energies-marines-renouvelables-hors-eolien-mer) — type `reference`

**Fiches liées après** : `centrale-hydraulique`, `energie-renouvelable`, `production-d-electricite`, `turbine`

```
fiche : energie-maremotrice
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 14. Énergie renouvelable — `energie-renouvelable`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (21 mots) :
> Source d'énergie, comme le soleil, le vent ou l'eau, considérée comme inépuisable à l'échelle humaine et utilisée pour la production d'électricité.

**Définition — après** (41 mots) :
> Énergie produite à partir d'une source considérée comme inépuisable à l'échelle humaine — le rayonnement solaire, le vent, l'eau, la chaleur du sous-sol ou la biomasse — et qui n'engendre pas ou peu d'émissions polluantes, à la différence des énergies fossiles.

**Synonymes** : — → **EnR**

**Sources après** (à ouvrir une par une) :
- [Ministère de la Transition écologique, « Les énergies renouvelables »](https://www.ecologie.gouv.fr/politiques-publiques/energies-renouvelables) — type `reference`

**Fiches liées après** : `biomasse`, `electricite`, `empreinte-carbone-de-l-electricite`, `energie-maremotrice`, `geothermie`, `hydrogene`, `mix-energetique`, `panneau-photovoltaique`, `production-d-electricite`, `stockage-d-energie`

```
fiche : energie-renouvelable
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 15. Éolienne — `eolienne`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (16 mots) :
> Machine équipée de pales qui transforme l'énergie du vent en électricité grâce à un générateur électrique.

**Définition — après** (36 mots) :
> Dispositif équipé de pales qui convertit l'énergie cinétique du vent en énergie mécanique, transformée le plus souvent en électricité grâce à un générateur électrique ; plusieurs éoliennes regroupées forment un parc éolien, aussi appelé centrale éolienne.

**Synonymes** : — → **aerogenerateur**

**Sources après** (à ouvrir une par une) :
- [Ministère de la Transition écologique, « Éolien terrestre »](https://www.ecologie.gouv.fr/politiques-publiques/eolien-terrestre) — type `reference`

**Fiches liées après** : `centrale-eolienne` (nouveau), `electricite`, `facteur-de-charge`, `generateur-electrique`, `terres-rares`

```
fiche : eolienne
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 16. Facteur de charge — `facteur-de-charge`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [RTE, glossaire « Analyses et données » — Facteur de charge](https://analysesetdonnees.rte-france.com/glossaire#facteur-de-charge) — type `reference`

**Fiches liées après** : `eolienne`, `panneau-photovoltaique`, `production-d-electricite`, `rendement-energetique`, `watt-crete`

```
fiche : facteur-de-charge
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 17. Géothermie — `geothermie`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [Ministère de la Transition écologique, « Géothermie »](https://www.ecologie.gouv.fr/politiques-publiques/geothermie) — type `reference`

**Fiches liées après** : `centrale-thermique`, `energie-renouvelable`, `production-d-electricite`, `turbine`

```
fiche : geothermie
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 18. Onduleur — `onduleur`

- Niveau scolaire : STI2D (cycles STI2D)
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (18 mots) :
> Appareil qui convertit un courant continu, par exemple issu d'un panneau photovoltaïque ou d'une batterie, en courant alternatif.

**Définition — après** (31 mots) :
> Convertisseur statique d'énergie électrique qui transforme un courant continu, par exemple issu d'un panneau photovoltaïque ou d'une batterie, en courant alternatif utilisable dans un bâtiment ou injectable sur le réseau électrique.

**Sources après** (à ouvrir une par une) :
- [Dictionnaire de français Larousse, article « onduleur »](https://www.larousse.fr/dictionnaires/francais/onduleur/56030) — type `reference`

**Fiches liées après** : `batterie`, `courant-alternatif`, `courant-continu`, `panneau-photovoltaique`, `transistor-igbt`

```
fiche : onduleur
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 19. Production d'électricité — `production-d-electricite`

- Niveau scolaire : TG (cycles TG, CAP, BACPRO, STI2D)
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (21 mots) :
> Ensemble des activités consistant à générer du courant électrique dans une centrale électrique, à partir d'une source d'énergie renouvelable ou fossile.

**Définition — après** (38 mots) :
> Ensemble des activités qui convertissent une énergie primaire — renouvelable, fossile ou nucléaire — en énergie électrique dans une centrale électrique, le plus souvent au moyen d'une turbine et d'un alternateur, avant son acheminement par le réseau électrique.

**Sources après** (à ouvrir une par une) :
- [Connaissance des Énergies, fiche pédagogique « Électricité »](https://www.connaissancedesenergies.org/fiche-pedagogique/electricite) — type `manuel`

**Fiches liées après** : `alternateur`, `biomasse`, `centrale-electrique`, `courant-electrique`, `energie-maremotrice`, `energie-renouvelable`, `facteur-de-charge`, `geothermie`, `mix-energetique`, `reseau-intelligent-smart-grid`, `turbine` (nouveau)

```
fiche : production-d-electricite
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 20. Watt-crête — `watt-crete`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [Connaissance des Énergies, « Solaire photovoltaïque : que signifie la puissance crête ? »](https://www.connaissancedesenergies.org/questions-et-reponses-energies/solaire-photovoltaique-que-signifie-la-puissance-crete) — type `manuel`

**Fiches liées après** : `centrale-solaire`, `facteur-de-charge`, `panneau-photovoltaique`, `puissance-electrique`, `watt`

```
fiche : watt-crete
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```
