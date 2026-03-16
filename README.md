# anthropics-education-FR

Skills pour Claude -accompagnement scolaire et universitaire.

## Objectif

Bibliothèque de skills `.md` open-source pour transformer Claude en assistant pédagogique adapté au système éducatif français, du lycée au master.

## Arborescence

```
anthropics-education-FR/
├── README.md
├── soutien-academique/
│   ├── SKILL.md                              ← Skill principal (8 modules)
│   └── references/                           ← Ressources chargées à la demande
│       ├── normes-citation.md                ← APA 7, norme française, Harvard, Vancouver, Chicago
│       ├── ecriture-naturelle.md             ← Filtre anti-détection IA (30+ paires avant/après)
│       ├── methodologie-recherche.md         ← Quali, quanti, mixte, grilles, analyse thématique
│       ├── questions-jury.md                 ← 50+ questions de jury par catégorie + méthode PREP
│       ├── structures-par-niveau.md          ← Attentes lycée → M2 recherche (tableau comparatif)
│       ├── dissertation-commentaire.md       ← Méthodes dissertation, commentaire, arrêt, document
│       ├── templates-documents.md            ← Pages de garde, sommaires, bibliographies, charte typo
│       ├── revisions-examens.md              ← Active recall, plannings, fiches par matière, jour J
│       ├── recherche-documentaire.md         ← Google Scholar, Cairn, HAL, évaluation CRAAP, fiches de lecture
│       ├── gestion-projet-memoire.md         ← Timeline, réunions tuteur, blocages, versioning
│       ├── note-synthese.md                  ← Méthode de dépouillement, plan de synthèse, pièges
│       └── disciplines-specificites.md       ← Normes et ressources par discipline (compta, droit, SHS, info, santé)
├── lettre-motivation/
│   ├── SKILL.md                              ← Lettres de motivation personnalisées
│   └── references/
│       ├── types-candidature.md              ← Spécificités par type de candidature
│       └── anti-generique.md                 ← 20 paires avant/après anti-phrases creuses
└── plume-naturelle/
    ├── SKILL.md                              ← Réécriture anti-IA (30 patterns, double passe)
    └── references/
        └── patterns-par-discipline.md        ← Patterns IA spécifiques par discipline
```

## Comment ça fonctionne

Le système utilise un **chargement progressif à 3 niveaux** :

1. **Metadata** (toujours en contexte) -Le `name` + `description` dans le frontmatter YAML du SKILL.md. C'est ce que Claude lit pour décider s'il doit activer le skill. ~150 mots.

2. **SKILL.md** (chargé quand le skill se déclenche) -Le corps principal avec les modules, les principes, les réponses types. Contient les règles et la logique, pas les détails exhaustifs.

3. **references/** (chargé à la demande) -Les fichiers détaillés que Claude consulte uniquement quand la conversation porte sur un sujet spécifique. Par exemple, `normes-citation.md` n'est lu que si l'étudiant demande de l'aide sur sa bibliographie.

Cette architecture évite de surcharger le contexte avec des informations inutiles tout en gardant la profondeur disponible quand elle est nécessaire.

## Skills disponibles

| Skill | Modules couverts | Niveaux ciblés |
|-------|-----------------|----------------|
| `soutien-academique` | Mémoire pro, mémoire recherche, rapport de stage, soutien scolaire, dissertation/commentaire, soutenance, projets de groupe/SAÉ, spécificités disciplinaires | Lycée → Master |
| `lettre-motivation` | LM personnalisées pour école, alternance, stage, emploi, candidature spontanée, reconversion | Tous niveaux |
| `plume-naturelle` | Réécriture anti-IA : diagnostic, 30 patterns de détection, double passe, injection d'âme | Tous niveaux |

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

## Installation

### Sur Claude.ai (avec Claude Code ou Cowork)

```bash
git clone https://github.com/StealthyLabsHQ/anthropics-education-FR.git

# Installer les skills souhaités (avec leurs références)
cp -r anthropics-education-FR/soutien-academique /mnt/skills/user/
cp -r anthropics-education-FR/lettre-motivation /mnt/skills/user/
cp -r anthropics-education-FR/plume-naturelle /mnt/skills/user/
```

> **Important :** copier le dossier entier (avec `references/`) pour que le chargement progressif fonctionne. Sans le dossier `references/`, Claude n'aura pas accès aux ressources détaillées.

### En tant que Project Instructions (claude.ai)

1. Créer un nouveau Project sur claude.ai
2. Copier le contenu de `SKILL.md` dans les instructions du projet
3. Ajouter les fichiers `references/` en tant que fichiers du projet
4. Claude les consultera automatiquement selon le contexte

### Utilisation directe (sans installation)

Copier-coller le contenu de `SKILL.md` dans la conversation ou dans les instructions système d'un appel API.

## Philosophie

1. **Accompagner, pas remplacer** -Les skills guident l'étudiant dans sa réflexion au lieu d'écrire à sa place
2. **Rigueur académique** -Aucune source inventée, normes de citation respectées
3. **Anti-détection IA** -Textes naturels avec filtre intégré (vocabulaire, structure, connecteurs)
4. **Adaptation au niveau** -Ajustement automatique de la profondeur selon le profil (lycée → M2)
5. **Chargement progressif** -Les références lourdes ne sont lues que quand c'est pertinent

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

- [x] Skill `soutien-academique` -Mémoires, rapports, révisions, dissertation
- [x] Skill `lettre-motivation` -LM personnalisées tous types
- [x] Skill `plume-naturelle` -Réécriture anti-IA avec diagnostic et double passe
- [ ] Skill `prepa-concours` -Préparation aux concours (CPGE, fonction publique, santé)
- [ ] Skill `bts-pro` -Spécificités BTS (épreuves E4/E6, fiches, PFMP)
- [ ] Skill `doctorat` -Accompagnement thèse (revue systématique, publication, HDR)
- [ ] Références supplémentaires par discipline (droit, santé, STAPS, info...)
- [ ] Templates DOCX/PPTX prêts à l'emploi

## Licence

MIT
