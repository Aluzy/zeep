---
lot: J4-CHAINE
titre: "Chaîne de production du contenu : backlog, missions, contrôle, validation, tableau de bord"
date: 2026-09-25
statut: termine
redacteur: agent-J4-CHAINE
controleur: aucun          # lot d'outillage (« site ») : aucune fiche modifiée
changesets: []
fiches_creees: []
fiches_modifiees: []
lacunes: []
decisions_humaines: ["Accès réseau des agents : l'environnement cloud utilisé pour ce lot bloque education.gouv.fr, eduscol.education.fr, electropedia.org et inrs.fr. Sans ces domaines autorisés, aucun lot de contenu ne peut respecter la règle « chaque source est ouverte avant d'être citée ».", "Source « programme » automatique pour les fiches qui reçoivent un niveau : la matrice ne donne que la référence du BO (« BO n°24 du 11-6-2026 »), sans URL ; il faut d'abord une table référence BO -> URL du texte, vérifiée à la main.", "Lacunes remontées par les anciens rapports (19, voir docs/ETAT.md) : les ajouter à lexique-attendu.json (attendu ou horsPerimetre) ?", "Programmer un lot hebdomadaire automatique (backlog -> rédaction -> contrôle -> PR) une fois l'accès aux sources réglé ?"]
---

# Rapport de lot J4-CHAINE — Chaîne de production du contenu

## Ce qui a été fait

1. **J4-L0 remis d'aplomb** (commit séparé) : `dette.py` → `scripts/`, `dette.json` → `src/data/`,
   `validate_content.py` → `scripts/`, `deploy.yml` → `.github/workflows/`, CSV J2-L2 → `agents/rapports/`.
   Le cliquet est désormais actif en CI (vérifié : une définition raccourcie sur une fiche hors base est bloquée).
2. **Backlog unifié** `scripts/backlog.py` : cinq files par priorité (`vs-avant-lycee` 21, `securite` 31,
   `niveaux` 22, `reecriture` 315, `creation` 98), recalculées depuis le dépôt ; une fiche n'apparaît que dans
   la première file qui la contient et porte **toutes** les règles qu'elle enfreint (passe complète). Les fiches
   des missions sans rapport sont « en cours » et ne sont pas reproposées.
3. **`scripts/prochain_lot.py`** :
   - sans option : taille des files ;
   - `--lot <LOT> [--file] [--taille] [--domaine]` : mission Markdown (contenu actuel, règles enfreintes, fiches
     voisines avec leur définition, articles qui citent la fiche, consignes) + **brouillon de changeset** dont
     les `old` sont recopiés par le script (définition, version simple, sources, synonymes selon les défauts) ;
     `create` pour la file `creation` ; pour `niveaux`, mission seule (le changeset vient de `mapping_niveau.py --lot`) ;
   - `--controle <LOT>` : mission du contrôleur (avant / après, règles encore enfreintes, sources à ouvrir,
     grille des 12 critères) **sans les justifications du rédacteur**, et brouillon `<LOT>-controle.jsonl`
     (une `relecture` par fiche, à remplir ou à supprimer). Refuse un changeset de rédacteur qui pose une
     relecture. Passes successives : une fiche refusée puis corrigée repasse seule (`<LOT>-controle-2.md`).
4. **`apply_changeset.py`** refuse toute opération contenant `"__A_REMPLIR__"` ; nouvelle fonction
   `avant_apres()` (état avant / après d'un changeset, appliqué ou non), partagée par le contrôle et la validation.
5. **`scripts/valider.py`** : `--apercu` écrit `agents/validations/<LOT>.md` (tableau avant / après, sources
   cliquables, état de la relecture) ; sans option, `agents/changesets/<LOT>-validation.jsonl`
   (`statut: valide`, `par: Alexandre`), uniquement pour les fiches relues par un contrôleur, `--sauf` pour en écarter.
   `validate_content.py` refuse désormais un `valide` posé par quelqu'un d'autre qu'Alexandre.
6. **`scripts/etat_projet.py`** → `docs/ETAT.md` : indicateurs, dette par règle, files du backlog, lots (d'après
   les en-têtes), missions en cours, brouillons, lacunes remontées absentes du lexique, décisions ouvertes,
   signalements. `--verifier` contrôle l'en-tête des rapports (CI) ; `--stdout` alimente le résumé de la CI.
   `synthese-zeep.md` est marquée « figée ».
7. **Mémoire du projet** : les 16 rapports supprimés le 25/09 (B1-B7, J1-L2, J1-L3, J2-L1 + aperçu, J2-L4,
   J2-L5, J3-L1, chantier A 4-5 et 6) sont restaurés depuis `9d21a28^`, avec un **en-tête ajouté a posteriori**
   (lacunes et décisions extraites de leur section « Hors périmètre »). Le cadrage de la série blog
   (`SERIE-BLOG-B1-B10.md`) rejoint `agents/missions/`. Les rapports B8-B10 n'ont jamais existé.
   Les 20 fiches douteuses de J1-L3 deviennent des données : `agents/donnees/signalements.json` (24 entrées),
   qui alimentent les files `securite` et `reecriture` et se ferment d'elles-mêmes à la relecture indépendante.
8. **En-têtes JSON** : `zeeplib.lire_entete()` (stdlib, commentaires `#` tolérés) ; `TEMPLATE.md` mis à jour.
9. **CI** : étapes `etat_projet.py --verifier`, tableau de bord dans le résumé, `verifie_liens_retour.py`
   (sous Node 22 pour exécuter le vrai `backlinks.ts`). Ce dernier script était cassé : attendus figés au 12/09
   (23 fiches, fiches « sans lien ») et index Python sans le champ `rang` ajouté par le chantier A-6 ; les
   témoins sont désormais des inclusions et le tri suit `localeCompare("fr")`.
10. **Premier lot prêt** : `agents/missions/J4-L1.md` et le brouillon `agents/changesets/J4-L1.jsonl`
    (21 fiches, 74 opérations : 21 versions simples, 21 sources, 17 définitions, 15 synonymes).
11. Documentation : `agents/missions/README.md` (déroulé, rôles, files), `AGENTS.md` (§2 bis, en-têtes),
    `README.md`.

## Fichiers produits
- Scripts : `scripts/backlog.py`, `scripts/prochain_lot.py`, `scripts/valider.py`, `scripts/etat_projet.py` (nouveaux) ;
  `scripts/zeeplib.py`, `scripts/apply_changeset.py`, `scripts/validate_content.py`,
  `agents/outils/mapping_niveau.py` (fonctions `table_perimee`, `backlog_programme`, `analyser`),
  `agents/outils/verifie_liens_retour.py`.
- Données : `agents/donnees/signalements.json`, `docs/ETAT.md`.
- Missions : `agents/missions/README.md`, `agents/missions/J4-L1.md`, `agents/missions/SERIE-BLOG-B1-B10.md`.
- Brouillon : `agents/changesets/J4-L1.jsonl` (non applicable tant qu'il contient `__A_REMPLIR__`).

## Critères d'acceptation

| Critère | Résultat |
|---|---|
| Fichiers de J4-L0 à leur place, cliquet actif | ✅ essai de régression bloqué (`definition_longueur`, nouvelle dette) |
| `prochain_lot.py` : backlog unifié, mission, brouillon avec `old` recopié | ✅ 5 files ; J4-L1 généré |
| `apply_changeset.py` refuse `__A_REMPLIR__` | ✅ |
| Mission du contrôleur générée depuis le changeset | ✅ passes successives comprises |
| `valider.py --apercu` et changeset de validation | ✅ |
| `etat_projet.py` → `docs/ETAT.md` | ✅ |
| Rapports B1-B7, J1, J3, chantier A récupérés, lacunes reportées | ✅ 16 rapports, 19 lacunes encore ouvertes dans ETAT |
| `verifie_liens_retour.py` en CI | ✅ réparé puis ajouté |

**Essai de bout en bout** (sur une copie jetable du dépôt, données factices jamais commitées) : brouillon de
3 fiches rempli → `--controle` → 2 fiches conformes, 1 refusée → application → `validate_content.py` 0 erreur →
`dette.py --abaisser` (6 fiches sorties de la base) → `valider.py --apercu` → `valider.py --sauf` → 1 fiche
`valide` appliquée, 0 erreur ; le backlog passe de 21 à 18 ; `--controle` en passe 2 ne propose que la fiche refusée.

## Indicateurs avant / après
Aucune fiche modifiée : indicateurs inchangés (voir `docs/ETAT.md`).

## Vérifications effectuées
- `python3 scripts/validate_content.py` : 0 erreur, 0 avertissement.
- `python3 scripts/audit_couverture.py --ci` : code de sortie 0.
- `python3 agents/outils/mapping_niveau.py --verifier` : OK ; sans option, le CSV J2-L2 régénéré est identique.
- `python3 agents/outils/verifie_liens_retour.py` : 0 erreur, index TypeScript = index Python.
- `python3 scripts/etat_projet.py --verifier` : 0 erreur.
- `python3 scripts/dette.py --abaisser` : sans objet (aucune fiche corrigée).

## Sources réellement ouvertes
Aucune : lot d'outillage. Tentative d'ouverture de education.gouv.fr, eduscol.education.fr, electropedia.org
et inrs.fr : bloquées par la politique réseau de l'environnement (voir décisions).

## Relecture (rempli par le contrôleur)
Sans objet : lot d'outillage, aucune fiche.

## Points d'attention pour la relecture humaine
- Le build Astro n'est pas lançable ici : aucun fichier du site n'a été modifié ; la CI le confirme.
- Le brouillon `J4-L1.jsonl` propose `synonymes` pour les fiches qui n'en ont pas : le rédacteur supprime la
  ligne s'il n'y a pas de forme équivalente.
- Dans `avant_apres()`, un changeset déjà appliqué est « défait » champ par champ pour l'aperçu ; les liens
  ajoutés (`related`) ne le sont pas.
- Le contrôle ne doit être lancé qu'avant l'application du changeset du rédacteur : une fois appliqué, une
  correction de fiche refusée n'est plus distinguable par `avant_apres()`.

## Hors périmètre repéré (à planifier)
- Issues GitHub `decision` pour les arbitrages du §8 de la passation (créées avec la PR).
- Lot hebdomadaire programmé : à activer quand les agents pourront ouvrir les sources.
- `audit_couverture.py --backlog` fait doublon avec la file `creation` de `prochain_lot.py` ; à retirer plus tard.
