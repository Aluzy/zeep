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
  }),
});

const blog = defineCollection({
  type: "content",
  schema: z.object({
    title: z.string(),
    domain: z.string(),
    excerpt: z.string(),
    related: z.array(z.string()).default([]),
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
