========================================
# Exercice 17: PORT SCANNER EN PYTHON
Défis progressifs avec focus red teaming
========================================

AVERTISSEMENT LÉGAL ET ÉTHIQUE:
========================================
Ces exercices sont destinés à l'apprentissage dans un environnement contrôlé et autorisé.

L'utilisation SANS autorisation écrite explicite est ILLÉGALE et peut entrainer:
- Poursuites judiciaires
- Amendes substantielles
- Emprisonnement
- Dommages-intérêts civils

Utilisez uniquement sur:
✓ Votre propre système/machine virtuelle
✓ Des systèmes avec contrat de pentesting signé
✓ Des environnements d'apprentissage contrôlés
✓ Des plateformes légales (HackTheBox, TryHackMe, OWASP)

JAMAIS sur:
✗ Systèmes publics sans permission
✗ Réseaux d'entreprises tierce
✗ Avec l'intention de nuire
✗ Pour reconnaissance préalable à une attaque

========================================
## Défi 1: Scanner Basique - Connexion TCP Simple
========================================

Objectif : Maîtriser socket.connect() et vérification d'état de port

Créez un script qui :
1. Définit une fonction check_port(host, port, timeout) qui:
   - Crée un socket TCP (socket.AF_INET, socket.SOCK_STREAM)
   - Utilise socket.connect_ex() pour tester la connexion
   - Retourne True si connecté (code 0), False sinon
   - Implémenter le timeout avec socket.settimeout()
   - Gérer les exceptions (socket.gaierror, socket.error)

2. Teste la fonction sur localhost (127.0.0.1):
   - Ports courants: 22, 80, 443, 3306, 5432, 8080, 9000
   - Timeout de 1 seconde
   - Affiche pour chaque port: "Port 22: OPEN" ou "Port 22: CLOSED"

3. Résultats attendus sur localhost:
   - Tous fermés (normal si pas de serveurs actifs)

Contraintes:
- Utiliser socket.connect_ex() (retourne 0 si succès)
- Ne JAMAIS laisser un socket ouvert sans le fermer
- Timeout obligatoire pour éviter blocages
- Gestion d'exception pour hosts invalides

Indications:
- socket.socket(socket.AF_INET, socket.SOCK_STREAM)
- socket.settimeout(timeout)
- socket.connect_ex((host, port))  # Retourne 0 si ouvert
- socket.close()
- try/except pour gaierror

Exemple de sortie attendue:
Scanning 127.0.0.1
Port 22:   CLOSED
Port 80:   CLOSED
Port 443:  CLOSED
Port 3306: CLOSED
Port 5432: CLOSED
Port 8080: CLOSED
Port 9000: CLOSED

========================================
## Défi 2: Banner Grabbing et Détection de Services
========================================

Objectif : Récupérer les bannières des services actifs et identifier les services

Créez deux fonctions:

1. grab_banner(host, port, timeout) :
   - Établir une connexion TCP
   - Recevoir les données initiales (bannière)
   - socket.recv(1024) pour capturer jusqu'à 1024 bytes
   - Décoder en UTF-8 (ignorer les erreurs)
   - Retourner la bannière ou None

2. get_service_name(port) :
   - Dictionnaire des ports courants (22: SSH, 80: HTTP, etc.)
   - Minimum 15 entrées (22, 25, 53, 80, 110, 143, 443, 445, 1433, 3306, 3389, 5432, 6379, 8080, 27017)
   - Retourner le nom du service

3. Script principal qui:
   - Scanne une liste de ports: [20, 21, 22, 25, 53, 80, 110, 143, 443, 3306]
   - Pour chaque port ouvert, récupérer et afficher la bannière
   - Afficher le service identifié
   - Format: "Port 80: HTTP - 'HTTP/1.1 200 OK'"

Contraintes:
- Pas d'exception non gérées (try/except pour tout)
- Timeout de 1 seconde pour banner grabbing
- Afficher "(no banner)" si pas de réponse
- Gestion multi-plateforme

Indications:
- socket.recv(1024) pour recevoir
- .decode('utf-8', errors='ignore')
- .strip() pour enlever les whitespace
- Dictionnaire pour KNOWN_SERVICES

Exemple de sortie attendue:
Port 22: SSH - 'SSH-2.0-OpenSSH_7.4'
Port 80: HTTP - 'HTTP/1.1 200 OK'
Port 443: HTTPS - (no banner)
Port 3306: MySQL - '5.7.30-0ubuntu0'
Port 5432: PostgreSQL - (no banner)

========================================
## Défi 3: Port Scanner Monothreaded avec Output Formaté
========================================

Objectif : Intégrer vérification ports + banners + formatage professionnel

Créez un script qui :

1. Classe SimplePortScanner:
   - __init__(host, timeout, ports_list)
   - scan() : lance le scan
   - Stocke les résultats dans un dictionnaire

2. Scan et récupération:
   - Pour chaque port, appeler check_port()
   - Si ouvert, appeler grab_banner()
   - Stocker: {port: {open, banner, service}}

3. Output formaté:
   - Générer un rapport professionnell
   - Inclure: Timestamp, target, ports scannés, ports ouverts, temps total
   - Tableau des résultats avec colonnes: Port | Service | State | Banner

4. Teste avec:
   - Target: 127.0.0.1
   - 50 ports: range(1, 51)
   - Affiche le temps écoulé et vitesse (ports/sec)

Contraintes:
- Pas de multi-threading (monothreaded)
- Output clairement formaté
- Timeouts strictes (1 seconde)
- Gestion complète d'erreurs

Indications:
- Créer une classe SimplePortScanner
- Dictionnaire pour results
- Utiliser datetime pour timestamp
- Format rapport ASCII propre

Exemple de sortie attendue:
======================================================
PORT SCANNER RESULTS
======================================================
Timestamp: 2024-11-07 14:30:45
Target: 127.0.0.1
Ports Scanned: 50
Open Ports: 0
Scan Time: 12.34 seconds
Rate: 4.05 ports/sec

No open ports found

======================================================

========================================
## Défi 4: Multi-threading avec Queue
========================================

Objectif : Paralléliser le scanning pour 10-100x speedup

Créez un script qui :

1. Classe ThreadedPortScanner:
   - __init__(host, timeout, max_threads)
   - scan_ports(port_list) : lancer le scan parallèle
   - Utiliser Queue pour queue les ports
   - Utiliser threading.Lock() pour protéger results

2. Architecture:
   - Queue contient les ports à scanner
   - N threads worker prennent les ports de la queue
   - Chaque worker scanne son port et stocke le résultat
   - threading.Lock() protège l'accès au dictionnaire shared

3. Implémentation:
   - def worker(): boucle sur queue.get(), scan port, queue.task_done()
   - Créer N threads (min(max_threads, len(ports)))
   - port_queue.join() pour attendre completion
   - socket.connect_ex() pour test rapide (pas de banner grabbing)

4. Comparaison de performance:
   - Afficher: "X ports avec 1 thread: Y.Z secondes"
   - Afficher: "X ports avec 10 threads: A.B secondes"
   - Afficher: "Speedup: {mono/multi:.1f}x"

5. Tests:
   - Ports 1-100 avec différents thread counts (1, 5, 10, 20)
   - Afficher le speedup pour chaque

Contraintes:
- TOUJOURS utiliser Lock() pour accès à results
- Timeout court (0.5 secondes) pour paramétriser test
- max_threads limité à 50 (ne pas DOS-er la cible)
- Gestion d'exception pour threads

Indications:
- from queue import Queue
- import threading
- Queue.get_nowait() pour non-bloquant
- Queue.task_done() après chaque travail
- Queue.join() pour attendre tout le monde
- threading.Lock() pour synchronisation

Exemple de sortie attendue:
ThreadedPortScanner Test
========================
Target: 127.0.0.1
Ports: 1-100 (100 ports)

1 thread:  5.23 seconds (19.1 ports/sec)
5 threads: 2.14 seconds (46.7 ports/sec)
10 threads: 1.45 seconds (69.0 ports/sec)
20 threads: 1.42 seconds (70.4 ports/sec)

Speedup (1 vs 10): 3.6x
Found open ports: 0

========================================
## Défi 5: Détection de Ports Communs et Filtrage Intelligent
========================================

Objectif : Scanner les ports "intéressants" avec détection automatique

Créez un script qui :

1. Définir une liste de ports communs (au moins 30):
   - Well-known ports (21, 22, 25, 53, 80, etc.)
   - Services courants (3306, 5432, 6379, 8080, etc.)
   - Ports à risque (445, 3389, 27017, etc.)

2. Créer des profils de scan:
   - QUICK: 20 ports courants (22, 80, 443, 3306, 5432, 8080, etc.)
   - STANDARD: 50 ports communs
   - COMPREHENSIVE: 100 ports

3. Implémentation:
   - Dictionnaire: {port: (service_short, service_long, risk_level)}
   - Fonctions pour récupérer profils
   - Scanner avec ports filtrés

4. Scanner complète:
   - Ajouter un paramètre "profile" au scanner
   - Afficher quels ports sont scannés
   - Marquer les ports dangereux avec [!]
   - Filtrer les résultats par risque

5. Résultats:
   - Trier par port
   - Afficher le "risk level" des ports ouverts
   - Alerter si ports dangereux ouverts

Contraintes:
- Minimum 30 entrées dans dictionnaire de services
- Trois profils minimum
- Affichage du risque
- Pas d'hardcoding de ports

Indications:
- Dictionnaire: {port: (name, description, risk)}
- Fonctions get_quick_profile(), get_standard_profile(), etc.
- Scanner avec filtre de ports

Exemple de sortie attendue:
INTELLIGENT PORT SCANNER
=========================
Profile: QUICK
Ports to scan: 20 (Common services)
Scanning...

Open Ports (sorted by port):
Port 22    [SSH]             Risk: LOW
Port 80    [HTTP]            Risk: LOW
Port 3306  [MySQL]           Risk: MEDIUM
Port 445   [SMB]             Risk: HIGH [!]
Port 27017 [MongoDB]         Risk: HIGH [!]

Summary:
- Total open: 5
- High risk ports: 2 *** ALERT ***

========================================
## Défi 6: Validation d'Entrée et Gestion d'Erreurs Robuste
========================================

Objectif : Créer un scanner production-ready avec validation complète

Créez une classe RobustPortScanner qui:

1. Validation d'entrée:
   - Valider host (IP ou hostname valide)
   - Utiliser ipaddress.ip_address() pour IP
   - Utiliser socket.gethostbyname() pour hostname
   - Valider port range (1-65535)
   - Valider timeout (0.5-30 secondes)
   - Valider max_threads (1-500)

2. Gestion d'erreurs complète:
   - socket.gaierror : Host invalide
   - socket.error : Erreur socket générique
   - socket.timeout : Timeout lors du scan
   - queue.Empty : Queue vide
   - threading exceptions : Threads erreurs
   - Capturer TOUS les cas sans crash

3. Logging détaillé:
   - Afficher quoi on scanne avant de commencer
   - Afficher progression (tous les 10 ports)
   - Afficher erreurs (host invalide, etc.)
   - Afficher résumé final

4. Tests with errors:
   - Host invalide: "this.is.invalid"
   - Hostname invalide: "!!!invalid!!!"
   - Port invalide: 0, 70000, -1
   - Timeout invalide: 0, 100

Contraintes:
- Validation stricte avant scan
- Exceptions avec messages clairs
- Pas de crash, messages d'erreur appropriés
- Logging de chaque erreur

Indications:
- ipaddress.ip_address(host)
- socket.gethostbyname(host)
- raise ValueError() pour validation
- try/except/finally pour resources
- logging.WARNING / ERROR pour messages

Exemple de sortie attendue:
RobustPortScanner Test
======================
[*] Validating input...
[+] Host: 127.0.0.1 (IP)
[+] Ports: 1-100
[+] Timeout: 1.0 sec
[+] Max threads: 10

[*] Starting scan...
[+] Scanned 10 ports...
[+] Scanned 20 ports...
...
[+] Scan complete: 100 ports, 0 open

[!] Error test:
Host 'invalid.host.!!!': Failed - Invalid IP address
Port 70000: Failed - Port out of range
Timeout -1: Failed - Invalid timeout

========================================
## Défi 7: Rapport Professionnel et Export de Résultats
========================================

Objectif : Générer des rapports professionnels et exploitables

Créez un scanner avec système de rapport:

1. Format de rapport:
   - En-tête avec timestamp, target, métadonnées
   - Section système (OS détecté, architecture si possible)
   - Résultats tabulaires (Port | Service | State | Banner)
   - Statistiques (temps, vitesse, ports ouverts)
   - Avertissements de sécurité si risque détecté

2. Exports multiples:
   - format_text() : Rapport lisible ASCII
   - format_csv() : Format CSV pour import
   - format_json() : Format JSON pour parsing
   - generate_file(filename) : Sauvegarder sur disque

3. Rapport texte:
   - Sections claires
   - Tableau aligné et bordé
   - Statistiques en bas
   - Avertissements en rouge (si terminal)

4. Export CSV:
   - Headers: Port,Service,State,Banner
   - Une ligne par port trouvé
   - Échapper les guillemets et virgules

5. Export JSON:
   - Structure: {metadata, results, statistics}
   - Dates en ISO format
   - Prêt pour traitement automatisé

Contraintes:
- Rapports structurés et propres
- Support multiple format
- Données valides et formatées
- Pas de crash lors d'export

Indications:
- Créer méthodes format_* pour chaque type
- Utiliser json.dumps() pour JSON
- csv.writer() pour CSV
- datetime.isoformat() pour dates
- Tester avec fichiers réels

Exemple de sortie attendue:
PORT SCANNER REPORT
=================================================
Generated: 2024-11-07 14:30:45
Target: 127.0.0.1
Scan Duration: 5.23 seconds
Scan Rate: 19.1 ports/sec

Port    Service       State       Banner
----    -------       -----       ------
22      SSH           OPEN        SSH-2.0-OpenSSH_7.4
80      HTTP          OPEN        HTTP/1.1 200 OK
443     HTTPS         OPEN        (TLS connection)
3306    MySQL         CLOSED      -
5432    PostgreSQL    CLOSED      -

Summary:
- Total ports scanned: 100
- Open ports: 3
- Closed ports: 97
- Filtered ports: 0

CSV Export:
22,SSH,OPEN,"SSH-2.0-OpenSSH_7.4"
80,HTTP,OPEN,"HTTP/1.1 200 OK"
443,HTTPS,OPEN,"(TLS connection)"

========================================
## Défi 8: Scanner Professionnel Complet (Challenge Final)
========================================

Objectif : Créer un outil professionnel complet et sécurisé

Créez un scanner production-ready qui combine TOUS les concepts:

1. Classe ProfessionalPortScanner:
   - Héritage ou composition avec classes précédentes
   - Toutes les validations de Défi 6
   - Tous les exports de Défi 7
   - Support des profils de Défi 5
   - Multi-threading de Défi 4
   - Banner grabbing de Défi 2

2. Architecture modulaire:
   - Classe Scanner (core scanning)
   - Classe ServiceDetector (détection services)
   - Classe ReportGenerator (génération rapports)
   - Classe ResultsFormatter (formatage output)

3. Fonctionnalités avancées:
   - Reprendre scan interrompu
   - Mode verbose/quiet
   - Support proxy (optionnel)
   - Détection OS basique
   - Chaîn JSON pour intégration

4. Sécurité:
   - JAMAIS de shell=True
   - Rate limiting (délai entre ports)
   - Gestion timeout robuste
   - Logs d'audit complets
   - Warnings éthiques/légaux

5. Interface CLI:
   - Script executable python3 scanner.py
   - Arguments: --target, --ports, --profile, --threads, --output
   - Exemples:
```python
     * python3 scanner.py --target 127.0.0.1 --profile QUICK
     * python3 scanner.py --target 192.168.1.100 --ports 1-100 --threads 20
     * python3 scanner.py --target target.com --output results.json

```
6. Rapport final:
   - Création d'un vrai rapport texte
   - Créer rapport.txt avec tous les détails
   - Format professionnel
   - Inclure warnings légaux

Contraintes CRITIQUES:
- 100% fonctionnel et sans erreurs
- Validation complète d'entrée
- Gestion exception robuste
- Code modulaire et réutilisable
- Documentation complète (docstrings)
- Commentaires en français
- Support multi-plateforme
- Pas de dépendances externes (socket, threading, json, csv seulement)

Indications pour structure:
- Fichier principal: scanner.py
- Imports: socket, threading, queue, json, csv, datetime, ipaddress
- Classe Scanner (core)
- Classe ServiceDetector (données + logique services)
- Classe ReportGenerator (génération rapports multiples formats)
- Fonction main() pour CLI parsing
- Lots de docstrings

Exemple de sortie attendue:
======================================================
PROFESSIONAL PORT SCANNER v1.0
======================================================

[*] Initializing scanner...
[+] Target: 192.168.1.100
[+] Profile: STANDARD (50 ports)
[+] Threads: 20
[+] Timeout: 2.0 seconds

[*] Starting scan...
[>] Scanning ports... [████████████████████] 100%

[+] Scan completed in 3.45 seconds
[+] Scan rate: 14.5 ports/sec

========================================================
RESULTS
========================================================
Port    Service         State       Banner
----    -------         -----       ------
22      SSH             OPEN        SSH-2.0-OpenSSH_8.2
80      HTTP            OPEN        Apache/2.4.41
443     HTTPS           OPEN        (TLS Connection)
3306    MySQL           CLOSED      -
5432    PostgreSQL      CLOSED      -

========================================================
SUMMARY
========================================================
Total Scanned: 50
Open Ports: 3
Closed Ports: 47
Filtered Ports: 0
Most Common Service: HTTP (ports 80, 8080, 8443)

========================================================
SECURITY NOTES
========================================================
[!] SSH exposed (port 22) - Consider restricting access
[!] HTTP exposed (port 80) - HTTPS recommended
[+] No obvious high-risk ports open

[*] Report exported to: results_192.168.1.100_20241107_143045.txt

========================================
BARÈME DE NOTATION
========================================

Défi 1 (Basiques):               10 points
Défi 2 (Banners):               15 points
Défi 3 (Output):                15 points
Défi 4 (Multi-threading):       15 points
Défi 5 (Filtrage intelligent):  15 points
Défi 6 (Validation robuste):    15 points
Défi 7 (Rapports):              15 points
Défi 8 (Challenge complet):     20 points

Total: 120 points

Bonus:
- Code modulaire et réutilisable: +10
- Documentation complète: +5
- Gestion d'erreurs robuste: +5
- Performance optimisée: +5
- Support professionnel complet: +10

Maximum: 150 points

NOTES IMPORTANTES:
- Ne tester que sur vos propres systèmes ou environnements autorisés
- Chaque défi doit fonctionner sans erreurs
- Vérifier la sécurité du code (pas de vulnérabilités)
- Code lisible avec commentaires en français
- Respecter les conventions Python (PEP 8)
