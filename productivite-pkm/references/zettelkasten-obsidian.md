# Référence : Zettelkasten et Obsidian — Configuration Complète

> **Quand charger ce fichier :** L'étudiant veut configurer Obsidian pour son mémoire,
> comprendre le Zettelkasten, ou a besoin de templates avancés et de plugins recommandés.

---

## Table des matières

1. [Installation et configuration d'Obsidian](#1-configuration-obsidian)
2. [Plugins recommandés pour le mémoire](#2-plugins)
3. [Templates complets](#3-templates)
4. [Workflows avancés](#4-workflows)
5. [La vue graphique — comment la lire et l'exploiter](#5-vue-graphique)

---

## 1. Installation et configuration d'Obsidian

### Installation

1. Télécharger Obsidian sur obsidian.md (gratuit, Windows/Mac/Linux/iOS/Android)
2. Créer un "Vault" (dossier local) dédié au mémoire
3. **Ne pas** mettre le Vault dans OneDrive/Google Drive par défaut — risques de conflits
   (utiliser plutôt le plugin Obsidian Sync ou Git pour la sauvegarde)

### Paramètres recommandés (Settings)

```
Editor :
  ✓ Live Preview (mode d'édition par défaut)
  ✓ Show line numbers
  ✓ Readable line length : 90 characters
  ✗ Strict line breaks (désactiver pour faciliter la rédaction)

Files & Links :
  ✓ Default location for new notes : "In the folder specified below"
     → Choisir : 00 - Inbox
  ✓ Default location for new attachments : "In subfolder under current folder"
  ✓ Automatically update internal links

Appearance :
  Thème recommandé : "Minimal" (sobre, focus sur le contenu)
```

### Structure de Vault recommandée (rappel)

```
📁 Vault [Titre du mémoire]
├── 📁 00 - Inbox/          # Notes brutes à traiter quotidiennement
├── 📁 01 - Sources/        # 1 note par source lue
├── 📁 02 - Concepts/       # Notes atomiques (1 idée par note)
├── 📁 03 - Mémoire/        # Structure et rédaction
│   ├── 📄 _Plan.md          # Plan vivant (mis à jour)
│   ├── 📄 _Problematique.md # La question centrale
│   ├── 📄 Chapitre1.md
│   ├── 📄 Chapitre2.md
│   └── 📄 Chapitre3.md
├── 📁 04 - Ressources/     # Guides, templates, notes de cours
├── 📁 05 - Archives/       # Notes abandonnées (garder pour ne pas recréer)
└── 📄 Dashboard.md         # Vue d'ensemble (tâches, liens importants)
```

---

## 2. Plugins recommandés pour le mémoire

### Plugins Core (intégrés, à activer)

| Plugin | Activation | Utilité |
|--------|-----------|---------|
| **Templates** | Settings > Core Plugins | Insérer des templates de notes pré-formatées |
| **Daily Notes** | Settings > Core Plugins | Journal de travail quotidien |
| **Backlinks** | Settings > Core Plugins | Voir quelles notes pointent vers la note actuelle |
| **Graph View** | Settings > Core Plugins | Vue graphique des connexions |
| **Tag Pane** | Settings > Core Plugins | Navigation par tags |
| **Search** | Settings > Core Plugins | Recherche full-text dans toutes les notes |

### Plugins Community (à installer via Community Plugins)

| Plugin | Utilité | Installation |
|--------|---------|-------------|
| **Dataview** | Requêtes dans les notes (ex: "affiche toutes les sources non lues") | Community Plugins > search "Dataview" |
| **Templater** | Templates avancés avec variables dynamiques | Community Plugins > search "Templater" |
| **Zotero Integration** | Import des notes Zotero directement dans Obsidian | Community Plugins > search "Zotero Integration" |
| **Calendar** | Vue calendrier pour les Daily Notes | Community Plugins > search "Calendar" |
| **Kanban** | Tableau de suivi des tâches type Trello | Community Plugins > search "Kanban" |
| **Reading View** | Amélioration de la lisibilité en mode lecture | Community Plugins > search "Reading View" |

### Configuration Zotero Integration

Prérequis : Zotero installé + plugin "Better BibTeX for Zotero" dans Zotero.

```
1. Dans Zotero : 
   - Installer Better BibTeX (Tools > Add-ons)
   - Exporter la bibliothèque en format Better BibTeX JSON
   - Activer "Keep updated" pour mise à jour automatique

2. Dans Obsidian (Zotero Integration settings) :
   - Import formats : configurer le template d'import
   - Citation format : "@{{citekey}}" pour les citations inline
```

---

## 3. Templates complets

### Template — Note de lecture (Sources)

Sauvegarder dans `04 - Ressources/Templates/Note de lecture.md`

```markdown
---
type: source
auteur: {{auteur}}
annee: {{annee}}
titre: {{titre}}
type_source: {{article | livre | rapport | thèse | site web}}
doi_url: {{lien}}
lu_le: {{date}}
statut: {{à lire | en cours | lu | à relire}}
tags: [source, {{discipline}}, {{thème}}]
---

# {{titre court ou mot-clé}}

## En 1 phrase (pour MON mémoire)
> {{Ce que cette source apporte spécifiquement à MON argument}}

## Résumé (5-8 lignes max)
{{Résumé factuel : thèse de l'auteur, méthode, terrain}}

## Arguments clés
- {{Argument 1 — formulé comme une affirmation}}
- {{Argument 2}}
- {{Argument 3}}

## Citation(s) utile(s)
> "{{Citation exacte entre guillemets}}" (p. {{numéro}})

> "{{Deuxième citation si utile}}" (p. {{numéro}})

## Évaluation critique
Fiabilité : {{haute | moyenne | à vérifier}}
Raison : {{pourquoi cette évaluation}}
Limites : {{biais, date, contexte, échantillon}}
Lien vers sources critiques : [[{{source qui la contredit}}]]

## Concepts clés à noter
→ [[{{Concept 1 — créer la note si elle n'existe pas}}]]
→ [[{{Concept 2}}]]

## Liens vers mon mémoire
→ Alimente : [[{{Chapitre ou section du mémoire}}]]
→ Confirme : [[{{Concept ou argument dans mon mémoire}}]]
→ Nuance : [[{{Ce que ça complexifie}}]]
→ Contredit : [[{{Ce que ça remet en question}}]]
```

---

### Template — Note conceptuelle (Concepts)

Sauvegarder dans `04 - Ressources/Templates/Note conceptuelle.md`

```markdown
---
type: concept
statut: {{embryonnaire | développé | mature}}
tags: [concept, {{discipline}}, {{thème}}]
---

# {{Titre = l'idée en 1 phrase affirmative}}

## Définition courte
{{2-3 lignes : définition de travail, pas encyclopédique}}

## Développement
{{5-10 lignes max — l'essentiel, pas tout}}

## Exemple concret
{{1 exemple précis qui illustre le concept}}

## Sources qui étayent
→ [[{{Source 1}}]] — {{ce qu'elle dit sur ce concept}}
→ [[{{Source 2}}]]

## Sources qui nuancent ou contredisent
→ [[{{Source contradictoire}}]] — {{en quoi}}

## Concepts reliés
→ [[{{Concept proche}}]] — {{relation}}
→ [[{{Concept opposé}}]] — {{tension}}

## Application dans mon mémoire
→ Utilisé dans : [[{{Chapitre}}]] pour argumenter {{quoi}}
→ Statut dans mon argument : {{central | secondaire | contexte}}
```

---

### Template — Dashboard (vue d'ensemble)

Sauvegarder à la racine du Vault comme `Dashboard.md`

```markdown
# Dashboard — [Titre du mémoire]

**Deadline :** {{date de rendu}}
**Directeur :** {{nom}}
**Prochain RDV tuteur :** {{date}}

---

## Où j'en suis

```dataview
TABLE statut, auteur, annee
FROM "01 - Sources"
WHERE statut = "à lire"
SORT annee ASC
```

## Concepts à développer

```dataview
LIST
FROM "02 - Concepts"
WHERE statut = "embryonnaire"
```

## Tâches de la semaine
- [ ] {{Tâche 1}}
- [ ] {{Tâche 2}}
- [ ] {{Tâche 3}}

---

## Liens rapides
→ [[_Plan]] — Plan du mémoire
→ [[_Problematique]] — La question centrale
→ [[Bibliographie]] — Sources confirmées
```

*Note : Les blocs `dataview` nécessitent le plugin Dataview.*

---

## 4. Workflows avancés

### Workflow quotidien (15-30 min)

```
☐ Ouvrir 00 - Inbox et traiter les notes brutes d'hier
   → Pour chaque note : est-ce une Source ou un Concept ?
   → Déplacer dans le bon dossier + compléter le template

☐ Lire 1 source planifiée → créer la note de lecture
   → Extraire 2-3 concepts atomiques

☐ Vérifier les liens vers le mémoire
   → Cette nouvelle note alimente quel chapitre ?

☐ Mise à jour du Dashboard (tâches, statut chapitres)
```

### Workflow de rédaction d'un chapitre

```
1. Ouvrir la note du chapitre
2. Lancer une requête Dataview :
   "Toutes les notes conceptuelles qui alimentent ce chapitre"
3. Organiser les notes par flux argumentatif
4. Rédiger en citant les notes directement (pas en réécrivant)
5. Les transitions = les liens entre notes conceptuelles
```

### Workflow de révision (2 semaines avant rendu)

```
1. Vue graphique → identifier les "orphelins" (notes sans liens)
   → Soit les relier, soit les archiver
2. Vérifier que chaque claim du mémoire est relié à ≥1 source
3. Vérifier que chaque source lue est utilisée dans ≥1 chapitre
   (sinon : source inutile ou chapitre manquant)
4. Contrôle de cohérence : les concepts clés apparaissent-ils
   dans les bons chapitres ?
```

---

## 5. La vue graphique — comment la lire et l'exploiter

### Lecture de la vue graphique

Dans Obsidian, la vue graphique (`Ctrl+G`) montre les connexions entre toutes les notes.

**Ce que chaque élément signifie :**
- **Nœud central (gros)** : note très connectée → idée centrale de votre mémoire
- **Nœud isolé** : note non reliée → à connecter ou à archiver
- **Cluster dense** : groupe d'idées fortement liées → un chapitre potentiel
- **Pont entre clusters** : note qui relie deux domaines → souvent vos contributions originales

### Signaux d'alerte dans la vue graphique

| Signal | Interprétation | Action |
|--------|----------------|--------|
| Beaucoup de nœuds isolés | Notes non intégrées au raisonnement | Forcer les liens ou supprimer |
| 1 seul cluster très dense | Pensée trop centrée sur 1 thème | Diversifier les angles |
| Sources jamais reliées aux concepts | Lectures non intégrées | Extraction de concepts nécessaire |
| Plan séparé du reste | Rédaction déconnectée des notes | Lier chaque section du plan aux concepts |

### Filtres utiles

```
Dans la vue graphique, utiliser les filtres pour :
- Voir seulement les Sources → filter: type:source
- Voir seulement les Concepts → filter: type:concept  
- Voir seulement un thème → filter: tag:#thème
- Voir les notes non reliées → filter: isolés uniquement
```
