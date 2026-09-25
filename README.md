# Zeep — wiki pédagogique électricité/électronique

Zeep réunit un **wiki** de notions reliées entre elles, un **blog** et des
**projets DIY** sur l'électricité et l'électronique, en français. Le public
prioritaire est **scolaire** : élèves du CE1 à la terminale, parents et
enseignants.

Chaque fiche du wiki donne une définition de référence et renvoie vers les
notions voisines. Ce dépôt est la **source de vérité** du contenu (le Google
Sheet n'en est qu'un export de consultation).

Le site est construit avec [Astro](https://astro.build) 4 (site statique) et
publié sur **GitHub Pages** : `https://aluzy.github.io/zeep/`.

## Structure du dépôt

```
AGENTS.md                  Règles de travail (humains et agents IA) : à lire avant toute modification
src/content/wiki/*.json    Fiches wiki, une par notion (nom du fichier = slug)
src/content/blog/*.md      Articles de blog (Markdown, frontmatter related = slugs du wiki)
src/content/diy/*.json     Projets DIY (étapes, matériel, vidéos, notions liées)
src/content/config.ts      Schémas des collections Astro
src/data/taxonomy.json     Domaines de classement des fiches
src/layouts/Base.astro     Gabarit commun (en-tête, navigation, pied de page)
src/pages/                 Routes du site (accueil, wiki, blog, projets DIY)
src/lib/                   Fonctions utilitaires (domaines, vidéos…)
public/assets/style.css    Système de design
public/assets/site.js      Recherche et filtre par domaine sur l'index du wiki
scripts/                   Outils Python (bibliothèque standard uniquement) : validation, changesets, renommage, tests
agents/changesets/         Changesets de contenu wiki (JSONL), appliqués par l'intégrateur
agents/rapports/           Rapports de lot (modèle : TEMPLATE.md)
.github/workflows/deploy.yml   Validation, construction, test de fumée et déploiement
```

## Développement local

```bash
npm install
npm run dev       # site en local sur http://localhost:4321/zeep/
npm run build     # génère dist/
```

## Intégration continue

Sur **toutes les branches** et pull requests, GitHub Actions valide le contenu
(`scripts/validate_content.py`, dont le cliquet de dette éditoriale), audite la couverture, construit le site puis lance le test de fumée
(`scripts/smoke_dist.py`). La mise en ligne sur GitHub Pages n'a lieu que
depuis `main`, si tout est vert.

## Contribuer

Les règles de travail, éditoriales et techniques sont dans
**[AGENTS.md](AGENTS.md)** : elles s'imposent à toute contribution, humaine ou IA.
En résumé :

- les fiches wiki ne sont **pas modifiées à la main** : on écrit un changeset
  `agents/changesets/<LOT>.jsonl` (format décrit en tête de `scripts/apply_changeset.py`) ;
- une fiche n'est renommée ou supprimée que sur décision explicite (cela casse son URL) ;
- slugs : `scripts/zeeplib.py::slugify` (apostrophes et espaces → tirets : `loi-d-ohm`).

Scripts utiles (à lancer depuis la racine du dépôt) :

```bash
python3 scripts/validate_content.py [--stats]                         # garde-fou du contenu : doit afficher 0 erreur
python3 scripts/dette.py [--detail REGLE | --indicateurs | --abaisser]    # dette éditoriale (cliquet, voir AGENTS.md §3 ter)
python3 agents/outils/mapping_niveau.py --verifier                     # table des niveaux scolaires (--lot <LOT> : changeset)
python3 scripts/apply_changeset.py agents/changesets/<LOT>.jsonl --dry-run   # vérifie puis applique un changeset
python3 scripts/rename_slug.py <ancien-slug> [--term "Nouveau terme"] --dry-run  # renomme une fiche et ses références
python3 scripts/smoke_dist.py --base /zeep                            # test de fumée du site construit (après npm run build)
python3 scripts/export_glossaire.py glossaire.csv                     # export tableur du glossaire
```

(Retirer `--dry-run` pour appliquer réellement un changeset ou un renommage.)

## Chantiers ouverts

- [ ] Niveau scolaire et version simple sur les fiches (notions vues avant le lycée)
- [ ] Illustrations des fiches
- [ ] Vidéos et liens d'achat des projets DIY (non affichés tant qu'ils ne sont pas renseignés)
- [ ] Panneau de contrôle (Decap CMS), qui nécessite une petite passerelle OAuth GitHub
