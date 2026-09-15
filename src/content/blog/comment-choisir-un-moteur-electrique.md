---
title: "Continu, asynchrone, brushless : comment choisir un moteur"
date: "2026-09-14"
domain: "F"
excerpt: "Un même besoin, faire tourner un axe, peut se résoudre avec cinq familles de moteurs très différentes. Voici les critères réels qui départagent un moteur à courant continu, un asynchrone, un brushless, un synchrone et un pas à pas."
related: ["moteur-a-courant-continu", "moteur-asynchrone", "moteur-brushless", "moteur-synchrone", "moteur-pas-a-pas", "servomoteur", "moteur-electrique", "rendement-energetique", "triphase"]
sources: [{"titre": "Éduscol — L'essentiel sur le moteur électrique à courant continu", "url": "https://eduscol.education.gouv.fr/sites/default/files/document/ra26-lycee-pro-phychi-essentielmoteur-electrique-127634.pdf", "type": "reference"}, {"titre": "Tecnipass — Comparatif de moteurs : rendement, usage et avantages", "url": "https://www.tecnipass.com/cours-materiels-machines-mpp.brushless", "type": "manuel"}]
---

Un ventilateur de bureau, un lave-linge, un drone et une imprimante 3D ont tous besoin de la même chose au fond : faire tourner un axe. Et pourtant, aucun de ces quatre appareils n'embarque le même type de moteur. Ce n'est pas un hasard de fabrication ni une simple question de coût : chaque famille de moteur électrique répond mieux à certains besoins qu'à d'autres, et personne ne choisit un moteur en se demandant seulement « lequel est le meilleur ». La bonne question est toujours « le meilleur pour faire quoi, et dans quelles conditions ». Voici les critères qui, en pratique, tranchent ce choix.

## Le moteur à courant continu : simple, mais qui s'use

Le moteur à courant continu classique, celui qu'on trouve dans un jouet ou une perceuse d'entrée de gamme, doit sa popularité à une qualité rare : sa vitesse se règle simplement en agissant sur la tension appliquée à ses bornes, sans électronique complexe. Son fonctionnement repose sur un collecteur et des balais, de petites pièces qui assurent le contact électrique entre la partie fixe et la partie tournante en inversant le sens du courant à chaque demi-tour. C'est justement cette pièce mécanique qui limite le moteur : les balais frottent, s'usent, et finissent par devoir être remplacés, ce qui rend ce moteur peu adapté à un usage industriel continu ou à un environnement où la maintenance est difficile d'accès. Il reste en revanche imbattable pour son couple de démarrage élevé et sa facilité de pilotage, ce qui explique sa présence massive dans l'électroménager, l'outillage grand public et les jouets.

## L'asynchrone : le cheval de trait de l'industrie

Le moteur asynchrone n'a ni balais ni aimants dans son rotor : il fonctionne grâce à un champ magnétique tournant créé par le stator, qui induit des courants dans le rotor sans aucun contact électrique glissant. Cette absence de pièce d'usure en fait un moteur d'une robustesse remarquable, capable de tourner des années sans entretien, ce qui explique qu'il équipe la très large majorité des machines industrielles, pompes et ventilateurs. Sa contrepartie est qu'il est alimenté en triphasé et que faire varier précisément sa vitesse demande une électronique dédiée, un variateur de fréquence, alors qu'un simple réglage de tension ne suffit pas comme pour un moteur à courant continu. C'est le choix par défaut dès qu'on cherche de la fiabilité à faible coût d'entretien, sans exigence de position précise.

## Brushless et synchrone : le rendement contre la simplicité

Le moteur brushless remplace les balais mécaniques du moteur à courant continu par une commutation électronique : des aimants permanents sont montés sur le rotor, et l'électronique de commande active les bobinages du stator dans le bon ordre pour le faire tourner. Le résultat est un moteur silencieux, endurant, au rendement élevé, qui équipe aujourd'hui les drones, les ventilateurs haut de gamme et l'outillage portatif sans fil. Le moteur synchrone à aimants permanents suit la même logique à plus grande échelle : son rotor tourne exactement à la vitesse du champ magnétique du stator, sans le léger décalage qui caractérise l'asynchrone, ce qui lui permet d'offrir un rendement particulièrement élevé et explique son adoption croissante dans les véhicules électriques. Le prix à payer, dans les deux cas, est la nécessité d'une électronique de commande plus élaborée, capable de connaître à tout moment la position du rotor pour activer les bons enroulements, ainsi qu'un coût de fabrication plus élevé lié aux aimants permanents.

## Le pas à pas et le servomoteur : quand la position compte plus que la vitesse

Certains usages ne demandent pas de faire tourner un axe vite, mais de le positionner précisément : une tête d'impression 3D, un axe de machine-outil, un volet roulant motorisé. Le moteur pas à pas répond à ce besoin en tournant par petits incréments angulaires très précis, chaque impulsion électrique reçue le faisant avancer d'un pas défini, ce qui permet de connaître sa position sans capteur, en comptant simplement les impulsions envoyées. Le servomoteur suit une logique proche mais différente : il intègre son propre capteur de position et boucle en permanence sur une consigne, ce qui lui permet de tenir un angle donné avec précision, y compris face à une force qui chercherait à l'en écarter, un atout décisif en modélisme et en robotique.

## Le tableau qui résume les critères réels

| Critère | Courant continu | Asynchrone | Brushless / synchrone | Pas à pas / servo |
|---|---|---|---|---|
| Couple au démarrage | Élevé | Moyen | Élevé | Élevé, à l'arrêt inclus |
| Entretien | Balais à remplacer | Quasi nul | Quasi nul | Quasi nul |
| Pilotage de la vitesse | Tension seule | Variateur de fréquence nécessaire | Électronique dédiée | Commande d'impulsions ou boucle de position |
| Coût | Faible | Faible à moyen | Élevé | Moyen |
| Usage typique | Outillage, jouets | Pompes, ventilateurs industriels | Drones, véhicules électriques | Impression 3D, robotique de précision |

## Une décision qui se prend à l'envers

Face à ce paysage, la bonne méthode consiste rarement à partir du moteur pour se demander ce qu'il peut faire. Elle consiste à partir du besoin réel : a-t-on besoin d'un couple de démarrage fort ou d'un maintien de position précis ? Le moteur tournera-t-il en continu pendant des années sans surveillance, ou par courtes sollicitations ? Le budget de commande électronique est-il disponible, ou faut-il rester sur un pilotage minimal ? Un moteur à courant continu qui aurait suffi coûte souvent bien moins cher qu'un brushless surdimensionné pour la même tâche, tandis qu'un asynchrone mal choisi dans une application demandant une position précise ne remplira jamais correctement sa fonction, quelle que soit la qualité de sa fabrication. C'est cette confrontation entre le besoin réel et les contraintes de chaque famille, plus que la performance brute d'un moteur pris isolément, qui doit guider le choix.
