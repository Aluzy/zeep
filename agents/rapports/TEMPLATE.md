---
# En-tête lu par les outils (scripts/etat_projet.py, scripts/prochain_lot.py) : garder les clés,
# remplir les valeurs. Une valeur par ligne ; listes et objets en JSON (clés entre guillemets),
# le dépôt n'ayant pas de lecteur YAML. Un commentaire « # … » en fin de ligne est ignoré.
lot: <LOT>
titre: "<titre court>"
date: AAAA-MM-JJ
statut: termine            # termine | partiel | bloque
redacteur: agent-<LOT>
controleur: agent-controleur-<LOT>   # autre agent, qui n'a pas vu la rédaction ; « aucun » pour un lot « site »
changesets: ["agents/changesets/<LOT>.jsonl", "agents/changesets/<LOT>-controle.jsonl"]
fiches_creees: []          # slugs, ex. ["farad", "coulomb"]
fiches_modifiees: []       # slugs
lacunes: []                # notions sans fiche : [{"terme": "…", "domaine": "A", "vu_dans": "slug ou article"}]
decisions_humaines: []     # questions à trancher par Alexandre, une phrase chacune : ["…", "…"]
---

# Rapport de lot <LOT> — <titre>

## Ce qui a été fait
- …

## Fichiers produits
- `agents/changesets/<LOT>.jsonl` (N opérations) et/ou commits : …

## Critères d'acceptation
| Critère | Résultat |
|---|---|
| … | ✅ / ❌ + détail |

## Indicateurs avant / après
Coller deux fois la sortie de `python3 scripts/dette.py --indicateurs` (avant le lot, puis
changeset appliqué sur une copie de travail) et ne garder que les lignes qui bougent.

| Indicateur | Avant | Après |
|---|---|---|
| … | … | … |

## Vérifications effectuées
- `python3 scripts/apply_changeset.py <changeset> --dry-run` : …
- `python3 scripts/validate_content.py` (changeset appliqué sur une copie) : N erreur(s) — doit être 0
- `python3 scripts/audit_couverture.py --ci` : code de sortie … — doit être 0
- `python3 agents/outils/mapping_niveau.py --verifier` : …
- `python3 scripts/dette.py --abaisser` lancé si des fiches de la base ont été corrigées : oui / non / sans objet

## Sources réellement ouvertes
Une ligne par URL citée dans le lot : URL précise (jamais une page d'accueil), date d'ouverture,
ce qu'elle appuie.
- <url> — AAAA-MM-JJ — appuie : …

## Relecture (rempli par le contrôleur)
Grille `docs/grille-relecture.md`, une ligne par fiche.

| Fiche | Critères en échec | Décision |
|---|---|---|
| … | — | conforme / corrigée (n°) / signalée (raison) |

## Points d'attention pour la relecture humaine
- (décisions prises seul, incertitudes, sources faibles)

## Hors périmètre repéré (à planifier)
- (reporter aussi chaque notion sans fiche dans `lacunes` de l'en-tête)
