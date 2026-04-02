---
name: productivite-pkm
description: >
  Aide les étudiants à organiser leurs notes, leur bibliographie et leur gestion des
  connaissances pour un mémoire, une thèse, ou un projet de recherche. Trigger dès que
  l'utilisateur mentionne : Obsidian, Notion, Zotero, Mendeley, PKM, "personal knowledge
  management", "gestion de notes", "prise de notes", "zettelkasten", "fiches de lecture",
  "organiser ma bibliographie", "je me perds dans mes notes", "je sais plus où j'en suis
  dans mes sources", "comment structurer mes recherches", "note atomique", "second cerveau",
  "logiciel de notes", "cartes mentales pour ma thèse", "comment retrouver mes sources",
  "je prends des notes mais je les relis jamais", ou tout contexte de gestion de l'information
  dans le cadre d'un travail académique ou de recherche.
  TOUJOURS utiliser ce skill pour toute demande liée à l'organisation des connaissances,
  la gestion des sources, ou la structuration des notes dans un contexte académique.
version: 1.0.0
---

# Skill : Productivité et PKM (Personal Knowledge Management)

Organisation des notes, de la bibliographie et de la gestion des connaissances
pour les mémoires, thèses et projets de recherche académique.

---

## Principe directeur

La prise de notes sans système de récupération est une illusion de travail. Un étudiant
peut passer 50 heures à lire et prendre des notes et ne retrouver aucune idée utile
au moment d'écrire.

Un bon système PKM répond à **une seule question** : dans 6 mois, quand je chercherai
une idée précise sur [sujet X], est-ce que je la retrouve en moins de 2 minutes ?

**Règle cardinale** : le système doit coûter peu à maintenir. Un système parfait mais
jamais utilisé est inutile. Un système imparfait utilisé chaque jour est excellent.

---

## Étape 0 : Diagnostic du contexte (OBLIGATOIRE)

Avant toute recommandation d'outil ou de méthode, identifier :

- **Type de travail :** mémoire professionnel / mémoire de recherche / thèse / projet
- **Volume de sources estimé :** <20 sources / 20-50 / 50-100 / >100
- **Niveau actuel d'organisation :** chaos total / dossiers mal structurés / système partiel
- **Outils déjà utilisés :** Word, OneNote, Notion, Obsidian, papier, aucun
- **Temps disponible pour mettre en place un système :** contrainte de délai forte ?
- **Confort technique :** à l'aise avec les outils numériques, ou préfère la simplicité ?

> En cas de délai très court : recommander le système minimal viable, pas le système idéal.

---

## Module 1 : Principes fondamentaux du PKM académique

### Les 3 erreurs universelles

**Erreur 1 : La note fourre-tout**
"Je copie tout le chapitre, je relirai plus tard." → jamais relu, jamais utilisé.
Solution : ne noter que ce qu'on peut relier à un argument ou une question existante.

**Erreur 2 : L'arborescence de dossiers infinie**
Dossier > Sous-dossier > Sous-sous-dossier > Fichier introuvable.
Solution : maximum 2 niveaux de hiérarchie + tags ou liens.

**Erreur 3 : La note non-reliée**
Une idée intéressante notée seule, sans connexion avec d'autres idées.
Solution : chaque nouvelle note doit pointer vers au moins une note existante.

### Les 3 types de notes à distinguer

| Type | Contenu | Format | Outil |
|------|---------|--------|-------|
| **Note de lecture** | Résumé d'une source + citation + évaluation | Structuré (voir template) | Zotero / Obsidian |
| **Note conceptuelle** | Une idée, une définition, un concept | Court, atomique | Obsidian / Notion |
| **Note de travail** | Plan en cours, brouillon, questions ouvertes | Libre | Peu importe |

La clé : **ne pas mélanger** les trois types dans le même fichier.

---

## Module 2 : Méthode Zettelkasten adaptée au mémoire

### Principe original (Niklas Luhmann)

Le sociologue Niklas Luhmann a produit 70 livres et 400 articles avec un système
de fiches sur papier. Chaque fiche : 1 idée, 1 numéro unique, des liens vers d'autres fiches.

### Adaptation numérique pour l'étudiant français

Pas besoin d'un Zettelkasten "pur" : une adaptation simple suffit.

**Règle des notes atomiques :**
- 1 note = 1 idée (pas 1 note = 1 chapitre ou 1 auteur)
- Titre de la note = la thèse ou l'idée en 1 phrase
- Contenu : 3-10 lignes max + 1-3 liens vers d'autres notes

**Exemple :**
```
Note : "La performance financière n'est pas un bon prédicteur de la satisfaction employé"
────────────────────────────────────────────────────────────────────────────────────────
[Auteur, Année] montrent dans une méta-analyse de 200 études que la corrélation entre
ROE et satisfaction employé est faible (r = 0.12). Cette relation est modérée par la
culture nationale (voir → [[Hofstede et variables culturelles]]).

→ Contre-argument potentiel : [[Mesure de la satisfaction employé - problèmes méthodologiques]]
→ Application dans mon mémoire : [[Chapitre 2 - Limites des indicateurs financiers]]
```

**Ce qui rend ce système puissant :** quand on écrit le mémoire, on ne part pas
d'une page blanche : on assemble des notes déjà reliées.

### Workflow Zettelkasten pour un mémoire

```
Lecture d'une source
    ↓
Note de lecture (résumé + citation exacte + évaluation)
    ↓
Extraction des idées clés → 2-5 notes conceptuelles atomiques
    ↓
Liaison vers notes existantes (quelles idées ça confirme ? contredit ? enrichit ?)
    ↓
Liaison vers la structure du mémoire (quelle partie cette idée alimente-t-elle ?)
```

**Référence étendue :** `references/zettelkasten-obsidian.md` : configuration
Obsidian pour le Zettelkasten, templates de notes, plugins recommandés.

---

## Module 3 : Obsidian pour le mémoire

### Pourquoi Obsidian

- Gratuit, local (tes notes ne sont pas sur le cloud d'une entreprise)
- Basé sur Markdown (format texte universel : tes notes survivront à l'outil)
- Système de liens bidirectionnels (voir la "carte" de tes idées)
- Communauté active, nombreux templates académiques disponibles

### Structure recommandée pour un mémoire

```
📁 Vault Mémoire
├── 📁 00 - Inbox         # Notes brutes, idées rapides à traiter
├── 📁 01 - Sources       # Notes de lecture (1 fichier = 1 source)
├── 📁 02 - Concepts      # Notes atomiques (1 fichier = 1 idée)
├── 📁 03 - Mémoire       # Plan, chapitres, brouillons
│   ├── Plan.md
│   ├── Chapitre 1.md
│   └── Bibliographie.md
├── 📁 04 - Ressources    # Templates, guides méthodologiques
└── 🗺️ Carte du mémoire   # Vue graphique des liens
```

### Template de note de lecture Obsidian

```markdown
---
type: source
auteur: [NOM, Prénom]
année: [XXXX]
titre: [Titre complet]
type_source: [article / livre / rapport / thèse]
lien: [DOI ou URL]
lu_le: [date]
---

# [Titre court / mot-clé principal]

## En 1 phrase
[Ce que cette source dit de plus important pour MON mémoire]

## Arguments clés
- [Argument 1]
- [Argument 2]

## Citation utile
> "[Citation exacte]" (p. XX)

## Évaluation critique
Fiabilité : [haute / moyenne / à vérifier]
Limites : [biais méthodologique, date, contexte]

## Liens vers mes notes
→ Confirme : [[Concept X]]
→ Contredit : [[Concept Y]]
→ Alimente : [[Chapitre Z de mon mémoire]]
```

---

## Module 4 : Notion pour les mémoires collaboratifs et SAÉ

### Quand Notion > Obsidian

- Projet de groupe (collaboration en temps réel)
- Besoin d'un tableau de bord visuellement structuré
- Suivi de progression + assignation de tâches

### Structure Notion recommandée pour un groupe

```
📋 Dashboard Mémoire [Vue calendrier + vue tableau]
├── 📚 Base de données Sources
│   [Propriétés : Auteur | Année | Lu ? | Chapitre alimenté]
├── 💡 Base de données Idées
│   [Propriétés : Idée | Confirmée par | Utilisée dans]
├── 📝 Chapitres en cours
│   [Propriétés : Statut | Rédacteur | Deadline | Relu ?]
└── ✅ Suivi des tâches
    [Propriétés : Tâche | Responsable | Échéance | Fait ?]
```

### Erreurs Notion fréquentes

- Passer plus de temps à configurer Notion qu'à travailler → simplifier
- Créer des bases de données non reliées → toujours lier les pages
- Ne pas utiliser les vues filtrées → créer 1 vue "mes tâches de la semaine"

---

## Module 5 : Zotero pour la bibliographie

### Pourquoi Zotero est indispensable pour un mémoire

- Gratuit et open-source
- Import automatique des métadonnées depuis les bases de données (Google Scholar, Cairn, etc.)
- Génération automatique des bibliographies en APA, Chicago, Vancouver, etc.
- Annotations PDF synchronisées
- Intégration Word et LibreOffice

### Configuration de base

**1. Installation :**
- Zotero desktop (gratuit)
- Zotero Connector (extension navigateur) : permet de sauvegarder une source en 1 clic
- Plugin Word/LibreOffice (inclus dans l'installation)

**2. Structure des collections :**
```
📁 Mémoire [Titre]
├── 📁 Sources primaires
├── 📁 Cadre théorique
├── 📁 Méthodologie
├── 📁 À lire (inbox)
└── 📁 Non retenu (garder au cas où)
```

**3. Tags recommandés :**
- `#lu` / `#non-lu`
- `#chap1` / `#chap2` / `#chap3`
- `#à-citer` / `#contexte-seulement`
- `#fiable` / `#à-vérifier`

### Workflow Zotero + Obsidian

Pour un mémoire de niveau master :
1. **Zotero** : gestion de toutes les références bibliographiques
2. **Obsidian** : notes de lecture et notes conceptuelles liées aux références Zotero
3. **Plugin Better BibTeX** (Zotero) + **Zotero Integration** (Obsidian) : lien automatique
   entre les deux outils (citer une source Zotero directement dans Obsidian)

**Référence étendue :** `references/zotero-bibliographie.md` : configuration avancée,
styles de citation français, synchronisation cloud, export vers Word.

---

## Module 6 : Système minimal viable (pour délais serrés)

Si l'étudiant manque de temps pour mettre en place un vrai système :

### Le minimum absolu (opérationnel en 30 min)

**Outil :** Zotero seul

**Workflow :**
1. Installer Zotero + Connector
2. Créer 3 collections : "À lire", "Lu - Utile", "Lu - Pas retenu"
3. Pour chaque source lue : ajouter dans "Lu - Utile" + une note courte Zotero (3-5 lignes)
4. Au moment d'écrire : la bibliographie se génère en 1 clic

**Ce que ça ne fait pas :** liaison des idées, vue graphique, notes atomiques.
Mais ça empêche de perdre des sources et génère la bibliographie automatiquement.
C'est déjà considérable.

---

## Checklist interne avant livraison

*(Usage interne : ne pas afficher à l'utilisateur)*

- [ ] Le diagnostic (volume, délai, confort technique) a été fait ?
- [ ] Les recommandations sont-elles réalistes au regard du temps disponible ?
- [ ] Pour un délai serré : ai-je proposé le système minimal viable plutôt que l'idéal ?
- [ ] Pour un travail de groupe : Notion ou Obsidian partagé est recommandé ?
- [ ] Zotero est-il mentionné pour tout mémoire avec >10 sources ?
- [ ] Le principe "1 note = 1 idée" est-il expliqué ?

---

## Références internes

| Fichier | Quand le consulter |
|---------|-------------------|
| `references/zettelkasten-obsidian.md` | Configuration Obsidian complète, plugins, templates avancés |
| `references/zotero-bibliographie.md` | Zotero avancé : styles de citation, synchronisation, export Word |

### Skills externes (si disponibles dans l'environnement)

| Skill | Quand le consulter |
|-------|-------------------|
| `/mnt/skills/user/soutien-academique/SKILL.md` | L'étudiant a besoin d'aide sur la méthodologie de recherche elle-même |
| `/mnt/skills/user/soutien-academique/references/recherche-documentaire.md` | Comment trouver et évaluer des sources |
| `/mnt/skills/user/soutien-academique/references/normes-citation.md` | Normes de citation APA, Chicago, Vancouver, françaises |
