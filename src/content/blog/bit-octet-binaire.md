---
title: "Bit, octet, binaire : compter avec deux chiffres seulement"
date: "2026-09-14"
domain: "L"
excerpt: "Une machine ne connaît que deux chiffres, zéro et un, et pourtant elle affiche des photos, lit de la musique et fait tourner des jeux vidéo. Voici comment se construisent le bit, l'octet et le système hexadécimal, et ce que pèse vraiment un fichier."
related: ["bit", "octet", "systeme-binaire", "systeme-hexadecimal", "memoire-vive-ram", "signal-numerique"]
sources: [{"titre": "Ministère de l'Éducation nationale — Programme de numérique et sciences informatiques de première générale (arrêté du 17 janvier 2019)", "url": "https://www.education.gouv.fr/sites/default/files/document/Programme%20de%20num%C3%A9rique%20et%20sciences%20informatiques%20de%20premi%C3%A8re%20g%C3%A9n%C3%A9rale-248139.pdf", "type": "programme"}, {"titre": "Interstices (Inria) — Octet", "url": "https://interstices.info/glossaire/octet/", "type": "reference"}]
---

Une photo de quelques mégaoctets, une chanson qui en pèse autant, un jeu vidéo qui en réclame plusieurs dizaines de milliers : tout ce qu'un ordinateur ou un smartphone manipule finit toujours par se ramener à des nombres. Ce qui surprend davantage, c'est que ces nombres ne sont eux-mêmes écrits qu'avec deux chiffres, zéro et un. Comprendre comment on compte avec seulement deux chiffres permet de comprendre ce que représentent vraiment un octet, un mégaoctet, ou les suites de lettres et de chiffres qu'on croise parfois dans un message d'erreur.

## Pourquoi seulement deux chiffres

Le chiffre habituel, celui qu'on utilise pour compter au quotidien, s'écrit avec dix symboles différents, de zéro à neuf : c'est le système décimal. Rien n'oblige pourtant à utiliser dix symboles pour représenter des nombres ; on peut tout aussi bien n'en utiliser que deux, zéro et un, à condition de changer la façon dont on construit les nombres au-delà du premier chiffre. C'est ce que fait le système binaire : chaque nombre y est écrit uniquement avec des zéros et des uns, en donnant à chaque position un poids qui double à chaque fois qu'on se déplace vers la gauche, tout comme, en système décimal, chaque position vaut dix fois la précédente.

Ce choix binaire n'est pas arbitraire : il correspond directement à ce qu'un circuit électronique numérique sait faire le plus simplement, distinguer deux états de tension, l'un bas et l'autre haut. Dans un circuit, ces deux états correspondent typiquement à l'absence ou à la présence de courant à un endroit donné : l'électronique n'a donc besoin de distinguer que deux niveaux pour représenter n'importe quel nombre écrit en binaire, ce qui la rend beaucoup plus fiable que si elle devait distinguer dix niveaux de tension différents pour représenter les dix chiffres du système décimal.

## Le bit, la plus petite information possible

Chaque zéro ou chaque un pris isolément porte un nom : un bit, la plus petite quantité d'information qu'un système numérique puisse manipuler. Un bit unique ne peut coder que deux possibilités, mais en assemblant plusieurs bits, le nombre de combinaisons possibles augmente très vite : deux bits permettent quatre combinaisons, trois bits en permettent huit, et ainsi de suite, chaque bit supplémentaire doublant le nombre de combinaisons disponibles.

C'est ce principe qui permet de représenter, avec suffisamment de bits assemblés, non seulement des nombres entiers, mais aussi des lettres, des couleurs de pixels ou des échantillons de son : tout dépend uniquement de la façon dont on choisit d'interpréter la suite de bits, la suite elle-même restant une simple succession de zéros et de uns.

## L'octet, l'unité qui structure tout le reste

En pratique, les bits ne sont presque jamais manipulés un par un : ils sont regroupés par paquets de huit, un groupement qu'on appelle un octet. Un octet permet de représenter 256 valeurs différentes, de zéro à deux cent cinquante-cinq, ce qui suffisait historiquement à coder un caractère de texte, chiffre, lettre ou signe de ponctuation compris, et qui reste aujourd'hui l'unité de référence pour mesurer la taille de toutes les données numériques.

C'est en octets, et en leurs multiples, que se mesure ce que pèse un fichier : un ko pour mille vingt-quatre octets environ, un mégaoctet pour mille vingt-quatre ko, un gigaoctet pour mille vingt-quatre mégaoctets, et ainsi de suite. Cette valeur de mille vingt-quatre plutôt que mille, qui surprend souvent, vient du fait que l'informatique construit historiquement ses multiples en doublant successivement une puissance de deux plutôt qu'en suivant les multiples de dix habituels du système décimal ; c'est la raison pour laquelle un disque annoncé pour un téraoctet par son fabricant, qui utilise en général la convention décimale de mille, affiche souvent un espace disponible légèrement inférieur une fois branché à un ordinateur, qui applique lui la convention de mille vingt-quatre.

## L'hexadécimal, une écriture plus courte du même binaire

Écrire un nombre en binaire devient vite peu pratique pour un humain : représenter une valeur modeste demande déjà plusieurs chiffres, et une adresse mémoire ou un identifiant technique en réclame beaucoup plus. Pour raccourcir cette écriture sans changer la nature du nombre représenté, l'informatique utilise couramment un troisième système de numération, le système hexadécimal, qui compte en base seize plutôt qu'en base deux ou en base dix. Comme il faut alors seize symboles différents, on complète les dix chiffres habituels par les six premières lettres de l'alphabet, de A à F, pour représenter les six valeurs qui n'ont pas de chiffre dédié dans le système décimal.

L'intérêt de cette base précise, seize, est qu'elle correspond exactement à quatre bits : un seul chiffre hexadécimal représente toujours exactement quatre chiffres binaires, ni plus ni moins, ce qui permet de passer très simplement de l'un à l'autre sans calcul compliqué. C'est pourquoi on retrouve l'hexadécimal partout où l'on doit afficher de façon compacte des valeurs qui sont, au fond, purement binaires : les codes de couleur utilisés sur le web, certaines adresses réseau, ou les messages techniques que peut afficher un système d'exploitation.

## Où vivent ces zéros et ces uns pendant qu'un programme s'exécute

Pendant qu'un programme fonctionne, les données qu'il manipule sous forme de bits et d'octets doivent être stockées quelque part pour rester immédiatement accessibles au processeur : c'est le rôle de la mémoire vive, une mémoire électronique qui garde ces valeurs le temps que l'appareil reste allumé, mais qui les perd dès qu'il s'éteint, contrairement au stockage permanent d'un disque. C'est parce que cette mémoire doit répondre extrêmement vite aux sollicitations du processeur qu'elle est conçue différemment d'un espace de stockage durable, quitte à devoir tout recommencer à chaque redémarrage.

Au bout de cette chaîne, chaque bit correspond, au moment précis où il est traité, à un signal numérique concret circulant dans un circuit électronique : une tension basse ou une tension haute, mesurable avec un instrument adapté, qui ne prend son sens qu'une fois interprétée collectivement avec les autres bits du même octet.

## Deux chiffres, une infinité d'usages

Zéro et un ne racontent, pris séparément, absolument rien. Ce n'est qu'en les assemblant par groupes, en octets puis en structures plus vastes, et en décidant à l'avance comment interpréter chaque groupe, qu'on obtient tour à tour un nombre, une lettre, une couleur ou un son. Le système binaire n'est donc pas une curiosité technique réservée aux informaticiens : c'est la convention, minimale et fiable, sur laquelle repose absolument tout ce qu'un appareil numérique affiche, lit ou calcule.
