========================================
# Exercice 17: SOLUTIONS COMPLÈTES
Port Scanner en Python
========================================

========================================
## Défi 1: SCANNER BASIQUE - CONNEXION TCP SIMPLE
========================================

Solution:

```python
#!/usr/bin/env python3
"""
Défi 1: Scanner Basique - Connexion TCP Simple
Maîtriser socket.connect() et vérification d'état de port
"""

```python
import socket

def check_port(host, port, timeout=2):
    """
    Vérifier si un port est ouvert

    Args:
        host: Hôte à tester (hostname ou IP)
        port: Numéro du port (1-65535)
        timeout: Délai d'attente en secondes

    Returns:
        True si le port est ouvert, False sinon
    """
    try:
        # Créer un socket TCP (IPv4)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Définir le timeout pour éviter les blocages infinis
        sock.settimeout(timeout)

        # Essayer de se connecter au port
        # connect_ex() retourne 0 si succès, sinon un code d'erreur
        result = sock.connect_ex((host, port))

        # Fermer le socket (IMPORTANT!)
        sock.close()

        # Retourner True si connexion réussie
        return result == 0

    except socket.gaierror:
        # Erreur de résolution DNS/hostname
        print(f"Erreur: impossible de résoudre le hostname '{host}'")
        return False
    except socket.error as e:
        # Autre erreur socket
        print(f"Erreur socket: {e}")
        return False

def main():
    """Programme principal"""
    print("="*50)
    print("DÉFI 1 : SCANNER BASIQUE")
    print("="*50)

    # Cible
    host = '127.0.0.1'
    ports = [22, 80, 443, 3306, 5432, 8080, 9000]

    print(f"\nScanning {host}:")
    print("-" * 30)

    # Tester chaque port
    for port in ports:
        is_open = check_port(host, port, timeout=1)
        status = "OPEN" if is_open else "CLOSED"
        print(f"Port {port:5d}: {status}")

    print("\nNota Bene:")
    print("- Si aucun port ouvert, c'est normal (pas de serveurs actifs)")
    print("- Sur votre machine, vérifiez avec 'netstat -tuln' (Linux)")

if __name__ == "__main__":
    main()
```
```

Points clés:
- socket.AF_INET: IPv4
- socket.SOCK_STREAM: TCP
- socket.settimeout(): éviter blocage infini
- socket.connect_ex(): retourne 0 si succès
- TOUJOURS fermer le socket avec close()
- Gérer socket.gaierror pour hosts invalides

========================================
## Défi 2: BANNER GRABBING ET DÉTECTION DE SERVICES
========================================

Solution:

```python
#!/usr/bin/env python3
"""
Défi 2: Banner Grabbing et Détection de Services
Récupérer les bannières et identifier les services
"""

```python
import socket

```
# Dictionnaire des services courants
KNOWN_SERVICES = {
    20: 'FTP-DATA',
    21: 'FTP',
    22: 'SSH',
    25: 'SMTP',
    53: 'DNS',
    80: 'HTTP',
    110: 'POP3',
    143: 'IMAP',
    443: 'HTTPS',
    445: 'SMB',
    1433: 'MSSQL',
    3306: 'MySQL',
    3389: 'RDP',
```python
    5432: 'PostgreSQL',
    5900: 'VNC',
    6379: 'Redis',
    8080: 'HTTP-ALT',
    8443: 'HTTPS-ALT',
    27017: 'MongoDB',
    9200: 'Elasticsearch',
```
}

```python
def grab_banner(host, port, timeout=2):
    """
    Récupérer la bannière d'un service

    Args:
        host: Hôte cible
        port: Port du service
        timeout: Délai d'attente

    Returns:
        Bannière reçue (string) ou None si impossible
    """
    try:
        # Créer et configurer le socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)

        # Se connecter
        sock.connect((host, port))

        # Recevoir les données initiales (bannière)
        banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()

        sock.close()

        # Retourner la bannière si reçue, sinon None
        return banner if banner else None

    except Exception:
        # Silencieusement ignorer les erreurs
        return None

def get_service_name(port):
    """
    Obtenir le nom du service pour un port

    Args:
        port: Numéro du port

    Returns:
        Nom du service (string)
    """
    return KNOWN_SERVICES.get(port, 'Unknown')

def check_port(host, port, timeout=1):
    """Vérifier si un port est ouvert"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except:
        return False

def main():
    """Programme principal"""
    print("="*60)
    print("DÉFI 2 : BANNER GRABBING ET DÉTECTION DE SERVICES")
    print("="*60)

    host = '127.0.0.1'
    ports = [20, 21, 22, 25, 53, 80, 110, 143, 443, 3306]

    print(f"\nScanning {host} for open ports and banners:")
    print("-" * 60)

    found_any = False

    for port in ports:
        # Vérifier si le port est ouvert
        if check_port(host, port, timeout=1):
            found_any = True

            # Récupérer la bannière
            banner = grab_banner(host, port, timeout=1)
            service = get_service_name(port)

            # Afficher
            if banner:
                # Limiter la longueur de la bannière
                if len(banner) > 50:
                    banner = banner[:47] + "..."
                print(f"Port {port:5d}: {service:15s} - '{banner}'")
            else:
                print(f"Port {port:5d}: {service:15s} - (no banner)")

    if not found_any:
        print("Aucun port ouvert trouvé (normal si pas de serveurs actifs)")

    print("\nServices disponibles dans la base de données:")
    for port in sorted(KNOWN_SERVICES.keys())[:10]:
        print(f"  Port {port}: {KNOWN_SERVICES[port]}")
    print(f"  ... et {len(KNOWN_SERVICES)-10} autres")

if __name__ == "__main__":
    main()
```
```

Points clés:
- socket.recv(1024) pour recevoir les données
- .decode('utf-8', errors='ignore') pour transformer bytes en string
- .strip() pour enlever les whitespace et newlines
- TOUJOURS gérer les exceptions (pas d'arrêt du programme)
- Dictionnaire pour serveurs courants

========================================
## Défi 3: SCANNER AVEC OUTPUT FORMATÉ
========================================

Solution:

```python
#!/usr/bin/env python3
"""
Défi 3: Scanner Monothreaded avec Output Formaté
Intégrer vérification ports + banners + formatage professionnel
"""

```python
import socket
import time
from datetime import datetime

```
KNOWN_SERVICES = {
```python
    20: 'FTP-DATA', 21: 'FTP', 22: 'SSH', 25: 'SMTP', 53: 'DNS',
    80: 'HTTP', 110: 'POP3', 143: 'IMAP', 443: 'HTTPS', 445: 'SMB',
    1433: 'MSSQL', 3306: 'MySQL', 3389: 'RDP', 5432: 'PostgreSQL',
    5900: 'VNC', 6379: 'Redis', 8080: 'HTTP-ALT', 8443: 'HTTPS-ALT',
    27017: 'MongoDB', 9200: 'Elasticsearch',
```
}

```python
class SimplePortScanner:
    """Scanner de ports simple (monothreaded)"""

    def __init__(self, host, timeout=2, ports_list=None):
        """
        Initialiser le scanner

        Args:
            host: Hôte à scanner
            timeout: Timeout pour chaque port
            ports_list: Liste des ports à scanner
        """
        self.host = host
        self.timeout = timeout
        self.ports_list = ports_list or list(range(1, 1025))
        self.results = {}
        self.scan_time = 0

    def _check_port(self, port):
        """Vérifier si un port est ouvert"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((self.host, port))
            sock.close()
            return result == 0
        except:
            return False

    def _grab_banner(self, port):
        """Récupérer la bannière d'un port"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            sock.connect((self.host, port))
            banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
            sock.close()
            return banner if banner else None
        except:
            return None

    def scan(self):
        """Lancer le scan"""
        start_time = time.time()

        print(f"Scanning {len(self.ports_list)} ports on {self.host}...")

        for port in self.ports_list:
            if self._check_port(port):
                # Port ouvert
                banner = self._grab_banner(port)
                service = KNOWN_SERVICES.get(port, 'Unknown')

                self.results[port] = {
                    'open': True,
                    'banner': banner,
                    'service': service
                }

        self.scan_time = time.time() - start_time

    def generate_report(self):
        """Générer un rapport formaté"""
        report = []
        report.append("=" * 60)
        report.append("PORT SCANNER RESULTS")
        report.append("=" * 60)
        report.append(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"Target: {self.host}")
        report.append(f"Ports Scanned: {len(self.ports_list)}")
        report.append(f"Open Ports: {len(self.results)}")
        report.append(f"Scan Time: {self.scan_time:.2f} seconds")

        if len(self.ports_list) > 0:
            rate = len(self.ports_list) / self.scan_time
            report.append(f"Rate: {rate:.2f} ports/sec")

        report.append("")

        if self.results:
            report.append("Port    Service         Banner")
            report.append("-" * 60)
            for port in sorted(self.results.keys()):
                info = self.results[port]
                service = info['service']
                banner = info['banner'] if info['banner'] else "(none)"
                if len(banner) > 40:
                    banner = banner[:37] + "..."
                report.append(f"{port:5d}   {service:15s} {banner}")
        else:
            report.append("No open ports found")

        report.append("=" * 60)
        return "\n".join(report)

def main():
    """Programme principal"""
    print("="*60)
    print("DÉFI 3 : SCANNER AVEC OUTPUT FORMATÉ")
    print("="*60)

    # Créer le scanner
    scanner = SimplePortScanner(
        host='127.0.0.1',
        timeout=1,
        ports_list=list(range(1, 51))  # Ports 1-50
    )

    # Lancer le scan
    print("\nLaunching scan...")
    scanner.scan()

    # Afficher le rapport
    report = scanner.generate_report()
    print("\n" + report)

if __name__ == "__main__":
    main()
```
```

Points clés:
- Créer une classe pour organiser le code
- Méthodes privées avec _ pour des helpers
- Dictionnaire self.results pour stocker les données
- datetime.now().strftime() pour les timestamps
- Format rapport professionnel et lisible

========================================
## Défi 4: MULTI-THREADING AVEC QUEUE
========================================

Solution:

```python
#!/usr/bin/env python3
"""
Défi 4: Multi-threading avec Queue
Paralléliser le scanning pour 10-100x speedup
"""

```python
import socket
import threading
import time
from queue import Queue

class ThreadedPortScanner:
    """Scanner multi-threaded"""

    def __init__(self, host, timeout=2, max_threads=10):
        """
        Initialiser le scanner

        Args:
            host: Hôte à scanner
            timeout: Timeout pour chaque port
            max_threads: Nombre de threads
        """
        self.host = host
        self.timeout = timeout
        self.max_threads = max_threads
        self.results = {}
        # Lock pour protéger l'accès au dictionnaire partagé
        self.lock = threading.Lock()

    def _scan_port(self, port):
        """Scanner un port unique"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((self.host, port))
            sock.close()

            if result == 0:
                # Port ouvert - stocker de manière thread-safe
                with self.lock:
                    self.results[port] = True
        except:
            pass

    def scan_ports(self, ports):
        """
        Scanner une liste de ports en parallèle

        Args:
            ports: Liste des ports à scanner

        Returns:
            Dictionnaire des ports ouverts
        """
        # Créer la queue
        port_queue = Queue()
        for port in ports:
            port_queue.put(port)

        # Fonction worker pour chaque thread
        def worker():
            while not port_queue.empty():
                try:
                    port = port_queue.get_nowait()
                    self._scan_port(port)
                except:
                    pass
                finally:
                    port_queue.task_done()

        # Créer et démarrer les threads
        num_threads = min(self.max_threads, len(ports))
        threads = []

        for _ in range(num_threads):
            t = threading.Thread(target=worker, daemon=True)
            t.start()
            threads.append(t)

        # Attendre que tous les threads terminent
        port_queue.join()

        return self.results

def main():
    """Programme principal"""
    print("="*60)
    print("DÉFI 4 : MULTI-THREADING AVEC QUEUE")
    print("="*60)

    host = '127.0.0.1'
    ports = list(range(1, 101))  # Ports 1-100

    print(f"\nComparison of single-threaded vs multi-threaded scanning:")
    print("-" * 60)

    # Test monothreaded (simulation)
    print("\nMonothreaded (1 port at a time):")
    scanner_mono = ThreadedPortScanner(host, timeout=0.5, max_threads=1)
    start = time.time()
    results_mono = scanner_mono.scan_ports(ports)
    time_mono = time.time() - start
    print(f"  Time: {time_mono:.2f} seconds ({len(ports)/time_mono:.1f} ports/sec)")

    # Test multi-threaded
    print("\nMulti-threaded (10 threads):")
    scanner_multi = ThreadedPortScanner(host, timeout=0.5, max_threads=10)
    start = time.time()
    results_multi = scanner_multi.scan_ports(ports)
    time_multi = time.time() - start
    print(f"  Time: {time_multi:.2f} seconds ({len(ports)/time_multi:.1f} ports/sec)")

    # Speedup
    speedup = time_mono / time_multi
    print(f"\nSpeedup (1 vs 10 threads): {speedup:.1f}x faster")
    print(f"Ports found: {len(results_multi)}")

if __name__ == "__main__":
    main()
```
```

Points clés:
- Queue() pour queue les ports
- threading.Thread() pour créer threads
- queue.get_nowait() pour non-bloquant
- queue.task_done() après chaque travail
- queue.join() pour attendre completion
- threading.Lock() pour synchronisation

========================================
## Défi 5: DÉTECTION PORTS COMMUNS ET FILTRAGE
========================================

Solution:

```python
#!/usr/bin/env python3
"""
Défi 5: Détection Ports Communs et Filtrage Intelligent
Scanner les ports intéressants avec détection automatique
"""

```python
import socket
import time
from queue import Queue
import threading

```
# Dictionnaire complet avec noms de services
SERVICES = {
```python
    20: ('FTP-DATA', 'File Transfer Data', 'LOW'),
    21: ('FTP', 'File Transfer Protocol', 'MEDIUM'),
    22: ('SSH', 'Secure Shell', 'LOW'),
    25: ('SMTP', 'Simple Mail Transfer', 'LOW'),
    53: ('DNS', 'Domain Name System', 'LOW'),
    80: ('HTTP', 'HyperText Transfer', 'MEDIUM'),
    110: ('POP3', 'Post Office Protocol', 'LOW'),
    143: ('IMAP', 'Internet Message Access', 'LOW'),
    443: ('HTTPS', 'HTTP Secure', 'LOW'),
    445: ('SMB', 'Server Message Block', 'HIGH'),
    1433: ('MSSQL', 'MS SQL Server', 'MEDIUM'),
    3306: ('MySQL', 'MySQL Database', 'MEDIUM'),
    3389: ('RDP', 'Remote Desktop', 'HIGH'),
    5432: ('PostgreSQL', 'PostgreSQL Database', 'MEDIUM'),
    5900: ('VNC', 'Virtual Network Comp', 'HIGH'),
    6379: ('Redis', 'Redis Cache', 'HIGH'),
    8080: ('HTTP-ALT', 'Alternate HTTP', 'MEDIUM'),
    8443: ('HTTPS-ALT', 'Alternate HTTPS', 'MEDIUM'),
    27017: ('MongoDB', 'MongoDB Database', 'HIGH'),
    9200: ('Elasticsearch', 'Elasticsearch', 'HIGH'),
```
}

# Profils de scan
PROFILES = {
```python
    'QUICK': [22, 80, 443, 3306, 5432, 8080],
    'STANDARD': [20, 21, 22, 25, 53, 80, 110, 143, 443, 445,
                 1433, 3306, 3389, 5432, 5900, 6379, 8080, 8443],
    'COMPREHENSIVE': list(range(1, 101)),
```
}

```python
def get_service_info(port):
    """Obtenir info du service"""
    if port in SERVICES:
        return SERVICES[port]
    return ('Unknown', 'Unknown Service', 'MEDIUM')

def get_profile(profile_name):
    """Récupérer un profil"""
    return PROFILES.get(profile_name.upper(), PROFILES['STANDARD'])

class IntelligentScanner:
    """Scanner intelligent avec filtrage"""

    def __init__(self, host, profile='STANDARD', max_threads=10):
        self.host = host
        self.profile = profile
        self.max_threads = max_threads
        self.ports = get_profile(profile)
        self.results = {}
        self.lock = threading.Lock()

    def _check_port(self, port):
        """Vérifier un port"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((self.host, port))
            sock.close()
            return result == 0
        except:
            return False

    def scan(self):
        """Lancer le scan"""
        print(f"Profile: {self.profile}")
        print(f"Ports to scan: {len(self.ports)}")
        print("Scanning...\n")

        port_queue = Queue()
        for port in self.ports:
            port_queue.put(port)

        def worker():
            while not port_queue.empty():
                try:
                    port = port_queue.get_nowait()
                    if self._check_port(port):
                        short, long_name, risk = get_service_info(port)
                        with self.lock:
                            self.results[port] = {
                                'service': short,
                                'risk': risk
                            }
                except:
                    pass
                finally:
                    port_queue.task_done()

        threads = []
        for _ in range(min(self.max_threads, len(self.ports))):
            t = threading.Thread(target=worker, daemon=True)
            t.start()
            threads.append(t)

        port_queue.join()

    def report(self):
        """Générer rapport"""
        print("="*60)
        print("OPEN PORTS")
        print("="*60)

        if not self.results:
            print("No open ports found")
            return

        # Trier par port
        for port in sorted(self.results.keys()):
            info = self.results[port]
            service = info['service']
            risk = info['risk']
            mark = " [!]" if risk == "HIGH" else ""
            print(f"Port {port:5d}  [{service:15s}]  Risk: {risk:6s}{mark}")

        # Résumé
        print("\n" + "="*60)
        print("SUMMARY")
        print("="*60)
        print(f"Total open: {len(self.results)}")

        high_risk = [p for p, i in self.results.items() if i['risk'] == 'HIGH']
        if high_risk:
            print(f"High risk ports: {len(high_risk)} *** ALERT ***")

def main():
    print("="*60)
    print("DÉFI 5 : DÉTECTION PORTS ET FILTRAGE")
    print("="*60 + "\n")

    scanner = IntelligentScanner('127.0.0.1', profile='QUICK', max_threads=10)
    scanner.scan()
    scanner.report()

if __name__ == "__main__":
    main()
```
```

Points clés:
- Dictionnaire avec (nom_court, nom_long, risque)
- Profils de scan prédéfinis
- Filtrage intelligent par profil
- Alertes pour ports dangereux

========================================
## Défi 6: VALIDATION D'ENTRÉE ET GESTION D'ERREURS
========================================

Solution:

```python
#!/usr/bin/env python3
"""
Défi 6: Validation d'Entrée et Gestion d'Erreurs Robuste
Production-ready scanner avec validation complète
"""

```python
import socket
import ipaddress

class RobustPortScanner:
    """Scanner avec validation robuste"""

    def __init__(self, host, ports=None, timeout=2, max_threads=10):
        """Initialiser avec validation complète"""
        # Valider host
        self.host = self._validate_host(host)

        # Valider ports
        self.ports = self._validate_ports(ports)

        # Valider timeout
        self.timeout = self._validate_timeout(timeout)

        # Valider max_threads
        self.max_threads = self._validate_max_threads(max_threads)

        self.results = {}

    def _validate_host(self, host):
        """Valider que host est une IP ou hostname valide"""
        # Essayer parse comme IP
        try:
            ipaddress.ip_address(host)
            print(f"[+] Host: {host} (IP)")
            return host
        except ValueError:
            pass

        # Essayer résoudre comme hostname
        try:
            ip = socket.gethostbyname(host)
            print(f"[+] Host: {host} -> {ip}")
            return host
        except socket.gaierror:
            raise ValueError(f"Invalid host: {host}")

    def _validate_ports(self, ports):
        """Valider les ports"""
        if ports is None:
            ports = [22, 80, 443]

        for port in ports:
            if not isinstance(port, int):
                raise ValueError(f"Port must be integer, got {type(port)}")
            if port < 1 or port > 65535:
                raise ValueError(f"Port {port} out of range (1-65535)")

        print(f"[+] Ports: {len(ports)} valid ports")
        return ports

    def _validate_timeout(self, timeout):
        """Valider le timeout"""
        try:
            timeout = float(timeout)
            if timeout < 0.1 or timeout > 30:
                raise ValueError(f"Timeout {timeout} out of range (0.1-30)")
            print(f"[+] Timeout: {timeout} sec")
            return timeout
        except ValueError as e:
            raise ValueError(f"Invalid timeout: {e}")

    def _validate_max_threads(self, max_threads):
        """Valider max_threads"""
        try:
            max_threads = int(max_threads)
            if max_threads < 1 or max_threads > 500:
                raise ValueError(f"Threads {max_threads} out of range (1-500)")
            print(f"[+] Max threads: {max_threads}")
            return max_threads
        except ValueError as e:
            raise ValueError(f"Invalid max_threads: {e}")

    def _check_port(self, port):
        """Vérifier un port"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((self.host, port))
            sock.close()
            return result == 0
        except Exception as e:
            return False

    def scan(self):
        """Lancer le scan"""
        print("\n[*] Starting scan...")
        for port in self.ports:
            if self._check_port(port):
                self.results[port] = True
        print(f"[+] Scan complete: {len(self.results)} open ports")

def main():
    """Tests avec gestion d'erreurs"""
    print("="*60)
    print("DÉFI 6 : VALIDATION ET GESTION D'ERREURS")
    print("="*60 + "\n")

    # Test valide
    print("Test 1: Valid input")
    print("-" * 40)
    try:
        scanner = RobustPortScanner('127.0.0.1', ports=[22, 80, 443])
        scanner.scan()
        print("[+] Success\n")
    except ValueError as e:
        print(f"[!] Error: {e}\n")

    # Test host invalide
    print("Test 2: Invalid host")
    print("-" * 40)
    try:
        scanner = RobustPortScanner('!!!invalid!!!')
    except ValueError as e:
        print(f"[!] Caught error: {e}\n")

    # Test port invalide
    print("Test 3: Port out of range")
    print("-" * 40)
    try:
        scanner = RobustPortScanner('127.0.0.1', ports=[80, 70000])
    except ValueError as e:
        print(f"[!] Caught error: {e}\n")

    # Test timeout invalide
    print("Test 4: Invalid timeout")
    print("-" * 40)
    try:
        scanner = RobustPortScanner('127.0.0.1', timeout=-1)
    except ValueError as e:
        print(f"[!] Caught error: {e}\n")

if __name__ == "__main__":
    main()
```
```

Points clés:
- ipaddress.ip_address() pour valider IPs
- socket.gethostbyname() pour valider hostnames
- Vérifier les ranges (ports, timeout, threads)
- Levée d'exception avec messages clairs
- Logging de chaque validation

========================================
## Défi 7: RAPPORTS PROFESSIONNEL ET EXPORTS
========================================

Solution:

```python
#!/usr/bin/env python3
"""
Défi 7: Rapports Professionnel et Exports Multiples
Générer des rapports en plusieurs formats
"""

```python
import socket
import json
import csv
import time
from datetime import datetime

class ReportGenerator:
    """Générateur de rapports"""

    def __init__(self, host, results, scan_time):
        self.host = host
        self.results = results
        self.scan_time = scan_time

    def format_text(self):
        """Générer rapport texte"""
        lines = []
        lines.append("="*70)
        lines.append("PORT SCANNER REPORT")
        lines.append("="*70)
        lines.append(f"Generated: {datetime.now().isoformat()}")
        lines.append(f"Target: {self.host}")
        lines.append(f"Scan Duration: {self.scan_time:.2f} seconds")
        lines.append(f"Scan Rate: {len(self.results)/self.scan_time:.1f} ports/sec")
        lines.append("")

        if self.results:
            lines.append("Port    Service       State       Banner")
            lines.append("-"*70)
            for port, info in sorted(self.results.items()):
                service = info['service']
                state = "OPEN"
                banner = info.get('banner', '(none)')
                if len(banner) > 45:
                    banner = banner[:42] + "..."
                lines.append(f"{port:5d}   {service:15s} {state:10s} {banner}")
        else:
            lines.append("No open ports found")

        lines.append("="*70)
        return "\n".join(lines)

    def format_csv(self):
        """Générer CSV"""
        lines = []
        lines.append("Port,Service,State,Banner")

        for port, info in sorted(self.results.items()):
            service = info['service']
            banner = info.get('banner', '').replace('"', '""')
            lines.append(f'{port},"{service}","OPEN","{banner}"')

        return "\n".join(lines)

    def format_json(self):
        """Générer JSON"""
        data = {
            'metadata': {
                'target': self.host,
                'timestamp': datetime.now().isoformat(),
                'scan_time': self.scan_time,
            },
            'results': [],
            'statistics': {
                'total_open': len(self.results),
            }
        }

        for port, info in sorted(self.results.items()):
            data['results'].append({
                'port': port,
                'service': info['service'],
                'state': 'OPEN',
                'banner': info.get('banner'),
            })

        return json.dumps(data, indent=2)

    def generate_file(self, filename, format='text'):
        """Générer et sauvegarder un fichier"""
        if format == 'text':
            content = self.format_text()
        elif format == 'csv':
            content = self.format_csv()
        elif format == 'json':
            content = self.format_json()
        else:
            raise ValueError(f"Unknown format: {format}")

        with open(filename, 'w') as f:
            f.write(content)

        print(f"[+] Report saved to: {filename}")

def main():
    print("="*60)
    print("DÉFI 7 : RAPPORTS ET EXPORTS")
    print("="*60 + "\n")

    # Résultats de test
    results = {
        22: {'service': 'SSH', 'banner': 'SSH-2.0-OpenSSH_7.4'},
        80: {'service': 'HTTP', 'banner': 'HTTP/1.1 200 OK'},
        443: {'service': 'HTTPS', 'banner': None},
    }

    generator = ReportGenerator('192.168.1.100', results, 5.23)

    # Afficher en texte
    print("TEXT FORMAT:")
    print(generator.format_text())

    print("\n\nCSV FORMAT:")
    print(generator.format_csv())

    print("\n\nJSON FORMAT:")
    print(generator.format_json())

if __name__ == "__main__":
    main()
```
```

Points clés:
- Méthodes format_* pour chaque type
- json.dumps(indent=2) pour JSON lisible
- csv.writer() ou formatage manuel
- datetime.isoformat() pour dates standards
- Méthode generate_file() pour sauvegarder

========================================
## Défi 8: SCANNER PROFESSIONNEL COMPLET
========================================

Solution (version allégée - concept):

```python
#!/usr/bin/env python3
"""
Défi 8: Scanner Professionnel Complet
Outil production-ready combinant tous les concepts
"""

```python
import socket
import threading
import json
import time
import ipaddress
from queue import Queue
from datetime import datetime

```
SERVICES = {
```python
    22: 'SSH', 80: 'HTTP', 443: 'HTTPS', 3306: 'MySQL',
    5432: 'PostgreSQL', 6379: 'Redis', 8080: 'HTTP-ALT',
```
}

```python
class ServiceDetector:
    """Détection de services"""

    @staticmethod
    def get_service(port):
        return SERVICES.get(port, 'Unknown')

class Scanner:
    """Core scanning engine"""

    def __init__(self, host, timeout=2, max_threads=10):
        self.host = self._validate_host(host)
        self.timeout = timeout
        self.max_threads = max_threads
        self.results = {}
        self.lock = threading.Lock()

    def _validate_host(self, host):
        try:
            ipaddress.ip_address(host)
        except ValueError:
            socket.gethostbyname(host)
        return host

    def _scan_port(self, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((self.host, port))
            sock.close()

            if result == 0:
                banner = None
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(0.5)
                    sock.connect((self.host, port))
                    banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
                    sock.close()
                except:
                    pass

                with self.lock:
                    self.results[port] = {
                        'service': ServiceDetector.get_service(port),
                        'banner': banner
                    }
        except:
            pass

    def scan(self, ports):
        port_queue = Queue()
        for port in ports:
            port_queue.put(port)

        def worker():
            while not port_queue.empty():
                try:
                    port = port_queue.get_nowait()
                    self._scan_port(port)
                except:
                    pass
                finally:
                    port_queue.task_done()

        threads = []
        for _ in range(min(self.max_threads, len(ports))):
            t = threading.Thread(target=worker, daemon=True)
            t.start()
            threads.append(t)

        port_queue.join()
        return self.results

class ReportGenerator:
    """Génération de rapports"""

    def __init__(self, host, results, scan_time, ports_scanned):
        self.host = host
        self.results = results
        self.scan_time = scan_time
        self.ports_scanned = ports_scanned

    def generate_text(self):
        report = []
        report.append("="*70)
        report.append("PROFESSIONAL PORT SCANNER REPORT")
        report.append("="*70)
        report.append(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"Target: {self.host}")
        report.append(f"Ports Scanned: {self.ports_scanned}")
        report.append(f"Ports Found: {len(self.results)}")
        report.append(f"Scan Duration: {self.scan_time:.2f} seconds")
        report.append(f"Scan Rate: {self.ports_scanned/self.scan_time:.1f} ports/sec")
        report.append("")

        if self.results:
            report.append("Port    Service         Banner")
            report.append("-"*70)
            for port in sorted(self.results.keys()):
                info = self.results[port]
                service = info['service']
                banner = info['banner'] if info['banner'] else "(none)"
                if len(banner) > 45:
                    banner = banner[:42] + "..."
                report.append(f"{port:5d}   {service:15s} {banner}")
        else:
            report.append("No open ports found")

        report.append("="*70)
        return "\n".join(report)

    def generate_json(self):
        return json.dumps({
            'target': self.host,
            'timestamp': datetime.now().isoformat(),
            'scan_time': self.scan_time,
            'ports_scanned': self.ports_scanned,
            'open_ports': len(self.results),
            'results': [
                {
                    'port': port,
                    'service': info['service'],
                    'banner': info['banner']
                }
                for port, info in sorted(self.results.items())
            ]
        }, indent=2)

def main():
    """Programme principal"""
    print("="*70)
    print("PROFESSIONAL PORT SCANNER v1.0")
    print("="*70)

    # Paramètres
    host = '127.0.0.1'
    ports = [20, 21, 22, 25, 53, 80, 110, 143, 443, 445,
             3306, 5432, 6379, 8080, 27017]

    print(f"\n[*] Scanning {host}")
    print(f"[*] Ports: {len(ports)}")
    print(f"[*] Starting scan...\n")

    # Lancer le scan
    start_time = time.time()
    scanner = Scanner(host, timeout=1, max_threads=10)
    results = scanner.scan(ports)
    scan_time = time.time() - start_time

    # Générer le rapport
    generator = ReportGenerator(host, results, scan_time, len(ports))

    # Afficher résultats
    print(generator.generate_text())

    # Sauvegarder en JSON
    with open('scan_results.json', 'w') as f:
        f.write(generator.generate_json())
    print(f"\n[+] Results saved to: scan_results.json")

if __name__ == "__main__":
    main()
```
```

Points clés:
- Architecture modulaire avec classes séparées
- Scanner, ServiceDetector, ReportGenerator
- Validation d'entrée robuste
- Gestion d'erreurs complète
- Support de multiples formats de rapport
- Logging et debugging
- Production-ready

========================================
TIPS ET TRICKS
========================================

1. Performance:
   - Utiliser timeout court (0.5-1s) pour scanning rapide
   - Augmenter threads jusqu'à 50-100 pour gros scans
   - Attention: trop de threads = DoS accidentel

2. Précision:
   - Banner grabbing améliore l'identification
   - Combiner multiple techniques pour confirmation
   - Vérifier les ports ouverts plusieurs fois si incertain

3. Debugging:
   - Ajouter prints pour tracking progress
   - Tester avec localhost d'abord
   - Vérifier timeouts avec 'sleep' command

4. Sécurité:
   - JAMAIS sans autorisation
   - Respecter rate limiting
   - Documenter les scans
   - Utiliser dans environnement légal

5. Optimisation:
   - Cacher les resultats courants
   - Utiliser pool de sockets réutilisables
   - Combiner scans rapides + détaillés
   - Paralléliser les tâches post-scan

========================================
ERREURS COURANTES À ÉVITER
========================================

1. Oublier de fermer les sockets
   - MAUVAIS: sock = socket.socket(...)
   - BON: sock.close() TOUJOURS

2. Pas de timeout
   - MAUVAIS: peut bloquer indéfiniment
   - BON: socket.settimeout(2)

3. Pas de gestion d'exception
   - MAUVAIS: crash si host invalide
   - BON: try/except partout

4. Banner grabbing sans timeout court
   - MAUVAIS: peut bloquer 2+ secondes
   - BON: timeout séparé pour banner (0.5s)

5. Trop de threads
   - MAUVAIS: 1000 threads = DoS accidentel
   - BON: limiter à 50 max

6. Shell=True (si utilisé)
   - MAUVAIS: vulnérable à injection
   - BON: pas de shell du tout, socket direct

========================================
RESSOURCES SUPPLÉMENTAIRES
========================================

- Python socket docs: https://docs.python.org/3/library/socket.html
- RFC 793 (TCP): https://tools.ietf.org/html/rfc793
- nmap man page: https://linux.die.net/man/1/nmap
- Scapy docs: https://scapy.readthedocs.io/
