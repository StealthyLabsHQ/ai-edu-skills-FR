# ai-edu-skills-FR

Skills pour ChatGPT & Claude : accompagnement scolaire et universitaire.

## Objectif

Bibliothèque de skills `.md` open-source pour transformer Claude et ChatGPT en assistant pédagogique adapté au système éducatif français, du lycée au master.

## Arborescence

```
ai-edu-skills-FR/
├── README.md
├── soutien-academique/
│   ├── SKILL.md                              ← Skill principal (10 modules)
│   └── references/                           ← Ressources chargées à la demande
│       ├── normes-citation.md                ← APA 7, norme française, Harvard, Vancouver, Chicago
│       ├── ecriture-naturelle.md             ← Filtre anti-détection IA (30+ paires avant/après)
│       ├── methodologie-recherche.md         ← Quali, quanti, mixte, grilles, analyse thématique
│       ├── questions-jury.md                 ← 50+ questions de jury + section 9 : questions pièges anti-IA
│       ├── structures-par-niveau.md          ← Attentes lycée → M2 recherche (tableau comparatif)
│       ├── dissertation-commentaire.md       ← Méthodes dissertation, commentaire, arrêt, document
│       ├── templates-documents.md            ← Pages de garde, sommaires, bibliographies, charte typo
│       ├── revisions-examens.md              ← Active recall, plannings, fiches par matière, jour J
│       ├── recherche-documentaire.md         ← Google Scholar, Cairn, HAL, évaluation CRAAP, fiches de lecture
│       ├── gestion-projet-memoire.md         ← Timeline, réunions tuteur, blocages, versioning
│       ├── note-synthese.md                  ← Méthode de dépouillement, plan de synthèse, pièges
│       ├── disciplines-specificites.md       ← Normes et ressources par discipline (compta, droit, SHS, info, santé)
│       ├── neurodiversite.md                 ← TDAH, dyslexie, DYS : adaptations, outils, aménagements officiels
│       └── peer-review-simulator.md          ← Simulateur Peer-Review : Mode Candide + Mode Reviewer 2
├── lettre-motivation/
│   ├── SKILL.md                              ← Lettres de motivation + réseautage digital (Module 5)
│   └── references/                           ← Ressources chargées à la demande
│       ├── types-candidature.md              ← Spécificités par type de candidature
│       ├── anti-generique.md                 ← 20 paires avant/après anti-phrases creuses
│       └── reseautage-digital.md             ← Cold emails, messages LinkedIn, relances, remerciements post-entretien
├── plume-naturelle/
│   ├── SKILL.md                              ← Réécriture anti-IA + Mode Pédagogique + Oralité
│   └── references/                           ← Ressources chargées à la demande
│       ├── patterns-par-discipline.md        ← Patterns IA spécifiques par discipline
│       ├── marqueurs-ia-francais.md          ← Liste noire transversale de 80+ marqueurs IA avec multiplicateurs
│       ├── prompts-detecteurs.md             ← Prompts de détection reconstitués (formules, seuils, architecture)
│       ├── formules-auto-evaluation.md       ← 38 formules mathématiques (Tier 1 à Tier 3 : PPL, GLTR, DetectGPT, σ²_D)
│       └── mode-pedagogique.md              ← Annotation pédagogique, remédiation, scripts de soutenance annotés
├── orientation-strategie/
│   ├── SKILL.md                              ← Parcoursup, MonMaster, réorientation, filières méconnues
│   └── references/                           ← Ressources chargées à la demande
│       ├── parcoursup-monmaster.md           ← Guide des filières, critères de sélection, calendriers
│       └── projet-formation-motive.md        ← Templates PFM, 15 paires avant/après, grille de vérification
├── entretien-oral/
│   ├── SKILL.md                              ← Entretiens blancs, méthode STAR, réponses bateau
│   └── references/                           ← Ressources chargées à la demande
│       ├── methode-star.md                   ← Exemples STAR par secteur, stock de 6 histoires, exercices
│       └── questions-pieges.md              ← 50+ questions avec antidotes, réponses bateau, erreurs de fond/forme
└── productivite-pkm/
    ├── SKILL.md                              ← Obsidian, Notion, Zotero, Zettelkasten pour mémoire
    └── references/                           ← Ressources chargées à la demande
        ├── zettelkasten-obsidian.md          ← Config Obsidian complète, plugins, templates, workflows
        └── zotero-bibliographie.md           ← Zotero avancé, styles de citation français, intégration Word
```

## Comment ça fonctionne

Le système utilise un **chargement progressif à 3 niveaux** :

1. **Metadata** (toujours en contexte) : Le `name` + `description` dans le frontmatter YAML du SKILL.md. C'est ce que Claude lit pour décider s'il doit activer le skill. ~150 mots.

2. **SKILL.md** (chargé quand le skill se déclenche) : Le corps principal avec les modules, les principes, les réponses types. Contient les règles et la logique, pas les détails exhaustifs.

3. **references/** (chargé à la demande) : Les fichiers détaillés que Claude consulte uniquement quand la conversation porte sur un sujet spécifique. Par exemple, `normes-citation.md` n'est lu que si l'étudiant demande de l'aide sur sa bibliographie.

Cette architecture évite de surcharger le contexte avec des informations inutiles tout en gardant la profondeur disponible quand elle est nécessaire.

## Skills disponibles

| Skill | Modules couverts | Niveaux ciblés |
|-------|-----------------|----------------|
| `soutien-academique` | Mémoire pro, mémoire recherche, rapport de stage, soutien scolaire, dissertation/commentaire, soutenance, projets de groupe/SAÉ, spécificités disciplinaires, **neurodiversité (TDAH/DYS)**, **simulateur peer-review** | Lycée → Master |
| `lettre-motivation` | LM personnalisées pour école, alternance, stage, emploi, candidature spontanée, reconversion, **cold emails, messages LinkedIn, relances et remerciements post-entretien** | Tous niveaux |
| `plume-naturelle` | Réécriture anti-IA : 48 patterns, 8 phases, **38 formules mathématiques** (Tier 1-3 : PPL, GLTR, DetectGPT, σ²_D), **mode pédagogique par annotation**, **scripts de soutenance oraux** | Tous niveaux |
| `orientation-strategie` | Exploration de filières méconnues, stratégie Parcoursup, MonMaster, réorientation, **rédaction du PFM** | Terminale → L3 / réorientation |
| `entretien-oral` | Méthode STAR, entretiens blancs simulés, traque des **réponses bateau**, questions pièges, présentations initiales | Tous niveaux |
| `productivite-pkm` | **Zettelkasten**, Obsidian, Notion, **Zotero** pour mémoires et thèses, organisation des sources, PKM académique | BUT → Doctorat |

## Exemples de prompts

```
"J'ai un mémoire de M1 en compta à rendre dans 3 mois, je sais pas par où commencer"
"Aide-moi à trouver des sources pour ma revue de littérature sur la digitalisation des PME"
"J'ai une note de synthèse à préparer pour le concours, c'est quoi la méthode ?"
"Corrige ma lettre de motivation pour un stage en cabinet comptable"
"Je comprends pas le cours sur les amortissements, explique-moi simplement"
"On a un projet de groupe SAÉ à rendre, comment on s'organise ?"
"Mon intro sonne trop ChatGPT, rends-la naturelle"
"Humanise ce texte, mon prof va voir que c'est de l'IA"
"J'ai un TDAH, aide-moi à réviser autrement"
"Annote mon texte pour que je comprenne pourquoi ça sonne IA"
"Je ne sais pas quoi faire après mon BUT, aide-moi à explorer les Masters"
"J'ai un entretien de sélection pour un Master demain, entraîne-moi"
"Comment j'organise mes notes Obsidian pour mon mémoire ?"
"J'ai besoin d'un message LinkedIn pour contacter un alumni"
"Simule le Reviewer 2 sur mon introduction de mémoire"
```

## Dépendances entre skills

Les skills peuvent se compléter selon le besoin :

| Besoin | Skill principal | Skill complémentaire |
|--------|----------------|---------------------|
| Mémoire + mise en forme Word | `soutien-academique` | `docx` (public) |
| Mémoire + candidature Master | `soutien-academique` | `lettre-motivation` |
| Texte à rendre plus naturel / anti-IA | `plume-naturelle` | `soutien-academique` |
| Soutenance + slides | `soutien-academique` | `pptx` (public) |
| Fiche de révision imprimable | `soutien-academique` | `pdf` (public) |
| Lettre qui sonne trop IA | `plume-naturelle` | `lettre-motivation` |
| Orientation + candidature | `orientation-strategie` | `lettre-motivation` |
| Orientation + entretien de sélection | `orientation-strategie` | `entretien-oral` |
| Mémoire + organisation des sources | `soutien-academique` | `productivite-pkm` |
| Préparation soutenance (écrit + oral) | `soutien-academique` | `plume-naturelle` (mode oralité) |
| Réorientation + LM + entretien | `orientation-strategie` | `lettre-motivation` + `entretien-oral` |

## Installation

### Comment installer les skills

#### Sur Claude : [claude.ai/customize/skills](https://claude.ai/customize/skills)

1. Aller sur [Claude](https://claude.ai/customize/skills)
2. Cliquer sur **"Add skill"**
3. Donner un nom au skill (ex : `soutien-academique`)
4. Coller le contenu du fichier `SKILL.md` correspondant dans le champ instructions
5. Ajouter les fichiers du dossier `references/` en pièces jointes du skill
6. Sauvegarder : le skill s'active automatiquement dès qu'il est pertinent

#### Sur ChatGPT : [chatgpt.com/skills](https://chatgpt.com/skills)

1. Aller sur [ChatGPT](https://chatgpt.com/skills)
2. Cliquer sur **"Create skill"**
3. Donner un nom et une description au skill
4. Coller le contenu du fichier `SKILL.md` dans le champ instructions
5. Importer les fichiers du dossier `references/` dans la base de connaissances du skill
6. Publier : le skill est disponible dans vos conversations

> **Conseil :** installer un skill à la fois pour tester avant d'en ajouter d'autres.

### Sur Claude.ai (avec Claude Code ou Cowork)

```bash
git clone https://github.com/StealthyLabsHQ/ai-edu-skills-FR.git

# Installer tous les skills
cp -r ai-edu-skills-FR/soutien-academique /mnt/skills/user/
cp -r ai-edu-skills-FR/lettre-motivation /mnt/skills/user/
cp -r ai-edu-skills-FR/plume-naturelle /mnt/skills/user/
cp -r ai-edu-skills-FR/orientation-strategie /mnt/skills/user/
cp -r ai-edu-skills-FR/entretien-oral /mnt/skills/user/
cp -r ai-edu-skills-FR/productivite-pkm /mnt/skills/user/
```

> **Important :** copier le dossier entier (avec `references/`) pour que le chargement progressif fonctionne. Sans le dossier `references/`, Claude n'aura pas accès aux ressources détaillées.

### En tant que Project Instructions (claude.ai)

1. Créer un nouveau Project sur claude.ai
2. Copier le contenu de `SKILL.md` dans les instructions du projet
3. Ajouter les fichiers `references/` en tant que fichiers du projet
4. Claude les consultera automatiquement selon le contexte

### Utilisation directe (sans installation)

Copier-coller le contenu de `SKILL.md` dans la conversation ou dans les instructions système d'un appel API.

## Plume Naturelle : le moteur anti-détection

Le skill `plume-naturelle` est le plus avancé du repo. Il a été construit à partir de
l'auto-analyse de **6 modèles LLM** qui décrivent leurs propres biais de génération.

**48 patterns** de détection/humanisation, **8 phases** d'analyse, **38 formules mathématiques**
d'auto-évaluation réparties en 3 tiers :

| Tier | Formules | Coût computationnel | Accès |
|------|----------|---------------------|-------|
| **Tier 1** | Formules 1-34 : stylométrie, N-grammes, POS-tagging, burstiness, TTR, Zipf, Brunet, Gini, entropie, similarité cosinus | O(N) : instantané | Direct dans ce skill |
| **Tier 2** | Formules 35-36 : Perplexité (PPL, Cross-Entropy Loss), Ratios GLTR (buckets de rang) | O(N × V) : nécessite inférence sur modèle proxy | API LLaMA/GPT-2 |
| **Tier 3** | Formule 37 : DetectGPT (Perturbation Discrepancy, Z-score) | O(K × N × V) : très coûteux | GPU dédié |
| **Syntaxique** | Formule 38 : Variance de la profondeur des arbres syntaxiques (σ²_D) | O(N) si parseur spaCy | Tier 1 (approximation) ou parseur |

**Mode Pédagogique** : annotation du texte de l'étudiant avec codes de patterns, exercices
de remédiation ciblés, synthèse des patterns récurrents, et progression multi-sessions.

**Mode Oralité** : patterns de "plume naturelle orale" pour scripts de soutenance annotés
avec pauses, connecteurs oraux légitimes, micro-hésitations, et gestion du stress.

**Estimation :** un texte IA brut score 85-99 % sur Compilatio. Avec le skill complet
et les détails de l'étudiant, l'objectif est 5-20 % (zone invisible pour Turnitin).

## Améliorations v2 (basées sur les retours Gemini)

### Skills existants enrichis

**`lettre-motivation`** :
- Nouveau Module 5 : réseautage digital (cold emails, messages LinkedIn 300 chars, relances, remerciements post-entretien)
- Checklist interne d'auto-évaluation Claude avant livraison
- Nouvelle référence `reseautage-digital.md` : templates complets, variantes sectorielles

**`plume-naturelle`** :
- Mode Pédagogique : annotation avec 12 codes de patterns, exercices de remédiation, progression multi-sessions
- Mode Oralité : scripts de soutenance annotés, connecteurs oraux, gestion du stress à l'oral
- 4 nouvelles formules Tier 2 & 3 (PPL, GLTR, DetectGPT, σ²_D) dans `formules-auto-evaluation.md`
- Nouvelle référence `mode-pedagogique.md` : grille d'annotation complète, scripts complets

**`soutien-academique`** :
- Module 9 : soutien à la neurodiversité (TDAH, dyslexie, DYS) : adaptations, Pomodoro, fiches DYS-friendly
- Module 10 : simulateur Peer-Review (Mode Candide + Mode Reviewer 2)
- Nouvelles références `neurodiversite.md` et `peer-review-simulator.md`

### Nouveaux skills

- **`orientation-strategie`** : exploration de filières, Parcoursup, MonMaster, PFM, réorientation
- **`entretien-oral`** : entretiens blancs, STAR, réponses bateau, 50+ questions avec antidotes
- **`productivite-pkm`** : Obsidian/Zettelkasten, Notion, Zotero pour mémoires et thèses

## Philosophie

1. **Accompagner, pas remplacer** : Les skills guident l'étudiant dans sa réflexion au lieu d'écrire à sa place
2. **Rigueur académique** : Aucune source inventée, normes de citation respectées
3. **Anti-détection IA** : 48 patterns, 8 phases, 38 formules (3 tiers), 5 prompts reconstitués, questionnaire d'ancrage
4. **Adaptation au niveau** : Ajustement automatique de la profondeur selon le profil (lycée → M2)
5. **Chargement progressif** : Les références lourdes ne sont lues que quand c'est pertinent
6. **Pédagogie de l'écriture** : Mode annotation pour que l'étudiant progresse, pas seulement pour corriger
7. **Accessibilité** : Support neurodiversité (TDAH, DYS) intégré

## Consommation des modèles

La génération de fichiers (PDF, DOCX, PPTX) consomme plus de ressources que les échanges textuels :
- **claude.ai** : consomme des messages du quota plus rapidement
- **API** : augmente le nombre de tokens (et le coût)

**Conseil** : valider le contenu en texte avant de demander la mise en forme fichier.

## Contribution

Les contributions sont bienvenues. Ouvrez une issue ou une PR pour :
- Proposer de nouveaux skills (ex: skill dédié aux prépas, BTS, doctorat)
- Ajouter des références (ex: normes spécifiques à une discipline)
- Améliorer les méthodologies existantes
- Ajouter des templates de documents par discipline
- Corriger des erreurs ou enrichir les paires avant/après anti-IA

## Roadmap

- [x] Skill `soutien-academique` : Mémoires, rapports, révisions, dissertation, neurodiversité, peer-review
- [x] Skill `lettre-motivation` : LM personnalisées + réseautage digital (cold email, LinkedIn, relances)
- [x] Skill `plume-naturelle` : Réécriture anti-IA : 48 patterns, 8 phases, 38 formules (Tier 1-3), mode pédagogique, oralité
- [x] Skill `orientation-strategie` : Parcoursup, MonMaster, PFM, filières méconnues, réorientation
- [x] Skill `entretien-oral` : STAR, entretiens blancs, réponses bateau, questions pièges
- [x] Skill `productivite-pkm` : Zettelkasten, Obsidian, Notion, Zotero pour mémoires et thèses
- [ ] Skill `prepa-concours` : Préparation aux concours (CPGE, fonction publique, santé)
- [ ] Skill `bts-pro` : Spécificités BTS (épreuves E4/E6, fiches, PFMP)
- [ ] Skill `doctorat` : Accompagnement thèse (revue systématique, publication, HDR)
- [ ] Références supplémentaires par discipline (droit, santé, STAPS, info...)
- [ ] Templates DOCX/PPTX prêts à l'emploi

## Licence

MIT
