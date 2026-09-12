# AGENTS.md — règles pour les agents IA qui travaillent sur Zeep

Ce fichier s'impose à tout agent (humain ou IA) qui modifie ce dépôt.
Le plan d'ensemble et les fiches de mission vivent dans le projet claude.ai
« Base de connaissance – wiki élec », dossier `workflow-agents/`.

## 1. Le projet en 5 lignes

- Zeep est un wiki + blog + projets DIY sur l'électricité et l'électronique, en français.
- **Public prioritaire de la v1 : scolaire** (élèves du CE1 à la terminale, parents, enseignants).
- Une fiche = une définition de référence (niveau lycée/adulte) + un **niveau scolaire**
  (où la notion apparaît dans les programmes) + une **version simple** pour les notions vues avant le lycée.
- **Ce dépôt est la source de vérité** du contenu. Le Google Sheet n'est qu'un export de consultation.
- Site Astro 4 statique, déployé sur GitHub Pages (`https://aluzy.github.io/zeep/`).

## 2. Règles de travail

1. **Un lot = une mission** décrite dans sa fiche. Ne rien faire hors du périmètre du lot ; signaler le reste dans le rapport.
2. **Contenu wiki : jamais d'édition manuelle des JSON.** Écrire un changeset `agents/changesets/<LOT>.jsonl`
   (format documenté dans `scripts/apply_changeset.py`) ; l'intégrateur l'applique. Exception : les lots « site » peuvent
   modifier le code, les gabarits, le blog et les projets DIY directement.
3. **Avant de rendre** : `python3 scripts/apply_changeset.py <changeset> --dry-run` (lots de contenu), puis
   `python3 scripts/validate_content.py` doit afficher **0 erreur** une fois le changeset appliqué sur une copie de travail.
4. **Pas de `npm install` possible dans l'environnement des agents** (registre bloqué) : le build Astro est vérifié par la CI
   GitHub. Écrire du code Astro/TypeScript prudent, sans nouvelle dépendance, et le relire deux fois.
5. **Ne jamais renommer ni supprimer une fiche** sans que la mission le demande explicitement (casse les URLs).
6. **Un rapport par lot** : `agents/rapports/<LOT>.md` selon `agents/rapports/TEMPLATE.md`.
7. **Commits** : petits, en français, préfixés par le lot : `J1-L2: corrige les slugs du blog`.

## 3. Règles éditoriales (lots de contenu)

- **Exactitude avant tout.** Aucune affirmation sans être sûr ; en cas de doute, ne pas écrire et le signaler dans le rapport.
- **Vocabulaire officiel des programmes** (voir la matrice curriculaire) : « tension » et non « voltage »,
  « intensité » et non « ampérage » ; les usages courants sont mentionnés comme tels.
- **Ne pas confondre électricité et énergie**, courant et tension, puissance et énergie.
- **Définition de référence** : 1 à 3 phrases, 25 à 60 mots, sans définir un mot par lui-même, sans jargon non défini
  (sinon créer le lien vers la fiche qui le définit).
- **Version simple** (notions vues avant le lycée) : 1 à 2 phrases, 12 à 35 mots, vocabulaire d'un élève de 8-11 ans,
  un exemple du quotidien, aucune formule. Toujours exacte : simplifier n'autorise pas l'erreur.
- **Sécurité** : toute fiche touchant au secteur 230 V rappelle qu'on n'y manipule pas soi-même.
- **Sources** : chaque fiche créée ou réécrite porte au moins une source dans `sources`
  (`{"titre": "...", "url": "...", "type": "programme|reference|norme|manuel"}`). Priorité : textes officiels (BO, Éduscol,
  Légifrance), organismes de référence (INRS, RTE, Enedis, CRE), puis ouvrages. Jamais Wikipédia comme source unique.
- **Droit d'auteur** : reformuler ; au plus une citation courte (< 15 mots) entre guillemets par source.
- **Relecture** : une fiche relue par un agent contrôleur reçoit `"relecture": {"date": "AAAA-MM-JJ", "par": "agent-controleur", "statut": "relu-ia"}`.
  Seul Alexandre peut poser `"statut": "valide"`.

## 4. Conventions techniques

- Slugs : `scripts/zeeplib.py::slugify` (apostrophes et espaces -> tirets : `loi-d-ohm`).
- Liens wiki toujours réciproques (le changeset s'en charge).
- Schéma des collections : `src/content/config.ts` et `scripts/validate_content.py` doivent rester synchronisés.
- Les liens entre contenus sont des slugs (chaînes). Deux filets les protègent : `validate_content.py`, qui tourne en CI
  avant le build, et les gabarits, qui lèvent une erreur explicite au build si un slug est introuvable (jamais de lien
  silencieusement ignoré). Migrer vers `reference()` d'Astro reste possible plus tard, mais n'est pas requis.
- Champs de fiche ajoutés le 12/09 (renseignés progressivement) : `niveau` (première apparition dans les programmes),
  `versionSimple`, `sources`, `relecture`. Ils sont déclarés dans `src/content/config.ts` et validés par le script.
