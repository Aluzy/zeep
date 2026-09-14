---
title: "Le pont diviseur de tension, le montage le plus utile du débutant"
date: "2026-09-14"
domain: "K"
excerpt: "Deux résistances en série suffisent à construire l'un des montages les plus employés de l'électronique. Adapter un signal, lire un capteur, régler un volume : trois usages très différents, un seul principe."
related: ["pont-diviseur-de-tension", "resistance", "potentiometre", "tension-electrique", "loi-d-ohm", "capteur", "composant-electronique", "carte-arduino"]
sources: [{"titre": "Sciences de l'Ingénieur au Lycée Blaise Pascal — Pont diviseur de tension", "url": "https://si.blaisepascal.fr/1t-pont-diviseur-de-tension/", "type": "manuel"}, {"titre": "Académie de Limoges — Séquence 3 : Sciences de l'Ingénieur, Le pont diviseur", "url": "https://pedagogie.ac-limoges.fr/sti_si/accueil/FichesConnaissances/Sequence3SSi/co/S3B22_Association_modele_composant_27.html", "type": "reference"}]
---

Un microcontrôleur ne comprend qu'une plage de tensions bien précise, souvent entre 0 et 3,3 ou 5 volts. Une pile de 9 volts est trop « forte » pour lui. Un capteur de température, lui, ne renvoie pas directement une tension : il change de résistance selon la chaleur qu'il mesure, et une résistance seule ne se lit pas sur une entrée électronique. Un potentiomètre de guitare, enfin, doit transformer la rotation d'un bouton en un réglage de volume progressif. Ces trois problèmes, pourtant très différents, se résolvent avec le même montage : deux résistances en série, appelé pont diviseur de tension.

## Le principe : deux résistances qui se partagent une tension

Dans un pont diviseur de tension, deux résistances sont placées l'une après l'autre entre les deux bornes d'une source de tension. Le point commun aux deux résistances, entre elles, devient un troisième point du circuit, où l'on peut prélever une tension intermédiaire, comprise entre zéro et la tension totale.

Cette tension intermédiaire dépend directement de la proportion que représente chaque résistance dans l'ensemble. Si les deux résistances ont la même valeur, la tension prélevée au point commun vaut exactement la moitié de la tension d'entrée : les deux résistances se « partagent » la tension à parts égales. Si l'une des deux résistances est plus grande que l'autre, elle « absorbe » une part plus importante de la tension, et le point commun se rapproche de l'extrémité opposée.

Cette relation découle directement de la loi d'Ohm : la même intensité traverse les deux résistances puisqu'elles sont montées en série, et la tension aux bornes de chacune est proportionnelle à sa valeur. C'est cette proportionnalité, simple mais très générale, qui rend le pont diviseur de tension utile dans des situations aussi différentes que l'adaptation d'un signal, la lecture d'un capteur ou le réglage d'un volume.

Un point de vigilance mérite d'être signalé, comme le rappelle la fiche de Sciences de l'Ingénieur du lycée Blaise Pascal de Clermont-Ferrand : ce montage ne fonctionne correctement que si le circuit branché après le point commun consomme très peu de courant par rapport à celui qui traverse les deux résistances. Sinon, la tension prélevée s'écarte de la valeur attendue, car une partie du courant est détournée par ce circuit. C'est pourquoi un pont diviseur de tension convient bien pour transmettre une information (une tension à mesurer), mais très mal pour transmettre de la puissance : le rendement du montage est volontairement faible.

## Premier usage : adapter un signal à une entrée électronique

Le cas le plus direct est celui de l'adaptation de tension. Un microcontrôleur, une carte de développement ou un convertisseur analogique-numérique n'acceptent en entrée qu'une tension limitée, généralement entre 0 et 3,3 ou 5 volts selon les modèles. Or de nombreux signaux à mesurer, issus d'une pile, d'un capteur industriel ou d'un autre circuit, dépassent cette plage.

Un pont diviseur de tension placé avant l'entrée réduit le signal dans une proportion connue et constante. Si l'on souhaite, par exemple, ramener une tension deux fois plus grande que ce que l'entrée accepte, il suffit de choisir deux résistances de même valeur : la tension prélevée au point commun sera exactement la moitié de la tension d'origine, et donc compatible avec l'entrée. Il reste ensuite, dans le programme du microcontrôleur, à multiplier la valeur lue par le facteur inverse pour retrouver la tension réelle d'origine.

Cette utilisation, très fréquente dans les projets à base de cartes comme l'Arduino, illustre bien le rôle du pont diviseur de tension comme intermédiaire de sécurité et de conversion, plutôt que comme composant actif.

## Deuxième usage : transformer une résistance variable en tension mesurable

De nombreux capteurs ne renvoient pas une tension, mais une résistance qui varie selon la grandeur physique mesurée : une thermistance change de résistance avec la température, une photorésistance avec la luminosité, une jauge de contrainte avec une déformation mécanique. Le problème est le même dans tous les cas : une entrée électronique mesure une tension, pas une résistance.

En plaçant le capteur résistif en série avec une résistance de valeur fixe et connue, et en alimentant l'ensemble avec une tension de référence stable, on obtient exactement un pont diviseur de tension. La tension prélevée entre les deux éléments varie alors avec la résistance du capteur : elle augmente ou diminue selon que la grandeur mesurée fait monter ou descendre cette résistance. Il devient possible de lire cette tension avec un convertisseur analogique-numérique et de la relier, par calcul, à la grandeur physique d'origine.

Le choix de la résistance fixe associée au capteur n'est pas anodin : une valeur mal choisie réduit fortement la sensibilité du montage sur la plage de mesure utile. C'est un réglage fin, propre à chaque type de capteur, mais qui repose toujours sur le même principe de partage de tension.

## Troisième usage : régler un volume avec un potentiomètre

Le potentiomètre pousse la logique du pont diviseur de tension un cran plus loin : au lieu de deux résistances fixes, il s'agit d'une seule résistance continue, parcourue par un curseur mobile que l'on déplace en tournant un bouton ou en faisant glisser un réglet. Le curseur définit, à chaque instant, deux portions de la résistance totale, situées de part et d'autre de sa position : c'est exactement l'équivalent de deux résistances en série, dont les valeurs changent continûment lorsque l'on tourne le bouton.

Dans un réglage de volume audio, le potentiomètre est alimenté par le signal audio lui-même plutôt que par une tension continue fixe. En position minimale, le curseur prélève une part quasi nulle du signal ; en position maximale, il en prélève la quasi-totalité. Entre les deux, chaque position du bouton correspond à une proportion précise du signal d'origine, ce qui donne à l'utilisateur une sensation de réglage progressif.

Ce même principe se retrouve dans de nombreux autres réglages continus : consigne d'un capteur de position, réglage de contraste d'un afficheur, ou entrée analogique variable pour un microcontrôleur, chaque fois qu'il faut transformer un geste mécanique continu en une tension qui varie de façon proportionnelle.

## Ce que le pont diviseur de tension ne fait pas

Il est utile de rappeler ce que ce montage ne fait pas, pour éviter une erreur fréquente chez les débutants : un pont diviseur de tension ne fournit pas une tension stable et indépendante de la charge qui lui est connectée, contrairement à un régulateur de tension ou à une diode Zener montée en référence. Il ne fait que répartir, dans une proportion fixée par les valeurs des résistances, une tension d'entrée entre les deux éléments du montage. Dès qu'un courant significatif est prélevé au point commun, cette proportion se dégrade.

C'est précisément parce qu'il reste simple, prévisible et peu coûteux à mettre en œuvre, avec seulement deux composants passifs, que le pont diviseur de tension figure parmi les tout premiers montages qu'apprend un débutant en électronique, avant même d'aborder les composants actifs comme les transistors ou les amplificateurs.
