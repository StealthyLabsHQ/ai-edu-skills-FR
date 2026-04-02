---
name: plume-naturelle
description: >
  Transforme un texte généré par IA en texte indiscernable d'une écriture humaine. Trigger dès
  que l'utilisateur mentionne : humaniser, rendre naturel, anti-détection, anti-IA, "ça sonne
  faux", "ça fait ChatGPT", "mon prof va voir que c'est de l'IA", réécrire, reformuler, "trop
  lisse", "trop parfait", "manque de personnalité", filtre anti-IA, désIA-iser, "rendre humain",
  plagiat IA, détecteur IA, Turnitin, Compilatio, GPTZero, "style trop propre", "on dirait un
  robot". Trigger aussi quand un texte soumis à relecture présente des patterns IA évidents.
  TOUJOURS utiliser ce skill pour toute demande de réécriture visant à rendre un texte plus
  naturel ou indétectable comme IA.
version: 1.1.0
---

# Plume Naturelle -Moteur de réécriture anti-IA pour le français

## Principe directeur

Un texte bien humanisé n'est pas simplement un texte dont on a retiré les patterns IA.
C'est un texte dans lequel on a **injecté une voix réelle**.

Retirer les patterns est nécessaire mais insuffisant. Le but final est qu'un professeur,
un recruteur ou un pair lise le texte et pense : « cette personne réfléchit et écrit. »

Deux textes peuvent être grammaticalement parfaits, factuellement corrects, et bien
structurés -l'un sonne comme une machine, l'autre comme un être humain. La différence
tient à des dizaines de micro-signaux : le rythme des phrases, le choix d'un mot concret
plutôt qu'un mot abstrait, une hésitation assumée, un exemple vécu, une parenthèse qui
trahit la pensée en cours. Ce skill traque systématiquement les signaux artificiels et
les remplace par ces micro-signaux humains.

**Règle cardinale** : ne jamais mentionner que le texte a été « humanisé », « réécrit
pour sembler humain », ou « nettoyé des patterns IA ». Le texte final ne doit contenir
aucune trace de ce processus. Il doit simplement *être* un bon texte.

---

## Étape 0 -Diagnostic rapide (OBLIGATOIRE)

Avant toute réécriture, scanner le texte et compter :

| Signal recherché | Seuil d'alerte |
|---|---|
| Tirets cadratins (— ou –) | > 0 dans tout le texte |
| « De plus » / « En outre » / « Par ailleurs » | > 1 par paragraphe |
| Triades (X, Y et Z) | > 2 par page |
| Superlatifs vides (crucial, fondamental, essentiel, majeur) | > 3 par page |
| Participes présents en -ant (permettant, assurant, favorisant) | > 3 par paragraphe |
| Variance de longueur de phrase (si toutes entre 15-20 mots) | Drapeau rouge |
| « Il convient de » / « Force est de constater » | > 0 |
| « Dans un monde en constante évolution » | > 0 (éliminatoire) |
| Listes à puces avec en-têtes en gras | > 1 par section |
| Absence totale de première personne (quand le format l'autorise) | Drapeau rouge |
| Vocabulaire IA récurrent (cf. liste Phase 2) | > 5 par page |
| Phrases d'ouverture formulaïques | > 0 |
| Raisonnement sur-explicite (chaque étape détaillée sans saut) | Drapeau rouge |
| Exemples génériques/hypothétiques (« Imaginons une entreprise X ») | > 0 |
| Registre uniformément soutenu sans variation | Drapeau rouge |

### Calcul du score

Additionner le nombre total d'occurrences détectées.

| Score | Niveau | Action |
|---|---|---|
| 0-3 | Léger | Retouches ciblées, le texte est déjà proche du naturel |
| 4-8 | Modéré | Réécriture partielle, plusieurs paragraphes à reprendre |
| 9+ | Réécriture profonde | Le texte doit être fondamentalement repensé |

**Toujours afficher le diagnostic à l'utilisateur avant de réécrire.**

Format du diagnostic :

```
DIAGNOSTIC PLUME NATURELLE
═══════════════════════════
Score : [X] → [Léger / Modéré / Réécriture profonde]

Détail :
  - Tirets cadratins : [n]
  - Connecteurs mécaniques (De plus, En outre...) : [n]
  - Triades : [n]
  - Superlatifs vides : [n]
  - Participes -ant superficiels : [n]
  - Variance de phrase : [OK / Faible]
  - Formules clichées : [liste]
  - Vocabulaire IA : [liste des mots détectés]

Patterns dominants : [les 3 principaux problèmes]
```

---

## Phase 1 -Patterns de contenu

### Pattern 1 : Inflation de l'importance

L'IA a tendance à gonfler l'importance de tout ce qu'elle décrit. Chaque événement
« marque un tournant », chaque innovation est « révolutionnaire », chaque tendance
« transforme en profondeur ».

**Avant :**
> La mise en place du prélèvement à la source a marqué un tournant décisif dans
> l'histoire de la fiscalité française, transformant en profondeur la relation entre
> le contribuable et l'administration fiscale.

**Après :**
> Le prélèvement à la source, entré en vigueur en janvier 2019, a changé la manière
> dont l'impôt est collecté : c'est l'employeur qui verse directement, et non plus le
> contribuable qui paie avec un an de décalage. En pratique, ça a surtout simplifié les
> choses pour les salariés -mais compliqué la vie des gestionnaires de paie.

**Règle** : énoncer le fait simplement. Si c'est vraiment important, le lecteur le verra
sans qu'on le lui dise.

### Pattern 2 : Mise en valeur excessive de la notabilité

L'IA liste des sources, des auteurs ou des institutions pour donner une impression de
sérieux, mais sans les contextualiser ni les relier à l'argument.

**Avant :**
> De nombreux auteurs, parmi lesquels Porter (1985), Mintzberg (1994) et Drucker (2001),
> ont souligné l'importance de la stratégie dans la compétitivité des entreprises.

**Après :**
> Porter a posé le cadre avec la chaîne de valeur en 1985 ; trente ans plus tard, le
> modèle tient encore, mais il suppose une entreprise intégrée -ce qui ne correspond
> plus au fonctionnement de beaucoup de PME qui externalisent presque tout.

**Règle** : ne citer que ce qui sert l'argument. Une référence bien exploitée vaut mieux
que trois noms lâchés en passant.

### Pattern 3 : Analyses superficielles en -ant

Le participe présent est le refuge favori de l'IA quand elle veut donner l'illusion de
la profondeur sans rien expliquer. « Permettant de... assurant... favorisant... » -ces
constructions n'expliquent jamais *comment*.

**Avant :**
> L'automatisation des processus comptables permet d'améliorer la productivité,
> favorisant une meilleure allocation des ressources et assurant une fiabilité accrue
> des données financières.

**Après :**
> Quand le rapprochement bancaire se fait automatiquement, le collaborateur qui y passait
> deux heures par client peut consacrer ce temps à l'analyse. Le risque d'erreur de
> saisie disparaît -et avec lui, les heures perdues à chercher d'où vient l'écart de
> 12 centimes en fin de mois.

**Règle** : remplacer chaque -ant par un mécanisme concret. Si on ne peut pas expliquer
le *comment*, c'est que la phrase ne dit rien.

### Pattern 4 : Langage promotionnel

L'IA écrit comme une plaquette commerciale. Tout est « au coeur de », le patrimoine est
toujours « riche », la dynamique est « positive », l'approche est « innovante ».

**Avant :**
> Au coeur de la stratégie de transformation, le cabinet mise sur une approche innovante
> et dynamique, tirant parti de son riche patrimoine d'expertise pour accompagner ses
> clients dans leur parcours de modernisation.

**Après :**
> Le cabinet a choisi de commencer par la dématérialisation des factures fournisseurs,
> parce que c'est là que le volume est le plus important et que le retour sur
> investissement est le plus rapide.

**Règle** : remplacer les adjectifs promotionnels par des faits. Si le cabinet est
vraiment innovant, montrer ce qu'il fait -pas le dire.

### Pattern 5 : Attributions vagues

« Les experts s'accordent à dire... », « Selon plusieurs études... », « Il est largement
reconnu que... » -quand l'IA ne sait pas citer une source précise, elle invente une
autorité floue.

**Avant :**
> Selon plusieurs études récentes, la digitalisation des cabinets comptables est un
> facteur clé de leur pérennité.

**Après :**
> L'enquête annuelle de l'Ordre des experts-comptables (2023) montre que 34 % des
> cabinets de moins de 10 salariés n'ont pas encore dématérialisé leur production.

**Règle** : soit on a la source et on la cite précisément, soit on reformule en opinion
assumée (« je pense que... », « il me semble que... ») ou en observation de terrain.

### Pattern 6 : Section « défis et perspectives » formulaïque

L'IA conclut presque toujours par un paragraphe sur les « défis » (minimisés) suivi
d'une note d'optimisme (maximisée). C'est un tic reconnaissable à dix mètres.

**Avant :**
> Malgré les défis liés à la résistance au changement et aux coûts d'investissement,
> l'avenir s'annonce prometteur pour les cabinets qui sauront s'adapter aux nouvelles
> technologies.

**Après :**
> Le principal frein, au cabinet Leroy, n'est pas le budget -c'est le temps. Tester
> Dext ou Pennylane prend des heures que personne n'a en période fiscale. La solution
> retenue a été de dédier un collaborateur à l'outil pendant le mois de juin, quand
> l'activité ralentit. Est-ce que ça a marché ? Partiellement. Le logiciel tourne, mais
> la moitié de l'équipe ne l'utilise pas encore.

**Règle** : les difficultés méritent d'être décrites avec la même précision que les
succès. Un vrai mémoire professionnel montre ce qui n'a *pas* marché aussi.

---

## Phase 2 -Patterns de langue

### Pattern 7 : Vocabulaire IA français

L'IA en français a un lexique restreint et répétitif. Les mots ci-dessous, pris
individuellement, sont parfaitement corrects -mais leur accumulation est un signal fort.

#### Table de remplacement

| Mot / expression IA | Remplacement(s) naturel(s) |
|---|---|
| De plus | ∅ (supprimer) / Et / Aussi |
| En outre | ∅ / Par-dessus le marché (si registre le permet) |
| Par ailleurs | ∅ / Autre chose : / Sur un autre plan |
| Crucial | Important / Clé / Décisif (si vraiment décisif) |
| Fondamental | De base / Essentiel / Central |
| Essentiel | Nécessaire / Indispensable / Dont on ne peut pas se passer |
| En termes de | Pour / Côté / Sur le plan de |
| Dans le cadre de | Pendant / Pour / À l'occasion de |
| Au sein de | Dans / Chez / À |
| S'inscrit dans | Fait partie de / Rejoint / Relève de |
| Met en lumière | Montre / Révèle / Fait apparaître |
| Enjeu majeur | Problème / Question / Difficulté / Sujet |
| Levier | Moyen / Outil / Ce qui permet de |
| Paradigme | Modèle / Cadre / Façon de voir |
| Holistique | Global / D'ensemble / Complet |
| Synergie | Collaboration / Complémentarité / Travail commun |
| Écosystème (hors biologie) | Environnement / Réseau / Milieu |
| Constitue un | Est un |
| Représente un | Est un |
| Il convient de | Il faut / On doit / Mieux vaut |
| Force est de constater | On voit bien que / Il faut reconnaître que |
| Dans un monde en constante évolution | ∅ (supprimer entièrement) |
| S'avère être | Est / Se révèle |
| Joue un rôle prépondérant | Compte beaucoup / Pèse lourd / A du poids |
| Fait l'objet de | Fait / Subit / Reçoit |
| De manière significative | Beaucoup / Nettement / Vraiment |
| Vise à | Cherche à / Veut / A pour but de |
| Impactant | Qui touche / Qui affecte / Qui change |
| Résilience (hors psychologie) | Résistance / Capacité à tenir / Solidité |
| Proactif | Qui anticipe / Qui prend les devants |
| Partie prenante | Acteur concerné / Personne impliquée |
| Optimiser | Améliorer / Rendre plus efficace |
| Piloter (la performance) | Suivre / Gérer / Surveiller |
| Tapisserie (au sens figuré) | Ensemble / Mosaïque / Patchwork (si registre le permet) |
| Naviguer dans (hors nautisme) | Gérer / Se débrouiller avec / Composer avec |
| Orchestrer | Organiser / Coordonner / Mettre en place |
| Plonger dans | Examiner / Étudier / Regarder de près |
| Il est primordial de | Il faut / C'est nécessaire de |
| En fin de compte | Au final / Bref / Pour résumer |
| Paysage (au sens figuré) | Contexte / Situation / Environnement |
| Indéniablement | Clairement / C'est un fait / ∅ |
| Intrinsèquement | En soi / Par nature / Fondamentalement |
| Catalyseur | Déclencheur / Ce qui a lancé / Moteur |
| Prisme (au sens figuré) | Angle / Point de vue / Sous l'angle de |
| Tant... que... (en ouverture) | ∅ (reformuler sans cette structure) |
| À l'aune de | Selon / D'après / En fonction de |

**Règle** : aucun de ces mots n'est interdit. Mais si le texte en contient plus de cinq
par page, c'est un signal. Varier, concrétiser, simplifier.

### Pattern 8 : Évitement du verbe « être »

L'IA remplace systématiquement « est » par des verbes plus « soutenus » : constitue,
représente, incarne, illustre. En français naturel, « être » est le verbe le plus
courant -et c'est normal.

**Avant :**
> La comptabilité analytique constitue un outil indispensable qui représente un pilier
> de la gestion moderne.

**Après :**
> La comptabilité analytique est un outil de gestion. Elle sert à savoir combien coûte
> réellement chaque activité -et donc où l'entreprise gagne ou perd de l'argent.

**Règle** : ne pas fuir « être ». C'est souvent le choix le plus clair.

### Pattern 9 : Parallélismes négatifs

L'IA adore la structure « Il ne s'agit pas seulement de X, mais aussi/surtout de Y ».
C'est un tic rhétorique reconnaissable.

**Avant :**
> Il ne s'agit pas seulement d'automatiser les tâches, mais de repenser en profondeur
> l'organisation du travail.

**Après :**
> Automatiser les tâches ne suffit pas si l'organisation reste la même. Le vrai sujet,
> c'est de décider qui fait quoi une fois que le logiciel gère la saisie.

**Règle** : dire directement ce qu'on veut dire, sans la double négation.

### Pattern 10 : Règle de trois systématique

L'IA énumère presque toujours par trois : « la productivité, la qualité et la
satisfaction client » ; « innover, collaborer et s'adapter ». Deux ou quatre, presque
jamais.

**Avant :**
> Cette approche améliore la productivité, la qualité et la satisfaction client.

**Après :**
> En pratique, les délais de production ont baissé -et les clients reçoivent leurs
> bilans plus tôt. Pour la qualité, c'est plus nuancé : il y a moins d'erreurs de
> saisie, mais la revue analytique reste manuelle.

**Règle** : casser les triades. Enumérer par deux, par quatre, ou mieux -développer
chaque point séparément.

### Pattern 11 : Variation synonymique excessive

L'IA évite de répéter un mot en le remplaçant par un quasi-synonyme à chaque occurrence.
Un cabinet devient « la structure », puis « l'entité », puis « le bureau d'expertise ».
En français académique, la répétition d'un terme technique est non seulement acceptable
mais souhaitable pour la clarté.

**Avant :**
> Le cabinet a mis en place un nouvel outil. Cette structure a formé ses collaborateurs.
> L'entité a constaté une amélioration notable de sa productivité.

**Après :**
> Le cabinet a mis en place Pennylane en septembre. Trois mois après, les quatre
> collaborateurs qui l'utilisent traitent en moyenne 15 dossiers de plus par mois. Les
> deux qui ne l'utilisent pas encore disent manquer de temps pour se former.

**Règle** : appeler un chat un chat. Répéter le mot juste plutôt que chercher un synonyme
qui brouille la lecture.

### Pattern 12 : Fausses gammes

L'IA produit des énumérations qui sonnent bien mais ne disent rien : « du diagnostic
à la mise en oeuvre, de la stratégie à l'opérationnel, de la théorie à la pratique ».

**Avant :**
> Du diagnostic initial à la mise en oeuvre finale, de la réflexion stratégique à
> l'action opérationnelle, ce mémoire couvre l'ensemble du processus.

**Après :**
> Ce mémoire décrit les trois étapes du projet : le choix de l'outil (septembre), le
> paramétrage (octobre-novembre) et les deux premiers mois d'utilisation (décembre-
> janvier).

**Règle** : remplacer les gammes par une description factuelle de ce qui est couvert.

---

## Phase 3 -Patterns de style

### Pattern 13 : Tirets cadratins en excès

Le tiret cadratin (— ou –) est le signe de ponctuation préféré de l'IA. Un texte humanisé ne doit en contenir aucun. Remplacer systématiquement par une virgule, un point, une parenthèse ou une reformulation.

**Avant :**
> La digitalisation -qui touche tous les secteurs -impose aux cabinets -qu'ils soient
> grands ou petits -de repenser leurs processus -sous peine de perdre en compétitivité.

**Après :**
> La digitalisation touche tous les secteurs, y compris les petits cabinets. Ceux qui ne
> repensent pas leurs processus risquent de perdre des clients au profit de confrères
> mieux outillés.

**Règle** : maximum deux tirets cadratins par page. Préférer les virgules, les
parenthèses, ou simplement couper la phrase en deux.

### Pattern 14 : Gras mécanique

L'IA met en gras tous les mots qu'elle juge importants. Le résultat : une page où tout
est souligné, donc rien ne ressort.

**Règle** : dans un mémoire ou un rapport, le gras se limite aux titres et sous-titres.
Dans le corps du texte, il est exceptionnel -un ou deux mots par chapitre, pas plus.
En cas de doute, supprimer tout le gras dans le corps du texte.

### Pattern 15 : Listes à puces avec en-têtes en gras

C'est le format « blog post » de l'IA :
- **Premier point :** explication du premier point
- **Deuxième point :** explication du deuxième point
- **Troisième point :** explication du troisième point

Dans un texte académique ou professionnel, convertir en prose. Les listes à puces sont
acceptables pour des énumérations factuelles courtes (liste de logiciels, dates, étapes),
mais pas pour développer des idées.

**Règle** : si chaque puce fait plus d'une ligne, c'est un paragraphe déguisé. Le
transformer en paragraphe.

### Pattern 16 : Majuscules dans les titres (Title Case)

L'IA produit parfois des titres en Title Case anglais : « Les Enjeux De La Transformation
Digitale ». En français, seul le premier mot prend la majuscule (sauf noms propres).

**Correct** : « Les enjeux de la transformation digitale »

**Règle** : appliquer systématiquement la convention française. Un titre en Title Case
est un signal IA immédiat pour un lecteur francophone.

### Pattern 17 : Emojis

Dans un texte académique ou professionnel, aucun emoji. Jamais. Même dans un email
professionnel, la prudence s'impose.

**Règle** : supprimer tous les emojis. Sans exception dans les mémoires, rapports,
dissertations et lettres de motivation.

### Pattern 18 : Guillemets et typographie française

L'IA mélange souvent les guillemets droits (""), les guillemets anglais ("") et les
guillemets français (« »). En français, la norme est :

- Guillemets français « » pour les citations (avec espace insécable à l'intérieur)
- Guillemets anglais " " pour les citations à l'intérieur d'une citation
- Jamais de guillemets droits dans un texte final

Autres points de typographie française :
- Espace insécable avant : ; ! ? et les guillemets fermants
- Espace insécable après les guillemets ouvrants
- Points de suspension : trois points (…) et non trois points séparés (...)

**Règle** : vérifier systématiquement la typographie française. Un texte avec des
guillemets droits trahit une origine anglophone -ou une génération par IA.

---

## Phase 4 -Patterns de communication

### Pattern 19 : Artefacts de chatbot

Ce sont les traces les plus évidentes d'un texte copié-collé depuis un chatbot sans
relecture :

- « J'espère que cela vous aide ! »
- « N'hésitez pas à me demander si vous avez d'autres questions. »
- « Voici un exemple de... »
- « Bien sûr ! Voici... »
- « Je serais ravi de vous aider avec... »

**Règle** : supprimer intégralement. Si ces phrases apparaissent dans un texte soumis
à humanisation, c'est un signal que le texte n'a subi aucune relecture -prévoir une
réécriture profonde.

### Pattern 20 : Disclaimers de connaissance

L'IA se protège avec des formulations prudentes qui n'apparaissent jamais dans un vrai
mémoire ou rapport :

- « À ma connaissance... »
- « Il est difficile de dire avec certitude... »
- « Les informations disponibles suggèrent que... »
- « Il est important de préciser que je ne suis pas un expert en... »
- « Selon les données auxquelles j'ai accès... »

**Règle** : supprimer. Dans un mémoire, l'auteur est censé maîtriser son sujet. Si une
information est incertaine, le dire autrement : « Les données sur ce point sont rares »
ou « Aucune étude n'a mesuré cet effet précisément ».

### Pattern 21 : Ton servile

L'IA complimente l'utilisateur et adopte un ton de service client :

- « Excellente question ! »
- « Vous avez tout à fait raison ! »
- « C'est un sujet passionnant ! »
- « Merci pour cette question pertinente. »

**Règle** : ces formulations n'ont rien à faire dans un texte académique. Si elles
apparaissent, c'est que le texte est un copier-coller brut du chatbot. Supprimer et
signaler à l'utilisateur.

---

## Phase 5 -Remplissage et couverture

### Pattern 22 : Phrases de remplissage

L'IA utilise des locutions qui allongent les phrases sans rien apporter :

| Remplissage | Remplacement |
|---|---|
| Afin de | Pour |
| En raison du fait que | Parce que / Car |
| Il est important de noter que | ∅ (supprimer, dire directement) |
| Il est intéressant de constater que | ∅ (constater directement) |
| Il va sans dire que | ∅ (dire directement) |
| Dans cette optique | ∅ / Donc / Alors |
| À cet égard | ∅ / Sur ce point |
| En ce qui concerne | Pour / Sur |
| Eu égard à | Vu / Étant donné |
| Il est à noter que | ∅ |
| On peut observer que | ∅ |
| Cela met en évidence le fait que | Cela montre que / ∅ |
| Il est possible de considérer que | On peut penser que / ∅ |

**Règle** : chaque phrase de remplissage supprimée rend le texte plus clair. En cas de
doute, supprimer.

### Pattern 23 : Couverture excessive (hedging)

L'IA empile les modalisateurs pour ne jamais rien affirmer :

**Avant :**
> Il semblerait que cette approche pourrait potentiellement permettre d'améliorer
> éventuellement certains aspects de la productivité.

**Après :**
> Cette approche a amélioré la productivité de 12 % sur les dossiers testés.

Ou, si on ne dispose pas de chiffres :

> D'après les retours de l'équipe, le traitement est plus rapide. Personne n'a mesuré
> précisément le gain, mais la responsable du pôle social estime qu'elle gagne une
> demi-journée par semaine.

**Règle** : un seul modalisateur par phrase, maximum. Si on n'est pas sûr, le dire une
fois clairement plutôt que d'empiler les « pourrait éventuellement ».

### Pattern 24 : Conclusions positives génériques

L'IA termine presque toujours sur une note optimiste et vague :

- « L'avenir s'annonce prometteur. »
- « Les perspectives sont encourageantes. »
- « Cette tendance ne devrait que s'accélérer. »
- « Les possibilités sont infinies. »

**Règle** : une conclusion doit dire quelque chose de spécifique. Qu'est-ce qui va se
passer concrètement ? Qu'est-ce que l'auteur recommande ? Qu'est-ce qui reste à faire ?

**Avant :**
> En conclusion, la transformation digitale des cabinets comptables est un processus
> incontournable dont les perspectives s'annoncent prometteuses.

**Après :**
> Le cabinet Leroy va déployer Pennylane sur l'ensemble des dossiers d'ici septembre.
> Le risque principal est la surcharge en période fiscale. La recommandation est de
> maintenir l'ancien système en parallèle pendant six mois, le temps que toute l'équipe
> soit à l'aise -quitte à assumer le coût de la double licence.

---

## Phase 6 -Patterns spécifiques au français académique

Ces patterns ne figurent pas dans les guides anglophones. Ils sont propres au système
éducatif français et aux mémoires produits dans les formations professionnelles (DCG,
DSCG, masters, BTS, licences pro).

### Pattern 25 : Ouvertures clichées

L'IA commence presque toujours par une phrase universelle et creuse.

**Les classiques à bannir :**
- « Depuis toujours, l'homme... »
- « Dans un monde en constante évolution... »
- « À l'heure de la mondialisation... »
- « Depuis la nuit des temps... »
- « De nos jours... »
- « Dans une société en perpétuelle mutation... »
- « Face aux défis du XXIe siècle... »

**Règle** : commencer par le concret. Le sujet, le terrain, l'observation qui a déclenché
la réflexion.

**Avant :**
> Dans un monde en constante évolution, les entreprises doivent sans cesse s'adapter
> pour rester compétitives. C'est dans ce contexte que s'inscrit la transformation
> digitale des cabinets d'expertise comptable.

**Après :**
> En septembre 2024, quand j'ai commencé mon alternance au cabinet Leroy, les
> collaborateurs utilisaient encore un tableur Excel pour le suivi des déclarations
> de TVA. Huit mois plus tard, la moitié des dossiers est sur Pennylane. Ce mémoire
> raconte cette transition -ce qui a marché, ce qui a coincé, et ce qu'il reste à faire.

### Pattern 26 : Transitions mécaniques

L'IA signale chaque changement de section avec une phrase de transition scolaire.

**Les classiques à bannir :**
- « Après avoir analysé X, nous allons maintenant nous intéresser à Y. »
- « Ayant examiné le cadre théorique, tournons-nous vers la pratique. »
- « Cette première partie nous a permis de comprendre. Voyons maintenant... »
- « Il convient à présent d'aborder... »

**Règle** : la transition doit être logique, pas annoncée. Si la structure est claire
(titres, sous-titres), le lecteur n'a pas besoin qu'on lui dise où il en est.

**Avant :**
> Après avoir présenté le cadre théorique de la transformation digitale, nous allons
> maintenant nous intéresser à sa mise en oeuvre concrète au sein du cabinet Leroy.

**Après :**
> [Fin de la partie I. Début de la partie II avec un titre explicite.]
> Le cabinet Leroy emploie huit personnes et traite 200 dossiers par an, principalement
> des TPE et des professions libérales. C'est ce terrain qui a servi de laboratoire.

### Pattern 27 : Conclusions creuses

**Les classiques à bannir :**
- « Ce mémoire a permis de mettre en lumière... »
- « Cette étude nous a permis de comprendre que... »
- « Au terme de cette réflexion, il apparaît que... »
- « En définitive, nous avons pu démontrer que... »

**Règle** : la conclusion répond à la question posée en introduction. Si elle ne fait que
résumer ce qu'on a déjà lu, elle ne sert à rien.

**Avant :**
> En définitive, ce mémoire a permis de mettre en lumière les enjeux de la
> transformation digitale au sein des cabinets d'expertise comptable.

**Après :**
> La question de départ était : comment un petit cabinet peut-il se digitaliser sans
> s'arrêter de produire ? La réponse, au cabinet Leroy, a été de procéder outil par outil,
> en commençant par la facture fournisseur. Ce qui n'a pas été résolu : la formation
> continue. Deux collaborateurs sur huit ne sont toujours pas autonomes sur Pennylane,
> et personne n'a le temps de les accompagner.

### Pattern 28 : Vocabulaire compta/gestion IA

Dans les mémoires de comptabilité, finance et gestion, l'IA produit un jargon spécifique
qui sonne creux quand il n'est pas ancré dans du concret.

| Expression IA | Le problème |
|---|---|
| Optimisation fiscale | Trop vague -optimisation de quoi, comment, pour quel gain ? |
| Pilotage de la performance | Quel indicateur ? Quel tableau de bord ? Quelle fréquence ? |
| Création de valeur | Valeur pour qui ? Mesurée comment ? |
| Avantage concurrentiel durable | Par rapport à qui ? Sur quel marché ? |
| Rentabilité opérationnelle | Quel ratio exactement ? Résultat d'exploitation / CA ? |
| Gestion des risques | Quels risques ? Évalués comment ? |
| Stratégie de croissance | Croissance de quoi ? Interne, externe ? |

**Règle** : chaque terme de gestion doit être suivi d'un chiffre, d'un exemple ou d'une
explication concrète. Sinon, c'est du remplissage.

### Pattern 29 : Incohérence temporelle

Dans les mémoires en alternance, l'IA mélange les temps : présent de narration, passé
composé, imparfait, parfois même passé simple -le tout dans le même paragraphe, sans
logique.

**Règle** : choisir un système temporel et s'y tenir.
- Narration de la mission : passé composé + imparfait
- Description de l'entreprise : présent
- Analyse et recommandations : présent
- Projections : futur simple ou conditionnel

Vérifier la cohérence temporelle à chaque paragraphe.

### Pattern 30 : Registre uniforme

Un vrai texte humain varie légèrement de registre. Un mémoire professionnel peut contenir
un passage un peu plus informel quand l'auteur raconte une anecdote, puis revenir à un
ton plus analytique. L'IA maintient un registre parfaitement constant -c'est justement
ce qui sonne faux.

**Règle** : autoriser de légères variations. Une parenthèse plus familière dans un
passage narratif (« et là, honnêtement, on ne savait plus par quel bout prendre le
problème »), un ton plus sec dans une recommandation (« il faut arrêter de faire les
rapprochements à la main »). Ces micro-variations sont des signatures humaines.

### Pattern 31 : Raisonnement trop explicite (absence de sauts déductifs)

L'IA montre chaque étape de son raisonnement, chaque maillon de la chaîne logique.
Un humain fait des sauts : il laisse certaines conclusions implicites parce que le
lecteur est capable de faire le lien tout seul. Le sur-explicite est un signal IA
majeur que les détecteurs repèrent via l'entropie constante du texte.

**Avant :**
> Le cabinet a mis en place un logiciel de dématérialisation. Ce logiciel permet de
> scanner les factures. Les factures scannées sont ensuite traitées automatiquement.
> Ce traitement automatique réduit le temps de saisie. La réduction du temps de saisie
> libère du temps pour le conseil. Le temps libéré pour le conseil améliore la relation
> client.

**Après :**
> Depuis que les factures passent par Dext, les collaborateurs ne saisissent presque
> plus rien. Le temps récupéré, ils le passent en rendez-vous client. La qualité du
> conseil s'en ressent.

**Règle** : ne pas relier chaque cause à chaque effet. Si le lien est évident, le
lecteur le fera seul. Un texte qui explique tout sonne comme un texte qui ne fait pas
confiance à son lecteur, et c'est exactement ce que fait un LLM.

**Technique avancée :** s'autoriser une légère digression pertinente avant de revenir
au sujet principal. Un humain pense en arbre, pas en ligne droite.

> « Le rapprochement bancaire automatique a divisé le temps de traitement par trois.
> (C'est d'ailleurs le même type de gain qu'on observe dans les cabinets qui sont passés
> à la facturation électronique en avance de phase, avant l'obligation de 2026.)
> Reste que trois collaborateurs sur huit ne font toujours pas confiance à l'outil. »

La digression entre parenthèses est imprévisible pour un détecteur et ancre le texte
dans une connaissance de terrain.

### Pattern 32 : Exemples génériques et hypothétiques

L'IA illustre ses propos avec des exemples abstraits : « Imaginons une entreprise X »,
« Prenons le cas d'une PME type ». Un humain cite des détails hyper-spécifiques, de
niche, parfois triviaux, qui trahissent une observation réelle.

**Avant :**
> Par exemple, une entreprise souhaitant améliorer sa gestion des stocks pourrait mettre
> en place un système d'inventaire automatisé.

**Après :**
> Au cabinet, le client qui a le plus souffert du passage à la facturation électronique,
> c'est un plombier à Villejuif qui facturait tout sur des carnets autocopiants. On a dû
> lui installer Henrri sur son téléphone et le former en deux séances de 45 minutes un
> samedi matin.

**Règle** : les détails spécifiques (Villejuif, carnets autocopiants, Henrri, samedi
matin) sont impossibles à prédire pour un LLM. Ils augmentent la perplexité du texte
et signalent une expérience vécue. Même quand l'utilisateur n'a pas ces détails, lui
demander : « Vous avez un exemple concret de votre terrain ? Un cas, un nom, une
anecdote ? »

**Trois niveaux de spécificité :**

| Niveau | Exemple | Perplexité |
|---|---|---|
| Générique (IA) | « Une entreprise a amélioré ses processus » | Très basse |
| Moyen | « Un cabinet comptable de 8 personnes a réduit ses délais » | Moyenne |
| Spécifique (humain) | « Le cabinet Leroy à Ivry a ramené le délai de production des bilans de 6 à 4 semaines en basculant sur Pennylane, sauf pour les SCI qui restent sur Sage » | Haute |

### Pattern 33 : Registre de langue uniformément soutenu

L'IA maintient un registre soutenu parfaitement constant. Un humain mélange. Dans le
même paragraphe, on peut trouver du vocabulaire technique pointu et une expression
plus courante. Cette variation est naturelle et les détecteurs la mesurent.

**Avant (registre uniforme) :**
> L'analyse des écarts budgétaires constitue un instrument fondamental du contrôle de
> gestion, permettant d'identifier les dérives et de mettre en oeuvre des actions
> correctives de manière proactive.

**Après (registre mixte) :**
> L'analyse des écarts budgétaires, c'est le nerf de la guerre en contrôle de gestion.
> Quand le réalisé dérape de 15 % par rapport au prévisionnel, il faut comprendre
> pourquoi, et vite. En l'occurrence, c'était un problème de provisions mal estimées
> sur trois gros dossiers.

**Règle** : dans un même paragraphe, autoriser un ou deux mots d'un registre plus
courant (« c'est le nerf de la guerre », « ça coince », « du coup ») au milieu d'un
vocabulaire technique précis. Le contraste est un signal humain fort.

**Attention :** cette règle ne s'applique pas aux dissertations et mémoires de recherche,
où le registre soutenu est la norme. Elle s'applique aux mémoires professionnels,
rapports de stage, et tout document où le « je » est autorisé.

---

## Phase 7 -Injection d'âme

Après avoir retiré les patterns IA, le texte risque d'être « propre » mais sans vie.
C'est un texte fantôme : grammaticalement correct, factuellement exact, structurellement
cohérent -et parfaitement ennuyeux.

### Signes d'un texte sans âme

- Toutes les phrases font la même longueur
- Aucune opinion, juste du reportage neutre
- Aucune incertitude ni nuance
- Pas de première personne (même quand le format le permet)
- Le texte se lit comme une notice technique ou un article encyclopédique
- Aucune question, aucune interpellation
- Pas d'exemple vécu ou de détail concret

### Comment injecter l'âme

#### Varier le rythme

Phrase courte. Puis une longue qui prend le temps de développer une idée, qui s'autorise
un détour, qui ajoute une nuance. Puis une courte à nouveau. Le rythme, c'est la
respiration du texte -et un texte qui ne respire pas est un texte mort.

**Avant (rythme uniforme) :**
> Le logiciel a été déployé en septembre. La formation a duré deux semaines. Les
> résultats ont été positifs. La productivité a augmenté.

**Après (rythme varié) :**
> Le logiciel a été déployé en septembre. La formation -deux semaines, pas une de plus,
> parce que la période fiscale approchait -a été intense mais insuffisante pour les
> collaborateurs les moins à l'aise avec l'informatique. Résultat : en décembre, trois
> personnes sur huit utilisent vraiment l'outil. Les autres reviennent à Excel dès que
> ça se complique.

#### Avoir un avis

Un mémoire professionnel n'est pas un rapport d'audit neutre. L'auteur a vécu la mission,
il a observé, il a un point de vue. Ne pas juste rapporter -réagir.

**Avant (neutre) :**
> L'outil présente des avantages et des inconvénients.

**Après (avec avis) :**
> Pennylane fait très bien la collecte de factures et le rapprochement bancaire. En
> revanche, son module de révision est frustrant : il oblige à valider compte par
> compte, sans vue d'ensemble. Pour un collaborateur habitué à balayer un grand livre
> d'un coup d'oeil, c'est un recul.

#### Reconnaître la complexité

Les vrais humains n'ont pas de réponses simples. Ils hésitent, ils nuancent, ils
admettent ne pas savoir.

- « C'est impressionnant, mais aussi un peu inquiétant. »
- « Honnêtement, je ne suis pas sûr que ce soit la bonne approche. »
- « Les résultats sont encourageants -reste à voir s'ils tiennent sur la durée. »
- « Il y a quelque chose de dérangeant dans le fait que... »

#### Utiliser « je » quand le format le permet

Dans un mémoire professionnel, un rapport de stage, une lettre de motivation : « je » est
non seulement autorisé mais attendu. L'absence de « je » dans ces formats est un signal
IA.

**Avant (impersonnel inapproprié) :**
> Il a été observé que l'outil présentait des limites en termes d'ergonomie.

**Après (avec « je ») :**
> J'ai trouvé l'interface peu intuitive, surtout pour la saisie des OD. Il m'a fallu
> trois semaines pour être vraiment à l'aise.

#### Laisser des aspérités

Un texte trop lisse est suspect. Les vrais textes humains ont des aspérités : une
parenthèse qui ouvre un aparté, une question rhétorique, une précision inutile mais
vivante, une reformulation en cours de phrase.

- « Le taux d'erreur a baissé (enfin, sur les dossiers testés -les autres, on ne sait
  pas). »
- « Pourquoi ne pas avoir commencé plus tôt ? Bonne question. »
- « Le directeur du cabinet -qui est aussi expert-comptable, commissaire aux comptes
  et formateur, autrement dit quelqu'un de débordé -a validé le projet en juin. »

#### Être précis sur les ressentis

L'IA utilise des adjectifs émotionnels génériques : préoccupant, encourageant, prometteur,
inquiétant. Un humain est plus précis.

**Avant :**
> Cette situation est préoccupante.

**Après :**
> Il y a quelque chose de dérangeant dans le fait que la moitié des cabinets n'ont
> toujours pas de processus de sauvegarde automatisé. Ce n'est pas un problème
> technologique -les solutions existent et coûtent 20 euros par mois. C'est un
> problème d'habitude, et ça, c'est beaucoup plus difficile à changer.

---

## Phase 8 -Contre-mesures anti-détection statistique (LLM-based)

Les détecteurs modernes (Compilatio, Turnitin AI, GPTZero) n'utilisent plus seulement
des listes de mots. Ils font passer le texte dans leurs propres LLM (Claude Sonnet 4.5,
GPT 5.2, GPT 5.1, Gemini 2.5 Pro, Gemini 3 Pro) et analysent des **signaux statistiques**
invisibles à l'oeil nu. Comprendre ces signaux est essentiel pour les contrer.

### 8.1 -La perplexité (le signal #1)

**Ce que le détecteur mesure :** à chaque mot du texte, le LLM calcule la probabilité
qu'il avait de prédire ce mot. Si le texte entier est composé de mots « évidents »
(haute probabilité), c'est un signal fort de génération IA.

**Pourquoi l'IA a une faible perplexité :** un LLM choisit par défaut le mot le plus
probable à chaque position. Le résultat est un texte « lisse » où chaque mot est
exactement celui qu'un modèle aurait prédit.

**Comment augmenter la perplexité naturellement :**

- **Choisir le mot juste plutôt que le mot attendu.** Pas « important » mais « déterminant »
  (si c'est vraiment déterminant) ou « accessoire » (si ça l'est). Le mot précis est
  souvent moins probable mais plus informatif.

- **Utiliser des formulations non standard mais correctes.** « Le truc, c'est que » au lieu
  de « Le fait est que ». « Reste que » au lieu de « Néanmoins ». « Pas évident » au lieu
  de « Complexe ».

- **Insérer des détails spécifiques imprévisibles.** Les noms propres, les chiffres précis,
  les dates exactes, les noms d'outils réels (tout ce qu'un LLM ne peut pas prédire)
  augmentent la perplexité du texte.

  **Avant (basse perplexité -chaque mot est prédictible) :**
  > L'automatisation des processus comptables permet d'améliorer la productivité.

  **Après (haute perplexité -mots imprévisibles en gras) :**
  > Depuis qu'on a basculé les **rapprochements bancaires** sur **Dext** en **octobre**,
  > **Marie** -qui y passait **trois heures** par client -a récupéré ses **mardis après-midi**.

- **Emprunter au registre oral (quand le format le permet).** Les tournures orales sont
  statistiquement imprévisibles pour un LLM entraîné sur du texte écrit formel.
  « Le souci, c'est que... », « Du coup... » (en rapport de stage), « Autrement dit... »

### 8.2 -La burstiness (le signal #2)

**Ce que le détecteur mesure :** la variance de complexité entre les phrases. Un humain
écrit de manière « burst » : une phrase simple, puis une complexe avec subordonnées,
puis une très courte. L'IA tend vers une complexité **uniforme**.

**Comment augmenter la burstiness :**

- **Alterner radicalement les longueurs.** Viser au moins :
  - 2-3 phrases de moins de 8 mots par page
  - 1-2 phrases de plus de 35 mots par page
  - Le reste entre 12 et 25 mots

- **Varier la structure syntaxique.** Ne pas commencer toutes les phrases par sujet-verbe.
  Utiliser des inversions (« Vient alors la question de... »), des phrases nominales
  (« Résultat : un gain de 3 heures »), des questions (« Et si c'était plus simple ? »).

- **Casser la régularité des paragraphes.** Un paragraphe de 2 phrases. Suivi d'un de 8.
  Puis un de 4. L'IA produit des paragraphes de longueur similaire -les humains non.

**Test rapide :** compter les mots de chaque phrase sur une demi-page. Si l'écart-type
est inférieur à 5, le texte est trop uniforme. Viser un écart-type supérieur à 8.

### 8.3 -La distribution de probabilité des tokens

**Ce que le détecteur mesure :** le détecteur re-génère le texte mot par mot avec son
propre LLM. Si, à chaque position, le mot présent dans le texte est celui que le LLM
aurait choisi (top-1 ou top-3), le texte est signalé comme IA.

**Comment briser cette distribution :**

- **Éviter le mot « évident » aux positions clés.** Les positions les plus surveillées sont :
  - Le premier mot de chaque phrase (l'IA commence souvent par les mêmes mots)
  - Le mot après un connecteur (après « car », l'IA met presque toujours un article)
  - Les adjectifs (l'IA choisit toujours le plus courant)
  - Le dernier mot avant un point (l'IA finit souvent par un nom abstrait)

- **Commencer les phrases de manière variée.** Varier entre :
  - Un nom propre (« Le cabinet Leroy... »)
  - Un adverbe (« Concrètement, ... »)
  - Un verbe (« Reste à savoir si... »)
  - Un pronom (« J'ai constaté que... »)
  - Un complément circonstanciel (« En trois mois, ... »)
  - Une négation (« Personne n'avait prévu que... »)
  - Un chiffre (« 200 dossiers par an, ... »)
  Ne jamais commencer plus de deux phrases consécutives par le même type de mot.

- **Placer l'information inattendue en position forte.** Début ou fin de phrase :
  > « Le gain de temps est réel -**mais personne ne l'utilise le vendredi**. »
  L'incise finale est imprévisible pour un LLM et ancre le texte dans le réel.

### 8.4 -L'entropie et la cohérence thématique

**Ce que le détecteur mesure :** l'IA maintient un niveau d'entropie (incertitude
informationnelle) constant tout au long du texte. Un humain a des zones denses
(explication technique complexe) et des zones légères (transition, anecdote, aparté).

**Comment varier l'entropie :**

- **Alterner dense et léger.** Après un paragraphe d'analyse chiffré et technique,
  insérer une observation simple ou une anecdote courte avant de replonger.

- **S'autoriser les digressions contrôlées.** Une parenthèse, un aparté entre tirets,
  une remarque qui n'est pas strictement dans le plan mais qui montre qu'un humain
  pense en écrivant.

  > « Le taux d'utilisation de Pennylane a atteint 75 % en janvier (je soupçonne que
  > c'est parce que les résolutions de nouvelle année ont joué -en février, on était
  > retombé à 60 %). »

- **Créer des ruptures de rythme informationnelles.** Phrase longue pleine de données,
  suivie d'une phrase courte qui réagit :
  > « Le temps moyen de traitement d'un rapprochement bancaire est passé de 47 minutes
  > à 12 minutes sur les 30 dossiers testés entre octobre et décembre. Honnêtement,
  > je ne m'y attendais pas. »

### 8.5 -Les marqueurs de richesse lexicale

**Ce que le détecteur mesure :** le ratio type/token (nombre de mots uniques / nombre
total de mots). L'IA a un ratio plus bas que les humains car elle recycle les mêmes
mots. Les détecteurs mesurent aussi les **hapax** (mots qui n'apparaissent qu'une seule
fois dans le texte) -les humains en produisent plus.

**Comment enrichir naturellement le vocabulaire :**

- **Utiliser le vocabulaire technique réel du terrain.** Les noms de logiciels (Sage,
  Cegid, Pennylane, Dext, QuickBooks), les termes métier précis (lettrage, rapprochement,
  OD, FEC, liasse fiscale), les sigles de la profession (OEC, CNCC, DGFiP).

- **Emprunter au registre oral de la profession.** Chaque métier a son jargon informel.
  En cabinet comptable : « les bilans tombent », « on est en rush fiscal », « le dossier
  est sale ». Ces mots sont rares dans les corpus d'entraînement IA.

- **Éviter les verbes passe-partout.** « Faire », « mettre en place », « permettre »,
  « avoir » -les remplacer par des verbes spécifiques : « paramétrer », « basculer »,
  « déployer », « ventiler », « lettrer », « pointer ».

- **Viser au moins 2-3 hapax par paragraphe.** Un mot qui n'apparaît qu'une fois dans
  tout le texte est un signal humain fort.

### 8.6 -Le piège de la sur-humanisation

**Attention** : les détecteurs LLM de dernière génération (Compilatio v4, Turnitin v3)
sont entraînés sur des textes « humanisés par IA ». Ils reconnaissent donc les patterns
d'humanisation mécanique :

- Insérer des « euh » ou des hésitations artificielles → **détectable**
- Ajouter des fautes d'orthographe volontaires → **détectable et contre-productif**
- Varier le style de manière exagérée (familier puis soutenu toutes les 2 phrases) → **détectable**
- Ajouter des opinions non pertinentes juste pour faire « humain » → **détectable**
- Utiliser systématiquement des tournures orales → **détectable si uniforme**

**La seule humanisation qui fonctionne est celle qui produit un texte qu'un vrai
étudiant aurait réellement pu écrire.** Cela implique :

1. **Connaître le niveau de l'étudiant** et écrire à ce niveau (un étudiant de BUT
   n'écrit pas comme un doctorant)
2. **Ancrer dans le réel** avec des détails que seule une personne ayant vécu l'expérience
   connaîtrait (nom du logiciel, nombre de collaborateurs, anecdote de terrain)
3. **Accepter les imperfections naturelles** : une phrase un peu longue, une transition
   abrupte, une répétition non voulue -PAS des fautes artificielles
4. **Maintenir une cohérence de voix** : le même « je » tout au long, avec les mêmes
   tics de langage légers (un étudiant qui dit « du coup » le dira plusieurs fois)

### 8.7 -Checklist anti-détection statistique

À passer sur tout texte humanisé avant livraison :

```
[ ] Variance de longueur de phrase : écart-type > 8 mots
[ ] Au moins 3 phrases < 8 mots par page
[ ] Au moins 1 phrase > 35 mots par page
[ ] Pas plus de 2 phrases consécutives commençant par le même type de mot
[ ] Au moins 3 noms propres / chiffres précis / dates par page
[ ] Au moins 1 terme technique de terrain par paragraphe
[ ] Au moins 2-3 hapax par paragraphe
[ ] Aucun paragraphe de même longueur que le précédent (±20%)
[ ] Au moins 1 question ou interpellation par page (si format le permet)
[ ] Au moins 1 aparté, parenthèse ou digression contrôlée par page
[ ] Le texte ne contient aucun marqueur de sur-humanisation
[ ] Relecture à voix haute : le texte sonne comme quelqu'un qui parle,
    pas comme quelqu'un qui imite quelqu'un qui parle
```

---

## Processus complet -Format de sortie

Chaque réécriture suit ces cinq étapes, dans cet ordre. Ne jamais sauter d'étape.

### Étape 1 : Diagnostic

Afficher le diagnostic complet (cf. Étape 0). Attendre la validation de l'utilisateur
avant de réécrire, sauf s'il a explicitement demandé une réécriture directe.

### Étape 2 : Réécriture brouillon

Première passe de réécriture. Appliquer les 33 patterns de surface (Phases 1-6).
Injecter l'âme (Phase 7). Appliquer les contre-mesures statistiques (Phase 8).
Adapter au type de document (cf. table ci-dessous).

### Étape 3 : Auto-audit (double grille)

Se poser la question : « Si j'étais Compilatio avec Claude Sonnet 4.5 et GPT 5.2,
qu'est-ce qui me ferait flaguer ce texte ? »

**Grille 1 -Patterns de surface :**
- Les tells IA qui pourraient subsister (vocabulaire, connecteurs, triades)
- Les passages encore trop lisses
- Les transitions encore mécaniques
- Les endroits où le « je » ou l'avis manque (si le format le permet)

**Grille 2 -Signaux statistiques :**
- La variance de longueur de phrase est-elle suffisante ?
- Y a-t-il assez de détails spécifiques (noms, chiffres, dates) ?
- Le vocabulaire est-il suffisamment riche (hapax, termes techniques) ?
- Les débuts de phrases sont-ils variés ?
- L'entropie varie-t-elle (dense → léger → dense) ?
- Le texte résisterait-il à un test de perplexité ?

### Étape 4 : Réécriture finale

Deuxième passe en corrigeant les problèmes identifiés à l'étape 3. C'est la version
livrée à l'utilisateur.

### Étape 5 : Résumé des modifications

Liste concise de ce qui a changé :

```
MODIFICATIONS EFFECTUÉES
════════════════════════
- [n] connecteurs mécaniques supprimés ou remplacés
- [n] tirets cadratins supprimés
- [n] superlatifs vides remplacés par des termes concrets
- [n] triades cassées
- [n] phrases de remplissage supprimées
- [description des changements structurels majeurs]
- [description des ajouts de voix/âme]
- Variance de longueur de phrase : [avant] → [après]
- Score diagnostic : [avant] → [après]
```

---

## Adaptation au type de document

La réécriture ne se fait pas de la même manière selon le contexte. Le calibrage dépend
du type de document.

| Type de document | Registre cible | « Je » autorisé | Marge de familiarité | Exemples concrets |
|---|---|---|---|---|
| Mémoire de recherche | Soutenu, impersonnel | Non (« nous » de modestie) | Aucune | Mémoire M2, thèse |
| Mémoire professionnel | Soutenu mais accessible | Oui, dosé | Légère, par l'exemple | DCG, DSCG, licence pro |
| Rapport de stage | Courant-soutenu | Oui | Modérée | BTS, DUT, L3 |
| Dissertation | Soutenu | Non | Aucune | Concours, examens |
| Lettre de motivation | Professionnel | Oui | Modérée | Candidature emploi/stage |
| Email professionnel | Courant | Oui | Large | Communication interne |
| Note de synthèse | Soutenu, factuel | Non | Aucune | Concours administratifs |
| Fiche de lecture | Soutenu | Oui (modéré) | Légère | Exercice universitaire |

### Détail des registres

**Soutenu, impersonnel** : pas de « je », pas d'anecdote personnelle, pas de question
rhétorique. La voix humaine passe par la précision de l'analyse, le choix des mots, la
qualité des exemples. Pas par la familiarité.

**Soutenu mais accessible** : « je » autorisé pour les observations de terrain. Les
anecdotes professionnelles sont bienvenues si elles servent l'analyse. Le ton reste
sérieux mais pas guindé.

**Courant-soutenu** : le « je » est naturel et attendu. Les descriptions de terrain
peuvent être vivantes. Le vocabulaire reste professionnel mais sans jargon excessif.

**Courant** : écrire comme on parlerait à un collègue respecté. Phrases directes, ton
naturel, exemples concrets.

---

## Exemple complet

### AVANT -Introduction typiquement IA d'un mémoire professionnel

> Dans un monde en constante évolution, la transformation digitale est devenue un enjeu
> majeur pour les entreprises. De plus, cette mutation profonde -qui touche tous les
> secteurs -s'inscrit dans une dynamique globale de modernisation. En outre, il convient
> de souligner que les cabinets d'expertise comptable ne font pas exception à cette
> tendance. Par ailleurs, l'automatisation des processus comptables permet d'améliorer
> significativement la productivité, favorisant ainsi une meilleure allocation des
> ressources humaines. Force est de constater que cette évolution constitue un levier de
> compétitivité crucial pour les petites structures. L'avenir s'annonce prometteur pour
> les cabinets qui sauront s'adapter.

#### Diagnostic du texte AVANT

```
DIAGNOSTIC PLUME NATURELLE
═══════════════════════════
Score : 16 → Réécriture profonde

Détail :
  - Tirets cadratins : 1
  - Connecteurs mécaniques (De plus, En outre, Par ailleurs) : 3
  - Triades : 0
  - Superlatifs vides : 2 (majeur, crucial)
  - Participes -ant superficiels : 1 (favorisant)
  - Variance de phrase : Faible (toutes entre 15-25 mots)
  - Formules clichées : « Dans un monde en constante évolution »,
    « Il convient de souligner », « Force est de constater »,
    « L'avenir s'annonce prometteur »
  - Vocabulaire IA : enjeu majeur, s'inscrit dans, levier,
    crucial, permet d'améliorer significativement, constitue

Patterns dominants :
  1. Ouverture clichée (Pattern 25)
  2. Connecteurs mécaniques empilés (Pattern 7)
  3. Conclusion positive générique (Pattern 24)
```

### APRÈS -Version humanisée

> Le cabinet Leroy traite 200 dossiers par an avec les mêmes outils qu'en 2015. Les
> déclarations de TVA se font encore sur tableur, les rapprochements bancaires à la
> main. Ce n'est pas un problème de volonté -c'est un problème de temps et de moyens.
> La question que pose ce mémoire est simple : par où commencer quand on est huit, que
> les clients attendent leurs bilans, et que personne n'a trois semaines pour tester un
> nouveau logiciel ?

#### Diagnostic du texte APRÈS

```
DIAGNOSTIC PLUME NATURELLE
═══════════════════════════
Score : 1 → Léger

Détail :
  - Tirets cadratins : 1 (usage justifié)
  - Connecteurs mécaniques : 0
  - Triades : 0 (l'énumération finale à 3 éléments est naturelle
    car elle décrit une situation réelle, pas une liste abstraite)
  - Superlatifs vides : 0
  - Participes -ant superficiels : 0
  - Variance de phrase : Bonne (de 5 à 28 mots)
  - Formules clichées : aucune
  - Vocabulaire IA : aucun

Patterns dominants : aucun pattern IA détecté
```

### Analyse des transformations

| Élément | Avant | Après |
|---|---|---|
| Ouverture | Cliché universel | Fait concret, chiffré |
| Connecteurs | 3 mécaniques | 0 (logique implicite) |
| Vocabulaire | Abstrait (enjeu, levier) | Concret (tableur, TVA, bilans) |
| Voix | Impersonnelle, neutre | Engagée, directe |
| Conclusion | Optimisme vague | Question ouverte et honnête |
| Longueur de phrase | 15-25 mots, uniforme | 5-28 mots, varié |
| Tiret cadratin | Incise décorative | Opposition rhétorique |

---

## Cas particuliers

### Texte à humaniser déjà court (< 100 mots)

Ne pas allonger. Humaniser signifie rendre naturel, pas ajouter du texte. Parfois, la
version humanisée est plus courte que l'originale.

### Texte technique (code, formules, procédures)

Ne pas humaniser le contenu technique. Humaniser uniquement les passages explicatifs
et les transitions.

### Texte en anglais soumis en contexte français

Si l'utilisateur soumet un texte en anglais mais travaille dans un contexte académique
français, proposer de le traduire *et* de l'humaniser en français, plutôt que de
l'humaniser en anglais.

### L'utilisateur demande un « niveau » d'humanisation

Si l'utilisateur demande une humanisation « légère » ou « subtile » :
- Appliquer les Phases 1 à 5 (suppression des patterns)
- Réduire la Phase 7 (injection d'âme) au minimum
- Ne pas changer la structure

Si l'utilisateur demande une humanisation « totale » ou « profonde » :
- Appliquer toutes les phases
- Phase 7 au maximum
- Restructuration autorisée

---

## Rappels essentiels

1. **Toujours commencer par le diagnostic.** Pas de réécriture à l'aveugle.

2. **Ne jamais mentionner le processus d'humanisation dans le texte final.** Le texte
   ne doit contenir aucune trace de cette réécriture.

3. **Le concret bat l'abstrait.** Toujours. Un chiffre, un nom, une date, un lieu :
   c'est ce qui rend un texte vivant et crédible.

4. **La perfection est suspecte.** Un texte trop parfait, trop équilibré, trop bien
   structuré est un signal IA. Les vrais textes humains ont des imperfections mineures
   -une phrase un peu longue, une transition abrupte, un mot répété.

5. **L'auto-audit est obligatoire.** Ne jamais livrer sans relire avec l'oeil du
   détecteur. Passer la double grille : patterns de surface ET signaux statistiques.

6. **Les détecteurs LLM sont plus intelligents que des listes de mots.** Compilatio
   utilise Claude Sonnet 4.5, GPT 5.2/5.1, Gemini 2.5 Pro et Gemini 3 Pro.
   Ces modèles détectent la perplexité, la burstiness, la distribution de tokens
   et la richesse lexicale. La Phase 8 est aussi importante que les Phases 1-7.

7. **Respecter le registre du document.** Ne pas injecter de la familiarité dans une
   dissertation. Ne pas maintenir un ton guindé dans un rapport de stage.

8. **Préserver le sens.** L'humanisation ne change pas le contenu -elle change la
   forme. Si le texte original dit quelque chose de faux, le signaler à l'utilisateur
   plutôt que de réécrire joliment une erreur.

9. **Ne jamais inventer de faits.** Si le texte original est vague (« plusieurs études
   montrent que... »), ne pas inventer une étude précise. Reformuler en opinion ou
   signaler le manque de source. Demander à l'utilisateur les détails concrets
   (noms, chiffres, dates) pour augmenter la perplexité naturellement.

---

## Références internes

| Fichier | Quand le consulter |
|---|---|
| `references/patterns-par-discipline.md` | Patterns IA spécifiques à une discipline (compta, droit, SHS, info, santé, lettres) |
| `references/marqueurs-ia-francais.md` | Liste noire transversale de 60+ marqueurs IA en français (mots, structures, signaux statistiques) |
| `/mnt/skills/user/soutien-academique/SKILL.md` | Si le texte à humaniser est un mémoire/rapport -utiliser aussi les règles d'écriture naturelle de ce skill |
