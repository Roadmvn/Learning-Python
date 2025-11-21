# Exercice 17 : Port Scanner

## Avertissement Éthique

**ATTENTION - UTILISATION LÉGALE UNIQUEMENT**

Le scanning de ports sans autorisation explicite est ILLÉGAL dans la plupart des juridictions. Ce code est fourni UNIQUEMENT à des fins éducatives et de tests de sécurité autorisés.

**Utilisations légales autorisées :**
- Scanner vos propres systèmes et réseaux
- Tests de pénétration avec accord écrit préalable
- Environnements de laboratoire et machines virtuelles personnelles
- Audits de sécurité contractuels avec autorisation formelle

**Interdictions strictes :**
- Scanner des systèmes sans autorisation écrite
- Scanner des réseaux d'entreprise sans permission
- Utiliser pour des activités malveillantes ou illégales
- Scanner des infrastructures publiques sans accord

**Responsabilité :** L'auteur décline toute responsabilité pour l'usage inapproprié de ce code. L'utilisateur est seul responsable de ses actions.

## Objectifs d'Apprentissage

Apprendre à créer un scanner de ports professionnel en Python pour :
- Scanner des ports TCP sur des hôtes distants
- Détecter les services en écoute sur un système
- Effectuer du banner grabbing pour identifier les services
- Utiliser le multi-threading pour accélérer les scans
- Gérer les timeouts et connexions réseau
- Formater et présenter les résultats de manière professionnelle

## Concepts Clés

### 1. Port Scanning TCP
Technique de reconnaissance réseau pour identifier les ports ouverts sur une cible :
```
Port States:
├── Open → Port en écoute, service actif
├── Closed → Port fermé, aucun service
├── Filtered → Pare-feu bloque les paquets
└── Unknown → État indéterminé (timeout)
```

**Méthode de connexion complète (TCP Connect)** :
- Établit une connexion TCP complète (3-way handshake)
- SYN → SYN-ACK → ACK
- Plus fiable mais plus détectable
- Ne nécessite pas de privilèges root

### 2. Multi-threading pour Port Scanning
Accélération du scan en parallélisant les connexions :
```
Architecture Threading:
├── Main Thread → Gestion globale et affichage
├── Worker Threads → Scan individuel de ports
├── Queue → Distribution des tâches
└── Lock → Synchronisation des résultats
```

**Avantages du multi-threading :**
- Réduction drastique du temps de scan
- Gestion efficace des timeouts réseau
- Utilisation optimale des ressources
- Scalabilité pour grands ranges de ports

### 3. Banner Grabbing
Récupération des bannières de service pour identification :
```
Banner Grabbing Process:
├── Connexion → Établissement TCP au port
├── Réception → Lecture de la bannière (si envoyée)
├── Parsing → Extraction des informations
└── Identification → Détermination du service/version
```

**Informations récupérables :**
- Nom et version du service (SSH, HTTP, FTP, etc.)
- Système d'exploitation sous-jacent
- Configuration et modules actifs
- Potentielles vulnérabilités connues

### 4. Service Detection
Identification intelligente des services par port et bannière :
```
Detection Methods:
├── Port Number → Mapping port → service standard
├── Banner Analysis → Parsing de la bannière reçue
├── Probe Requests → Envoi de requêtes spécifiques
└── Pattern Matching → Reconnaissance de signatures
```

**Ports communs à scanner :**
```
Service Standards:
├── 21  → FTP (File Transfer Protocol)
├── 22  → SSH (Secure Shell)
├── 23  → Telnet
├── 25  → SMTP (Simple Mail Transfer Protocol)
├── 53  → DNS (Domain Name System)
├── 80  → HTTP (Web)
├── 110 → POP3 (Mail)
├── 143 → IMAP (Mail)
├── 443 → HTTPS (Web sécurisé)
├── 445 → SMB (Windows Shares)
├── 3306 → MySQL
├── 3389 → RDP (Remote Desktop)
├── 5432 → PostgreSQL
└── 8080 → HTTP Alternate
```

### 5. Output Formaté et Reporting
Présentation professionnelle des résultats :
```
Output Formats:
├── Console → Affichage temps réel
├── CSV → Import dans tableurs
├── JSON → Parsing automatisé
└── HTML → Rapports visuels
```

## Composants du Scanner

### Scanner Simple
```python
# Scan basique d'un seul port
def scan_port(host, port, timeout=1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0  # True si port ouvert
    except:
        return False
```

### Scanner Multi-threadé
```python
# Scan rapide avec workers parallèles
def threaded_scan(host, ports, num_threads=100):
    queue = Queue()
    for port in ports:
        queue.put(port)

    threads = []
    for _ in range(num_threads):
        t = Thread(target=worker, args=(queue, host))
        threads.append(t)
        t.start()
```

### Banner Grabber
```python
# Récupération de la bannière de service
def grab_banner(host, port, timeout=2):
    try:
        sock = socket.socket()
        sock.settimeout(timeout)
        sock.connect((host, port))
        banner = sock.recv(1024).decode().strip()
        sock.close()
        return banner
    except:
        return None
```

## Use Cases Red Teaming

### Reconnaissance
- Cartographie de l'infrastructure cible
- Identification des services exposés
- Détection des versions vulnérables
- Découverte de ports non-standard

### Analyse de Surface d'Attaque
- Énumération complète des services
- Identification des points d'entrée potentiels
- Détection de services mal configurés
- Mapping des technologies utilisées

### Post-Exploitation
- Scan de réseaux internes après compromission
- Identification de pivots potentiels
- Découverte de services internes sensibles
- Cartographie latérale du réseau

## Bonnes Pratiques

### Performance
- Ajuster le nombre de threads selon la cible
- Utiliser des timeouts appropriés (1-3 secondes)
- Scanner par ranges plutôt que tous les ports
- Implémenter un rate limiting si nécessaire

### Discrétion
- Éviter les scans trop rapides (détectables)
- Randomiser l'ordre des ports scannés
- Utiliser des timeouts réalistes
- Espacer les connexions si nécessaire

### Fiabilité
- Gérer correctement les exceptions réseau
- Implémenter des retry pour les timeouts
- Valider les bannières récupérées
- Logger les erreurs pour debugging

## Fichiers de l'Exercice

- `main.py` : Implémentation complète avec exemples commentés
- `exercice.txt` : 8 défis progressifs pour pratiquer
- `solution.txt` : Solutions complètes des exercices

## Exemples d'Utilisation

### Scan Basique
```bash
python main.py
# Scan des ports communs sur localhost
```

### Scan Personnalisé
```python
# Scanner une plage de ports spécifique
scanner = PortScanner("192.168.1.1", timeout=2)
results = scanner.scan_range(1, 1024)
scanner.display_results(results)
```

### Scan avec Banner Grabbing
```python
# Scan avec identification de services
scanner = AdvancedScanner("example.com")
results = scanner.full_scan([80, 443, 22, 21])
scanner.export_json(results, "scan_results.json")
```

## Ressources Additionnelles

### Documentation Python
- `socket` : Opérations réseau bas niveau
- `threading` : Parallélisation des scans
- `queue` : Gestion des tâches de scan
- `json` : Export des résultats

### Outils Professionnels
- **Nmap** : Scanner de ports de référence
- **Masscan** : Scanner ultra-rapide
- **Unicornscan** : Scanner asynchrone avancé
- **ZMap** : Scanner Internet-scale

### Concepts Avancés
- SYN Stealth Scanning (nécessite root)
- UDP Port Scanning
- OS Fingerprinting
- Firewall/IDS Evasion Techniques

## Notes de Sécurité

**Détection et Logs** :
- Les scans de ports sont généralement loggés
- Les IDS/IPS modernes détectent les scans
- Les pare-feu peuvent bloquer après détection
- Les scans rapides sont très visibles

**Alternatives légales** :
- HackTheBox pour pratiquer légalement
- TryHackMe pour labs de sécurité
- DVWA (Damn Vulnerable Web App)
- Metasploitable pour tests locaux

**Rappel légal final** : N'utilisez ce code que sur des systèmes dont vous avez l'autorisation écrite. Le scanning non autorisé est illégal et peut entraîner des poursuites judiciaires.
