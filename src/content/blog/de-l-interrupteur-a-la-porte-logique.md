---
title: "De l'interrupteur à la porte logique : comment une machine calcule"
date: "2026-09-14"
domain: "L"
excerpt: "Un ordinateur ne connaît que deux états, allumé ou éteint. Voici comment, à partir de ce choix minimal, on construit des portes logiques capables de raisonner, puis des circuits capables de calculer, sans qu'aucune machine n'ait jamais eu besoin de comprendre un nombre entier."
related: ["porte-logique", "algebre-de-boole", "table-de-verite", "porte-et-and", "porte-ou-or", "circuit-logique", "transistor"]
sources: [{"titre": "Ministère de l'Éducation nationale — Programme de numérique et sciences informatiques de première générale (arrêté du 17 janvier 2019)", "url": "https://www.education.gouv.fr/sites/default/files/document/Programme%20de%20num%C3%A9rique%20et%20sciences%20informatiques%20de%20premi%C3%A8re%20g%C3%A9n%C3%A9rale-248139.pdf", "type": "programme"}, {"titre": "Interstices (Inria) — Nom de code : binaire", "url": "https://interstices.info/nom-de-code-binaire/", "type": "reference"}]
---

Un simple interrupteur mural n'a que deux positions : allumé ou éteint. Il n'existe pas de position intermédiaire qu'on utiliserait normalement. Cette limitation, qui semble d'abord pauvre comparée à la richesse du monde réel, est pourtant exactement ce dont un ordinateur a besoin pour fonctionner. Toute la puissance de calcul d'un smartphone ou d'un ordinateur repose, en définitive, sur des milliards de minuscules interrupteurs électroniques qui n'ont, eux non plus, que deux états possibles.

## Pourquoi se contenter de deux états

À l'intérieur d'un circuit électronique numérique, un signal électrique est presque toujours interprété selon deux niveaux seulement : une tension basse, associée à l'état zéro, et une tension haute, associée à l'état un. Ce choix n'est pas une contrainte technique regrettable : c'est au contraire ce qui rend les circuits numériques fiables. Un circuit qui devrait distinguer dix niveaux de tension différents pour représenter dix chiffres serait beaucoup plus sensible aux moindres parasites électriques ; avec seulement deux niveaux bien séparés, une petite variation de tension due au bruit électrique ne risque pas de faire basculer un zéro en un ou inversement. C'est cette robustesse qui a fait retenir le système binaire, à deux états, comme langage de base de toute l'électronique numérique.

Le composant qui matérialise ces deux états est le transistor, utilisé ici non pas pour amplifier un signal mais pour le faire commuter : selon ce qu'il reçoit sur son entrée de commande, il laisse ou non passer le courant, exactement comme un interrupteur électronique. En combinant plusieurs transistors selon des schémas précis, on obtient des circuits capables de produire une sortie qui dépend logiquement de leurs entrées : ce sont les portes logiques.

## La porte logique, une décision élémentaire

Une porte logique est le plus petit circuit capable de prendre une décision à partir d'un ou plusieurs signaux d'entrée, chacun valant zéro ou un, pour produire une seule sortie, elle-même valant zéro ou un. Chaque type de porte correspond à une règle de décision différente.

La porte ET, par exemple, ne produit une sortie active que si toutes ses entrées sont actives en même temps : on peut l'imaginer comme deux interrupteurs placés en série sur un même fil, où le courant ne passe que si les deux sont fermés à la fois. La porte OU, à l'inverse, produit une sortie active dès qu'au moins une de ses entrées est active, comme deux interrupteurs placés en parallèle, où le courant passe dès que l'un des deux est fermé. Il existe aussi une porte qui inverse simplement son entrée : ce qui arrive à un devient zéro, et ce qui arrive à zéro devient un.

Ces règles de décision ne sont pas propres à l'électronique : elles reprennent le raisonnement logique formalisé au dix-neuvième siècle par le mathématicien britannique George Boole, qui a montré qu'on pouvait manipuler des propositions vraies ou fausses avec des règles de calcul aussi rigoureuses que celles de l'arithmétique ordinaire. On appelle aujourd'hui cette branche de la logique l'algèbre de Boole ; elle fournit les règles qui permettent de vérifier qu'un circuit se comporte comme prévu, et parfois de le simplifier avant même de le construire.

## La table de vérité, la description complète d'une porte

Pour décrire précisément le comportement d'une porte logique, on n'a pas besoin d'en connaître le circuit intérieur : il suffit d'énumérer, pour chaque combinaison possible des entrées, la valeur de la sortie qui en résulte. Cette description complète porte un nom, la table de vérité, et elle a l'avantage de décrire un comportement sans présupposer la façon dont il est réalisé, que ce soit avec des transistors, des relais mécaniques ou tout autre dispositif à deux états.

Pour une porte à deux entrées comme la porte ET, il n'existe que quatre combinaisons possibles pour les entrées, et la table de vérité les énumère toutes avec la sortie correspondante :

- entrée zéro et entrée zéro : sortie zéro ;
- entrée zéro et entrée un : sortie zéro ;
- entrée un et entrée zéro : sortie zéro ;
- entrée un et entrée un : sortie un.

On voit sur cette liste que la sortie ne vaut un que dans le seul cas où les deux entrées valent un en même temps, ce qui correspond bien à la règle de décision annoncée plus haut. La table de vérité d'une porte OU suivrait le même principe, mais la sortie y vaudrait un dès qu'au moins une des deux entrées vaut un.

## Assembler des portes pour construire un circuit logique

Une seule porte logique ne fait qu'une décision très simple, mais on peut relier la sortie d'une porte à l'entrée d'une autre, puis répéter l'opération autant de fois que nécessaire, pour obtenir un circuit logique capable de traiter un raisonnement bien plus complexe qu'une porte isolée. C'est exactement ainsi que sont construits, à l'intérieur d'un microprocesseur, les circuits qui additionnent deux nombres, qui comparent deux valeurs, ou qui décident quelle instruction exécuter ensuite : chacune de ces opérations, aussi élaborée qu'elle paraisse de l'extérieur, se décompose en une combinaison de portes logiques élémentaires, chacune ne faisant jamais qu'une seule décision entre deux états.

Le programme officiel de la spécialité numérique et sciences informatiques, enseignée en classe de première, rattache d'ailleurs explicitement cette logique aux circuits réels : il précise que les circuits combinatoires, ces assemblages de portes sans mémoire interne, réalisent des fonctions booléennes, c'est-à-dire des fonctions qui ne manipulent que des valeurs vraies ou fausses combinées par les opérateurs logiques de base.

## D'un interrupteur à un calcul

Ce qui frappe, une fois ce mécanisme compris, c'est l'écart entre la simplicité de chaque brique et la complexité du résultat final. Aucun transistor pris isolément ne « sait » additionner ou comparer quoi que ce soit : chacun ne fait que basculer entre deux états selon ce qu'il reçoit. C'est en assemblant des milliards de ces décisions élémentaires, organisées en portes puis en circuits logiques, qu'un processeur devient capable d'exécuter les calculs les plus sophistiqués. Le point de départ reste pourtant celui d'un simple interrupteur : allumé, ou éteint.
