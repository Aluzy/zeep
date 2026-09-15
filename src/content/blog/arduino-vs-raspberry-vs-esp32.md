---
title: "Arduino, Raspberry Pi, ESP32 : lequel choisir pour son projet"
date: "2026-09-14"
domain: "O"
excerpt: "Les trois noms reviennent sans cesse dans les projets de makers, mais ils répondent à des besoins différents. Consommation, connectivité, présence d'un système d'exploitation : les critères qui doivent vraiment guider le choix."
related: ["carte-arduino", "carte-raspberry-pi", "esp32", "microcontroleur", "microprocesseur", "electronique-embarquee", "objet-connecte-iot", "firmware", "gpio"]
sources: [{"titre": "Arduino Documentation — UNO R3", "url": "https://docs.arduino.cc/hardware/uno-rev3", "type": "reference"}, {"titre": "Raspberry Pi Documentation", "url": "https://www.raspberrypi.com/documentation/", "type": "reference"}, {"titre": "Espressif Systems — ESP32 Wi-Fi & Bluetooth SoC", "url": "https://www.espressif.com/en/products/socs/esp32", "type": "reference"}]
---

Un capteur de température doit tourner cinq ans sur une pile, un robot doit réagir en une fraction de seconde à un obstacle, un boîtier doit héberger un petit serveur web avec caméra : trois projets, trois besoins, et pourtant beaucoup de débutants posent la même question — Arduino, Raspberry Pi ou ESP32 ? La réponse ne tient pas à la popularité de la carte, mais à ce qui tourne réellement dessus.

## Microcontrôleur ou microprocesseur : la distinction qui tranche tout

Une carte Arduino et une carte ESP32 sont construites autour d'un microcontrôleur : un circuit intégré unique qui regroupe un processeur, de la mémoire vive, de la mémoire morte et des broches d'entrée-sortie sur la même puce, pensé pour exécuter un seul programme en boucle et pour piloter directement du matériel. La carte Arduino Uno, par exemple, embarque un microcontrôleur ATmega328P cadencé par un résonateur céramique à 16 mégahertz et propose quatorze broches numériques d'entrée-sortie : de quoi allumer des LED, lire des capteurs et commander des moteurs, sans rien d'autre qui tourne en parallèle.

La carte Raspberry Pi, elle, embarque un microprocesseur complet, distinct de la mémoire et des autres composants, capable de faire fonctionner un véritable système d'exploitation. La documentation officielle de la fondation présente ainsi une gamme qui va des ordinateurs jusqu'aux microcontrôleurs, les premiers étant destinés à faire tourner « Raspberry Pi OS », le système d'exploitation officiel du projet. Cette différence n'est pas un détail technique : elle change tout ce qu'on peut faire avec la carte, et tout ce qu'elle coûte en énergie et en simplicité.

## L'Arduino : piloter du matériel simple, sans intermédiaire

Sans système d'exploitation à démarrer, une carte Arduino exécute son programme dès la mise sous tension et réagit à un signal électrique en un temps prévisible, de l'ordre de la microseconde. C'est ce qui en fait un bon choix pour tout ce qui touche au temps réel au sens strict : un programme qui doit répondre à un événement matériel dans un délai garanti, sans qu'un autre processus ne vienne perturber le calcul. Elle consomme aussi très peu, puisqu'il n'y a ni système à maintenir en mémoire ni processus à ordonnancer. En contrepartie, elle ne sait faire tourner qu'un seul programme à la fois, n'a pas de réseau ni d'écran natifs, et sa puissance de calcul reste limitée face à un microprocesseur.

## Le Raspberry Pi : quand le projet a besoin d'un système complet

Le Raspberry Pi change de catégorie dès qu'un projet a besoin de plusieurs tâches en parallèle, d'un système de fichiers, d'un navigateur, d'un flux vidéo ou d'une connexion réseau élaborée. Sous son système d'exploitation, il gère nativement une caméra, un écran, du stockage et plusieurs programmes lancés en même temps — des usages hors de portée d'un microcontrôleur seul. Cette puissance a un prix : le démarrage prend plusieurs dizaines de secondes, le temps que le système d'exploitation s'initialise, et la consommation électrique au repos dépasse largement celle d'un microcontrôleur, ce qui rend la carte peu adaptée à un fonctionnement sur pile pendant plusieurs mois.

## L'ESP32 : un microcontrôleur pensé pour le sans-fil

L'ESP32 se situe entre les deux, mais du côté microcontrôleur : Espressif, le fabricant, le présente comme une puce intégrant nativement le Wi-Fi et le Bluetooth, avec l'amplificateur, les filtres et les circuits de gestion d'énergie déjà présents sur la puce elle-même. C'est ce qui en fait le choix par défaut d'un objet connecté qui doit communiquer sans multiplier les modules externes. La documentation du fabricant insiste aussi sur une consommation ajustée finement grâce à plusieurs modes d'alimentation et une mise à l'échelle dynamique de la puissance, pensée pour les appareils mobiles, les objets portables et les usages IoT où l'autonomie compte. L'ESP32 reste néanmoins un microcontrôleur : pas de système d'exploitation complet, un seul environnement d'exécution, et une puissance de calcul pensée pour la communication et le pilotage de capteurs plutôt que pour du calcul lourd.

## Consommation, connectivité, temps réel : ce qui doit vraiment guider le choix

Le bon critère de départ n'est jamais « quelle carte est la plus puissante », mais « qu'est-ce que le projet doit réellement faire ». Un objet qui doit tenir des mois ou des années sur une pile élimine d'emblée le Raspberry Pi et oriente vers un microcontrôleur en veille profonde, Arduino ou ESP32 selon le besoin de communication sans fil. Un projet qui doit se connecter au Wi-Fi ou au Bluetooth sans ajouter de module externe pointe vers l'ESP32. Un projet qui doit répondre à un signal matériel dans un délai garanti et constant, sans qu'un système d'exploitation ne vienne perturber le minutage, réclame un microcontrôleur plutôt qu'un microprocesseur généraliste. Et un projet qui manipule une caméra, un écran, un flux réseau complexe ou plusieurs programmes en parallèle a besoin d'un système d'exploitation complet, donc d'un Raspberry Pi.

Ces trois familles ne sont d'ailleurs pas concurrentes dans l'absolu : beaucoup de projets combinent un microcontrôleur au plus près des capteurs, économe et réactif, et un Raspberry Pi en coordinateur, chargé du réseau et du stockage. Comprendre ce que chaque puce fait réellement, plutôt que sa réputation, évite de choisir une carte trop puissante et trop gourmande pour un capteur sur pile, ou trop limitée pour un projet qui a besoin d'un vrai système derrière son firmware.
