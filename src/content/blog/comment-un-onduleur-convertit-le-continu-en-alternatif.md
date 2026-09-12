---
title: "Comment un onduleur convertit le continu en alternatif ?"
domain: "M"
excerpt: "Batterie ou panneau solaire produisent un courant continu que les appareils du secteur ne peuvent pas utiliser directement : l'onduleur le transforme en courant alternatif compatible avec le réseau."
related: ["onduleur", "courant-continu", "courant-alternatif", "redresseur", "electronique-de-puissance", "mosfet", "frequence-electrique", "batterie"]
---

Une installation solaire sur le toit, une batterie de secours dans le garage, ou encore une batterie de véhicule qu'on voudrait utiliser pour alimenter un appareil de la maison : dans ces trois cas, la source d'énergie électrique ne peut pas être branchée directement sur une prise. Il manque un boîtier intermédiaire, l'onduleur, sans lequel rien ne fonctionne. Comprendre ce qu'il fait, et comment il le fait, permet de mieux lire une notice d'installation solaire ou de choisir un onduleur de secours adapté.

## Pourquoi une conversion est nécessaire

Une batterie et un panneau photovoltaïque produisent tous deux un courant continu : le courant circule toujours dans le même sens, avec une intensité globalement stable. C'est le type de courant que l'on trouve dans une pile ou dans un accumulateur.

Le réseau électrique qui alimente les prises de la maison distribue, lui, un courant alternatif : le sens et l'intensité du courant varient périodiquement, à une fréquence de 50 Hz en France. La plupart des appareils domestiques — des moteurs aux transformateurs internes de certains chargeurs — sont conçus pour fonctionner avec cette alternance, et le réseau électrique lui-même est construit autour du courant alternatif depuis plus d'un siècle, notamment parce qu'il se transporte plus facilement sur de longues distances via des transformateurs.

Brancher une source de courant continu directement sur une installation prévue pour du courant alternatif ne fonctionne donc pas : il faut un appareil capable de faire la conversion. C'est le rôle de l'onduleur.

## Ce que fait concrètement un onduleur

Un onduleur ne « fabrique » pas un courant alternatif à partir de rien : il découpe le courant continu d'entrée en une succession très rapide d'impulsions, à l'aide de composants d'électronique de puissance qui agissent comme des interrupteurs électroniques. On trouve typiquement des transistors de type MOSFET pour les onduleurs de petite ou moyenne puissance, capables de s'ouvrir et de se fermer des milliers de fois par seconde.

En faisant varier la durée de chaque impulsion selon une technique appelée modulation de largeur d'impulsion, l'électronique de commande obtient, en moyenne sur une courte durée, une tension qui suit progressivement toutes les valeurs intermédiaires nécessaires. Un circuit de filtrage, placé en sortie, lisse ensuite ces impulsions pour reconstituer une onde qui se rapproche d'une sinusoïde à la fréquence attendue du réseau.

Cette opération est en quelque sorte l'inverse de celle réalisée par un redresseur, qui convertit au contraire un courant alternatif en courant continu — on en trouve par exemple à l'intérieur de nombreux chargeurs et alimentations électroniques.

## Onde sinusoïdale pure ou onde simplifiée

Tous les onduleurs ne produisent pas un signal de la même qualité. Les modèles dits « à onde sinusoïdale pure » filtrent finement les impulsions de découpage pour obtenir une courbe très proche de la sinusoïde parfaite du réseau électrique. Des modèles plus simples et moins coûteux se contentent d'un signal en créneaux ou en marches d'escalier, une approximation plus grossière de la sinusoïde.

Cette différence n'est pas seulement une question de confort électrique : un signal éloigné d'une sinusoïde propre peut faire chauffer ou mal fonctionner certains appareils sensibles, en particulier ceux équipés de moteurs ou d'une électronique de contrôle fine. C'est pourquoi les onduleurs raccordés au réseau, notamment ceux des installations solaires, visent systématiquement une onde sinusoïdale de bonne qualité.

## Le cas particulier du solaire : suivre le point de puissance maximale

Dans une installation photovoltaïque, l'onduleur a une seconde mission en plus de la conversion continu-alternatif : il doit en permanence ajuster son fonctionnement pour extraire la puissance maximale disponible sur les panneaux, qui varie selon l'ensoleillement, la température et l'ombrage. Cette recherche continue, appelée suivi du point de puissance maximale, explique pourquoi un onduleur solaire est un appareil électronique piloté en temps réel, et non un simple convertisseur figé.

Un onduleur de secours domestique, alimenté par une batterie plutôt que par des panneaux, n'a pas cette contrainte de suivi : il se concentre uniquement sur la conversion continu-alternatif, généralement pour une durée limitée le temps que revienne le courant du réseau.

## Une conversion qui n'est jamais parfaite

Comme toute conversion électronique, celle réalisée par un onduleur s'accompagne de pertes, principalement sous forme de chaleur dissipée par les composants de commutation. Le rendement d'un onduleur — la part de l'énergie continue reçue qui ressort effectivement sous forme de courant alternatif utilisable — dépasse en général 94 % chez les modèles récents, certains atteignant près de 98 % à leur point de fonctionnement optimal ; ce rendement varie toutefois selon la charge appliquée, d'où l'usage d'un rendement moyen pondéré, plus représentatif d'un usage réel qu'une seule valeur de crête.

## Le rappel qui compte au moment du branchement

Que ce soit pour une installation solaire raccordée au réseau ou pour un onduleur de secours relié au tableau électrique, la sortie de l'appareil rejoint à un moment le réseau domestique en 230 V. Cette partie de l'installation ne se manipule pas soi-même : le raccordement au tableau électrique et toute intervention côté secteur relèvent d'un professionnel qualifié, seul habilité à garantir la sécurité de ce type de branchement.

En résumé, un onduleur transforme un courant continu, issu d'une batterie ou de panneaux solaires, en un courant alternatif compatible avec les appareils domestiques et le réseau électrique, grâce à un découpage rapide du courant suivi d'un filtrage qui reconstitue une onde proche de la sinusoïde attendue. C'est un maillon d'électronique de puissance discret, mais sans lequel aucune installation solaire domestique ni aucun onduleur de secours ne pourrait fonctionner.
