---
title: "Zener, Schottky, LED : trois façons d'utiliser une diode"
date: "2026-09-14"
domain: "K"
excerpt: "Une diode ne fait, en principe, qu'une seule chose : laisser passer le courant dans un seul sens. À partir de ce même mécanisme, trois variantes rendent des services très différents dans un circuit."
related: ["diode", "diode-zener", "diode-schottky", "diode-electroluminescente-led", "jonction-pn", "tension-de-seuil", "semi-conducteur", "resistance"]
sources: [{"titre": "onsemi — Zener Theory and Design Considerations Handbook (HBD854/D)", "url": "https://www.onsemi.com/pub/Collateral/HBD854-D.PDF", "type": "reference"}, {"titre": "Vishay Semiconductors — Zener and Avalanche Breakdown Diodes, Z-Diodes", "url": "https://www.vishay.com/docs/49494/49494.pdf", "type": "reference"}, {"titre": "Conrad — LED, la diode électroluminescente en bref", "url": "https://www.conrad.ch/fr/guides/industrie-40/led-diode-electroluminescente.html", "type": "reference"}, {"titre": "onsemi — HDTMOS Power MOSFETs Excel in Synchronous Rectifier Applications (AN1520/D)", "url": "https://www.onsemi.com/download/application-notes/pdf/an1520-d.pdf", "type": "reference"}]
---

Sur une même carte électronique, on trouve parfois trois diodes qui n'ont, en apparence, rien en commun : l'une clignote pour indiquer que l'appareil est sous tension, une autre stabilise une tension de référence à quelques dixièmes de volt près, une troisième redresse un courant sans presque rien lui faire perdre en chemin. Ce sont pourtant, à la base, le même composant : une jonction PN, qui ne laisse passer le courant que dans un seul sens. Ce qui les distingue, c'est la façon dont chacune exploite, voire détourne, ce principe commun.

## Le socle commun : la jonction PN

Une diode est un composant électronique construit à partir d'un semi-conducteur, le plus souvent du silicium, dont deux zones voisines ont été dopées différemment : l'une pour y créer un excès d'électrons, l'autre un déficit. La frontière entre ces deux zones s'appelle une jonction PN. Elle a une propriété remarquable : appliquée dans un sens, dit sens direct, elle laisse circuler le courant dès que la tension appliquée dépasse une valeur appelée tension de seuil ; appliquée dans l'autre sens, dit sens inverse, elle bloque presque totalement le passage du courant, jusqu'à une certaine limite de tension.

C'est ce comportement asymétrique qui fait de la diode un composant si utile : elle peut protéger un circuit contre une inversion de polarité, redresser un courant alternatif en un courant qui garde toujours le même sens, ou encore, sous certaines formes, transformer de l'énergie électrique en lumière. La diode Zener, la diode Schottky et la diode électroluminescente partent toutes de cette même jonction PN, mais chacune l'exploite selon un objectif différent.

## La diode Zener : exploiter volontairement le sens inverse

Une diode ordinaire, en sens inverse, ne doit jamais être poussée au-delà de sa tension limite : au-delà, elle se met à conduire brutalement, ce qui la détruit généralement si rien ne limite le courant. La diode Zener retourne cette contrainte à son avantage : elle est conçue et dopée spécifiquement pour supporter cette conduction en sens inverse, une fois une tension précise atteinte, sans être endommagée, à condition que le courant qui la traverse reste dans les limites prévues par le fabricant.

Le manuel de référence d'onsemi consacré à ces composants explique que, au-delà de cette tension de claquage, la tension aux bornes de la diode reste ensuite pratiquement constante, quelle que soit la légère variation du courant qui la traverse. Cette propriété en fait un composant de référence de tension : placée dans un circuit avec une résistance de limitation de courant, une diode Zener impose une tension stable à ses bornes, utile par exemple pour fournir une tension de comparaison fiable à un autre circuit, ou pour protéger une entrée sensible contre une surtension accidentelle, en détournant l'excès de tension dès que la limite fixée est dépassée.

Il existe deux mécanismes physiques à l'origine de cette conduction en sens inverse, comme le précise la documentation de Vishay Semiconductors sur ces diodes : l'effet Zener proprement dit, pour les tensions les plus basses, et le claquage par avalanche, pour les tensions plus élevées, où le courant croît alors très rapidement une fois le seuil atteint. Dans les deux cas, l'usage reste le même : fixer une tension de référence stable ou protéger un circuit contre une tension excessive.

## La diode Schottky : réduire les pertes de la conduction directe

La diode Schottky prend le problème dans l'autre sens : elle cherche à améliorer le fonctionnement normal, en sens direct, plutôt qu'à exploiter le sens inverse. Une diode silicium classique, lorsqu'elle conduit, présente une chute de tension à ses bornes d'environ 0,6 à 0,7 volt : une partie de l'énergie électrique qui la traverse est donc systématiquement perdue, transformée en chaleur, même quand la diode fonctionne normalement.

La diode Schottky remplace la jonction entre deux semi-conducteurs par un contact direct entre un métal et un semi-conducteur, ce qui abaisse nettement cette tension de seuil : une note d'application d'onsemi consacrée aux redresseurs basse tension situe cette chute de tension autour de 0,3 volt pour une diode Schottky, contre 0,6 à 0,7 volt pour une diode silicium classique. Cette différence, qui peut sembler minime, compte beaucoup dans une alimentation qui redresse un courant important : moins de tension perdue à chaque diode, c'est moins de chaleur à évacuer et un meilleur rendement global du montage.

Cette même construction confère à la diode Schottky une autre qualité recherchée : elle change d'état, entre bloquée et passante, beaucoup plus rapidement qu'une diode silicium classique. C'est pourquoi on la retrouve en priorité dans les alimentations à découpage, où le courant est commuté à très haute fréquence, et dans les circuits basse tension où chaque dixième de volt perdu compte.

## La diode électroluminescente : transformer l'énergie en lumière

La diode électroluminescente, plus connue sous son sigle LED, exploite un troisième aspect du même mécanisme de base. Lorsqu'une diode conduit en sens direct, les porteurs de charge de chaque côté de la jonction PN se recombinent : les électrons en excès d'un côté comblent les déficits de l'autre. Dans une diode ordinaire, cette recombinaison libère de l'énergie sous forme de chaleur. Dans une LED, comme le rappelle le guide technique du distributeur Conrad, les matériaux semi-conducteurs sont choisis pour que cette énergie soit libérée en grande partie sous forme de lumière plutôt que de chaleur.

La couleur émise dépend directement des matériaux utilisés dans la jonction, et donc de la tension de seuil propre à chaque LED : une diode rouge conduit typiquement à partir d'environ 1,6 à 2,2 volts, tandis qu'une diode bleue ou blanche nécessite une tension de seuil plus élevée, autour de 2,7 à 3,5 volts. Cette tension de seuil, contrairement à une diode Zener, n'est pas exploitée en sens inverse mais bien en sens direct, comme pour toute diode ordinaire.

Une LED ne supporte pas d'être alimentée directement par une tension supérieure à sa tension de seuil sans limitation : au-delà, le courant qui la traverse augmente très rapidement et peut la détruire en quelques instants. C'est pourquoi une résistance de limitation de courant, dimensionnée selon la loi d'Ohm à partir de la tension d'alimentation et de la tension de seuil de la LED, est systématiquement associée à ce composant dans un montage simple sur pile ou sur alimentation de laboratoire à très basse tension.

## Un même principe, trois exploitations

La diode Zener exploite volontairement le sens inverse pour fixer une tension stable. La diode Schottky optimise le sens direct pour réduire les pertes et accélérer la commutation. La diode électroluminescente convertit l'énergie de la recombinaison en lumière plutôt qu'en chaleur. Ces trois usages, très différents dans leurs effets, reposent pourtant sur la même jonction PN et sur la même dissymétrie de conduction entre le sens direct et le sens inverse. Comprendre ce socle commun permet de deviner, face à une diode inconnue sur un schéma, ce qu'elle est probablement en train de faire dans le circuit qui l'entoure.
