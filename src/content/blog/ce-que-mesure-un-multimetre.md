---
title: "Que mesure vraiment un multimètre quand il affiche 230 V ?"
date: "2026-09-14"
domain: "A"
excerpt: "Un multimètre branché sur une prise affiche 230 volts, mais la tension du secteur ne reste jamais à cette valeur : elle monte et redescend en permanence, jusqu'à dépasser 320 volts à son maximum. Ce que le multimètre affiche est une moyenne particulière, la valeur efficace — pas la tension réelle instant par instant."
related: ["valeur-efficace", "valeur-crete", "multimetre", "tension-electrique", "effet-joule", "courant-alternatif", "frequence-electrique", "voltmetre", "electrisation", "habilitation-electrique"]
sources: [{"titre": "SRD Énergies — Qualité de la tension distribuée", "url": "https://www.srd-energies.fr/wp-content/uploads/sites/7/2022/02/Qualite-de-distribution.pdf", "type": "reference"}, {"titre": "INRS — Risques électriques : ce qu'il faut retenir", "url": "https://www.inrs.fr/risques/electriques/ce-qu-il-faut-retenir.html", "type": "reference"}]
---

Un multimètre branché entre les deux bornes d'une prise de courant affiche 230 volts, un chiffre que presque tout le monde a déjà vu ou entendu. Ce nombre semble décrire une valeur fixe, stable, comme si la tension du secteur restait immobile à 230 volts en permanence. Ce n'est pourtant pas le cas : la tension du réseau domestique change de valeur à chaque instant, et elle atteint même, à certains moments, des valeurs bien supérieures à 230 volts. Ce que l'appareil de mesure affiche n'est donc pas « la » tension à un instant donné, mais un résumé particulier de son comportement dans le temps, appelé valeur efficace.

## Une tension qui ne reste jamais à 230 volts

Le courant électrique livré dans les logements est un courant alternatif : sa tension ne reste pas constante, mais varie continuellement, dessinant une courbe qui monte, redescend, s'annule, repart dans l'autre sens, cinquante fois par seconde. À aucun instant cette tension n'est réellement égale à 230 volts de façon durable : elle passe par cette valeur en montant, la dépasse largement, puis redescend, passe par zéro, puis remonte dans l'autre sens. Le maximum atteint par cette tension au cours de chaque cycle s'appelle la valeur crête, et pour la tension du secteur français, cette valeur crête dépasse 320 volts — nettement plus que les 230 volts habituellement cités.

Cet écart peut surprendre, mais il découle directement de la façon dont on calcule la valeur efficace à partir d'un signal qui varie de façon sinusoïdale : pour ce type de signal, la valeur crête vaut environ une fois et demie la valeur efficace. Autrement dit, les 230 volts affichés par le multimètre ne représentent jamais la tension réellement présente à un instant précis ; ils représentent une valeur calculée à partir de l'ensemble du signal, sur un cycle complet.

## Ce que mesure réellement la valeur efficace

La valeur efficace d'un courant ou d'une tension alternative est définie comme la valeur qu'aurait un courant continu produisant le même effet — au sens de l'échauffement d'un conducteur par effet Joule — que le courant alternatif considéré. Autrement dit, un radiateur électrique alimenté sous une tension alternative de valeur efficace 230 volts chauffe exactement comme s'il était alimenté par une tension continue constante de 230 volts, même si la tension alternative réelle, elle, ne cesse de varier entre plus de 320 volts et moins de 320 volts au cours de chaque cycle.

C'est cette propriété qui rend la valeur efficace si utile en pratique : elle permet de comparer directement un courant alternatif à un courant continu en matière d'énergie transférée, et c'est donc elle qui est indiquée sur les appareils électriques, dans les normes, et affichée par les multimètres, plutôt que la valeur crête ou une quelconque valeur instantanée. Quand une ampoule est annoncée pour fonctionner sous 230 volts, c'est la valeur efficace qui est visée, pas la valeur crête ni une moyenne simple du signal — qui, pour un signal parfaitement symétrique comme une sinusoïde, serait d'ailleurs nulle, puisque les portions positives et négatives s'annuleraient exactement.

## Pourquoi un multimètre ne se contente pas de lire une valeur instantanée

Un multimètre réglé en mode tension alternative ne mesure donc pas la tension à l'instant précis où on le consulte : son électronique interne échantillonne le signal sur une durée suffisante — au moins un cycle complet — et calcule à partir de ces mesures la valeur efficace correspondante, qu'il affiche ensuite comme un nombre stable. C'est ce traitement qui explique que l'affichage reste immobile à 230 volts, alors que la tension réelle, instant par instant, ne cesse de varier. Un multimètre est un instrument polyvalent qui combine les fonctions de voltmètre, d'ampèremètre et d'ohmmètre : dans chacun de ces modes, il applique le même principe de calcul lorsque la grandeur mesurée est alternative.

Cette distinction entre valeur affichée et valeur instantanée n'est pas qu'une curiosité de vocabulaire : elle explique pourquoi certains composants électroniques, notamment les condensateurs utilisés dans les alimentations, doivent être choisis pour supporter une tension bien supérieure à 230 volts. Un composant qui ne supporterait que 230 volts serait en réalité soumis, à intervalles réguliers, à une tension dépassant 320 volts, et risquerait donc d'être endommagé ou détruit.

## Un rappel de sécurité qui n'est pas facultatif

Que la tension affichée soit 230 volts ou que la tension réelle grimpe momentanément au-delà de 320 volts, l'un comme l'autre restent des valeurs largement suffisantes pour provoquer une électrisation grave, voire mortelle, en cas de contact direct avec un conducteur sous tension. Le risque électrique ne se limite d'ailleurs pas au contact direct : un défaut d'isolement, un court-circuit ou un arc électrique peuvent également causer des blessures graves ou un incendie. C'est pourquoi on n'intervient jamais soi-même sur le câblage ou les composants d'une installation électrique sous tension : mesurer une tension avec un multimètre, en respectant les précautions d'usage de l'appareil, est à la portée de toute personne prudente, mais diagnostiquer un défaut, ouvrir un tableau électrique au-delà du simple réarmement d'un disjoncteur, ou remplacer un élément défectueux d'une installation sont des opérations réservées à un professionnel qualifié et habilité.

## Retenir l'essentiel

Le chiffre affiché par un multimètre n'est ni une moyenne ordinaire ni la valeur maximale d'un signal : c'est une valeur efficace, construite précisément pour représenter l'effet réel — au sens de l'échauffement — d'un courant ou d'une tension qui varie en permanence. Retenir que les 230 volts du secteur ne sont qu'un résumé, et que la tension réelle grimpe et redescend bien au-delà à chaque instant, c'est comprendre pourquoi les composants électriques doivent être dimensionnés avec des marges, et pourquoi une tension qui semble « modérée » sur un afficheur reste, à tout instant, suffisamment dangereuse pour justifier la plus grande prudence face à une installation sous tension.
