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

/**
 * Regroupement des codes de niveau en 4 paliers pédagogiques (page d'accueil,
 * page « Choisis ton niveau »). Périmètre voulu : Primaire = CP·CE1·CE2·CM1·CM2,
 * Collège = 6e·5e·4e·3e. C3 (« CM1-6e ») est le code officiel du cycle 3, qui
 * chevauche cette frontière (CM1-CM2 relèvent du primaire, 6e du collège) ; comme
 * une fiche n'est pas subdivisée plus finement que son code de cycle, C3 est
 * rattaché à Collège pour que le 6e n'apparaisse plus sous Primaire — quitte à
 * ce qu'une future fiche de cycle 3 vraiment CM1/CM2 s'affiche elle aussi côté
 * Collège. Aucune fiche n'utilise C3 à ce jour (voir audit), donc ce choix n'a
 * aucun effet visible sur le contenu existant.
 */
export type NiveauBucket = "primaire" | "college" | "lycee" | "approfondissement";

export const NIVEAU_BUCKET: Record<string, NiveauBucket> = {
  C1: "primaire",
  C2: "primaire",
  C3: "college",
  C4: "college",
  "2GT": "lycee",
  "1G": "lycee",
  TG: "lycee",
  "1-TG": "lycee",
  STI2D: "approfondissement",
  CAP: "approfondissement",
  BACPRO: "approfondissement",
};

/** Métadonnées d'affichage par palier (nom, sous-titre, couleurs), partagées entre
 * la page d'accueil (« Explorer par niveau ») et la page « Choisis ton niveau ». */
export const BUCKET_INFO: Record<
  NiveauBucket,
  { name: string; sub: string; color: string; bg: string; icon: string }
> = {
  primaire: {
    name: "Primaire",
    sub: "CP · CE1 · CE2 · CM1 · CM2",
    color: "var(--green)",
    bg: "var(--green-dim)",
    icon: `<path d="M6 8V6a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v2"/><rect x="4" y="8" width="16" height="12" rx="2"/><line x1="4" y1="13" x2="20" y2="13"/>`,
  },
  college: {
    name: "Collège",
    sub: "6e · 5e · 4e · 3e",
    color: "#2456E8",
    bg: "var(--accent-dim)",
    icon: `<path d="M12 3L2 8l10 5 10-5-10-5z"/><path d="M6 10.5V16c0 1.5 3 3 6 3s6-1.5 6-3v-5.5"/>`,
  },
  lycee: {
    name: "Lycée",
    sub: "2nde · 1ère · Terminale",
    color: "#8B5CF6",
    bg: "#EDE7FC",
    icon: `<path d="M4 4l8 8 8-8"/><path d="M4 20l8-8 8 8"/>`,
  },
  approfondissement: {
    name: "Approfondissement",
    sub: "STI2D · CAP · Bac pro",
    color: "#E2672A",
    bg: "#FBE7DC",
    icon: `<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="3"/>`,
  },
};

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

/**
 * Temps de lecture estimé d'un texte, à ~200 mots/minute (arrondi, minimum 1 min).
 * Calculé à la construction à partir du markdown brut de l'article (approximation :
 * la syntaxe markdown elle-même compte comme des "mots", comme pour le seuil de
 * scripts/validate_content.py).
 */
export function readingTimeMinutes(text: string): number {
  const words = text.trim().split(/\s+/).filter(Boolean).length;
  return Math.max(1, Math.round(words / 200));
}
