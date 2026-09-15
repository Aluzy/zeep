---
title: "Ce que fait un variateur de fréquence dans une usine"
date: "2026-09-14"
domain: "F"
excerpt: "Un moteur asynchrone tourne normalement à une vitesse fixe, imposée par la fréquence du réseau. Le variateur de fréquence contourne cette contrainte pour faire varier sa vitesse sans le brutaliser."
related: ["convertisseur-de-frequence", "moteur-asynchrone", "transistor-igbt", "electronique-de-puissance", "triphase", "onduleur", "redresseur", "rendement-energetique"]
sources: [{"titre": "Schneider Electric — Cahier technique n° 208 : Démarreurs et variateurs de vitesse électroniques", "url": "https://formatis.pro/ct208.pdf", "type": "reference"}, {"titre": "Service public de Wallonie — Les moteurs asynchrones, électrotechnique des moteurs dans les applications industrielles", "url": "https://energie.wallonie.be/fr/les-moteurs-asynchrones.html?IDC=8042&IDD=97676", "type": "officiel"}]
---

Dans une usine, un moteur asynchrone qui entraîne un convoyeur, une pompe ou un ventilateur ne démarre presque jamais brutalement, et il tourne rarement à une seule vitesse fixe alors que sa charge, elle, varie constamment. Ce réglage n'a pourtant rien d'évident sur le plan physique : la vitesse d'un moteur asynchrone dépend directement de la fréquence du courant alternatif qui l'alimente, et cette fréquence, sur le réseau électrique, est fixée une fois pour toutes à 50 hertz. Comment fait-on alors varier la vitesse d'un moteur branché sur un réseau dont la fréquence ne bouge jamais ? La réponse tient dans un boîtier discret installé entre le réseau et le moteur : le variateur de fréquence.

## Pourquoi la fréquence commande la vitesse

Dans un moteur asynchrone, le courant alternatif triphasé qui traverse les bobinages du stator crée un champ magnétique tournant, dont la vitesse de rotation est directement proportionnelle à la fréquence du courant qui l'alimente. Le rotor suit ce champ, avec un léger retard appelé glissement, ce qui explique le nom du moteur. Tant que le moteur reste raccordé directement au réseau à 50 hertz, sa vitesse reste donc, pour l'essentiel, imposée par le réseau lui-même, quelle que soit la charge mécanique entraînée. Un document du service public de Wallonie consacré aux moteurs asynchrones industriels le confirme explicitement : la variation de la vitesse s'obtient en faisant varier la fréquence d'alimentation des enroulements du stator, ce qui est précisément ce qu'un variateur électronique de vitesse permet de réaliser.

## Trois étages pour fabriquer une fréquence sur mesure

Un variateur de fréquence ne modifie évidemment pas la fréquence du réseau lui-même : il reconstruit, à partir du courant reçu, un nouveau courant alternatif dont il choisit la fréquence et l'amplitude. Le cahier technique consacré aux variateurs de vitesse électroniques, publié par Schneider Electric, décrit cette architecture en trois étages : un redresseur convertit d'abord le courant alternatif du réseau en courant continu, des condensateurs lissent cette tension continue, puis un onduleur reconstruit à partir de cette tension continue un nouveau courant alternatif, dont la fréquence et l'amplitude sont librement ajustables. C'est cet onduleur qui fait tout le travail : en commandant très rapidement des transistors de puissance, le plus souvent des transistors IGBT capables de commuter des courants importants sous forte tension, il découpe la tension continue pour reconstituer, par modulation, un signal dont la fréquence moyenne équivaut à celle voulue.

Le même document précise un point technique essentiel pour qui veut comprendre le fonctionnement réel du variateur : pour qu'un moteur asynchrone conserve un couple constant quelle que soit sa vitesse, il faut maintenir son flux magnétique constant, ce qui impose de faire varier la tension en même temps que la fréquence, selon un rapport à peu près constant entre les deux. Un variateur de fréquence n'ajuste donc jamais la fréquence seule : il pilote conjointement la tension et la fréquence envoyées au moteur.

## Ne pas brutaliser un moteur au démarrage

L'intérêt d'un variateur de fréquence ne se limite pas à faire varier une vitesse de croisière. Un moteur asynchrone branché directement sur le réseau démarre en appelant un courant très supérieur à son courant nominal, plusieurs fois sa valeur en régime établi, ce qui produit un à-coup mécanique brutal sur l'ensemble de la transmission, et sollicite fortement le réseau électrique de l'installation. Le cahier technique de Schneider Electric le formule directement : la mise en vitesse du moteur, avec un variateur, est contrôlée au moyen d'une rampe d'accélération, qui fait monter progressivement la fréquence, et donc la vitesse, de zéro jusqu'à la valeur voulue. Cette montée en douceur supprime les à-coups mécaniques lors des démarrages, ce qui prolonge la durée de vie des accouplements, des courroies et des pièces mécaniques entraînées, tout en évitant les creux de tension sur l'installation électrique au moment du démarrage.

## Faire tourner un moteur seulement à la vitesse utile

Le dernier bénéfice, souvent le plus concret pour une usine, est l'économie d'énergie. De nombreuses charges industrielles, comme les pompes et les ventilateurs, suivent une loi physique particulière : la puissance qu'elles consomment croît beaucoup plus vite que leur vitesse. Ralentir légèrement une pompe pour l'adapter au débit réellement nécessaire, plutôt que de la faire tourner à pleine vitesse en permanence et de freiner le débit en excès par une vanne, peut ainsi réduire très sensiblement la facture d'électricité. Le document du service public de Wallonie chiffre ce potentiel entre 10 et 50 % d'économie d'énergie pour ce type d'applications à couple dit quadratique, ce qui explique pourquoi les variateurs de fréquence se sont largement généralisés sur les pompes et les ventilateurs industriels, bien au-delà des seuls besoins de pilotage précis de la vitesse.

## Un appareil raccordé au réseau, pas un jouet d'atelier

Un variateur de fréquence industriel est raccordé au réseau électrique et manipule en interne des tensions continues élevées, y compris après la coupure de l'alimentation, le temps que les condensateurs internes se déchargent. Son installation, son câblage et son réglage relèvent donc, comme tout équipement électrique de puissance connecté au réseau, d'un professionnel habilité, et jamais d'une intervention improvisée sur une armoire électrique industrielle.

## En résumé

Le variateur de fréquence répond à une contrainte simple : la vitesse d'un moteur asynchrone dépend de la fréquence qui l'alimente, et cette fréquence est fixe sur le réseau. En reconstruisant, à l'aide d'un redresseur et d'un onduleur à transistors IGBT, un courant alternatif de fréquence et de tension ajustables, il permet de faire démarrer un moteur en douceur, de l'adapter précisément à sa charge et de réduire sa consommation, là où un raccordement direct au réseau ne proposait qu'une seule vitesse, imposée dès la mise sous tension.
