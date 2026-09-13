---
title: "À quoi sert un condensateur dans un circuit électronique ?"
date: "2026-09-12"
domain: "K"
excerpt: "Un condensateur stocke temporairement une charge électrique pour lisser une tension, filtrer un signal ou protéger un circuit des variations brutales. Explications à partir d'exemples concrets."
related: ["condensateur", "circuit-analogique", "filtre-electronique", "resistance", "composant-electronique", "signal-analogique"]
sources: [{"titre": "Farnell — Capacitor Types and Performance", "url": "https://fr.farnell.com/capacitor-types-and-performance", "type": "reference"}, {"titre": "Académie de Bordeaux — De l'alternatif au continu (condensateur de lissage)", "url": "https://webetab.ac-bordeaux.fr/Pedagogie/Physique/Physico/Electro/e06trans.htm", "type": "manuel"}]
---

Certains appareils électroniques restent allumés une petite seconde après qu'on a relâché l'interrupteur. Une diode continue à briller, un ventilateur ralentit doucement au lieu de s'arrêter net. Ce court délai n'est pas un défaut : il vient souvent d'un composant électronique qui a stocké un peu de charge électrique et la restitue lorsque l'alimentation disparaît. Ce composant, c'est le condensateur.

## Un petit réservoir de charge électrique

Un condensateur est un composant électronique constitué de deux surfaces conductrices, appelées armatures, séparées par un matériau isolant très fin. Lorsqu'une tension est appliquée à ses bornes, des charges électriques s'accumulent sur chaque armature : le condensateur se charge. Lorsque la tension qui l'alimente diminue ou disparaît, il restitue une partie de cette charge dans le circuit : il se décharge.

Cette capacité à stocker puis relâcher une charge électrique, sur des durées très courtes, distingue le condensateur d'une pile ou d'une batterie. Une batterie conserve de l'énergie chimique pendant des heures ou des jours ; un condensateur ordinaire restitue sa charge en quelques millisecondes à quelques secondes. C'est justement cette rapidité qui le rend utile pour lisser, filtrer ou protéger un circuit, plutôt que pour alimenter un appareil durablement.

Il faut ici distinguer deux grandeurs qu'on confond parfois : la charge stockée dépend à la fois de la tension aux bornes du condensateur et de sa capacité, une caractéristique propre au composant qui se mesure en farads. Un farad est une unité très grande pour l'électronique courante : la plupart des condensateurs utilisés dans les circuits électroniques ont une capacité qui va de quelques picofarads (un millionième de millionième de farad) à quelques milliers de microfarads. Des condensateurs plus volumineux, appelés supercondensateurs, peuvent atteindre plusieurs centaines, voire des milliers de farads, mais ils relèvent d'un usage différent, proche du stockage d'énergie.

## Lisser une tension dans une alimentation

L'un des usages les plus répandus du condensateur se trouve dans les blocs d'alimentation. Le secteur domestique fournit une tension alternative à 230 V, qui change périodiquement de sens. Or la plupart des circuits électroniques ont besoin d'une tension continue, stable, pour fonctionner correctement. Ce sujet ne concerne pas une intervention personnelle sur l'installation : toute opération sur le secteur 230 V reste réservée à des professionnels habilités, et un bloc d'alimentation grand public est conçu pour être branché, jamais ouvert.

À l'intérieur du bloc, un montage appelé pont de diodes transforme d'abord la tension alternative en une tension qui reste toujours du même signe, mais qui ondule encore fortement : elle monte, redescend presque à zéro, remonte, selon le même rythme que le secteur. Un condensateur placé juste après ce montage se charge quand la tension monte, puis se décharge progressivement dans le circuit quand elle redescend, comblant en partie le creux. Le résultat est une tension beaucoup plus régulière, avec de faibles variations résiduelles plutôt que des creux profonds. On parle de condensateur de lissage ou de filtrage. Plus sa capacité est grande, plus les variations restantes sont faibles, à condition que le circuit alimenté ne consomme pas une intensité trop importante entre deux charges.

Un point de vigilance mérite d'être signalé : un condensateur de grande capacité utilisé dans une alimentation peut rester chargé un certain temps après la coupure de l'appareil, y compris après débranchement. C'est une des raisons pour lesquelles l'intérieur d'un bloc d'alimentation ou d'un appareil relié au secteur ne doit pas être manipulé par un particulier.

## Filtrer un signal dans un circuit audio

Le condensateur ne sert pas seulement à stabiliser une tension continue : associé à une résistance, il forme un filtre électronique, un circuit qui laisse passer certaines fréquences d'un signal analogique et en atténue d'autres. C'est le principe utilisé dans un haut-parleur à plusieurs voies, où le signal audio doit être réparti entre un boomer, chargé des fréquences graves, et un tweeter, chargé des fréquences aiguës.

Un condensateur placé en série devant le tweeter laisse passer plus facilement les variations rapides du signal, c'est-à-dire les fréquences aiguës, et s'oppose davantage aux variations lentes, les fréquences graves. Ce comportement, propre au condensateur, vient du fait qu'il réagit à la vitesse de variation de la tension plutôt qu'à sa valeur à un instant donné. Associé différemment à une résistance, il peut au contraire privilégier les fréquences graves. Ces montages, appelés filtres passe-haut et passe-bas, se combinent pour construire des filtres plus élaborés.

## Protéger un circuit contre les variations brutales : le découplage

Un troisième usage, moins visible mais tout aussi courant, concerne le découplage. Dans un circuit électronique comportant plusieurs composants, l'intensité appelée par chacun d'eux peut varier brusquement, par exemple lorsqu'un microcontrôleur change d'état plusieurs millions de fois par seconde. Ces appels brusques d'intensité peuvent faire chuter localement la tension d'alimentation pendant un très court instant, ce qui perturbe le fonctionnement des composants voisins.

Un petit condensateur placé au plus près d'un composant sensible, entre son alimentation et la masse du circuit, joue alors le rôle de réserve locale : il fournit l'intensité nécessaire pendant ces appels très brefs, avant que le reste du circuit n'ait le temps de réagir. C'est ce qu'on appelle un condensateur de découplage. Cette fonction, à l'échelle de quelques nanosecondes, explique pourquoi on trouve souvent plusieurs petits condensateurs disséminés sur une carte électronique, à côté de chaque composant important, plutôt qu'un seul condensateur de grande capacité placé à un endroit unique.

## Un composant discret mais présent partout

Ces trois usages, lisser une tension, filtrer un signal, découpler un composant, reposent tous sur la même propriété de base : la capacité du condensateur à stocker puis restituer rapidement une charge électrique. C'est cette propriété qui le distingue d'une résistance, laquelle ne stocke rien et se contente de s'opposer au passage du courant, ou d'une bobine, qui stocke elle aussi de l'énergie mais sous une forme différente, magnétique plutôt qu'électrique.

Le condensateur figure ainsi parmi les composants électroniques les plus répandus, aux côtés des résistances, présent dans la quasi-totalité des circuits, de l'alimentation d'un ordinateur à la carte d'un jouet électronique, en passant par un simple amplificateur audio. Sa discrétion physique, souvent un petit cylindre ou une puce de quelques millimètres, contraste avec le rôle qu'il joue dans la stabilité et la qualité du fonctionnement des circuits qui l'entourent.
