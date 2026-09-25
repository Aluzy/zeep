---
lot: J4-L1
role: controle
date: 2026-09-25
changeset: agents/changesets/J4-L1.jsonl
elements: ["actionneur", "cable-electrique", "capteur", "electronique-embarquee", "generateur-electrique", "protocole-de-communication"]
---

# Contrôle du lot J4-L1 — passe 2

6 fiche(s), 99 opération(s) du rédacteur (changeset non encore appliqué).

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

**Définition — après** (45 mots) :
> Constituant de la chaîne d'énergie d'un objet ou d'une machine qui convertit l'énergie qu'il reçoit, le plus souvent électrique, en action physique : mouvement, chaleur, lumière ou son. Il agit sur ordre de la chaîne d'information. Un moteur électrique ou un servomoteur sont des actionneurs.

**Version simple — avant** (0 mots) :
_(vide)_

**Version simple — après** (27 mots) :
> Un actionneur est la pièce qui agit quand une machine reçoit un ordre : par exemple le petit moteur qui fait tourner les roues d'une voiture télécommandée.

**Synonymes** : — → **actuateur**

**Sources après** (à ouvrir une par une) :
- [Programme du cycle 4 en vigueur à la rentrée 2020 (d'après le BOEN n° 31 du 30 juillet 2020), p. 124 : technologie, « Écrire, mettre au point et exécuter un programme » (systèmes embarqués ; capteur, actionneur, interface)](https://eduscol.education.gouv.fr/sites/default/files/document/programme-d-enseignement-du-cycle-4-67722.pdf#page=124) — type `programme`
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

**Définition — après** (46 mots) :
> Ensemble d'un ou de plusieurs conducteurs métalliques, chacun entouré de sa propre enveloppe isolante, le tout protégé par une gaine extérieure contre les chocs et les contacts. Selon son usage, il achemine l'énergie électrique jusqu'aux appareils ou transporte des signaux, par exemple entre deux équipements informatiques.

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
> Un capteur est comme un organe des sens pour une machine : il mesure quelque chose, par exemple la lumière. Quand la nuit tombe, il fait allumer tout seuls les phares d'une voiture.

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

### 4. Électronique embarquée — `electronique-embarquee`

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
- [Programme du cycle 4 en vigueur à la rentrée 2020 (d'après le BOEN n° 31 du 30 juillet 2020), p. 124 : technologie, « Écrire, mettre au point et exécuter un programme » (systèmes embarqués ; capteur, actionneur, interface)](https://eduscol.education.gouv.fr/sites/default/files/document/programme-d-enseignement-du-cycle-4-67722.pdf#page=124) — type `programme`
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

### 5. Générateur électrique — `generateur-electrique`

- Niveau scolaire : C2 (cycles C2, C3, 1G) — version simple obligatoire
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (17 mots) :
> Dispositif qui produit de l'électricité à partir d'une autre forme d'énergie, comme un alternateur ou une dynamo.

**Définition — après** (52 mots) :
> Appareil qui fournit de l'énergie électrique à un circuit en la convertissant à partir d'une autre forme d'énergie : chimique dans une pile, mécanique dans un alternateur ou une dynamo, lumineuse dans un panneau photovoltaïque. Il crée entre ses bornes une tension qui fait circuler le courant lorsque le circuit est fermé.

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

### 6. Protocole de communication — `protocole-de-communication`

- Niveau scolaire : C4 (cycles C4) — version simple obligatoire
- Règles automatiques encore enfreintes : aucune

**Définition — avant** (25 mots) :
> Ensemble de règles définissant l'échange de données sur un bus de données ou une interface série, comme le bus I2C, le bus SPI ou l'USB.

**Définition — après** (47 mots) :
> Ensemble de règles communes qui fixent comment des appareils échangent des données : format des messages, ordre des échanges, détection des erreurs. Il en existe pour les liaisons entre composants, comme le bus I2C ou l'USB, et pour les réseaux, comme Internet, le Wi-Fi ou le Bluetooth.

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
