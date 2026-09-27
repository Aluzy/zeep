---
lot: J4-L7
role: controle
date: 2026-09-27
changeset: agents/changesets/J4-L7.jsonl
elements: ["facteur-de-puissance", "farad", "frequence-electrique", "henry", "hertz", "induction-electromagnetique", "ion", "joule", "kilowatt", "loi-de-faraday", "loi-de-lenz", "multimetre", "ohm", "ohmmetre", "periode", "pont-de-wheatstone", "pont-diviseur-de-courant", "pont-diviseur-de-tension", "puissance-active", "puissance-apparente"]
---

# Contrôle du lot J4-L7

20 fiche(s), 29 opération(s) du rédacteur (changeset non encore appliqué).

## Consignes du contrôleur

Tu es le **contrôleur** du lot J4-L7. Tu n'as pas participé à la rédaction et tu ne la vois qu'à
travers ce document : les justifications du rédacteur sont volontairement absentes. Tu vérifies
chaque fiche contre les **12 critères** de `docs/grille-relecture.md` (lis-la en entier d'abord).

1. **Ouvre chaque URL de source** et vérifie qu'elle appuie la définition. Une source que tu ne
   peux pas ouvrir, imprécise (page d'accueil) ou qui n'appuie pas l'affirmation = critère 8 en échec.
2. Une fiche est **conforme** si les 12 critères passent. Dans `agents/changesets/J4-L7-controle.jsonl`, remplace alors
   `"__A_REMPLIR__"` de `new` par
   `{"date": "2026-09-27", "par": "agent-controleur-J4-L7", "statut": "relu-ia"}` et `why` par
   « Relue selon la grille (12 critères) ».
3. Une fiche **refusée** : supprime sa ligne dans `agents/changesets/J4-L7-controle.jsonl`, et note les critères en échec. Tu ne
   réécris pas la fiche : le rédacteur la corrige (nouvelle passe de contrôle) ou la retire du lot.
   Si le défaut porte sur une fiche hors lot, ajoute-la à `agents/donnees/signalements.json`.
4. Écris tes verdicts dans la section « Relecture (rempli par le contrôleur) » de
   `agents/rapports/J4-L7.md`, une ligne par fiche : critères en échec, décision.
5. Vérifie : `python3 scripts/apply_changeset.py agents/changesets/J4-L7.jsonl agents/changesets/J4-L7-controle.jsonl --dry-run`.
   Tu ne poses **jamais** `"statut": "valide"` (réservé à Alexandre).


## Fiches à contrôler

### 1. Facteur de puissance — `facteur-de-puissance`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Synonymes** : cos phi, cos φ, cosinus phi, facteur de puissance → **cos phi, cos φ, cosinus phi**

**Sources après** (à ouvrir une par une) :
- [Larousse — facteur de puissance](https://www.larousse.fr/dictionnaires/francais/puissance/65022#165621) — type `reference`

**Fiches liées après** : `condensateur`, `dephasage`, `puissance-active`, `puissance-apparente`, `puissance-reactive`, `voltampere`

```
fiche : facteur-de-puissance
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 2. Farad — `farad`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [Larousse — farad](https://www.larousse.fr/dictionnaires/francais/farad/32865) — type `reference`

**Fiches liées après** : `charge-electrique`, `condensateur`, `coulomb`, `dielectrique`, `supercondensateur`, `tension-electrique`

```
fiche : farad
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 3. Fréquence électrique — `frequence-electrique`

- Niveau scolaire : BACPRO (cycles BACPRO)
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (19 mots) :
> Nombre de cycles par seconde d'un courant alternatif, exprimé en hertz, généralement 50 Hz sur le réseau électrique français.

**Définition — après** (46 mots) :
> Grandeur qui indique le nombre de fois par seconde qu'un courant alternatif ou une tension alternative reprend la même valeur, exprimée en hertz. Sur le réseau électrique français, elle vaut cinquante hertz ; un convertisseur de fréquence peut la régler pour piloter la vitesse d'un moteur.

**Sources après** (à ouvrir une par une) :
- [Larousse — fréquence (sens 4, Physique)](https://www.larousse.fr/dictionnaires/francais/fr%C3%A9quence/35185) — type `reference`

**Fiches liées après** : `convertisseur-de-frequence`, `courant-alternatif`, `delestage`, `generateur-de-fonctions`, `harmoniques`, `hertz`, `impedance`, `modulation`, `oscillateur`, `oscilloscope`, `periode`, `reactance`, `reseau-electrique`, `resonance`, `transformateur`

```
fiche : frequence-electrique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 4. Henry — `henry`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [Larousse — henry](https://www.larousse.fr/dictionnaires/francais/henry/39575) — type `reference`

**Fiches liées après** : `bobine-inductance`, `impedance`, `induction-electromagnetique`, `tension-electrique`

```
fiche : henry
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 5. Hertz — `hertz`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [Larousse — hertz](https://www.larousse.fr/dictionnaires/francais/hertz/39733) — type `reference`

**Fiches liées après** : `courant-alternatif`, `frequence-electrique`, `periode`, `signal-analogique`

```
fiche : hertz
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 6. Induction électromagnétique — `induction-electromagnetique`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (22 mots) :
> Phénomène par lequel un champ magnétique variable produit une tension électrique dans un conducteur électrique, principe utilisé par l'alternateur et le transformateur.

**Définition — après** (47 mots) :
> Phénomène par lequel la variation du flux magnétique traversant un circuit électrique y fait apparaître une tension induite, décrite par la loi de Faraday ; le sens du courant qui en résulte obéit à la loi de Lenz. Il fonde le fonctionnement de l'alternateur et du transformateur.

**Sources après** (à ouvrir une par une) :
- [Larousse — Encyclopédie, induction électromagnétique](https://www.larousse.fr/encyclopedie/divers/induction_%C3%A9lectromagn%C3%A9tique/61023) — type `reference`

**Fiches liées après** : `alternateur`, `champ-magnetique`, `conducteur-electrique`, `henry`, `histoire-de-l-electricite`, `loi-de-faraday`, `loi-de-lenz`, `tension-electrique`, `tesla`, `transformateur`, `weber`

```
fiche : induction-electromagnetique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 7. Ion — `ion`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [Larousse — ion](https://www.larousse.fr/dictionnaires/francais/ion/44184) — type `reference`

**Fiches liées après** : `atome`, `batterie-lithium-ion`, `charge-electrique`, `electrolyse`, `electron`

```
fiche : ion
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 8. Joule — `joule`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [Larousse — joule](https://www.larousse.fr/dictionnaires/francais/joule/45028) — type `reference`

**Fiches liées après** : `effet-joule`, `energie-electrique`, `kilowattheure`, `puissance-electrique`, `watt`

```
fiche : joule
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 9. Kilowatt — `kilowatt`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (19 mots) :
> Unité de puissance électrique équivalente à 1000 watts, utilisée pour exprimer la puissance des appareils ou d'une installation électrique.

**Définition — après** (33 mots) :
> Unité de mesure de la puissance, de symbole kW, équivalant à mille watts. Elle exprime aussi bien la puissance électrique d'un appareil ou d'une installation que celle d'un moteur thermique ou d'une chaudière.

**Sources après** (à ouvrir une par une) :
- [Larousse — kilowatt](https://www.larousse.fr/dictionnaires/francais/kilowatt/45540) — type `reference`

**Fiches liées après** : `installation-electrique`, `kilowattheure`, `puissance-electrique`

```
fiche : kilowatt
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 10. Loi de Faraday — `loi-de-faraday`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [Larousse — Encyclopédie, induction électromagnétique](https://www.larousse.fr/encyclopedie/divers/induction_%C3%A9lectromagn%C3%A9tique/61023) — type `reference`

**Fiches liées après** : `alternateur`, `dynamo`, `induction-electromagnetique`, `loi-de-lenz`, `transformateur`, `weber`

```
fiche : loi-de-faraday
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 11. Loi de Lenz — `loi-de-lenz`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [Larousse — Encyclopédie, induction électromagnétique](https://www.larousse.fr/encyclopedie/divers/induction_%C3%A9lectromagn%C3%A9tique/61023) — type `reference`

**Fiches liées après** : `bobine-inductance`, `champ-magnetique`, `induction-electromagnetique`, `loi-de-faraday`

```
fiche : loi-de-lenz
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 12. Multimètre — `multimetre`

- Niveau scolaire : 2GT (cycles 2GT, 1G)
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (24 mots) :
> Instrument de mesure polyvalent permettant de mesurer la tension électrique, l'intensité électrique et la résistance électrique, combinant les fonctions de voltmètre, ampèremètre et ohmmètre.

**Définition — après** (36 mots) :
> Instrument de mesure polyvalent qui combine les fonctions du voltmètre, de l'ampèremètre et de l'ohmmètre : selon le réglage choisi, il mesure la tension électrique, l'intensité électrique ou la résistance électrique d'un circuit ou d'un composant.

**Sources après** (à ouvrir une par une) :
- [Larousse — multimètre](https://www.larousse.fr/dictionnaires/francais/multim%C3%A8tre/53191) — type `reference`

**Fiches liées après** : `amperemetre`, `caracteristique-tension-courant`, `code-couleur-des-resistances`, `intensite-electrique`, `ohmmetre`, `oscilloscope`, `pince-amperemetrique`, `pont-de-wheatstone`, `resistance-electrique`, `technicien-de-maintenance`, `tension-electrique`, `valeur-efficace`, `voltmetre`

```
fiche : multimetre
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 13. Ohm — `ohm`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (13 mots) :
> Unité de mesure de la résistance électrique dans le Système international, symbole Ω.

**Définition — après** (40 mots) :
> Unité de mesure de la résistance électrique dans le Système international, de symbole Ω. Un conducteur électrique a une résistance de un ohm si une tension de un volt entre ses deux bornes y produit un courant de un ampère.

**Sources après** (à ouvrir une par une) :
- [Larousse — ohm](https://www.larousse.fr/dictionnaires/francais/ohm/55778) — type `reference`

**Fiches liées après** : `code-couleur-des-resistances`, `conducteur-electrique` (nouveau), `impedance`, `loi-d-ohm`, `reactance`, `resistance`, `resistance-electrique`, `siemens`

```
fiche : ohm
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 14. Ohmmètre — `ohmmetre`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (16 mots) :
> Instrument de mesure de la résistance électrique d'un composant ou d'un conducteur électrique, exprimée en ohms.

**Définition — après** (37 mots) :
> Instrument de mesure de la résistance électrique d'un composant ou d'un conducteur, exprimée en ohms. Il applique une tension connue au composant, hors tension et déconnecté du circuit, et calcule sa résistance à partir du courant mesuré.

**Synonymes** : — → **ohm-mètre**

**Sources après** (à ouvrir une par une) :
- [Larousse — ohmmètre](https://www.larousse.fr/dictionnaires/francais/ohmm%C3%A8tre/55781) — type `reference`

**Fiches liées après** : `conducteur-electrique`, `multimetre`, `resistance-electrique`

```
fiche : ohmmetre
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 15. Période — `periode`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [Larousse — période (sens 12, Physique)](https://www.larousse.fr/dictionnaires/francais/p%C3%A9riode/59576) — type `reference`

**Fiches liées après** : `courant-alternatif`, `frequence-electrique`, `hertz`, `oscilloscope`, `signal-analogique`, `triphase`, `valeur-crete`

```
fiche : periode
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 16. Pont de Wheatstone — `pont-de-wheatstone`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [Larousse — pont (sens 4, Électricité)](https://www.larousse.fr/dictionnaires/francais/pont/62556) — type `reference`

**Fiches liées après** : `capteur`, `multimetre`, `pont-diviseur-de-tension`, `resistance-electrique`, `thermistance`

```
fiche : pont-de-wheatstone
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 17. Pont diviseur de courant — `pont-diviseur-de-courant`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [IUT en ligne — Bases de l'électricité, chap. 1 : lois générales de l'électricité en régime continu (M. Piou)](https://public.iutenligne.net/electronique/piou_fruitet_fortun/baselecpro/acquisition/pdf/DL-001051-04-01.01.00.pdf#page=17) — type `manuel`

**Fiches liées après** : `circuit-electrique`, `courant-electrique`, `loi-des-noeuds`, `resistance`

```
fiche : pont-diviseur-de-courant
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 18. Pont diviseur de tension — `pont-diviseur-de-tension`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [IUT en ligne — Bases de l'électricité, chap. 1 : lois générales de l'électricité en régime continu (M. Piou)](https://public.iutenligne.net/electronique/piou_fruitet_fortun/baselecpro/acquisition/pdf/DL-001051-04-01.01.00.pdf#page=9) — type `manuel`

**Fiches liées après** : `circuit-electrique`, `loi-d-ohm`, `pont-de-wheatstone`, `potentiometre`, `resistance`, `tension-electrique`

```
fiche : pont-diviseur-de-tension
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 19. Puissance active — `puissance-active`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [Larousse — puissance active](https://www.larousse.fr/dictionnaires/francais/puissance/65022#165623) — type `reference`

**Fiches liées après** : `compteur-electrique`, `facteur-de-puissance`, `puissance-apparente`, `puissance-electrique`, `puissance-reactive`, `watt`

```
fiche : puissance-active
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 20. Puissance apparente — `puissance-apparente`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [Larousse — puissance apparente](https://www.larousse.fr/dictionnaires/francais/apparent/4640#150991) — type `reference`

**Fiches liées après** : `facteur-de-puissance`, `puissance-active`, `puissance-reactive`, `transformateur`, `voltampere`

```
fiche : puissance-apparente
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```
