---
# En-tête ajouté a posteriori (J4-CHAINE, 25/09/2026) : le rapport d'origine n'en avait pas.
lot: chantier-A-6
titre: "Liens contextuels dans les définitions du wiki"
date: 2026-09-13
statut: termine
redacteur: agent-site
controleur: aucun
changesets: []
fiches_creees: []
fiches_modifiees: []
lacunes: []
decisions_humaines: []
---
# Rapport de lot chantier A (étape 6) — Liens contextuels dans les définitions du wiki

- **Agent** : IA (site)
- **Date** : 2026-09-13
- **Statut** : terminé (build Astro non vérifiable localement, cf. « Vérifications effectuées »)

## Ce qui a été fait

- Nouveau module `src/lib/definition-links.ts` : repère dans le texte d'une définition les mots
  qui désignent une notion traitée par un article de blog, et renvoie la définition enrichie de
  liens. Les fiches JSON ne sont pas touchées : tout se fait au rendu, sur une copie de la chaîne.
- `src/lib/backlinks.ts` : un seul ajout, le champ `rang` sur `ArticleLie` (position de la fiche
  dans le `related` de l'article). Le calcul « quels articles citent quelle fiche » n'est pas
  refait ailleurs — le module ci-dessus part de l'index inverse existant.
- `src/pages/wiki/[slug].astro` : le vocabulaire liable est bâti une seule fois dans
  `getStaticPaths()` (à côté de l'index des liens retour) ; chaque fiche reçoit sa définition
  enrichie en prop. Les blocs de bas de page sont inchangés.
- `public/assets/style.css` : classe `.def-lien` — pointillé discret au repos, surlignage
  (`--accent-dim` + `--accent`) au survol **et** au focus clavier, contour `:focus-visible`,
  transition neutralisée sous `prefers-reduced-motion`.

## Stratégie de correspondance

1. **Vocabulaire** : les fiches citées par au moins un article. La fiche courante est exclue
   (le bloc « Articles qui en parlent » la couvre déjà).
2. **Article cible** quand plusieurs articles traitent la notion : rang le plus bas dans le
   `related` (0 = sujet de l'article), départage par titre. Déterministe d'un build à l'autre.
3. **Normalisation** : NFD sans diacritiques, minuscules, apostrophes et tirets traités comme
   des séparateurs de mots.
4. **Comparaison par suites de mots**, jamais par sous-chaîne : impossible de surligner
   l'intérieur d'un mot. Deux mots d'un même terme doivent être séparés seulement par une
   espace, un tiret ou une apostrophe — pas par une virgule.
5. **Pluriels** : radical tolérant (`s`/`x` final, `-al ↔ -aux`, `-ail ↔ -aux`) sur les mots
   d'au moins 4 caractères.
6. **Terme contenu dans un autre** : balayage de gauche à droite, correspondance la plus longue
   d'abord ; le passage reconnu est consommé qu'il soit lié ou non, donc jamais de repli sur un
   terme plus court à l'intérieur d'un terme plus long, et jamais deux liens sur le même passage.
   Un seul lien par notion et par définition.
7. **Doute → pas de lien** : formes normalisées en collision entre deux fiches, mots isolés de
   moins de 4 caractères, et **formes tronquées** — « Résistance » commence aussi
   « Résistance électrique », deux notions distinctes, donc le mot seul n'est pas lié.
8. **HTML des définitions** (trois fiches contiennent `<strong>`/`<br>`) : découpage en segments
   balise/texte, recherche uniquement dans le texte, jamais à cheval sur une balise. Le texte
   d'origine est réémis verbatim ; seuls les attributs fabriqués (`href`, `title`) sont échappés.
   Si une définition contenait un jour un `<a>`, elle est rendue telle quelle (pas de lien imbriqué).

## Fichiers produits

- `src/lib/definition-links.ts` (nouveau), `src/lib/backlinks.ts`, `src/pages/wiki/[slug].astro`,
  `public/assets/style.css`, ce rapport. Aucun changeset : pas de modification de contenu.

## Critères d'acceptation

| Critère | Résultat |
|---|---|
| Mots de la définition cliquables vers les articles | ✅ 121 liens sur 88 des 207 fiches |
| Champ `definition` des JSON inchangé | ✅ vérifié par invariant : définition enrichie moins les `<a>` = définition d'origine, sur les 207 fiches |
| Accents, casse, pluriels | ✅ `signaux/signal`, `piles/pile`, `Énergie/énergies` |
| Terme contenu dans un autre | ✅ « courant continu » l'emporte sur « courant » ; « batterie lithium-ion » sur « batterie » |
| Jamais deux fois le même passage | ✅ passage consommé + un lien par notion et par définition |
| Doute → pas de lien | ✅ « Résistance » et « Batterie » retirés par la règle des formes tronquées |
| Survol **et** focus clavier | ✅ `.def-lien:hover, .def-lien:focus-visible` + `outline` au focus |
| Bloc de bas de page conservé | ✅ inchangé |

## Vérifications effectuées

- `python3 scripts/validate_content.py --stats` : **0 erreur**, 6 avertissements préexistants
  (articles courts / sans source, hors périmètre du lot).
- Module testé hors Astro avec `node --experimental-strip-types` sur les 207 fiches réelles :
  invariant de non-altération du texte, relecture des 121 liens dans leur contexte.
- `npm install` impossible dans l'environnement de l'agent (registre npm hors liste d'autorisation),
  donc `npm run build` et `scripts/smoke_dist.py --base /zeep` sont vérifiés par la CI GitHub
  sur la branche / la pull request (AGENTS.md §2.4).

## Points d'attention pour la relecture humaine

- Le choix de l'article quand plusieurs traitent la notion se joue au rang dans `related` :
  « courant continu » pointe vers l'article panneau photovoltaïque (rang 1, à égalité avec
  l'article onduleur, départagé par titre). Si un article doit primer, il suffit de remonter le
  slug dans son `related`.
- Le vocabulaire liable ne compte que 31 termes aujourd'hui, faute d'articles. Il grossira tout
  seul à chaque nouvel article, sans code à toucher — mais chaque nouvel article élargit aussi
  la surface de faux positifs : à surveiller sur les termes très courants.

## Hors périmètre repéré (à planifier)

- Les mêmes liens seraient pertinents dans la « version simple » des fiches et dans les
  définitions affichées sur `wiki/index.astro`.
- « Résistance » et « Batterie » restent non liés faute de pouvoir lever l'ambiguïté au rendu ;
  un champ « synonymes / formes liables » dans les fiches permettrait de trancher au contenu.
