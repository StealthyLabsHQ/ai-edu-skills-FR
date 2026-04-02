# Référence : Zotero et Bibliographie — Configuration Avancée

> **Quand charger ce fichier :** L'étudiant configure Zotero, a des problèmes avec sa
> bibliographie, veut changer de style de citation, ou a besoin d'exporter vers Word.

---

## Table des matières

1. [Configuration de base Zotero](#1-configuration-de-base)
2. [Import et gestion des sources](#2-import-des-sources)
3. [Styles de citation français](#3-styles-de-citation)
4. [Intégration Word et LibreOffice](#4-intégration-word)
5. [Annotations PDF dans Zotero](#5-annotations-pdf)
6. [Synchronisation et sauvegarde](#6-synchronisation)
7. [Erreurs fréquentes et corrections](#7-erreurs-fréquentes)

---

## 1. Configuration de base Zotero

### Installation complète

1. **Zotero Desktop** : zotero.org/download (gratuit, Windows/Mac/Linux)
2. **Zotero Connector** : extension navigateur (Chrome/Firefox/Safari) — sauvegarde une source en 1 clic depuis n'importe quelle page
3. **Plugin Word/LibreOffice** : installé automatiquement lors de l'installation de Zotero

### Paramètres recommandés (Edit > Preferences)

```
General :
  ✓ Automatically take snapshots when creating items from web pages
  ✓ At startup, reopen the last... [bibliothèque]

Sync (si compte Zotero créé) :
  ✓ Sync automatically
  ✓ Sync full-text content of files

Export :
  Format par défaut : selon la norme de votre formation (voir section 3)

Advanced :
  → Files and Folders : configurer le dossier de stockage des PDF
```

### Structure des collections recommandée

```
📚 Ma bibliothèque Zotero
├── 📁 [Titre du mémoire]
│   ├── 📁 Cadre théorique
│   ├── 📁 Méthodologie
│   ├── 📁 Contexte / terrain
│   ├── 📁 Résultats à comparer
│   └── 📁 À lire (inbox)
├── 📁 Cours [semestre]
└── 📁 Non retenu (garder — peut servir plus tard)
```

---

## 2. Import et gestion des sources

### Méthodes d'import (par ordre de fiabilité)

**1. Zotero Connector (recommandé) :**
Aller sur la page web de la source → cliquer sur l'icône Zotero dans le navigateur →
les métadonnées s'importent automatiquement (titre, auteur, date, DOI, etc.)

Fonctionne sur : Google Scholar, Cairn, PubMed, JSTOR, HAL, PERSÉE, arXiv, etc.

**2. Import par DOI / ISBN / PMID :**
Dans Zotero : icône "baguette magique" → entrer le DOI/ISBN → import automatique

**3. Import de fichier PDF :**
Glisser-déposer le PDF dans Zotero → clic droit > "Retrieve Metadata for PDF" →
Zotero cherche les métadonnées automatiquement (résultats variables)

**4. Entrée manuelle (dernier recours) :**
Bouton "+" → "New Item" → choisir le type → remplir les champs

### Tags recommandés

Systématiser les tags dès le début pour filtrer facilement :

```
État de lecture :
#lu            → Source lue et notée
#non-lu        → Dans la file d'attente
#à-relire      → Mérite une deuxième lecture
#partiel       → Seulement une partie lue

Utilisation dans le mémoire :
#chap1 / #chap2 / #chap3    → Par chapitre
#à-citer                     → Citation utile identifiée
#contexte-seulement          → Utile pour le contexte, pas à citer
#méthodologie                → Utile pour la partie méthodo

Évaluation :
#fiable         → Source validée (revue à comité, institution reconnue)
#à-vérifier     → Fiabilité incertaine
#obsolète       → Intéressant mais trop ancien pour être cité
```

### Notes Zotero

Pour chaque source lue, ajouter une note enfant (clic droit > "Add Note") :

```
Format de note recommandé :
────────────────────────────
ARGUMENT PRINCIPAL : [en 1 phrase]

CITATIONS UTILES :
p.XX : "[citation exacte]"
p.YY : "[citation exacte]"

LIEN AVEC MON MÉMOIRE :
→ Alimente [partie/argument]
→ Confirme / Nuance / Contredit [claim]

ÉVALUATION :
Méthode : [type d'étude / terrain]
Limites : [biais, date, contexte]
```

---

## 3. Styles de citation français

### Styles disponibles et leur contexte d'usage

| Style | Contexte en France | Exemple note de bas de page |
|-------|-------------------|----------------------------|
| **APA 7** | Sciences humaines, psychologie, gestion | (Dupont & Martin, 2021, p. 45) |
| **Normes françaises NF Z 44-005** | Droit, sciences politiques, histoire | Dupont, J., 2021. *Titre*. Éditeur, p. 45. |
| **Chicago Note-bibliographie** | Histoire, lettres, SHS | ¹ Jean Dupont, *Titre* (Éditeur, 2021), 45. |
| **Vancouver** | Médecine, pharmacie, sciences de la santé | [1] Dupont J, Martin P. Titre. Revue. 2021;5(2):45. |
| **Harvard** | Sciences économiques, management | (Dupont, Martin, 2021 : 45) |

### Installer un style manquant

Zotero Style Repository : zotero.org/styles
→ Rechercher le style voulu → clic → installation automatique

**Pour les normes françaises :** chercher "French" dans le repository.
Les styles les plus utilisés en France académique :
- "APA (French)" — adapté à la langue française
- "Bibliographie style Sciences Po" — pour les sciences politiques
- "French Legal" — pour le droit

### Modifier un style existant (avancé)

Si aucun style ne correspond exactement aux exigences du directeur de mémoire :
1. Télécharger le `.csl` du style le plus proche depuis le repository
2. Modifier dans un éditeur de texte (ou l'éditeur CSL en ligne)
3. Importer dans Zotero (Preferences > Cite > Styles > "+")

---

## 4. Intégration Word et LibreOffice

### Utilisation du plugin Word

Le plugin Zotero apparaît comme un onglet "Zotero" dans Word.

**Insérer une citation :**
1. Placer le curseur à l'endroit voulu dans Word
2. Cliquer "Add/Edit Citation" dans l'onglet Zotero
3. Chercher la source dans la barre de recherche
4. Sélectionner + ajouter le numéro de page si nécessaire
5. Enter → la citation s'insère dans le format choisi

**Générer la bibliographie :**
1. Placer le curseur en fin de document
2. Cliquer "Add/Edit Bibliography"
3. La bibliographie complète s'insère et se met à jour automatiquement

### Erreurs courantes avec le plugin Word

| Erreur | Cause | Solution |
|--------|-------|---------|
| "Zotero.exe is not running" | Zotero Desktop fermé | Ouvrir Zotero Desktop, puis retourner dans Word |
| Citations en texte brut (pas formatées) | Style non sélectionné | Onglet Zotero > Document Preferences > choisir le style |
| Bibliographie incomplète | Sources non citées dans le texte | Toutes les sources de la bibliographie doivent être citées au moins une fois |
| Mise en forme incorrecte | Version du style obsolète | Onglet Zotero > Refresh pour mettre à jour |

### Workflow Word + Zotero recommandé

```
1. TOUJOURS avoir Zotero Desktop ouvert quand on travaille sur le mémoire
2. Insérer les citations directement pendant la rédaction (pas après)
3. Ne JAMAIS modifier manuellement une citation insérée par Zotero
   → Elle sera écrasée lors du prochain "Refresh"
   → Corriger dans Zotero Desktop, puis "Refresh" dans Word
4. Avant le rendu final : "Unlink Citations" pour rendre le document indépendant
   → ATTENTION : cette action est irréversible — garder une copie avant
```

---

## 5. Annotations PDF dans Zotero

### Fonctionnement depuis Zotero 6+

Zotero intègre un lecteur PDF avec annotation intégrée (plus besoin d'Acrobat).

**Types d'annotations disponibles :**
- Surlignage (couleurs personnalisables)
- Note marginale
- Zone de sélection (image)
- Commentaire en plein texte

**Import des annotations dans les notes Zotero :**
Après annotation du PDF → clic droit sur l'item → "Add Note from Annotations" →
toutes les annotations exportées dans une note Zotero formatée.

### Code couleur recommandé pour annotations

| Couleur | Utilisation |
|---------|-------------|
| 🟡 Jaune | Citation utile — à potentiellement citer |
| 🔴 Rouge | Argument central — crucial pour mon mémoire |
| 🔵 Bleu | Définition ou concept à noter |
| 🟢 Vert | Méthodologie intéressante |
| 🟠 Orange | Point à vérifier ou source à trouver |

---

## 6. Synchronisation et sauvegarde

### Options de synchronisation

**Option A : Zotero Sync (officiel)**
- 300 Mo gratuit pour les fichiers joints (PDF)
- Au-delà : 2$/mois (20 Go) ou 6$/mois (illimité)
- Avantage : simple, officiel, synchronisation mobile

**Option B : WebDAV (alternative)**
- Compatible avec la plupart des services cloud (pCloud, Koofr, etc.)
- Gratuit si le service WebDAV l'est
- Configuration : Preferences > Sync > File Syncing > WebDAV

**Option C : Zotero Local + Git pour les notes**
- Bibliothèque Zotero en local (pas de sync de fichiers)
- Sync Git du Vault Obsidian (incluant les notes Zotero intégrées)
- Recommandé pour les utilisateurs avancés

### Sauvegarde manuelle

Indépendamment de la synchronisation, sauvegarder régulièrement :
1. **Bibliothèque Zotero (données)** : File > Export Library → format "Zotero RDF"
2. **Fichiers PDF** : copier le dossier `Zotero/storage` sur disque externe ou cloud
3. **Styles personnalisés** : copier les `.csl` depuis `Zotero/styles`

---

## 7. Erreurs fréquentes et corrections

| Erreur | Symptôme | Solution |
|--------|----------|---------|
| Métadonnées incorrectes après import automatique | Auteur mal orthographié, date manquante | Clic droit sur l'item > "Edit Item" → corriger manuellement |
| Doublon de source | Même source en 2 entrées | Clic droit > "Merge Items" pour les fusionner |
| PDF non joint | L'item est dans Zotero mais pas le PDF | Clic droit > "Find Available PDF" ou glisser le PDF manuellement |
| Citation mal formatée (ex: prénom avant nom) | Style paramétré pour l'anglais | Vérifier le style "French" ou adapter manuellement |
| Bibliographie avec "n.d." (no date) | Date manquante dans les métadonnées | Compléter la date dans l'item Zotero |
| Items sans collection | Items dans "Ma Bibliothèque" non classés | Sélectionner > glisser dans la collection voulue |
| Synchronisation bloquée | Conflit de version | Preferences > Sync > Reset File Sync History |

### Les 3 habitudes pour une bibliographie propre

1. **Vérifier les métadonnées à l'import** — ne pas faire confiance à l'automatique pour les sources françaises (les bases de données françaises ont des standards d'export variables)

2. **Un item = un PDF joint** — si le PDF manque, aller le chercher immédiatement (accès plus difficile plus tard)

3. **Tagger immédiatement** — un item sans tag est un item perdu dans 3 mois
