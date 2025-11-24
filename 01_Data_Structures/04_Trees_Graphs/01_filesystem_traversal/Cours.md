# Cours : Parcours de Système de Fichiers & Ransomware

## 1. Le Système de Fichiers est un Arbre

Votre disque dur n'est pas une liste plate de fichiers. C'est une structure hiérarchique : un **Arbre (Tree)**.
- La **Racine (Root)** est `/` (Linux/Mac) ou `C:\` (Windows).
- Les **Dossiers** sont des nœuds internes (branches).
- Les **Fichiers** sont des feuilles (leaves).

Pour trouver un fichier spécifique ou pour agir sur tous les fichiers (ex: antivirus, backup, ransomware), il faut **parcourir** cet arbre.

## 2. La Récursion (DFS)

La méthode la plus naturelle pour parcourir un arbre est la **Récursion** (Depth-First Search).

### Le Concept
Une fonction récursive est une fonction qui s'appelle elle-même.
Pour scanner un dossier :
1.  Je regarde ce qu'il y a dedans.
2.  Si je vois un fichier -> Je le traite.
3.  Si je vois un dossier -> **Je lance la même fonction sur ce dossier**.

### Implémentation en Python

Le module `os` est votre meilleur ami.

```python
import os

def scanner(dossier):
    # 1. Lister le contenu
    try:
        contenu = os.listdir(dossier)
    except PermissionError:
        return # On ignore les dossiers interdits

    for element in contenu:
        chemin_complet = os.path.join(dossier, element)
        
        # 2. Si c'est un dossier -> Récursion
        if os.path.isdir(chemin_complet):
            scanner(chemin_complet)
            
        # 3. Si c'est un fichier -> Action
        elif os.path.isfile(chemin_complet):
            print(f"Fichier trouvé : {chemin_complet}")
```

## 3. Application Sécurité : Ransomware

Un ransomware (logiciel de rançon) a une contrainte de **vitesse**. Il doit chiffrer vos documents avant que vous ne coupiez l'alimentation ou que l'antivirus ne réagisse.

### Logique d'un Ransomware
1.  **Priorisation** : Ne pas perdre de temps sur `C:\Windows`. Viser `C:\Users`.
2.  **Filtrage** : Chiffrer uniquement les fichiers importants (`.docx`, `.pdf`, `.jpg`, `.xls`).
3.  **Vitesse** : Utiliser le multi-threading (que nous verrons plus tard) pour parcourir l'arbre plus vite.

### Détection
Les outils de sécurité (EDR) surveillent les programmes qui :
- Ouvrent des milliers de fichiers en peu de temps.
- Modifient l'entropie des fichiers (un fichier chiffré ressemble à du bruit aléatoire).
- Parcourent l'arborescence de manière systématique.

## 4. Alternative : `os.walk`

Python fournit une fonction optimisée pour cela : `os.walk()`. Elle fait le travail récursif pour vous.

```python
for root, dirs, files in os.walk("/home/user"):
    for file in files:
        print(os.path.join(root, file))
```

C'est plus simple, mais pour comprendre l'algorithme (et pour l'exercice), il est important de savoir le faire "à la main".
