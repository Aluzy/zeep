import { defineCollection, z } from "astro:content";

const wiki = defineCollection({
  type: "data",
  schema: z.object({
    term: z.string(),
    slug: z.string(),
    domains: z.array(z.string()),
    sourceDomain: z.array(z.string()),
    merged: z.boolean(),
    pillar: z.boolean().default(false),
    illustration: z.string().nullable().default(null),
    definition: z.string(),
    related: z.array(z.string()),
    // Formes équivalentes du terme (abréviations, symboles, variantes).
    // Servent à la recherche du wiki et à l'audit de couverture
    // (scripts/audit_couverture.py) : un mot déclaré ici n'est plus « orphelin ».
    synonymes: z.array(z.string()).default([]),
    // Champs pédagogiques et de traçabilité (affichage : lot J2-L1).
    // Déclarés dès maintenant pour qu'Astro ne les supprime pas des données.
    niveau: z
      .object({
        premiereApparition: z.string(),
        cycles: z.array(z.string()).default([]),
        familles: z.array(z.string()).default([]),
        matriceIds: z.array(z.string()).default([]),
      })
      .nullable()
      .default(null),
    versionSimple: z.string().nullable().default(null),
    sources: z
      .array(
        z.object({
          titre: z.string(),
          url: z.string().optional(),
          type: z.string().optional(),
        })
      )
      .default([]),
    relecture: z
      .object({
        date: z.string(),
        par: z.string(),
        statut: z.enum(["relu-ia", "valide"]),
      })
      .nullable()
      .default(null),
  }),
});

const blog = defineCollection({
  type: "content",
  schema: z.object({
    title: z.string(),
    domain: z.string(),
    // Date de publication, format AAAA-MM-JJ (chaîne, pas un type Date :
    // scripts/zeeplib.py lit le frontmatter comme du JSON ligne à ligne).
    date: z.string().regex(/^\d{4}-\d{2}-\d{2}$/, "date attendue au format AAAA-MM-JJ"),
    excerpt: z.string(),
    related: z.array(z.string()).default([]),
    // Sources externes vérifiées lors de la rédaction (même structure que le wiki).
    sources: z
      .array(
        z.object({
          titre: z.string(),
          url: z.string().optional(),
          type: z.string().optional(),
        })
      )
      .default([]),
  }),
});

const diy = defineCollection({
  type: "data",
  schema: z.object({
    slug: z.string(),
    title: z.string(),
    level: z.enum(["debutant", "intermediaire", "avance"]),
    domain: z.string(),
    duration: z.string(),
    excerpt: z.string(),
    related: z.array(z.string()).default([]),
    videos: z
      .array(
        z.object({
          label: z.string(),
          url: z.string(),
        })
      )
      .default([]),
    composants: z
      .array(
        z.object({
          nom: z.string(),
          quantite: z.string(),
          liens: z
            .array(
              z.object({
                label: z.string(),
                url: z.string(),
              })
            )
            .default([]),
        })
      )
      .default([]),
    etapes: z.array(z.string()),
    pourAllerPlusLoin: z.string().default(""),
  }),
});

export const collections = { wiki, blog, diy };
