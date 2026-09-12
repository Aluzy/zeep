/**
 * Liens retour (« backlinks ») du wiki.
 *
 * Le maillage est déclaré dans un seul sens : un article de blog et une fiche projet
 * listent les fiches wiki qu'ils citent (champ `related`). Ce module construit
 * l'index inverse — slug de fiche -> articles et projets qui la citent — prévu au §3
 * du plan de contenu (blocs « Articles de blog liés » et « Projets DIY liés »).
 *
 * Usage : **une seule construction par page au plus**. Sur `wiki/[slug].astro`,
 * l'index est bâti dans `getStaticPaths()` (donc une fois pour les 197 fiches) et
 * chaque page ne reçoit en props que ses propres liens retour.
 *
 * Aucune dépendance : les types d'entrée sont décrits de façon structurelle pour ne pas
 * importer `astro:content` ici. Les entrées de collection Astro s'y conforment.
 */

/** Ce qu'on lit d'un article de blog (collection `blog`, type `content`). */
export interface EntreeArticle {
  /** Slug d'URL de l'article, dérivé du nom de fichier par Astro. */
  slug: string;
  data: { title: string; related?: string[] };
}

/** Ce qu'on lit d'une fiche projet (collection `diy`, type `data`). */
export interface EntreeProjet {
  data: {
    slug: string;
    title: string;
    level: string;
    duration?: string;
    related?: string[];
  };
}

/** Un article qui cite la fiche. */
export interface ArticleLie {
  slug: string;
  titre: string;
}

/** Un projet qui cite la fiche. `duree` vaut "" quand le champ est absent ou blanc. */
export interface ProjetLie {
  slug: string;
  titre: string;
  niveau: string;
  duree: string;
}

/** Liens retour d'une fiche wiki. Les deux listes peuvent être vides. */
export interface LiensRetour {
  articles: ArticleLie[];
  projets: ProjetLie[];
}

/** Index inverse complet : slug de fiche wiki -> ses liens retour. */
export type IndexLiensRetour = Map<string, LiensRetour>;

/** Tri stable et lisible : par titre, insensible à la casse et aux accents. */
function parTitre(a: { titre: string }, b: { titre: string }): number {
  return a.titre.localeCompare(b.titre, "fr");
}

function entree(index: IndexLiensRetour, slug: string): LiensRetour {
  let liens = index.get(slug);
  if (!liens) {
    liens = { articles: [], projets: [] };
    index.set(slug, liens);
  }
  return liens;
}

/**
 * Construit l'index inverse à partir des collections `blog` et `diy`.
 *
 * `slugsWiki` est la liste des slugs de fiches existantes : un `related` qui n'y
 * figure pas fait **échouer le build** avec le même message que les gabarits de
 * l'article et du projet — jamais de lien silencieusement ignoré (AGENTS.md §4).
 */
export function buildBacklinkIndex(
  articles: EntreeArticle[],
  projets: EntreeProjet[],
  slugsWiki: Iterable<string>
): IndexLiensRetour {
  const connus = new Set(slugsWiki);
  const index: IndexLiensRetour = new Map();

  for (const a of articles) {
    const vus = new Set<string>();
    for (const cible of a.data.related || []) {
      if (!connus.has(cible)) {
        throw new Error(
          `Fiche wiki introuvable « ${cible} » référencée par l'article de blog ${a.slug}`
        );
      }
      if (vus.has(cible)) continue;
      vus.add(cible);
      entree(index, cible).articles.push({ slug: a.slug, titre: a.data.title });
    }
  }

  for (const p of projets) {
    const vus = new Set<string>();
    for (const cible of p.data.related || []) {
      if (!connus.has(cible)) {
        throw new Error(
          `Fiche wiki introuvable « ${cible} » référencée par le projet DIY ${p.data.slug}`
        );
      }
      if (vus.has(cible)) continue;
      vus.add(cible);
      entree(index, cible).projets.push({
        slug: p.data.slug,
        titre: p.data.title,
        niveau: p.data.level,
        duree: (p.data.duration || "").trim(),
      });
    }
  }

  for (const liens of index.values()) {
    liens.articles.sort(parTitre);
    liens.projets.sort(parTitre);
  }
  return index;
}

/**
 * Liens retour d'une fiche. Renvoie toujours un objet : une fiche que personne ne
 * cite (la majorité des 197) reçoit deux listes vides, et les blocs restent masqués.
 */
export function liensRetourDe(index: IndexLiensRetour, slug: string): LiensRetour {
  return index.get(slug) || { articles: [], projets: [] };
}
