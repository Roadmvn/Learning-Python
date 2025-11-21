========================================
# Exercice 16: SUBPROCESS EN PYTHON
Défis progressifs avec focus cybersécurité
========================================

AVERTISSEMENT LÉGAL ET ÉTHIQUE:
Ces exercices sont destinés à l'apprentissage dans un environnement contrôlé et autorisé.
L'utilisation sur des systèmes sans autorisation explicite est ILLÉGALE.

Utilisez uniquement sur:
- Votre propre système
- Des machines virtuelles de test
- Des environnements autorisés
- Des systèmes pour lesquels vous avez une autorisation écrite

========================================
## Défi 1: Exécution de Commandes Basiques
========================================

Objectif : Maîtriser subprocess.run() et la capture de sortie

Créez un script qui :
- Définit une fonction execute_command(cmd) qui :
  * Utilise subprocess.run() avec shell=False
  * Capture stdout et stderr séparément
  * Retourne un dictionnaire avec 'success', 'output', 'error', 'returncode'
- Teste la fonction avec:
  * Un succès: ['echo', 'Hello']
  * Une erreur: ['ls', '/nonexistent']
  * Une commande inexistante

Contraintes :
- Gérer les exceptions (FileNotFoundError, CalledProcessError)
- Utiliser capture_output=True et text=True
- N'utiliser JAMAIS shell=True
- Afficher les résultats formatés

Indications :
- subprocess.run()
- capture_output=True
- text=True
- try/except pour FileNotFoundError

Exemple de sortie attendue :
Exécution: echo Hello
Succès: True
Sortie: Hello
Code retour: 0

Exécution: ls /nonexistent
Succès: False
Erreur: ls: cannot access '/nonexistent': No such file or directory
Code retour: 1

========================================
## Défi 2: Reconnaissance Système
========================================

Objectif : Créer un script d'énumération système multi-plateforme

Créez une fonction system_recon() qui collecte:

1. Informations système:
   - Nom du système (uname -s ou systeminfo)
   - Version complète (uname -a)
   - Hostname (hostname)

2. Informations utilisateur:
   - Utilisateur courant (whoami)
   - ID et groupes (id sur Unix, whoami /groups sur Windows)
   - Répertoire home (echo $HOME ou USERPROFILE)

3. Informations réseau:
   - Interfaces réseau (ifconfig/ipconfig)
   - Adresses IP
   - Table de routage

4. Détection multi-plateforme (sys.platform)

Contraintes :
- Fonctionner sur Linux, macOS, Windows
- Gérer les commandes non disponibles
- Implementer des timeouts (max 2s par commande)
- Capturer stdout et stderr

Indications :
- sys.platform ('linux', 'darwin', 'win32')
- Commandes différentes selon l'OS
- subprocess.run() avec capture_output=True
- Gestion des exceptions pour commandes manquantes
- Format de sortie organisé

Exemple de sortie attendue :
=== RECONNAISSANCE SYSTÈME ===

[*] Système d'exploitation
Système: Linux
Hostname: kali
Version: Linux kali 5.10.0

[*] Utilisateur
Utilisateur: kali
UID/GID: uid=1000(kali) gid=1000(kali)

[*] Réseau
Interfaces: eth0, lo
Routes: 3 routes configurées

========================================
## Défi 3: Injection de Commandes (Protection)
========================================

Objectif : Démontrer les risques d'injection et implémenter les protections

Créez deux fonctions:

1. vulnerable_ping(hostname: str):
   - Code VULNÉRABLE: subprocess.run(f"ping {hostname}", shell=True)
   - Montrer comment une entrée "google.com; cat /etc/passwd"
```python
     exécuterait deux commandes

```
2. secure_ping(hostname: str):
   - Utiliser shell=False avec liste d'arguments
   - Valider le hostname avec regex (alphanumériques, point, tiret)
   - Implementer un timeout

3. Test:
   - Créer une entrée malveillante: "google.com; whoami"
   - Afficher ce qui se passerait avec vulnerable_ping()
   - Afficher comment secure_ping() la traite

Contraintes :
- Créer une fonction validate_hostname(hostname) avec regex
- Utiliser shell=False obligatoirement dans secure_ping()
- Timeout maximum 3 secondes
- Afficher des explications claires des risques

Indications :
- re.match() pour validation
- subprocess.run() avec shell=False
- shlex.quote() pour alternative avec shell=True
- Démonstration sans exécuter réellement les injections

Exemple de sortie attendue :
=== INJECTION DE COMMANDES ===

Entrée malveillante: google.com; whoami

Avec shell=True (VULNÉRABLE):
Exécuterait:
  1. ping google.com
  2. whoami
RÉSULTAT: Exécution de commandes arbitraires!

Avec shell=False (SÛRE):
Traite comme simple argument: "google.com; whoami"
Tentative ping vers "google.com; whoami"
RÉSULTAT: Sûr, pas d'injection possible

========================================
## Défi 4: Énumération de Ports (avec Timeouts)
========================================

Objectif : Scanner des ports avec gestion des timeouts

Créez un script qui :
- Définit une fonction check_port(host, port, timeout=1) qui:
  * Utilise netcat (nc), nmap, ou telnet selon disponibilité
  * Retourne True si le port est ouvert
  * Retourne False si fermé ou timeout
  * Gère subprocess.TimeoutExpired

- Scanne une liste de ports communs (22, 80, 443, 8080, 3306, 5432)
  * Sur localhost (127.0.0.1)
  * Avec timeout de 1 seconde
  * Affiche ports ouverts/fermés

- Implémenter une version avec netcat (plus simple):
  * subprocess.run(['nc', '-zv', host, port], timeout=1)
  * Alternative: telnet sur port donné

Contraintes :
- Timeout impératif pour chaque vérification
- Gérer subprocess.TimeoutExpired
- Afficher progression et résultats
- Utiliser shell=False

Indications :
- nc -zv host port (netcat) ou equiv
- timeout=1 pour subprocess.run()
- try/except subprocess.TimeoutExpired
- Ports à tester: 22, 80, 443, 8080, 3306, 5432

Exemple de sortie attendue :
Scanner de ports de 127.0.0.1
=================================
Port 22   : Fermé
Port 80   : Fermé
Port 443  : Fermé
Port 8080 : Fermé
Port 3306 : Fermé
Port 5432 : Fermé

Résultats: 0 port(s) ouvert(s)

========================================
## Défi 5: Capture d'Output Avancée (Parsing)
========================================

Objectif : Capturer et parser la sortie de commandes complexes

Créez un script qui :
- Lance la commande: ps aux (ou tasklist sur Windows)
- Capture la sortie complète
- Parse les lignes pour extraire:
  * Nombre total de processus
  * Processus Python actifs
  * Processus occupant le plus de mémoire
  * Processus occupant le plus de CPU

- Affiche des statistiques formatées

Contraintes :
- Utiliser subprocess.run() avec capture_output=True
- Parser le texte avec split() et list comprehension
- Gérer multi-plateforme (ps aux sur Unix, tasklist sur Windows)
- Gestion des erreurs si commande manquante

Indications :
- subprocess.run(['ps', 'aux'], capture_output=True, text=True)
- result.stdout.split('\n')
- Parsing des colonnes par index
- Conversion int() pour mémoire/CPU

Exemple de sortie attendue :
=== ANALYSE PROCESSUS ===

Total processus: 125
Processus Python: 3
  - /usr/bin/python3 (PID 2341)
  - /usr/bin/python3 (PID 3442)

Plus haute consommation mémoire:
  chrome (1250 MB)

Plus haute consommation CPU:
  python3 (15%)

========================================
## Défi 6: Gestion des Signaux et Termination
========================================

Objectif : Maîtriser terminate() et kill() pour les processus longs

Créez un script qui :
- Définit une fonction run_with_timeout(cmd, timeout) qui:
  * Lance un processus avec subprocess.Popen()
  * Attendre avec wait(timeout=...)
  * Si timeout, essayer terminate() (SIGTERM)
  * Si toujours actif après 1s, appliquer kill() (SIGKILL)
  * Retourner le code de sortie final

- Teste avec:
  * Une commande rapide: ['echo', 'test']
  * Une commande moyenne: ['sleep', '2'] avec timeout=5
  * Une commande lente: ['sleep', '10'] avec timeout=1
```python
    (doit être kilée)

```
Contraintes :
- Pattern: wait -> timeout -> terminate -> wait -> timeout -> kill
- Implementer au moins 3 cas de test
- Afficher le résultat et le signal qui a terminé le processus
- Gestion complète des exceptions

Indications :
- subprocess.Popen()
- process.wait(timeout=X)
- process.terminate() (SIGTERM)
- process.kill() (SIGKILL)
- try/except subprocess.TimeoutExpired

Exemple de sortie attendue :
Test 1: echo test (timeout=5)
Terminé naturellement
Code de sortie: 0

Test 2: sleep 2 (timeout=5)
Terminé naturellement après 2s
Code de sortie: 0

Test 3: sleep 10 (timeout=1)
Timeout après 1s
SIGTERM envoyé
Timeout de SIGTERM
SIGKILL envoyé
Processus tué
Code de sortie: -9

========================================
## Défi 7: Redirection et Pipes
========================================

Objectif : Manipuler stdin, stdout, stderr et pipes

Créez un script qui :
1. Démontre subprocess.PIPE:
   - Redirection de stdout: ['echo', 'test'] -> capture
   - Redirection de stderr: erreur -> capture
   - Combinaison stderr+stdout: ['ls', '/nonexist'] -> mélangées

2. Communication bidirectionnelle (stdin/stdout):
   - Lance 'cat' qui lit stdin
   - Envoie du texte en input
   - Récupère la sortie avec communicate()

3. Chaînage de commandes:
   - Alternative au pipe shell ("|")
   - Utiliser stdout d'une commande comme stdin de la suivante

4. Suppression de sortie:
   - Utiliser subprocess.DEVNULL
   - Exécuter sans afficher/capturer la sortie

Contraintes :
- Pas de shell=True
- Utiliser PIPE ou DEVNULL
- Illustrer avec des exemples concrets
- Afficher les résultats de chaque étape

Indications :
- subprocess.PIPE pour capture/direction
- subprocess.STDOUT pour combiner stderr
- subprocess.DEVNULL pour suppression
- process.communicate(input=...) pour stdin
- process.stdout/process.stderr pour accès direct

Exemple de sortie attendue :
=== REDIRECTION ET PIPES ===

1. Capture stdout:
Input: echo "Hello World"
Output: "Hello World"

2. Capture stderr:
Input: ls /nonexistent
Error output: ls: cannot access '/nonexistent'...

3. Communication stdin/stdout:
Envoyé: "Ligne 1\nLigne 2"
Reçu: "Ligne 1\nLigne 2"

4. Suppression DEVNULL:
echo "ceci n'est pas affiché" -> sortie supprimée

========================================
## Défi 8: Automatisation Red Teaming (Challenge Final)
========================================

Objectif : Créer un tool d'énumération complet et sécurisé

Créez un script d'énumération automatisé qui combine tous les concepts:

1. Enumeration Système Complète:
   - Récupérer: OS, utilisateur, hostname, IP, processus
   - Utiliser les fonctions des défis précédents
   - Afficher dans un rapport structuré

2. Sécurité Maximale:
   - JAMAIS shell=True
   - TOUS les inputs validés/échappés (shlex.quote())
   - Timeouts pour CHAQUE commande
   - Gestion d'erreurs complète

3. Rapports:
   - Générer un rapport texte structuré
   - Ajouter timestamps
   - Inclure les erreurs/limitations
   - Format lisible et professional

4. Commandes à inclure:
   - whoami, id, uname -a, hostname, pwd
   - ifconfig ou ipconfig
   - ps aux (top processus)
   - Vérification de ports courants
   - Informations DNS (si disponible)

5. Structure du code:
   - Classe Enumerator avec méthodes pour chaque catégorie
   - Méthode run_command() centralisée (avec timeout/sécurité)
   - Méthode generate_report() pour affichage
   - Main qui orchestre l'énumération

Contraintes CRITIQUES:
- Sécurité: shell=False partout
- Timeout: maximum 2 secondes par commande
- Erreurs: capture et rapport sans crash
- Multi-plateforme: détecter l'OS
- Logging: afficher ce qui se passe
- Code: commentaires en français, fonctions claires

Indications :
- Créer une classe Enumerator
- Méthode privée _run_safe_command(cmd, timeout)
- Dictionnaire de commandes par OS
- Exception handling complet
- Format rapport ASCII lisible

Exemple de sortie attendue :
========================================
RAPPORT D'ÉNUMÉRATION
Généré: 2024-11-07 14:30:45
Système cible: 127.0.0.1
========================================

[*] INFORMATIONS SYSTÈME
Système: Linux
Hostname: kali-machine
Architecture: x86_64
Noyau: 5.10.0-kali9-amd64
Uptime: 5 jours 3 heures

[*] UTILISATEUR COURANT
Utilisateur: kali
UID: 1000
Groupes: kali, sudo, docker
Répertoire: /home/kali
Permissions sudo: Yes

[*] RÉSEAU
Interface eth0: 192.168.1.100
Gateway: 192.168.1.1
DNS: 8.8.8.8, 8.8.4.4

[*] PROCESSUS PRINCIPAUX
Total processus: 125
Python processes: 3
Top CPU: chrome (15%)
Top Memory: firefox (1250 MB)

[*] PORTS OUVERTS
Port 22: SSH
Port 80: HTTP
Port 8080: HTTP-ALT

[*] NOTES DE SÉCURITÉ
- Aucune vulnérabilité évidente détectée
- Système à jour
- Recommandation: vérifier les services inutiles

========================================

========================================
BARÈME DE NOTATION
========================================

Défi 1 (Basiques):       10 points
Défi 2 (Reconnaissance): 15 points
Défi 3 (Sécurité):       15 points
Défi 4 (Timeouts):       15 points
Défi 5 (Parsing):        15 points
Défi 6 (Signaux):        15 points
Défi 7 (Redirection):    15 points
Défi 8 (Challenge):      20 points

Total: 120 points

Bonus:
- Code modulaire et réutilisable: +10
- Documentation complète: +5
- Gestion d'erreurs robuste: +5
- Performance optimisée: +5

Maximum: 145 points
