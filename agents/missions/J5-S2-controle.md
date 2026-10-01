---
lot: J5-S2
role: controle
date: 2026-10-01
changeset: agents/changesets/J5-S2.jsonl
elements: ["autoconsommation", "borne-de-recharge", "eco-conception", "empreinte-carbone-de-l-electricite", "freinage-regeneratif", "hydrogene", "indice-de-reparabilite", "obsolescence-programmee", "pile-a-combustible", "station-de-transfert-d-energie-par-pompage", "terres-rares", "thermostat-connecte", "vehicule-electrique"]
---

# Contrôle du lot J5-S2

13 fiche(s), 20 opération(s) du rédacteur (changeset non encore appliqué).

## Consignes du contrôleur

Tu es le **contrôleur** du lot J5-S2. Tu n'as pas participé à la rédaction et tu ne la vois qu'à
travers ce document : les justifications du rédacteur sont volontairement absentes. Tu vérifies
chaque fiche contre les **12 critères** de `docs/grille-relecture.md` (lis-la en entier d'abord).

1. **Ouvre chaque URL de source** et vérifie qu'elle appuie la définition. Une source que tu ne
   peux pas ouvrir, imprécise (page d'accueil) ou qui n'appuie pas l'affirmation = critère 8 en échec.
2. Une fiche est **conforme** si les 12 critères passent. Dans `agents/changesets/J5-S2-controle.jsonl`, remplace alors
   `"__A_REMPLIR__"` de `new` par
   `{"date": "2026-10-01", "par": "agent-controleur-J5-S2", "statut": "relu-ia"}` et `why` par
   « Relue selon la grille (12 critères) ».
3. Une fiche **refusée** : supprime sa ligne dans `agents/changesets/J5-S2-controle.jsonl`, et note les critères en échec. Tu ne
   réécris pas la fiche : le rédacteur la corrige (nouvelle passe de contrôle) ou la retire du lot.
   Si le défaut porte sur une fiche hors lot, ajoute-la à `agents/donnees/signalements.json`.
4. Écris tes verdicts dans la section « Relecture (rempli par le contrôleur) » de
   `agents/rapports/J5-S2.md`, une ligne par fiche : critères en échec, décision.
5. Vérifie : `python3 scripts/apply_changeset.py agents/changesets/J5-S2.jsonl agents/changesets/J5-S2-controle.jsonl --dry-run`.
   Tu ne poses **jamais** `"statut": "valide"` (réservé à Alexandre).


## Fiches à contrôler

### 1. Autoconsommation — `autoconsommation`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (26 mots) :
> Consommation sur place de l'électricité produite par sa propre installation, généralement photovoltaïque. Le surplus non consommé est stocké, partagé ou injecté sur le réseau de distribution.

**Définition — après** (26 mots) :
> Consommation sur place de l'électricité produite par sa propre installation, généralement photovoltaïque. Le surplus non consommé peut être réinjecté sur le réseau public de distribution d'électricité.

**Sources après** (à ouvrir une par une) :
- [ADEME — Comment produire de l'électricité chez soi ?](https://agirpourlatransition.ademe.fr/particuliers/amenager-maison/renover/produire-electricite-chez-soi) — type `reference`
- [Enedis (Observatoire) — Autoconsommation](https://observatoire.enedis.fr/autoconsommation) — type `reference`
- [Enedis — Comment fonctionne l'autoconsommation ?](https://www.enedis.fr/faq/autoconsom-mation-produire-et-consommer-son-electricite/comment-fonctionne-lautoconsommation) — type `reference`

**Fiches liées après** : `compteur-linky`, `facture-d-electricite`, `panneau-photovoltaique`, `reseau-de-distribution`, `stockage-d-energie`

```
fiche : autoconsommation
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 2. Borne de recharge — `borne-de-recharge`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (30 mots) :
> Équipement qui délivre l'énergie à un véhicule électrique en dialoguant avec lui pour ajuster le courant. La recharge lente se fait en alternatif, la recharge rapide directement en courant continu.

**Définition — après** (37 mots) :
> Équipement raccordé à une alimentation électrique qui permet de recharger la batterie d'un véhicule électrique. Selon sa puissance, la recharge est dite normale, accélérée ou rapide ; plus la puissance est élevée, plus la recharge est courte.

**Sources après** (à ouvrir une par une) :
- [Ministère de la Transition écologique — Développer les bornes de recharge pour véhicules électriques](https://www.ecologie.gouv.fr/politiques-publiques/developper-bornes-recharge-vehicules-electriques) — type `reference`
- [Enedis — Guide pratique pour recharger sa voiture électrique](https://www.enedis.fr/sites/default/files/documents/pdf/guide-pratique-pour-recharger-sa-voiture-electrique.pdf) — type `reference`

**Fiches liées après** : `batterie-de-traction`, `courant-alternatif`, `courant-continu`, `installation-electrique`, `vehicule-electrique`

```
fiche : borne-de-recharge
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 3. Éco-conception — `eco-conception`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [ADEME — Intégrez l'écoconception dans vos activités industrielles](https://agirpourlatransition.ademe.fr/entreprises/ecoconception) — type `reference`

**Fiches liées après** : `efficacite-energetique`, `empreinte-carbone-de-l-electricite`, `indice-de-reparabilite`, `obsolescence-programmee`, `recyclage-des-dechets-electroniques-deee`, `terres-rares`

```
fiche : eco-conception
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 4. Empreinte carbone de l'électricité — `empreinte-carbone-de-l-electricite`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [RTE — Bilan électrique 2024 : émissions de gaz à effet de serre](https://analysesetdonnees.rte-france.com/bilan-electrique-2024/emissions) — type `reference`

**Fiches liées après** : `eco-conception`, `energie-fossile`, `energie-renouvelable`, `kilowattheure`, `mix-energetique`

```
fiche : empreinte-carbone-de-l-electricite
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 5. Freinage régénératif — `freinage-regeneratif`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (28 mots) :
> Technique qui fait fonctionner le moteur de traction en génératrice lors du ralentissement, renvoyant de l'énergie vers la batterie. Elle augmente l'autonomie et réduit l'usure des freins mécaniques.

**Définition — après** (29 mots) :
> Technique qui fait fonctionner le moteur de traction en génératrice lors du ralentissement, renvoyant l'énergie cinétique vers la batterie sous forme électrique. Les freins mécaniques sont ainsi moins sollicités.

**Sources après** (à ouvrir une par une) :
- [Ministère de la Transition écologique — Vrai-Faux : voitures électriques](https://www.ecologie.gouv.fr/sites/default/files/documents/03102025%20Vrai-Faux%20v%C3%A9hicules%20%C3%A9lectriques%20Vdef_0.pdf) — type `reference`
- [Enedis — Guide pratique pour recharger sa voiture électrique](https://www.enedis.fr/sites/default/files/documents/pdf/guide-pratique-pour-recharger-sa-voiture-electrique.pdf) — type `reference`

**Fiches liées après** : `batterie-de-traction`, `generateur-electrique`, `moteur-electrique`, `supercondensateur`, `vehicule-electrique`

```
fiche : freinage-regeneratif
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 6. Hydrogène — `hydrogene`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [RTE — Hydrogène vert : mythe ou réalité ?](https://www.rte-france.com/bases-electricite/production-electricite/hydrogene-vert-mythe-ou-realite) — type `reference`
- [ADEME — Favorisez les solutions hydrogène renouvelable et bas carbone](https://agirpourlatransition.ademe.fr/collectivites/favorisez-solutions-hydrogene-bas-carbone-renouvelable) — type `reference`

**Fiches liées après** : `electrolyse`, `energie-renouvelable`, `pile-a-combustible`, `stockage-d-energie`

```
fiche : hydrogene
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 7. Indice de réparabilité — `indice-de-reparabilite`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [Ministère de l'Économie — Tout savoir sur l'indice de réparabilité](https://www.economie.gouv.fr/particuliers/mes-droits-conso/bien-consommer/tout-savoir-sur-lindice-de-reparabilite) — type `reference`
- [Ministère de la Transition écologique — Durée de vie des produits](https://www.ecologie.gouv.fr/politiques-publiques/duree-vie-produits) — type `reference`
- [ADEME — Acheter des appareils électriques et électroniques faits pour durer](https://agirpourlatransition.ademe.fr/particuliers/mieux-consommer/electromenager/appareils-electriques-electroniques-durables) — type `reference`

**Fiches liées après** : `composant-electronique`, `eco-conception`, `obsolescence-programmee`, `recyclage-des-dechets-electroniques-deee`

```
fiche : indice-de-reparabilite
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 8. Obsolescence programmée — `obsolescence-programmee`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [Ministère de la Transition écologique — Durée de vie des produits](https://www.ecologie.gouv.fr/politiques-publiques/duree-vie-produits) — type `reference`
- [Ministère de l'Économie — Tout savoir sur l'indice de réparabilité](https://www.economie.gouv.fr/particuliers/mes-droits-conso/bien-consommer/tout-savoir-sur-lindice-de-reparabilite) — type `reference`

**Fiches liées après** : `eco-conception`, `indice-de-reparabilite`, `recyclage-des-dechets-electroniques-deee`

```
fiche : obsolescence-programmee
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 9. Pile à combustible — `pile-a-combustible`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (27 mots) :
> Générateur qui produit de l'électricité par réaction entre l'hydrogène et l'oxygène, en ne rejetant que de l'eau. Elle alimente certains véhicules lourds et des installations de secours.

**Définition — après** (29 mots) :
> Générateur qui produit de l'électricité par réaction entre l'hydrogène et l'oxygène, en dégageant de l'eau et de la chaleur. Elle alimente certains véhicules, notamment lourds, et des sites isolés.

**Version simple — avant** (16 mots) :
> Cette pile fabrique de l'électricité à partir d'hydrogène et d'air, et ne rejette que de l'eau.

**Version simple — après** (20 mots) :
> Cette pile fabrique de l'électricité à partir d'hydrogène et d'air, et rejette seulement de l'eau et un peu de chaleur.

**Sources après** (à ouvrir une par une) :
- [CEA — L'hydrogène (chapitre 5 : la pile à combustible)](https://www.cea.fr/comprendre/Pages/energies/renouvelables/hydrogene.aspx?Type=Chapitre&numero=5) — type `reference`
- [ADEME — Favorisez les solutions hydrogène renouvelable et bas carbone](https://agirpourlatransition.ademe.fr/collectivites/favorisez-solutions-hydrogene-bas-carbone-renouvelable) — type `reference`

**Fiches liées après** : `hydrogene`, `pile-electrique`, `stockage-d-energie`, `vehicule-electrique`

```
fiche : pile-a-combustible
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 10. Station de transfert d'énergie par pompage — `station-de-transfert-d-energie-par-pompage`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (29 mots) :
> Installation qui remonte de l'eau dans un bassin supérieur quand l'électricité est abondante, puis la turbine quand la demande augmente. C'est le principal moyen de stockage à grande échelle.

**Définition — après** (33 mots) :
> Installation qui remonte de l'eau dans un bassin supérieur quand l'électricité est abondante, puis la turbine quand la demande augmente. C'est le moyen de stockage de l'électricité à grande échelle le plus mature.

**Sources après** (à ouvrir une par une) :
- [RTE — Si on pouvait stocker l'électricité à grande échelle ?](https://www.rte-france.com/bases-electricite/systeme-electrique/stocker-electricite-grande-echelle) — type `reference`

**Fiches liées après** : `barrage-hydroelectrique`, `centrale-hydraulique`, `reseau-electrique`, `stockage-d-energie`, `turbine`

```
fiche : station-de-transfert-d-energie-par-pompage
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 11. Terres rares — `terres-rares`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [ADEME — Terres rares, énergies renouvelables et stockage d'énergies](https://librairie.ademe.fr/energies-renouvelables-reseaux-et-stockage/492-terres-rares-energies-renouvelables-et-stockage-d-energies.html) — type `reference`
- [ADEME — Avis : quels leviers pour une transition énergétique robuste face à la dépendance en matériaux ?](https://www.ademe.fr/presse/communique-national/avis-de-lademe-quels-leviers-pour-une-transition-energetique-robuste-face-a-la-dependance-en-materiaux/) — type `reference`

**Fiches liées après** : `composant-electronique`, `eco-conception`, `eolienne`, `moteur-electrique`, `moteur-synchrone`, `recyclage-des-dechets-electroniques-deee`

```
fiche : terres-rares
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 12. Thermostat connecté — `thermostat-connecte`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Sources après** (à ouvrir une par une) :
- [ADEME — Réduire sa facture de chauffage avec un thermostat programmable](https://agirpourlatransition.ademe.fr/particuliers/maison/economies-denergie/reduire-facture-chauffage-thermostat-programmable) — type `reference`

**Fiches liées après** : `capteur-de-temperature`, `domotique`, `economie-d-energie`, `objet-connecte-iot`, `scenario-domotique`

```
fiche : thermostat-connecte
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```

### 13. Véhicule électrique — `vehicule-electrique`

- Niveau scolaire : aucun
- Règles automatiques encore enfreintes : ⚠ « relu-ia » posé par un autre agent que le contrôleur

**Définition — avant** (28 mots) :
> Véhicule propulsé par un moteur électrique alimenté par une batterie de traction rechargeable. Il n'émet aucun polluant à l'usage et récupère une partie de l'énergie lors des freinages.

**Définition — après** (29 mots) :
> Véhicule propulsé par un moteur électrique alimenté par une batterie de traction rechargeable. Il n'émet aucun polluant atmosphérique à l'échappement et récupère une partie de l'énergie lors des freinages.

**Sources après** (à ouvrir une par une) :
- [Ministère de la Transition écologique — Vrai-Faux : voitures électriques](https://www.ecologie.gouv.fr/sites/default/files/documents/03102025%20Vrai-Faux%20v%C3%A9hicules%20%C3%A9lectriques%20Vdef_0.pdf) — type `reference`
- [Enedis — Guide pratique pour recharger sa voiture électrique](https://www.enedis.fr/sites/default/files/documents/pdf/guide-pratique-pour-recharger-sa-voiture-electrique.pdf) — type `reference`

**Fiches liées après** : `batterie-de-traction`, `batterie-lithium-ion`, `borne-de-recharge`, `bus-can`, `freinage-regeneratif`, `moteur-electrique`, `moteur-synchrone`, `pile-a-combustible`

```
fiche : vehicule-electrique
 1 exactitude scientifique         [ ]    7 sécurité 230 V                              [ ]
 2 pas de circularité              [ ]    8 sources ouvertes et précises                [ ]
 3 vocabulaire officiel            [ ]    9 version simple (8-11 ans, exemple, exacte)  [ ]
 4 grandeurs non confondues        [ ]   10 cohérence avec le niveau                    [ ]
 5 format 25-60 mots, texte brut   [ ]   11 unités et symboles                          [ ]
 6 jargon relié (fiche + lien)     [ ]   12 ton neutre, texte original                  [ ]
décision : conforme / refusée (n° des critères)
```
