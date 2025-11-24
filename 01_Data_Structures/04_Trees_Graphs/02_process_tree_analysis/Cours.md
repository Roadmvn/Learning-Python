# Cours : Arbres de Processus & Evasion

## 1. La Hiérarchie des Processus

Dans un système d'exploitation (Windows, Linux, macOS), chaque programme en cours d'exécution est un **Processus**.
Ces processus ne naissent pas de nulle part : ils sont créés par d'autres processus.

Cela forme un **Arbre N-aire** (un parent peut avoir N enfants).

### Structure
- **PID (Process ID)** : Identifiant unique du processus.
- **PPID (Parent Process ID)** : Identifiant du parent qui l'a créé.

**Exemple Linux :**
```
init (1)
 ├── systemd (100)
 │    └── sshd (500)
 │         └── bash (501)
 │              └── python (600)
 └── chrome (200)
      ├── chrome_renderer (201)
      └── chrome_renderer (202)
```

## 2. Relations Suspectes (Parent-Enfant)

En sécurité offensive (Red Team) et défensive (Blue Team), l'analyse de cet arbre est cruciale.

### La Chaîne d'Attaque Classique (Phishing)
1.  La victime ouvre une pièce jointe (Word/Excel).
2.  Le document contient une Macro malveillante.
3.  La Macro lance une commande système (PowerShell/CMD).
4.  La commande télécharge le malware.

**Signature dans l'arbre :**
`WINWORD.EXE` (Parent) -> `CMD.EXE` (Enfant)

C'est une anomalie ! Word est un éditeur de texte, il n'est pas censé lancer un terminal de commande. Les EDR (Endpoint Detection and Response) bloquent cela immédiatement.

## 3. Techniques d'Evasion

Les attaquants essaient de casser cette chaîne parent-enfant pour se cacher.

### PPID Spoofing (Usurpation de Parent)
Au lieu de lancer le malware directement (ce qui dirait "Parent = Moi"), l'attaquant demande à Windows de lancer le malware en disant "Le Parent est `explorer.exe`".

**Résultat :**
L'arbre ressemble à : `explorer.exe` -> `malware.exe`.
C'est beaucoup plus discret, car `explorer.exe` lance légitimement plein de programmes.

### Process Injection / Migration
Le malware démarre, puis injecte son code dans un processus légitime existant (ex: `notepad.exe`).
Le malware initial se termine. Le code malveillant tourne maintenant *à l'intérieur* de `notepad.exe`.

## 4. Analyse Forensique

Pour l'exercice, nous allons jouer le rôle de l'EDR. Nous allons reconstruire l'arbre des processus à partir d'une liste (comme celle fournie par la commande `ps` ou le Gestionnaire des tâches) et chercher des anomalies.

Il faudra :
1.  Lier chaque processus à son parent via le PPID.
2.  Parcourir l'arbre.
3.  Vérifier si un nœud "Bureautique" a un enfant "Système/Terminal".
