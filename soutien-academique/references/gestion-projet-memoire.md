# Gestion de projet pour un memoire

**Quand charger cette reference** : l'etudiant demande de l'aide pour organiser le calendrier de son memoire, planifier ses reunions avec son directeur/tuteur, surmonter un blocage d'ecriture (page blanche, procrastination, syndrome de l'imposteur), ou mettre en place un systeme de versioning de son document.

---

## 1. Timeline type par niveau

### BUT (2-3 mois)

| Semaine | Jalon | Livrable |
|---------|-------|----------|
| S1-S2 | Choix du sujet et validation | Fiche de sujet signee |
| S3-S4 | Recherche documentaire | Bibliographie annotee (10-15 sources) |
| S5-S6 | Redaction du plan detaille | Plan detaille valide par le tuteur |
| S7-S8 | Redaction du corps | Brouillon complet (introduction, parties, conclusion) |
| S9-S10 | Relecture et corrections | Version relue, mise en forme |
| S11-S12 | Finalisation et depot | Document final + preparation soutenance |

### Master 1 (4 mois)

| Semaine | Jalon | Livrable |
|---------|-------|----------|
| S1-S2 | Cadrage du sujet | Fiche de cadrage (sujet, problematique, methode envisagee) |
| S3-S4 | Revue de litterature initiale | Fiche de lecture pour chaque source cle (15-20 sources) |
| S5-S6 | Construction du cadre theorique | Plan detaille + introduction provisoire |
| S7-S8 | Collecte de donnees / terrain | Grille d'entretien, questionnaire, ou protocole |
| S9-S10 | Analyse des resultats | Chapitre resultats (brouillon) |
| S11-S12 | Redaction partie discussion | Discussion + limites (brouillon) |
| S13-S14 | Relecture globale | Version complete relue |
| S15-S16 | Corrections finales et depot | Document final + preparation soutenance |

**Livrable intermediaire recommande** : remettre les chapitres 1 et 2 au tuteur a la fin de S8 pour un retour avant de poursuivre.

### Master 2 recherche (6 mois)

| Semaine | Jalon | Livrable |
|---------|-------|----------|
| S1-S3 | Cadrage et etat de l'art preliminaire | Note de cadrage + premiere bibliographie (30+ sources) |
| S4-S6 | Revue de litterature approfondie | Chapitre revue de litterature (brouillon) |
| S7-S9 | Cadre theorique et methodologie | Chapitre methodologie (brouillon) |
| S10-S12 | Collecte de donnees / experimentation | Donnees brutes, journal de terrain |
| S13-S15 | Analyse des resultats | Chapitre resultats (brouillon) |
| S16-S18 | Redaction discussion et conclusion | Chapitres discussion + conclusion (brouillon) |
| S19-S21 | Relecture complete, introduction generale | Version complete integree |
| S22-S24 | Corrections, mise en forme, depot | Document final + preparation soutenance |

**Livrable intermediaire 1** : chapitre revue de litterature a S6.
**Livrable intermediaire 2** : chapitres methodologie + resultats a S15.

### Diagramme de Gantt simplifie (Master 2 recherche, 24 semaines)

```
Semaine        1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
               |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
Cadrage        =========#
Revue litt.          ==========#
                              LI1
Methodologie               ==========#
Collecte                         ==========#
Analyse                                ==========#
                                             LI2
Discussion                                      ==========#
Relecture                                              ==========#
Finalisation                                                  =========#
                                                                      DEPOT

Legende : === phase active | # jalon | LI1/LI2 livrable intermediaire | DEPOT date limite
```

---

## 2. Reunions avec le tuteur

### Frequence recommandee

| Niveau | Frequence | Remarque |
|--------|-----------|----------|
| BUT | Toutes les 2-3 semaines | Le tuteur est souvent a l'initiative des RDV |
| Master 1 | Toutes les 2-3 semaines | Prendre l'initiative de demander les RDV |
| Master 2 recherche | Toutes les 2 semaines minimum | Plus rapproche en phase de terrain et de redaction finale |

### Quoi preparer avant chaque reunion

Arriver les mains vides a une reunion, c'est perdre du temps pour tout le monde. Avant chaque RDV, preparer :

1. **Un point d'avancement** : ce qui a ete fait depuis la derniere reunion (meme si c'est peu).
2. **Les questions precises** : pas "je suis bloque", mais "j'hesite entre telle et telle approche pour analyser mes donnees, voici les arguments pour chacune".
3. **Les blocages identifies** : decrire le probleme concretement et ce qui a deja ete tente.
4. **Un document a jour** : envoyer la derniere version du memoire 48h avant la reunion pour que le tuteur ait le temps de la lire.

### Template d'email pour demander un rendez-vous

```
Objet : Memoire [INTITULE COURT] - Demande de rendez-vous

Bonjour [Madame/Monsieur NOM],

Je me permets de vous contacter pour fixer un rendez-vous concernant
mon memoire sur [sujet en une ligne].

Depuis notre dernier echange, j'ai avance sur les points suivants :
- [point 1]
- [point 2]

J'aurais besoin de votre avis sur :
- [question 1]
- [question 2]

Seriez-vous disponible dans les deux prochaines semaines ? Je suis
libre [proposer 2-3 creneaux]. Je vous enverrai ma derniere version
du document avant notre rencontre.

En vous remerciant,
[Prenom NOM]
[Formation, annee]
```

### Template de compte-rendu de reunion

Envoyer ce compte-rendu au tuteur dans les 24h suivant la reunion.

```
COMPTE-RENDU DE REUNION - MEMOIRE
==================================
Date : [JJ/MM/AAAA]
Presents : [etudiant], [tuteur]
Duree : [XX min]

POINTS DISCUTES
---------------
1. [Sujet aborde]
   - [Ce qui a ete dit / decide]

2. [Sujet aborde]
   - [Ce qui a ete dit / decide]

DECISIONS PRISES
----------------
- [Decision 1]
- [Decision 2]

PROCHAINES ETAPES (pour l'etudiant)
------------------------------------
- [ ] [Tache 1] - echeance : [date]
- [ ] [Tache 2] - echeance : [date]
- [ ] [Tache 3] - echeance : [date]

PROCHAINE REUNION
-----------------
Date prevue : [JJ/MM/AAAA] ou a fixer avant le [date]
```

### Comment gerer un tuteur peu disponible

C'est une situation courante. Voici des strategies concretes :

- **Etre proactif** : ne pas attendre que le tuteur propose un RDV. Envoyer un email avec des creneaux precis.
- **Envoyer des avancements courts par email** : meme sans reunion, un email de 5 lignes toutes les deux semaines montre que le travail avance et maintient le lien.
- **Poser des questions fermees** : au lieu de "qu'en pensez-vous ?", ecrire "j'hesite entre A et B, je penche pour A parce que [raison]. Est-ce que ca vous semble correct ?". Le tuteur peut repondre en une ligne.
- **Fixer des deadlines claires** : "je prevois de boucler le chapitre 2 pour le 15 mars, pourriez-vous me faire un retour d'ici le 22 mars ?"
- **Avoir un plan B** : identifier un co-encadrant, un doctorant du labo, ou un camarade avance qui peut relire en attendant.
- **En dernier recours** : si l'absence de retour met en danger le calendrier, alerter le responsable de formation ou la scolarite. C'est un droit, pas une delation.

---

## 3. Gestion du blocage

### Page blanche

La page blanche n'est pas un probleme de competence, c'est un probleme de demarrage. Voici des techniques qui fonctionnent :

- **Ecrire mal d'abord** : se donner la permission d'ecrire un brouillon nul. Le but est de remplir la page, pas de produire un texte parfait. On corrigera apres. Un mauvais paragraphe est toujours mieux qu'un paragraphe inexistant.
- **Technique Pomodoro** : regler un minuteur sur 25 minutes. Pendant ces 25 minutes, ecrire sans s'arreter, sans relire, sans corriger. Pause de 5 minutes. Recommencer. Apres 4 cycles, pause longue de 15-20 minutes.
- **Commencer par la partie la plus facile** : rien n'oblige a ecrire dans l'ordre. Si la methodologie est claire, commencer par la. L'introduction se redige souvent en dernier.
- **Parler avant d'ecrire** : expliquer a voix haute (ou a un ami) ce qu'on veut dire, puis ecrire ce qu'on vient de dire. Le langage oral est plus fluide que l'ecrit.
- **Lister avant de rediger** : ecrire 5-10 points a aborder dans la section sous forme de liste, puis transformer chaque point en paragraphe.

### Procrastination

La procrastination vient souvent de taches trop grosses et trop floues. La solution : decouper.

- **Micro-taches de 25 minutes** : au lieu de "rediger le chapitre 2", ecrire "rediger le paragraphe sur la definition du concept X (25 min)".
- **Regle des 2 minutes** : si une tache prend moins de 2 minutes (envoyer un email, ajouter une reference), la faire tout de suite.
- **To-do list quotidienne** : maximum 3 taches par jour liees au memoire. Pas plus, pour eviter l'effet decourageant d'une liste interminable.
- **Ritualiser le travail** : meme lieu, meme heure, meme routine de demarrage (ouvrir le fichier, relire le dernier paragraphe, ecrire).

### Perfectionnisme

Le perfectionnisme est l'ennemi du memoire termine. A retenir :

> **Un memoire rendu vaut mieux qu'un memoire parfait jamais fini.**

- La premiere version n'a pas besoin d'etre bonne. Elle a besoin d'exister.
- Le tuteur est la pour corriger et guider. Lui envoyer un travail imparfait, c'est lui permettre de faire son travail.
- Les corrections font partie du processus normal. Personne ne redige un memoire en une seule passe.
- Se fixer une limite : maximum 2 relectures par chapitre avant envoi au tuteur. Au-dela, on tourne en rond.

### Syndrome de l'imposteur

Le syndrome de l'imposteur est **normal et frequent** chez les etudiants qui redigent un memoire. Les pensees typiques :

- "Je ne comprends pas assez bien mon sujet pour ecrire dessus."
- "Tout a deja ete dit, je n'apporte rien."
- "Mon tuteur va voir que je ne suis pas au niveau."

Reponses a se repeter :

- **On n'attend pas de tout comprendre pour ecrire. On ecrit pour comprendre.** L'ecriture est un outil de reflexion, pas seulement un produit fini.
- Un memoire de Master n'est pas une these. On n'attend pas une contribution revolutionnaire, mais une demarche rigoureuse.
- Le tuteur sait qu'on est etudiant. Il n'attend pas la perfection, il attend du travail et de la progression.
- Parler de ses doutes (tuteur, camarades, proches) est sain. Les garder pour soi les amplifie.

### Quand alerter le tuteur ou la scolarite

Certaines situations necessitent d'alerter :

- **Blocage de plus de 2-3 semaines** sans aucune production ecrite, malgre les techniques ci-dessus.
- **Probleme d'acces au terrain** (refus d'entretien, donnees indisponibles) qui remet en cause la faisabilite du memoire.
- **Problemes personnels** (sante, financiers, familiaux) qui empechent de travailler. Les universites ont des dispositifs d'aide : assistantes sociales, services de sante, amenagements d'examens.
- **Conflit avec le tuteur** : en parler au responsable de formation, pas sur les reseaux sociaux.
- **Retard important sur le calendrier** (plus de 3 semaines de retard sur le planning initial) : mieux vaut prevenir tot que decouvrir le probleme au moment du depot.

---

## 4. Versioning du document

### Convention de nommage

Utiliser un schema de nommage clair et constant :

```
Memoire_NOM_v1.2_2024-03-15.docx
```

Ou :
- `NOM` : nom de famille de l'etudiant
- `v1.2` : numero de version (majeur.mineur)
  - **Version majeure** (v1, v2, v3) : restructuration importante, nouveau chapitre complet
  - **Version mineure** (v1.1, v1.2) : corrections, ajouts de paragraphes, modifications locales
- `2024-03-15` : date au format ISO (annee-mois-jour) pour un tri chronologique facile

Exemples concrets :

```
Memoire_DUPONT_v0.1_2024-01-20.docx    <- premier plan detaille
Memoire_DUPONT_v0.5_2024-02-10.docx    <- brouillon partiel
Memoire_DUPONT_v1.0_2024-03-01.docx    <- premiere version complete
Memoire_DUPONT_v1.1_2024-03-10.docx    <- apres retour tuteur
Memoire_DUPONT_v2.0_2024-03-25.docx    <- restructuration majeure
Memoire_DUPONT_vFINALE_2024-04-15.docx <- version deposee
```

### Regle d'or : ne jamais ecraser un fichier

**Ne jamais enregistrer par-dessus une version precedente.** Toujours faire "Enregistrer sous" avec un nouveau numero de version. Si on a casse quelque chose, on peut toujours revenir en arriere.

Creer un dossier `_archives` pour ranger les anciennes versions et garder le dossier principal propre :

```
Memoire/
  Memoire_DUPONT_v2.1_2024-03-20.docx    <- version de travail actuelle
  _archives/
    Memoire_DUPONT_v0.1_2024-01-20.docx
    Memoire_DUPONT_v1.0_2024-03-01.docx
    Memoire_DUPONT_v1.1_2024-03-10.docx
    Memoire_DUPONT_v2.0_2024-03-15.docx
```

### Sauvegarde dans le cloud

Utiliser **OneDrive**, **Google Drive** ou **Nextcloud** (souvent propose par l'universite) :

- Activer la **synchronisation automatique** du dossier du memoire.
- Verifier que l'**historique des versions** est active (Google Drive et OneDrive le font par defaut). Cela permet de restaurer une version anterieure meme si on a enregistre par-dessus par erreur.
- Ne pas compter uniquement sur le cloud : ce n'est pas une sauvegarde, c'est une synchronisation. Si on supprime un fichier localement, il disparait aussi du cloud.

### Regle de sauvegarde 3-2-1 simplifiee

La regle professionnelle 3-2-1 adaptee aux etudiants :

- **3 copies** du fichier : une sur l'ordinateur, une sur le cloud, une sur un support externe.
- **2 supports differents** : disque dur de l'ordinateur + cle USB ou disque dur externe.
- **1 copie distante** : le cloud (Google Drive, OneDrive, etc.).

En pratique, le minimum vital :

```
1. Ordinateur          -> travail quotidien
2. Google Drive/OneDrive -> synchronisation automatique
3. Cle USB             -> copie manuelle 1x par semaine (ou a chaque version majeure)
```

Faire un rappel hebdomadaire dans son agenda : "Sauvegarder le memoire sur cle USB".

### Git pour les etudiants en informatique

Pour les etudiants en informatique ou ceux qui redigent en LaTeX, **Git** est un outil de versioning bien plus puissant :

- Chaque modification est tracee avec un message de commit.
- On peut revenir a n'importe quel etat precedent du document.
- On peut travailler sur des branches (par exemple une branche pour tester une restructuration).
- Depot distant sur **GitHub** ou **GitLab** (les universites proposent souvent une instance GitLab).

Cela depasse le cadre de cette fiche, mais c'est une competence utile a developper pour les profils techniques.

---

## 5. Integrer les feedbacks du tuteur

Recevoir des commentaires sur son travail peut etre destabilisant. Voici une methode pour les traiter efficacement.

### Etape 1 : Lire tous les commentaires avant de modifier

Ne pas commencer a corriger des le premier commentaire lu. Lire l'ensemble des retours pour avoir une vision globale. Certains commentaires se recoupent, d'autres se contredisent (le tuteur a pu changer d'avis en lisant la suite).

### Etape 2 : Classer les commentaires

Creer trois categories :

| Type | Description | Exemple | Priorite |
|------|-------------|---------|----------|
| **Structurel** | Concerne l'organisation, le plan, la logique d'ensemble | "Cette partie devrait etre avant la methodologie" | Haute |
| **Redactionnel** | Concerne le style, la clarte, la grammaire | "Reformuler cette phrase, trop longue" | Moyenne |
| **Suggestion** | Idee complementaire, reference a ajouter, piste a explorer | "Tu pourrais aussi citer Untel (2020)" | Basse |

### Etape 3 : Traiter le structurel d'abord

Les modifications structurelles (deplacer des sections, fusionner des chapitres, supprimer une partie) impactent tout le reste. Les faire en premier evite de peaufiner un paragraphe qui sera supprime ensuite.

Ordre de traitement recommande :

1. Modifications structurelles (plan, organisation)
2. Modifications de contenu (arguments, donnees, references)
3. Modifications redactionnelles (style, clarte)
4. Corrections de forme (orthographe, mise en page)

### Etape 4 : Ne pas tout reecrire a chaque retour

Un retour du tuteur ne signifie pas qu'il faut tout recommencer. Identifier ce qui doit changer et ce qui peut rester en l'etat. Si le tuteur ne commente pas une partie, c'est generalement qu'elle est acceptable.

Piege a eviter : reecrire completement un chapitre a chaque retour, au risque d'introduire de nouveaux problemes et de ne jamais converger vers une version finale.

### Etape 5 : Tracker les modifications

- **Dans Word** : utiliser le **mode Revision** (onglet Revision > Suivi des modifications). Le tuteur verra exactement ce qui a change.
- **Dans Google Docs** : utiliser le **mode Suggestion** pour les modifications et les **commentaires** pour les reponses.
- **Dans LaTeX** : utiliser le package `changes` ou `latexdiff` pour generer un document montrant les differences.

### Etape 6 : Repondre au tuteur

Apres avoir integre les retours, envoyer un email ou un document recapitulatif. Le tuteur appreciera de savoir ce qui a ete pris en compte.

```
Objet : Memoire [SUJET] - Retour sur vos commentaires (v1.1 -> v1.2)

Bonjour [Madame/Monsieur NOM],

Veuillez trouver ci-joint la version mise a jour de mon memoire (v1.2)
integrant vos retours du [date].

Voici un recapitulatif des modifications :

MODIFICATIONS EFFECTUEES
- [Commentaire 1] : corrige. J'ai deplace la section X avant la
  section Y comme suggere.
- [Commentaire 2] : corrige. J'ai ajoute la reference a Untel (2020)
  et developpe l'argument en p.12.
- [Commentaire 3] : corrige. Phrase reformulee en p.8.

POINTS NON MODIFIES (avec justification)
- [Commentaire 4] : j'ai choisi de conserver la structure actuelle
  car [raison]. Je reste ouvert(e) a en discuter si vous pensez
  que c'est necessaire.

QUESTIONS EN SUSPENS
- [Question 1]
- [Question 2]

N'hesitez pas a me faire part de vos remarques.

Cordialement,
[Prenom NOM]
```

Ce recapitulatif montre au tuteur que ses commentaires ont ete lus, reflechis et traites serieusement. Il accelere aussi les echanges car le tuteur n'a pas besoin de tout relire pour verifier si ses retours ont ete pris en compte.

---

## Recapitulatif : checklist hebdomadaire du memoire

```
[ ] J'ai travaille au moins [X] heures sur le memoire cette semaine
[ ] J'ai produit du texte (meme imparfait)
[ ] J'ai sauvegarde ma version actuelle (cloud + support externe)
[ ] J'ai mis a jour mon planning si necessaire
[ ] J'ai prepare / envoye un point d'avancement au tuteur si c'est la semaine prevue
[ ] J'ai note mes questions et blocages pour la prochaine reunion
```
