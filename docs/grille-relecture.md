# Grille de relecture des fiches wiki

Document de travail des agents relecteurs. Il complète `AGENTS.md` §3 (règles éditoriales)
et sert de consigne unique pour la relecture des 197 fiches (Jour 3, 4 agents en parallèle).

Une fiche est **relue** quand les 12 critères ci-dessous ont été passés un par un.
Un seul critère en échec suffit à refuser la fiche : on la corrige, ou on la signale
si la correction demande une décision humaine.

---

## Mode d'emploi (à lire avant de commencer)

1. **Périmètre.** Chaque agent reçoit un lot de fiches (ordre alphabétique des slugs).
   On ne relit que ses fiches ; une erreur vue dans la fiche d'un autre se signale dans le rapport,
   on n'y touche pas (deux agents qui modifient la même fiche = conflit de changeset).
2. **Aucune édition manuelle des JSON.** Toute correction passe par une ligne de changeset
   `agents/changesets/<LOT>.jsonl` (`{"op":"set","slug":…,"field":"definition","old":"<valeur exacte actuelle>","new":…,"why":…}`).
   Le champ `old` doit être recopié à l'identique depuis le fichier, sinon l'application échoue.
3. **Vérifier avant d'écrire.** Une affirmation qu'on ne sait pas sourcer ne s'écrit pas :
   on garde l'ancienne formulation et on inscrit le doute dans le rapport. L'exactitude prime sur la complétude.
4. **Ouvrir chaque URL de source** avant de la citer. Une URL qui ne répond pas, qui ne mène pas
   au document annoncé ou qui n'appuie pas l'affirmation est remplacée, pas conservée.
5. **Marquer la fiche relue** : `{"op":"set", …,"field":"relecture","new":{"date":"AAAA-MM-JJ","par":"agent-<LOT>","statut":"relu-ia"}}`.
   Le statut `valide` est réservé à Alexandre : ne jamais le poser.
6. **Avant de rendre** : `python3 scripts/apply_changeset.py <changeset> --dry-run` doit passer,
   puis `python3 scripts/validate_content.py` doit afficher 0 erreur une fois le changeset appliqué sur une copie de travail.

**Gravité à indiquer dans le rapport**

| Gravité | Quand | Traitement |
|---|---|---|
| **Haute** | Erreur factuelle, confusion de grandeurs, conseil dangereux, sécurité absente sur du 230 V | Correction dans le lot, obligatoire |
| **Moyenne** | Formulation imprécise ou ambiguë, vocabulaire non officiel, circularité, longueur, lien manquant | Correction dans le lot si elle ne demande aucun arbitrage |
| **Basse** | Style, redondance, enrichissement souhaitable | Signalement dans le rapport, pas de correction |

---

## Les 12 critères

### 1. Exactitude scientifique

**Question de contrôle** — Chaque affirmation de la fiche est-elle exacte, et pourrais-je la retrouver
telle quelle dans un texte officiel, une norme, une fiche constructeur ou un ouvrage de référence ?

- ✅ **Conforme** — `induction-electromagnetique` : « Phénomène par lequel un champ magnétique variable
  produit une tension électrique dans un conducteur électrique, principe utilisé par l'alternateur et le transformateur. »
  Le mécanisme est juste et chaque terme est à sa place.
- ❌ **Non conforme** — `impedance` : « Grandeur qui caractérise l'opposition d'un circuit électronique au passage
  d'un signal analogique, **combinant résistance, condensateur et bobine**. » L'impédance combine des *grandeurs*
  (résistance et réactances), pas des *composants*, et elle s'oppose au passage d'un courant alternatif,
  pas d'un « signal analogique ».

### 2. Pas de circularité

**Question de contrôle** — Le mot défini (ou un mot de la même famille) sert-il à se définir lui-même ?
La fiche apprend-elle quelque chose à quelqu'un qui ne connaît pas le terme ?

- ✅ **Conforme** — `intensite-electrique` : « Quantité de charge électrique traversant un conducteur électrique
  par unité de temps, mesurée en ampères à l'aide d'un ampèremètre. » Aucun renvoi à « intensité ».
- ❌ **Non conforme** — `conductivite-electrique` : « …inverse de la résistivité » et `resistivite` :
  « …inverse de la conductivité électrique ». Les deux fiches se renvoient l'une à l'autre :
  le lecteur qui ignore les deux mots n'apprend rien.

### 3. Vocabulaire officiel des programmes

**Question de contrôle** — La fiche emploie-t-elle **tension**, **intensité du courant**, **puissance**, **énergie**,
et non *voltage*, *ampérage*, *consommation en volts* ? Quand un usage courant est mentionné, est-il présenté
comme tel, avec le terme officiel à employer en classe ?

- ✅ **Conforme** — `voltage` (réécrite J1-L3) : « Mot de la langue courante employé pour désigner la tension électrique […]
  les programmes scolaires parlent de "tension" : c'est ce terme officiel qu'il faut employer en classe et dans un devoir. »
- ❌ **Non conforme** — `voltage` (version d'origine) : « Terme usuel désignant la tension électrique d'une installation
  ou d'un appareil, exprimée en volts. » Le mot est donné comme un simple synonyme : un élève qui l'emploie dans un devoir sera corrigé.

### 4. Grandeurs non confondues

**Question de contrôle** — La fiche distingue-t-elle **électricité** (les phénomènes) et **énergie** ;
**courant** (déplacement de charges, en ampères) et **tension** (différence de potentiel, en volts) ;
**puissance** (watts) et **énergie** (wattheures ou joules) ? Un générateur y convertit-il de l'énergie
plutôt que de « produire du courant » ?

- ✅ **Conforme** — `moteur-electrique` : « Machine qui convertit l'énergie électrique en énergie mécanique,
  fonctionnant à l'inverse d'un générateur électrique. »
- ❌ **Non conforme** — `alternateur` : « Machine électrique qui convertit **l'énergie mécanique en courant alternatif** ».
  On convertit une énergie en une autre énergie ; le courant alternatif n'est pas une forme d'énergie,
  c'est la forme sous laquelle l'énergie électrique est fournie. Même défaut dans `alimentation-electrique`
  (« Fourniture de courant électrique ») et `production-delectricite` (« générer du courant électrique »).

### 5. Format de la définition de référence

**Question de contrôle** — 1 à 3 phrases, **25 à 60 mots**, du texte brut (aucune balise HTML, aucun gras,
aucune liste, aucun titre), une seule définition et non deux versions juxtaposées ?

- ✅ **Conforme** — `microcontroleur` (28 mots, 1 phrase) : « Circuit intégré combinant un processeur, une mémoire vive,
  une mémoire morte et des entrées-sorties, utilisé pour piloter un objet connecté ou un système embarqué comme une carte Arduino. »
- ❌ **Non conforme** — `court-circuit` : « `<strong>`Vu côté électricité :`</strong>` … `<br><br>` `<strong>`Vu côté électronique :`</strong>` … »
  Balises HTML dans un champ de données et deux définitions dans une seule fiche. Mêmes cas : `domotique`, `redresseur`.
  À l'inverse, `phase-electrique` (13 mots) est trop courte pour être utile.
  *Repère de lot : 184 fiches sur 197 sont actuellement sous les 25 mots (moyenne 19,4).*

### 6. Aucun terme technique laissé sans porte de sortie

**Question de contrôle** — Chaque terme technique employé dans la définition a-t-il sa propre fiche,
et le lien figure-t-il bien dans `related` ? Sinon : soit on le relie (`{"op":"link", …}`),
soit on l'explique en trois mots, soit on le retire.

- ✅ **Conforme** — `induction-electromagnetique` mentionne champ magnétique, conducteur électrique, tension électrique,
  alternateur et transformateur : les cinq fiches existent et les cinq liens sont dans `related`.
- ❌ **Non conforme** — `condensateur` : « stocke une **charge électrique** entre deux armatures, utilisé notamment
  dans les **filtres électroniques** ». Les fiches `charge-electrique` et `filtre-electronique` existent,
  mais aucune des deux n'est liée. *Repère de lot : au moins 34 fiches citent un terme dont la fiche existe sans la relier
  (décompte strict, sur le terme exact ; le nombre réel est plus élevé).*

### 7. Sécurité dès que le 230 V est en jeu

**Question de contrôle** — La fiche touche-t-elle au secteur (230 V, prise, tableau, phase, neutre, installation,
câblage, court-circuit, variateur) ? Si oui, dit-elle explicitement qu'on n'intervient pas soi-même ?
La fiche ne donne-t-elle jamais un mode opératoire qui inviterait un élève à manipuler le secteur ?

- ✅ **Conforme** — `triac` (réécrite J1-L3) : « Ces montages étant souvent reliés au secteur 230 V, on n'y intervient pas soi-même. »
- ❌ **Non conforme** — `phase-electrique` : « Conducteur actif d'un circuit électrique transportant le courant électrique,
  par opposition au neutre. » C'est le conducteur sous tension d'une prise domestique et la fiche ne comporte aucun avertissement.
  Même manque dans `neutre`, `prise-de-courant`, `tableau-electrique`, `cablage-electrique`.

### 8. Sources vérifiées

**Question de contrôle** — La fiche créée ou réécrite porte-t-elle au moins une source
`{"titre": …, "url": …, "type": "programme|reference|norme|manuel"}` ? Ai-je **ouvert** chaque URL ?
Le titre correspond-il au titre réel du document ? La source appuie-t-elle vraiment l'affirmation ?
Priorité : BO / Éduscol / Légifrance, puis INRS, RTE, Enedis, CRE, normes, fiches constructeur, ouvrages.
Wikipédia n'est jamais la source unique.

- ✅ **Conforme** — `electricite` (réécrite J1-L3) : programme de physique-chimie de première générale
  (« en évitant soigneusement toute confusion entre les concepts d'électricité et d'énergie »),
  complété par l'Académie française et le Larousse.
- ❌ **Non conforme** — une entrée « Wikipédia, article *Triac* » seule ; une URL recopiée de mémoire sans l'ouvrir ;
  un titre approximatif (« cours d'électronique de puissance ») alors que le document est une annexe précise
  (« *Cours d'électronique de puissance*, IUT GEII de Tours, annexe "Gradateur à triac" »).

### 9. Version simple (notions vues avant le lycée)

**Question de contrôle** — 1 à 2 phrases, **12 à 35 mots**, vocabulaire d'un élève de 8-11 ans,
**un exemple du quotidien**, **aucune formule**, aucun symbole d'unité non expliqué —
et surtout : exacte. Simplifier n'autorise pas l'erreur.
*Aucune fiche ne porte encore de `versionSimple` (champ créé au Jour 2) : l'exemple conforme ci-dessous
est un modèle rédigé, pas un extrait du dépôt.*

- ✅ **Conforme** — `interrupteur` : « Un interrupteur ouvre ou ferme le chemin du courant. Quand tu appuies
  sur celui du mur, la lampe du plafond s'allume ou s'éteint. » (26 mots, un exemple, aucune formule)
- ❌ **Non conforme** — « L'interrupteur commande la fermeture du circuit, ce qui autorise le passage d'un courant
  d'intensité I = U/R. » (formule, jargon, aucun exemple) — et tout aussi refusé :
  « L'électricité, c'est quand ça bouge dans les fils » (faux, donc inutilisable même pour les petits).

### 10. Cohérence avec le niveau scolaire

**Question de contrôle** — Le champ `niveau` correspond-il à la **première apparition** de la notion dans les programmes
(matrice curriculaire) ? La définition n'utilise-t-elle pas des notions enseignées plus tard que ce niveau ?
Toute notion vue avant le lycée a-t-elle une `versionSimple` ?

- ✅ **Conforme** — `circuit-electrique` : notion de cycle 3/4, définie sans aucune grandeur ni formule
  (« Ensemble de composants reliés par des conducteurs électriques formant un chemin fermé… »).
- ❌ **Non conforme** — définir `fusible` (cycle 4) en s'appuyant sur l'impédance ou l'effet Joule volumique ;
  ou marquer `impedance` comme notion de cycle 4 alors qu'elle relève du lycée ; ou laisser
  une fiche de cycle 2-3 (`interrupteur`, `pile-electrique`) sans version simple.

### 11. Unités, symboles et ordres de grandeur

**Question de contrôle** — Les unités et symboles du Système international sont-ils corrects et bien écrits
(A, V, Ω, W, Wh, Hz, espace entre le nombre et l'unité) ? N'a-t-on pas inventé une unité « électrique »
là où l'unité est générale ? Les valeurs citées (230 V, 50 Hz) sont-elles exactes ?

- ✅ **Conforme** — `frequence-electrique` : « Nombre de cycles par seconde d'un courant alternatif,
  exprimé en hertz, généralement 50 Hz sur le réseau électrique français. »
- ❌ **Non conforme** — `kilowatt` : « Unité de **puissance électrique** équivalente à 1000 watts ».
  Le watt est l'unité de puissance quelle que soit la forme d'énergie ; la restreindre à l'électricité
  entretient exactement la confusion que le programme demande d'éviter. Même défaut dans `watt`.

### 12. Ton neutre, texte original, pas de publicité

**Question de contrôle** — Le texte est-il reformulé (jamais un copier-coller) ? Compte-t-il au plus
une citation courte (moins de 15 mots) entre guillemets par source ? Est-il neutre — ni marque,
ni conseil d'achat, ni superlatif invérifiable ?

- ✅ **Conforme** — `semi-conducteur` : « Matériau, comme le silicium, dont la conductivité électrique intermédiaire
  permet de fabriquer des diodes, des transistors et des circuits intégrés. »
- ❌ **Non conforme** — `ampoule-led` : « **réputée pour** sa faible consommation électrique et sa longue durée de vie ».
  « Réputée pour » n'est ni vérifiable ni neutre : écrire ce qui est mesurable (efficacité lumineuse en lumens par watt,
  durée de vie annoncée par le fabricant) ou ne rien écrire.

---

## Aide-mémoire à recopier dans le rapport de lot

```
fiche : <slug>
1 exactitude          [ ]      7 sécurité 230 V        [ ]
2 non-circularité     [ ]      8 sources vérifiées     [ ]
3 vocabulaire officiel[ ]      9 version simple        [ ]
4 grandeurs distinctes[ ]     10 niveau scolaire       [ ]
5 format 25-60 mots   [ ]     11 unités et symboles    [ ]
6 jargon relié        [ ]     12 ton neutre            [ ]
décision : conforme / corrigée (n° des critères) / signalée (raison)
```

## En cas de doute

- **Doute scientifique** : ne pas écrire, garder l'ancienne définition, inscrire la fiche dans
  « Points d'attention » du rapport avec la question précise à trancher.
- **Renommage ou suppression de fiche** (`court-jus-panne-de-courant`, doublons `processeur-cpu` / `microprocesseur`) :
  interdit par changeset, casse les URLs — signalement au rapport uniquement.
- **Fiche manifestement hors périmètre du glossaire** ou notion absente : signalement, pas de création
  sauf si la mission du lot le demande.
