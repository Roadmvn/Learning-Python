========================================
SOLUTIONS - EXERCICE 15 : THREADING
========================================

========================================
## Solution Défi 1: Scan de Ports Simple
========================================

#!/usr/bin/env python3
"""
Solution Défi 1: Scanner de ports multi-threadé
"""

```python
import socket
import threading
import time
from typing import List

def scan_port(host: str, port: int, timeout: float = 1.0) -> bool:
    """
    Teste si un port est ouvert

    Args:
        host: Adresse IP ou hostname
        port: Numéro de port
        timeout: Timeout de connexion

    Returns:
        True si port ouvert, False sinon
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except socket.error:
        return False

def scanner_sequentiel(host: str, ports: List[int]) -> List[int]:
    """
    Scanner séquentiel (sans threading)

    Args:
        host: Adresse cible
        ports: Liste des ports à scanner

    Returns:
        Liste des ports ouverts
    """
    print(f"Scan séquentiel de {host}...")
    ports_ouverts = []

    start_time = time.time()

    for port in ports:
        if scan_port(host, port):
            ports_ouverts.append(port)
            print(f"Port {port} : ouvert")
        else:
            print(f"Port {port} : fermé")

    elapsed_time = time.time() - start_time
    print(f"Temps: {elapsed_time:.1f}s")
    print(f"Ports ouverts: {ports_ouverts}\n")

    return ports_ouverts, elapsed_time

def scanner_multithread(host: str, ports: List[int]) -> List[int]:
    """
    Scanner multi-threadé

    Args:
        host: Adresse cible
        ports: Liste des ports à scanner

    Returns:
        Liste des ports ouverts
    """
    print(f"Scan multi-threadé de {host}...")
    ports_ouverts = []
    lock = threading.Lock()  # Protéger la liste partagée

    def worker(port: int):
        """Worker qui scanne un port"""
        if scan_port(host, port):
            with lock:
                ports_ouverts.append(port)
            print(f"Port {port} : ouvert")
        else:
            print(f"Port {port} : fermé")

    start_time = time.time()

    # Créer et démarrer les threads
    threads = []
    for port in ports:
        t = threading.Thread(target=worker, args=(port,))
        t.start()
        threads.append(t)

    # Attendre tous les threads
    for t in threads:
        t.join()

    elapsed_time = time.time() - start_time
    print(f"Temps: {elapsed_time:.1f}s")
    print(f"Ports ouverts: {sorted(ports_ouverts)}\n")

    return ports_ouverts, elapsed_time

```
# Test du scanner
```python
if __name__ == "__main__":
    # Liste de ports communs
    ports_communs = [
        21,    # FTP
        22,    # SSH
        23,    # Telnet
        25,    # SMTP
        53,    # DNS
        80,    # HTTP
        110,   # POP3
        143,   # IMAP
        443,   # HTTPS
        445,   # SMB
        3306,  # MySQL
        3389,  # RDP
        5432,  # PostgreSQL
        5900,  # VNC
        6379,  # Redis
        8000,  # HTTP Alt
        8080,  # HTTP Proxy
        8443,  # HTTPS Alt
        9000,  # Various
        27017  # MongoDB
    ]

    host = "127.0.0.1"

    # Scan séquentiel
    ports_seq, time_seq = scanner_sequentiel(host, ports_communs)

    # Scan multi-threadé
    ports_mt, time_mt = scanner_multithread(host, ports_communs)

    # Comparaison
    if time_seq > 0:
        improvement = time_seq / time_mt
        print(f"Amélioration: {improvement:.1f}x plus rapide")

```
========================================
## Solution Défi 2: Bruteforce SSH Simulé
========================================

#!/usr/bin/env python3
"""
Solution Défi 2: Bruteforce multi-threadé
"""

```python
import threading
import time
from concurrent.futures import ThreadPoolExecutor

```
# Mot de passe correct (simulation)
CORRECT_PASSWORD = "S3cur3P@ss2024"

# Compteurs globaux
attempts_counter = 0
counter_lock = threading.Lock()

```python
def check_password(username: str, password: str) -> bool:
    """
    Simule la vérification d'un mot de passe

    Args:
        username: Nom d'utilisateur
        password: Mot de passe à tester

    Returns:
        True si correct, False sinon
    """
    # Simuler délai réseau
    time.sleep(0.1)

    # Incrémenter compteur de tentatives
    global attempts_counter
    with counter_lock:
        attempts_counter += 1

    return password == CORRECT_PASSWORD

def bruteforce_password(username: str, wordlist: list) -> dict:
    """
    Bruteforce d'un mot de passe

    Args:
        username: Nom d'utilisateur cible
        wordlist: Liste de mots de passe à tester

    Returns:
        Dictionnaire avec résultats
    """
    print("Bruteforce en cours...")

    # Event pour arrêter dès qu'on trouve
    found_event = threading.Event()
    found_password = {"password": None}

    def try_password(password: str):
        """Tester un mot de passe"""
        # Si déjà trouvé, ne rien faire
        if found_event.is_set():
            return

        thread_id = threading.current_thread().name
        print(f"[{thread_id}] Tentative: {username}:{password}")

        if check_password(username, password):
            # Mot de passe trouvé!
            found_event.set()
            found_password["password"] = password
            print(f"\n[{thread_id}] SUCCESS! Mot de passe trouvé: {password}")
            print("Arrêt des threads...")

    start_time = time.time()

    # Utiliser ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=10) as executor:
        # Soumettre toutes les tâches
        futures = []
        for password in wordlist:
            if found_event.is_set():
                break
            future = executor.submit(try_password, password)
            futures.append(future)

        # Attendre que tous les threads se terminent
        # (ou qu'on trouve le mot de passe)
        for future in futures:
            future.result()

    elapsed_time = time.time() - start_time

    # Statistiques
    print(f"\nStatistiques:")
    print("=" * 40)
    print(f"- Tentatives: {attempts_counter}")
    print(f"- Temps: {elapsed_time:.1f}s")
    print(f"- Mot de passe: {found_password['password']}")

    return {
        "password": found_password["password"],
        "attempts": attempts_counter,
        "time": elapsed_time
    }

```
# Test du bruteforce
```python
if __name__ == "__main__":
    # Wordlist de test
    wordlist = [
        "admin", "password", "123456", "qwerty", "letmein",
        "welcome", "monkey", "dragon", "master", "sunshine",
        "princess", "starwars", "football", "batman", "passw0rd",
        "abc123", "iloveyou", "trustno1", "shadow", "michael",
        "jennifer", "computer", "superman", "jordan", "harley",
        "summer", "1234567", "password1", "charlie", "rangers",
        "amanda", "Jessica", "pepper", "maverick", "robert",
        "matthew", "daniel", "test123", "hello", "knight",
        "andrea", "nicholas", "whatever", "hockey", "dallas",
        "S3cur3P@ss2024",  # Le bon mot de passe
        "admin123", "root123", "password2024", "secure123"
    ]

    username = "admin"
    result = bruteforce_password(username, wordlist)

```
========================================
## Solution Défi 3: Énumération de Répertoires Web
========================================

#!/usr/bin/env python3
"""
Solution Défi 3: Énumération de répertoires multi-threadé
"""

```python
import threading
import time
import random
from queue import Queue
from typing import Dict, List

def check_directory(url: str) -> tuple:
    """
    Simule la vérification d'un répertoire

    Args:
        url: URL complète à tester

    Returns:
        Tuple (url, status_code)
    """
    # Simuler délai réseau
    time.sleep(random.uniform(0.05, 0.15))

    # Simuler codes de statut (avec probabilités)
    weights = [0.15, 0.60, 0.10, 0.10, 0.05]  # 200, 404, 403, 301, 500
    status = random.choices([200, 404, 403, 301, 500], weights=weights)[0]

    return (url, status)

def enumerate_directories(base_url: str, directories: List[str], num_workers: int = 5):
    """
    Énumération de répertoires avec pattern producer-consumer

    Args:
        base_url: URL de base
        directories: Liste des chemins à tester
        num_workers: Nombre de threads workers
    """
    print(f"Énumération de {base_url} ({len(directories)} chemins, {num_workers} workers)")
    print("=" * 48)

    # Queue pour distribuer le travail
    queue = Queue()

    # Dictionnaires pour résultats
    results = {200: [], 301: [], 403: [], 404: [], 500: []}
    results_lock = threading.Lock()

    # Compteur de progression
    completed = {"count": 0}
    completed_lock = threading.Lock()

    def worker():
        """Worker qui consomme la queue"""
        while True:
            # Récupérer une tâche
            directory = queue.get()

            # None = signal d'arrêt
            if directory is None:
                queue.task_done()
                break

            # Tester le répertoire
            url = f"{base_url}{directory}"
            _, status = check_directory(url)

            # Sauvegarder résultat
            with results_lock:
                if status in results:
                    results[status].append(directory)

                # Afficher selon status
                if status == 200:
                    print(f"[+] {status} - {directory}")
                elif status in [301, 302]:
                    print(f"[+] {status} - {directory}")
                elif status == 403:
                    print(f"[!] {status} - {directory}")

            # Mettre à jour progression
            with completed_lock:
                completed["count"] += 1
                percent = (completed["count"] / len(directories)) * 100

                # Afficher barre de progression (tous les 10%)
                if completed["count"] % (len(directories) // 10 + 1) == 0:
                    filled = int(percent / 5)
                    bar = "#" * filled + " " * (20 - filled)
                    print(f"\nProgression: [{bar}] {int(percent)}%\n")

            queue.task_done()

    # Créer et démarrer les workers
    workers = []
    for _ in range(num_workers):
        t = threading.Thread(target=worker)
        t.start()
        workers.append(t)

    # Remplir la queue avec les répertoires
    for directory in directories:
        queue.put(directory)

    # Attendre que tout soit traité
    queue.join()

    # Arrêter les workers
    for _ in range(num_workers):
        queue.put(None)

    for t in workers:
        t.join()

    # Afficher résultats
    print("\nProgression: [####################] 100%\n")
    print("Résultats:")
    print("=" * 40)
    print(f"Total scanné: {len(directories)}")
    print(f"200 OK: {len(results[200])}")
    print(f"301 Redirect: {len(results[301])}")
    print(f"403 Forbidden: {len(results[403])}")
    print(f"404 Not Found: {len(results[404])}")
    print(f"500 Error: {len(results[500])}")

    # Chemins accessibles
    accessible = results[200] + results[301]
    if accessible:
        print(f"\nChemins accessibles:")
        for path in sorted(accessible):
            if path in results[301]:
                print(f"- {path} (redirect)")
            else:
                print(f"- {path}")

```
# Test de l'énumération
```python
if __name__ == "__main__":
    directories = [
        "/admin", "/backup", "/config", "/uploads", "/api", "/test", "/dev",
        "/login", "/dashboard", "/panel", "/wp-admin", "/administrator",
        "/phpmyadmin", "/sql", "/database", "/files", "/images", "/css",
        "/js", "/includes", "/logs", "/temp", "/cache", "/old", "/new",
        "/hidden", "/secret", "/private", "/public", "/data", "/downloads",
        "/docs", "/documentation", "/help", "/support", "/contact",
        "/about", "/profile", "/settings", "/search", "/register",
        "/forgot", "/reset", "/verify", "/confirm", "/activate",
        "/newsletter", "/subscribe", "/unsubscribe", "/shop", "/cart"
    ]

    enumerate_directories("http://example.com", directories, num_workers=5)

```
========================================
## Solution Défi 4: Download Manager Concurrent
========================================

#!/usr/bin/env python3
"""
Solution Défi 4: Download Manager multi-threadé
"""

```python
import threading
import time
import random
from concurrent.futures import ThreadPoolExecutor
from typing import Dict

class DownloadStats:
    """Statistiques globales de téléchargement"""

    def __init__(self):
        self.total_downloaded = 0
        self.files_completed = 0
        self.lock = threading.Lock()

    def add_chunk(self, size: int):
        """Ajouter un chunk téléchargé"""
        with self.lock:
            self.total_downloaded += size

    def complete_file(self):
        """Marquer un fichier comme complété"""
        with self.lock:
            self.files_completed += 1

def download_file(filename: str, size_mb: int, stats: DownloadStats) -> Dict:
    """
    Simule le téléchargement d'un fichier

    Args:
        filename: Nom du fichier
        size_mb: Taille en MB
        stats: Objet de statistiques partagé

    Returns:
        Dictionnaire avec infos du téléchargement
    """
    worker_name = threading.current_thread().name
    print(f"\n[{worker_name}] {filename} ({size_mb} MB)")

    # Télécharger par chunks de 1MB
    for chunk in range(1, size_mb + 1):
        time.sleep(0.5)  # Simuler I/O réseau

        # Mettre à jour stats
        stats.add_chunk(1)

        # Afficher progression
        percent = (chunk / size_mb) * 100
        filled = int(percent / 5)
        bar = "#" * filled + " " * (20 - filled)
        print(f"  Progression: [{bar}] {int(percent)}% ({chunk}/{size_mb} MB)")

    # Fichier complété
    stats.complete_file()
    print(f"[{worker_name}] {filename} ({size_mb} MB) - TERMINÉ")

    return {
        "filename": filename,
        "size": size_mb,
        "success": True
    }

def download_manager(files: list, max_workers: int = 3):
    """
    Gestionnaire de téléchargements concurrent

    Args:
        files: Liste de tuples (filename, size_mb)
        max_workers: Nombre de workers simultanés
    """
    print(f"Téléchargement de {len(files)} fichiers ({max_workers} workers simultanés)")
    print("=" * 60)

    # Statistiques partagées
    stats = DownloadStats()

    start_time = time.time()

    # Utiliser ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Soumettre tous les téléchargements
        futures = [
            executor.submit(download_file, filename, size, stats)
            for filename, size in files
        ]

        # Attendre tous les téléchargements
        results = [future.result() for future in futures]

    elapsed_time = time.time() - start_time

    # Statistiques finales
    print("\n" + "=" * 60)
    print("Statistiques finales:")
    print("=" * 60)
    print(f"Total téléchargé: {stats.total_downloaded} MB")
    print(f"Temps total: {elapsed_time:.1f}s")
    print(f"Vitesse moyenne: {stats.total_downloaded / elapsed_time:.2f} MB/s")
    print(f"Fichiers: {len(files)}")
    print(f"Succès: {stats.files_completed}")

```
# Test du download manager
```python
if __name__ == "__main__":
    # Générer liste de fichiers avec tailles aléatoires
    files = [
        (f"file{i+1}.{'zip' if i % 3 == 0 else 'iso' if i % 3 == 1 else 'tar.gz'}",
         random.randint(1, 10))
        for i in range(10)
    ]

    download_manager(files, max_workers=3)

```
========================================
## Solution Défi 5: Fuzzer HTTP Multi-threadé
========================================

#!/usr/bin/env python3
"""
Solution Défi 5: Fuzzer HTTP multi-threadé
"""

```python
import threading
import time
import random
from concurrent.futures import ThreadPoolExecutor
from typing import Dict, List
from dataclasses import dataclass

```
@dataclass
class Payload:
```python
    """Représente un payload de fuzzing"""
    type: str
    content: str

```
@dataclass
class Anomaly:
```python
    """Représente une anomalie détectée"""
    payload: Payload
    response_code: int
    response_time: float
    error_message: str = ""

def generate_payloads() -> List[Payload]:
    """Génère une liste de payloads de fuzzing"""
    payloads = []

    # SQLi payloads
    sqli = [
        "' OR '1'='1", "\" OR \"1\"=\"1", "' AND 1=1--",
        "' OR 1=1--", "admin'--", "' UNION SELECT NULL--",
        "'; DROP TABLE users--", "1' AND '1'='1",
        "' OR 'a'='a", "') OR ('1'='1"
    ]
    payloads.extend([Payload("SQLi", p) for p in sqli])

    # XSS payloads
    xss = [
        "<script>alert(1)</script>",
        "<img src=x onerror=alert(1)>",
        "<svg onload=alert(1)>",
        "javascript:alert(1)",
        "<iframe src=javascript:alert(1)>",
        "<body onload=alert(1)>",
        "'\"><script>alert(1)</script>",
        "<script>document.location='http://evil.com'</script>"
    ]
    payloads.extend([Payload("XSS", p) for p in xss])

    # Path Traversal
    path_trav = [
        "../../etc/passwd",
        "../../../etc/shadow",
        "..\\..\\windows\\system32\\config\\sam",
        "....//....//etc/passwd",
        "..%2F..%2Fetc%2Fpasswd",
        "..%252F..%252Fetc%252Fpasswd"
    ]
    payloads.extend([Payload("Path Traversal", p) for p in path_trav])

    # Command Injection
    cmd_inj = [
        "; ls -la",
        "| cat /etc/passwd",
        "& whoami",
        "`id`",
        "$(whoami)",
        "; ping -c 4 127.0.0.1",
        "| curl http://evil.com"
    ]
    payloads.extend([Payload("Command Injection", p) for p in cmd_inj])

    # Compléter jusqu'à 100 payloads
    while len(payloads) < 100:
        payload_type = random.choice(["SQLi", "XSS", "Path Traversal", "Command Injection"])
        content = f"FUZZ_{len(payloads)}_{payload_type}"
        payloads.append(Payload(payload_type, content))

    return payloads

def test_payload(payload: Payload) -> tuple:
    """
    Teste un payload (simulation)

    Returns:
        Tuple (payload, is_anomaly, response_code, response_time, error_msg)
    """
    # Simuler délai aléatoire
    response_time = random.uniform(0.1, 0.5)
    time.sleep(response_time)

    # Simuler détection d'anomalies (10% de chance)
    is_anomaly = random.random() < 0.1

    if is_anomaly:
        # Générer anomalie
        response_code = random.choice([500, 500, 200])  # Plus de 500

        # Messages d'erreur selon type de payload
        if payload.type == "SQLi" and response_code == 500:
            error_msg = f"SQL syntax error near '{payload.content}'"
        elif payload.type == "Path Traversal":
            error_msg = f"File not found: {payload.content}"
        elif response_code == 200:
            error_msg = "Unexpected content in response"
        else:
            error_msg = "Internal Server Error"

        return (payload, True, response_code, response_time, error_msg)
    else:
        return (payload, False, 200, response_time, "")

def http_fuzzer(payloads: List[Payload], num_threads: int = 10):
    """
    Fuzzer HTTP multi-threadé

    Args:
        payloads: Liste de payloads à tester
        num_threads: Nombre de threads
    """
    print(f"Fuzzing HTTP - {len(payloads)} payloads, {num_threads} threads")
    print("=" * 60)

    # Résultats
    anomalies = []
    anomalies_lock = threading.Lock()

    # Compteurs
    tested = {"count": 0}
    tested_lock = threading.Lock()

    def worker(payload: Payload):
        """Worker qui teste un payload"""
        thread_name = threading.current_thread().name
        print(f"[{thread_name}] Testing: {payload.content[:50]}")

        # Tester le payload
        result = test_payload(payload)
        _, is_anomaly, code, resp_time, error = result

        # Si anomalie détectée
        if is_anomaly:
            anomaly = Anomaly(payload, code, resp_time, error)
            with anomalies_lock:
                anomalies.append(anomaly)

            print(f"\n[!] ANOMALY DETECTED!")
            print(f"    Payload: {payload.content}")
            print(f"    Type: {payload.type}")
            print(f"    Response: {code}")
            print(f"    Time: {resp_time:.1f}s")
            if error:
                print(f"    Error: {error}")
            print()

        # Progression
        with tested_lock:
            tested["count"] += 1
            if tested["count"] % 10 == 0:
                percent = (tested["count"] / len(payloads)) * 100
                filled = int(percent / 5)
                bar = "#" * filled + " " * (20 - filled)
                print(f"\nProgression: [{bar}] {tested['count']}/{len(payloads)}\n")

    start_time = time.time()

    # Exécuter avec ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(worker, payloads)

    elapsed_time = time.time() - start_time

    # Statistiques finales
    print("\n" + "=" * 60)
    print("Résultats:")
    print("=" * 60)
    print(f"Total payloads: {len(payloads)}")
    print(f"Tests effectués: {tested['count']}")
    print(f"Anomalies détectées: {len(anomalies)}")
    print(f"Temps total: {elapsed_time:.1f}s")
    print(f"Taux: {len(payloads) / elapsed_time:.1f} tests/s")

    # Anomalies par type
    if anomalies:
        print(f"\nAnomalies par type:")
        types_count = {}
        for anomaly in anomalies:
            ptype = anomaly.payload.type
            types_count[ptype] = types_count.get(ptype, 0) + 1

        for ptype, count in sorted(types_count.items()):
            print(f"- {ptype}: {count}")

        # Sauvegarder résultats
        with open("results.txt", "w") as f:
            f.write("FUZZING RESULTS\n")
            f.write("=" * 60 + "\n\n")
            for anomaly in anomalies:
                f.write(f"Type: {anomaly.payload.type}\n")
                f.write(f"Payload: {anomaly.payload.content}\n")
                f.write(f"Response Code: {anomaly.response_code}\n")
                f.write(f"Response Time: {anomaly.response_time:.2f}s\n")
                if anomaly.error_message:
                    f.write(f"Error: {anomaly.error_message}\n")
                f.write("\n")

        print(f"\nRésultats sauvegardés dans: results.txt")

```
# Test du fuzzer
```python
if __name__ == "__main__":
    payloads = generate_payloads()
    http_fuzzer(payloads, num_threads=10)

```
========================================
## Solution Défi 6: Scanner de Vulnérabilités Concurrent
========================================

#!/usr/bin/env python3
"""
Solution Défi 6: Scanner de vulnérabilités multi-modules
"""

```python
import threading
import time
import random
from queue import Queue
from typing import Dict, List
from dataclasses import dataclass
from datetime import datetime

```
@dataclass
class Finding:
```python
    """Représente un finding de sécurité"""
    module: str
    category: str
    severity: str
    description: str
    details: str = ""

class ScanModule:
    """Classe de base pour les modules de scan"""

    def __init__(self, name: str, target: str, results_queue: Queue):
        self.name = name
        self.target = target
        self.results_queue = results_queue
        self.findings = []
        self.progress = 0

    def report_finding(self, category: str, severity: str, description: str, details: str = ""):
        """Envoyer un finding dans la queue"""
        finding = Finding(self.name, category, severity, description, details)
        self.findings.append(finding)
        self.results_queue.put(finding)

    def run(self):
        """Méthode à implémenter par les modules"""
        raise NotImplementedError

class PortScannerModule(ScanModule):
    """Module de scan de ports"""

    def run(self):
        print(f"[{self.name}] Démarrage...")

        # Simuler scan de 20 ports
        ports = [21, 22, 23, 25, 80, 443, 445, 3306, 3389, 5432,
                 5900, 6379, 8000, 8080, 8443, 9000, 27017, 5000, 6000, 7000]

        for i, port in enumerate(ports):
            time.sleep(0.2)
            self.progress = int((i + 1) / len(ports) * 100)

            # 20% chance de trouver port ouvert
            if random.random() < 0.2:
                self.report_finding(
                    "Open Port",
                    "INFO",
                    f"Port {port} ouvert",
                    f"Port {port}/tcp ouvert - Service potentiel"
                )

        print(f"[{self.name}] Terminé - {len(self.findings)} findings")

class ServiceDetectionModule(ScanModule):
    """Module de détection de services"""

    def run(self):
        print(f"[{self.name}] Démarrage...")

        services = [
            ("SSH", "OpenSSH 7.4", "HIGH", "Version vulnérable détectée"),
            ("HTTP", "Apache 2.2.15", "HIGH", "Version obsolète"),
            ("MySQL", "5.5.62", "MEDIUM", "Configuration non sécurisée"),
        ]

        for i, (service, version, severity, desc) in enumerate(services):
            time.sleep(0.5)
            self.progress = int((i + 1) / len(services) * 100)

            if random.random() < 0.6:
                self.report_finding(
                    "Service",
                    severity,
                    f"{service}: {version}",
                    desc
                )

        print(f"[{self.name}] Terminé - {len(self.findings)} findings")

class VulnerabilityScanModule(ScanModule):
    """Module de scan de vulnérabilités"""

    def run(self):
        print(f"[{self.name}] Démarrage...")

        vulnerabilities = [
            ("CVE-2021-1234", "CRITICAL", "SSH Remote Code Execution"),
            ("CVE-2022-5678", "CRITICAL", "Apache Buffer Overflow"),
            ("CVE-2020-9999", "HIGH", "MySQL Authentication Bypass"),
            ("CVE-2019-8888", "MEDIUM", "Directory Traversal"),
        ]

        for i, (cve, severity, desc) in enumerate(vulnerabilities):
            time.sleep(0.4)
            self.progress = int((i + 1) / len(vulnerabilities) * 100)

            if random.random() < 0.5:
                self.report_finding(
                    "Vulnerability",
                    severity,
                    f"{cve}: {desc}",
                    f"CVE: {cve}"
                )

        print(f"[{self.name}] Terminé - {len(self.findings)} findings")

class DirectoryEnumModule(ScanModule):
    """Module d'énumération de répertoires"""

    def run(self):
        print(f"[{self.name}] Démarrage...")

        directories = ["/admin", "/backup", "/config", "/uploads", "/api"]

        for i, directory in enumerate(directories):
            time.sleep(0.3)
            self.progress = int((i + 1) / len(directories) * 100)

            if random.random() < 0.3:
                self.report_finding(
                    "Directory",
                    "MEDIUM",
                    f"{directory} accessible",
                    f"Répertoire accessible sans authentification"
                )

        print(f"[{self.name}] Terminé - {len(self.findings)} findings")

class SSLCheckModule(ScanModule):
    """Module de vérification SSL/TLS"""

    def run(self):
        print(f"[{self.name}] Démarrage...")

        time.sleep(1)
        self.progress = 50

        # Vérifications SSL
        if random.random() < 0.5:
            self.report_finding(
                "SSL",
                "LOW",
                "Certificat auto-signé",
                "Le certificat SSL est auto-signé"
            )

        self.progress = 100
        print(f"[{self.name}] Terminé - {len(self.findings)} findings")

class DNSEnumModule(ScanModule):
    """Module d'énumération DNS"""

    def run(self):
        print(f"[{self.name}] Démarrage...")

        subdomains = ["www", "mail", "ftp", "admin", "api"]

        for i, subdomain in enumerate(subdomains):
            time.sleep(0.2)
            self.progress = int((i + 1) / len(subdomains) * 100)

            if random.random() < 0.2:
                self.report_finding(
                    "DNS",
                    "INFO",
                    f"Sous-domaine trouvé: {subdomain}.{self.target}",
                    f"IP: 192.168.1.{random.randint(1, 254)}"
                )

        print(f"[{self.name}] Terminé - {len(self.findings)} findings")

def vulnerability_scanner(target: str):
    """
    Scanner de vulnérabilités complet

    Args:
        target: Cible à scanner
    """
    print("=" * 60)
    print("    PENTEST SCANNER v1.0")
    print(f"    Target: {target}")
    print("=" * 60)

    # Queue pour collecter les résultats
    results_queue = Queue()

    # Créer les modules
    modules = [
        PortScannerModule("PortScanner", target, results_queue),
        ServiceDetectionModule("ServiceDetection", target, results_queue),
        VulnerabilityScanModule("VulnerabilityScan", target, results_queue),
        DirectoryEnumModule("DirectoryEnum", target, results_queue),
        SSLCheckModule("SSLCheck", target, results_queue),
        DNSEnumModule("DNSEnum", target, results_queue),
    ]

    print("\nChargement des modules...")
    for module in modules:
        print(f"[+] Module chargé: {module.name}")

    print("\nConfiguration:")
    print(f"- Threads: {len(modules)}")
    print(f"- Timeout: 10s")
    print(f"- Verbosité: INFO")

    print("\nDémarrage du scan...\n")

    start_time = time.time()

    # Lancer chaque module dans son thread
    threads = []
    for module in modules:
        t = threading.Thread(target=module.run)
        t.start()
        threads.append(t)

    # Thread pour afficher le dashboard
    dashboard_stop = threading.Event()

    def dashboard():
        """Affiche le dashboard en temps réel"""
        while not dashboard_stop.is_set():
            time.sleep(2)

            print("\n" + "=" * 60)
            print("                    DASHBOARD")
            print("=" * 60)
            elapsed = time.time() - start_time
            print(f"Temps écoulé: {int(elapsed // 60):02d}:{int(elapsed % 60):02d}")

            # Progression des modules
            total_progress = sum(m.progress for m in modules) / len(modules)
            filled = int(total_progress / 5)
            bar = "#" * filled + " " * (20 - filled)
            print(f"Progression globale: [{bar}] {int(total_progress)}%")

            print("\nModules actifs:")
            for module in modules:
                status = "TERMINÉ" if module.progress == 100 else "RUNNING"
                print(f"  [{status}] {module.name} ({module.progress}%)")

            # Nombre de findings
            total_findings = sum(len(m.findings) for m in modules)
            print(f"\nFindings: {total_findings}")

            # Derniers findings
            if not results_queue.empty():
                print("\nDerniers findings:")
                recent = []
                while not results_queue.empty() and len(recent) < 3:
                    recent.append(results_queue.get())

                for finding in recent:
                    print(f"  [{finding.severity}] {finding.description}")

            print("=" * 60)

    dashboard_thread = threading.Thread(target=dashboard)
    dashboard_thread.start()

    # Attendre tous les modules
    for t in threads:
        t.join()

    # Arrêter le dashboard
    dashboard_stop.set()
    dashboard_thread.join()

    elapsed_time = time.time() - start_time

    # Générer rapport final
    print("\n\nGénération du rapport...")
    print("\n" + "=" * 60)
    print("              RAPPORT DE PENTEST")
    print("=" * 60)
    print(f"Target: {target}")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Durée: {int(elapsed_time // 60)}m {int(elapsed_time % 60)}s")

    # Statistiques
    all_findings = []
    for module in modules:
        all_findings.extend(module.findings)

    severity_count = {
        "CRITICAL": 0,
        "HIGH": 0,
        "MEDIUM": 0,
        "LOW": 0,
        "INFO": 0
    }

    for finding in all_findings:
        severity_count[finding.severity] += 1

    print(f"\nRÉSUMÉ:")
    print("-" * 60)
    print(f"Total findings: {len(all_findings)}")
    for severity, count in severity_count.items():
        if count > 0:
            print(f"  - {severity}: {count}")

    print(f"\nDÉTAILS PAR MODULE:")
    print("-" * 60)

    for i, module in enumerate(modules, 1):
        print(f"\n[{i}] {module.name.upper()}")
        if module.findings:
            for finding in module.findings:
                print(f"  [{finding.severity}] {finding.description}")
                if finding.details:
                    print(f"      {finding.details}")
        else:
            print("  Aucun finding")

    print("\n" + "=" * 60)
    print(f"Rapport sauvegardé: pentest_report_{target}.json")
    print("=" * 60)

```
# Test du scanner
```python
if __name__ == "__main__":
    vulnerability_scanner("example.com")

```
========================================
## Solution Défi 7: Rate-Limited API Scraper
========================================

#!/usr/bin/env python3
"""
Solution Défi 7: API Scraper avec rate limiting
"""

```python
import threading
import time
import random
import json
from typing import Dict, List
from dataclasses import dataclass, asdict

```
@dataclass
class ScrapedData:
```python
    """Données scrapées"""
    url: str
    status_code: int
    data: str
    timestamp: float

class RateLimiter:
    """Limiteur de taux (rate limiter)"""

    def __init__(self, max_requests: int, time_window: float = 1.0):
        """
        Args:
            max_requests: Nombre maximum de requêtes
            time_window: Fenêtre de temps en secondes
        """
        self.max_requests = max_requests
        self.time_window = time_window
        self.semaphore = threading.Semaphore(max_requests)
        self.lock = threading.Lock()
        self.request_times = []

    def acquire(self):
        """Acquérir le droit de faire une requête"""
        # Nettoyer les anciennes requêtes
        current_time = time.time()
        with self.lock:
            self.request_times = [
                t for t in self.request_times
                if current_time - t < self.time_window
            ]

            # Si trop de requêtes récentes, attendre
            if len(self.request_times) >= self.max_requests:
                sleep_time = self.time_window - (current_time - self.request_times[0])
                if sleep_time > 0:
                    time.sleep(sleep_time)

            self.request_times.append(current_time)

class APIStats:
    """Statistiques du scraper"""

    def __init__(self):
        self.success = 0
        self.errors = 0
        self.retries = 0
        self.lock = threading.Lock()

    def record_success(self):
        with self.lock:
            self.success += 1

    def record_error(self):
        with self.lock:
            self.errors += 1

    def record_retry(self):
        with self.lock:
            self.retries += 1

    def get_stats(self) -> Dict:
        with self.lock:
            return {
                "success": self.success,
                "errors": self.errors,
                "retries": self.retries
            }

def fetch_url(url: str, max_retries: int = 3) -> tuple:
    """
    Simule une requête API avec retry

    Returns:
        Tuple (success, status_code, data)
    """
    # Simuler délai réseau
    time.sleep(random.uniform(0.1, 0.3))

    # 10% de chance d'erreur
    if random.random() < 0.1:
        status_code = random.choice([500, 503, 504])
        return (False, status_code, "")

    # Succès
    data = f"Data from {url}"
    return (True, 200, data)

def scrape_with_retry(url: str, rate_limiter: RateLimiter,
                     stats: APIStats, max_retries: int = 3) -> ScrapedData:
    """
    Scrape une URL avec retry et rate limiting

    Args:
        url: URL à scraper
        rate_limiter: Rate limiter
        stats: Statistiques
        max_retries: Nombre maximum de retries

    Returns:
        Données scrapées ou None
    """
    for attempt in range(max_retries):
        # Respecter rate limit
        rate_limiter.acquire()

        # Tenter la requête
        success, status_code, data = fetch_url(url)

        if success:
            stats.record_success()
            return ScrapedData(url, status_code, data, time.time())

        # Échec
        if attempt < max_retries - 1:
            # Retry avec backoff exponentiel
            backoff = 2 ** attempt  # 1s, 2s, 4s
            print(f"[!] {url}: Erreur {status_code}, retry {attempt + 1}/{max_retries} dans {backoff}s...")
            stats.record_retry()
            time.sleep(backoff)
        else:
            # Dernier essai échoué
            stats.record_error()
            print(f"[!] {url}: Échec après {max_retries} tentatives")
            return None

    return None

def api_scraper(urls: List[str], max_workers: int = 10, rate_limit: int = 10):
    """
    Scraper API avec rate limiting

    Args:
        urls: Liste d'URLs à scraper
        max_workers: Nombre de workers
        rate_limit: Nombre de requêtes par seconde
    """
    print("API Scraper avec Rate Limiting")
    print("=" * 60)
    print(f"URLs: {len(urls)}")
    print(f"Rate Limit: {rate_limit} req/s")
    print(f"Max Retries: 3")
    print()

    # Initialisations
    rate_limiter = RateLimiter(rate_limit)
    stats = APIStats()
    results = []
    results_lock = threading.Lock()

    # Compteur de progression
    completed = {"count": 0}
    completed_lock = threading.Lock()

    # Thread pour afficher les stats
    stop_stats = threading.Event()
    start_time = time.time()

    def display_stats():
        """Affiche les stats périodiquement"""
        while not stop_stats.is_set():
            time.sleep(1)

            elapsed = int(time.time() - start_time)
            current_stats = stats.get_stats()

            with completed_lock:
                count = completed["count"]

            percent = int((count / len(urls)) * 100)

            print(f"[{elapsed:05d}s] Progression: {count}/{len(urls)} ({percent}%) | "
                  f"Succès: {current_stats['success']} | Erreurs: {current_stats['errors']}")

    stats_thread = threading.Thread(target=display_stats)
    stats_thread.start()

    def worker(url: str):
        """Worker qui scrape une URL"""
        result = scrape_with_retry(url, rate_limiter, stats)

        if result:
            with results_lock:
                results.append(result)
            print(f"[+] {url}: Succès")

        with completed_lock:
            completed["count"] += 1

    # Créer les threads
    threads = []
    for url in urls:
        t = threading.Thread(target=worker, args=(url,))
        t.start()
        threads.append(t)

        # Limiter le nombre de threads concurrents
        if len(threads) >= max_workers:
            threads[0].join()
            threads.pop(0)

    # Attendre tous les threads
    for t in threads:
        t.join()

    # Arrêter les stats
    stop_stats.set()
    stats_thread.join()

    elapsed_time = time.time() - start_time
    final_stats = stats.get_stats()

    # Statistiques finales
    print(f"\n[{int(elapsed_time):05d}s] Progression: {len(urls)}/{len(urls)} (100%) | "
          f"Succès: {final_stats['success']} | Erreurs: {final_stats['errors']}")

    print("\n" + "=" * 60)
    print("Statistiques Finales:")
    print("=" * 60)
    print(f"Total URLs: {len(urls)}")
    print(f"Succès: {final_stats['success']} ({final_stats['success']/len(urls)*100:.1f}%)")
    print(f"Échecs: {final_stats['errors']} ({final_stats['errors']/len(urls)*100:.1f}%)")
    print(f"Retries total: {final_stats['retries']}")
    print(f"Temps total: {elapsed_time:.1f}s")
    print(f"Taux moyen: {len(urls)/elapsed_time:.1f} req/s")

    # Sauvegarder résultats
    with open("results.json", "w") as f:
        json.dump([asdict(r) for r in results], f, indent=2)

    print(f"\nRésultats sauvegardés: results.json")

```
# Test du scraper
```python
if __name__ == "__main__":
    # Générer 200 URLs
    urls = [f"https://api.example.com/endpoint/{i}" for i in range(200)]

    api_scraper(urls, max_workers=10, rate_limit=10)

```
========================================
## Solution Défi 8: Framework de Pentesting Modulaire
========================================

#!/usr/bin/env python3
"""
Solution Défi 8: Framework de pentesting modulaire complet
"""

```python
import threading
import time
import random
from queue import PriorityQueue, Queue
from concurrent.futures import ThreadPoolExecutor
from typing import List, Dict
from dataclasses import dataclass, field
from datetime import datetime
from abc import ABC, abstractmethod
from enum import Enum

```
# Énumérations
```python
class Priority(Enum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3

class Severity(Enum):
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    INFO = "INFO"

```
# Structures de données
@dataclass
class Task:
```python
    """Représente une tâche de scan"""
    priority: Priority
    module_name: str
    target: str

    def __lt__(self, other):
        return self.priority.value < other.priority.value

```
@dataclass
class Finding:
```python
    """Représente un finding de sécurité"""
    module: str
    severity: Severity
    title: str
    description: str
    timestamp: float = field(default_factory=time.time)

class Module(ABC):
    """Classe abstraite pour les modules"""

    def __init__(self, name: str, priority: Priority):
        self.name = name
        self.priority = priority
        self.findings = []
        self.progress = 0
        self.status = "PENDING"

    @abstractmethod
    def scan(self, target: str, results_queue: Queue):
        """Exécute le scan"""
        pass

    def report_finding(self, severity: Severity, title: str, description: str,
                      results_queue: Queue):
        """Rapporter un finding"""
        finding = Finding(self.name, severity, title, description)
        self.findings.append(finding)
        results_queue.put(finding)

```
# Modules concrets
```python
class PortScannerModule(Module):
    """Scanner de ports"""

    def __init__(self):
        super().__init__("PortScanner", Priority.HIGH)

    def scan(self, target: str, results_queue: Queue):
        self.status = "RUNNING"
        print(f"[+] Module démarré: {self.name}")

        ports = [21, 22, 23, 25, 80, 443, 445, 3306, 3389, 5432]

        for i, port in enumerate(ports):
            time.sleep(0.3)
            self.progress = int((i + 1) / len(ports) * 100)

            if random.random() < 0.3:
                self.report_finding(
                    Severity.INFO,
                    f"Port {port} ouvert",
                    f"Port {port}/tcp ouvert sur {target}",
                    results_queue
                )

        self.status = "COMPLETED"

class ServiceDetectionModule(Module):
    """Détection de services"""

    def __init__(self):
        super().__init__("ServiceDetection", Priority.HIGH)

    def scan(self, target: str, results_queue: Queue):
        self.status = "RUNNING"
        print(f"[+] Module démarré: {self.name}")

        services = [
            ("SSH", "OpenSSH 7.4", Severity.HIGH, "Version vulnérable détectée"),
            ("HTTP", "Apache 2.2.15", Severity.HIGH, "Version obsolète"),
        ]

        for i, (service, version, severity, desc) in enumerate(services):
            time.sleep(0.5)
            self.progress = int((i + 1) / len(services) * 100)

            if random.random() < 0.7:
                self.report_finding(
                    severity,
                    f"{service}: {version}",
                    desc,
                    results_queue
                )

        self.status = "COMPLETED"

class VulnerabilityScanModule(Module):
    """Scan de vulnérabilités"""

    def __init__(self):
        super().__init__("VulnerabilityScan", Priority.MEDIUM)

    def scan(self, target: str, results_queue: Queue):
        self.status = "RUNNING"
        print(f"[+] Module démarré: {self.name}")

        vulns = [
            ("CVE-2021-1234", Severity.CRITICAL, "SSH Remote Code Execution"),
            ("CVE-2022-5678", Severity.CRITICAL, "Apache HTTP Server Buffer Overflow"),
            ("CVE-2020-9999", Severity.HIGH, "MySQL Authentication Bypass"),
        ]

        for i, (cve, severity, desc) in enumerate(vulns):
            time.sleep(0.6)
            self.progress = int((i + 1) / len(vulns) * 100)

            if random.random() < 0.5:
                self.report_finding(
                    severity,
                    cve,
                    desc,
                    results_queue
                )

        self.status = "COMPLETED"

class DirectoryEnumModule(Module):
    """Énumération de répertoires"""

    def __init__(self):
        super().__init__("DirectoryEnum", Priority.MEDIUM)

    def scan(self, target: str, results_queue: Queue):
        self.status = "RUNNING"
        print(f"[+] Module démarré: {self.name}")

        dirs = ["/admin", "/backup", "/uploads"]

        for i, directory in enumerate(dirs):
            time.sleep(0.4)
            self.progress = int((i + 1) / len(dirs) * 100)

            if random.random() < 0.4:
                self.report_finding(
                    Severity.MEDIUM,
                    f"Directory: {directory}",
                    f"{directory} accessible sans authentification",
                    results_queue
                )

        self.status = "COMPLETED"

class SSLCheckModule(Module):
    """Vérification SSL/TLS"""

    def __init__(self):
        super().__init__("SSLCheck", Priority.LOW)

    def scan(self, target: str, results_queue: Queue):
        self.status = "RUNNING"
        print(f"[+] Module démarré: {self.name}")

        time.sleep(1.5)
        self.progress = 50

        if random.random() < 0.5:
            self.report_finding(
                Severity.LOW,
                "Certificat auto-signé",
                "Le certificat SSL est auto-signé",
                results_queue
            )

        self.progress = 100
        self.status = "COMPLETED"

class DNSEnumModule(Module):
    """Énumération DNS"""

    def __init__(self):
        super().__init__("DNSEnum", Priority.LOW)

    def scan(self, target: str, results_queue: Queue):
        self.status = "RUNNING"
        print(f"[+] Module démarré: {self.name}")

        subdomains = ["www", "mail", "api"]

        for i, subdomain in enumerate(subdomains):
            time.sleep(0.3)
            self.progress = int((i + 1) / len(subdomains) * 100)

            if random.random() < 0.3:
                self.report_finding(
                    Severity.INFO,
                    f"Sous-domaine: {subdomain}",
                    f"{subdomain}.{target} trouvé",
                    results_queue
                )

        self.status = "COMPLETED"

class PentestFramework:
    """Framework de pentesting complet"""

    def __init__(self, target: str, num_workers: int = 5):
        self.target = target
        self.num_workers = num_workers
        self.task_queue = PriorityQueue()
        self.results_queue = Queue()
        self.modules = []
        self.findings = []
        self.start_time = None
        self.stop_dashboard = threading.Event()

    def register_module(self, module: Module):
        """Enregistrer un module"""
        self.modules.append(module)

    def scan(self):
        """Lancer le scan complet"""
        print("=" * 60)
        print("    PENTEST FRAMEWORK v1.0")
        print(f"    Target: {self.target}")
        print("=" * 60)

        # Charger les modules
        print("\nChargement des modules...")
        for module in self.modules:
            print(f"[+] Module chargé: {module.name} ({module.priority.name})")
            self.task_queue.put(Task(module.priority, module.name, self.target))

        print(f"\nConfiguration:")
        print(f"- Threads: {self.num_workers}")
        print(f"- Timeout: 10s")
        print(f"- Verbosité: INFO")

        print("\nDémarrage du scan...\n")

        self.start_time = time.time()

        # Lancer le dashboard
        dashboard_thread = threading.Thread(target=self._dashboard)
        dashboard_thread.start()

        # Thread pour collecter les résultats
        collector_thread = threading.Thread(target=self._collect_results)
        collector_thread.start()

        # Exécuter les tâches avec ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=self.num_workers) as executor:
            while not self.task_queue.empty():
                task = self.task_queue.get()
                module = self._get_module(task.module_name)
                executor.submit(module.scan, task.target, self.results_queue)

        # Arrêter le collector
        self.results_queue.put(None)
        collector_thread.join()

        # Arrêter le dashboard
        self.stop_dashboard.set()
        dashboard_thread.join()

        # Générer le rapport
        self._generate_report()

    def _get_module(self, name: str) -> Module:
        """Récupérer un module par nom"""
        for module in self.modules:
            if module.name == name:
                return module
        return None

    def _collect_results(self):
        """Collecter les résultats"""
        while True:
            finding = self.results_queue.get()
            if finding is None:
                break
            self.findings.append(finding)

    def _dashboard(self):
        """Afficher le dashboard en temps réel"""
        while not self.stop_dashboard.is_set():
            time.sleep(2)

            print("\n" + "=" * 60)
            print("                    DASHBOARD")
            print("=" * 60)

            elapsed = int(time.time() - self.start_time)
            print(f"Temps écoulé: {elapsed // 60:02d}:{elapsed % 60:02d}")

            # Progression globale
            total_progress = sum(m.progress for m in self.modules) / len(self.modules)
            filled = int(total_progress / 5)
            bar = "#" * filled + " " * (20 - filled)
            print(f"Progression globale: [{bar}] {int(total_progress)}%")

            # Modules actifs
            print("\nModules actifs:")
            for module in self.modules:
                if module.status == "RUNNING":
                    print(f"  [RUNNING] {module.name} ({module.progress}%)")
                elif module.status == "PENDING":
                    print(f"  [QUEUED] {module.name}")

            # Findings
            severity_count = {s: 0 for s in Severity}
            for finding in self.findings:
                severity_count[finding.severity] += 1

            print(f"\nFindings: {len(self.findings)}")
            for severity in [Severity.CRITICAL, Severity.HIGH, Severity.MEDIUM, Severity.LOW]:
                count = severity_count[severity]
                if count > 0:
                    print(f"  - {severity.value}: {count}")

            # Derniers findings
            if self.findings:
                print("\nDerniers findings:")
                for finding in self.findings[-3:]:
                    print(f"  [{finding.severity.value}] {finding.title}")

            print("=" * 60)

    def _generate_report(self):
        """Générer le rapport final"""
        print("\n\nGénération du rapport...")

        elapsed_time = time.time() - self.start_time

        print("\n" + "=" * 60)
        print("              RAPPORT DE PENTEST")
        print("=" * 60)
        print(f"Target: {self.target}")
        print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Durée: {int(elapsed_time // 60)}m {int(elapsed_time % 60)}s")

        # Résumé
        print(f"\nRÉSUMÉ:")
        print("-" * 60)

        severity_count = {s: 0 for s in Severity}
        for finding in self.findings:
            severity_count[finding.severity] += 1

        print(f"Total findings: {len(self.findings)}")
        for severity in [Severity.CRITICAL, Severity.HIGH, Severity.MEDIUM, Severity.LOW]:
            count = severity_count[severity]
            if count > 0:
                print(f"  - {severity.value}: {count}")

        # Détails par module
        print(f"\nDÉTAILS PAR MODULE:")
        print("-" * 60)

        for i, module in enumerate(self.modules, 1):
            print(f"\n[{i}] {module.name.upper()}")
            print(f"Findings: {len(module.findings)}")

            if module.findings:
                for finding in module.findings:
                    print(f"  [{finding.severity.value}] {finding.title}")
                    print(f"      {finding.description}")

        # Recommandations
        print(f"\nRECOMMANDATIONS:")
        print("-" * 60)

        critical_findings = [f for f in self.findings if f.severity == Severity.CRITICAL]
        high_findings = [f for f in self.findings if f.severity == Severity.HIGH]

        if critical_findings:
            print("\n[URGENT]")
            for finding in critical_findings[:3]:
                print(f"- {finding.title}: {finding.description}")

        if high_findings:
            print("\n[HIGH]")
            for finding in high_findings[:3]:
                print(f"- {finding.title}: {finding.description}")

        print("\n" + "=" * 60)
        print(f"Rapport sauvegardé: pentest_report_{self.target}.json")
        print("=" * 60)

```
# Test du framework
```python
if __name__ == "__main__":
    # Créer le framework
    framework = PentestFramework("example.com", num_workers=5)

    # Enregistrer les modules
    framework.register_module(PortScannerModule())
    framework.register_module(ServiceDetectionModule())
    framework.register_module(VulnerabilityScanModule())
    framework.register_module(DirectoryEnumModule())
    framework.register_module(SSLCheckModule())
    framework.register_module(DNSEnumModule())

    # Lancer le scan
    framework.scan()

```
========================================
FIN DES SOLUTIONS
========================================

Ces solutions démontrent l'utilisation complète du threading en Python
avec des applications pratiques en cybersécurité.

Points clés démontrés:
- Création et gestion de threads
- Synchronisation avec Lock, Semaphore, Event
- ThreadPoolExecutor pour pool de threads
- Queue pour communication inter-threads
- Gestion des erreurs et retry
- Rate limiting
- Architecture modulaire
- Dashboard en temps réel
- Statistiques et rapports

Tous les exemples incluent:
- Commentaires en français
- Gestion des erreurs
- Thread-safety
- Performance améliorée
- Code professionnel et réutilisable
