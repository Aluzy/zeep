---
lot: J5-S4
role: controle
date: 2026-10-01
changeset: agents/changesets/J5-S4.jsonl
elements: ["controleur-d-isolement", "courant-de-fuite", "defaut-d-isolement", "electrisation", "disjoncteur-differentiel"]
---

# Contrôle du lot J5-S4 — passe 3

5 fiche(s), 41 opération(s) du rédacteur (changeset non encore appliqué).

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

### 1. Contrôleur d'isolement — `controleur-d-isolement`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (28 mots) :
> Appareil qui applique une tension continue élevée entre conducteurs et terre pour mesurer la résistance d'isolement. Un résultat trop faible signale un câble ou une machine à remplacer.

**Définition — après** (52 mots) :
> Appareil qui applique une tension continue connue, par exemple 500 V pour une installation en 230 V, entre deux éléments conducteurs, puis mesure le courant pour en déduire la résistance d'isolement, signe de la qualité de l'isolation. Réservé à un professionnel, le test se fait sur une installation hors tension et déconnectée.

**Version simple — avant** (17 mots) :
> Cet appareil vérifie que les gaines des fils isolent encore correctement, avant qu'un défaut ne devienne dangereux.

**Version simple — après** (30 mots) :
> Cet appareil vérifie que les gaines des fils isolent encore bien. Un électricien s'en sert, par exemple, pour contrôler les câbles d'un vieux tableau avant qu'un défaut ne devienne dangereux.

**Sources après** (à ouvrir une par une) :
- [Guide de la mesure d'isolement, Chauvin Arnoux (2010), hébergé par Éduscol STI](https://sti.eduscol.education.fr/sites/eduscol.education.fr.sti/files/ressources/techniques/2537/2537-guide-de-la-mesure-disolement.pdf) — type `reference`

**Fiches liées après** : `courant-continu` (nouveau), `courant-de-fuite` (nouveau), `defaut-d-isolement`, `electricien`, `installation-electrique`, `isolant-electrique`, `resistance-electrique`, `tension-electrique` (nouveau)

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

### 2. Courant de fuite — `courant-de-fuite`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (28 mots) :
> Courant qui quitte le circuit prévu pour rejoindre la terre à travers un défaut d'isolement ou les filtres d'un appareil. Au-delà d'un seuil, il déclenche le dispositif différentiel.

**Définition — après** (51 mots) :
> Courant qui traverse l'isolant d'un circuit pour rejoindre les masses métalliques ou la terre. Faible et stable avec un isolant en bon état, il augmente quand l'isolant se dégrade et devient anormal en cas de défaut d'isolement. Un courant de fuite élevé est dangereux : seul un électricien intervient sur l'installation.

**Version simple — avant** (20 mots) :
> Une petite partie du courant peut s'échapper par un fil abîmé. Un appareil de protection le repère et coupe tout.

**Version simple — après** (34 mots) :
> Même en bon état, la gaine d'un fil de lampe laisse passer un tout petit courant. Si elle s'abîme, cette fuite grandit et devient dangereuse : on n'y touche pas, on prévient un adulte.

**Sources après** (à ouvrir une par une) :
- [INRS — Accidents d'origine électrique](https://www.inrs.fr/risques/electriques/accidents-origine-electrique.html) — type `reference`
- [Guide de la mesure d'isolement, Chauvin Arnoux (2010), hébergé par Éduscol STI](https://sti.eduscol.education.fr/sites/eduscol.education.fr.sti/files/ressources/techniques/2537/2537-guide-de-la-mesure-disolement.pdf) — type `reference`

**Fiches liées après** : `circuit-electrique` (nouveau), `controleur-d-isolement` (nouveau), `defaut-d-isolement`, `disjoncteur-differentiel`, `electricien` (nouveau), `isolant-electrique`, `mise-a-la-terre`

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

### 3. Défaut d'isolement — `defaut-d-isolement`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (30 mots) :
> Dégradation de l'isolant séparant un conducteur actif des masses métalliques ou de la terre. Il met les carcasses sous tension et constitue la première cause d'électrisation dans les installations vieillissantes.

**Définition — après** (53 mots) :
> Dégradation de l'isolant qui sépare un conducteur actif des masses métalliques ou de la terre. Elle provoque une circulation anormale de courant vers la masse ou la terre et peut mettre une carcasse sous tension, d'où un risque d'électrisation au contact de cette pièce métallique. Seul un électricien recherche et répare ce défaut.

**Version simple — avant** (19 mots) :
> Quand la gaine d'un fil est abîmée, l'électricité peut atteindre la carcasse d'un appareil et devenir dangereuse au toucher.

**Version simple — après** (28 mots) :
> Si le fil d'un grille-pain est abîmé, le courant peut atteindre sa carcasse métallique et devenir dangereux au toucher. On n'y touche pas et on prévient un adulte.

**Sources après** (à ouvrir une par une) :
- [INRS — Accidents d'origine électrique](https://www.inrs.fr/risques/electriques/accidents-origine-electrique.html) — type `reference`
- [INRS — Risques liés à l'électricité](https://www.inrs.fr/risques/electriques/risques-electricite.html) — type `reference`

**Fiches liées après** : `controleur-d-isolement`, `courant-de-fuite`, `disjoncteur-differentiel`, `electricien` (nouveau), `electrisation` (nouveau), `isolant-electrique`, `mise-a-la-terre`, `prise-de-terre`, `regime-de-neutre`, `tension-electrique` (nouveau)

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

### 4. Électrisation — `electrisation`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (29 mots) :
> Passage d'un courant électrique à travers le corps humain, provoquant brûlures, contractions musculaires ou troubles cardiaques. Sa gravité dépend de l'intensité, du trajet et de la durée du contact.

**Définition — après** (60 mots) :
> Passage d'un courant électrique à travers le corps humain, qui provoque des blessures plus ou moins graves, notamment une tétanisation (contraction involontaire des muscles) ou une fibrillation ventriculaire, battements désordonnés du cœur pouvant conduire à son arrêt. La gravité dépend notamment de l'intensité, du trajet et de la durée du passage du courant. Seul un électricien intervient sur une installation.

**Version simple — avant** (21 mots) :
> C'est ce qui arrive quand le courant traverse le corps. Même une faible quantité peut faire très mal et devenir dangereuse.

**Version simple — après** (29 mots) :
> Si l'on touche un fil abîmé d'un appareil branché, le courant peut traverser le corps : c'est l'électrisation. C'est dangereux, alors on prévient un adulte au lieu d'y toucher.

**Sources après** (à ouvrir une par une) :
- [INRS — Accidents d'origine électrique](https://www.inrs.fr/risques/electriques/accidents-origine-electrique.html) — type `reference`
- [INRS — Risques liés à l'électricité](https://www.inrs.fr/risques/electriques/risques-electricite.html) — type `reference`

**Fiches liées après** : `courant-electrique`, `defaut-d-isolement` (nouveau), `disjoncteur-differentiel`, `electricien` (nouveau), `electrocution`, `habilitation-electrique`, `intensite-electrique` (nouveau), `mise-a-la-terre`, `phase-electrique`, `tres-basse-tension-de-securite`

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

### 5. Disjoncteur différentiel — `disjoncteur-differentiel`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (31 mots) :
> Appareil qui compare le courant entrant et le courant sortant d'un circuit et coupe dès qu'un écart apparaît. Un modèle 30 milliampères protège les personnes contre les contacts directs et indirects.

**Définition — après** (59 mots) :
> Appareil qui compare les courants de la phase et du neutre et coupe dès que leur écart atteint sa sensibilité, par exemple 30 mA. Il protège contre surcharges et courts-circuits, et contre le contact avec une carcasse mise sous tension par un défaut ; contre un fil sous tension, le 30 mA n'est qu'un complément. Pose par un électricien.

**Version simple — avant** (19 mots) :
> Cet appareil surveille si un peu d'électricité s'échappe du circuit, par exemple à travers une personne, et coupe aussitôt.

**Version simple — après** (31 mots) :
> Dans le tableau électrique de la maison, cet appareil coupe le courant quand un peu de courant s'échappe, par exemple par un fil abîmé. Seul un électricien l'installe ou le change.

**Synonymes** : DDR, differentiel 30 mA, disjoncteur differentiel, interrupteur differentiel → **DDR, differentiel 30 mA, disjoncteur differentiel**

**Sources après** (à ouvrir une par une) :
- [La protection différentielle dans les installations électriques BT, Schneider Electric, revue Intersections (juin 2001), hébergé par Éduscol STI](https://sti.eduscol.education.fr/sites/eduscol.education.fr.sti/files/ressources/techniques/680/680-gt-differentiel.pdf) — type `reference`
- [INRS — Risques électriques : glossaire (contact direct, contact indirect)](https://www.inrs.fr/risques/electriques/glossaire.html) — type `reference`

**Fiches liées après** : `courant-de-fuite`, `court-circuit` (nouveau), `defaut-d-isolement`, `disjoncteur`, `electricien` (nouveau), `electrisation`, `electrocution`, `mise-a-la-terre`, `neutre` (nouveau), `phase-electrique` (nouveau), `regime-de-neutre`, `tableau-electrique`, `tension-electrique` (nouveau)

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
