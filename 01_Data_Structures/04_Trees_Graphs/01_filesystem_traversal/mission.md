# Mission : Le Scanner de Ransomware (Simulation)

## Objectif
Comprendre comment parcourir un arbre de fichiers (Filesystem) de manière récursive. C'est la base fondamentale de tout **ransomware** ou **outil de recherche de données sensibles**.

## Contexte
Un système de fichiers est un **Arbre (Tree)** :
- La racine est le dossier de départ.
- Les dossiers sont des nœuds internes.
- Les fichiers sont des feuilles.

Pour chiffrer ou voler des données, un malware doit visiter **chaque nœud** de cet arbre le plus efficacement possible.

## Votre Mission
Vous devez compléter le script `scanner.py` pour :
1.  Parcourir récursivement le dossier `test_env`.
2.  Trouver tous les fichiers avec l'extension `.secret`.
3.  Retourner la liste des chemins absolus de ces fichiers.

## Contraintes
- Vous ne devez pas utiliser `os.walk` (trop facile !).
- Vous devez implémenter votre propre fonction récursive ou itérative (DFS).
- Utilisez `os.listdir`, `os.path.join`, `os.path.isdir`, `os.path.isfile`.

## Exemple
Si `test_env` contient :
```
test_env/
├── documents/
│   ├── projet.secret
│   └── note.txt
├── images/
│   └── vacances.jpg
└── password.secret
```

Votre fonction doit retourner :
```python
[
    "/.../test_env/documents/projet.secret",
    "/.../test_env/password.secret"
]
```

## Lancement
1.  Lancez `python3 scanner.py` pour tester votre code.
2.  Si tout fonctionne, comparez avec `solution.py`.
