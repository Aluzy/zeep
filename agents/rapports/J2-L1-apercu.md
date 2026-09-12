# J2-L1 — Aperçu de l'affichage des nouveaux champs

Aucune fiche du dépôt n'a été modifiée : les champs `niveau` et `versionSimple` arriveront
par les lots **J2-L2** et **J2-L4**. Ce document décrit ce que le gabarit
`src/pages/wiki/[slug].astro` produira une fois les données présentes, pour que l'intégrateur
et les lots suivants sachent exactement à quoi s'attendre.

Les essais d'affichage ont été faits sur une **copie jetable du dépôt**, hors du dépôt
(`scratchpad/essai-J2-L1`), jamais sur `src/content/wiki/`.

---

## 1. Fiche de démonstration (données d'exemple, non commitées)

```json
{
  "term": "Tension électrique",
  "slug": "tension-electrique",
  "domains": ["A"],
  "definition": "Grandeur, exprimée en volts, qui…",
  "niveau": {
    "premiereApparition": "C2",
    "cycles": ["C2", "C4"],
    "familles": ["FAM01"],
    "matriceIds": ["M002", "M015"]
  },
  "versionSimple": "La tension, c'est ce qui pousse le courant dans un fil, comme la pente pousse l'eau d'un toboggan.",
  "sources": [
    { "titre": "Programme du cycle 4, BO n° 31 du 30 juillet 2020", "url": "https://…", "type": "programme" },
    { "titre": "Manuel de physique-chimie 4e, chapitre 7" }
  ],
  "relecture": { "date": "2026-09-12", "par": "agent-J2-L4", "statut": "relu-ia" }
}
```

## 2. HTML produit (fiche complète)

```html
<div class="term-card">
  <h1>Tension électrique</h1>

  <!-- (1) badge de niveau, à la suite des puces de domaine -->
  <div class="term-meta">
    <div class="chip-row">
      <a href="/zeep/wiki/?domain=A" class="chip is-accent">Électricité — fondamentaux et physique</a>
      <span class="chip niveau-badge"
            title="Cette notion apparaît dans les programmes scolaires à ce niveau : CP-CE2.">
        <span class="k">Niveau</span>CP-CE2
      </span>
    </div>
    <p class="niveau-note">Apparaît dans les programmes à ce niveau.</p>
  </div>

  <div class="definition">Grandeur, exprimée en volts, qui…</div>

  <!-- (2) encadré « En simple », juste après la définition de référence -->
  <aside class="simple-box">
    <p class="simple-label">En simple</p>
    <p class="simple-text">La tension, c'est ce qui pousse le courant dans un fil, comme la pente pousse l'eau d'un toboggan.</p>
  </aside>

  <div class="related-block">…</div>

  <!-- (3) sources, en bas de fiche -->
  <div class="sources-block">
    <h2 class="section-label">Sources (2)</h2>
    <ol class="source-list">
      <li class="source-item">
        <a class="source-title" href="https://…" target="_blank" rel="noopener noreferrer">Programme du cycle 4, BO n° 31 du 30 juillet 2020</a>
        <span class="source-type">Programme officiel</span>
      </li>
      <li class="source-item">
        <span class="source-title">Manuel de physique-chimie 4e, chapitre 7</span>
      </li>
    </ol>
  </div>

  <!-- (4) mention de relecture, tout en bas -->
  <p class="relecture-note">Relu par IA le 12/09/2026</p>
</div>
```

## 3. Ce que chaque champ déclenche (et ce qui disparaît sans lui)

| Champ | Rendu | Absent / vide |
|---|---|---|
| `niveau` | puce `Niveau <libellé>` + info-bulle + ligne « Apparaît dans les programmes à ce niveau. » | rien : la ligne des domaines est identique à aujourd'hui |
| `versionSimple` | `<aside class="simple-box">` après la définition | l'`<aside>` n'est pas émis (test sur la chaîne **après `trim()`**) |
| `sources` | bloc `Sources (n)` + `<ol>` | aucun `<div class="sources-block">`, pas de titre orphelin |
| `sources[].url` | titre en lien externe (`target="_blank" rel="noopener noreferrer"`) | titre en `<span>`, non cliquable |
| `sources[].type` | `<span class="source-type">` discret | pas de span |
| `relecture.statut` | `relu-ia` → « Relu par IA le JJ/MM/AAAA » ; `valide` → « Validé le JJ/MM/AAAA » | aucun paragraphe |

Une fiche sans aucun de ces champs — c'est le cas des 190 fiches actuelles — rend **exactement**
la même page qu'avant le lot, au seul détail près du `<div class="term-meta">` qui enveloppe
désormais la ligne des puces (la marge de 20 px, auparavant en style en ligne sur `.chip-row`,
est portée par ce conteneur).

## 4. Libellés de niveau

Table exportée : `NIVEAU_LABEL` dans `src/lib/helpers.ts` (fonction `niveauLabel(code)`).
Codes repris de la colonne `Cycle_scolaire_normalise` de la matrice curriculaire v2.

| Code | Libellé affiché |
|---|---|
| `C1` | Maternelle |
| `C2` | CP-CE2 |
| `C3` | CM1-6e |
| `C4` | Collège (5e-3e) |
| `2GT` | Seconde |
| `1G` | Première |
| `TG` | Terminale |
| `1-TG` | Première et terminale |
| `STI2D` | STI2D |
| `CAP` | CAP |
| `BACPRO` | Bac pro |

Un code inconnu est affiché tel quel par le gabarit (aucune page cassée) **et** refusé par
`scripts/validate_content.py`, qui tourne en CI avant le build.

## 5. Types de source

`SOURCE_TYPE_LABEL` (`src/lib/helpers.ts`) : `programme` → « Programme officiel »,
`reference` → « Référence », `norme` → « Norme », `manuel` → « Manuel ».
Tout autre type est affiché tel quel (le schéma laisse `type` libre).
