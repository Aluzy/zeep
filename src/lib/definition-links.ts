/**
 * Liens contextuels dans la définition d'une fiche wiki.
 *
 * Certains mots de la définition désignent une notion dont un article de blog
 * parle : ils deviennent cliquables vers cet article (surlignés au survol et au
 * focus clavier). Le calcul « quels articles citent quelle fiche » n'est pas
 * refait ici : on part de l'index inverse de `backlinks.ts`.
 *
 * Le champ `definition` des fiches JSON n'est **jamais** modifié : tout se fait
 * au rendu, sur une copie de la chaîne.
 *
 * Règle directrice : en cas de doute, on ne lie pas. Un faux lien coûte plus
 * cher qu'un lien manquant, surtout pour un public scolaire.
 *
 * Usage : construire le vocabulaire **une seule fois** par build (dans
 * `getStaticPaths()`), puis appeler `enrichirDefinition` pour chaque fiche.
 */

import type { IndexLiensRetour } from "./backlinks";

/** Ce qu'on lit d'une fiche wiki (collection `wiki`, type `data`). */
export interface EntreeFiche {
  data: { slug: string; term: string };
}

/** Notion reconnaissable dans un texte, et l'article vers lequel elle pointe. */
export interface TermeLiable {
  /** Slug de la fiche wiki désignée (sert aussi à ne pas s'auto-lier). */
  slug: string;
  /** Terme d'origine, pour les libellés de survol. */
  terme: string;
  /** Article retenu quand plusieurs parlent de la notion. */
  article: { slug: string; titre: string };
}

/**
 * Vocabulaire indexé par forme normalisée (« radicaux » séparés par une espace),
 * plus la longueur maximale d'un terme en mots, pour le balayage.
 */
export interface Vocabulaire {
  parForme: Map<string, TermeLiable>;
  motsMax: number;
}

/** Longueur minimale d'un terme d'un seul mot : en dessous, trop de faux positifs. */
const LONGUEUR_MOT_MIN = 4;

/** Un mot = lettres et chiffres. Les apostrophes et tirets séparent les mots. */
const MOT = /[\p{L}\p{N}]+/gu;

/** Entre deux mots d'un même terme, seuls ces caractères sont tolérés. */
const LIAISON = /^[\s\-‐-―'’]+$/;

/** Minuscules sans accents ni cédille. */
function sansAccents(mot: string): string {
  return mot.normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase();
}

/**
 * Radical tolérant au pluriel : « signaux » et « signal », « piles » et « pile »
 * donnent la même forme. Les mots courts sont laissés tels quels (« gaz », « axe »).
 */
export function radical(mot: string): string {
  const m = sansAccents(mot);
  if (m.length < LONGUEUR_MOT_MIN) return m;
  if (m.endsWith("aux")) return m.slice(0, -3) + "al"; // signaux -> signal, travaux -> traval
  if (m.endsWith("ail")) return m.slice(0, -3) + "al"; // travail -> traval
  if (m.endsWith("s") || m.endsWith("x")) return m.slice(0, -1);
  return m;
}

/** Un mot repéré dans un texte, avec ses bornes dans la chaîne d'origine. */
interface Mot {
  radical: string;
  debut: number;
  fin: number;
}

function decouperMots(texte: string): Mot[] {
  const mots: Mot[] = [];
  MOT.lastIndex = 0;
  let m: RegExpExecArray | null;
  while ((m = MOT.exec(texte)) !== null) {
    mots.push({ radical: radical(m[0]), debut: m.index, fin: m.index + m[0].length });
  }
  return mots;
}

/** Forme normalisée d'un terme : « Loi d'Ohm » -> « loi d ohm ». */
function formeDe(terme: string): { forme: string; mots: number } {
  const mots = decouperMots(terme).map((x) => x.radical);
  return { forme: mots.join(" "), mots: mots.length };
}

/**
 * Construit le vocabulaire liable : les fiches wiki citées par au moins un
 * article de blog. Un terme ambigu (deux fiches qui se normalisent pareil) est
 * retiré des deux côtés plutôt que d'être attribué au hasard.
 */
export function buildVocabulaireDefinitions(
  fiches: EntreeFiche[],
  backlinks: IndexLiensRetour
): Vocabulaire {
  const parForme = new Map<string, TermeLiable>();
  const ambigues = new Set<string>();
  let motsMax = 0;

  // Formes tronquées : « Résistance » commence aussi « Résistance électrique »,
  // deux notions distinctes (le composant, la grandeur). Le mot seul, dans une
  // phrase, peut désigner l'une ou l'autre : on ne le lie pas. Comparaison sur
  // toutes les fiches, pas seulement celles qui ont un article.
  const prefixes = new Set<string>();
  const formes = fiches.map((f) => ({ slug: f.data.slug, ...formeDe(f.data.term) }));
  for (const a of formes) {
    if (!a.forme) continue;
    for (const b of formes) {
      if (a.slug === b.slug || b.mots <= a.mots) continue;
      if (b.forme.startsWith(a.forme + " ")) {
        prefixes.add(a.forme);
        break;
      }
    }
  }

  for (const f of fiches) {
    const articles = backlinks.get(f.data.slug)?.articles;
    if (!articles || articles.length === 0) continue;

    const { forme, mots } = formeDe(f.data.term);
    if (!forme) continue;
    // Un mot unique trop court ne discrimine rien : on ne le lie pas.
    if (mots === 1 && forme.length < LONGUEUR_MOT_MIN) continue;

    if (ambigues.has(forme) || prefixes.has(forme)) continue;
    const dejaLa = parForme.get(forme);
    if (dejaLa && dejaLa.slug !== f.data.slug) {
      parForme.delete(forme);
      ambigues.add(forme);
      continue;
    }

    // Article principal : celui qui cite la fiche le plus tôt dans son `related`
    // (rang 0 = sujet de l'article), départagé par titre pour rester déterministe.
    const article = articles.reduce((meilleur, a) =>
      a.rang < meilleur.rang ||
      (a.rang === meilleur.rang && a.titre.localeCompare(meilleur.titre, "fr") < 0)
        ? a
        : meilleur
    );

    parForme.set(forme, {
      slug: f.data.slug,
      terme: f.data.term,
      article: { slug: article.slug, titre: article.titre },
    });
    if (mots > motsMax) motsMax = mots;
  }

  return { parForme, motsMax };
}

function echapperAttribut(valeur: string): string {
  return valeur
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

/** Une correspondance retenue dans un segment de texte. */
interface Correspondance {
  debut: number;
  fin: number;
  cible: TermeLiable;
}

/**
 * Cherche les termes dans un fragment de texte brut (jamais dans une balise).
 * Balayage de gauche à droite, correspondance la plus longue d'abord : les
 * passages déjà pris ne sont plus candidats, et « courant électrique » l'emporte
 * sur « courant ». `dejaLies` garantit un seul lien par notion et par définition.
 */
function correspondances(
  texte: string,
  vocab: Vocabulaire,
  exclus: Set<string>,
  dejaLies: Set<string>
): Correspondance[] {
  const mots = decouperMots(texte);
  const trouvees: Correspondance[] = [];

  for (let i = 0; i < mots.length; i++) {
    const maxi = Math.min(vocab.motsMax, mots.length - i);
    for (let longueur = maxi; longueur >= 1; longueur--) {
      // On ne se rabat jamais sur un terme plus court contenu dans un terme plus
      // long déjà reconnu : « courant » à l'intérieur de « courant alternatif »
      // désignerait autre chose que ce que dit la phrase.
      // Les mots d'un terme doivent se suivre : seules espaces, tirets et
      // apostrophes peuvent les séparer, pas une virgule ni un point.
      let contigus = true;
      for (let k = 1; k < longueur; k++) {
        const entre = texte.slice(mots[i + k - 1].fin, mots[i + k].debut);
        if (!LIAISON.test(entre)) {
          contigus = false;
          break;
        }
      }
      if (!contigus) continue;

      const forme = mots
        .slice(i, i + longueur)
        .map((x) => x.radical)
        .join(" ");
      const cible = vocab.parForme.get(forme);
      if (!cible) continue;

      // Terme reconnu : le passage est consommé, qu'on le lie ou non.
      if (!exclus.has(cible.slug) && !dejaLies.has(cible.slug)) {
        dejaLies.add(cible.slug);
        trouvees.push({ debut: mots[i].debut, fin: mots[i + longueur - 1].fin, cible });
      }
      i += longueur - 1;
      break;
    }
  }
  return trouvees;
}

/**
 * Renvoie la définition enrichie de liens vers les articles de blog.
 *
 * `definition` peut contenir un peu de HTML (`<strong>`, `<br>`) : les balises
 * sont recopiées telles quelles et jamais fouillées ; la recherche n'a lieu que
 * dans les fragments de texte, et ne traverse pas une balise. Le texte d'origine
 * est réémis mot pour mot — seuls les attributs fabriqués ici sont échappés.
 *
 * `slugFiche` est exclu : le bloc « Articles qui en parlent » en bas de page
 * couvre déjà la notion de la fiche elle-même.
 */
export function enrichirDefinition(
  definition: string,
  vocab: Vocabulaire,
  slugFiche: string,
  base: string
): string {
  if (!definition || vocab.parForme.size === 0) return definition;
  // Aucune définition ne contient de lien aujourd'hui ; si cela changeait, on
  // rend la définition telle quelle plutôt que d'imbriquer deux <a>.
  if (/<a[\s>]/i.test(definition)) return definition;

  const exclus = new Set([slugFiche]);
  const dejaLies = new Set<string>();
  let sortie = "";
  let position = 0;

  const balise = /<[^>]*>/g;
  let b: RegExpExecArray | null;
  const segments: Array<{ debut: number; fin: number }> = [];
  while ((b = balise.exec(definition)) !== null) {
    if (b.index > position) segments.push({ debut: position, fin: b.index });
    position = b.index + b[0].length;
  }
  if (position < definition.length) segments.push({ debut: position, fin: definition.length });

  let curseur = 0;
  for (const seg of segments) {
    // Tout ce qui précède le segment (les balises) est recopié tel quel.
    sortie += definition.slice(curseur, seg.debut);
    const texte = definition.slice(seg.debut, seg.fin);
    let dans = 0;
    for (const c of correspondances(texte, vocab, exclus, dejaLies)) {
      const libelle = texte.slice(c.debut, c.fin);
      const href = `${base}blog/${encodeURIComponent(c.cible.article.slug)}/`;
      const titre = echapperAttribut(`Article : ${c.cible.article.titre}`);
      sortie +=
        texte.slice(dans, c.debut) +
        `<a class="def-lien" href="${echapperAttribut(href)}" title="${titre}">${libelle}</a>`;
      dans = c.fin;
    }
    sortie += texte.slice(dans);
    curseur = seg.fin;
  }
  sortie += definition.slice(curseur);
  return sortie;
}
