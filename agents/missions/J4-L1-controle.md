---
lot: J4-L1
role: controle
date: 2026-09-25
changeset: agents/changesets/J4-L1.jsonl
elements: ["actionneur", "cable-electrique", "capteur", "circuit-electrique", "circuit-ferme", "circuit-ouvert", "conducteur-electrique", "electronique-embarquee", "generateur-electrique", "intensite-electrique", "interrupteur", "isolant-electrique", "microcontroleur", "pile-electrique", "processeur-cpu", "protocole-de-communication", "puissance-electrique", "resistance-electrique", "signal-analogique", "signal-numerique", "tension-electrique"]
---

# Contrôle du lot J4-L1

21 fiche(s), 98 opération(s) du rédacteur (changeset non encore appliqué).

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

### 1. Actionneur — `actionneur`

- Niveau scolaire : C4 (cycles C4, 2GT) — version simple obligatoire
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (20 mots) :
> Composant électronique ou électromécanique, comme un servomoteur ou un relais électronique, qui convertit un signal de commande en action physique.

**Définition — après** (41 mots) :
> Constituant d'un système automatisé qui transforme un ordre de commande, le plus souvent un signal électrique envoyé par un microcontrôleur, en action sur le monde physique : mouvement, chaleur, lumière ou son. Un moteur électrique ou un servomoteur sont des actionneurs.

**Version simple — avant** (0 mots) :
_(vide)_

**Version simple — après** (27 mots) :
> Un actionneur est la pièce qui agit quand une machine reçoit un ordre : par exemple le petit moteur qui fait tourner les roues d'une voiture télécommandée.

**Synonymes** : — → **actuateur**

**Sources après** (à ouvrir une par une) :
- [Programme du cycle 4 en vigueur à la rentrée 2020 (d'après le BOEN n° 31 du 30 juillet 2020), p. 124 : technologie, « Écrire, mettre au point et exécuter un programme » (systèmes embarqués ; capteur, actionneur, interface ; notion de protocole)](https://eduscol.education.gouv.fr/sites/default/files/document/programme-d-enseignement-du-cycle-4-67722.pdf#page=124) — type `programme`
- [Dictionnaire de français Larousse, article « actionneur »](https://www.larousse.fr/dictionnaires/francais/actionneur/934) — type `reference`

**Fiches liées après** : `asservissement`, `automate-programmable`, `bras-robotise`, `chaine-d-energie`, `chaine-d-information`, `codeur-rotatif`, `composant-electronique`, `detecteur`, `electronique`, `electronique-embarquee` (nouveau), `microcontroleur` (nouveau), `moteur-electrique` (nouveau), `moteur-pas-a-pas`, `relais-electronique`, `servomoteur`, `ventilateur-de-refroidissement`, `volet-roulant-motorise`

```
fiche : actionneur
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 2. Câble électrique — `cable-electrique`

- Niveau scolaire : C2 (cycles C2, C3) — version simple obligatoire
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (17 mots) :
> Ensemble de fils électriques regroupés et protégés par une gaine isolante, servant au transport du courant électrique.

**Définition — après** (41 mots) :
> Ensemble de fils conducteurs isolés les uns des autres et réunis sous une gaine commune qui les protège électriquement et mécaniquement. Il sert à amener l'énergie électrique jusqu'aux appareils ou à transmettre des signaux, par exemple dans les réseaux de télécommunication.

**Version simple — avant** (0 mots) :
_(vide)_

**Version simple — après** (25 mots) :
> Un câble électrique regroupe plusieurs fils de métal, chacun entouré de plastique, dans une même gaine. Le cordon d'un chargeur de téléphone est un câble.

**Synonymes** : — → **câble**

**Sources après** (à ouvrir une par une) :
- [Programme de sciences et technologie du cycle 2 (annexe 1 de l'arrêté du 5 juin 2026, BO n° 24 du 11 juin 2026), p. 11 : objets techniques (pile électrique, câbles, interrupteur, ampoule)](https://www.education.gouv.fr/sites/default/files/document/annexe-1-programme-de-sciences-et-technologie-du-cycle-2-519020.pdf#page=11) — type `programme`
- [Dictionnaire de français Larousse, article « câble »](https://www.larousse.fr/dictionnaires/francais/c%C3%A2ble/11884) — type `reference`

**Fiches liées après** : `chute-de-tension`, `conducteur-electrique` (nouveau), `connecteur-electrique`, `courant-electrique`, `energie-electrique` (nouveau), `fil-electrique` (nouveau), `isolant-electrique` (nouveau), `section-de-cable`

```
fiche : cable-electrique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 3. Capteur — `capteur`

- Niveau scolaire : C4 (cycles C4, 2GT, 1G, TG, BACPRO, STI2D) — version simple obligatoire
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (22 mots) :
> Composant électronique qui transforme une grandeur physique, comme la température ou la pression, en signal analogique ou numérique exploitable par un microcontrôleur.

**Définition — après** (42 mots) :
> Dispositif qui prélève une grandeur physique, comme une température, une lumière ou une distance, et la traduit en une autre grandeur, le plus souvent électrique, exploitable pour mesurer ou commander. Dans la chaîne d'information d'un objet, il fournit ses données au microcontrôleur.

**Version simple — avant** (0 mots) :
_(vide)_

**Version simple — après** (33 mots) :
> Un capteur est comme un organe des sens pour une machine : il mesure quelque chose, par exemple la lumière qui fait allumer les phares d'une voiture à la tombée de la nuit.

**Sources après** (à ouvrir une par une) :
- [Programme du cycle 4 en vigueur à la rentrée 2020 (d'après le BOEN n° 31 du 30 juillet 2020), p. 123 : technologie, « Mesurer des grandeurs » (capteur, nature du signal analogique ou numérique)](https://eduscol.education.gouv.fr/sites/default/files/document/programme-d-enseignement-du-cycle-4-67722.pdf#page=123) — type `programme`
- [Programme de technologie du cycle 4 (annexe, BO n° 9 du 29 février 2024), p. 9 : « Fonctions, solutions, constituants de la chaîne d'information » (capteurs, microcontrôleur)](https://www.education.gouv.fr/sites/default/files/document/Annexe%20%E2%80%94%20Programme%20de%20technologie%20du%20cycle%204-368016.pdf#page=9) — type `programme`
- [Dictionnaire de français Larousse, article « capteur »](https://www.larousse.fr/dictionnaires/francais/capteur/13016) — type `reference`

**Fiches liées après** : `asservissement`, `automate-programmable`, `bus-spi`, `capteur-de-pression`, `capteur-de-temperature`, `capteur-optique`, `chaine-d-information`, `codeur-rotatif`, `composant-electronique`, `detecteur`, `detecteur-de-presence`, `drone`, `effet-hall`, `electronique`, `electronique-embarquee` (nouveau), `interruption`, `lora`, `microcontroleur`, `microphone`, `photodiode`, `phototransistor`, `pont-de-wheatstone`, `signal-analogique`, `thermistance`, `zigbee`

```
fiche : capteur
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 4. Circuit électrique — `circuit-electrique`

- Niveau scolaire : C2 (cycles C2, C3, C4, 1G, CAP) — version simple obligatoire
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (18 mots) :
> Ensemble de composants reliés par des conducteurs électriques formant un chemin fermé permettant la circulation du courant électrique.

**Définition — après** (40 mots) :
> Ensemble de dipôles, comme un générateur, un interrupteur et une lampe, reliés entre eux par des fils conducteurs. Lorsqu'il forme une boucle complète entre les deux bornes du générateur, un courant électrique y circule et fait fonctionner les appareils branchés.

**Version simple — avant** (0 mots) :
_(vide)_

**Version simple — après** (30 mots) :
> Un circuit électrique est un chemin de fils qui part de la pile et y revient en passant par une lampe : si le chemin est complet, la lampe s'allume.

**Synonymes** : — → **circuit**

**Sources après** (à ouvrir une par une) :
- [Programme de sciences et technologie du cycle 2 (annexe 1 de l'arrêté du 5 juin 2026, BO n° 24 du 11 juin 2026), p. 4 : « L'électricité » (circuit à une boucle, circuit ouvert ou fermé, matériaux conducteurs et isolants)](https://www.education.gouv.fr/sites/default/files/document/annexe-1-programme-de-sciences-et-technologie-du-cycle-2-519020.pdf#page=4) — type `programme`
- [Programme de sciences et technologie du cycle 3 (annexe 2 de l'arrêté du 5 juin 2026, BO n° 24 du 11 juin 2026), p. 7 : « Électricité » (circuit électrique à une boucle, matériaux conducteurs et isolants)](https://www.education.gouv.fr/sites/default/files/document/annexe-2-programme-de-sciences-et-technologie-du-cycle-3-519023.pdf#page=7) — type `programme`
- [Dictionnaire de français Larousse, article « circuit »](https://www.larousse.fr/dictionnaires/francais/circuit/16145) — type `reference`

**Fiches liées après** : `circuit-ferme`, `circuit-ouvert`, `courant-electrique`, `dipole`, `disjoncteur`, `fil-electrique` (nouveau), `fusible`, `generateur-electrique` (nouveau), `interrupteur`, `loi-des-mailles`, `loi-des-noeuds`, `neutre`, `phase-electrique`, `pont-diviseur-de-courant`, `pont-diviseur-de-tension`, `schema-electrique`, `tension-electrique`, `theoreme-de-millman`, `theoreme-de-norton`, `theoreme-de-superposition`, `theoreme-de-thevenin`, `voltmetre`, `wattmetre`

```
fiche : circuit-electrique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 5. Circuit fermé — `circuit-ferme`

- Niveau scolaire : C2 (cycles C2, C3) — version simple obligatoire
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (16 mots) :
> État d'un circuit électrique dont le trajet est complet, permettant au courant électrique de circuler normalement.

**Définition — après** (39 mots) :
> Circuit électrique dans lequel une boucle conductrice relie sans interruption les deux bornes du générateur, par exemple parce que l'interrupteur est fermé. Le courant électrique peut alors circuler et les appareils du circuit fonctionnent, comme une lampe qui s'allume.

**Version simple — avant** (0 mots) :
_(vide)_

**Version simple — après** (31 mots) :
> Un circuit est fermé quand le chemin du courant n'est coupé nulle part : quand on appuie sur le bouton d'une lampe de poche, le circuit se ferme et elle s'allume.

**Sources après** (à ouvrir une par une) :
- [Programme de sciences et technologie du cycle 2 (annexe 1 de l'arrêté du 5 juin 2026, BO n° 24 du 11 juin 2026), p. 4 : « L'électricité » (circuit à une boucle, circuit ouvert ou fermé, matériaux conducteurs et isolants)](https://www.education.gouv.fr/sites/default/files/document/annexe-1-programme-de-sciences-et-technologie-du-cycle-2-519020.pdf#page=4) — type `programme`
- [Programme de sciences et technologie du cycle 3 (annexe 2 de l'arrêté du 5 juin 2026, BO n° 24 du 11 juin 2026), p. 7 : « Électricité » (circuit électrique à une boucle, matériaux conducteurs et isolants)](https://www.education.gouv.fr/sites/default/files/document/annexe-2-programme-de-sciences-et-technologie-du-cycle-3-519023.pdf#page=7) — type `programme`

**Fiches liées après** : `circuit-electrique`, `circuit-ouvert` (nouveau), `courant-electrique`, `generateur-electrique` (nouveau), `interrupteur` (nouveau), `loi-des-mailles`

```
fiche : circuit-ferme
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 6. Circuit ouvert — `circuit-ouvert`

- Niveau scolaire : C2 (cycles C2, C3) — version simple obligatoire
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (16 mots) :
> État d'un circuit électrique dans lequel la continuité est interrompue, empêchant le courant électrique de circuler.

**Définition — après** (44 mots) :
> Circuit électrique dont le chemin est interrompu en au moins un point, par exemple par un interrupteur ouvert, un fil débranché ou une lampe grillée. Dans un circuit à une seule boucle, le courant électrique ne peut alors plus circuler et les appareils s'arrêtent.

**Version simple — avant** (0 mots) :
_(vide)_

**Version simple — après** (28 mots) :
> Un circuit est ouvert quand son chemin est coupé quelque part, par exemple par un interrupteur ouvert : le courant ne passe plus et la lampe reste éteinte.

**Sources après** (à ouvrir une par une) :
- [Programme de sciences et technologie du cycle 2 (annexe 1 de l'arrêté du 5 juin 2026, BO n° 24 du 11 juin 2026), p. 4 : « L'électricité » (circuit à une boucle, circuit ouvert ou fermé, matériaux conducteurs et isolants)](https://www.education.gouv.fr/sites/default/files/document/annexe-1-programme-de-sciences-et-technologie-du-cycle-2-519020.pdf#page=4) — type `programme`
- [Programme de sciences et technologie du cycle 3 (annexe 2 de l'arrêté du 5 juin 2026, BO n° 24 du 11 juin 2026), p. 7 : « Électricité » (circuit électrique à une boucle, matériaux conducteurs et isolants)](https://www.education.gouv.fr/sites/default/files/document/annexe-2-programme-de-sciences-et-technologie-du-cycle-3-519023.pdf#page=7) — type `programme`

**Fiches liées après** : `circuit-electrique`, `circuit-ferme` (nouveau), `courant-electrique`, `fil-electrique` (nouveau), `interrupteur` (nouveau)

```
fiche : circuit-ouvert
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 7. Conducteur électrique — `conducteur-electrique`

- Niveau scolaire : C2 (cycles C2, C3) — version simple obligatoire
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (16 mots) :
> Matériau, souvent métallique, qui laisse circuler facilement le courant électrique, utilisé notamment dans les câbles électriques.

**Définition — après** (43 mots) :
> Matériau qui laisse facilement passer le courant électrique, parce qu'il contient des charges électriques libres de se déplacer, comme les électrons des métaux. Le cuivre et l'aluminium, utilisés dans les fils et les câbles électriques, ainsi que le graphite, sont de bons conducteurs.

**Version simple — avant** (0 mots) :
_(vide)_

**Version simple — après** (31 mots) :
> Un conducteur est une matière qui laisse passer le courant, comme le métal. Si on place une cuillère en métal dans le circuit d'une pile et d'une lampe, la lampe s'allume.

**Synonymes** : — → **matériau conducteur**

**Sources après** (à ouvrir une par une) :
- [Programme de sciences et technologie du cycle 2 (annexe 1 de l'arrêté du 5 juin 2026, BO n° 24 du 11 juin 2026), p. 4 : « L'électricité » (circuit à une boucle, circuit ouvert ou fermé, matériaux conducteurs et isolants)](https://www.education.gouv.fr/sites/default/files/document/annexe-1-programme-de-sciences-et-technologie-du-cycle-2-519020.pdf#page=4) — type `programme`
- [Programme de sciences et technologie du cycle 3 (annexe 2 de l'arrêté du 5 juin 2026, BO n° 24 du 11 juin 2026), p. 7 : « Électricité » (circuit électrique à une boucle, matériaux conducteurs et isolants)](https://www.education.gouv.fr/sites/default/files/document/annexe-2-programme-de-sciences-et-technologie-du-cycle-3-519023.pdf#page=7) — type `programme`
- [Dictionnaire de français Larousse, article « conducteur »](https://www.larousse.fr/dictionnaires/francais/conducteur/18033) — type `reference`

**Fiches liées après** : `amperemetre`, `atome`, `bande-interdite`, `cable-electrique` (nouveau), `caracteristique-tension-courant`, `charge-electrique` (nouveau), `courant-electrique`, `electrolyse`, `electron`, `fil-electrique`, `induction-electromagnetique`, `intensite-electrique`, `isolant-electrique` (nouveau), `loi-d-ohm`, `ohmmetre`, `resistance-electrique`, `siemens`, `supraconductivite`

```
fiche : conducteur-electrique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 8. Électronique embarquée — `electronique-embarquee`

- Niveau scolaire : C4 (cycles C4, 2GT) — version simple obligatoire
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (19 mots) :
> Ensemble des systèmes électroniques, souvent construits autour d'un microcontrôleur, intégrés dans un objet pour en assurer le fonctionnement autonome.

**Définition — après** (40 mots) :
> Ensemble des circuits électroniques intégrés à un objet ou à un véhicule pour le faire fonctionner de façon autonome, sans ordinateur extérieur. Construite en général autour d'un microcontrôleur, elle lit des capteurs, exécute un programme enregistré et commande des actionneurs.

**Version simple — avant** (0 mots) :
_(vide)_

**Version simple — après** (29 mots) :
> L'électronique embarquée est un petit cerveau électronique caché dans un objet. Dans une machine à laver, elle suit le programme choisi pour chauffer l'eau et faire tourner le tambour.

**Synonymes** : — → **système embarqué**

**Sources après** (à ouvrir une par une) :
- [Programme du cycle 4 en vigueur à la rentrée 2020 (d'après le BOEN n° 31 du 30 juillet 2020), p. 124 : technologie, « Écrire, mettre au point et exécuter un programme » (systèmes embarqués ; capteur, actionneur, interface ; notion de protocole)](https://eduscol.education.gouv.fr/sites/default/files/document/programme-d-enseignement-du-cycle-4-67722.pdf#page=124) — type `programme`
- [Programme de technologie du cycle 4 (annexe, BO n° 9 du 29 février 2024), p. 9 : « Fonctions, solutions, constituants de la chaîne d'information » (capteurs, microcontrôleur)](https://www.education.gouv.fr/sites/default/files/document/Annexe%20%E2%80%94%20Programme%20de%20technologie%20du%20cycle%204-368016.pdf#page=9) — type `programme`

**Fiches liées après** : `actionneur` (nouveau), `batterie-lithium-ion`, `capteur` (nouveau), `capteur-de-pression`, `carte-arduino`, `carte-raspberry-pi`, `domotique`, `drone`, `firmware`, `interruption`, `microcontroleur`, `robotique`

```
fiche : electronique-embarquee
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 9. Générateur électrique — `generateur-electrique`

- Niveau scolaire : C2 (cycles C2, C3, 1G) — version simple obligatoire
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (17 mots) :
> Dispositif qui produit de l'électricité à partir d'une autre forme d'énergie, comme un alternateur ou une dynamo.

**Définition — après** (53 mots) :
> Dipôle qui fournit de l'énergie électrique à un circuit en la convertissant à partir d'une autre forme d'énergie : chimique dans une pile, mécanique dans un alternateur ou une dynamo, lumineuse dans un panneau photovoltaïque. Il crée entre ses deux bornes une tension qui fait circuler le courant lorsque le circuit est fermé.

**Version simple — avant** (0 mots) :
_(vide)_

**Version simple — après** (29 mots) :
> Un générateur donne au circuit l'énergie qui fait fonctionner les appareils. La pile d'une lampe de poche en est un : sans elle, la lampe ne peut pas s'allumer.

**Synonymes** : — → **générateur**

**Sources après** (à ouvrir une par une) :
- [Programme de sciences et technologie du cycle 2 (annexe 1 de l'arrêté du 5 juin 2026, BO n° 24 du 11 juin 2026), p. 4 : « L'électricité » (circuit à une boucle, circuit ouvert ou fermé, matériaux conducteurs et isolants)](https://www.education.gouv.fr/sites/default/files/document/annexe-1-programme-de-sciences-et-technologie-du-cycle-2-519020.pdf#page=4) — type `programme`
- [Dictionnaire de français Larousse, article « générateur »](https://www.larousse.fr/dictionnaires/francais/g%C3%A9n%C3%A9rateur/36533) — type `reference`

**Fiches liées après** : `alternateur`, `chaine-d-energie`, `circuit-electrique` (nouveau), `circuit-ferme` (nouveau), `courant-electrique` (nouveau), `dipole`, `dynamo`, `electricite`, `energie-electrique` (nouveau), `eolienne`, `freinage-regeneratif`, `loi-des-mailles`, `moteur-electrique`, `panneau-photovoltaique` (nouveau), `pile-electrique`, `tension-electrique` (nouveau), `theoreme-de-superposition`, `theoreme-de-thevenin`

```
fiche : generateur-electrique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 10. Intensité électrique — `intensite-electrique`

- Niveau scolaire : C4 (cycles C4, 2GT, 1G) — version simple obligatoire
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (19 mots) :
> Quantité de charge électrique traversant un conducteur électrique par unité de temps, mesurée en ampères à l'aide d'un ampèremètre.

**Définition — après** (51 mots) :
> Grandeur qui mesure le débit du courant électrique, c'est-à-dire la quantité de charge électrique qui traverse une section d'un conducteur par seconde. Elle s'exprime en ampères (symbole A) et se mesure avec un ampèremètre branché en série. Dans un circuit à une seule boucle, elle est la même en tout point.

**Version simple — avant** (0 mots) :
_(vide)_

**Version simple — après** (29 mots) :
> L'intensité dit combien de courant passe dans un fil, un peu comme le débit de l'eau dans un tuyau. On la mesure en ampères avec un appareil appelé ampèremètre.

**Sources après** (à ouvrir une par une) :
- [Programme du cycle 4 en vigueur à la rentrée 2020 (d'après le BOEN n° 31 du 30 juillet 2020), p. 103 : « Réaliser des circuits électriques simples et exploiter les lois de l'électricité »](https://eduscol.education.gouv.fr/sites/default/files/document/programme-d-enseignement-du-cycle-4-67722.pdf#page=103) — type `programme`
- [Dictionnaire de français Larousse, article « intensité »](https://www.larousse.fr/dictionnaires/francais/intensit%C3%A9/43584) — type `reference`

**Fiches liées après** : `amperage`, `ampere`, `amperemetre`, `caracteristique-tension-courant`, `charge-electrique`, `conducteur-electrique`, `courant-electrique`, `court-circuit`, `dipole`, `fusible`, `loi-d-ohm`, `loi-des-noeuds`, `multimetre`, `pince-amperemetrique`, `puissance-electrique`, `resistance-electrique` (nouveau)

```
fiche : intensite-electrique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 11. Interrupteur — `interrupteur`

- Niveau scolaire : C2 (cycles C2, C3) — version simple obligatoire
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (17 mots) :
> Dispositif permettant d'ouvrir ou de fermer manuellement un circuit électrique pour couper ou rétablir le courant électrique.

**Définition — après** (47 mots) :
> Dispositif qui permet d'ouvrir ou de fermer un circuit électrique à la demande : en position fermée, il laisse circuler le courant ; en position ouverte, il interrompt la boucle et le courant s'arrête. On le manœuvre à la main, comme le bouton d'une lampe de poche.

**Version simple — avant** (0 mots) :
_(vide)_

**Version simple — après** (29 mots) :
> Un interrupteur sert à couper ou à laisser passer le courant. Quand tu appuies sur le bouton d'une lampe de poche, tu fermes le circuit et la lampe s'allume.

**Sources après** (à ouvrir une par une) :
- [Programme de sciences et technologie du cycle 2 (annexe 1 de l'arrêté du 5 juin 2026, BO n° 24 du 11 juin 2026), p. 4 : « L'électricité » (circuit à une boucle, circuit ouvert ou fermé, matériaux conducteurs et isolants)](https://www.education.gouv.fr/sites/default/files/document/annexe-1-programme-de-sciences-et-technologie-du-cycle-2-519020.pdf#page=4) — type `programme`
- [Programme de sciences et technologie du cycle 3 (annexe 2 de l'arrêté du 5 juin 2026, BO n° 24 du 11 juin 2026), p. 7 : « Électricité » (circuit électrique à une boucle, matériaux conducteurs et isolants)](https://www.education.gouv.fr/sites/default/files/document/annexe-2-programme-de-sciences-et-technologie-du-cycle-3-519023.pdf#page=7) — type `programme`
- [Dictionnaire de français Larousse, article « interrupteur »](https://www.larousse.fr/dictionnaires/francais/interrupteur/43842) — type `reference`

**Fiches liées après** : `bouton-poussoir`, `circuit-electrique`, `circuit-ferme` (nouveau), `circuit-ouvert` (nouveau), `contacteur`, `courant-electrique`, `detecteur`

```
fiche : interrupteur
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 12. Isolant électrique — `isolant-electrique`

- Niveau scolaire : C2 (cycles C2, C3) — version simple obligatoire
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (17 mots) :
> Matériau qui empêche ou limite fortement le passage du courant électrique, utilisé pour protéger les conducteurs électriques.

**Définition — après** (48 mots) :
> Matériau qui ne laisse pratiquement pas passer le courant électrique, car ses charges électriques ne peuvent presque pas se déplacer. Le plastique, le verre, le caoutchouc, la céramique ou l'air sec sont des isolants, utilisés pour entourer les fils et protéger les personnes des contacts avec les conducteurs.

**Version simple — avant** (0 mots) :
_(vide)_

**Version simple — après** (31 mots) :
> Un isolant est une matière qui ne laisse pas passer le courant, comme le plastique, le verre ou le caoutchouc. C'est pour cela que les fils électriques sont entourés de plastique.

**Synonymes** : — → **matériau isolant**

**Sources après** (à ouvrir une par une) :
- [Programme de sciences et technologie du cycle 2 (annexe 1 de l'arrêté du 5 juin 2026, BO n° 24 du 11 juin 2026), p. 4 : « L'électricité » (circuit à une boucle, circuit ouvert ou fermé, matériaux conducteurs et isolants)](https://www.education.gouv.fr/sites/default/files/document/annexe-1-programme-de-sciences-et-technologie-du-cycle-2-519020.pdf#page=4) — type `programme`
- [Programme de sciences et technologie du cycle 3 (annexe 2 de l'arrêté du 5 juin 2026, BO n° 24 du 11 juin 2026), p. 7 : « Électricité » (circuit électrique à une boucle, matériaux conducteurs et isolants)](https://www.education.gouv.fr/sites/default/files/document/annexe-2-programme-de-sciences-et-technologie-du-cycle-3-519023.pdf#page=7) — type `programme`
- [Dictionnaire de français Larousse, article « isolant »](https://www.larousse.fr/dictionnaires/francais/isolant/44460) — type `reference`

**Fiches liées après** : `atome`, `bande-interdite`, `cable-electrique` (nouveau), `charge-electrique` (nouveau), `classe-d-isolation`, `conducteur-electrique` (nouveau), `controleur-d-isolement`, `courant-de-fuite`, `courant-electrique`, `defaut-d-isolement`, `dielectrique`, `fil-electrique` (nouveau), `gaine-thermoretractable`

```
fiche : isolant-electrique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 13. Microcontrôleur — `microcontroleur`

- Niveau scolaire : C4 (cycles C4, 2GT, 1G, TG, STI2D) — version simple obligatoire
- Règles automatiques encore enfreintes : aucune

**Version simple — avant** (0 mots) :
_(vide)_

**Version simple — après** (32 mots) :
> Un microcontrôleur est une petite puce qui fonctionne comme un ordinateur très simple. On le programme pour commander un objet, par exemple un robot qui avance quand on appuie sur un bouton.

**Sources après** (à ouvrir une par une) :
- [FranceTerme (Commission d'enrichissement de la langue française), fiche « microcontrôleur »](https://www.culture.fr/franceterme/terme/INFO680) — type `reference`
- [Programme de technologie du cycle 4 (annexe, BO n° 9 du 29 février 2024), p. 9 : « Fonctions, solutions, constituants de la chaîne d'information » (capteurs, microcontrôleur)](https://www.education.gouv.fr/sites/default/files/document/Annexe%20%E2%80%94%20Programme%20de%20technologie%20du%20cycle%204-368016.pdf#page=9) — type `programme`

**Fiches liées après** : `actionneur` (nouveau), `asic`, `bus-i2c`, `bus-spi`, `capteur`, `capteur-de-temperature`, `carte-arduino`, `chaine-d-information`, `circuit-integre`, `convertisseur-analogique-numerique-can`, `electronique-embarquee`, `esp32`, `firmware`, `gpio`, `interruption`, `machine-a-etats`, `memoire-morte-rom`, `memoire-vive-ram`, `modulation-de-largeur-d-impulsion-pwm`, `moteur-pas-a-pas`, `objet-connecte-iot`, `oscillateur`, `processeur-cpu`, `signal-numerique`, `systeme-hexadecimal`

```
fiche : microcontroleur
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 14. Pile électrique — `pile-electrique`

- Niveau scolaire : C2 (cycles C2) — version simple obligatoire
- Règles automatiques encore enfreintes : aucune

**Version simple — avant** (0 mots) :
_(vide)_

**Version simple — après** (29 mots) :
> Une pile fournit l'énergie qui fait marcher une télécommande ou une lampe de poche. À l'intérieur, des produits chimiques réagissent ; quand ils sont épuisés, la pile est vide.

**Synonymes** : — → **pile**

**Sources après** (à ouvrir une par une) :
- [Programme de sciences et technologie du cycle 2 (annexe 1 de l'arrêté du 5 juin 2026, BO n° 24 du 11 juin 2026), p. 4 : « L'électricité » (circuit à une boucle, circuit ouvert ou fermé, matériaux conducteurs et isolants)](https://www.education.gouv.fr/sites/default/files/document/annexe-1-programme-de-sciences-et-technologie-du-cycle-2-519020.pdf#page=4) — type `programme`
- [Programme de sciences et technologie du cycle 2 (annexe 1 de l'arrêté du 5 juin 2026, BO n° 24 du 11 juin 2026), p. 11 : objets techniques (pile électrique, câbles, interrupteur, ampoule)](https://www.education.gouv.fr/sites/default/files/document/annexe-1-programme-de-sciences-et-technologie-du-cycle-2-519020.pdf#page=11) — type `programme`
- [Dictionnaire de français Larousse, article « pile »](https://www.larousse.fr/dictionnaires/francais/pile/60903) — type `reference`

**Fiches liées après** : `accumulateur`, `ampere-heure`, `batterie`, `generateur-electrique`, `histoire-de-l-electricite`, `pile-a-combustible`

```
fiche : pile-electrique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 15. Processeur (CPU) — `processeur-cpu`

- Niveau scolaire : C2 (cycles C2) — version simple obligatoire
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (20 mots) :
> Composant qui exécute les calculs et les instructions d'un programme informatique, présent sous forme de microprocesseur sur la carte mère.

**Définition — après** (43 mots) :
> Composant électronique qui interprète et exécute les instructions d'un programme informatique, en effectuant des calculs et des opérations logiques sur des données. Cœur de tout ordinateur, il est aujourd'hui réalisé sous la forme d'un microprocesseur, un circuit intégré placé sur la carte mère.

**Version simple — avant** (0 mots) :
_(vide)_

**Version simple — après** (28 mots) :
> Le processeur est la partie d'un ordinateur ou d'une tablette qui fait les calculs. Il suit les instructions des programmes, par exemple pour afficher un jeu à l'écran.

**Sources après** (à ouvrir une par une) :
- [Programme de sciences et technologie du cycle 2 (annexe 1 de l'arrêté du 5 juin 2026, BO n° 24 du 11 juin 2026), p. 11 : dispositifs numériques (clavier, processeur, écran)](https://www.education.gouv.fr/sites/default/files/document/annexe-1-programme-de-sciences-et-technologie-du-cycle-2-519020.pdf#page=11) — type `programme`
- [Dictionnaire de français Larousse, article « processeur »](https://www.larousse.fr/dictionnaires/francais/processeur/64060) — type `reference`

**Fiches liées après** : `bus-de-donnees`, `carte-mere`, `circuit-integre` (nouveau), `convertisseur-analogique-numerique-can`, `dissipateur-thermique`, `memoire-vive-ram`, `microcontroleur`, `microprocesseur`

```
fiche : processeur-cpu
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 16. Protocole de communication — `protocole-de-communication`

- Niveau scolaire : C4 (cycles C4) — version simple obligatoire
- Règles automatiques encore enfreintes : aucune

**Version simple — avant** (0 mots) :
_(vide)_

**Version simple — après** (31 mots) :
> Un protocole, ce sont les règles que deux appareils suivent pour se comprendre, comme une langue commune. Grâce à lui, une manette sans fil peut parler à une console de jeu.

**Synonymes** : — → **protocole**

**Sources après** (à ouvrir une par une) :
- [Programme du cycle 4 en vigueur à la rentrée 2020 (d'après le BOEN n° 31 du 30 juillet 2020), p. 124 : technologie, « Écrire, mettre au point et exécuter un programme » (systèmes embarqués ; capteur, actionneur, interface ; notion de protocole)](https://eduscol.education.gouv.fr/sites/default/files/document/programme-d-enseignement-du-cycle-4-67722.pdf#page=124) — type `programme`
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

### 17. Puissance électrique — `puissance-electrique`

- Niveau scolaire : C4 (cycles C4, 1G, BACPRO) — version simple obligatoire
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (23 mots) :
> Quantité d'énergie électrique consommée ou produite par unité de temps, exprimée en watts, égale au produit de la tension électrique par l'intensité électrique.

**Définition — après** (48 mots) :
> Grandeur qui indique la quantité d'énergie électrique qu'un appareil convertit chaque seconde. Elle s'exprime en watts (symbole W). En courant continu, elle est égale au produit de la tension par l'intensité, P = U × I ; l'énergie consommée est la puissance multipliée par la durée de fonctionnement.

**Version simple — avant** (0 mots) :
_(vide)_

**Version simple — après** (28 mots) :
> La puissance dit combien d'énergie un appareil utilise à chaque seconde. Un radiateur électrique a une grande puissance, une petite lampe à LED en a une toute petite.

**Sources après** (à ouvrir une par une) :
- [Programme du cycle 4 en vigueur à la rentrée 2020 (d'après le BOEN n° 31 du 30 juillet 2020), p. 103 : « Réaliser des circuits électriques simples et exploiter les lois de l'électricité »](https://eduscol.education.gouv.fr/sites/default/files/document/programme-d-enseignement-du-cycle-4-67722.pdf#page=103) — type `programme`
- [Dictionnaire de français Larousse, article « puissance »](https://www.larousse.fr/dictionnaires/francais/puissance/65022) — type `reference`

**Fiches liées après** : `courant-continu` (nouveau), `effet-joule`, `energie-electrique`, `intensite-electrique`, `joule`, `kilowatt`, `puissance-active`, `resistance`, `tension-electrique`, `triac`, `voltampere`, `watt`, `watt-crete`, `wattmetre`

```
fiche : puissance-electrique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 18. Résistance électrique — `resistance-electrique`

- Niveau scolaire : C4 (cycles C4) — version simple obligatoire
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (18 mots) :
> Opposition qu'un conducteur électrique oppose au passage du courant électrique, exprimée en ohms et mesurée avec un ohmmètre.

**Définition — après** (49 mots) :
> Grandeur qui caractérise la difficulté plus ou moins grande qu'a le courant électrique à traverser un dipôle. Elle s'exprime en ohms (symbole Ω) et se mesure avec un ohmmètre. Pour un conducteur ohmique, elle relie la tension et l'intensité par la loi d'Ohm : U = R × I.

**Version simple — avant** (0 mots) :
_(vide)_

**Version simple — après** (29 mots) :
> La résistance dit si le courant a du mal ou non à traverser un objet. Avec la même pile, plus la résistance est grande, moins il passe de courant.

**Sources après** (à ouvrir une par une) :
- [Programme du cycle 4 en vigueur à la rentrée 2020 (d'après le BOEN n° 31 du 30 juillet 2020), p. 103 : « Réaliser des circuits électriques simples et exploiter les lois de l'électricité »](https://eduscol.education.gouv.fr/sites/default/files/document/programme-d-enseignement-du-cycle-4-67722.pdf#page=103) — type `programme`
- [Dictionnaire de français Larousse, article « résistance »](https://www.larousse.fr/dictionnaires/francais/r%C3%A9sistance/68632) — type `reference`

**Fiches liées après** : `chute-de-tension`, `conducteur-electrique`, `controleur-d-isolement`, `courant-electrique`, `dipole` (nouveau), `effet-joule`, `intensite-electrique` (nouveau), `loi-d-ohm`, `multimetre`, `ohm`, `ohmmetre`, `pont-de-wheatstone`, `resistance`, `siemens`, `supraconductivite`, `tension-electrique` (nouveau), `theoreme-de-norton`, `theoreme-de-thevenin`

```
fiche : resistance-electrique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 19. Signal analogique — `signal-analogique`

- Niveau scolaire : C4 (cycles C4) — version simple obligatoire
- Règles automatiques encore enfreintes : aucune

**Version simple — avant** (0 mots) :
_(vide)_

**Version simple — après** (32 mots) :
> Un signal analogique varie en douceur, sans faire de sauts, comme la température qui monte peu à peu le matin. Le son capté par un micro donne un signal de ce type.

**Sources après** (à ouvrir une par une) :
- [Programme du cycle 4 en vigueur à la rentrée 2020 (d'après le BOEN n° 31 du 30 juillet 2020), p. 123 : technologie, « Mesurer des grandeurs » (capteur, nature du signal analogique ou numérique)](https://eduscol.education.gouv.fr/sites/default/files/document/programme-d-enseignement-du-cycle-4-67722.pdf#page=123) — type `programme`
- [Dictionnaire de français Larousse, article « analogique »](https://www.larousse.fr/dictionnaires/francais/analogique/3223) — type `reference`

**Fiches liées après** : `amplificateur-audio`, `amplificateur-operationnel`, `bruit-electronique`, `capteur`, `chaine-d-information`, `convertisseur-analogique-numerique-can`, `convertisseur-numerique-analogique-cna`, `echantillonnage`, `filtre-electronique`, `generateur-de-fonctions`, `hertz`, `impedance`, `microphone`, `oscilloscope`, `periode`, `redresseur`, `signal-audio`, `signal-numerique`, `valeur-crete`

```
fiche : signal-analogique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 20. Signal numérique — `signal-numerique`

- Niveau scolaire : C4 (cycles C4, TG) — version simple obligatoire
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (17 mots) :
> Signal électrique codé sous forme d'états discrets, généralement binaires, traité par un circuit numérique ou un microcontrôleur.

**Définition — après** (48 mots) :
> Signal qui ne peut prendre qu'un nombre limité de valeurs bien distinctes, le plus souvent deux états notés 0 et 1, et qui représente des informations sous forme de nombres. Produit et traité par des circuits numériques comme un microcontrôleur, il résiste mieux aux perturbations qu'un signal analogique.

**Version simple — avant** (0 mots) :
_(vide)_

**Version simple — après** (30 mots) :
> Un signal numérique ne prend que quelques valeurs bien séparées, souvent deux : allumé ou éteint, 1 ou 0. C'est ainsi que les ordinateurs et les téléphones échangent des informations.

**Synonymes** : — → **signal digital**

**Sources après** (à ouvrir une par une) :
- [Programme du cycle 4 en vigueur à la rentrée 2020 (d'après le BOEN n° 31 du 30 juillet 2020), p. 123 : technologie, « Mesurer des grandeurs » (capteur, nature du signal analogique ou numérique)](https://eduscol.education.gouv.fr/sites/default/files/document/programme-d-enseignement-du-cycle-4-67722.pdf#page=123) — type `programme`
- [Dictionnaire de français Larousse, article « numérique »](https://www.larousse.fr/dictionnaires/francais/num%C3%A9rique/55253) — type `reference`

**Fiches liées après** : `algebre-de-boole`, `bit`, `chaine-d-information`, `circuit-numerique`, `convertisseur-analogique-numerique-can`, `convertisseur-numerique-analogique-cna`, `detecteur`, `echantillonnage`, `gpio`, `microcontroleur`, `porte-logique`, `quantification`, `rapport-cyclique`, `servomoteur`, `signal-analogique`, `systeme-binaire`

```
fiche : signal-numerique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 21. Tension électrique — `tension-electrique`

- Niveau scolaire : C4 (cycles C4, 2GT, 1G, BACPRO) — version simple obligatoire
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (20 mots) :
> Différence de potentiel électrique entre deux points d'un circuit électrique, exprimée en volts, qui met en mouvement le courant électrique.

**Définition — après** (45 mots) :
> Grandeur électrique qui existe entre deux points d'un circuit et qui provoque le déplacement des charges électriques lorsque ces points sont reliés par un chemin conducteur. Elle s'exprime en volts (symbole V) et se mesure avec un voltmètre branché en dérivation entre ces deux points.

**Version simple — avant** (0 mots) :
_(vide)_

**Version simple — après** (33 mots) :
> La tension fait circuler le courant dans un circuit fermé, un peu comme une pente fait couler l'eau. Elle se mesure en volts : une pile de lampe de poche donne 1,5 volt.

**Sources après** (à ouvrir une par une) :
- [Programme du cycle 4 en vigueur à la rentrée 2020 (d'après le BOEN n° 31 du 30 juillet 2020), p. 103 : « Réaliser des circuits électriques simples et exploiter les lois de l'électricité »](https://eduscol.education.gouv.fr/sites/default/files/document/programme-d-enseignement-du-cycle-4-67722.pdf#page=103) — type `programme`
- [Dictionnaire de français Larousse, article « tension »](https://www.larousse.fr/dictionnaires/francais/tension/77330) — type `reference`

**Fiches liées après** : `caracteristique-tension-courant`, `charge-electrique` (nouveau), `circuit-electrique`, `courant-electrique`, `dipole`, `farad`, `generateur-electrique` (nouveau), `henry`, `induction-electromagnetique`, `loi-d-ohm`, `loi-des-mailles`, `monophase`, `mosfet`, `multimetre`, `oscilloscope`, `pont-diviseur-de-tension`, `poste-de-transformation`, `potentiometre`, `puissance-electrique`, `resistance-electrique` (nouveau), `theoreme-de-millman`, `transformateur`, `tres-basse-tension-de-securite`, `valeur-efficace`, `volt`, `voltage`, `voltmetre`

```
fiche : tension-electrique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```
