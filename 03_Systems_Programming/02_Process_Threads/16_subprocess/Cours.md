# Exercice 16 : Subprocess en Python

## Objectifs d'Apprentissage

- Comprendre le module `subprocess` pour exécuter des programmes externes
- Maîtriser les différentes méthodes d'exécution de commandes
- Utiliser `subprocess.run()` pour les cas simples
- Utiliser `subprocess.Popen()` pour plus de contrôle
- Capturer la sortie standard et d'erreur
- Comprendre les risques de sécurité avec `shell=True`
- Protéger contre les injections de commandes (command injection)
- Gérer les timeouts et les signaux
- Appliquer subprocess aux tâches de cybersécurité

## Concepts Clés

### Module subprocess

Le module `subprocess` permet d'exécuter des programmes externes et de communiquer avec eux.

```
Programme Python
├── subprocess.run() → Exécution simple et synchrone
├── subprocess.Popen() → Exécution avancée avec plus de contrôle
├── subprocess.check_output() → Obtenir la sortie directement
├── subprocess.check_call() → Exécuter et vérifier le code de retour
└── subprocess.call() → Exécuter et récupérer le code de retour
```

**Avantages** :
- Exécution de commandes système
- Communication avec des programmes externes
- Capture de sortie/erreur
- Gestion des processus enfants

**Cas d'usage en cybersécurité** :
- Exécution de commandes système sécurisées
- Utilisation d'outils externes (nmap, ffuf, sqlmap)
- Énumération de systèmes
- Collecte d'informations de sécurité
- Automatisation de tests de pénétration

### subprocess.run()

La fonction `run()` est la méthode recommandée pour les cas simples.

```python
import subprocess

# Cas basique
result = subprocess.run(['ls', '-la'], capture_output=True)
print(result.returncode)  # Code de sortie
print(result.stdout)      # Sortie standard
print(result.stderr)      # Erreur standard

# Avec timeout
subprocess.run(['sleep', '10'], timeout=5)  # Lève TimeoutExpired après 5s
```

**Paramètres principaux** :
- `args` : Liste des arguments (pas de shell)
- `capture_output` : Capture stdout et stderr
- `text` : Renvoie strings au lieu de bytes
- `timeout` : Délai maximum d'exécution
- `cwd` : Répertoire de travail
- `env` : Variables d'environnement
- `shell` : Utiliser le shell (DANGEREUX!)

### subprocess.Popen()

`Popen` offre plus de contrôle pour les cas complexes.

```python
import subprocess

# Exécution avec plus de contrôle
process = subprocess.Popen(
    ['ls', '-la'],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

# Communiquer avec le processus
stdout, stderr = process.communicate()
return_code = process.returncode
```

**Flux de contrôle** :
```
Popen() → [Process en cours]
           ├── communicate() → Attendre + capturer
           ├── wait() → Attendre la fin
           ├── poll() → Vérifier l'état (non-bloquant)
           ├── send_signal() → Envoyer un signal
           ├── terminate() → Terminer gracieux
           └── kill() → Terminer forcé
```

**Attributs importants** :
- `pid` : Identifiant du processus
- `returncode` : Code de sortie (None si actif)
- `stdin` : Descripteur d'entrée
- `stdout` : Descripteur de sortie
- `stderr` : Descripteur d'erreur

### Capture de sortie

**Méthode 1 : capture_output (Python 3.7+)** :
```python
result = subprocess.run(['whoami'], capture_output=True, text=True)
print(result.stdout)
print(result.stderr)
```

**Méthode 2 : PIPE classique** :
```python
process = subprocess.Popen(
    ['whoami'],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)
stdout, stderr = process.communicate()
print(stdout)
```

**Différence STDOUT vs STDERR** :
```
Commande normale :  Output → STDOUT
Commande erreur :   Error → STDERR
Redirect shell :    2>&1 mixe stdout et stderr
```

### shell=True vs shell=False - ATTENTION SÉCURITÉ!

**shell=False (RECOMMANDÉ)** :
```python
# SÛRE - Arguments séparés
subprocess.run(['ls', '-la', '/home'])

# La commande est exécutée directement, pas d'interprétation shell
```

**shell=True (DANGEREUX!)** :
```python
# RISQUE DE SÉCURITÉ - Injection de commande possible!
user_input = "test; rm -rf /"  # Entrée malveillante
subprocess.run(f"ls {user_input}", shell=True)
# Exécute: ls test; rm -rf /
# CATASTROPHIQUE!
```

### Command Injection - Attaques Courantes

**Scénario 1 : Injection via paramètre** :
```python
# VULNERABLE CODE
hostname = input("Entrez un hostname: ")
subprocess.run(f"ping -c 1 {hostname}", shell=True)

# Attaquant entre: "google.com; cat /etc/passwd"
# Résultat: ping -c 1 google.com; cat /etc/passwd
```

**Scénario 2 : Injection via variable d'environnement** :
```python
# VULNERABLE CODE
username = os.environ.get('USER', '')
subprocess.run(f"echo {username}", shell=True)

# Attaquant set USER="test; whoami"
# Résultat: echo test; whoami
```

**Protection : Utiliser des listes au lieu de strings** :
```python
# SÛRE
hostname = input("Entrez un hostname: ")
subprocess.run(['ping', '-c', '1', hostname])  # Arguments séparés
# L'entrée "google.com; cat /etc/passwd" ne sera pas interprétée
```

### Gestion des Timeouts

```python
import subprocess

try:
    # Exécution avec timeout de 5 secondes
    result = subprocess.run(['sleep', '10'], timeout=5)
except subprocess.TimeoutExpired:
    print("La commande a dépassé le timeout")
```

**Terminer un processus qui timeout** :
```python
try:
    result = subprocess.run(['sleep', '100'], timeout=5)
except subprocess.TimeoutExpired as e:
    # Tuer le processus
    e.kill()  # Python 3.7+
```

### Gestion des Signaux et Termination

```python
import subprocess
import signal

process = subprocess.Popen(['sleep', '100'])

# Arrêt gracieux (SIGTERM)
process.terminate()

# Attendre avec timeout
try:
    process.wait(timeout=5)
except subprocess.TimeoutExpired:
    # Forcer l'arrêt (SIGKILL)
    process.kill()
    process.wait()
```

### Codes de Retour

```python
import subprocess

result = subprocess.run(['ls', '/nonexistent'])

if result.returncode == 0:
    print("Succès")
elif result.returncode == 1:
    print("Erreur générale")
elif result.returncode == 127:
    print("Commande non trouvée")
elif result.returncode == 124:
    print("Timeout (code UNIX)")
```

**Codes courants** :
- `0` : Succès
- `1` : Erreur générale
- `2` : Mauvaise utilisation
- `127` : Commande non trouvée
- `128 + N` : Tué par signal N
- `137` : Tué par SIGKILL (9)
- `143` : Tué par SIGTERM (15)

## Applications en Cybersécurité

### Exécution d'Outils de Scan

```
Automaton de Sécurité:
├── subprocess → nmap scan
├── subprocess → ffuf enumeration
├── subprocess → dirsearch
└── subprocess → gobuster
```

Automatisation d'outils de pentesting.

### Collecte d'Informations Système

```
Reconnaissance:
├── subprocess → whoami
├── subprocess → id
├── subprocess → uname
├── subprocess → hostname
└── subprocess → ifconfig
```

Information gathering sécurisée.

### Énumération de Services

```
Service Enumeration:
├── subprocess → nmap service detection
├── subprocess → curl version detection
├── subprocess → banner grabbing
└── subprocess → protocol detection
```

Identification de services cibles.

## Bonnes Pratiques de Sécurité

### 1. JAMAIS utiliser shell=True avec entrées utilisateur

```python
# VULNERABLE
user_input = input("Commande: ")
subprocess.run(user_input, shell=True)  # TRÈS DANGEREUX!

# SÛRE
command = input("Entrez un hostname: ")
subprocess.run(['ping', '-c', '1', command])  # Les arguments sont échappés
```

### 2. Valider et nettoyer les entrées

```python
import re
import subprocess

def validate_hostname(hostname):
    """Valider un hostname avant utilisation"""
    # Accepter uniquement alphanumériques, point, tiret
    if not re.match(r'^[a-zA-Z0-9.-]+$', hostname):
        raise ValueError(f"Hostname invalide: {hostname}")
    return hostname

hostname = validate_hostname(input("Hostname: "))
subprocess.run(['ping', '-c', '1', hostname])
```

### 3. Utiliser shlex pour échapper

```python
import shlex
import subprocess

# shlex.quote() échappe les caractères spéciaux
hostname = shlex.quote(input("Hostname: "))
command = f"ping -c 1 {hostname}"
subprocess.run(command, shell=True)  # Maintenant plus sûr (mais shell=False reste préférable)
```

### 4. Implémenter des timeouts

```python
import subprocess

try:
    result = subprocess.run(
        ['nmap', 'target.com'],
        timeout=300,  # 5 minutes max
        capture_output=True,
        text=True
    )
except subprocess.TimeoutExpired:
    print("Scan dépassé le timeout - arrêt")
```

### 5. Gérer les ressources

```python
import subprocess

# Vérifier les ressources disponibles avant d'exécuter
import psutil
if psutil.virtual_memory().available > 100 * 1024 * 1024:  # 100 MB libre
    subprocess.run(['heavy_operation'])
```

## Outils Utiles

### subprocess Module

- `subprocess.run()` : Interface recommandée
- `subprocess.Popen()` : Contrôle avancé
- `subprocess.check_output()` : Obtenir la sortie
- `subprocess.check_call()` : Vérifier le code de retour
- `subprocess.call()` : Récupérer le code de retour
- `subprocess.TimeoutExpired` : Exception timeout
- `subprocess.PIPE` : Redirection standard

### Modules Complémentaires

```python
import shlex          # Analyse et échappement de commandes
import signal         # Gestion des signaux
import os            # Variables d'environnement
import sys           # Arguments système
```

## Avertissements de Sécurité

### Risques Majeurs

1. **Command Injection** : L'attaque la plus dangereuse avec subprocess
   - Utiliser TOUJOURS des listes au lieu de strings
   - Ne JAMAIS faire confiance aux entrées utilisateur

2. **Shell Metacharacters** : Caractères interprétés par le shell
   - `;` : Exécution séquentielle
   - `|` : Pipe
   - `&&` `||` : Exécution conditionnelle
   - `>` `<` : Redirection
   - `$()` : Substitution de commande
   - `` ` `` : Backticks

3. **Dénégation de Service** : Utiliser des timeouts!
   - Processus bloqués indéfiniment
   - Consommation excessive de ressources
   - Déverrouillage de fichiers

4. **Exposition d'Informations** : Attention aux erreurs
   - Les messages d'erreur peuvent révéler des infos
   - Capturer et valider les sorties
   - Utiliser du logging approprié

### Utilisation Éthique

- Obtenir les autorisations avant tout scan
- Respecter les limite de rate-limiting
- Ne pas faire de DDoS même "accidentellement"
- Utiliser uniquement dans un cadre légal
- Documenter les activités de test
- Obtenir des contrats de pénétration avant tests

## Ressources

- Documentation Python subprocess : https://docs.python.org/3/library/subprocess.html
- CWE-78 : Improper Neutralization of Special Elements used in an OS Command
- OWASP Command Injection : https://owasp.org/www-community/attacks/Command_Injection
- PEP 8 : Style Guide for Python Code
- Real Python Subprocess Tutorial
