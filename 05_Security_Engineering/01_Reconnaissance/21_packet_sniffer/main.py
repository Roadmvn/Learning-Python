#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
AVERTISSEMENT CRITIQUE:
Cette application nécessite des privilèges root/administrateur pour fonctionner.
Utilisation légale UNIQUEMENT. À utiliser uniquement sur votre propre réseau.
L'interception non-autorisée de trafic réseau est ILLÉGALE.
"""

import sys
import os
from scapy.all import sniff, IP, TCP, UDP, ICMP, DNS, DNSQR, Raw, ARP, IPv6
from scapy.layers.inet import IP
from scapy.layers.l2 import Ether
import argparse
from datetime import datetime


# Vérification des privilèges root
def verifier_privileges():
    """
    Vérifie si l'utilisateur a les privilèges nécessaires pour capturer les paquets.
    Sur Unix/Linux/macOS, cela nécessite root.
    """
    if os.geteuid() != 0:
        print("ERREUR: Privilèges root requis!")
        print("Relancez avec: sudo python3 main.py")
        sys.exit(1)


# Classe pour stocker les statistiques globales
class StatsCapture:
    """Classe pour accumuler les statistiques de capture."""

    def __init__(self):
        self.total_paquets = 0
        self.paquets_ip = 0
        self.paquets_tcp = 0
        self.paquets_udp = 0
        self.paquets_icmp = 0
        self.paquets_dns = 0
        self.paquets_http = 0
        self.paquets_autres = 0
        self.adresses_ip_sources = set()
        self.adresses_ip_destinations = set()
        self.ports_tcp = {}
        self.ports_udp = {}


stats = StatsCapture()


def analyser_paquet_ethernet(paquet):
    """
    Analyse la couche Ethernet (couche 2 - Liaison de données).
    Extrait les adresses MAC source et destination.

    Args:
        paquet: Paquet Scapy à analyser

    Returns:
        dict: Informations Ethernet extraites
    """
    if Ether in paquet:
        couche_ethernet = paquet[Ether]
        return {
            "mac_src": couche_ethernet.src,
            "mac_dst": couche_ethernet.dst,
            "type": couche_ethernet.type
        }
    return None


def analyser_paquet_ip(paquet):
    """
    Analyse la couche IP (couche 3 - Réseau).
    Extrait les adresses IP, TTL, protocol, flags, etc.

    Args:
        paquet: Paquet Scapy à analyser

    Returns:
        dict: Informations IP extraites
    """
    if IP not in paquet:
        return None

    couche_ip = paquet[IP]

    # Enregistrer les adresses IP pour les statistiques
    stats.adresses_ip_sources.add(couche_ip.src)
    stats.adresses_ip_destinations.add(couche_ip.dst)

    return {
        "version": couche_ip.version,
        "header_len": couche_ip.ihl * 4,  # En-tête en bytes
        "tos": couche_ip.tos,
        "total_len": couche_ip.len,
        "id": couche_ip.id,
        "flags": couche_ip.flags,
        "ttl": couche_ip.ttl,
        "protocol": couche_ip.proto,
        "checksum": couche_ip.chksum,
        "src": couche_ip.src,
        "dst": couche_ip.dst,
        "options": couche_ip.options
    }


def analyser_paquet_tcp(paquet):
    """
    Analyse la couche TCP (couche 4 - Transport).
    Extrait ports, numéros de séquence, flags, fenêtre de réception, etc.

    Args:
        paquet: Paquet Scapy à analyser

    Returns:
        dict: Informations TCP extraites
    """
    if TCP not in paquet:
        return None

    couche_tcp = paquet[TCP]

    # Enregistrer les ports pour les statistiques
    stats.ports_tcp[couche_tcp.dport] = stats.ports_tcp.get(couche_tcp.dport, 0) + 1

    # Décoder les flags TCP
    flags_active = []
    if couche_tcp.flags.F:  # FIN
        flags_active.append("FIN")
    if couche_tcp.flags.S:  # SYN
        flags_active.append("SYN")
    if couche_tcp.flags.R:  # RST
        flags_active.append("RST")
    if couche_tcp.flags.P:  # PSH
        flags_active.append("PSH")
    if couche_tcp.flags.A:  # ACK
        flags_active.append("ACK")
    if couche_tcp.flags.U:  # URG
        flags_active.append("URG")

    return {
        "port_src": couche_tcp.sport,
        "port_dst": couche_tcp.dport,
        "seq": couche_tcp.seq,
        "ack": couche_tcp.ack,
        "data_offset": couche_tcp.dataofs * 4,  # En bytes
        "flags": flags_active,
        "window": couche_tcp.window,
        "checksum": couche_tcp.chksum,
        "urgent_pointer": couche_tcp.urgptr
    }


def analyser_paquet_udp(paquet):
    """
    Analyse la couche UDP (couche 4 - Transport).
    Extrait ports et longueur de données.

    Args:
        paquet: Paquet Scapy à analyser

    Returns:
        dict: Informations UDP extraites
    """
    if UDP not in paquet:
        return None

    couche_udp = paquet[UDP]

    # Enregistrer les ports pour les statistiques
    stats.ports_udp[couche_udp.dport] = stats.ports_udp.get(couche_udp.dport, 0) + 1

    return {
        "port_src": couche_udp.sport,
        "port_dst": couche_udp.dport,
        "length": couche_udp.len,
        "checksum": couche_udp.chksum
    }


def analyser_paquet_dns(paquet):
    """
    Analyse les requêtes et réponses DNS (couche applicative).
    Extrait les noms de domaine queryés et les réponses.

    Args:
        paquet: Paquet Scapy à analyser

    Returns:
        dict: Informations DNS extraites
    """
    if DNS not in paquet:
        return None

    couche_dns = paquet[DNS]

    resultats = {
        "id": couche_dns.id,
        "is_response": couche_dns.qr,
        "opcode": couche_dns.opcode,
        "authoritative": couche_dns.aa,
        "truncated": couche_dns.tc,
        "recursion_desired": couche_dns.rd,
        "recursion_available": couche_dns.ra,
        "response_code": couche_dns.rcode,
        "queries": [],
        "answers": []
    }

    # Extraire les requêtes DNS
    if DNSQR in paquet:
        questions = paquet[DNS].questions
        for question in questions:
            resultats["queries"].append({
                "name": question.qname.decode('utf-8') if isinstance(question.qname, bytes) else question.qname,
                "type": question.qtype,
                "class": question.qclass
            })

    # Extraire les réponses DNS
    if paquet[DNS].an:
        for answer in paquet[DNS].an:
            resultats["answers"].append({
                "name": answer.rrname.decode('utf-8') if isinstance(answer.rrname, bytes) else answer.rrname,
                "type": answer.type,
                "ttl": answer.ttl,
                "rdata": str(answer.rdata)
            })

    return resultats


def analyser_paquet_http(paquet):
    """
    Analyse les données HTTP (couche applicative).
    Extrait les méthodes HTTP, URLs, en-têtes, etc.

    Args:
        paquet: Paquet Scapy à analyser

    Returns:
        dict: Informations HTTP extraites
    """
    if Raw not in paquet:
        return None

    donnees_brutes = paquet[Raw].load

    # Vérifier si c'est du HTTP en cherchant les méthodes communes
    methodes_http = [b"GET", b"POST", b"PUT", b"DELETE", b"HEAD", b"OPTIONS", b"PATCH"]

    try:
        # Essayer de décoder en UTF-8
        contenu = donnees_brutes.decode('utf-8', errors='ignore')

        # Vérifier la signature HTTP
        if "HTTP/" not in contenu:
            return None

        # Splitter par lignes
        lignes = contenu.split('\r\n')
        if not lignes:
            return None

        # Première ligne: méthode HTTP
        premiere_ligne = lignes[0].split()
        if len(premiere_ligne) < 3:
            return None

        resultats = {
            "methode": premiere_ligne[0],
            "url": premiere_ligne[1],
            "version": premiere_ligne[2],
            "en_tetes": {},
            "corps": ""
        }

        # Extraire les en-têtes
        index_corps = 1
        for i, ligne in enumerate(lignes[1:], 1):
            if ligne == "":
                index_corps = i + 1
                break
            if ":" in ligne:
                cle, valeur = ligne.split(":", 1)
                resultats["en_tetes"][cle.strip()] = valeur.strip()

        # Extraire le corps si présent
        if index_corps < len(lignes):
            resultats["corps"] = '\r\n'.join(lignes[index_corps:])[:200]  # Limiter à 200 chars

        return resultats

    except Exception as e:
        return None


def callback_paquet(paquet):
    """
    Fonction callback appelée pour chaque paquet capturé.
    Effectue l'analyse complète du paquet et affiche les informations.

    Args:
        paquet: Paquet Scapy capturé
    """
    stats.total_paquets += 1

    # Timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

    print(f"\n{'='*80}")
    print(f"[PAQUET #{stats.total_paquets}] {timestamp}")
    print(f"{'='*80}")

    # Analyser Ethernet (couche 2)
    eth_info = analyser_paquet_ethernet(paquet)
    if eth_info:
        print(f"\n[COUCHE 2 - ETHERNET]")
        print(f"  MAC Source      : {eth_info['mac_src']}")
        print(f"  MAC Destination : {eth_info['mac_dst']}")
        print(f"  Type            : 0x{eth_info['type']:04x}")

    # Analyser IP (couche 3)
    ip_info = analyser_paquet_ip(paquet)
    if ip_info:
        stats.paquets_ip += 1
        print(f"\n[COUCHE 3 - IP]")
        print(f"  Version         : IPv{ip_info['version']}")
        print(f"  Longueur en-tête: {ip_info['header_len']} bytes")
        print(f"  ToS             : 0x{ip_info['tos']:02x}")
        print(f"  Longueur totale : {ip_info['total_len']} bytes")
        print(f"  Identification  : {ip_info['id']}")
        print(f"  Flags           : {ip_info['flags']}")
        print(f"  TTL             : {ip_info['ttl']}")
        print(f"  Protocole       : {ip_info['protocol']}")
        print(f"  IP Source       : {ip_info['src']}")
        print(f"  IP Destination  : {ip_info['dst']}")
        if ip_info['options']:
            print(f"  Options IP      : {ip_info['options']}")

    # Analyser TCP (couche 4)
    tcp_info = analyser_paquet_tcp(paquet)
    if tcp_info:
        stats.paquets_tcp += 1
        print(f"\n[COUCHE 4 - TCP]")
        print(f"  Port Source     : {tcp_info['port_src']}")
        print(f"  Port Destination: {tcp_info['port_dst']}")
        print(f"  Numéro Sequence : {tcp_info['seq']}")
        print(f"  Numéro ACK      : {tcp_info['ack']}")
        print(f"  Longueur en-tête: {tcp_info['data_offset']} bytes")
        print(f"  Flags TCP       : {', '.join(tcp_info['flags']) if tcp_info['flags'] else 'Aucun'}")
        print(f"  Fenêtre         : {tcp_info['window']}")
        if tcp_info['urgent_pointer']:
            print(f"  Pointeur URG    : {tcp_info['urgent_pointer']}")

    # Analyser UDP (couche 4)
    udp_info = analyser_paquet_udp(paquet)
    if udp_info:
        stats.paquets_udp += 1
        print(f"\n[COUCHE 4 - UDP]")
        print(f"  Port Source     : {udp_info['port_src']}")
        print(f"  Port Destination: {udp_info['port_dst']}")
        print(f"  Longueur        : {udp_info['length']} bytes")

    # Analyser ICMP
    if ICMP in paquet:
        stats.paquets_icmp += 1
        couche_icmp = paquet[ICMP]
        print(f"\n[COUCHE 4 - ICMP]")
        print(f"  Type            : {couche_icmp.type}")
        print(f"  Code            : {couche_icmp.code}")
        print(f"  Checksum        : 0x{couche_icmp.chksum:04x}")

    # Analyser DNS (couche applicative)
    dns_info = analyser_paquet_dns(paquet)
    if dns_info:
        stats.paquets_dns += 1
        print(f"\n[COUCHE 7 - DNS]")
        print(f"  ID Requête      : {dns_info['id']}")
        print(f"  Réponse         : {'Oui' if dns_info['is_response'] else 'Non'}")
        print(f"  Code Réponse    : {dns_info['response_code']}")
        if dns_info['queries']:
            print(f"  Requêtes:")
            for query in dns_info['queries']:
                print(f"    - {query['name']} ({query['type']})")
        if dns_info['answers']:
            print(f"  Réponses:")
            for answer in dns_info['answers']:
                print(f"    - {answer['name']} -> {answer['rdata']} (TTL: {answer['ttl']})")

    # Analyser HTTP (couche applicative)
    http_info = analyser_paquet_http(paquet)
    if http_info:
        stats.paquets_http += 1
        print(f"\n[COUCHE 7 - HTTP]")
        print(f"  Méthode         : {http_info['methode']}")
        print(f"  URL             : {http_info['url']}")
        print(f"  Version HTTP    : {http_info['version']}")
        if http_info['en_tetes']:
            print(f"  En-têtes:")
            for cle, valeur in http_info['en_tetes'].items():
                # Limiter la longueur des valeurs
                valeur_courte = valeur[:60] + "..." if len(valeur) > 60 else valeur
                print(f"    {cle}: {valeur_courte}")
        if http_info['corps']:
            print(f"  Corps (aperçu)  : {http_info['corps'][:100]}...")

    # Vérifier les données brutes
    if Raw in paquet:
        donnees = paquet[Raw].load
        if not http_info and not dns_info:  # Ne pas afficher si déjà analysé
            print(f"\n[DONNÉES BRUTES]")
            # Afficher en hexadécimal et ASCII
            hex_str = donnees[:64].hex()
            print(f"  Hex (premiers 64 bytes): {hex_str}")

    # Afficher la taille totale du paquet
    print(f"\n[RÉSUMÉ]")
    print(f"  Taille total    : {len(paquet)} bytes")

    # Statistiques partielles
    stats.paquets_autres = (stats.total_paquets - stats.paquets_tcp -
                            stats.paquets_udp - stats.paquets_icmp)


def afficher_statistiques_globales():
    """
    Affiche les statistiques cumulées de la capture.
    """
    print(f"\n\n{'='*80}")
    print(f"[STATISTIQUES GLOBALES]")
    print(f"{'='*80}")
    print(f"Total paquets capturés      : {stats.total_paquets}")
    print(f"  - Paquets IP              : {stats.paquets_ip}")
    print(f"  - Paquets TCP             : {stats.paquets_tcp}")
    print(f"  - Paquets UDP             : {stats.paquets_udp}")
    print(f"  - Paquets ICMP            : {stats.paquets_icmp}")
    print(f"  - Paquets DNS             : {stats.paquets_dns}")
    print(f"  - Paquets HTTP            : {stats.paquets_http}")

    print(f"\nAdresses IP uniques sources : {len(stats.adresses_ip_sources)}")
    for ip in sorted(stats.adresses_ip_sources)[:10]:
        print(f"  - {ip}")
    if len(stats.adresses_ip_sources) > 10:
        print(f"  ... et {len(stats.adresses_ip_sources) - 10} autres")

    print(f"\nAdresses IP uniques destinations : {len(stats.adresses_ip_destinations)}")
    for ip in sorted(stats.adresses_ip_destinations)[:10]:
        print(f"  - {ip}")
    if len(stats.adresses_ip_destinations) > 10:
        print(f"  ... et {len(stats.adresses_ip_destinations) - 10} autres")

    if stats.ports_tcp:
        print(f"\nPorts TCP capturés (top 10):")
        ports_tries = sorted(stats.ports_tcp.items(), key=lambda x: x[1], reverse=True)
        for port, count in ports_tries[:10]:
            print(f"  - Port {port}: {count} paquets")

    if stats.ports_udp:
        print(f"\nPorts UDP capturés (top 10):")
        ports_tries = sorted(stats.ports_udp.items(), key=lambda x: x[1], reverse=True)
        for port, count in ports_tries[:10]:
            print(f"  - Port {port}: {count} paquets")


def capturer_paquets(filtre=None, nombre_paquets=0, interface=None, afficher_stats=True):
    """
    Fonction principale pour capturer les paquets réseau.

    Args:
        filtre (str): Filtre BPF (Berkeley Packet Filter) pour cibler les paquets
                      Ex: "tcp port 80", "ip src 192.168.1.1", "udp port 53"
        nombre_paquets (int): Nombre de paquets à capturer (0 = infini)
        interface (str): Interface réseau à surveiller (ex: "eth0")
        afficher_stats (bool): Afficher les statistiques à la fin

    Exemples de filtres BPF:
        - "tcp port 80"           : Tout trafic TCP sur le port 80 (HTTP)
        - "tcp port 443"          : Tout trafic TCP sur le port 443 (HTTPS)
        - "udp port 53"           : Tout trafic UDP sur le port 53 (DNS)
        - "ip src 192.168.1.1"    : Tout trafic provenant de 192.168.1.1
        - "ip dst 8.8.8.8"        : Tout trafic destiné à 8.8.8.8
        - "tcp and port 22"       : Trafic TCP sur le port 22 (SSH)
        - "icmp"                  : Tout trafic ICMP (ping)
        - "not port 22"           : Tous les paquets sauf SSH
    """
    try:
        print(f"{'='*80}")
        print("PACKET SNIFFER - ANALYSEUR RÉSEAU")
        print(f"{'='*80}")
        print(f"Démarrage de la capture...")

        if filtre:
            print(f"Filtre actif: {filtre}")
        if nombre_paquets > 0:
            print(f"Nombre de paquets à capturer: {nombre_paquets}")
        else:
            print(f"Nombre de paquets: Infini (Ctrl+C pour arrêter)")

        print(f"\nEn attente de paquets...")
        print(f"Appuyez sur Ctrl+C pour arrêter la capture\n")

        # Capturer les paquets
        sniff(
            prn=callback_paquet,           # Fonction appelée pour chaque paquet
            filter=filtre,                  # Appliquer le filtre BPF
            iface=interface,                # Interface réseau (optionnel)
            count=nombre_paquets if nombre_paquets > 0 else 0,  # Nombre de paquets
            store=False                     # Ne pas stocker les paquets en mémoire
        )

    except KeyboardInterrupt:
        print(f"\n\n{'='*80}")
        print("Capture interrompue par l'utilisateur (Ctrl+C)")
        print(f"{'='*80}")

    except PermissionError:
        print("ERREUR: Privilèges insuffisants!")
        print("Cette application nécessite les privilèges root/administrateur.")
        print("Relancez avec: sudo python3 main.py")
        sys.exit(1)

    except Exception as e:
        print(f"ERREUR: {e}")
        sys.exit(1)

    finally:
        if afficher_stats:
            afficher_statistiques_globales()


def main():
    """
    Fonction principale pour parser les arguments et démarrer la capture.
    """
    # Vérifier les privilèges root
    verifier_privileges()

    # Parser les arguments de ligne de commande
    parser = argparse.ArgumentParser(
        description="Packet Sniffer - Analyseur de paquets réseau",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples d'utilisation:

  # Capturer tous les paquets
  sudo python3 main.py

  # Capturer uniquement le trafic HTTP
  sudo python3 main.py -f "tcp port 80"

  # Capturer uniquement le trafic DNS
  sudo python3 main.py -f "udp port 53"

  # Capturer 100 paquets
  sudo python3 main.py -c 100

  # Capturer le trafic d'une adresse IP spécifique
  sudo python3 main.py -f "ip src 192.168.1.1"

  # Capturer sur l'interface eth0
  sudo python3 main.py -i eth0

  # Capturer le trafic TCP sauf SSH
  sudo python3 main.py -f "tcp and not port 22"
        """
    )

    parser.add_argument(
        "-f", "--filter",
        type=str,
        default=None,
        help="Filtre BPF (ex: 'tcp port 80', 'udp port 53')"
    )
    parser.add_argument(
        "-c", "--count",
        type=int,
        default=0,
        help="Nombre de paquets à capturer (0 = infini, défaut: 0)"
    )
    parser.add_argument(
        "-i", "--interface",
        type=str,
        default=None,
        help="Interface réseau à surveiller (ex: eth0, wlan0)"
    )
    parser.add_argument(
        "-s", "--stats",
        action="store_true",
        default=True,
        help="Afficher les statistiques (défaut: activé)"
    )

    args = parser.parse_args()

    # Démarrer la capture
    capturer_paquets(
        filtre=args.filter,
        nombre_paquets=args.count,
        interface=args.interface,
        afficher_stats=args.stats
    )


if __name__ == "__main__":
    main()
