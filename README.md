# Élektropédia (zeep) — v2, migration Astro

Migration de l'ossature v1 (site statique zéro-dépendance) vers un vrai
projet [Astro](https://astro.build), pour préparer la suite : panneau de
contrôle (CMS), vidéos sur les projets DIY, sourcing des composants.

## Pourquoi ce dépôt

La v1 avait été construite dans un environnement cloud qui bloquait toute
installation de paquet (`npm`/`pip` en erreur 403). Ce dépôt permet de
lever cette contrainte : le code est poussé ici, et c'est **GitHub Actions**
(`.github/workflows/deploy.yml`) qui installe les dépendances et construit
le site, sur les serveurs de GitHub — sans dépendre de l'environnement local.

Le site se construit et se déploie automatiquement sur **GitHub Pages** à
chaque `push` sur `main`, à l'adresse `https://<utilisateur>.github.io/zeep/`.

## Structure

```
src/content/wiki/*.json    197 fiches wiki (collection Astro "data")
src/content/blog/*.md      Articles de blog (collection Astro "content", Markdown)
src/content/diy/*.json     Projets DIY, avec vidéos et sourcing des composants
src/content/config.ts      Schémas des collections (validation automatique)
src/data/taxonomy.json     Les 24 domaines
src/layouts/Base.astro     Gabarit commun (header, nav, sélecteur d'âge, footer)
src/pages/                 Toutes les routes du site
src/lib/                   Fonctions utilitaires (domaines, vidéos…)
public/assets/style.css    Système de design (thèmes cuivre/or)
public/assets/site.js      Sélecteur de tranche d'âge + recherche/filtre wiki
.github/workflows/deploy.yml   Construction + déploiement automatique
```

## Développement local

```bash
npm install
npm run dev       # site en local sur http://localhost:4321/zeep/
npm run build     # génère dist/
```

## Statut

- [x] Contenu migré depuis la v1 (197 termes, 3 doublons fusionnés, 3 articles de blog, 3 projets DIY)
- [x] Champs vidéo et sourcing des composants ajoutés au modèle des projets DIY (à remplir)
- [x] Construction et déploiement automatiques via GitHub Actions → GitHub Pages
- [ ] Panneau de contrôle (Decap CMS) — prochaine étape, nécessite une petite passerelle OAuth GitHub
- [ ] Remplir les liens de sourcing et les vidéos des projets DIY existants
- [ ] Reprendre les chantiers de contenu de la v1 (textes par tranche d'âge, illustrations, animations)
