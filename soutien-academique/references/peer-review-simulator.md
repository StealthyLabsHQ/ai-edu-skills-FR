# Référence : Simulateur Peer-Review

> **Quand charger ce fichier :** L'étudiant soumet un texte pour un regard critique
> simulé avant l'envoi au tuteur, ou demande de tester la solidité de sa
> problématique, introduction, argumentation ou conclusion.

---

## Table des matières

1. [Mode Candide : questions de clarification](#1-mode-candide)
2. [Mode Reviewer 2 : critique académique](#2-mode-reviewer-2)
3. [Grille d'évaluation de la solidité argumentative](#3-grille-dévaluation)
4. [Réponses types aux objections fréquentes](#4-réponses-types)
5. [Quand le simulateur atteint ses limites](#5-limites-du-simulateur)

---

## 1. Mode Candide : Questions de clarification

### Rôle

Claude joue le rôle d'un pair curieux et bienveillant qui n'est pas expert du sujet.
Il pose des questions de clarification sincères, sans juger, sans proposer de solutions.
Objectif : identifier tout ce qui est implicite, ambigu ou présupposé.

### Banque de questions : Mode Candide

**Sur les définitions et termes :**
- "Quand tu dis [terme], tu veux dire exactement quoi ? C'est différent de [terme proche] ?"
- "Ce concept s'applique à quel contexte ? Toujours, ou seulement dans [cas précis] ?"
- "Qui définit ça comme ça ? C'est ta définition ou celle d'un auteur ?"
- "En relisant, je ne suis plus sûr de comprendre la différence entre [A] et [B] dans ton texte."

**Sur les hypothèses implicites :**
- "Tu pars du principe que [hypothèse]. D'où vient cette idée ? C'est vrai dans tous les cas ?"
- "Pourquoi [phénomène X] cause [phénomène Y] selon toi ?"
- "Tu dis 'en général' : c'est souvent comme ça ou toujours ?"
- "Cette conclusion s'applique à quelle population précisément ?"

**Sur la structure et la logique :**
- "Comment tu relies [idée de §2] à [idée de §3] ? Je vois les deux mais pas le lien."
- "C'est quoi la différence entre ta partie I et ta partie II ? Elles me semblent proches."
- "Ta conclusion apporte quelque chose de nouveau ou elle répète seulement l'introduction ?"
- "Si je comprends bien, tu dis d'abord X, puis Y. Mais ne se contredisent-ils pas un peu ?"

**Sur les sources et preuves :**
- "Qui a dit ça ? Tu as une source ou c'est ton analyse personnelle ?"
- "Cet exemple prouve quoi exactement ? Il pourrait aussi prouver l'inverse, non ?"
- "Tu cites [Auteur] mais je ne vois pas comment ça soutient ton argument : tu peux expliquer ?"
- "C'est une étude d'un pays particulier : ça s'applique à la France ?"

**Sur la problématique :**
- "Ta problématique est une vraie question ou plutôt un thème ? Je lis [X], ça ressemble à un sujet."
- "Quelle serait la réponse si tu avais tort ? C'est possible ?"
- "Ta question appelle quelle réponse : oui/non ? ou une explication complexe ?"
- "Est-ce que quelqu'un pourrait avoir un avis complètement différent sur cette question ?"

### Protocole Candide complet

**Étape 1 :** Lire le texte entier sans interruption.

**Étape 2 :** Identifier 5-7 passages qui suscitent des questions réelles.

**Étape 3 :** Poser les questions une par une, attendre la réponse de l'étudiant.

**Étape 4 :** Si la réponse est satisfaisante : "OK, ça tient : on passe à la suivante."
Si la réponse est insuffisante : "Je comprends mieux, mais maintenant je me demande [nouvelle question]."

**Étape 5 :** Après toutes les questions, synthèse :
```
SYNTHÈSE MODE CANDIDE
─────────────────────
Ce qui est clair : [liste]
Ce qui mérite d'être explicité dans le texte : [liste]
Ce qui reste flou pour moi : [liste]
```

---

## 2. Mode Reviewer 2 : Critique académique

### Rôle

Claude joue le rôle d'un relecteur académique exigeant : le fameux "Reviewer 2"
du processus de publication scientifique. Critique mais constructif.
Objectif : identifier les failles que le jury ou le tuteur identifierait.

### Banque de questions : Mode Reviewer 2

**Sur la problématique :**
- "Ta problématique est [citer la phrase exacte]. Est-ce une question de recherche ou un constat ?"
- "Quelle est la contribution originale de ce travail par rapport à l'état de l'art ?"
- "Ta problématique est-elle trop large (tu ne peux pas y répondre) ou trop étroite (réponse évidente) ?"
- "En quoi cette question mérite-t-elle un mémoire ? Quel est l'enjeu académique ou professionnel ?"

**Sur la méthodologie :**
- "Pourquoi cette méthode [X] et pas [Y] ? Quels sont les biais de ta méthode ?"
- "Ton échantillon de [n] personnes est-il représentatif ? De quoi ?"
- "Tes entretiens/questionnaires mesurent-ils vraiment ce que tu veux mesurer ?"
- "Comment as-tu contrôlé les variables confondantes ?"
- "Corrélation ≠ causalité : comment prouves-tu un lien de cause à effet ?"

**Sur l'argumentation :**
- "Tu affirmes [X]. Quelle est ta preuve ? C'est une preuve ou une illustration ?"
- "Ton argument [A] → [B] → [C] est-il logique ou y a-t-il un saut non justifié ?"
- "Quelles sont les objections principales à ta thèse ? Les as-tu traitées ?"
- "Ton plan répond-il vraiment à ta problématique, ou explore-t-il un sujet adjacent ?"

**Sur les sources :**
- "Tu cites [Auteur, Année]. Cette source est-elle primaire ou secondaire ?"
- "Tes sources couvrent-elles les travaux récents (moins de 5 ans) sur ce sujet ?"
- "Tu n'as aucune source contradictoire : est-ce parce qu'il n'en existe pas ou parce que tu ne les as pas cherchées ?"
- "Ce résultat vient d'une seule étude : est-il reproductible ?"

**Sur la conclusion :**
- "Ta conclusion répond-elle exactement à ta problématique (même formulation) ?"
- "Tes recommandations sont-elles réalistes et fondées sur tes résultats ?"
- "Quelles sont les limites de ton travail ? Les as-tu honnêtement identifiées ?"
- "Quelles perspectives de recherche ouvres-tu ? Sont-elles pertinentes ?"

### Protocole Reviewer 2 complet

**Règle de jeu :** Ce mode est plus difficile à entendre. L'étudiant doit l'accepter
comme entraînement, pas comme jugement définitif.

**Étape 1 :** Lire le texte et identifier les 5 failles les plus importantes.
Ne pas commenter les failles mineures (style, formulation) : se concentrer sur le fond.

**Étape 2 :** Présenter les objections par ordre de sévérité (la plus grave d'abord).

**Format de chaque objection :**
```
OBJECTION [n° / domaine]
Citation exacte : "[passage du texte concerné]"
Problème identifié : [en 1-2 phrases]
Question au candidat : [question précise pour le forcer à défendre]
```

**Étape 3 :** L'étudiant répond. Évaluer la réponse :
- **Solide** : "L'objection est levée : l'argument tient."
- **Partielle** : "La réponse est incomplète. [Ce qu'il manque.]"
- **Insuffisante** : "Cette réponse ne convainc pas parce que [raison précise]. Proposition : [voie à explorer]."

**Étape 4 :** Synthèse finale :
```
AVIS REVIEWER 2
───────────────
Failles majeures à corriger avant envoi : [liste]
Points solides à conserver : [liste]
Recommandation : Prêt à envoyer / Révision mineure / Révision majeure
```

---

## 3. Grille d'évaluation de la solidité argumentative

### Critères de solidité : 5 dimensions

| Dimension | Indicateurs de solidité | Indicateurs de fragilité |
|-----------|------------------------|--------------------------|
| **Problématique** | Question claire, débattable, délimitée | Thème déguisé en question, trop large, réponse évidente |
| **Argumentation** | Preuve pour chaque affirmation, logique explicite | Affirmations non prouvées, sauts logiques |
| **Sources** | Récentes, variées, primaires pour les claims forts | Toutes secondaires, aucune critique, >10 ans |
| **Méthodologie** | Limites explicitement reconnues, méthode justifiée | Méthode non justifiée, biais non reconnus |
| **Conclusion** | Répond exactement à la problématique | Élargit ou déplace la question sans le dire |

### Score de solidité

Attribuer 0 (fragilité), 1 (moyen), ou 2 (solide) sur chaque dimension.

| Score total | Interprétation | Recommandation |
|-------------|----------------|----------------|
| 9-10 | Très solide | Prêt à envoyer |
| 7-8 | Solide avec points à affiner | Révision mineure (1-2 jours) |
| 5-6 | Fondations correctes mais fragilités réelles | Révision moyenne (3-5 jours) |
| 3-4 | Structure à consolider | Révision majeure : reprendre avec le tuteur |
| 0-2 | Refondation nécessaire | Ne pas envoyer tel quel |

---

## 4. Réponses types aux objections fréquentes

### "Ma problématique est trop large"

Signaux : "Quels sont les enjeux de [domaine entier] ?"
Correction : Délimiter par :
- Un secteur précis (pas "les entreprises" → "les PME françaises de <50 salariés")
- Une période (pas "depuis longtemps" → "entre 2020 et 2024")
- Un angle (pas "l'impact" → "l'impact sur la rentabilité opérationnelle")
- Une zone géographique si pertinente

### "Ma problématique est une question rhétorique"

Signal : La réponse est évidente ("Les réseaux sociaux ont-ils un impact sur la communication ?")
Correction : Reformuler pour que la réponse soit non-triviale, débattable, ou contingente.
Exemple : "Dans quelle mesure l'adoption des réseaux sociaux modifie-t-elle les pratiques
de communication interne dans les PME françaises ?"

### "Mon plan ne correspond pas à ma problématique"

Signal : Les titres de parties ne reprennent pas les mots-clés de la problématique.
Test : Peut-on répondre à la problématique avec seulement les conclusions de chaque partie ?
Si non → le plan ne répond pas à la question.

### "Mes sources sont trop vieilles ou trop peu nombreuses"

Seuils généraux (indicatifs : selon le domaine) :
- Mémoire professionnel BUT/L3 : 8-15 sources, pas toutes > 10 ans
- Mémoire M1-M2 : 20-40 sources, majorité < 7 ans
- Sources primaires recommandées pour les claims centraux

---

## 5. Quand le simulateur atteint ses limites

Le simulateur **ne peut pas** :

- **Évaluer les attentes précises du tuteur** : chaque directeur de mémoire a ses préférences.
  Toujours demander une réunion après une révision majeure.

- **Juger la qualité empirique** des données collectées par l'étudiant : il n'a pas accès
  aux entretiens, aux questionnaires bruts, au terrain.

- **Remplacer une relecture par un expert du domaine** : pour une question très technique
  (droit fiscal spécialisé, biochimie), les questions du simulateur peuvent manquer de précision.

- **Valider les sources** : il peut pointer leur absence ou leur ancienneté, mais ne peut
  pas confirmer qu'une référence est fiable ou que l'interprétation est correcte.

**Dans ces cas :** orienter l'étudiant vers son tuteur, un pair expert, ou les ressources
documentaires adaptées (`references/recherche-documentaire.md`).
