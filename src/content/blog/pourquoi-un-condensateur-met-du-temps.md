---
title: "Pourquoi un condensateur ne se remplit pas instantanément"
date: "2026-09-14"
domain: "K"
excerpt: "Une LED qui s'éteint en fondu plutôt que d'un coup : ce petit délai révèle une propriété essentielle du condensateur, la constante de temps, qui gouverne toute une famille de montages électroniques."
related: ["constante-de-temps", "circuit-rc", "condensateur", "regime-transitoire", "farad", "resistance", "tension-electrique", "diode-electroluminescente-led"]
sources: [{"titre": "Académie d'Amiens — Fiche 13 : Retard à l'allumage (Capacités Numériques, Physique-Chimie)", "url": "https://spc.ac-amiens.fr/904-retard-a-l-allumage.html", "type": "officiel"}, {"titre": "Académie de Guyane — TP : Constante de temps τ d'un circuit RC", "url": "https://physique-chimie.dis.ac-guyane.fr/IMG/pdf/tp28_tempsreponsecircuitrc.pdf", "type": "officiel"}]
---

Débranche un petit montage à LED alimenté par pile, et regarde bien la diode au moment où tu coupes l'alimentation : au lieu de s'éteindre d'un coup, elle s'assombrit progressivement, en une fraction de seconde parfois perceptible à l'œil nu. Ce fondu n'est pas un défaut du montage. Il révèle la présence d'un condensateur dans le circuit, et une propriété que tout condensateur partage : il ne se charge ni ne se décharge instantanément. Comprendre pourquoi permet de comprendre une bonne partie des circuits électroniques qui nous entourent.

## Un condensateur ne réagit jamais tout de suite

Un condensateur est un composant qui stocke une charge électrique entre deux armatures séparées par un isolant. Quand on lui applique une tension, il ne se charge pas d'un coup : la tension à ses bornes met du temps à rejoindre la valeur imposée. De la même façon, quand on retire l'alimentation, la charge stockée ne disparaît pas immédiatement : elle se dissipe progressivement dans le reste du circuit, ce qui explique le fondu observé sur la LED.

Ce comportement s'oppose à celui d'une résistance seule, qui réagit de façon quasi instantanée à toute variation de tension. Associer une résistance et un condensateur dans un même circuit, ce qu'on appelle un circuit RC, crée précisément ce délai : la résistance limite le courant qui peut circuler vers le condensateur ou depuis lui, et c'est cette limitation qui étale la charge et la décharge dans le temps plutôt que de les rendre immédiates.

## La constante de temps, une durée caractéristique du montage

Ce délai n'est pas une simple approximation qualitative : il se mesure, et il porte un nom, la constante de temps du circuit. Elle dépend de deux grandeurs seulement, la valeur de la résistance et la capacité du condensateur associé : plus l'une ou l'autre est grande, plus la constante de temps est longue, et plus la charge ou la décharge du condensateur prend de temps.

La constante de temps ne représente pas la durée totale de la charge ou de la décharge, mais une durée de référence à partir de laquelle on peut estimer l'état du circuit. L'académie de Guyane, dans son TP consacré à cette grandeur, rappelle qu'au bout d'une constante de temps, le condensateur a déjà atteint une fraction importante de sa charge finale, et qu'il faut environ cinq constantes de temps pour considérer que le régime est pratiquement établi, la tension du condensateur étant alors très proche de sa valeur finale. Avant ce moment, le circuit traverse ce qu'on appelle un régime transitoire : une phase d'évolution, avant que tout ne se stabilise dans ce qu'on appelle le régime permanent.

C'est cette même grandeur qui explique pourquoi une LED alimentée en aval d'un condensateur qui se décharge s'éteint progressivement plutôt que brutalement : tant que la tension aux bornes du condensateur reste supérieure à la tension de seuil de la diode, un peu de courant continue à circuler, et la lumière décroît doucement au fur et à mesure que le condensateur se vide.

## L'expérience du retard à l'allumage

Le lien entre cette théorie et l'observation concrète est illustré par la fiche « Retard à l'allumage » proposée par l'académie d'Amiens dans le cadre des Capacités Numériques de physique-chimie. Le montage associe une résistance, un condensateur et une LED pilotée par une carte programmable : au lieu d'observer une extinction en fondu, l'expérience met en évidence un allumage retardé de la diode, le temps que la tension aux bornes du condensateur atteigne la tension de seuil nécessaire à son fonctionnement.

Cette activité pédagogique demande justement d'établir la relation entre la tension aux bornes du condensateur et le temps écoulé, pour retrouver par le calcul la durée du retard observé expérimentalement. Elle illustre un point important : la présence d'un condensateur dans un circuit ne se traduit pas seulement par un stockage de charge, mais par une véritable dynamique temporelle, qui peut être mise à profit pour créer volontairement un retard, un allumage progressif, ou au contraire une extinction en fondu.

## Une propriété exploitée dans de nombreux montages

Ce comportement transitoire n'est pas un simple curiosité de laboratoire : il est utilisé de façon délibérée dans de nombreux circuits. Un circuit de temporisation, qui allume un éclairage pendant une durée fixe après avoir appuyé sur un bouton, repose sur la charge ou la décharge d'un condensateur à travers une résistance, dont la constante de temps est choisie pour correspondre à la durée souhaitée. Un filtre électronique, qui laisse passer certaines fréquences d'un signal et en atténue d'autres, exploite lui aussi le fait que le condensateur réagit différemment selon la rapidité des variations de tension qu'on lui applique : une variation lente laisse le temps au condensateur de suivre la tension, une variation rapide non.

Même un simple bouton-poussoir, dans un montage numérique, bénéficie parfois d'un petit circuit RC placé à dessein pour ralentir les changements d'état trop brusques et éviter que de multiples signaux parasites, dus aux micro-rebonds mécaniques du contact, ne soient interprétés à tort comme plusieurs appuis successifs.

## Ce qu'il faut retenir de ce délai

Le condensateur ne « refuse » pas de se charger instantanément par caprice : sa charge dépend de la quantité de courant qu'il reçoit, et ce courant est nécessairement limité par le reste du circuit, en particulier par une résistance placée en série. Plus cette résistance est grande, ou plus la capacité du condensateur est importante, plus la charge et la décharge prennent du temps, selon une relation que la constante de temps résume en une seule valeur.

Cette dynamique, loin d'être un inconvénient à éviter systématiquement, est au contraire l'un des outils les plus employés de l'électronique analogique : elle permet de temporiser, de filtrer, de lisser une tension ou d'adoucir une transition, chaque fois qu'un phénomène a besoin de s'étaler dans le temps plutôt que de se produire d'un coup. La prochaine fois qu'une diode s'éteindra en fondu plutôt que net, ce sera le signe qu'un condensateur, quelque part dans le montage, prend le temps de se vider.
