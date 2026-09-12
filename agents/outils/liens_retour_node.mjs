// Enveloppe d'essai : exécute le vrai src/lib/backlinks.ts hors d'Astro.
//
//     node --experimental-strip-types agents/outils/liens_retour_node.mjs < donnees.json
//
// Entrée (stdin, JSON) : { "articles": [...], "projets": [...], "slugsWiki": [...] }
// Sortie (stdout, JSON) : { "ok": true, "index": { "<slug>": { articles, projets } } }
//                         { "ok": false, "erreur": "<message>" } si le garde-fou se déclenche.
//
// Appelé par agents/outils/verifie_liens_retour.py, qui compare cet index à celui
// qu'il reconstruit lui-même depuis src/content/. Aucune dépendance npm.
import { buildBacklinkIndex } from "../../src/lib/backlinks.ts";

const entree = JSON.parse(await new Promise((resolve, reject) => {
  let buf = "";
  process.stdin.setEncoding("utf8");
  process.stdin.on("data", (c) => (buf += c));
  process.stdin.on("end", () => resolve(buf));
  process.stdin.on("error", reject);
}));

try {
  const index = buildBacklinkIndex(entree.articles, entree.projets, entree.slugsWiki);
  process.stdout.write(JSON.stringify({ ok: true, index: Object.fromEntries(index) }));
} catch (e) {
  process.stdout.write(JSON.stringify({ ok: false, erreur: String(e && e.message ? e.message : e) }));
}
