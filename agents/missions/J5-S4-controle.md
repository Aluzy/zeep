---
lot: J5-S4
role: controle
date: 2026-10-01
changeset: agents/changesets/J5-S4.jsonl
elements: ["arc-electrique", "consignation-electrique", "controleur-d-isolement", "courant-de-fuite", "defaut-d-isolement", "electrisation", "habilitation-electrique", "disjoncteur-differentiel"]
---

# Contrôle du lot J5-S4

8 fiche(s), 30 opération(s) du rédacteur (changeset non encore appliqué).

## Consignes du contrôleur

Tu es le **contrôleur** du lot J5-S4. Tu n'as pas participé à la rédaction et tu ne la vois qu'à
travers ce document : les justifications du rédacteur sont volontairement absentes. Tu vérifies
chaque fiche contre les **12 critères** de `docs/grille-relecture.md` (lis-la en entier d'abord).

1. **Ouvre chaque URL de source** et vérifie qu'elle appuie la définition. Une source que tu ne
   peux pas ouvrir, imprécise (page d'accueil) ou qui n'appuie pas l'affirmation = critère 8 en échec.
2. Une fiche est **conforme** si les 12 critères passent. Dans `agents/changesets/J5-S4-controle.jsonl`, remplace alors
   `"__A_REMPLIR__"` de `new` par
   `{"date": "2026-10-01", "par": "agent-controleur-J5-S4", "statut": "relu-ia"}` et `why` par
   « Relue selon la grille (12 critères) ».
3. Une fiche **refusée** : supprime sa ligne dans `agents/changesets/J5-S4-controle.jsonl`, et note les critères en échec. Tu ne
   réécris pas la fiche : le rédacteur la corrige (nouvelle passe de contrôle) ou la retire du lot.
   Si le défaut porte sur une fiche hors lot, ajoute-la à `agents/donnees/signalements.json`.
4. Écris tes verdicts dans la section « Relecture (rempli par le contrôleur) » de
   `agents/rapports/J5-S4.md`, une ligne par fiche : critères en échec, décision.
5. Vérifie : `python3 scripts/apply_changeset.py agents/changesets/J5-S4.jsonl agents/changesets/J5-S4-controle.jsonl --dry-run`.
   Tu ne poses **jamais** `"statut": "valide"` (réservé à Alexandre).


## Fiches à contrôler

### 1. Arc électrique — `arc-electrique`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (30 mots) :
> Décharge lumineuse et très chaude entre deux conducteurs séparés par un isolant devenu conducteur. Il provoque brûlures et incendies, et impose des équipements de protection lors des manœuvres sous charge.

**Définition — après** (35 mots) :
> Décharge électrique entre deux conducteurs, susceptible d'apparaître quand on ouvre ou ferme un circuit, ou lors d'un court-circuit. Elle peut provoquer des brûlures et déclencher un incendie. Seule une personne habilitée intervient sur une installation.

**Version simple — avant** (23 mots) :
> Quand le courant saute d'un fil à l'autre, il crée un éclair très chaud capable de brûler gravement et de déclencher un incendie.

**Version simple — après** (29 mots) :
> Quand on débranche un appareil et qu'une étincelle apparaît, c'est un petit arc électrique. Un arc plus fort peut brûler ou provoquer un incendie : seul un électricien intervient.

**Sources après** (à ouvrir une par une) :
- [INRS — Risques liés à l'électricité](https://www.inrs.fr/risques/electriques/risques-electricite.html) — type `reference`
- [INRS — Accidents d'origine électrique](https://www.inrs.fr/risques/electriques/accidents-origine-electrique.html) — type `reference`

**Fiches liées après** : `court-circuit`, `disjoncteur`, `fusible`, `habilitation-electrique`, `sectionneur`

```
fiche : arc-electrique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 2. Consignation électrique — `consignation-electrique`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (29 mots) :
> Procédure en quatre temps — séparer, condamner, vérifier l'absence de tension, mettre à la terre — qui garantit qu'une installation ne peut être remise sous tension pendant une intervention.

**Définition — après** (51 mots) :
> Procédure décrite par la norme NF C 18-510 qui précède un travail hors tension : séparer l'installation de toute source d'énergie électrique, condamner les organes de séparation ouverts, identifier la partie concernée, vérifier l'absence de tension, puis mettre à la terre et en court-circuit. Elle est confiée à une personne habilitée.

**Version simple — avant** (23 mots) :
> Avant de travailler, on coupe le courant, on empêche qu'il soit rallumé par erreur, et on vérifie qu'il n'y en a vraiment plus.

**Version simple — après** (33 mots) :
> Avant de réparer l'installation d'une maison, un électricien coupe l'alimentation, bloque l'interrupteur ouvert pour que personne ne le rallume, puis vérifie qu'il n'y a plus de tension. On ne le fait pas soi-même.

**Sources après** (à ouvrir une par une) :
- [INRS — Prévention du risque électrique](https://www.inrs.fr/risques/electriques/prevention-risque-electrique.html) — type `reference`

**Fiches liées après** : `court-circuit` (nouveau), `electricien`, `habilitation-electrique`, `mise-a-la-terre`, `sectionneur`, `tableau-electrique`, `technicien-de-maintenance`

```
fiche : consignation-electrique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 3. Contrôleur d'isolement — `controleur-d-isolement`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (28 mots) :
> Appareil qui applique une tension continue élevée entre conducteurs et terre pour mesurer la résistance d'isolement. Un résultat trop faible signale un câble ou une machine à remplacer.

**Définition — après** (46 mots) :
> Appareil qui applique une tension continue de valeur connue entre deux éléments conducteurs, par exemple un conducteur et la terre, puis mesure le courant pour en déduire la résistance d'isolement, qui indique la qualité de l'isolation. Une valeur qui baisse nettement est un problème à rechercher.

**Version simple — avant** (17 mots) :
> Cet appareil vérifie que les gaines des fils isolent encore correctement, avant qu'un défaut ne devienne dangereux.

**Version simple — après** (30 mots) :
> Cet appareil vérifie que les gaines des fils isolent encore bien. Un électricien s'en sert, par exemple, pour contrôler les câbles d'un vieux tableau avant qu'un défaut ne devienne dangereux.

**Sources après** (à ouvrir une par une) :
- [Éduscol STI — Guide de la mesure d'isolement](https://sti.eduscol.education.fr/sites/eduscol.education.fr.sti/files/ressources/techniques/2537/2537-guide-de-la-mesure-disolement.pdf) — type `reference`

**Fiches liées après** : `courant-continu` (nouveau), `courant-de-fuite` (nouveau), `defaut-d-isolement`, `electricien`, `installation-electrique`, `isolant-electrique`, `resistance-electrique`

```
fiche : controleur-d-isolement
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 4. Courant de fuite — `courant-de-fuite`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (28 mots) :
> Courant qui quitte le circuit prévu pour rejoindre la terre à travers un défaut d'isolement ou les filtres d'un appareil. Au-delà d'un seuil, il déclenche le dispositif différentiel.

**Définition — après** (42 mots) :
> Courant qui circule de façon anormale entre un circuit et les masses métalliques ou la terre, à cause d'un défaut d'isolement, c'est-à-dire d'un isolant dégradé. Plus la résistance d'isolement est faible, plus le risque de voir circuler de tels courants est grand.

**Version simple — avant** (20 mots) :
> Une petite partie du courant peut s'échapper par un fil abîmé. Un appareil de protection le repère et coupe tout.

**Version simple — après** (30 mots) :
> Quand la gaine d'un fil de lampe est abîmée, un peu de courant peut s'échapper vers la carcasse de l'appareil. Ce n'est pas sans danger : on appelle un électricien.

**Sources après** (à ouvrir une par une) :
- [INRS — Accidents d'origine électrique](https://www.inrs.fr/risques/electriques/accidents-origine-electrique.html) — type `reference`
- [Éduscol STI — Guide de la mesure d'isolement](https://sti.eduscol.education.fr/sites/eduscol.education.fr.sti/files/ressources/techniques/2537/2537-guide-de-la-mesure-disolement.pdf) — type `reference`

**Fiches liées après** : `controleur-d-isolement` (nouveau), `defaut-d-isolement`, `disjoncteur-differentiel`, `isolant-electrique`, `mise-a-la-terre`

```
fiche : courant-de-fuite
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 5. Défaut d'isolement — `defaut-d-isolement`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (30 mots) :
> Dégradation de l'isolant séparant un conducteur actif des masses métalliques ou de la terre. Il met les carcasses sous tension et constitue la première cause d'électrisation dans les installations vieillissantes.

**Définition — après** (45 mots) :
> Dégradation de l'isolant qui sépare un conducteur actif des masses métalliques ou de la terre. Elle provoque une circulation anormale de courant vers la masse ou la terre et peut mettre une carcasse sous tension, d'où un risque d'électrisation au contact de cette pièce métallique.

**Version simple — avant** (19 mots) :
> Quand la gaine d'un fil est abîmée, l'électricité peut atteindre la carcasse d'un appareil et devenir dangereuse au toucher.

**Version simple — après** (27 mots) :
> Si le fil d'un grille-pain est abîmé, le courant peut atteindre sa carcasse métallique et devenir dangereux au toucher. On le débranche et on appelle un électricien.

**Sources après** (à ouvrir une par une) :
- [INRS — Accidents d'origine électrique](https://www.inrs.fr/risques/electriques/accidents-origine-electrique.html) — type `reference`
- [INRS — Risques liés à l'électricité](https://www.inrs.fr/risques/electriques/risques-electricite.html) — type `reference`

**Fiches liées après** : `controleur-d-isolement`, `courant-de-fuite`, `disjoncteur-differentiel`, `isolant-electrique`, `mise-a-la-terre`, `prise-de-terre`, `regime-de-neutre`

```
fiche : defaut-d-isolement
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 6. Électrisation — `electrisation`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (29 mots) :
> Passage d'un courant électrique à travers le corps humain, provoquant brûlures, contractions musculaires ou troubles cardiaques. Sa gravité dépend de l'intensité, du trajet et de la durée du contact.

**Définition — après** (54 mots) :
> Passage d'un courant électrique à travers le corps humain, qui provoque des blessures plus ou moins graves : contraction involontaire des muscles (tétanisation) ou fibrillation ventriculaire, c'est-à-dire battements désordonnés du cœur pouvant conduire à son arrêt. La gravité dépend de l'intensité du courant et de son trajet. Sur une installation, seul un électricien intervient.

**Version simple — avant** (21 mots) :
> C'est ce qui arrive quand le courant traverse le corps. Même une faible quantité peut faire très mal et devenir dangereuse.

**Version simple — après** (29 mots) :
> Si l'on touche un fil abîmé d'un appareil branché, le courant peut traverser le corps : c'est l'électrisation. C'est dangereux, alors on prévient un adulte au lieu d'y toucher.

**Sources après** (à ouvrir une par une) :
- [INRS — Accidents d'origine électrique](https://www.inrs.fr/risques/electriques/accidents-origine-electrique.html) — type `reference`
- [INRS — Risques liés à l'électricité](https://www.inrs.fr/risques/electriques/risques-electricite.html) — type `reference`

**Fiches liées après** : `courant-electrique`, `disjoncteur-differentiel`, `electrocution`, `habilitation-electrique`, `mise-a-la-terre`, `phase-electrique`, `tres-basse-tension-de-securite`

```
fiche : electrisation
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 7. Habilitation électrique — `habilitation-electrique`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (31 mots) :
> Reconnaissance par l'employeur de la capacité d'une personne à effectuer en sécurité des travaux d'ordre électrique. Elle repose sur une formation, un avis médical et un symbole précisant les opérations autorisées.

**Définition — après** (34 mots) :
> Reconnaissance par l'employeur de la capacité d'une personne à effectuer en sécurité des travaux d'ordre électrique. Elle repose sur une formation, la vérification des aptitudes, notamment médicales, et des symboles précisant les opérations autorisées.

**Version simple — avant** (19 mots) :
> Pour travailler sur des installations électriques, il faut avoir été formé et reconnu capable de le faire sans danger.

**Version simple — après** (22 mots) :
> Comme un permis de conduire, l'habilitation montre qu'un salarié a été formé et que son employeur l'autorise à faire certains travaux électriques.

**Sources après** (à ouvrir une par une) :
- [INRS — Journées techniques Électricité : la démarche d'habilitation](https://inrs.fr/dam/jcr:685bc917-afe0-4c3e-8c86-4bc78b334ea4/JT%20Elec%20-%2009%20Lombard%20Demarche%20habilitation.pdf) — type `reference`
- [INRS — Prévention du risque électrique](https://www.inrs.fr/risques/electriques/prevention-risque-electrique.html) — type `reference`

**Fiches liées après** : `arc-electrique`, `consignation-electrique`, `electricien`, `electrisation`, `electrocution`, `installation-electrique`, `norme-electrique-nf-c-15-100`, `sectionneur`, `technicien-de-maintenance`

```
fiche : habilitation-electrique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 8. Disjoncteur différentiel — `disjoncteur-differentiel`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (31 mots) :
> Appareil qui compare le courant entrant et le courant sortant d'un circuit et coupe dès qu'un écart apparaît. Un modèle 30 milliampères protège les personnes contre les contacts directs et indirects.

**Définition — après** (60 mots) :
> Appareil qui surveille la somme des courants de la phase et du neutre d'un circuit, nulle en temps normal, et coupe quand une fuite atteint sa sensibilité, par exemple 30 mA. Il protège aussi contre surcharges et courts-circuits. Le modèle 30 mA complète seulement la protection contre le contact avec une partie sous tension ; son installation relève d'un électricien.

**Version simple — avant** (19 mots) :
> Cet appareil surveille si un peu d'électricité s'échappe du circuit, par exemple à travers une personne, et coupe aussitôt.

**Version simple — après** (31 mots) :
> Dans le tableau électrique de la maison, cet appareil coupe le courant quand un peu de courant s'échappe, par exemple par un fil abîmé. Seul un électricien l'installe ou le change.

**Synonymes** : DDR, differentiel 30 mA, disjoncteur differentiel, interrupteur differentiel → **DDR, differentiel 30 mA, disjoncteur differentiel**

**Sources après** (à ouvrir une par une) :
- [Éduscol STI — La protection différentielle dans les installations électriques basse tension](https://sti.eduscol.education.fr/sites/eduscol.education.fr.sti/files/ressources/techniques/680/680-gt-differentiel.pdf) — type `reference`
- [INRS — Risques électriques : glossaire (contact direct, contact indirect)](https://www.inrs.fr/risques/electriques/glossaire.html) — type `reference`

**Fiches liées après** : `courant-de-fuite`, `court-circuit` (nouveau), `defaut-d-isolement`, `disjoncteur`, `electrisation`, `electrocution`, `mise-a-la-terre`, `phase-electrique` (nouveau), `regime-de-neutre`, `tableau-electrique`

```
fiche : disjoncteur-differentiel
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```
