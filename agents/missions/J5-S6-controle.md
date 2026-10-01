---
lot: J5-S6
role: controle
date: 2026-10-01
changeset: agents/changesets/J5-S6.jsonl
elements: ["octet", "pont-de-diodes", "porte-non-et", "porte-non-ou", "porte-ou-exclusif", "quantification", "regime-transitoire", "supraconductivite", "systeme-binaire", "systeme-hexadecimal", "table-de-verite", "technicien-de-maintenance", "theoreme-de-shannon", "trou-electronique", "mix-energetique", "stockage-d-energie"]
---

# Contrôle du lot J5-S6

16 fiche(s), 53 opération(s) du rédacteur (changeset non encore appliqué).

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

### 1. Octet — `octet`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (28 mots) :
> Groupe de huit bits, unité de base de la mémoire informatique. Un octet permet de coder 256 valeurs différentes, ce qui suffit à représenter un caractère de texte.

**Définition — après** (42 mots) :
> Groupe de huit bits traité comme un tout par un système numérique. Il permet de coder 256 valeurs différentes et sert d'unité pour exprimer la taille des fichiers et la capacité des mémoires, avec des multiples comme le kilo-octet ou le gigaoctet.

**Version simple — avant** (21 mots) :
> Un octet est un paquet de huit bits. Les mémoires et les fichiers se comptent en milliers ou en millions d'octets.

**Version simple — après** (26 mots) :
> Un octet est un paquet de huit bits. La taille d'une photo ou d'un jeu sur une tablette se compte en millions ou en milliards d'octets.

**Synonymes** : Go, Mo, byte, kilo octet, octet → **byte, o, octet**

**Sources après** (à ouvrir une par une) :
- [IEC 60050 (Electropedia), IEV 171-02-12 « byte / octet »](https://electropedia.org/iev/iev.nsf/IEVref_xref/en:171-02-12) — type `reference`
- [Office québécois de la langue française, Grand dictionnaire terminologique, fiche « octet »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8387944/octet) — type `reference`
- [Encyclopédie Larousse, article « octet »](https://www.larousse.fr/encyclopedie/divers/octet/187782) — type `reference`

**Fiches liées après** : `bit`, `memoire-morte-rom`, `memoire-vive-ram`, `microprocesseur`, `systeme-binaire`, `systeme-hexadecimal`

```
fiche : octet
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 2. Pont de diodes — `pont-de-diodes`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (25 mots) :
> Assemblage de quatre diodes qui redresse les deux alternances d'une tension alternative. Associé à un condensateur de filtrage, il constitue l'étage d'entrée de nombreuses alimentations.

**Définition — après** (42 mots) :
> Montage redresseur formé de quatre diodes, aussi appelé pont de Graetz. Alimenté par une tension alternative, il fait circuler le courant dans la charge toujours dans le même sens, pendant les deux alternances, c'est-à-dire que la tension d'entrée soit positive ou négative.

**Version simple — avant** (19 mots) :
> Ce montage transforme un courant qui change de sens en un courant qui va toujours dans le même sens.

**Version simple — après** (29 mots) :
> Ce montage de quatre diodes reçoit un courant qui change sans cesse de sens et le fait circuler toujours dans le même sens, comme une rue à sens unique.

**Sources après** (à ouvrir une par une) :
- [IUT de Caen, Mesures physiques 1re année, TD d'électronique « Redressement », § 2.2 « Montage en pont (pont de Graetz) »](https://langloisp.users.greyc.fr/electronique/td/redres.pdf) — type `manuel`
- [IEC 60050 (Electropedia), IEV 551-15-14 « bridge connection »](https://electropedia.org/iev/iev.nsf/17127c61f2426ed8c1257cb5003c9bec/cec9dcd5367b5329c12571ef004ff66d) — type `reference`

**Fiches liées après** : `alimentation-electronique`, `courant-alternatif`, `courant-continu`, `diode`, `redresseur`

```
fiche : pont-de-diodes
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 3. Porte NON-ET — `porte-non-et`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Version simple — avant** (20 mots) :
> Cette porte répond non seulement quand toutes ses entrées disent oui. Avec elle seule, on peut fabriquer toutes les autres.

**Version simple — après** (31 mots) :
> Cette porte répond « non » seulement quand toutes ses entrées disent « oui », comme une lampe qui reste allumée sauf si l'on appuie sur deux boutons à la fois.

**Sources après** (à ouvrir une par une) :
- [Eric Cariou (Université de Pau et des Pays de l'Adour), cours d'architecture des ordinateurs, « Circuits logiques »](https://lab-sticc.univ-brest.fr/~ecariou/cours/archi/cours-3-circuits-logiques.pdf) — type `manuel`
- [Programme d'enseignement de spécialité de numérique et sciences informatiques de première générale (arrêté du 17 janvier 2019, BO spécial n° 1 du 22 janvier 2019), rubrique « Représentation des données : types et valeurs de base »](https://eduscol.education.fr/document/30007/download) — type `programme`

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

### 4. Porte NON-OU — `porte-non-ou`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Version simple — avant** (11 mots) :
> Cette porte répond oui seulement quand aucune entrée ne dit oui.

**Version simple — après** (32 mots) :
> Cette porte répond « oui » seulement quand aucune de ses entrées ne dit « oui », comme une lampe qui s'éteint dès qu'on appuie sur au moins un des deux boutons.

**Sources après** (à ouvrir une par une) :
- [Eric Cariou (Université de Pau et des Pays de l'Adour), cours d'architecture des ordinateurs, « Circuits logiques »](https://lab-sticc.univ-brest.fr/~ecariou/cours/archi/cours-3-circuits-logiques.pdf) — type `manuel`
- [Programme d'enseignement de spécialité de numérique et sciences informatiques de première générale (arrêté du 17 janvier 2019, BO spécial n° 1 du 22 janvier 2019), rubrique « Représentation des données : types et valeurs de base »](https://eduscol.education.fr/document/30007/download) — type `programme`

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

### 5. Porte OU exclusif — `porte-ou-exclusif`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (27 mots) :
> Porte logique dont la sortie est vraie lorsque ses deux entrées diffèrent. Elle réalise l'addition binaire sans retenue et sert au calcul des codes de contrôle d'erreur.

**Définition — après** (41 mots) :
> Porte logique dont la sortie est vraie lorsque ses deux entrées sont différentes. Elle donne le chiffre de la somme de deux bits, sans la retenue, ce qui en fait un élément du demi-additionneur, circuit qui additionne deux nombres d'un bit.

**Version simple — avant** (14 mots) :
> Cette porte dit oui quand ses deux entrées ne sont pas d'accord entre elles.

**Version simple — après** (31 mots) :
> Cette porte dit « oui » quand ses deux entrées sont différentes, comme une lampe qui s'allume si l'on appuie sur un seul des deux boutons, mais pas sur les deux.

**Sources après** (à ouvrir une par une) :
- [Programme d'enseignement de spécialité de numérique et sciences informatiques de première générale (arrêté du 17 janvier 2019, BO spécial n° 1 du 22 janvier 2019), rubrique « Représentation des données : types et valeurs de base »](https://eduscol.education.fr/document/30007/download) — type `programme`
- [Eric Cariou (Université de Pau et des Pays de l'Adour), cours d'architecture des ordinateurs, « Circuits logiques »](https://lab-sticc.univ-brest.fr/~ecariou/cours/archi/cours-3-circuits-logiques.pdf) — type `manuel`

**Fiches liées après** : `algebre-de-boole`, `bit` (nouveau), `circuit-logique`, `porte-logique`, `systeme-binaire`, `table-de-verite`

```
fiche : porte-ou-exclusif
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 6. Quantification — `quantification`

- Niveau scolaire : STI2D (cycles STI2D)
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (30 mots) :
> Attribution d'une valeur numérique parmi un nombre fini de niveaux à chaque échantillon mesuré. Le nombre de bits du convertisseur fixe la finesse obtenue et le bruit de quantification résiduel.

**Définition — après** (42 mots) :
> Opération qui découpe l'étendue des valeurs possibles d'un signal en intervalles et remplace chaque valeur mesurée par une valeur unique choisie dans son intervalle. Dans un convertisseur analogique-numérique, elle est notamment caractérisée par le nombre de bits utilisés pour coder chaque valeur.

**Version simple — avant** (21 mots) :
> Chaque mesure doit être arrondie à une valeur disponible. Plus il y a de valeurs possibles, plus la copie est fidèle.

**Version simple — après** (22 mots) :
> Comme un thermomètre qui n'affiche que des degrés entiers, un appareil numérique arrondit chaque mesure à l'une des valeurs qu'il sait écrire.

**Synonymes** : bits de resolution, pas de quantification, quantification, resolution → **quantification, quantization**

**Sources après** (à ouvrir une par une) :
- [IEC 60050 (Electropedia), IEV 702-04-07 « quantization »](https://electropedia.org/iev/iev.nsf/IEVref_xref/en:702-04-07) — type `reference`
- [Programme d'innovation technologique et d'ingénierie et développement durable de première et d'ingénierie, innovation et développement durable de terminale STI2D (Éduscol), § 2.4.2 « Conversion Analogique/Numérique (CAN) »](https://eduscol.education.fr/document/24916/download) — type `programme`

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

### 7. Régime transitoire — `regime-transitoire`

- Niveau scolaire : TG (cycles TG)
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (25 mots) :
> Phase pendant laquelle un circuit évolue après un changement, avant d'atteindre son état stable appelé régime permanent. C'est durant cette phase qu'apparaissent les surintensités d'enclenchement.

**Définition — après** (44 mots) :
> Phase pendant laquelle un circuit passe d'un état stable à un autre après un changement, par exemple sa mise sous tension. L'état stable, dans lequel les caractéristiques du circuit restent constantes au cours du temps, est appelé régime permanent, régime établi ou régime stationnaire.

**Synonymes** : regime permanent, regime transitoire, transitoire → **regime transitoire, transitoire**

**Sources après** (à ouvrir une par une) :
- [Programme de physique-chimie de terminale générale, enseignement de spécialité (BO spécial n° 8 du 25 juillet 2019), « Étudier la dynamique d'un système électrique »](https://cache.media.education.gouv.fr/file/SPE8_MENJ_25_7_2019/92/9/spe249_annexe_1158929.pdf) — type `programme`
- [Programme d'innovation technologique et d'ingénierie et développement durable de première et d'ingénierie, innovation et développement durable de terminale STI2D (Éduscol), § 3.3 « régime établi » et « régime transitoire »](https://eduscol.education.fr/document/24916/download) — type `programme`
- [IEC 60050 (Electropedia), IEV 103-05-02 « transient »](https://electropedia.org/iev/iev.nsf/IEVref_xref/en:103-05-02) — type `reference`
- [IEC 60050 (Electropedia), IEV 103-05-01 « steady state »](https://electropedia.org/iev/iev.nsf/IEVref_xref/en:103-05-01) — type `reference`

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

### 8. Supraconductivité — `supraconductivite`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (27 mots) :
> État de certains matériaux refroidis sous une température critique, dans lequel la résistance électrique disparaît totalement. Il permet des électroaimants très puissants, au prix d'une réfrigération coûteuse.

**Définition — après** (43 mots) :
> Propriété de certains matériaux qui, dans des conditions favorables, notamment sous une température dite critique, ne présentent plus aucune résistance au passage d'un courant continu et expulsent le champ magnétique. Elle sert par exemple à réaliser des bobines produisant des champs magnétiques intenses.

**Version simple — avant** (21 mots) :
> Refroidis très fort, certains matériaux laissent passer le courant sans aucune perte. On s'en sert pour faire des aimants très puissants.

**Version simple — après** (26 mots) :
> Refroidis très fort, certains matériaux laissent passer le courant sans résistance. On s'en sert dans certains appareils d'IRM, qui font des images de l'intérieur du corps.

**Sources après** (à ouvrir une par une) :
- [IEC 60050 (Electropedia), IEV 815-20-02 « superconductivity »](https://electropedia.org/iev/iev.nsf/IEVref_xref/en:815-20-02) — type `reference`
- [IEC 60050 (Electropedia), IEV 815-20-10 « critical temperature »](https://electropedia.org/iev/iev.nsf/IEVref_xref/en:815-20-10) — type `reference`
- [CEA, Clefs CEA n° 56 (hiver 2007-2008), « RMN, magnétisme et santé »](https://www.cea.fr/multimedia/Documents/publications/clefs-cea/archives/fr/p029_Lethimonier.pdf) — type `reference`

**Fiches liées après** : `bobine-inductance` (nouveau), `champ-magnetique`, `conducteur-electrique`, `courant-continu` (nouveau), `resistance-electrique`, `resistivite`

```
fiche : supraconductivite
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 9. Système binaire — `systeme-binaire`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (29 mots) :
> Numération en base deux n'utilisant que les chiffres zéro et un. C'est la seule représentation directement manipulable par les circuits logiques, dont les composants n'ont que deux états stables.

**Définition — après** (40 mots) :
> Système de numération en base deux, qui n'utilise que les chiffres zéro et un, chacun appelé bit. Les circuits numériques l'emploient parce que ces deux chiffres se représentent facilement par deux états électriques, comme l'absence ou la présence d'un courant.

**Version simple — avant** (17 mots) :
> Au lieu de compter avec dix chiffres, les machines comptent avec deux seulement : zéro et un.

**Version simple — après** (22 mots) :
> Au lieu de compter avec dix chiffres comme nous, un ordinateur ou un téléphone compte avec deux seulement : zéro et un.

**Sources après** (à ouvrir une par une) :
- [Programme d'enseignement de spécialité de numérique et sciences informatiques de première générale (arrêté du 17 janvier 2019, BO spécial n° 1 du 22 janvier 2019), rubrique « Représentation des données : types et valeurs de base »](https://eduscol.education.fr/document/30007/download) — type `programme`
- [Programme d'innovation technologique et d'ingénierie et développement durable de première et d'ingénierie, innovation et développement durable de terminale STI2D (Éduscol), § 2.4.3 « Encodage de l'information : binaire, hexadécimal, ASCII »](https://eduscol.education.fr/document/24916/download) — type `programme`
- [Eric Cariou (Université de Pau et des Pays de l'Adour), cours d'architecture des ordinateurs, « Codage des nombres »](https://lab-sticc.univ-brest.fr/~ecariou/cours/archi/cours-1-codage.pdf) — type `manuel`

**Fiches liées après** : `bit`, `circuit-numerique`, `compteur-numerique`, `octet`, `porte-ou-exclusif`, `signal-numerique`, `systeme-hexadecimal`

```
fiche : systeme-binaire
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 10. Système hexadécimal — `systeme-hexadecimal`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (28 mots) :
> Numération en base seize utilisant les chiffres de zéro à neuf puis les lettres A à F. Elle abrège l'écriture binaire, chaque chiffre hexadécimal représentant exactement quatre bits.

**Définition — après** (39 mots) :
> Système de numération en base seize, qui utilise les chiffres de zéro à neuf puis les lettres A à F. Il permet d'écrire plus brièvement les nombres binaires, car un chiffre hexadécimal correspond à un groupe de quatre bits.

**Version simple — avant** (18 mots) :
> C'est une façon plus courte d'écrire les nombres binaires, en utilisant aussi des lettres de A à F.

**Version simple — après** (31 mots) :
> C'est une façon de compter avec seize symboles : les chiffres de 0 à 9 et les lettres A à F. Sur les sites web, le rouge s'écrit par exemple FF0000.

**Sources après** (à ouvrir une par une) :
- [Programme d'enseignement de spécialité de numérique et sciences informatiques de première générale (arrêté du 17 janvier 2019, BO spécial n° 1 du 22 janvier 2019), rubrique « Représentation des données : types et valeurs de base »](https://eduscol.education.fr/document/30007/download) — type `programme`
- [Programme d'innovation technologique et d'ingénierie et développement durable de première et d'ingénierie, innovation et développement durable de terminale STI2D (Éduscol), § 2.4.3 « Encodage de l'information : binaire, hexadécimal, ASCII »](https://eduscol.education.fr/document/24916/download) — type `programme`
- [Eric Cariou (Université de Pau et des Pays de l'Adour), cours d'architecture des ordinateurs, « Codage des nombres »](https://lab-sticc.univ-brest.fr/~ecariou/cours/archi/cours-1-codage.pdf) — type `manuel`
- [IEC 60050 (Electropedia), IEV 171-02-08 « hexadecimal »](https://electropedia.org/iev/iev.nsf/17127c61f2426ed8c1257cb5003c9bec/b5a1788cabf36dccc1258398005897ff) — type `reference`
- [MDN Web Docs (Mozilla), « Valeurs de couleur », notation hexadécimale](https://developer.mozilla.org/fr/docs/Web/CSS/Guides/Colors/Color_values) — type `reference`

**Fiches liées après** : `bit`, `microcontroleur`, `octet`, `systeme-binaire`

```
fiche : systeme-hexadecimal
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 11. Table de vérité — `table-de-verite`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Version simple — avant** (17 mots) :
> C'est une liste de tous les cas possibles et de la réponse du circuit pour chacun d'eux.

**Version simple — après** (26 mots) :
> C'est un tableau qui donne la réponse d'un circuit dans tous les cas possibles, par exemple si une lampe s'allume pour chaque position de deux interrupteurs.

**Sources après** (à ouvrir une par une) :
- [Programme d'enseignement de spécialité de numérique et sciences informatiques de première générale (arrêté du 17 janvier 2019, BO spécial n° 1 du 22 janvier 2019), « Dresser la table d'une expression booléenne »](https://eduscol.education.fr/document/30007/download) — type `programme`
- [Eric Cariou (Université de Pau et des Pays de l'Adour), cours d'architecture des ordinateurs, « Circuits logiques »](https://lab-sticc.univ-brest.fr/~ecariou/cours/archi/cours-3-circuits-logiques.pdf) — type `manuel`

**Fiches liées après** : `algebre-de-boole`, `circuit-logique`, `porte-et-and`, `porte-logique`, `porte-non-et`, `porte-non-ou`, `porte-ou-exclusif`, `porte-ou-or`

```
fiche : table-de-verite
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 12. Technicien de maintenance — `technicien-de-maintenance`

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

### 13. Théorème de Shannon — `theoreme-de-shannon`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (28 mots) :
> Règle selon laquelle un signal ne peut être reconstruit fidèlement que si la fréquence d'échantillonnage dépasse le double de sa fréquence maximale. En dessous, apparaissent des repliements irréversibles.

**Définition — après** (43 mots) :
> Résultat de théorie du signal selon lequel un signal dont les fréquences ne dépassent pas une valeur maximale peut, en théorie, être reconstitué sans distorsion à partir de ses échantillons si la fréquence d'échantillonnage vaut au moins le double de cette fréquence maximale.

**Version simple — avant** (21 mots) :
> Pour bien enregistrer un son, il faut le mesurer au moins deux fois plus vite que sa note la plus aiguë.

**Version simple — après** (26 mots) :
> Pour bien enregistrer un son, il faut prendre des mesures au moins deux fois plus souvent que ne vibre le son le plus aigu qu'il contient.

**Sources après** (à ouvrir une par une) :
- [IEC 60050 (Electropedia), IEV 723-10-28 « Nyquist frequency »](https://electropedia.org/iev/iev.nsf/17127c61f2426ed8c1257cb5003c9bec/93f14ad8e095fed8c125727c00326887) — type `reference`

**Fiches liées après** : `bande-passante`, `convertisseur-analogique-numerique-can`, `echantillonnage`, `filtre-passe-bas`

```
fiche : theoreme-de-shannon
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 14. Trou électronique — `trou-electronique`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (29 mots) :
> Place laissée vacante par un électron dans un cristal semi-conducteur. Elle se déplace comme une charge positive et participe à la conduction au même titre que les électrons libres.

**Définition — après** (43 mots) :
> Absence d'un électron à une place qu'il occuperait normalement dans un cristal semi-conducteur. Ce manque se comporte comme une particule de charge positive : sous l'effet d'un champ électrique, il se déplace et participe, avec les électrons libres, à la conduction du courant.

**Version simple — avant** (20 mots) :
> Quand un électron part, il laisse un vide. Ce vide se déplace lui aussi, comme s'il était une charge positive.

**Version simple — après** (29 mots) :
> Quand un électron quitte sa place, il laisse un vide qui se déplace comme une charge positive, comme une place libre qui recule dans une file quand chacun avance.

**Sources après** (à ouvrir une par une) :
- [Office québécois de la langue française, Grand dictionnaire terminologique, fiche « trou »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8876557/trou) — type `reference`
- [IEC 60050 (Electropedia), IEV 521-02-18 « hole conduction »](https://electropedia.org/iev/iev.nsf/17127c61f2426ed8c1257cb5003c9bec/9bc89e2a00a16302c125727c0031203d) — type `reference`
- [IEC 60050 (Electropedia), IEV 521-02-23 « valence band »](https://electropedia.org/iev/iev.nsf/17127c61f2426ed8c1257cb5003c9bec/89d8a20d854a02d1c125727c00312072) — type `reference`

**Fiches liées après** : `champ-electrique` (nouveau), `charge-electrique`, `dopage`, `electron`, `jonction-pn`, `semi-conducteur`

```
fiche : trou-electronique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 15. Mix énergétique — `mix-energetique`

- Niveau scolaire : STI2D (cycles STI2D)
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (24 mots) :
> Répartition des différentes sources utilisées pour produire l'électricité d'un territoire. Il détermine le coût, la disponibilité et le contenu carbone de chaque kilowattheure consommé.

**Définition — après** (44 mots) :
> Répartition, souvent exprimée en pourcentages, des différentes sources d'énergie, comme le pétrole, le gaz, le charbon, le nucléaire ou les énergies renouvelables, consommées dans un territoire pour couvrir ses besoins. Le mix électrique, plus restreint, ne décrit que les sources utilisées pour produire l'électricité.

**Version simple — avant** (16 mots) :
> C'est la part de chaque source — nucléaire, éolien, solaire, gaz — dans l'électricité d'un pays.

**Version simple — après** (30 mots) :
> C'est la part de chaque source d'énergie dans tout ce qu'un pays consomme : le pétrole des carburants pour les voitures, le gaz, le nucléaire, le vent ou le soleil.

**Synonymes** : bouquet energetique, mix electrique, mix energetique → **bouquet energetique, mix energetique, portefeuille energetique**

**Sources après** (à ouvrir une par une) :
- [Programme d'innovation technologique et d'ingénierie et développement durable de première et d'ingénierie, innovation et développement durable de terminale STI2D (Éduscol), § 4.3.1 « mix énergétique approprié »](https://eduscol.education.fr/document/24916/download) — type `programme`
- [Office québécois de la langue française, Grand dictionnaire terminologique, fiche « bouquet énergétique »](https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26559068/bouquet-energetique) — type `reference`
- [Connaissance des Énergies, fiche pédagogique « Mix énergétique de la France » (mise à jour du 18 septembre 2024)](https://www.connaissancedesenergies.org/fiche-pedagogique/mix-energetique-de-la-france) — type `reference`

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

### 16. Stockage d'énergie — `stockage-d-energie`

- Niveau scolaire : 1-TG (cycles 1-TG)
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (28 mots) :
> Ensemble des techniques permettant de conserver de l'énergie électrique pour la restituer plus tard. Batteries, stations de pompage et hydrogène compensent le décalage entre production renouvelable et consommation.

**Définition — après** (38 mots) :
> Ensemble des techniques qui mettent de l'énergie en réserve, sous forme chimique, électrique, mécanique ou thermique, pour la restituer plus tard. Batteries, stations de pompage et hydrogène aident à compenser les variations de la production solaire et éolienne.

**Version simple — avant** (23 mots) :
> L'électricité se garde mal. On la transforme donc en autre chose, comme de l'eau montée dans un lac, pour la réutiliser plus tard.

**Version simple — après** (29 mots) :
> Pour garder de l'énergie et s'en servir plus tard, on la met en réserve, par exemple dans la batterie d'un téléphone ou en remontant de l'eau dans un lac.

**Sources après** (à ouvrir une par une) :
- [Programme de sciences de l'ingénieur de première et terminale générales (Éduscol), « Stockage de l'énergie »](https://eduscol.education.fr/document/22492/download) — type `programme`
- [Programme d'innovation technologique et d'ingénierie et développement durable de première et d'ingénierie, innovation et développement durable de terminale STI2D (Éduscol), § 2.3.2 « Types d'énergie stockée : chimique, électrique, mécanique, thermique »](https://eduscol.education.fr/document/24916/download) — type `programme`
- [RTE, Bases de l'électricité — « Stocker l'électricité à grande échelle »](https://www.rte-france.com/bases-electricite/systeme-electrique/stocker-electricite-grande-echelle) — type `reference`

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
