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

/**
 * Niveaux scolaires : codes de la colonne `Cycle_scolaire_normalise` de la matrice
 * curriculaire (champ `niveau.premiereApparition` d'une fiche) -> libellé lisible.
 * Même liste que `NIVEAUX` dans `scripts/validate_content.py` : garder les deux
 * synchronisées (cf. AGENTS.md §4).
 */
export const NIVEAU_LABEL: Record<string, string> = {
  C1: "Maternelle",
  C2: "CP-CE2",
  C3: "CM1-6e",
  C4: "Collège (5e-3e)",
  "2GT": "Seconde",
  "1G": "Première",
  TG: "Terminale",
  "1-TG": "Première et terminale",
  STI2D: "STI2D",
  CAP: "CAP",
  BACPRO: "Bac pro",
};

/** Libellé d'un code de niveau ; renvoie le code tel quel s'il est inconnu. */
export function niveauLabel(code: string): string {
  return NIVEAU_LABEL[code] || code;
}

/** Types de source admis dans `sources[].type` -> libellé affiché. */
export const SOURCE_TYPE_LABEL: Record<string, string> = {
  programme: "Programme officiel",
  reference: "Référence",
  norme: "Norme",
  manuel: "Manuel",
};

/** "2026-09-11" -> "11/09/2026". Purement textuel : pas de fuseau horaire en jeu. */
export function formatDateFr(iso: string): string {
  const m = /^(\d{4})-(\d{2})-(\d{2})/.exec(iso);
  return m ? `${m[3]}/${m[2]}/${m[1]}` : iso;
}
