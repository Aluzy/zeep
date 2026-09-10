import taxonomyRaw from "../data/taxonomy.json";

export const TAXONOMY: Record<string, string> = taxonomyRaw as Record<string, string>;

const ELEC = new Set(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]);
const ELECTRO = new Set(["K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W"]);

export type Group = "electricite" | "electronique" | "neutre";

export function domainGroup(domains: string[]): Group {
  const inE = domains.some((d) => ELEC.has(d));
  const inK = domains.some((d) => ELECTRO.has(d));
  if (inE && !inK) return "electricite";
  if (inK && !inE) return "electronique";
  return "neutre";
}

export const LEVEL_LABEL: Record<string, string> = {
  debutant: "Débutant",
  intermediaire: "Intermédiaire",
  avance: "Avancé",
};
