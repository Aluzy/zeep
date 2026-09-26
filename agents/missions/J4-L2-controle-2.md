---
lot: J4-L2
role: controle
date: 2026-09-25
changeset: agents/changesets/J4-L2.jsonl
elements: ["consommation-electrique", "court-circuit", "electrocution", "fiche-electrique", "harmoniques", "impedance", "modulation"]
---

# Contrôle du lot J4-L2 — passe 2

7 fiche(s), 89 opération(s) du rédacteur (changeset non encore appliqué).

## Consignes du contrôleur

Tu es le **contrôleur** du lot J4-L2. Tu n'as pas participé à la rédaction et tu ne la vois qu'à
travers ce document : les justifications du rédacteur sont volontairement absentes. Tu vérifies
chaque fiche contre les **12 critères** de `docs/grille-relecture.md` (lis-la en entier d'abord).

1. **Ouvre chaque URL de source** et vérifie qu'elle appuie la définition. Une source que tu ne
   peux pas ouvrir, imprécise (page d'accueil) ou qui n'appuie pas l'affirmation = critère 8 en échec.
2. Une fiche est **conforme** si les 12 critères passent. Dans `agents/changesets/J4-L2-controle.jsonl`, remplace alors
   `"__A_REMPLIR__"` de `new` par
   `{"date": "2026-09-25", "par": "agent-controleur-J4-L2", "statut": "relu-ia"}` et `why` par
   « Relue selon la grille (12 critères) ».
3. Une fiche **refusée** : supprime sa ligne dans `agents/changesets/J4-L2-controle.jsonl`, et note les critères en échec. Tu ne
   réécris pas la fiche : le rédacteur la corrige (nouvelle passe de contrôle) ou la retire du lot.
   Si le défaut porte sur une fiche hors lot, ajoute-la à `agents/donnees/signalements.json`.
4. Écris tes verdicts dans la section « Relecture (rempli par le contrôleur) » de
   `agents/rapports/J4-L2.md`, une ligne par fiche : critères en échec, décision.
5. Vérifie : `python3 scripts/apply_changeset.py agents/changesets/J4-L2.jsonl agents/changesets/J4-L2-controle.jsonl --dry-run`.
   Tu ne poses **jamais** `"statut": "valide"` (réservé à Alexandre).


## Fiches à contrôler

### 1. Consommation électrique — `consommation-electrique`

- Niveau scolaire : 2GT (cycles 2GT)
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (19 mots) :
> Quantité d'énergie électrique utilisée par un appareil, un logement ou une entreprise, mesurée par le compteur électrique en kilowattheures.

**Définition — après** (54 mots) :
> Quantité d'énergie électrique utilisée par un appareil, un foyer ou une entreprise pendant une durée donnée, exprimée en kilowattheures. Pour une habitation, elle se lit sur le compteur électrique : la différence entre deux index relevés donne l'énergie consommée entre ces deux dates. Elle ne se confond pas avec la puissance, exprimée en watts.

**Version simple — avant** (0 mots) :
_(vide)_

**Version simple — après** (26 mots) :
> La consommation électrique, c'est la quantité d'énergie électrique utilisée. Plus un appareil fonctionne longtemps, plus il consomme : un radiateur allumé toute la nuit consomme beaucoup.

**Synonymes** : — → **consommation d'électricité**

**Sources après** (à ouvrir une par une) :
- [Programme du cycle 4 en vigueur à la rentrée 2020 (d'après le BOEN n° 31 du 30 juillet 2020), p. 103 : « Conduire un calcul de consommation d'énergie électrique relatif à une situation de la vie courante »](https://eduscol.education.gouv.fr/sites/default/files/document/programme-d-enseignement-du-cycle-4-67722.pdf#page=103) — type `programme`
- [Enedis, FAQ « Comment lire l'index du compteur électrique ? »](https://www.enedis.fr/faq/compteur-electrique/comment-lire-lindex-du-compteur-electrique) — type `reference`
- [Dictionnaire de français Larousse, article « consommation »](https://www.larousse.fr/dictionnaires/francais/consommation/18427) — type `reference`

**Fiches liées après** : `ampoule-led`, `compteur-electrique`, `compteur-linky`, `delestage`, `economie-d-energie`, `energie-electrique`, `facture-d-electricite`, `heures-creuses`, `kilowattheure` (nouveau), `puissance-electrique` (nouveau), `reseau-intelligent-smart-grid`, `watt` (nouveau)

```
fiche : consommation-electrique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 2. Court-circuit — `court-circuit`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (48 mots) :
> <strong>Vu côté électricité :</strong> Contact accidentel entre deux conducteurs électriques de potentiels différents, provoquant une intensité électrique excessive pouvant déclencher un disjoncteur ou un fusible.<br><br><strong>Vu côté électronique :</strong> Contact accidentel entre deux points d'un circuit électronique de potentiels différents, provoquant un courant excessif pouvant endommager les composants électroniques.

**Définition — après** (57 mots) :
> Liaison accidentelle, de résistance presque nulle, entre deux points d'un circuit entre lesquels existe normalement une tension, par exemple les deux bornes d'une pile ou deux conducteurs d'un câble abîmé. L'intensité devient très grande et peut provoquer échauffement ou incendie ; fusibles et disjoncteurs coupent alors le circuit. Un câble abîmé se fait remplacer par un électricien.

**Sources après** (à ouvrir une par une) :
- [INRS, dossier Risques électriques, « Prévention du risque électrique » (surintensités, mise à la terre des masses, NF C 15-100)](https://www.inrs.fr/risques/electriques/prevention-risque-electrique.html) — type `reference`
- [Dictionnaire de français Larousse, article « court-circuit »](https://www.larousse.fr/dictionnaires/francais/court-circuit/19961) — type `reference`

**Fiches liées après** : `arc-electrique`, `cable-electrique` (nouveau), `circuit-electrique` (nouveau), `court-jus`, `disjoncteur`, `electricien` (nouveau), `electronique`, `fusible`, `intensite-electrique`, `pile-electrique` (nouveau), `resistance-electrique` (nouveau), `tension-electrique` (nouveau)

```
fiche : court-circuit
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 3. Électrocution — `electrocution`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (28 mots) :
> Électrisation entraînant la mort de la personne. Le risque devient majeur dès quelques dizaines de milliampères traversant la cage thoracique, bien en deçà du courant d'un appareil ménager.

**Définition — après** (47 mots) :
> Électrisation qui entraîne la mort de la personne traversée par le courant électrique. Un courant alternatif de quelques dizaines de milliampères passant par le cœur pendant une seconde peut suffire, bien moins que celui d'un appareil ménager : toute tension supérieure à 50 V est potentiellement mortelle.

**Version simple — avant** (17 mots) :
> C'est une électrisation qui tue. Il faut beaucoup moins d'électricité qu'on ne l'imagine pour que cela arrive.

**Version simple — après** (31 mots) :
> L'électrocution, c'est quand le courant traverse le corps et tue. Un courant plus faible que celui d'une petite lampe suffit : on ne touche jamais une prise ni un fil abîmé.

**Sources après** (à ouvrir une par une) :
- [INRS, dossier Risques électriques, « Accidents d'origine électrique » (électrisation, électrocution, effets du courant)](https://www.inrs.fr/risques/electriques/accidents-origine-electrique.html) — type `reference`
- [INRS, brochure ED 6344 « Électricité : 10 règles élémentaires de sécurité » (2019), p. 4 : 230 V aux prises des particuliers, tensions au-delà de 50 V potentiellement mortelles](https://www.inrs.fr/dam/inrs/CataloguePapier/ED/TI-ED-6344.pdf#page=4) — type `reference`
- [Dictionnaire de français Larousse, article « électrocution »](https://www.larousse.fr/dictionnaires/francais/%C3%A9lectrocution_n_f_/28237) — type `reference`
- [INRS, dossier Risques électriques, « Principes généraux sur l'électricité » (courant de 65 mA dans une lampe de 15 W sous 230 V)](https://www.inrs.fr/risques/electriques/principes-generaux-electricite.html) — type `reference`

**Fiches liées après** : `courant-alternatif` (nouveau), `courant-electrique`, `disjoncteur-differentiel`, `electrisation`, `habilitation-electrique`, `mise-a-la-terre`, `tension-electrique` (nouveau)

```
fiche : electrocution
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 4. Fiche électrique — `fiche-electrique`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (18 mots) :
> Élément mobile équipé de broches, connecté à un appareil, destiné à être inséré dans une prise de courant.

**Définition — après** (54 mots) :
> Partie mâle d'un raccordement, fixée au bout du cordon d'un appareil, dont les broches s'enfoncent dans une prise de courant pour l'alimenter. Pour débrancher, on tire sur la fiche et non sur le câble ; une fiche cassée se fait remplacer par un professionnel, avec un modèle normalisé, et ne se bricole jamais soi-même.

**Synonymes** : — → **prise mâle**

**Sources après** (à ouvrir une par une) :
- [INRS, brochure ED 6344 « Électricité : 10 règles élémentaires de sécurité » (2019), p. 6 : « Ne pas bricoler » : l'électricien est un professionnel qualifié ; fiche cassée à faire remplacer](https://www.inrs.fr/dam/inrs/CataloguePapier/ED/TI-ED-6344.pdf#page=6) — type `reference`
- [INRS, brochure ED 6344 « Électricité : 10 règles élémentaires de sécurité » (2019), p. 8 : « Ne pas tirer sur le câble d'alimentation […] mais sur sa fiche d'alimentation »](https://www.inrs.fr/dam/inrs/CataloguePapier/ED/TI-ED-6344.pdf#page=8) — type `reference`

**Fiches liées après** : `cable-electrique` (nouveau), `connecteur-electrique`, `prise-de-courant`

```
fiche : fiche-electrique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 5. Harmoniques — `harmoniques`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (31 mots) :
> Composantes d'un signal dont les fréquences sont des multiples de la fréquence fondamentale. Injectées par les appareils à découpage, elles déforment la tension du réseau et échauffent les conducteurs de neutre.

**Définition — après** (45 mots) :
> Composantes d'une tension ou d'un courant périodique dont les fréquences sont des multiples entiers de la fréquence fondamentale, celle du réseau électrique. Leur présence déforme la courbe sinusoïdale de la tension ; leur mesure sur une installation sous tension est réservée à un professionnel qualifié.

**Version simple — avant** (21 mots) :
> Certains appareils renvoient dans les fils des signaux parasites plus rapides que le courant normal. Ils abîment la qualité de l'électricité.

**Version simple — après** (25 mots) :
> Sur le réseau, la tension devrait suivre une courbe bien régulière. Certains appareils la déforment en y ajoutant de petites ondes plus serrées, appelées harmoniques.

**Sources après** (à ouvrir une par une) :
- [Dictionnaire de français Larousse, article « harmonique »](https://www.larousse.fr/dictionnaires/francais/harmonique/39116) — type `reference`

**Fiches liées après** : `alimentation-a-decoupage`, `analyseur-de-spectre`, `compatibilite-electromagnetique-cem`, `courant-alternatif`, `distorsion`, `filtre-electronique`, `frequence-electrique` (nouveau), `neutre`, `tension-electrique` (nouveau)

```
fiche : harmoniques
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 6. Impédance — `impedance`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (17 mots) :
> Grandeur qui caractérise l'opposition d'un circuit électronique au passage d'un signal analogique, combinant résistance, condensateur et bobine.

**Définition — après** (48 mots) :
> Grandeur qui caractérise l'opposition d'un dipôle au passage d'un courant alternatif : en régime sinusoïdal, c'est le rapport de l'amplitude de la tension à ses bornes à celle du courant qui le traverse. Exprimée en ohms, elle combine la résistance et la réactance, qui dépend de la fréquence.

**Sources après** (à ouvrir une par une) :
- [Dictionnaire de français Larousse, article « impédance »](https://www.larousse.fr/dictionnaires/francais/imp%C3%A9dance/41833) — type `reference`

**Fiches liées après** : `bobine-inductance`, `condensateur`, `courant-alternatif` (nouveau), `dephasage`, `dipole` (nouveau), `electronique`, `frequence-electrique` (nouveau), `haut-parleur`, `henry`, `ohm` (nouveau), `reactance`, `resistance`, `resistance-electrique` (nouveau), `signal-analogique`, `tension-electrique` (nouveau), `valeur-crete` (nouveau)

```
fiche : impedance
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 7. Modulation — `modulation`

- Niveau scolaire : TG (cycles TG)
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (27 mots) :
> Technique consistant à faire varier une caractéristique d'un signal, souvent porté par une fréquence de commutation, pour y transmettre une information, utilisée notamment par un émetteur radiofréquence.

**Définition — après** (54 mots) :
> Technique de transmission qui consiste à modifier l'amplitude, la fréquence ou la phase d'une onde porteuse, un signal sinusoïdal de fréquence élevée, en fonction du message à envoyer, comme la voix ou des données. Chaque émetteur peut ainsi utiliser sa propre gamme de fréquences, à la manière des stations de radio AM ou FM.

**Sources après** (à ouvrir une par une) :
- [Dictionnaire de français Larousse, article « modulation »](https://www.larousse.fr/dictionnaires/francais/modulation/51977) — type `reference`

**Fiches liées après** : `dephasage` (nouveau), `emetteur-radiofrequence`, `frequence-electrique` (nouveau), `signal-analogique` (nouveau), `valeur-crete` (nouveau)

```
fiche : modulation
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```
