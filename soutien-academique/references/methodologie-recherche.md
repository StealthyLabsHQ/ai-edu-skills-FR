# Méthodologie de recherche  - Guide de référence

> Consulté quand l'étudiant travaille sur la partie méthodologique d'un mémoire ou d'une thèse.
> Couvre les approches qualitatives, quantitatives et mixtes.

---

## Table des matières

1. Choisir sa méthodologie
2. Approche qualitative
3. Approche quantitative
4. Approche mixte
5. Rédiger la partie méthodologie
6. Erreurs fréquentes

---

## 1. Choisir sa méthodologie

Le choix ne se fait pas au hasard. Il découle de la problématique.

| Ta question de recherche ressemble à... | Approche adaptée |
|----------------------------------------|-----------------|
| "Comment les salariés vivent-ils X ?" | Qualitative (entretiens) |
| "Quel est l'impact de X sur Y ?" | Quantitative (questionnaire, données) |
| "Dans quelle mesure X influence Y dans le contexte Z ?" | Mixte ou quantitative |
| "Quels sont les facteurs qui expliquent X ?" | Qualitative exploratoire puis quantitative confirmatoire |
| "Comment fonctionne le processus de X ?" | Qualitative (observation, étude de cas) |
| "X est-il corrélé à Y ?" | Quantitative |
| "Comment améliorer X ?" | Recherche-action ou étude de cas avec préconisations |

### Justifier son choix

Ne jamais écrire "J'ai choisi la méthode qualitative car elle est adaptée à mon sujet."
Expliquer POURQUOI elle est adaptée :

> "Le phénomène étudié  - l'adoption d'outils numériques par des comptables seniors  -
> est peu documenté dans la littérature. Une approche exploratoire par entretiens
> semi-directifs permet de faire émerger des catégories d'analyse que les travaux
> existants n'ont pas identifiées."

---

## 2. Approche qualitative

### Entretien semi-directif

**Quand l'utiliser :** Explorer un vécu, comprendre des perceptions, recueillir
des pratiques professionnelles. C'est l'outil le plus courant en mémoire pro et M2 SHS.

**Préparer la grille d'entretien :**

```
THÈME 1  - [Nom du thème]
  Question principale : ...
  Relance 1 : ...
  Relance 2 : ...

THÈME 2  - [Nom du thème]
  Question principale : ...
  Relance 1 : ...
  Relance 2 : ...

[3 à 5 thèmes maximum]
```

Règles :
- Questions ouvertes, jamais fermées ("Comment...?" et non "Est-ce que...?")
- Pas de questions orientées ("Ne pensez-vous pas que X est un problème ?")
- Prévoir des relances pour approfondir sans influencer
- Commencer par des questions faciles (parcours, fonction) avant les sujets sensibles
- Durée idéale : 30-60 min par entretien

**Combien d'entretiens ?**

| Niveau | Nombre minimum | Saturation |
|--------|---------------|-----------|
| BUT / Licence pro | 4-6 | Quand les réponses commencent à se répéter |
| Master 1 | 6-10 | Idem |
| Master 2 recherche | 10-15 | Saturation théorique formalisée |
| Thèse | 15-30+ | Saturation théorique démontrée |

**Analyser les entretiens  - méthode thématique (Paillé & Mucchielli) :**

1. Retranscrire intégralement (verbatim)
2. Lecture flottante de l'ensemble
3. Codage : identifier les unités de sens, leur attribuer un code
4. Regrouper les codes en catégories thématiques
5. Construire un arbre thématique
6. Interpréter en lien avec la littérature

Outils gratuits : RQDA (R), QualCoder, ou simplement un tableur avec
colonnes Verbatim / Code / Thème / Sous-thème.

### Observation participante

**Quand l'utiliser :** L'étudiant est en stage/alternance et observe les pratiques
de l'intérieur. Particulièrement adapté aux mémoires professionnels.

**Journal de terrain :**
Tenir un carnet (physique ou numérique) avec :
- Date et contexte de l'observation
- Description factuelle de ce qui s'est passé
- Impressions et interprétations (séparées des faits)
- Questions qui émergent

### Étude de cas

**Quand l'utiliser :** Analyser un phénomène en profondeur dans son contexte réel.
Référence méthodologique : Yin (2018).

Un cas = une unité d'analyse (une entreprise, un projet, un service).
Multi-cas = comparaison de 2-4 cas pour identifier des régularités.

Sources de données dans une étude de cas :
- Documents internes
- Entretiens
- Observation directe
- Données chiffrées

La force de l'étude de cas est la triangulation : croiser plusieurs sources
pour renforcer la validité.

---

## 3. Approche quantitative

### Questionnaire

**Quand l'utiliser :** Mesurer un phénomène, tester des hypothèses, généraliser
des résultats à une population.

**Construire le questionnaire :**

1. Définir les variables à mesurer (issues de la revue de littérature)
2. Opérationnaliser : comment chaque variable se traduit en questions
3. Types de questions :
   - Likert (1-5 ou 1-7) : "Tout à fait d'accord" → "Pas du tout d'accord"
   - Choix multiples
   - Échelles numériques
   - Questions ouvertes (limiter à 1-2 pour le traitement)
4. Tester le questionnaire sur 5-10 personnes avant diffusion (pré-test)

**Taille de l'échantillon :**

| Type d'analyse | Minimum recommandé |
|---------------|-------------------|
| Statistiques descriptives (moyennes, %) | 30 réponses |
| Tests de corrélation / chi² | 50-100 |
| Régression | 10-15 réponses par variable indépendante |
| Analyse factorielle | 5 réponses par item minimum |

Pour un mémoire pro : 30-50 réponses exploitables est un objectif réaliste.
Pour un M2 recherche : viser 100+ si possible.

**Outils de diffusion :** Google Forms (gratuit), LimeSurvey (open source),
Typeform, Microsoft Forms.

**Analyse des données :**

| Ce que tu veux faire | Outil / test |
|---------------------|-------------|
| Décrire (moyennes, répartition) | Statistiques descriptives, tableaux croisés |
| Comparer deux groupes | Test t de Student, Mann-Whitney |
| Comparer 3+ groupes | ANOVA, Kruskal-Wallis |
| Mesurer une relation entre 2 variables | Corrélation de Pearson ou Spearman |
| Tester l'effet de X sur Y | Régression linéaire |
| Vérifier la fiabilité d'une échelle | Alpha de Cronbach |

Outils gratuits : JASP, PSPP (alternative à SPSS), R, Google Sheets (pour le basique),
Excel avec l'utilitaire d'analyse.

### Données secondaires

Utiliser des données existantes : bases INSEE, données Open Data, rapports sectoriels,
données internes de l'entreprise.

Toujours préciser : source, date, périmètre, limites.

---

## 4. Approche mixte

Combiner quali et quanti. Deux designs classiques :

**Séquentiel exploratoire :**
Quali d'abord (entretiens pour explorer) → Quanti ensuite (questionnaire pour confirmer)
Usage : sujet peu étudié, besoin de construire les hypothèses avant de les tester.

**Séquentiel explicatif :**
Quanti d'abord (questionnaire pour mesurer) → Quali ensuite (entretiens pour comprendre les résultats)
Usage : résultats quantitatifs surprenants ou à nuancer.

**Convergent (simultané) :**
Quali ET quanti en même temps, croisement des résultats.
Usage : quand le temps le permet et que les deux approches éclairent des facettes différentes.

---

## 5. Rédiger la partie méthodologie

### Structure recommandée

```
1. Rappel de la problématique et des objectifs
2. Positionnement épistémologique (M2 recherche / thèse uniquement)
3. Choix de l'approche et justification
4. Terrain / population / échantillon
   - Description et justification du choix
   - Mode de sélection (critères d'inclusion/exclusion)
   - Taille et caractéristiques
5. Outils de collecte
   - Description de l'outil (grille, questionnaire...)
   - Processus de construction
   - Pré-test éventuel
6. Protocole de collecte
   - Comment, quand, où les données ont été collectées
   - Conditions pratiques (durée des entretiens, taux de réponse...)
7. Méthode d'analyse
   - Outil logiciel utilisé
   - Procédure d'analyse pas à pas
8. Limites méthodologiques
   - Biais identifiés
   - Ce que la méthode ne permet pas de dire
```

### Positionnement épistémologique (M2 recherche / thèse)

Pas nécessaire en mémoire pro ou BUT. Obligatoire en M2 recherche.

| Paradigme | Vision | Méthode typique |
|-----------|--------|----------------|
| Positiviste | La réalité existe, elle est mesurable | Quantitative, hypothético-déductive |
| Interprétativiste | La réalité est construite par les acteurs | Qualitative, compréhensive |
| Constructiviste | La connaissance se construit dans l'interaction | Mixte, recherche-action |
| Pragmatiste | Ce qui compte c'est ce qui fonctionne | Mixte, orientée résultats |

---

## 6. Erreurs fréquentes

| Erreur | Pourquoi c'est un problème | Correction |
|--------|---------------------------|-----------|
| "J'ai choisi le qualitatif car c'est plus simple" | Ce n'est pas une justification méthodologique | Justifier par la nature de la question de recherche |
| Pas de grille d'entretien présentée | Le jury ne peut pas évaluer la rigueur | Mettre la grille en annexe, la décrire dans le texte |
| "J'ai interviewé 3 personnes" sans justification | 3 peut suffire en étude de cas, pas en exploration large | Justifier le nombre, parler de saturation ou de contraintes |
| Questionnaire sans pré-test | Des questions ambiguës passent inaperçues | Toujours tester sur 5-10 personnes |
| Confondre corrélation et causalité | "X est corrélé à Y" ne veut pas dire "X cause Y" | Utiliser le vocabulaire approprié : "associé à", "lié à" |
| Aucune mention des limites | Donne l'impression que l'étudiant n'a pas de recul | Section limites obligatoire, honnête et concrète |
| Méthodologie décrite en 10 lignes | Partie la plus évaluée par le jury | Développer, justifier chaque choix |
