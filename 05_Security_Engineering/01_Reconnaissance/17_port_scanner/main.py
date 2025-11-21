#!/usr/bin/env python3
"""
Port Scanner - Red Teaming Tool
Exercice 17 : Scanning de ports TCP avec multi-threading et banner grabbing

AVERTISSEMENT LÉGAL :
Ce code est fourni UNIQUEMENT à des fins éducatives et de tests de sécurité
autorisés. Le scanning de ports sans autorisation explicite est ILLÉGAL.
Utilisez uniquement sur vos propres systèmes ou avec permission écrite.
"""

import socket
import threading
from queue import Queue
from datetime import datetime
import json
import csv
import sys
import time


# ============================================================================
# PARTIE 1 : SCANNER DE PORTS SIMPLE
# ============================================================================

def scan_port_simple(host, port, timeout=1):
    """
    Scan basique d'un seul port TCP

    Args:
        host: Adresse IP ou hostname de la cible
        port: Numéro de port à scanner
        timeout: Délai d'attente en secondes

    Returns:
        True si le port est ouvert, False sinon
    """
    try:
        # Créer un socket TCP/IP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Définir le timeout pour éviter les blocages
        sock.settimeout(timeout)

        # Tenter la connexion (connect_ex retourne 0 si succès)
        result = sock.connect_ex((host, port))

        # Fermer le socket
        sock.close()

        # Retourner True si connexion réussie (port ouvert)
        return result == 0

    except socket.gaierror:
        # Erreur de résolution DNS
        print(f"[!] Erreur : Impossible de résoudre le hostname {host}")
        return False
    except socket.error:
        # Erreur de connexion réseau
        return False


def scan_ports_range(host, start_port, end_port, timeout=1):
    """
    Scanner une plage de ports de manière séquentielle

    Args:
        host: Cible à scanner
        start_port: Port de début
        end_port: Port de fin (inclus)
        timeout: Timeout par connexion

    Returns:
        Liste des ports ouverts
    """
    print(f"\n[*] Scan de {host} : ports {start_port}-{end_port}")
    print(f"[*] Début du scan : {datetime.now().strftime('%H:%M:%S')}\n")

    open_ports = []

    # Scanner chaque port dans la plage
    for port in range(start_port, end_port + 1):
        if scan_port_simple(host, port, timeout):
            print(f"[+] Port {port} : OUVERT")
            open_ports.append(port)

    print(f"\n[*] Scan terminé : {datetime.now().strftime('%H:%M:%S')}")
    print(f"[*] Ports ouverts trouvés : {len(open_ports)}")

    return open_ports


# ============================================================================
# PARTIE 2 : SCANNER MULTI-THREADÉ
# ============================================================================

class ThreadedScanner:
    """
    Scanner de ports utilisant le multi-threading pour performance accrue
    """

    def __init__(self, host, timeout=1, num_threads=100):
        """
        Initialiser le scanner threadé

        Args:
            host: Cible à scanner
            timeout: Timeout par connexion
            num_threads: Nombre de threads workers
        """
        self.host = host
        self.timeout = timeout
        self.num_threads = num_threads
        self.open_ports = []
        self.lock = threading.Lock()  # Pour synchroniser l'accès à open_ports
        self.queue = Queue()  # File d'attente des ports à scanner

    def scan_port(self, port):
        """
        Scanner un port individuel (méthode worker)

        Args:
            port: Numéro de port à scanner
        """
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((self.host, port))
            sock.close()

            # Si port ouvert, l'ajouter à la liste (avec lock pour thread-safety)
            if result == 0:
                with self.lock:
                    self.open_ports.append(port)
                    print(f"[+] Port {port} : OUVERT")

        except socket.error:
            pass

    def worker(self):
        """
        Thread worker qui récupère et scanne les ports de la queue
        """
        while True:
            # Récupérer un port de la queue
            port = self.queue.get()

            # Scanner le port
            self.scan_port(port)

            # Marquer la tâche comme terminée
            self.queue.task_done()

    def scan(self, ports):
        """
        Lancer le scan multi-threadé sur une liste de ports

        Args:
            ports: Liste ou range de ports à scanner

        Returns:
            Liste triée des ports ouverts
        """
        print(f"\n[*] Scan multi-threadé de {self.host}")
        print(f"[*] Threads : {self.num_threads}")
        print(f"[*] Ports à scanner : {len(ports)}")
        print(f"[*] Début : {datetime.now().strftime('%H:%M:%S')}\n")

        start_time = time.time()

        # Ajouter tous les ports à la queue
        for port in ports:
            self.queue.put(port)

        # Créer et démarrer les threads workers
        for _ in range(self.num_threads):
            thread = threading.Thread(target=self.worker, daemon=True)
            thread.start()

        # Attendre que tous les ports soient scannés
        self.queue.join()

        # Calculer le temps écoulé
        elapsed = time.time() - start_time

        print(f"\n[*] Scan terminé : {datetime.now().strftime('%H:%M:%S')}")
        print(f"[*] Temps écoulé : {elapsed:.2f} secondes")
        print(f"[*] Ports ouverts : {len(self.open_ports)}")

        # Retourner les ports triés
        return sorted(self.open_ports)


# ============================================================================
# PARTIE 3 : BANNER GRABBING
# ============================================================================

def grab_banner(host, port, timeout=2):
    """
    Récupérer la bannière d'un service sur un port

    Args:
        host: Cible
        port: Port du service
        timeout: Timeout de connexion

    Returns:
        Bannière (string) ou None si échec
    """
    try:
        # Créer le socket et se connecter
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((host, port))

        # Certains services envoient une bannière automatiquement
        # D'autres nécessitent une requête
        try:
            banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
        except:
            # Si rien reçu, essayer d'envoyer une requête générique
            sock.send(b'\r\n')
            banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()

        sock.close()
        return banner if banner else None

    except:
        return None


def grab_banner_http(host, port, timeout=2):
    """
    Récupérer la bannière HTTP avec requête GET

    Args:
        host: Cible
        port: Port HTTP
        timeout: Timeout

    Returns:
        Bannière HTTP ou None
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((host, port))

        # Envoyer une requête HTTP GET basique
        request = f"GET / HTTP/1.1\r\nHost: {host}\r\n\r\n"
        sock.send(request.encode())

        # Récupérer la réponse
        response = sock.recv(4096).decode('utf-8', errors='ignore')
        sock.close()

        # Extraire la première ligne (status) et le header Server
        lines = response.split('\r\n')
        status = lines[0] if lines else ""
        server = ""

        for line in lines:
            if line.lower().startswith('server:'):
                server = line.split(':', 1)[1].strip()
                break

        return f"{status} | Server: {server}" if server else status

    except:
        return None


# ============================================================================
# PARTIE 4 : DÉTECTION DE SERVICES
# ============================================================================

# Mapping des ports standards vers services connus
COMMON_PORTS = {
    20: "FTP-DATA",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    993: "IMAPS",
    995: "POP3S",
    1433: "MSSQL",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    5900: "VNC",
    6379: "Redis",
    8080: "HTTP-Proxy",
    8443: "HTTPS-Alt",
    27017: "MongoDB"
}


def identify_service(port):
    """
    Identifier le service standard pour un port donné

    Args:
        port: Numéro de port

    Returns:
        Nom du service ou "Unknown"
    """
    return COMMON_PORTS.get(port, "Unknown")


class ServiceScanner:
    """
    Scanner avancé avec détection de services et banner grabbing
    """

    def __init__(self, host, timeout=2):
        """
        Initialiser le scanner de services

        Args:
            host: Cible à scanner
            timeout: Timeout des connexions
        """
        self.host = host
        self.timeout = timeout
        self.results = []

    def scan_port_with_service(self, port):
        """
        Scanner un port et identifier le service

        Args:
            port: Port à scanner

        Returns:
            Dict avec infos du port ou None si fermé
        """
        # Vérifier si le port est ouvert
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((self.host, port))
            sock.close()

            if result != 0:
                return None

        except:
            return None

        # Port ouvert : récupérer les infos
        service_name = identify_service(port)
        banner = None

        # Tenter le banner grabbing selon le type de service
        if port in [80, 8080, 8000, 8443]:
            banner = grab_banner_http(self.host, port, self.timeout)
        else:
            banner = grab_banner(self.host, port, self.timeout)

        return {
            'port': port,
            'state': 'open',
            'service': service_name,
            'banner': banner
        }

    def scan(self, ports):
        """
        Scanner une liste de ports avec détection de services

        Args:
            ports: Liste de ports à scanner

        Returns:
            Liste de résultats (dicts)
        """
        print(f"\n[*] Scan de services sur {self.host}")
        print(f"[*] Début : {datetime.now().strftime('%H:%M:%S')}\n")

        self.results = []

        for port in ports:
            result = self.scan_port_with_service(port)
            if result:
                self.results.append(result)
                banner_info = f" | {result['banner']}" if result['banner'] else ""
                print(f"[+] Port {port:5d} : {result['service']:15s}{banner_info}")

        print(f"\n[*] Scan terminé : {datetime.now().strftime('%H:%M:%S')}")
        print(f"[*] Services trouvés : {len(self.results)}")

        return self.results

    def display_results(self):
        """
        Afficher les résultats formatés
        """
        if not self.results:
            print("\n[!] Aucun port ouvert trouvé")
            return

        print("\n" + "="*80)
        print(f"RÉSULTATS DU SCAN - {self.host}")
        print("="*80)
        print(f"{'PORT':<10} {'SERVICE':<20} {'BANNIÈRE'}")
        print("-"*80)

        for result in self.results:
            banner = result['banner'][:50] if result['banner'] else "N/A"
            print(f"{result['port']:<10} {result['service']:<20} {banner}")

        print("="*80)

    def export_json(self, filename):
        """
        Exporter les résultats en JSON

        Args:
            filename: Nom du fichier de sortie
        """
        data = {
            'target': self.host,
            'scan_time': datetime.now().isoformat(),
            'results': self.results
        }

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print(f"\n[*] Résultats exportés vers {filename}")

    def export_csv(self, filename):
        """
        Exporter les résultats en CSV

        Args:
            filename: Nom du fichier de sortie
        """
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['port', 'state', 'service', 'banner'])
            writer.writeheader()
            writer.writerows(self.results)

        print(f"[*] Résultats exportés vers {filename}")


# ============================================================================
# PARTIE 5 : EXEMPLES D'UTILISATION
# ============================================================================

def exemple_scan_simple():
    """
    Exemple 1 : Scanner simple de ports communs
    """
    print("\n" + "="*80)
    print("EXEMPLE 1 : SCAN SIMPLE")
    print("="*80)

    host = "127.0.0.1"  # localhost
    ports_communs = [21, 22, 23, 25, 80, 443, 3306, 8080]

    print(f"\n[*] Scan des ports communs sur {host}")

    for port in ports_communs:
        if scan_port_simple(host, port):
            service = identify_service(port)
            print(f"[+] Port {port} ({service}) : OUVERT")


def exemple_scan_threaded():
    """
    Exemple 2 : Scan multi-threadé rapide
    """
    print("\n" + "="*80)
    print("EXEMPLE 2 : SCAN MULTI-THREADÉ")
    print("="*80)

    host = "127.0.0.1"

    # Scanner les 1024 premiers ports (well-known ports)
    scanner = ThreadedScanner(host, timeout=0.5, num_threads=50)
    open_ports = scanner.scan(range(1, 1025))

    if open_ports:
        print(f"\n[*] Ports ouverts : {open_ports}")


def exemple_service_detection():
    """
    Exemple 3 : Détection de services avec banner grabbing
    """
    print("\n" + "="*80)
    print("EXEMPLE 3 : DÉTECTION DE SERVICES")
    print("="*80)

    host = "127.0.0.1"
    ports_a_scanner = [21, 22, 25, 80, 443, 3306, 5432, 8080]

    scanner = ServiceScanner(host, timeout=2)
    results = scanner.scan(ports_a_scanner)
    scanner.display_results()

    # Exporter les résultats
    if results:
        scanner.export_json("scan_results.json")
        scanner.export_csv("scan_results.csv")


def exemple_scan_complet():
    """
    Exemple 4 : Scan complet avec toutes les fonctionnalités
    """
    print("\n" + "="*80)
    print("EXEMPLE 4 : SCAN COMPLET PROFESSIONNEL")
    print("="*80)

    # Configuration
    host = "127.0.0.1"

    # Étape 1 : Scan rapide des ports communs
    print("\n[ÉTAPE 1] Scan rapide des ports bien connus...")
    common_ports = list(COMMON_PORTS.keys())

    threaded_scanner = ThreadedScanner(host, timeout=1, num_threads=20)
    open_ports = threaded_scanner.scan(common_ports)

    # Étape 2 : Identification détaillée des services trouvés
    if open_ports:
        print("\n[ÉTAPE 2] Identification détaillée des services...")
        service_scanner = ServiceScanner(host, timeout=2)
        results = service_scanner.scan(open_ports)
        service_scanner.display_results()

        # Étape 3 : Export des résultats
        print("\n[ÉTAPE 3] Export des résultats...")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        service_scanner.export_json(f"scan_{host}_{timestamp}.json")
        service_scanner.export_csv(f"scan_{host}_{timestamp}.csv")
    else:
        print("\n[!] Aucun port ouvert trouvé dans les ports communs")


def menu_interactif():
    """
    Menu interactif pour choisir le type de scan
    """
    print("\n" + "="*80)
    print("PORT SCANNER - MENU INTERACTIF")
    print("="*80)
    print("\nAVERTISSEMENT : Utilisez uniquement sur vos propres systèmes")
    print("              ou avec autorisation écrite explicite.\n")
    print("Options :")
    print("1. Scan simple de ports communs")
    print("2. Scan multi-threadé rapide")
    print("3. Scan avec détection de services")
    print("4. Scan complet professionnel")
    print("5. Scan personnalisé")
    print("0. Quitter")

    try:
        choix = input("\nVotre choix : ").strip()

        if choix == "1":
            exemple_scan_simple()
        elif choix == "2":
            exemple_scan_threaded()
        elif choix == "3":
            exemple_service_detection()
        elif choix == "4":
            exemple_scan_complet()
        elif choix == "5":
            scan_personnalise()
        elif choix == "0":
            print("\n[*] Au revoir !")
            sys.exit(0)
        else:
            print("\n[!] Choix invalide")

    except KeyboardInterrupt:
        print("\n\n[!] Scan interrompu par l'utilisateur")
        sys.exit(0)


def scan_personnalise():
    """
    Permettre à l'utilisateur de configurer un scan personnalisé
    """
    print("\n" + "="*80)
    print("SCAN PERSONNALISÉ")
    print("="*80)

    try:
        # Demander la cible
        host = input("\nCible (IP ou hostname) : ").strip()
        if not host:
            host = "127.0.0.1"

        # Demander le type de scan
        print("\nType de scan :")
        print("1. Ports communs uniquement")
        print("2. Plage personnalisée")
        print("3. Liste de ports spécifiques")

        type_scan = input("Choix : ").strip()

        if type_scan == "1":
            ports = list(COMMON_PORTS.keys())
        elif type_scan == "2":
            start = int(input("Port de début : "))
            end = int(input("Port de fin : "))
            ports = range(start, end + 1)
        elif type_scan == "3":
            ports_str = input("Ports séparés par des virgules : ")
            ports = [int(p.strip()) for p in ports_str.split(',')]
        else:
            print("[!] Choix invalide, utilisation des ports communs")
            ports = list(COMMON_PORTS.keys())

        # Demander si détection de services
        detect_services = input("\nDétection de services ? (o/n) : ").strip().lower() == 'o'

        # Lancer le scan
        if detect_services:
            scanner = ServiceScanner(host, timeout=2)
            results = scanner.scan(ports)
            scanner.display_results()

            if results and input("\nExporter les résultats ? (o/n) : ").strip().lower() == 'o':
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                scanner.export_json(f"scan_{host}_{timestamp}.json")
                scanner.export_csv(f"scan_{host}_{timestamp}.csv")
        else:
            scanner = ThreadedScanner(host, timeout=1, num_threads=50)
            open_ports = scanner.scan(ports)
            if open_ports:
                print(f"\n[*] Ports ouverts : {open_ports}")

    except KeyboardInterrupt:
        print("\n\n[!] Scan interrompu")
    except ValueError:
        print("\n[!] Erreur : Entrée invalide")
    except Exception as e:
        print(f"\n[!] Erreur : {e}")


# ============================================================================
# POINT D'ENTRÉE PRINCIPAL
# ============================================================================

def main():
    """
    Fonction principale
    """
    # Afficher l'avertissement légal
    print("\n" + "="*80)
    print("PORT SCANNER - OUTIL DE RECONNAISSANCE RÉSEAU")
    print("="*80)
    print("\nAVERTISSEMENT LÉGAL")
    print("\nCe programme est fourni UNIQUEMENT à des fins éducatives.")
    print("Le scanning de ports sans autorisation est ILLÉGAL.")
    print("\nUtilisations autorisées :")
    print("  - Vos propres systèmes et réseaux")
    print("  - Tests de pénétration avec accord écrit")
    print("  - Environnements de laboratoire personnels")
    print("\nL'utilisateur est seul responsable de l'usage de cet outil.")
    print("="*80)

    confirmation = input("\nJ'ai compris et j'utilise cet outil légalement (oui/non) : ")

    if confirmation.lower() not in ['oui', 'o', 'yes', 'y']:
        print("\n[!] Utilisation annulée")
        sys.exit(0)

    # Lancer le menu interactif
    while True:
        menu_interactif()

        if input("\nAutre scan ? (o/n) : ").strip().lower() != 'o':
            print("\n[*] Au revoir !")
            break


if __name__ == "__main__":
    main()
