# Mission : Analyseur d'Arbre de Processus (Process Tree)

## Objectif
Comprendre la structure d'un **Arbre N-aire** (où un nœud peut avoir N enfants) en analysant une liste de processus. C'est crucial pour la **détection d'intrusions (EDR)** et l'**évasion**.

## Contexte
Dans un OS, chaque processus a un `PID` (Process ID) et un `PPID` (Parent Process ID).
L'ensemble forme un arbre :
- `init` (Linux) ou `System` (Windows) est la racine.
- Chaque processus est un nœud.
- Les processus qu'il lance sont ses enfants.

**En Sécurité** : Certaines relations parent-enfant sont suspectes.
- Exemple : `winword.exe` (Word) qui lance `cmd.exe` ou `powershell.exe`. C'est souvent une macro malveillante !

## Votre Mission
Vous devez compléter `analyzer.py` pour :
1.  Construire un arbre de processus à partir d'une liste plate de processus (dictionnaires).
2.  Parcourir cet arbre pour détecter des anomalies.
3.  Signaler si `word.exe` a lancé `cmd.exe` ou `powershell.exe`.

## Données
Une liste de processus simulée :
```python
processes = [
    {"pid": 1, "ppid": 0, "name": "system"},
    {"pid": 100, "ppid": 1, "name": "explorer.exe"},
    {"pid": 200, "ppid": 100, "name": "word.exe"},
    {"pid": 300, "ppid": 200, "name": "cmd.exe"},  # SUSPECT !
]
```

## Structure de Données
Utilisez une classe `ProcessNode` :
```python
class ProcessNode:
    def __init__(self, pid, name):
        self.pid = pid
        self.name = name
        self.children = []  # Liste d'enfants (N-aire)
```

## Lancement
1.  Lancez `python3 analyzer.py`.
2.  Vérifiez si votre code détecte l'alerte de sécurité.
