# Exercice 11 : Gestion de Fichiers

## Objectifs

- Maîtriser l'ouverture et fermeture de fichiers (`open`, `close`)
- Utiliser le context manager `with` pour gérer les fichiers proprement
- Comprendre les modes de fichiers (r, w, a, rb, wb, etc.)
- Lire et écrire du contenu texte dans les fichiers
- Travailler avec le format JSON
- Gérer les chemins de fichiers (`os.path`, `pathlib`)
- Appliquer aux contextes de cybersécurité et red teaming

## Concepts

### Fonction open()

```python
# Syntaxe basique
fichier = open('nom_fichier.txt', mode='r', encoding='utf-8')

# Modes disponibles :
# 'r'  : lecture (défaut) - fichier doit exister
# 'w'  : écriture - crée ou écrase le fichier
# 'a'  : ajout - ajoute à la fin du fichier
# 'x'  : création exclusive - erreur si existe
# 'b'  : binaire (rb, wb, ab)
# 't'  : texte (défaut)
# '+'  : lecture ET écriture (r+, w+, a+)
```

### Lecture de fichiers

```python
# Lire tout le fichier
contenu = fichier.read()

# Lire ligne par ligne
ligne = fichier.readline()

# Lire toutes les lignes dans une liste
lignes = fichier.readlines()

# Itérer sur les lignes
for ligne in fichier:
    print(ligne.strip())
```

### Écriture de fichiers

```python
# Écrire du texte
fichier.write("Bonjour!")

# Écrire plusieurs lignes
fichier.writelines(["ligne 1\n", "ligne 2\n"])

# Ajouter à la fin
with open('fichier.txt', 'a') as f:
    f.write("\nNouvelle ligne")
```

### Context Manager avec `with`

```python
# Recommandé : ferme automatiquement le fichier
with open('fichier.txt', 'r') as f:
    contenu = f.read()
# Fichier fermé automatiquement après le bloc with

# Non recommandé : risque d'oublier de fermer
f = open('fichier.txt', 'r')
contenu = f.read()
f.close()  # À ne pas oublier !
```

### Modes de fichiers détaillés

| Mode | Description | Crée ? | Écrase ? | Pointeur |
|------|-------------|--------|----------|----------|
| r    | Lecture     | Non    | N/A      | Début    |
| w    | Écriture    | Oui    | Oui      | Début    |
| a    | Ajout       | Oui    | Non      | Fin      |
| x    | Création    | Oui    | Erreur   | Début    |
| r+   | Lec/Écr     | Non    | Non      | Début    |
| w+   | Écr/Lec     | Oui    | Oui      | Début    |
| rb   | Lecture binaire    | Non    | N/A      | Début    |
| wb   | Écriture binaire   | Oui    | Oui      | Début    |

### Module JSON

```python
import json

# Lire JSON d'un fichier
with open('data.json', 'r') as f:
    data = json.load(f)

# Écrire JSON dans un fichier
with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)

# Convertir chaîne JSON en objet Python
objet = json.loads('{"nom": "Alice"}')

# Convertir objet Python en chaîne JSON
chaine_json = json.dumps({"nom": "Bob"}, indent=2)
```

### Chemins de fichiers avec os.path

```python
import os

# Vérifier existence
if os.path.exists('/chemin/fichier.txt'):
    print("Fichier existe")

# Jointure de chemins
chemin = os.path.join('/home/user', 'dossier', 'fichier.txt')

# Obtenir le nom du fichier
nom = os.path.basename('/home/user/fichier.txt')  # fichier.txt

# Obtenir le répertoire
rep = os.path.dirname('/home/user/fichier.txt')  # /home/user

# Chemin absolu
absolu = os.path.abspath('fichier.txt')

# Vérifier si c'est un fichier/dossier
os.path.isfile(chemin)
os.path.isdir(chemin)
```

### Chemins de fichiers avec pathlib

```python
from pathlib import Path

# Créer un objet Path
p = Path('/home/user/fichier.txt')

# Vérifier existence
if p.exists():
    print("Fichier existe")

# Lire contenu
contenu = p.read_text()

# Écrire contenu
p.write_text("Bonjour!")

# Obtenir le nom
p.name  # fichier.txt

# Obtenir le répertoire parent
p.parent  # /home/user

# Vérifier type
p.is_file()
p.is_dir()

# Jointure de chemins
nouveau_chemin = p.parent / 'autre.txt'
```

### Gestion d'erreurs avec fichiers

```python
try:
    with open('fichier.txt', 'r') as f:
        contenu = f.read()
except FileNotFoundError:
    print("Fichier non trouvé")
except IOError as e:
    print(f"Erreur d'E/S : {e}")
except Exception as e:
    print(f"Erreur : {e}")
```

## Contexte Cybersécurité et Red Teaming

La gestion de fichiers est critique pour :
- **Logs d'attaques** : écrire les timestamps et détails des tentatives
- **Sauvegarde de configurations** : stocker les paramètres d'attaque
- **Stockage de credentials** : gérer les données sensibles (JSON)
- **Résultats de scans** : exporter les résultats de reconnaissance
- **Payloads** : lire les payloads depuis des fichiers
- **Traces** : gérer les logs de reconnaissance

## Instructions

1. Lisez le fichier `main.py`
2. Exécutez : `python main.py`
3. Observez l'utilisation des fichiers et du JSON
4. Testez la lecture/écriture de fichiers
5. Essayez les défis dans `exercice.txt`

## Durée estimée

4-5 heures

## Prérequis

- Exercice 01 : Hello Print
- Exercice 02 : Variables et Types
- Exercice 03 : Input et Output
- Exercice 04 : Opérateurs
- Exercice 05 : Structures Conditionnelles
- Exercice 06 : Boucles
- Exercice 07 : Listes et Tuples
- Exercice 08 : Dictionnaires
- Exercice 09 : Fonctions
- Exercice 10 : Modules et Imports

## Concepts clés à retenir

- `open()` ouvre un fichier avec un mode spécifique
- `with` ferme automatiquement le fichier (recommandé)
- Modes : r (lecture), w (écriture), a (ajout), b (binaire)
- `read()`, `readline()`, `readlines()` pour lire
- `write()`, `writelines()` pour écrire
- JSON pour stocker des données structurées
- `os.path` et `pathlib` gèrent les chemins portablement
- Toujours fermer les fichiers ou utiliser `with`

## Prochaine étape

Exercice 12 : Gestion des Exceptions
