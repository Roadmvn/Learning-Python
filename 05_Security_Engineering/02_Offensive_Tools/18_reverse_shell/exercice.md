================================================================================
# Exercice 18: REVERSE SHELL EN PYTHON
================================================================================

AVERTISSEMENT ÉTHIQUE CRITIQUE:
===============================
Ces exercices couvrent des techniques de cybersécurité offensives.

INTERDIT:
- Utiliser sur des systèmes sans autorisation ÉCRITE
- Tester sur des réseaux d'autres personnes
- Accès non autorisé, vol de données, sabotage
- Cela constitue un CRIME avec poursuites pénales

AUTORISÉ:
- Red teaming avec contrat signé
- Tests de pénétration avec ROE (Rules of Engagement)
- Environnements sandbox/VM pour apprentissage
- Recherche en sécurité autorisée

================================================================================
DÉFIS PROGRESSIFS - REVERSE SHELL
================================================================================

## Défi 1: Reverse Shell Basique (Fondations)
============================================
Objectifs:
- Comprendre la communication socket bidirectionnelle
- Implémenter un handler (serveur d'écoute) simple
- Implémenter un payload (client) simple
- Exécuter des commandes de base

Tâches:
1. Créer une classe ReverseShellBasic avec:
   - Handler: Écoute sur localhost:5000
   - Payload: Se connecte à localhost:5000
   - Communication bidirectionnelle simple

2. Le handler doit:
   - Écouter sur 0.0.0.0:5000
   - Accepter une connexion
   - Permettre l'envoi de commandes via input()
   - Recevoir et afficher les résultats

3. Le payload doit:
   - Se connecter au handler
   - Recevoir des commandes
   - Exécuter via subprocess
   - Renvoyer l'output

4. Tester avec des commandes simples:
   - whoami
   - pwd (ou cd sur Windows)
   - ls / dir
   - date / time

Questions d'apprentissage:
- Comment fonctionnent les sockets TCP?
- Quelle est la différence server/client?
- Pourquoi c'est une "reverse" shell?
- Quels sont les problèmes de sécurité?

Indice: Voir main.py - ReverseShellHandler et ReverseShellPayload

## Défi 2: Gestion des Erreurs et Robustesse
=============================================
Objectifs:
- Améliorer la gestion d'erreurs
- Gérer les connexions interrompues
- Implémenter les timeouts

Tâches:
1. Ajouter gestion d'erreurs complète:
   - Erreurs de connexion
   - Erreurs lors de l'exécution
   - Erreurs d'encodage/décodage

2. Implémenter timeouts:
   - Timeout pour accept() si aucune connexion en 30s
   - Timeout pour recv() si aucune donnée en 10s
   - Timeout pour commandes (30s max d'exécution)

3. Ajouter messages informatifs:
   - État de la connexion
   - Messages d'erreur clairs
   - Logs des actions importantes

4. Tester les scénarios d'erreur:
   - Tuer le payload et relancer
   - Tuer le handler pendant l'exécution
   - Envoyer une commande qui ne existe pas
   - Commande qui prend plus de 30s

Code starter:
```python
try:
```python
    # Votre code
except socket.error as e:
    print(f"Erreur socket: {e}")
except subprocess.TimeoutExpired:
    print("Commande timeout")
except Exception as e:
    print(f"Erreur générale: {e}")
```
```

## Défi 3: Authentification Simple
==================================
Objectifs:
- Ajouter une couche d'authentification
- Empêcher l'accès non autorisé au payload

Tâches:
1. Implémenter un système d'authentification simple:
   - Hash d'un mot de passe (utiliser hashlib.sha256)
   - Vérification lors de la connexion

2. Le payload doit:
   - Attendre l'authentification avant de réagir
   - Refuser les commandes si non authentifié
   - Déconnecter après 3 tentatives échouées

3. Le handler doit:
   - Demander le mot de passe à la connexion
   - Envoyer le hash du mot de passe
   - Afficher erreur si rejet

4. Tester:
   - Connexion avec bon mot de passe → succès
   - Connexion avec mauvais mot de passe → rejet
   - Tentative 3x mauvais password → déconnexion

Code starter:
```python
```python
import hashlib

```
# Hash du mot de passe
password = "admin123"
password_hash = hashlib.sha256(password.encode()).hexdigest()
```

Questions:
- Pourquoi utiliser un hash au lieu du mot de passe brut?
- Comment améliorer cela (salts, PBKDF2)?

## Défi 4: Persistance avec Reconnexion Automatique
===================================================
Objectifs:
- Implémenter une reconnexion automatique
- Maintenir la persistence du payload

Tâches:
1. Modifier le payload pour:
   - Essayer de reconnecter automatiquement si la connexion est perdue
   - Utiliser un backoff exponentiel (1s, 2s, 4s, 8s... max 60s)
   - Logs des tentatives de reconnexion

2. Le handler ne change pas, mais doit:
   - Pouvoir accepter plusieurs connexions (refaire serverSocket.listen/accept)

3. Tester le scénario:
   - Lancer le payload
   - Lancer le handler et exécuter une commande
   - Arrêter le handler
   - Observer reconnexion du payload
   - Relancer le handler
   - Vérifier que la reconnexion fonctionne

4. Ajouter un compteur de reconnexions

Exemple backoff:
```python
tentative = 0
```python
while True:
    try:
        socket.connect(...)
        break
    except:
        delai = min(2 ** tentative, 60)  # Backoff expo max 60s
        tentative += 1
        time.sleep(delai)
```
```

Questions:
- Pourquoi le backoff exponentiel?
- Comment détecter que le handler a redémarré?
- Quels risques cette persistance crée-t-elle?

## Défi 5: Encodage / Obfuscation Basique
=========================================
Objectifs:
- Implémenter une obfuscation basique
- Contourner les filtres simples

Tâches:
1. Ajouter encodage Base64:
   - Encoder toutes les commandes en Base64
   - Décoder les commandes reçues
   - Encoder les résultats avant envoi

2. Le handler doit:
   - Encoder les commandes en Base64
   - Décoder les résultats reçus

3. Le payload doit:
   - Décoder les commandes reçues (Base64)
   - Encoder les résultats avant envoi

4. Tester:
   - Exécuter les commandes normales
   - Vérifier que le trafic est encodé

5. Ajouter un mode ROT13 en alternative (optionnel)

Code starter:
```python
```python
import base64

```
# Encoder
message_encode = base64.b64encode(message.encode()).decode()

# Décoder
message_decode = base64.b64decode(message_encode).decode()
```

Questions:
- Est-ce que Base64 est du chiffrement? Pourquoi?
- Quels autres encodages existe-t-il?
- Comment faire du vrai chiffrement (AES)?
- Pourquoi l'obfuscation seule n'est pas suffisante?

## Défi 6: Exécution de Commandes Avancées
===========================================
Objectifs:
- Gérer les commandes complexes et interactives
- Gérer les pipes, redirections, etc.

Tâches:
1. Permettre l'exécution de commandes complexes:
   - Pipes: "ls | grep txt"
   - Redirections: "cat > fichier.txt"
   - Commandes composées: "cd /tmp && ls"
   - Variables d'environnement: "echo $HOME" ou "%USERPROFILE%"

2. Tester:
   ```
   whoami
   ls | head -5
   echo "test" > /tmp/test.txt && cat /tmp/test.txt
   pwd
   echo $HOME
   ```

3. Gérer les cas spéciaux:
   - Commandes qui demandent input (y/n) → timeout
   - Commandes longues (plus de 30s) → timeout + kill
   - Commandes qui changent de répertoire → garder le state

4. Implémenter un changement de répertoire persistant:
   - Garder track du `cwd` (current working directory)
   - Utiliser `cwd` dans chaque subprocess.Popen()
   - Permettre "cd" pour changer de répertoire

Code starter:
```python
```python
import os

```
current_dir = os.getcwd()

# Vérifier si commande est "cd"
```python
if commande.startswith("cd "):
    nouveau_dir = commande[3:].strip()
    try:
        os.chdir(nouveau_dir)
        current_dir = os.getcwd()
        return f"Répertoire courant: {current_dir}\n"
    except Exception as e:
        return f"Erreur: {e}\n"
```
```

Questions:
- Pourquoi les redirections marchent avec shell=True?
- Quel est le danger de shell=True?
- Comment implémenter cd sans shell=True?

## Défi 7: Obfuscation Avancée et Anti-Analyse
==============================================
Objectifs:
- Implémenter des techniques d'obfuscation avancées
- Contourner les détections basiques

Tâches:
1. Ajouter chiffrement AES (utiliser cryptography):
   ```bash
   pip install cryptography
   ```
   - Générer une clé partagée
   - Chiffrer/déchiffrer les communications
   - Utiliser un IV aléatoire

2. Ajouter anti-détection simples:
   - Déterminer le système (Windows vs Linux)
   - Adapter les commandes au système
   - Utiliser des noms de variables génériques ("data", "c", etc.)

3. Ajouter des délais aléatoires:
   - Ajouter des délais random entre 0.1s et 0.5s
   - Échapper les patterns de détection IDS

4. Ajouter une vérification de sandbox:
   - Vérifier si exécuté dans une VM
   - Vérifier certains processus de debug
   - Quitter silencieusement si détecté

Code starter:
```python
```python
from cryptography.fernet import Fernet
import random
import time

```
# Chiffrement
key = Fernet.generate_key()
cipher = Fernet(key)

# Utiliser
encrypted = cipher.encrypt(data.encode())
decrypted = cipher.decrypt(encrypted).decode()

# Délai random
time.sleep(random.uniform(0.1, 0.5))
```

Questions:
- Comment détecter si on est dans une VM?
- Pourquoi les délais aléatoires aident?
- Comment implémenter vrai anti-analysis?

## Défi 8: Rapport Complet et Démonstration
===========================================
Objectifs:
- Intégrer toutes les améliorations précédentes
- Créer une reverse shell complète et documentée
- Démontrer la connaissance maîtrisée

Tâches:
1. Créer une classe ReverseShellComplete qui intègre:
   - Authentification (défi 3)
   - Persistance (défi 4)
   - Obfuscation Base64 (défi 5)
   - Commandes avancées + cd (défi 6)

2. Écrire un rapport (rapport_18.txt) contenant:
   - Architecture générale
   - Diagramme ASCII du flux de données
   - Explication de chaque composant
   - Points de sécurité clés
   - Défenses contre les reverse shells
   - Améliorations possibles

3. Créer un script de démonstration:
   - Démarrer handler
   - Démarrer payload (dans un thread)
   - Exécuter une série de commandes
   - Afficher logs complets

4. Ajouter des commentaires exhaustifs en français

5. Tests à exécuter:
   - Démonstration basique
   - Vérifier authentication
   - Vérifier persistance (couper connexion, reconnecter)
   - Vérifier obfuscation (captures réseau encodées)
   - Vérifier exécution de commandes complexes

Fichiers attendus:
- reverse_shell_complete.py (votre implémentation)
- rapport_18.txt (documentation)
- test_script.py (tests)

================================================================================
## Conseils PRATIQUES
================================================================================

1. SÉCURITÉ D'ABORD:
   - Toujours étudier en environnement sandbox (VM, Docker)
   - JAMAIS tester sur des systèmes "réels"
   - Comprendre les implications légales

2. DÉBOGAGE:
   - Utilisez print() pour logger les opérations
   - Testez handler et payload séparément d'abord
   - Utilisez un terminal pour chaque composant

3. TESTEZ:
   ```bash
   # Terminal 1 - Handler
   python3 main.py handler

   # Terminal 2 - Payload
   python3 main.py payload localhost 4444
   ```

4. COMPRENEZ:
   - Lisez le code existant (main.py)
   - Testez chaque partie isolément
   - Documentez votre apprentissage

================================================================================
RESSOURCES ET LIENS PÉDAGOGIQUES
================================================================================

Concepts réseaux:
- Sockets TCP/IP
- Protocoles de communication
- Modèle OSI

Cybersécurité:
- Reverse shells et leur fonctionnement
- Red teaming vs défense
- Techniques d'attaque

Python:
- Module socket
- subprocess et exécution de commandes
- Threading et multiprocessing
- Encodage/chiffrement

Documentation officielle:
- Python socket: https://docs.python.org/3/library/socket.html
- subprocess: https://docs.python.org/3/library/subprocess.html
- cryptography: https://cryptography.io/

================================================================================
RUBRIQUE D'ÉVALUATION
================================================================================

Chaque défi est évalué sur:

1. Fonctionnalité (50%):
   - Code exécute sans erreurs
   - Toutes les tâches réalisées
   - Tests réussissent

2. Code Quality (25%):
   - Code lisible et bien structuré
   - Commentaires exhaustifs en français
   - Gestion d'erreurs appropriée
   - Nommage de variables explicite

3. Sécurité (15%):
   - Comprendre les risques
   - Implémenter les protections correctes
   - Documenter les limitations

4. Documentation (10%):
   - Explications claires
   - Exemples d'utilisation
   - Architecture bien documentée

================================================================================
IMPORTANT: RESPONSABILITÉ ÉTHIQUE
================================================================================

En complétant ces exercices, vous acceptez que:
- Ces techniques sont puissantes et dangereuses
- L'usage non autorisé est CRIMINEL
- Vous comprenez les implications légales
- Vous n'utiliserez ces compétences que de manière éthique et légale

Technologie n'est neutre que dans l'usage qu'on en fait.

================================================================================
