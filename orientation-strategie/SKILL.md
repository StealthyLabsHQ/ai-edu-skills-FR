---
name: orientation-strategie
description: >
  Aide les étudiants à construire une stratégie d'orientation, choisir entre des filières,
  rédiger leur "Projet de Formation Motivé" Parcoursup ou MonMaster, préparer un dossier
  de réorientation, ou explorer des formations adaptées à leur profil. Trigger dès que
  l'utilisateur mentionne : Parcoursup, MonMaster, réorientation, choix de filière,
  "je sais pas quoi faire après le bac", "je veux changer de voie", "je rate mon master",
  "je comprends pas les attendus", "PFM", "projet de formation motivé", "lettre de voeux",
  "classement Parcoursup", "dossier de candidature Parcoursup", "que faire après [diplôme]",
  "quelles formations pour [domaine]", "débouchés", "passerelle", ou demande une aide au
  choix d'orientation sans mentionner explicitement les outils.
  TOUJOURS utiliser ce skill pour toute demande liée au choix d'orientation, à Parcoursup,
  MonMaster, ou à la construction d'un projet professionnel post-diplôme.
version: 1.0.0
---

# Skill — Orientation Stratégique

Aide à la construction du projet d'orientation : choix de filière, Parcoursup,
MonMaster, réorientation, et rédaction du Projet de Formation Motivé (PFM).

---

## Principe directeur

L'orientation n'est pas un choix unique et définitif — c'est une trajectoire à
construire avec les informations disponibles aujourd'hui. L'objectif n'est pas de
trouver "la voie parfaite", mais d'identifier la prochaine étape logique qui ouvre
le plus de portes vers les ambitions identifiées.

**Règle cardinale** : ne jamais orienter sans comprendre les contraintes réelles
(notes, géographie, contraintes familiales, motivation profonde). Une orientation
brillante sur le papier est inutile si elle n'est pas faisable.

---

## Étape 0 — Collecte du profil (OBLIGATOIRE avant tout conseil)

Ne jamais donner de recommandation sans ces éléments. Si des informations sont
déjà connues dans la conversation, les utiliser sans re-demander.

### Profil académique
- Formation actuelle (intitulé exact, établissement, niveau)
- Notes ou moyennes dans les matières clés (pas besoin de toutes — les 3-4 les plus
  représentatives suffisent)
- Points forts et points faibles académiques perçus

### Motivations et intérêts
- Domaines qui suscitent de l'intérêt (même vague)
- Ce que l'étudiant déteste faire (aussi important que ce qu'il aime)
- Activités extra-scolaires ou projets personnels s'il y en a

### Contraintes pratiques
- Mobilité géographique possible (local uniquement, région, national, international ?)
- Contraintes financières (alternance nécessaire ? logement ?)
- Contraintes de calendrier (délai de Parcoursup, résultats de bac)

### Vision du futur (même floue)
- Secteurs ou métiers envisagés (même sans certitude)
- Ce que l'étudiant imagine faire dans 5 ans (même approximativement)
- Ce qui lui semble exclu (secteurs ou types de postes qu'il ne veut pas faire)

> Si toutes ces informations manquent, poser 3 questions ciblées plutôt que toutes à la
> fois. Commencer par : "Tu as une idée, même vague, de ce que tu voudrais faire ?"

---

## Module 1 — Exploration des filières

### 1a. Croisement profil / nomenclature des diplômes français

À partir du profil collecté, identifier les filières pertinentes en croisant :
- Notes et appétences → formations accessibles et alignées
- Contraintes pratiques → formations géographiquement / financièrement accessibles
- Projet professionnel (même flou) → formations qui ouvrent vers ces secteurs

**Nomenclature de référence (niveau post-bac) :**

| Niveau | Durée | Exemples de formations |
|--------|-------|------------------------|
| Bac+2 | 2 ans | BTS, BUT (1ère année), CPGE (prépa) |
| Bac+3 | 3 ans | BUT (complet), Licence, LP (Licence Pro) |
| Bac+5 | 5 ans | Master (M1-M2), école d'ingénieur, école de commerce |
| Bac+8 | 8 ans | Doctorat |

### 1b. Filières méconnues à explorer

Systématiquement signaler des filières que l'étudiant n'a probablement pas considérées
et qui correspondent au profil. Les grandes écoles connues saturent les candidatures —
beaucoup de formations moins connues offrent d'excellents débouchés.

Exemples de filières souvent méconnues à mentionner selon le profil :
- **Profil compta/gestion/chiffres** : DSCG par voie libre, MIAGE, Masters CCA mentions rares
- **Profil tech/développement** : Masters IA spécialisés (NLP, vision), MSc en école d'ingénieur
- **Profil communication/SHS** : Licences pro Digital et Communication, Masters en UX Research
- **Profil santé/paramédical** : IFSI (infirmiers), Ergothérapie, Orthoptie, Masters Santé Publique
- **Profil droit/politique** : Sciences Po régionaux (hors Paris IEP), Masters droit spécialisés DU

### 1c. Débouchés et insertion professionnelle

Ne jamais présenter les débouchés de façon abstraite. Toujours :
- Donner des intitulés de postes concrets
- Mentionner les taux d'insertion si connus (enquêtes BCO/OVE pour les BUT, enquêtes IP pour les Masters)
- Signaler les secteurs recruteurs et les zones géographiques actives

**Ressource étendue :** `references/parcoursup-monmaster.md` — guide des filières
Parcoursup et MonMaster, critères d'évaluation, taux de sélectivité.

---

## Module 2 — Parcoursup (Terminale → Bac+1/2/3)

### 2a. Comprendre les attendus nationaux

Chaque formation Parcoursup publie des "attendus nationaux" et parfois des critères locaux.
Ces attendus doivent transparaître explicitement dans le PFM.

**Structure des attendus types (à adapter par formation) :**
- Compétences attendues (ex : "maîtrise des bases mathématiques" pour une CPGE scientifique)
- Qualités personnelles valorisées (ex : "capacité à travailler en équipe" pour les BUT)
- Connaissances du secteur (ex : "connaissance des métiers de la comptabilité" pour un BTS CG)

### 2b. Stratégie de voeux

**Règles de base :**
- Maximum 10 voeux Parcoursup (depuis la réforme)
- Diversifier les niveaux de sélectivité : ambitieux / cohérents / sécurité
- Toujours inclure des formations locales pour maximiser les chances

**Grille de priorisation :**

| Catégorie | Proportion recommandée | Critère |
|-----------|------------------------|---------|
| Voeux ambitieux | 2-3 voeux | Profil en-dessous de la moyenne des admis |
| Voeux cohérents | 4-5 voeux | Profil dans la moyenne des admis |
| Voeux sécurité | 2-3 voeux | Profil au-dessus de la moyenne des admis |

### 2c. Rédaction du PFM (Projet de Formation Motivé)

Voir section dédiée : [Module 4 — PFM Parcoursup](#module-4---pfm-parcoursup).

---

## Module 3 — MonMaster (Licence → Master)

### 3a. Spécificités de MonMaster

MonMaster centralise les candidatures en M1. Contraintes :
- **Délais courts** : candidatures en mars-avril pour rentrée septembre
- **Dossier** : relevés de notes, CV, lettre de motivation, parfois PFM
- **Entretien possible** : les Masters sélectifs font des entretiens

### 3b. Stratégie MonMaster

**Ce qui fait la différence dans un dossier MonMaster :**
1. La cohérence du parcours avec le Master visé (pas nécessairement la note la plus haute)
2. Une expérience concrète dans le domaine (stage, emploi, projet)
3. Une lettre de motivation qui montre la connaissance du programme (voir skill lettre-motivation)
4. Des recommandations si le programme les accepte

**Profil atypique / réorientation :**
Signaler explicitement la valeur de l'atypisme : un L3 droit qui candidate en Master
Management apporte une perspective juridique rare. Transformer la différence en argument.

### 3c. Alternatives si refus MonMaster

- LP (Licence Professionnelle) : bac+3 professionnalisant avec de bonnes perspectives
- Inscription directe dans un Master 1 moins sélectif pour valider la première année
- Classe préparatoire aux Masters (CPM) dans certains établissements
- VAE (Validation des Acquis de l'Expérience) si expérience professionnelle significative

---

## Module 4 — PFM Parcoursup

### Différences PFM vs Lettre de Motivation classique

| Critère | Lettre de Motivation | PFM Parcoursup |
|---------|---------------------|----------------|
| Longueur | 300-500 mots | 1500 caractères max (espaces inclus) |
| Identité | Prénom/Nom en en-tête | Anonyme — PAS de nom, prénom, établissement |
| Destinataire | Connu (recruteur nommé) | Commission anonyme |
| Format | Document formel | Texte libre dans interface |
| Objectif | Convaincre un recruteur | Prouver l'adéquation aux attendus de la formation |

### Structure recommandée du PFM (1500 caractères)

```
§1 — Pourquoi cette formation (200-250 caractères)
  → 1 élément spécifique du programme nommé
  → Lien direct avec une expérience ou un projet personnel

§2 — Preuve de l'adéquation (500-600 caractères)
  → 2-3 éléments concrets du parcours (cours, projets, stages, centres d'intérêt)
  → Montrer explicitement que les attendus sont couverts
  → "Show, don't tell" — pas "je suis motivé", mais "j'ai fait X"

§3 — Projet professionnel (400-450 caractères)
  → Où on se voit dans 3-5 ans (même approximativement)
  → Pourquoi cette formation est la voie logique vers cet objectif

§4 — Connaissance du secteur (250-300 caractères)
  → Une démarche concrète prouvant l'intérêt : JPO, échange avec un étudiant,
    salon, lecture d'une publication, visite d'entreprise
```

**Contraintes absolues Parcoursup :**
- Zéro nom propre (ni prénom, ni NOM, ni établissement d'origine)
- Zéro date dans le texte
- Intitulé exact de la formation visée (ex : "BUT Informatique" et non "l'IUT")
- Mentionner les attendus nationaux implicitement ou explicitement

**Référence étendue :** `references/projet-formation-motive.md` — templates par type
de formation, 15+ paires avant/après, grille de vérification Parcoursup.

---

## Module 5 — Réorientation

### Diagnostiquer la situation

Avant de recommander une réorientation, comprendre pourquoi :
- **Mauvaise orientation initiale** (le domaine ne correspond pas) → nouvelle exploration
- **Difficulté temporaire** (surcharge, période difficile) → solutions d'adaptation
- **Inadéquation avec l'établissement** (méthodes, ambiance) → même formation ailleurs

> Ces causes ont des réponses différentes. Ne pas recommander une réorientation totale
> pour un problème qui peut se résoudre avec un changement d'établissement.

### Options de réorientation en cours d'année

| Situation | Options |
|-----------|---------|
| En cours de L1 | Passerelle vers BTS/BUT, redépôt Parcoursup |
| Fin de L1 ratée | Intégrer un BTS en 1ère ou 2ème année (admission parallèle) |
| BTS/BUT en cours | Passerelle vers Licence (L2 ou L3) par validation de crédits |
| Master 1 raté | Redoubler, LP, ou changer de spécialité en M1 |

### Formuler la réorientation positivement

Dans les documents de candidature : une réorientation est une preuve de maturité
et de connaissance de soi, pas un aveu d'échec. La formuler comme :
"Mon parcours en [X] m'a permis de comprendre que mon profil est mieux aligné avec [Y]
pour les raisons suivantes : [raisons concrètes]."

---

## Checklist interne avant livraison

*(Usage interne — ne pas afficher à l'utilisateur)*

- [ ] Le profil complet a-t-il été collecté (notes, motivations, contraintes, vision) ?
- [ ] Les recommandations sont-elles réalistes au regard des notes et contraintes ?
- [ ] Ai-je mentionné au moins une filière méconnue pertinente ?
- [ ] Pour Parcoursup : le PFM est-il anonyme et dans les 1500 caractères ?
- [ ] Pour MonMaster : la cohérence du parcours avec le Master est-elle mise en avant ?
- [ ] Pour une réorientation : la cause profonde a-t-elle été identifiée ?
- [ ] Les débouchés cités sont-ils concrets (intitulés de postes) ?

---

## Références internes

| Fichier | Quand le consulter |
|---------|-------------------|
| `references/parcoursup-monmaster.md` | Guide détaillé des filières, critères de sélection, taux d'admission |
| `references/projet-formation-motive.md` | Templates PFM, paires avant/après, grille de vérification |

### Skills externes (si disponibles dans l'environnement)

| Skill | Quand le consulter |
|-------|-------------------|
| `/mnt/skills/user/lettre-motivation/SKILL.md` | Rédaction de la lettre de motivation pour MonMaster ou candidature complémentaire |
| `/mnt/skills/user/entretien-oral/SKILL.md` | Préparation à l'entretien de sélection d'un Master ou d'une grande école |
| `/mnt/skills/user/soutien-academique/SKILL.md` | L'étudiant a besoin d'aide sur son dossier académique (mémoire, rapport) comme argument de dossier |
