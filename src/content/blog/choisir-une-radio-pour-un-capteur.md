---
title: "LoRa, Zigbee, Wi-Fi : choisir une radio pour un capteur"
date: "2026-09-14"
domain: "Q"
excerpt: "Un capteur qui doit tenir cinq ans sur une pile n'a pas les mêmes besoins radio qu'une caméra qui filme en continu. Portée, débit, consommation : pourquoi il n'existe pas une seule bonne réponse sans fil pour un objet connecté."
related: ["lora", "zigbee", "wi-fi", "objet-connecte-iot", "reseau-maille", "antenne", "bluetooth", "esp32"]
sources: [{"titre": "Semtech — LoRa® and LoRaWAN® : A Technical Overview", "url": "https://www.semtech.com/uploads/technology/LoRa/lora-and-lorawan.pdf", "type": "reference"}, {"titre": "Connectivity Standards Alliance — Zigbee", "url": "https://csa-iot.org/all-solutions/zigbee/", "type": "reference"}, {"titre": "Wi-Fi Alliance — Discover Wi-Fi", "url": "https://www.wi-fi.org/discover-wi-fi", "type": "reference"}]
---

Un capteur de température posé dans un champ, alimenté par une pile, doit parfois fonctionner plusieurs années sans qu'on y touche. Une caméra de surveillance connectée, elle, doit transmettre un flux vidéo en continu. Brancher les deux au Wi-Fi paraît naturel puisque c'est la radio la plus connue, mais c'est justement le choix qui viderait la pile du capteur en quelques jours. Choisir une radio pour un objet connecté revient à arbitrer entre trois grandeurs qui se tirent mutuellement vers le bas : la portée, le débit et la consommation.

## Le triangle portée, débit, consommation

Aucune technologie radio ne peut maximiser en même temps ces trois grandeurs : porter loin, transmettre beaucoup de données et consommer très peu d'énergie sont des objectifs qui se contrarient. Porter plus loin demande soit plus de puissance d'émission, soit un signal plus robuste mais plus lent à transmettre ; transmettre plus de données plus vite demande davantage d'énergie par seconde ; économiser l'énergie impose de réduire la portée, le débit, ou de laisser la radio éteinte la plupart du temps. Chaque technologie radio occupe donc une place différente dans ce triangle, et c'est cette place qui doit guider le choix, pas la notoriété de la technologie.

## Wi-Fi : le débit, au prix de la consommation

Le Wi-Fi a été conçu pour relier des appareils à un réseau local et à Internet avec un débit élevé, suffisant pour du flux vidéo ou de gros transferts de fichiers. L'Alliance Wi-Fi, l'organisme qui rassemble les fabricants autour de la norme, met en avant une connectivité pensée pour relier « tout le monde et tout, partout » avec un débit et une portée pensés pour un usage domestique ou professionnel courant, alimenté sur secteur ou par une batterie rechargée régulièrement. Cette générosité en débit a un revers : maintenir une liaison Wi-Fi active consomme une énergie que la plupart des capteurs sur pile ne peuvent pas se permettre sur la durée. Le Wi-Fi reste donc le bon choix pour un objet connecté qui reste branché ou qu'on recharge souvent, et qui a réellement besoin de transmettre beaucoup de données.

## Zigbee : un réseau maillé économe, pensé pour la maison

Zigbee répond à un besoin différent : celui d'un réseau de nombreux petits appareils domestiques, capteurs de porte, interrupteurs, ampoules connectées, qui doivent communiquer entre eux sans vider leur pile. La Connectivity Standards Alliance, qui maintient la spécification Zigbee, décrit une topologie en réseau maillé auto-organisé et auto-réparateur, capable de rassembler des milliers de nœuds. Dans un tel réseau, chaque appareil alimenté peut relayer les messages de ses voisins plutôt que de dépendre d'un unique point central, ce qui étend la portée globale du réseau et permet à un message de trouver un autre chemin si un appareil tombe en panne. Zigbee est présenté par cet organisme comme optimisé pour une consommation minimale, ce qui explique sa place de choix dans la domotique résidentielle, où de nombreux petits capteurs doivent cohabiter sur pile pendant des mois.

## LoRa : la très longue portée, au prix du débit

LoRa répond à un troisième besoin : celui d'un capteur isolé, loin de toute box ou de tout point d'accès, qui doit néanmoins remonter une information de temps en temps. Selon la documentation technique de Semtech, l'entreprise à l'origine de cette technologie radio, une liaison LoRa porte typiquement jusqu'à cinq kilomètres en milieu urbain et jusqu'à quinze kilomètres ou davantage en zone rurale dégagée. Cette portée s'obtient en sacrifiant largement le débit : LoRa n'est pas conçu pour transmettre beaucoup de données, mais de très petits messages, peu fréquents. La contrepartie est une consommation extrêmement faible en veille, mesurée en milliwatts selon Semtech, qui permet à des capteurs alimentés par pile de fonctionner pendant plusieurs années sans intervention. LoRa désigne la modulation radio elle-même ; LoRaWAN, le protocole souvent associé, ajoute par-dessus la gestion des adresses, le chiffrement des messages et l'organisation du réseau en passerelles et serveurs.

## Un capteur sur pile n'est jamais en Wi-Fi

Cette comparaison explique une règle simple, souvent ignorée des débutants en objets connectés : un capteur qui doit tenir plusieurs années sur une pile n'est presque jamais raccordé en Wi-Fi. Le choix se fait plutôt entre Zigbee, quand le capteur reste à portée d'un réseau maillé domestique et qu'il n'a que quelques mètres à quelques dizaines de mètres à parcourir, et LoRa, quand le capteur est isolé et doit atteindre une passerelle à plusieurs kilomètres avec un message minuscule. Le Bluetooth, plus proche du Wi-Fi en portée mais nettement plus économe en énergie sur de courtes distances, occupe une place intermédiaire pour des objets portés ou proches d'un smartphone, comme un bracelet connecté ou un capteur de vélo.

## Choisir en fonction du capteur, pas de la mode

Avant de retenir une radio pour un projet d'objet connecté, il faut donc répondre à trois questions dans l'ordre : quelle distance sépare le capteur du point de collecte des données, quelle quantité d'information doit réellement être transmise, et quelle autonomie est attendue de l'alimentation. Un capteur proche d'une box, alimenté sur secteur, qui doit transmettre une image régulièrement, s'oriente vers le Wi-Fi. Un ensemble de capteurs domestiques dispersés dans une maison, sur pile, s'oriente vers Zigbee et son réseau maillé. Un capteur isolé en extérieur, loin de tout réseau local, qui n'a qu'une poignée de valeurs à transmettre chaque jour, s'oriente vers LoRa. Le triangle portée, débit, consommation ne se résout jamais entièrement ; il se choisit, projet par projet, en acceptant consciemment ce qu'on sacrifie.
