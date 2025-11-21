#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Exercice 14 - Sockets TCP
Concepts : module socket, protocole TCP/IP, client/serveur, reconnaissance réseau

AVERTISSEMENT ÉTHIQUE :
Ce code est fourni uniquement à des fins éducatives et de sécurité défensive.
L'utilisation de ces techniques contre des systèmes sans autorisation écrite
explicite est ILLÉGALE. Utilisez uniquement sur vos propres systèmes ou avec
une autorisation formelle.
"""

import socket
import sys
import threading
import time
from datetime import datetime

# ============================================================================
# PARTIE 1 : CRÉATION DE SOCKETS
# ============================================================================

def exemple_creation_socket():
    """
    Démonstration de la création de différents types de sockets.
    """
    print("\n=== CRÉATION DE SOCKETS ===\n")

    # Socket TCP/IPv4 (le plus courant)
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket TCP/IPv4 créé")
    print(f"Type : {tcp_socket.type}")
    print(f"Famille : {tcp_socket.family}")
    tcp_socket.close()

    # Socket UDP/IPv4
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("\nSocket UDP/IPv4 créé")
    print(f"Type : {udp_socket.type}")
    udp_socket.close()

    # Socket TCP/IPv6
    try:
        tcp6_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        print("\nSocket TCP/IPv6 créé")
        tcp6_socket.close()
    except OSError as e:
        print(f"\nIPv6 non disponible : {e}")

    # Utilisation du context manager (recommandé)
    print("\n--- Utilisation avec context manager ---")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        print("Socket créé et sera fermé automatiquement")
        print(f"Socket : {sock}")

    print("\nSocket fermé automatiquement après le bloc with")


# ============================================================================
# PARTIE 2 : CLIENT TCP
# ============================================================================

def exemple_client_tcp_simple():
    """
    Client TCP basique qui se connecte à un serveur web.
    """
    print("\n=== CLIENT TCP SIMPLE ===\n")

    # Création du socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Configuration du timeout (évite de bloquer indéfiniment)
        client.settimeout(5)

        print("Connexion à example.com sur le port 80...")

        # Connexion au serveur
        client.connect(("example.com", 80))
        print("Connecté avec succès !")

        # Préparation de la requête HTTP
        request = "GET / HTTP/1.1\r\n"
        request += "Host: example.com\r\n"
        request += "Connection: close\r\n"
        request += "\r\n"

        # Envoi de la requête
        print(f"\nEnvoi de la requête :\n{request}")
        client.sendall(request.encode('utf-8'))

        # Réception de la réponse
        print("\nRéception de la réponse...\n")
        response = b""

        while True:
            chunk = client.recv(4096)
            if not chunk:  # Connexion fermée par le serveur
                break
            response += chunk

        # Affichage des premiers 500 caractères
        response_text = response.decode('utf-8', errors='ignore')
        print(response_text[:500])
        print(f"\n... (Total : {len(response)} octets reçus)")

    except socket.timeout:
        print("ERREUR : Timeout de connexion")
    except socket.error as e:
        print(f"ERREUR socket : {e}")
    except Exception as e:
        print(f"ERREUR : {e}")
    finally:
        # Fermeture du socket
        client.close()
        print("\nSocket fermé")


def client_tcp_personnalise(host, port, message):
    """
    Client TCP générique pour envoyer un message et recevoir une réponse.

    Args:
        host (str): Adresse IP ou nom de domaine
        port (int): Numéro de port
        message (str): Message à envoyer

    Returns:
        str: Réponse du serveur ou None en cas d'erreur
    """
    try:
        # Création et configuration du socket
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(5)

        # Connexion
        client.connect((host, port))

        # Envoi du message
        if isinstance(message, str):
            message = message.encode('utf-8')
        client.sendall(message)

        # Réception de la réponse
        response = client.recv(4096)

        # Fermeture
        client.close()

        return response.decode('utf-8', errors='ignore')

    except socket.timeout:
        return None
    except socket.error:
        return None
    except Exception:
        return None


# ============================================================================
# PARTIE 3 : SERVEUR TCP
# ============================================================================

def exemple_serveur_tcp_simple():
    """
    Serveur TCP basique qui accepte une connexion et renvoie un message.
    """
    print("\n=== SERVEUR TCP SIMPLE ===\n")

    # Création du socket serveur
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Option pour réutiliser immédiatement l'adresse
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        # Liaison à l'adresse et au port
        host = "127.0.0.1"  # Localhost
        port = 9999

        print(f"Liaison du serveur à {host}:{port}...")
        server.bind((host, port))

        # Mise en écoute (max 5 connexions en attente)
        server.listen(5)
        print(f"Serveur en écoute sur {host}:{port}")
        print("En attente de connexion...\n")

        # Acceptation d'une connexion
        client_socket, client_address = server.accept()
        print(f"Connexion reçue de {client_address[0]}:{client_address[1]}")

        # Réception des données
        data = client_socket.recv(1024)
        print(f"Données reçues : {data.decode('utf-8', errors='ignore')}")

        # Envoi d'une réponse
        response = "Message reçu par le serveur !"
        client_socket.sendall(response.encode('utf-8'))
        print(f"Réponse envoyée : {response}")

        # Fermeture de la connexion client
        client_socket.close()
        print("Connexion client fermée")

    except socket.error as e:
        print(f"ERREUR serveur : {e}")
    except KeyboardInterrupt:
        print("\nArrêt du serveur...")
    finally:
        # Fermeture du socket serveur
        server.close()
        print("Serveur fermé")


def serveur_tcp_multi_clients(host, port):
    """
    Serveur TCP qui gère plusieurs clients séquentiellement.

    Args:
        host (str): Adresse d'écoute
        port (int): Port d'écoute
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server.bind((host, port))
        server.listen(5)
        print(f"[*] Serveur en écoute sur {host}:{port}")

        while True:
            # Acceptation d'une nouvelle connexion
            client_socket, client_address = server.accept()
            print(f"\n[+] Client connecté : {client_address[0]}:{client_address[1]}")

            try:
                # Réception des données
                data = client_socket.recv(1024)

                if data:
                    message = data.decode('utf-8', errors='ignore')
                    print(f"[>] Message reçu : {message}")

                    # Traitement et réponse
                    response = f"Echo: {message}"
                    client_socket.sendall(response.encode('utf-8'))
                    print(f"[<] Réponse envoyée")

            except Exception as e:
                print(f"[!] Erreur avec le client : {e}")
            finally:
                client_socket.close()
                print(f"[-] Client déconnecté")

    except KeyboardInterrupt:
        print("\n[*] Arrêt du serveur...")
    finally:
        server.close()


# ============================================================================
# PARTIE 4 : BANNER GRABBING
# ============================================================================

def grab_banner(target_ip, target_port, timeout=3):
    """
    Récupère le banner d'un service réseau.

    Args:
        target_ip (str): Adresse IP de la cible
        target_port (int): Port du service
        timeout (int): Timeout en secondes

    Returns:
        str: Banner du service ou None
    """
    try:
        # Création du socket avec timeout
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)

        # Connexion
        sock.connect((target_ip, target_port))

        # Certains services envoient automatiquement leur banner
        banner = sock.recv(1024)

        # Si aucun banner automatique, envoyer une requête vide
        if not banner:
            sock.send(b"\r\n")
            banner = sock.recv(1024)

        sock.close()

        return banner.decode('utf-8', errors='ignore').strip()

    except socket.timeout:
        return None
    except socket.error:
        return None
    except Exception:
        return None


def exemple_banner_grabbing():
    """
    Démonstration du banner grabbing sur des services courants.
    """
    print("\n=== BANNER GRABBING ===\n")

    # Services publics à tester (avec permission)
    services = [
        ("scanme.nmap.org", 22, "SSH"),      # SSH
        ("scanme.nmap.org", 80, "HTTP"),     # HTTP
    ]

    print("AVERTISSEMENT : Test uniquement sur scanme.nmap.org (autorisé)")
    print("Ne jamais scanner des cibles sans autorisation !\n")

    for host, port, service_name in services:
        print(f"--- {service_name} ({host}:{port}) ---")
        banner = grab_banner(host, port)

        if banner:
            print(f"Banner trouvé :\n{banner}\n")
        else:
            print("Aucun banner reçu ou service fermé\n")

        time.sleep(1)  # Délai entre les requêtes (politesse)


def banner_grabbing_avance(target_ip, target_port):
    """
    Banner grabbing avancé avec détection du type de service.

    Args:
        target_ip (str): Adresse IP cible
        target_port (int): Port cible

    Returns:
        dict: Informations sur le service
    """
    result = {
        "ip": target_ip,
        "port": target_port,
        "banner": None,
        "service": "unknown",
        "status": "closed"
    }

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        sock.connect((target_ip, target_port))

        result["status"] = "open"

        # Réception du banner
        banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()

        if banner:
            result["banner"] = banner

            # Détection basique du service
            if "SSH" in banner:
                result["service"] = "SSH"
            elif "FTP" in banner:
                result["service"] = "FTP"
            elif "SMTP" in banner:
                result["service"] = "SMTP"
            elif "HTTP" in banner or "200 OK" in banner:
                result["service"] = "HTTP"

        sock.close()

    except socket.timeout:
        result["status"] = "filtered"
    except socket.error:
        result["status"] = "closed"

    return result


# ============================================================================
# PARTIE 5 : SCANNER DE PORTS
# ============================================================================

def scan_port(target_ip, target_port, timeout=1):
    """
    Vérifie si un port est ouvert sur une cible.

    Args:
        target_ip (str): Adresse IP cible
        target_port (int): Port à scanner
        timeout (float): Timeout en secondes

    Returns:
        bool: True si le port est ouvert
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)

        # connect_ex() retourne 0 si la connexion réussit
        result = sock.connect_ex((target_ip, target_port))

        sock.close()

        return result == 0

    except:
        return False


def scanner_ports_simple(target_ip, start_port, end_port):
    """
    Scanner de ports TCP basique.

    Args:
        target_ip (str): Adresse IP à scanner
        start_port (int): Port de départ
        end_port (int): Port de fin
    """
    print(f"\n=== SCANNER DE PORTS ===\n")
    print(f"Cible : {target_ip}")
    print(f"Ports : {start_port}-{end_port}\n")

    open_ports = []

    print("Scan en cours...\n")
    start_time = time.time()

    for port in range(start_port, end_port + 1):
        if scan_port(target_ip, port, timeout=0.5):
            print(f"[+] Port {port} OUVERT")
            open_ports.append(port)

    end_time = time.time()

    print(f"\n--- Résultats ---")
    print(f"Ports ouverts : {len(open_ports)}")
    print(f"Temps écoulé : {end_time - start_time:.2f} secondes")

    if open_ports:
        print(f"Liste : {open_ports}")


def scanner_avec_banner(target_ip, ports):
    """
    Scanner de ports avec récupération des banners.

    Args:
        target_ip (str): Adresse IP cible
        ports (list): Liste des ports à scanner
    """
    print(f"\n=== SCANNER AVEC BANNER GRABBING ===\n")
    print(f"Cible : {target_ip}\n")

    results = []

    for port in ports:
        print(f"Scan du port {port}...", end=" ")

        if scan_port(target_ip, port, timeout=1):
            print("OUVERT", end=" ")

            banner = grab_banner(target_ip, port)
            if banner:
                print(f"- Banner : {banner[:50]}...")
                results.append((port, banner))
            else:
                print("- Pas de banner")
                results.append((port, None))
        else:
            print("FERMÉ")

    print(f"\n--- Résultats ---")
    print(f"Ports ouverts avec banner : {len([r for r in results if r[1]])}")

    return results


# ============================================================================
# PARTIE 6 : OUTILS RED TEAMING
# ============================================================================

def client_netcat_like(host, port):
    """
    Client similaire à netcat pour interaction manuelle.

    Args:
        host (str): Hôte cible
        port (int): Port cible
    """
    print(f"\n=== CLIENT NETCAT-LIKE ===\n")
    print(f"Connexion à {host}:{port}...")

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))

        print("Connecté ! (Tapez 'quit' pour quitter)\n")

        while True:
            # Envoi
            message = input("> ")

            if message.lower() == "quit":
                break

            sock.sendall(message.encode('utf-8') + b"\n")

            # Réception
            try:
                sock.settimeout(2)
                response = sock.recv(4096)

                if response:
                    print(f"< {response.decode('utf-8', errors='ignore')}")
                else:
                    print("Connexion fermée par le serveur")
                    break

            except socket.timeout:
                print("< (pas de réponse)")

        sock.close()

    except Exception as e:
        print(f"ERREUR : {e}")


def serveur_reverse_shell_handler(listen_port):
    """
    Handler pour reverse shell (ÉDUCATIF - NE PAS UTILISER ILLÉGALEMENT).

    Args:
        listen_port (int): Port d'écoute
    """
    print(f"\n=== REVERSE SHELL HANDLER (ÉDUCATIF) ===\n")
    print("AVERTISSEMENT : Uniquement pour tests autorisés !\n")

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server.bind(("0.0.0.0", listen_port))
        server.listen(1)

        print(f"[*] En attente de connexion sur le port {listen_port}...")

        client, addr = server.accept()
        print(f"[+] Connexion reçue de {addr[0]}:{addr[1]}\n")

        while True:
            command = input("shell> ")

            if command.lower() in ["exit", "quit"]:
                break

            if not command.strip():
                continue

            # Envoi de la commande
            client.send(command.encode('utf-8') + b"\n")

            # Réception du résultat
            try:
                client.settimeout(5)
                output = client.recv(4096)

                if output:
                    print(output.decode('utf-8', errors='ignore'))
                else:
                    print("[!] Connexion perdue")
                    break

            except socket.timeout:
                print("[!] Timeout")

        client.close()

    except KeyboardInterrupt:
        print("\n[*] Arrêt du handler...")
    finally:
        server.close()


def http_request_manual(host, port, method, path, headers=None):
    """
    Effectue une requête HTTP manuelle (pour tests de sécurité).

    Args:
        host (str): Hôte cible
        port (int): Port (généralement 80 ou 443)
        method (str): Méthode HTTP (GET, POST, etc.)
        path (str): Chemin de la ressource
        headers (dict): Headers HTTP additionnels

    Returns:
        str: Réponse du serveur
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        sock.connect((host, port))

        # Construction de la requête
        request = f"{method} {path} HTTP/1.1\r\n"
        request += f"Host: {host}\r\n"

        if headers:
            for key, value in headers.items():
                request += f"{key}: {value}\r\n"

        request += "Connection: close\r\n"
        request += "\r\n"

        # Envoi
        sock.sendall(request.encode('utf-8'))

        # Réception
        response = b""
        while True:
            chunk = sock.recv(4096)
            if not chunk:
                break
            response += chunk

        sock.close()

        return response.decode('utf-8', errors='ignore')

    except Exception as e:
        return f"ERREUR : {e}"


def exemple_http_manual():
    """
    Démonstration de requêtes HTTP manuelles.
    """
    print("\n=== REQUÊTES HTTP MANUELLES ===\n")

    # Requête GET basique
    print("--- Requête GET simple ---")
    response = http_request_manual("example.com", 80, "GET", "/")
    print(response[:500])

    print("\n--- Requête avec headers personnalisés ---")
    custom_headers = {
        "User-Agent": "CustomScanner/1.0",
        "Accept": "*/*"
    }
    response = http_request_manual("example.com", 80, "GET", "/", custom_headers)
    print(response.split('\r\n\r\n')[0])  # Headers seulement


# ============================================================================
# PARTIE 7 : GESTION DES ERREURS ET TIMEOUT
# ============================================================================

def exemple_gestion_erreurs():
    """
    Démonstration de la gestion des erreurs socket.
    """
    print("\n=== GESTION DES ERREURS SOCKET ===\n")

    # Erreur 1 : Connection refused
    print("--- Test : Port fermé ---")
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        sock.connect(("127.0.0.1", 9876))  # Port probablement fermé
    except ConnectionRefusedError:
        print("ERREUR : Connexion refusée (port fermé)")
    except Exception as e:
        print(f"ERREUR : {e}")
    finally:
        sock.close()

    # Erreur 2 : Timeout
    print("\n--- Test : Timeout ---")
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect(("192.0.2.1", 80))  # IP non routable (timeout garanti)
    except socket.timeout:
        print("ERREUR : Timeout de connexion")
    except Exception as e:
        print(f"ERREUR : {e}")
    finally:
        sock.close()

    # Erreur 3 : Host introuvable
    print("\n--- Test : Host introuvable ---")
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        sock.connect(("domaine-inexistant-xyz123.com", 80))
    except socket.gaierror:
        print("ERREUR : Impossible de résoudre le nom de domaine")
    except Exception as e:
        print(f"ERREUR : {e}")
    finally:
        sock.close()

    # Erreur 4 : Bind sur port privilégié
    print("\n--- Test : Port privilégié ---")
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("0.0.0.0", 80))  # Nécessite root/admin
    except PermissionError:
        print("ERREUR : Permission refusée (port < 1024 nécessite root)")
    except Exception as e:
        print(f"ERREUR : {e}")
    finally:
        sock.close()


def exemple_timeout_configuration():
    """
    Démonstration de la configuration des timeouts.
    """
    print("\n=== CONFIGURATION DES TIMEOUTS ===\n")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Timeout par défaut (bloquant)
    print(f"Timeout par défaut : {sock.gettimeout()}")

    # Définir un timeout
    sock.settimeout(5.0)
    print(f"Timeout défini : {sock.gettimeout()} secondes")

    # Mode non-bloquant
    sock.setblocking(False)
    print(f"Mode non-bloquant : {sock.gettimeout()}")

    # Retour au mode bloquant
    sock.setblocking(True)
    print(f"Retour mode bloquant : {sock.gettimeout()}")

    sock.close()


# ============================================================================
# PARTIE 8 : RÉSOLUTION D'ADRESSES
# ============================================================================

def exemple_resolution_dns():
    """
    Démonstration de la résolution DNS.
    """
    print("\n=== RÉSOLUTION DNS ===\n")

    # Résolution d'un nom de domaine
    hostname = "example.com"
    print(f"Résolution de {hostname}...")

    try:
        ip_address = socket.gethostbyname(hostname)
        print(f"Adresse IP : {ip_address}")

        # Informations complètes
        host_info = socket.gethostbyname_ex(hostname)
        print(f"Nom canonique : {host_info[0]}")
        print(f"Alias : {host_info[1]}")
        print(f"Adresses IP : {host_info[2]}")

    except socket.gaierror as e:
        print(f"ERREUR de résolution : {e}")

    # Résolution inverse
    print(f"\n--- Résolution inverse ---")
    try:
        ip = "8.8.8.8"
        hostname = socket.gethostbyaddr(ip)
        print(f"IP {ip} -> {hostname[0]}")
    except socket.herror:
        print(f"Pas de reverse DNS pour {ip}")

    # Obtenir le nom de la machine locale
    print(f"\n--- Machine locale ---")
    print(f"Nom d'hôte : {socket.gethostname()}")
    print(f"FQDN : {socket.getfqdn()}")


# ============================================================================
# MENU PRINCIPAL
# ============================================================================

def afficher_menu():
    """
    Affiche le menu des exemples disponibles.
    """
    print("\n" + "="*60)
    print("  EXERCICE 14 - SOCKETS TCP")
    print("="*60)
    print("\n  PARTIE 1 : Bases")
    print("  1.  Création de sockets")
    print("  2.  Client TCP simple")
    print("  3.  Serveur TCP simple")
    print("\n  PARTIE 2 : Banner Grabbing")
    print("  4.  Banner grabbing basique")
    print("  5.  Banner grabbing avancé")
    print("\n  PARTIE 3 : Scanning")
    print("  6.  Scanner de ports simple")
    print("  7.  Scanner avec banner grabbing")
    print("\n  PARTIE 4 : Red Teaming (Éducatif)")
    print("  8.  Client netcat-like")
    print("  9.  Requêtes HTTP manuelles")
    print("\n  PARTIE 5 : Avancé")
    print("  10. Gestion des erreurs")
    print("  11. Configuration des timeouts")
    print("  12. Résolution DNS")
    print("\n  0.  Quitter")
    print("="*60)


def main():
    """
    Fonction principale avec menu interactif.
    """
    while True:
        afficher_menu()
        choix = input("\nVotre choix : ").strip()

        if choix == "1":
            exemple_creation_socket()

        elif choix == "2":
            exemple_client_tcp_simple()

        elif choix == "3":
            exemple_serveur_tcp_simple()

        elif choix == "4":
            exemple_banner_grabbing()

        elif choix == "5":
            ip = input("IP cible (ex: scanme.nmap.org) : ").strip()
            port = int(input("Port (ex: 22) : ").strip())
            result = banner_grabbing_avance(ip, port)
            print(f"\nRésultat : {result}")

        elif choix == "6":
            # Scanner uniquement localhost par défaut (sécurité)
            ip = input("IP cible (LOCALHOST recommandé) : ").strip() or "127.0.0.1"
            start = int(input("Port de départ (ex: 1) : ").strip() or "1")
            end = int(input("Port de fin (ex: 100) : ").strip() or "100")

            if ip != "127.0.0.1":
                confirm = input(f"ATTENTION : Scanner {ip} ? (oui/non) : ")
                if confirm.lower() != "oui":
                    print("Annulé")
                    continue

            scanner_ports_simple(ip, start, end)

        elif choix == "7":
            ip = input("IP cible : ").strip()
            ports_str = input("Ports (séparés par des virgules) : ").strip()
            ports = [int(p.strip()) for p in ports_str.split(",")]
            scanner_avec_banner(ip, ports)

        elif choix == "8":
            host = input("Hôte : ").strip()
            port = int(input("Port : ").strip())
            client_netcat_like(host, port)

        elif choix == "9":
            exemple_http_manual()

        elif choix == "10":
            exemple_gestion_erreurs()

        elif choix == "11":
            exemple_timeout_configuration()

        elif choix == "12":
            exemple_resolution_dns()

        elif choix == "0":
            print("\nAu revoir !")
            break

        else:
            print("\nChoix invalide !")

        input("\nAppuyez sur Entrée pour continuer...")


if __name__ == "__main__":
    print("""
    ╔════════════════════════════════════════════════════════════╗
    ║                  AVERTISSEMENT ÉTHIQUE                     ║
    ╠════════════════════════════════════════════════════════════╣
    ║  Ce code est fourni uniquement à des fins éducatives.     ║
    ║  L'utilisation de ces techniques contre des systèmes      ║
    ║  sans autorisation écrite est ILLÉGALE.                   ║
    ║                                                            ║
    ║  Utilisez uniquement sur :                                ║
    ║  - Vos propres systèmes                                   ║
    ║  - Des cibles avec autorisation écrite                    ║
    ║  - Des environnements de test autorisés (labs, CTF)       ║
    ╚════════════════════════════════════════════════════════════╝
    """)

    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterruption par l'utilisateur. Au revoir !")
        sys.exit(0)
