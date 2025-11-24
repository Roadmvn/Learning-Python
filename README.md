# Apprentissage Python : De Zéro au Red Teaming

## Description

Ce projet est un parcours d'apprentissage complet de Python, débutant des concepts les plus basiques (print, variables) jusqu'aux techniques avancées de red teaming et développement de malware éthique.

**Durée estimée : 6-8 semaines de pratique intensive**

## Avertissements Éthiques et Légaux

### IMPORTANT - LIRE AVANT DE COMMENCER

Ce matériel pédagogique contient des techniques offensives de cybersécurité. **L'utilisation de ces outils est strictement encadrée** :

**AUTORISÉ :**
- Environnements de test personnels (machines virtuelles isolées)
- Laboratoires de formation en cybersécurité
- Compétitions CTF (Capture The Flag)
- Penetration testing avec autorisation écrite explicite
- Recherche académique en sécurité informatique

**STRICTEMENT INTERDIT :**
- Attaques contre des systèmes sans autorisation écrite
- Utilisation malveillante des outils développés
- Violation de la vie privée d'autrui
- Toute activité illégale

**Responsabilité :** L'utilisateur de ce matériel est seul responsable de ses actions. La violation des lois sur la cybercriminalité peut entraîner des poursuites pénales graves.

## Prérequis

### Système
- Python 3.10 ou supérieur
- Système d'exploitation : Linux (recommandé), macOS, ou Windows
- 2 Go d'espace disque disponible
- Connexion Internet pour l'installation des dépendances

### Connaissances
- Aucune connaissance en programmation requise
- Compréhension basique de l'utilisation du terminal
- Motivation pour apprendre

## Installation

### 1. Cloner ou télécharger le projet

```bash
cd ~/Desktop
git clone [URL_DU_REPO] learning-python
cd learning-python
```

### 2. Vérifier la version de Python

```bash
python3 --version
# Doit afficher Python 3.10.0 ou supérieur
```

### 3. Créer un environnement virtuel

```bash
python3 -m venv venv
source venv/bin/activate  # Sur Linux/macOS
# OU
venv\Scripts\activate     # Sur Windows
```

### 4. Installer les dépendances

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Exécuter le script de setup (optionnel)

```bash
chmod +x setup.sh
./setup.sh
```

## Structure du Projet

```
learning-python/
├── README.md              ← Vous êtes ici
├── PROGRESSION.md         ← Plan de progression détaillé
├── requirements.txt       ← Dépendances Python
├── setup.sh              ← Script d'installation automatique
├── .gitignore            ← Fichiers à ignorer par Git
├── 00_CS_Fundamentals/   ← Bases de l'informatique
├── 01_Data_Structures/   ← Structures de données (Trees, Graphs...)
├── 02_Algorithms/        ← Algorithmes (Bit Manipulation, Sorting...)
├── 03_Systems_Programming/ ← Programmation Système
├── 04_Object_Oriented_Design/ ← Conception Orientée Objet
└── 05_Security_Engineering/ ← Sécurité Offensive & Malware Dev
```

Chaque dossier d'exercice contient :
- **README.md** : Objectifs, concepts, instructions détaillées
- **main.py** : Code avec commentaires exhaustifs en français
- **exercice.txt** : Défis à essayer par vous-même
- **solution.txt** : Indices et solutions complètes
- **requirements.txt** : Dépendances spécifiques (si nécessaire)

## Progression Recommandée

### Phase 1 : Fondations Python (Semaines 1-3)
**Exercices 01-13** : Maîtriser les bases du langage
- Variables, types, opérateurs
- Structures de contrôle (if, loops)
- Structures de données (lists, dicts)
- Fonctions, modules, classes
- Gestion de fichiers et exceptions

### Phase 2 : Networking et Système (Semaine 4)
**Exercices 14-16** : Comprendre les interactions système
- Programmation socket (TCP/IP)
- Multi-threading et parallélisme
- Exécution de commandes système

### Phase 3 : Red Team Tools (Semaines 5-8)
**Exercices 17-25** : Développement d'outils offensifs
- Scanning et reconnaissance
- Post-exploitation
- Persistance et évasion

### Phase 4 : Malware Development & CS Fundamentals (Nouveau)
**Modules Avancés** : Application des concepts CS à la sécurité offensive
- **Trees & Graphs** : Ransomware logic, Process evasion, Lateral movement
- **Bit Manipulation** : Obfuscation, Shellcode encoding, API Hashing
- **Algorithms** : Evasion heuristique, Optimisation d'attaques

Voir [PROGRESSION.md](PROGRESSION.md) pour le plan détaillé.

## Utilisation

### Démarrer un exercice

```bash
cd exercices/01_hello_print
cat README.md              # Lire les instructions
python main.py             # Exécuter le code d'exemple
cat exercice.txt           # Voir les défis
```

### Ordre recommandé

Suivez l'ordre numérique : 01 → 02 → 03 → ... → 25

Chaque exercice s'appuie sur les concepts précédents.

### Conseils d'apprentissage

1. **Ne pas sauter d'étapes** : Même si vous connaissez déjà certains concepts
2. **Expérimenter** : Modifier le code, casser les choses, comprendre pourquoi
3. **Faire les exercices** : La lecture ne suffit pas, il faut pratiquer
4. **Lire les solutions** : Seulement après avoir essayé sérieusement
5. **Prendre des notes** : Documenter ce que vous apprenez

## Environnement de Test Recommandé

Pour les exercices avancés (17-25), utilisez un environnement isolé :

### Option 1 : Machines Virtuelles
```
VM Attaquant (Kali Linux)
    ↓
VM Cible (Ubuntu/Windows)
```

### Option 2 : Docker Containers
```bash
docker run -it ubuntu:latest bash
```

### Option 3 : Cloud Lab
- TryHackMe
- HackTheBox
- PentesterLab

**Ne jamais tester sur des machines en production ou sans autorisation.**

## Ressources Complémentaires

### Documentation Officielle
- [Python.org Documentation](https://docs.python.org/3/)
- [PEP 8 Style Guide](https://peps.python.org/pep-0008/)

### Cybersécurité
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [MITRE ATT&CK Framework](https://attack.mitre.org/)

### Pratique
- [TryHackMe](https://tryhackme.com/)
- [HackTheBox](https://www.hackthebox.com/)
- [OverTheWire](https://overthewire.org/)

## Troubleshooting

### Problème : Module non trouvé

```bash
# Vérifier que l'environnement virtuel est activé
which python
# Doit pointer vers venv/bin/python

# Réinstaller les dépendances
pip install -r requirements.txt
```

### Problème : Permission denied (Linux/macOS)

```bash
# Pour les exercices nécessitant des privilèges
sudo python main.py
# OU installer les capabilities
sudo setcap cap_net_raw=eip $(which python3)
```

### Problème : Scapy ne fonctionne pas (Windows)

```bash
# Installer Npcap
# https://npcap.com/#download
```

## Contribution

Ce projet est à des fins pédagogiques. Si vous trouvez des erreurs ou souhaitez améliorer le contenu :

1. Identifiez le problème clairement
2. Proposez une solution
3. Testez votre modification
4. Documentez le changement

## Licence

Ce matériel pédagogique est fourni à des fins éducatives uniquement.

**L'auteur décline toute responsabilité pour l'utilisation abusive de ce contenu.**

## Contact et Support

Pour des questions ou du support :
- Ouvrir une issue sur le dépôt
- Consulter la documentation Python officielle
- Rejoindre des communautés de cybersécurité éthique

---

**Bon apprentissage et restez éthique !**
