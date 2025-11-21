# Exercice 10 : Modules et Imports

## Objectifs

- Comprendre le système de modules en Python
- Utiliser `import` et `from...import`
- Maîtriser les modules standards (os, sys, time, datetime, random, hashlib)
- Créer ses propres modules
- Utiliser `__name__ == "__main__"`
- Organiser du code en packages
- Appliquer les modules aux contextes de cybersécurité et red teaming

## Concepts

### Instruction import basique

```python
import os
# Accès : os.getcwd(), os.listdir(), etc.
```

### Instruction from...import

```python
from os import getcwd, listdir
# Accès direct : getcwd(), listdir()
```

### Import avec alias

```python
import datetime as dt
# Accès : dt.datetime.now()

from os.path import join as path_join
# Accès direct : path_join()
```

### Modules standards essentiels

**os** : Interactions système (fichiers, répertoires, environnement)
```python
import os
os.getcwd()              # Répertoire courant
os.listdir('.')          # Lister fichiers
os.path.exists('/path')  # Vérifier existence
os.system('command')     # Exécuter commande système
```

**sys** : Interpréteur Python et paramètres système
```python
import sys
sys.argv                 # Arguments ligne de commande
sys.exit(0)             # Quitter le programme
sys.version             # Version Python
sys.platform            # Plateforme (linux, win32, darwin)
```

**time** : Gestion du temps
```python
import time
time.time()             # Timestamp Unix actuel
time.sleep(2)           # Pause en secondes
time.localtime()        # Temps local structuré
```

**datetime** : Dates et heures avancées
```python
from datetime import datetime, timedelta
datetime.now()          # Date et heure actuelles
datetime.fromtimestamp(1234567890)  # Convertir timestamp
timedelta(days=7)       # Durée (7 jours)
```

**random** : Nombres et choix aléatoires
```python
import random
random.randint(1, 100)           # Entier aléatoire
random.choice(['a', 'b', 'c'])   # Choix aléatoire
random.shuffle(liste)            # Mélanger une liste
```

**hashlib** : Hachage cryptographique
```python
import hashlib
hashlib.md5(b'texte').hexdigest()     # MD5 (déprécié)
hashlib.sha256(b'texte').hexdigest()  # SHA256
hashlib.sha512(b'texte').hexdigest()  # SHA512
```

### Créer ses propres modules

**File: utils.py**
```python
def saluer(nom):
    return f"Bonjour, {nom}!"

def additionner(a, b):
    return a + b
```

**File: main.py**
```python
import utils
print(utils.saluer("Alice"))

# Ou :
from utils import saluer
print(saluer("Bob"))
```

### `__name__ == "__main__"`

```python
def fonction():
    print("Je fais quelque chose")

if __name__ == "__main__":
    # Ce code s'exécute UNIQUEMENT si le fichier est lancé directement
    # PAS s'il est importé comme module
    fonction()
```

### Structure de packages

```
mon_projet/
├── main.py
├── utils/
│   ├── __init__.py      # Rend utils un package
│   ├── crypto.py        # Module crypto
│   └── network.py       # Module network
└── config/
    ├── __init__.py
    └── settings.py
```

## Contexte Cybersécurité et Red Teaming

Les modules sont essentiels pour :
- Automatiser des tâches système (os)
- Gérer des timestamps pour les logs (time, datetime)
- Générer des données aléatoires pour les payloads (random)
- Calculer des empreintes cryptographiques (hashlib)
- Extraire des paramètres d'exécution (sys)

## Instructions

1. Lisez le fichier `main.py`
2. Exécutez : `python main.py`
3. Observez l'utilisation des modules
4. Créez des modules personnalisés
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

## Concepts clés à retenir

- `import` charge un module entier
- `from...import` importe des éléments spécifiques
- Les modules standards offrent des fonctionnalités puissantes
- Créer des modules réutilisables organise le code
- `__name__ == "__main__"` contrôle l'exécution
- Les packages organisent les modules en hiérarchies
- Modules critiques pour automatisation et cybersécurité

## Prochaine étape

Exercice 11 : Gestion des Fichiers et Exceptions
