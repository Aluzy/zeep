---
title: "La jonction PN, le passage à sens unique qui a tout changé"
date: "2026-09-14"
domain: "N"
excerpt: "Un même assemblage de silicium traité de deux façons différentes explique à la fois pourquoi une diode ne laisse passer le courant que dans un sens, comment un transistor amplifie un signal, et comment un panneau solaire produit de l'électricité. Sans équation, voici ce mécanisme commun."
related: ["jonction-pn", "dopage", "trou-electronique", "diode", "transistor", "semi-conducteur", "silicium"]
sources: [{"titre": "CEA — Découvrir & Comprendre : l'essentiel sur les cellules photovoltaïques", "url": "https://www.cea.fr/comprendre/Pages/energies/renouvelables/essentiel-sur-cellules-photovoltaiques.aspx", "type": "reference"}, {"titre": "CEA — Découvrir & Comprendre : la microélectronique", "url": "https://www.cea.fr/comprendre/Pages/nouvelles-technologies/essentiel-sur-microelectronique.aspx", "type": "reference"}]
---

Une diode qui empêche un courant de repartir dans le mauvais sens, un transistor qui amplifie un signal audio, une cellule d'un panneau solaire qui transforme la lumière en électricité : ces trois objets n'ont, à première vue, rien en commun. Ils reposent pourtant sur un seul et même mécanisme, découvert au cœur du silicium au milieu du vingtième siècle, et qui a plus changé l'électronique que n'importe quel autre composant : la jonction PN.

## Un même cristal, deux traitements différents

Le silicium pur, tel qu'il sort du lingot dont on découpe les wafers, conduit très mal le courant électrique : c'est un semi-conducteur, un matériau dont la conductivité se situe entre celle d'un métal, qui conduit bien, et celle d'un isolant, qui ne conduit pas du tout. Pour le rendre réellement utile en électronique, on le soumet à un dopage : on introduit, en quantité infime mais parfaitement maîtrisée, des atomes étrangers au cœur du cristal.

Deux dopages opposés donnent deux comportements opposés. En ajoutant des atomes qui apportent un électron supplémentaire par rapport au silicium, comme le phosphore, on obtient une zone dite de type N, plus riche en électrons libres que le silicium seul. En ajoutant au contraire des atomes qui ont un électron de moins, comme le bore, on obtient une zone de type P, où il manque localement des électrons. Cette absence d'électron n'est pas un vide inerte : elle se comporte elle-même comme une charge positive mobile, qu'on appelle un trou électronique, capable de se déplacer dans le cristal presque comme le ferait un électron, mais en sens inverse.

## La frontière qui ne laisse passer que dans un sens

Lorsqu'on met en contact direct une zone de type N et une zone de type P, on obtient une jonction PN, littéralement la frontière entre les deux zones dopées différemment. À cette frontière, les électrons en excès de la zone N et les trous en excès de la zone P s'attirent et se recombinent sur une fine épaisseur, ce qui vide cette zone de contact de tout porteur de charge mobile. Cette zone appauvrie constitue une barrière naturelle, qui s'oppose spontanément à toute nouvelle circulation de charges d'une zone vers l'autre.

Cette barrière n'est cependant pas infranchissable dans les deux sens de la même façon. En appliquant une tension électrique extérieure d'un côté précis, on peut réduire cette barrière et permettre au courant de circuler facilement à travers la jonction : c'est le sens dit passant. En appliquant la tension dans l'autre sens, on renforce au contraire la barrière et le courant reste bloqué : c'est le sens dit bloquant. C'est très exactement ce mécanisme qui fait d'une diode, le composant construit à partir d'une seule jonction PN, un dispositif qui ne laisse passer le courant électrique que dans un seul sens, en le bloquant dans l'autre.

## Le transistor, deux jonctions qui se pilotent l'une l'autre

Le transistor, lui, assemble non pas une mais deux jonctions PN, en alternant les zones dopées selon un ordre précis. Cette structure permet à une faible tension ou à un faible courant, appliqué sur l'une des zones centrales du composant, de commander une circulation de courant beaucoup plus importante entre les deux autres zones. C'est ce contrôle d'un courant important par un signal beaucoup plus faible qui permet au transistor de remplir deux fonctions essentielles de l'électronique moderne : amplifier un signal, en reproduisant ses variations mais avec une intensité plus grande, ou le faire commuter, c'est-à-dire basculer très rapidement entre un état passant et un état bloquant, comme le ferait un interrupteur commandé électriquement plutôt qu'à la main. C'est cette seconde fonction, la commutation, qui fait du transistor la brique de base de tous les circuits intégrés numériques : chaque transistor y agit comme un minuscule interrupteur, activé ou non selon les signaux qu'il reçoit.

Avant l'apparition du transistor à jonctions, dans les années 1950, cette même fonction était assurée par des tubes électroniques, des composants beaucoup plus volumineux, plus fragiles et qui nécessitaient un temps de chauffe avant de fonctionner. Le remplacement progressif de ces tubes par des transistors à base de jonctions PN, bien plus compacts et immédiatement opérationnels, a rendu possible la miniaturisation de l'électronique jusqu'aux circuits intégrés actuels.

## Quand la lumière prend la place de la tension électrique

La cellule d'un panneau photovoltaïque utilise la même jonction PN, mais elle en inverse en quelque sorte l'usage habituel : au lieu d'appliquer une tension pour faire circuler un courant à travers la jonction, elle utilise la lumière du soleil pour créer elle-même ce courant. Le CEA décrit une cellule photovoltaïque comme un assemblage de couches de silicium dopées différemment, en « sandwich », où chaque photon de lumière qui pénètre dans le matériau et qui possède assez d'énergie libère un électron, créant du même coup, à l'endroit qu'il quitte, un trou électronique : le CEA parle d'une « paire électron-trou » créée à chaque photon absorbé.

Sans jonction PN, cet électron libéré et ce trou fraîchement créé se recombineraient presque immédiatement, sans produire aucun effet utile. Mais parce que la paire électron-trou apparaît précisément dans la zone de la jonction, le champ électrique qui y règne naturellement sépare l'électron et le trou avant qu'ils ne se recombinent, et les envoie chacun vers l'une des deux faces de la cellule. Cette séparation permanente de charges, répétée par des milliards de photons chaque seconde, est ce qui permet de collecter les électrons ainsi libérés pour créer un courant électrique continu, exploitable pour alimenter un appareil ou être injecté dans le réseau.

## Un seul mécanisme, des usages qui n'ont l'air de rien avoir en commun

Diode, transistor, cellule photovoltaïque : ces trois composants partent du même principe, une frontière entre deux zones de silicium dopées différemment, qui ne laisse passer les charges électriques que dans certaines conditions. Ce que change chaque application, c'est la façon dont on exploite cette frontière : la bloquer dans un sens pour une diode, la commander avec un signal faible pour un transistor, ou la laisser séparer les charges créées par la lumière pour une cellule solaire. Comprendre ce mécanisme commun permet de reconnaître, derrière des objets aussi différents qu'un redresseur de courant, un amplificateur audio ou un panneau installé sur un toit, une seule et même invention du solide.
