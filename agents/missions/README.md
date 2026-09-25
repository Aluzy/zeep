# Missions — la chaîne de production du contenu

Tout le processus vit dans le dépôt : ce dossier contient les fiches de mission, générées par
`scripts/prochain_lot.py` pour les lots de contenu, écrites à la main pour les autres
(`SERIE-BLOG-B1-B10.md`, cadrage de la série blog).

```
backlog unifié ──► mission du rédacteur ──► changeset ──► mission du contrôleur ──► PR ──► validation humaine
 scripts/backlog.py   prochain_lot.py --lot   (agent 1)    prochain_lot.py --controle  (CI)   valider.py (Alexandre)
                                                           (agent 2, sans le contexte
                                                            de la rédaction)
```

Principes : **une fiche = une seule passe complète** (définition, version simple, sources,
synonymes, liens) ; lots de **15 à 25 fiches** ; **trois rôles séparés** (rédacteur, contrôleur,
valideur humain) ; tout ce qui peut être généré ou contrôlé par un script l'est.

## Déroulé d'un lot de contenu

| Étape | Qui | Commande | Produit |
|---|---|---|---|
| 0. Choisir | intégrateur | `python3 scripts/prochain_lot.py` | taille de chaque file du backlog |
| 1. Générer | intégrateur | `python3 scripts/prochain_lot.py --lot J4-L1 [--file …] [--taille 20]` | `agents/missions/J4-L1.md`, brouillon `agents/changesets/J4-L1.jsonl` |
| 2. Rédiger | agent rédacteur | remplit chaque `"__A_REMPLIR__"` du brouillon | changeset rempli, rapport `agents/rapports/J4-L1.md` |
| 3. Préparer le contrôle | rédacteur ou intégrateur | `python3 scripts/prochain_lot.py --controle J4-L1` | `agents/missions/J4-L1-controle.md`, brouillon `agents/changesets/J4-L1-controle.jsonl` |
| 4. Contrôler | **autre** agent, sans le contexte de la rédaction | grille des 12 critères (`docs/grille-relecture.md`) | verdicts dans le rapport, `relecture` posée sur les fiches conformes |
| 5. Corriger | rédacteur | fiches refusées : corrigées ou retirées du changeset, puis `--controle` à nouveau (passe 2) | |
| 6. Intégrer | intégrateur | `apply_changeset.py J4-L1.jsonl J4-L1-controle.jsonl`, `dette.py --abaisser`, `etat_projet.py` | PR, CI verte |
| 7. Valider | **Alexandre** | `python3 scripts/valider.py J4-L1 --apercu`, puis `python3 scripts/valider.py J4-L1 [--sauf …]` | `agents/validations/J4-L1.md`, `agents/changesets/J4-L1-validation.jsonl` |

N'appliquer le changeset du rédacteur qu'une fois le contrôle terminé : une fiche refusée ne
doit jamais arriver sur le site en l'état.

## Files du backlog (ordre de priorité)

Définies dans `scripts/backlog.py`, recalculées à chaque appel depuis le dépôt (une fiche corrigée
sort de sa file d'elle-même) :

1. `vs-avant-lycee` — notions vues avant le lycée sans version simple (public prioritaire) ;
2. `securite` — fiches secteur sans rappel de sécurité, définitions en HTML, signalements graves ;
3. `niveaux` — entrées périmées de la TABLE de `agents/outils/mapping_niveau.py` ;
4. `reecriture` — définitions hors 25-60 mots, sources imprécises, signalements (par domaine : `--domaine A`) ;
5. `creation` — lexique attendu sans fiche, puis termes de programme sans fiche.

Une fiche citée dans une mission de rédaction sans rapport est « en cours » et n'est pas
reproposée. Les fiches douteuses qu'aucun script ne sait détecter sont signalées dans
`agents/donnees/signalements.json`.

## Rôles et agents

- **Rédacteur** : lit `AGENTS.md` puis sa mission ; n'écrit que dans son changeset et son rapport ;
  ne pose jamais de `relecture`. Doit pouvoir **ouvrir** les sources (accès réseau aux sites
  officiels : Légifrance, Éduscol, education.gouv.fr, Electropedia, INRS…).
- **Contrôleur** : un sous-agent ou une session distincte, lancé avec la seule mission
  `<LOT>-controle.md` (ni la conversation, ni les justifications du rédacteur). Pose
  `"par": "agent-controleur-<LOT>"`.
- **Alexandre** : fusionne la PR, lit l'aperçu, valide par lot (`statut: valide`, contrôlé par
  `validate_content.py`).

Le tableau de bord `docs/ETAT.md` (généré par `scripts/etat_projet.py`) donne à tout moment les
indicateurs, la taille des files, les missions en cours et les décisions ouvertes.
