---
title: "Du micro au haut-parleur : où le son se filtre et où il se déforme"
date: "2026-09-14"
domain: "T"
excerpt: "Entre la voix captée par un micro et le son restitué par une enceinte, le signal audio traverse des filtres, des amplificateurs et des limites physiques. Voici où il se façonne, et où il se casse."
related: ["signal-audio", "microphone", "haut-parleur", "amplificateur-audio", "distorsion", "filtre-passe-bas", "bande-passante", "condensateur"]
sources: [{"titre": "Shure — Mic Basics : What Are Transducers?", "url": "https://www.shure.com/fr-FR/perspectives/mic-basics-transducers", "type": "reference"}, {"titre": "haut-parleur.net — Découvrez les secrets de fonctionnement d'un haut-parleur (bobine mobile)", "url": "https://haut-parleur.net/bobine-mobile-comment-ca-marche.html", "type": "reference"}, {"titre": "Lycée LaMache STI2D — Exemple et calculs pour un filtre passe-bas du premier ordre", "url": "https://sti2d.ecolelamache.org/ii_exemple_et_calculs_pour_un_filtre_passebas_1er_ordre.html", "type": "manuel"}]
---

Pousser le volume d'une petite enceinte au-delà d'un certain seuil fait apparaître un son râpeux, comme cassé, alors que la même musique reste propre à volume modéré. Entre la voix captée par un microphone et le son qui sort d'un haut-parleur, le signal traverse plusieurs étapes, chacune susceptible de le transformer, de le nettoyer ou, si elle est poussée trop loin, de l'abîmer. Suivre ce trajet permet de comprendre où se joue la qualité d'un son, et pourquoi il finit parfois par saturer.

## Le microphone : transformer un son en signal électrique

Tout commence par le microphone, un transducteur, c'est-à-dire un composant qui convertit une forme d'énergie en une autre. Comme le rappelle le fabricant Shure dans sa présentation des principes de base du microphone, un microphone a une seule fonction : convertir un son en signal électrique, pour qu'il puisse ensuite être amplifié, enregistré ou transmis.

Deux familles de microphones dominent les usages courants. Le microphone dynamique fait vibrer une membrane légère solidaire d'une petite bobine, elle-même placée dans le champ magnétique d'un aimant : le mouvement de la bobine dans ce champ produit directement un signal électrique, sans avoir besoin d'alimentation. Le microphone à condensateur, plus sensible, utilise au contraire une membrane très fine placée face à une plaque fixe chargée électriquement ; les vibrations sonores modifient l'espacement entre les deux, ce qui fait varier une tension. Ce second type nécessite une alimentation externe, souvent appelée alimentation fantôme.

Dans les deux cas, le signal obtenu en sortie du microphone est très faible, de l'ordre de quelques millivolts. On parle de niveau micro, par opposition au niveau ligne, beaucoup plus élevé, utilisé pour relier les appareils entre eux. C'est pourquoi un microphone est presque toujours suivi d'un préamplificateur, chargé d'élever ce signal faible à un niveau exploitable, avant même que la moindre égalisation ou tout autre traitement ne lui soit appliqué.

## Le filtre : sélectionner des fréquences, pas seulement les couper

Une fois le signal audio amplifié à un niveau exploitable, il traverse souvent un ou plusieurs filtres électroniques. Un filtre ne se contente pas de couper une partie du son : il laisse passer certaines fréquences avec peu ou pas d'atténuation, tout en réduisant progressivement l'amplitude des autres, au-delà d'une fréquence de coupure propre au montage.

Le filtre passe-bas en est un exemple simple, construit à partir d'une résistance et d'un condensateur. Comme le montre la ressource pédagogique du lycée LaMache, dédiée aux sciences de l'ingénieur, un tel filtre laisse passer les basses fréquences et atténue les hautes fréquences, avec une transition progressive plutôt que brutale autour de sa fréquence de coupure. Le filtre passe-haut fait l'inverse : il privilégie les fréquences aiguës. En combinant plusieurs filtres de ce type, un système audio répartit le signal entre les différents haut-parleurs d'une enceinte, un boomer pour les graves, un tweeter pour les aigus, chacun ne recevant que la portion du signal qu'il est capable de restituer correctement.

Cette sélection de fréquences détermine la bande passante du dispositif, c'est-à-dire l'intervalle de fréquences qu'il transmet sans atténuation notable. Un microphone, un amplificateur ou un haut-parleur possèdent chacun leur propre bande passante, et c'est la plus étroite de la chaîne qui limite en pratique la richesse du son final : un excellent microphone branché sur un haut-parleur à bande passante réduite ne rendra jamais un son plus riche que ce que ce haut-parleur peut reproduire.

## L'amplificateur audio : donner de la puissance sans changer la forme du signal

Le signal issu du microphone, même préamplifié, reste trop faible pour faire vibrer un haut-parleur avec suffisamment de puissance sonore. C'est le rôle de l'amplificateur audio, un circuit électronique conçu pour augmenter la puissance d'un signal analogique tout en conservant, le plus fidèlement possible, sa forme d'origine. Un bon amplificateur ne doit rien ajouter au signal et rien lui retirer : il doit seulement le rendre plus puissant.

Cette exigence de fidélité a une limite physique claire : tout amplificateur ne peut fournir qu'une tension et une puissance maximales, fixées par son alimentation et par sa conception. Tant que le signal d'entrée reste dans cette plage, la sortie reproduit fidèlement sa forme, à une échelle plus grande. Au-delà, l'amplificateur ne peut plus suivre l'amplitude demandée.

## La distorsion : quand le signal ne peut plus suivre

C'est précisément ce qui se produit lorsqu'on pousse trop le volume d'un dispositif audio : l'amplificateur reçoit un signal qu'il ne peut plus reproduire fidèlement, faute de puissance disponible. Au lieu de suivre la forme d'origine du signal, sa sortie se retrouve écrêtée, aplatie au sommet de chaque variation, ce qu'on appelle une distorsion.

La distorsion désigne, plus largement, toute déformation d'un signal par rapport à sa forme d'origine. Elle se mesure généralement en pourcentage, et une distorsion trop importante dégrade nettement la fidélité de restitution : le son devient râpeux, agressif, avec une coloration que l'oreille perçoit comme désagréable au-delà d'un certain seuil. La saturation d'un amplificateur poussé au-delà de ses capacités en est la cause la plus fréquente dans un usage domestique, mais un haut-parleur peut lui aussi introduire sa propre distorsion s'il est sollicité au-delà de ce que sa membrane et sa bobine mobile peuvent supporter mécaniquement.

## Le haut-parleur : reconvertir le signal électrique en son

Au bout de la chaîne, le haut-parleur effectue l'opération inverse du microphone : il reconvertit un signal électrique en onde sonore. La technologie la plus répandue, la bobine mobile, place une bobine de fil conducteur dans l'entrefer d'un aimant permanent. Lorsque le signal audio amplifié traverse cette bobine, une force apparaît entre le courant et le champ magnétique de l'aimant : elle déplace la bobine, qui entraîne à son tour la membrane du haut-parleur, produisant ainsi les variations de pression de l'air perçues comme un son.

L'amplitude et la rapidité du mouvement de la membrane suivent, dans un haut-parleur bien conçu, les variations du signal électrique d'entrée. Mais cette membrane a elle aussi ses limites mécaniques : au-delà d'un certain déplacement, elle ne peut plus suivre fidèlement le signal, ce qui ajoute une nouvelle source possible de distorsion, distincte de celle produite par l'amplificateur.

## Une chaîne aussi fidèle que son maillon le plus faible

Du microphone au haut-parleur, chaque étape de la chaîne audio transforme le signal : conversion en énergie électrique, amplification, filtrage, puis reconversion en son. Une chaîne bien conçue vise à traverser toutes ces étapes sans en déformer la forme, hormis les filtrages volontaires destinés à répartir les fréquences entre les haut-parleurs adaptés. La qualité perçue d'un son dépend ainsi rarement d'un seul composant, mais de l'ensemble de la chaîne, et de sa capacité collective à rester dans les limites que chaque élément peut supporter sans distordre le signal qu'on lui confie.
