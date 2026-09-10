import { defineConfig } from "astro/config";

// Site déployé sur GitHub Pages en tant que "project site" :
// https://<user>.github.io/zeep/  -> nécessite un "base" non racine.
// A ajuster si un domaine personnalisé est branché plus tard (base: '/').
export default defineConfig({
  site: "https://aluzy.github.io",
  base: "/zeep",
  output: "static",
  trailingSlash: "always",
});
