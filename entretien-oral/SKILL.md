---
name: entretien-oral
description: >
  Prépare les étudiants et candidats aux entretiens oraux de sélection : entretien
  de Master, grande école, alternance, stage, CDI/CDD, entretien de motivation,
  jury de concours. Trigger dès que l'utilisateur mentionne : entretien, jury,
  "j'ai un entretien", "je sais pas comment répondre", "questions d'entretien",
  "comment me présenter", "entretien blanc", "simuler un entretien", "parler de moi",
  "mes défauts en entretien", "méthode STAR", "j'ai peur du jury", "oraux de concours",
  "entretien de motivation", "j'ai un oral demain", ou toute demande de préparation
  à une situation de prise de parole évaluative.
  TOUJOURS utiliser ce skill pour toute demande liée à la préparation d'un entretien,
  d'un oral de sélection, ou d'une présentation devant un jury.
version: 1.0.0
---

# Skill — Entretien Oral

Préparation complète aux entretiens de sélection : méthode STAR, traque des réponses
"bateau", entretiens blancs simulés, et adaptation au type de jury.

---

## Principe directeur

Un entretien n'est pas une récitation de son CV. C'est une démonstration en temps réel
de la façon dont un candidat réfléchit, s'exprime, et gère l'inconfort.

Les jurys sélectionnent sur deux axes :
1. **La substance** : le candidat a-t-il les compétences et le projet qu'il prétend avoir ?
2. **La forme** : est-il capable de les expliquer clairement sous pression ?

**Règle cardinale** : une réponse "bateau" est une réponse qui pourrait être donnée par
n'importe quel candidat. Elle ne différencie pas — elle dilue.

---

## Étape 0 — Collecte du contexte (OBLIGATOIRE)

Avant tout entretien blanc ou conseil, identifier :

- **Type d'entretien :** motivation Master / sélection école / alternance / emploi /
  concours de la fonction publique / autre
- **Entité qui reçoit :** université, école d'ingénieur, école de commerce, entreprise,
  administreation publique
- **Format connu :** durée, nombre d'intervieweurs, questions attendues, cas pratique ?
- **Profil du candidat :** formation actuelle, expériences clés, point fort et point faible
  perçus, "moment déclencheur" (ce qui a mené à cette candidature)
- **Angoisse spécifique :** question redoutée, aspect du profil considéré comme un point faible

> Si le contexte est incomplet : poser max 3 questions ciblées pour démarrer l'entretien blanc.

---

## Module 1 — Méthode STAR

### Qu'est-ce que la méthode STAR

STAR est la structure de réponse universelle pour les questions comportementales
("Parlez-moi d'une situation où vous avez dû...").

| Lettre | Composant | Ce qu'on dit | Durée |
|--------|-----------|--------------|-------|
| **S** | Situation | Contexte en 2 phrases | ~15 sec |
| **T** | Tâche | Mission ou objectif précis | ~15 sec |
| **A** | Action | Ce que j'ai fait (verbes d'action) | ~45 sec |
| **R** | Résultat | Résultat concret (chiffre ou fait observable) | ~15 sec |

**Durée totale recommandée :** 90 secondes à 2 minutes. Ni plus (perd l'attention), ni moins (manque de substance).

### Erreurs STAR fréquentes

| Erreur | Conséquence | Correction |
|--------|-------------|------------|
| Pas de résultat chiffré ou observable | Réponse "floue" | Toujours : "résultat : [X]" |
| "On a fait" au lieu de "j'ai fait" | Rôle personnel invisible | Toujours préciser sa contribution individuelle |
| Situation trop banale | Pas différenciant | Choisir un exemple avec une vraie difficulté surmontée |
| Réponse trop longue | Perd le jury | Entraîner avec minuterie |
| Pas de T (Tâche) | Logique floue | Préciser l'objectif assigné ou auto-fixé |

### Construction d'un stock de réponses STAR

Avant l'entretien, préparer 5-6 histoires STAR polyvalentes qui peuvent répondre
à plusieurs types de questions :

1. **Gestion d'un conflit ou d'un désaccord** (équipe, client, hiérarchie)
2. **Projet conduit de A à Z** (initiative, autonomie, livraison)
3. **Échec ou erreur et rebond** (capacité d'apprentissage)
4. **Situation de pression ou de délai serré** (gestion du stress)
5. **Adaptation à un changement inattendu** (flexibilité)
6. **Exemple de leadership ou d'influence sans autorité formelle**

Chacune doit avoir un résultat mesurable ou observable.

---

## Module 2 — Entretien blanc simulé

### Format de l'entretien blanc

Claude joue le rôle du jury selon le type d'entretien précisé. L'étudiant répond comme
en situation réelle. Claude évalue ensuite chaque réponse sur 3 critères.

**Règle de jeu :** Ne pas interrompre pendant la réponse. Évaluer après.

**Critères d'évaluation de chaque réponse :**
1. **Substance** : la réponse dit-elle quelque chose de concret et différenciant ?
2. **Structure** : la réponse est-elle organisée (STAR ou équivalent) ?
3. **Authenticité** : la réponse sonne-t-elle vraie ou "préparée par cœur" ?

**Format de feedback :**
```
RÉPONSE À : "[question posée]"
─────────────────────────────
Substance : [Solide / À étoffer / Trop vague]
Structure : [Claire / À retravailler / Absente]
Authenticité : [Naturelle / Un peu récitée / Réponse bateau]

Point fort : [ce qui fonctionne, en 1 phrase]
Point à améliorer : [1 seule chose, avec suggestion concrète]
Reformulation suggérée : [si nécessaire — débuter la réponse différemment]
```

### Questions d'entretien blanc par catégorie

**Voir `references/questions-pieges.md`** pour la banque complète de questions
avec analyse des réponses bateau et reformulations recommandées.

---

## Module 3 — Traque des réponses "bateau"

### Définition

Une réponse bateau est une réponse universelle, attendue, non-différenciante.
Elle prouve que le candidat a préparé, pas qu'il est le bon candidat.

### Les 10 réponses bateau les plus fréquentes (et leurs antidotes)

**1. "Mon plus grand défaut est d'être perfectionniste."**
- Pourquoi c'est bateau : tout le monde le dit, c'est perçu comme une pseudo-qualité déguisée
- Antidote : citer un vrai défaut (tendance à vouloir tout contrôler, difficulté à déléguer,
  impatience face aux délais flous) + montrer ce qu'on fait concrètement pour le corriger

**2. "Je suis très motivé par votre entreprise / formation."**
- Pourquoi c'est bateau : aucune preuve fournie
- Antidote : nommer un élément spécifique (un cours, un projet de l'équipe, une publication,
  un alumni rencontré) + expliquer le lien avec sa propre trajectoire

**3. "Je m'adapte facilement à n'importe quelle situation."**
- Pourquoi c'est bateau : déclaration sans preuve
- Antidote : exemple STAR d'une adaptation réelle dans un contexte précis

**4. "Je suis passionné par [domaine]."**
- Pourquoi c'est bateau : tout le monde dans la salle dit la même chose
- Antidote : "Ma passion pour X se manifeste par [action concrète] — j'ai lu [livre
  précis / suivi [formation] / travaillé sur [projet] en dehors des cours."

**5. "Je travaille bien en équipe."**
- Pourquoi c'est bateau : attendu et non-prouvé
- Antidote : exemple STAR où la dynamique d'équipe était difficile et a été surmontée

**6. "Je suis à l'aise à l'oral."** (dit souvent d'une voix tremblante)
- Pourquoi c'est contre-productif : l'entretien est la preuve — inutile de le déclarer
- Antidote : ne rien dire sur ses qualités orales — les démontrer par la performance

**7. "Je suis très rigoureux."**
- Antidote : "J'ai mis en place [système précis] dans [contexte] pour [résultat]."

**8. "Je veux intégrer ce Master pour développer mes compétences."**
- Pourquoi c'est bateau : toutes les formations développent des compétences
- Antidote : nommer la compétence précise, pourquoi elle manque, comment ce programme
  la développe spécifiquement, et à quoi elle servira dans le projet précis

**9. "Je suis curieux et j'aime apprendre."**
- Antidote : "Récemment, j'ai [appris X] en dehors des cours parce que [raison précise]."

**10. "Je suis disponible immédiatement."**
- Ce n'est pas une réponse bateau mais un détail logistique — ne jamais l'utiliser
  comme argument de candidature principal

---

## Module 4 — Types d'entretiens spécifiques

### Entretien de motivation Master / Grande École

**Format typique :** 20-30 min, 1-3 membres du jury, questions sur le projet pro et le parcours

**Questions fréquentes :**
- "Présentez-vous en 2 minutes."
- "Pourquoi ce Master ?"
- "Quel est votre projet professionnel à 5 ans ?"
- "Quelles sont vos forces et faiblesses ?"
- "Qu'avez-vous fait pendant votre stage/alternance ?"
- "Pourquoi pas [formation concurrente] ?"
- "Avez-vous des questions ?"

**Piège de la dernière question :** "Avez-vous des questions ?" — toujours préparer 2-3
questions concrètes sur le programme (pas sur des informations déjà sur le site).

### Entretien d'alternance / stage

**Format typique :** 30-45 min, RH + manager opérationnel

**Différences clés :**
- Plus orienté compétences techniques et savoir-faire concrets
- Les exemples de projets réalisés (mêmes académiques) ont beaucoup de poids
- La question "pourquoi l'alternance et pas le présentiel" peut être posée — préparer la réponse

**Question piège fréquente :** "Vous avez fait [X] en cours — vous savez vraiment faire ça ?"
→ Répondre honnêtement sur le niveau (débutant/intermédiaire) + montrer la capacité d'apprentissage

### Entretien concours fonction publique

**Format typique :** 20-30 min devant un jury de 3-5 personnes, souvent suivi d'un exposé

**Particularités :**
- Neutralité attendue sur les sujets politiques
- Connaissance du secteur public et de l'institution attendue
- Le "pourquoi le service public" est une question quasi-systématique — préparer une réponse
  sincère et argumentée (pas "pour la sécurité de l'emploi")

---

## Module 5 — Présentation initiale : "Parlez-moi de vous"

La présentation initiale (1-3 min selon le contexte) est souvent mal préparée car
elle semble simple. C'est pourtant le moment qui donne le ton.

### Structure recommandée

```
[Accroche contextuelle — 15 sec]
  → Pas "Je m'appelle X et j'ai Y ans" — inutile, le jury a le dossier
  → Commencer par le "fil rouge" de son parcours : pourquoi je suis là

[Parcours en 3 temps — 60 sec]
  → Formation de base et ce qu'elle m'a apporté (concrètement)
  → Expérience(s) clé(s) et ce que j'en ai retiré (chiffre ou résultat)
  → Ce que ça m'a amené à vouloir faire (projet professionnel bref)

[Pourquoi ce programme / ce poste — 30 sec]
  → 1 élément spécifique nommé + lien avec le parcours

[Invitation à l'échange — 5 sec]
  → "Je suis prêt à approfondir tout point qui vous intéresse."
```

### Ce qu'il ne faut PAS faire dans la présentation initiale

- Réciter son CV chronologiquement ("En 2021, j'ai fait... En 2022...")
- Mentionner des informations que le jury a déjà (nom, âge, établissement)
- Parler plus de 3 minutes sans invitation à continuer
- Finir par "voilà" sans invitation à l'échange

---

## Checklist interne avant l'entretien blanc

*(Usage interne — ne pas afficher à l'utilisateur)*

- [ ] Le contexte exact de l'entretien est connu (type, durée, jury) ?
- [ ] Le profil du candidat (formation, expériences, point fort/faible) est collecté ?
- [ ] Le stock de 5-6 histoires STAR est préparé ou demandé ?
- [ ] La présentation initiale est structurée (pas récitation de CV) ?
- [ ] Les 10 réponses bateau ont été identifiées et travaillées ?
- [ ] La dernière question "avez-vous des questions" est préparée ?

---

## Références internes

| Fichier | Quand le consulter |
|---------|-------------------|
| `references/methode-star.md` | Exemples détaillés de réponses STAR par secteur, exercices de construction |
| `references/questions-pieges.md` | Banque de 50+ questions avec analyse des réponses bateau et reformulations |

### Skills externes (si disponibles dans l'environnement)

| Skill | Quand le consulter |
|-------|-------------------|
| `/mnt/skills/user/lettre-motivation/SKILL.md` | Préparer la lettre de motivation ou le pitch écrit en amont de l'entretien |
| `/mnt/skills/user/orientation-strategie/SKILL.md` | L'étudiant a besoin d'affiner son projet pro avant l'entretien |
| `/mnt/skills/user/plume-naturelle/references/mode-pedagogique.md` | Section oralité : scripts de soutenance, gestion du stress, voix |
