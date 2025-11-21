SOLUTIONS - EXERCICE 21: PACKET SNIFFER
========================================

==============================
SOLUTION 1: SNIFFER BASIQUE
==============================

Code complet:

```python
#!/usr/bin/env python3
```python
from scapy.all import sniff, IP
import os
import sys

def verifier_privileges():
    if os.geteuid() != 0:
        print("Erreur: Privilèges root requis! (sudo)")
        sys.exit(1)

def afficher_paquet(paquet):
    """Affiche les informations basiques d'un paquet."""
    if IP in paquet:
        ip_src = paquet[IP].src
        ip_dst = paquet[IP].dst
        taille = len(paquet)

        # Déterminer le protocole
        if paquet[IP].proto == 6:
            protocole = "TCP"
        elif paquet[IP].proto == 17:
            protocole = "UDP"
        elif paquet[IP].proto == 1:
            protocole = "ICMP"
        else:
            protocole = f"Autre({paquet[IP].proto})"

        # Numéro du paquet
        numero = getattr(afficher_paquet, 'compteur', 0) + 1
        afficher_paquet.compteur = numero

        print(f"[{numero}] {ip_src} -> {ip_dst} | {protocole} | {taille} bytes")

def main():
    verifier_privileges()

    print("Capture des 10 premiers paquets...")
    print("Ctrl+C pour arrêter\n")

    sniff(
        prn=afficher_paquet,
        count=10,
        store=False
    )

    print("\nCapture terminée!")

if __name__ == "__main__":
    main()
```
```

Exécution:
```bash
sudo python3 solution_1.py
```

Points clés:
- Vérifier les privilèges root
- Utiliser sniff() avec count=10
- Accéder à paquet[IP].src et paquet[IP].dst
- Vérifier le protocole avec paquet[IP].proto
- Utiliser un compteur pour numéroter les paquets

==============================
SOLUTION 2: FILTRE BPF
==============================

Code complet:

```python
#!/usr/bin/env python3
```python
from scapy.all import sniff, DNS, DNSQR, DNSRR
import os
import sys
from datetime import datetime

def verifier_privileges():
    if os.geteuid() != 0:
        print("Erreur: Privilèges root requis!")
        sys.exit(1)

def analyser_dns(paquet):
    """Analyse les paquets DNS."""
    if DNS not in paquet:
        return

    dns_paquet = paquet[DNS]
    timestamp = datetime.now().strftime("%H:%M:%S")

    # Vérifier si c'est une requête ou une réponse
    if dns_paquet.qr == 0:  # Requête
        for question in dns_paquet.questions:
            domaine = question.qname.decode('utf-8') if isinstance(question.qname, bytes) else question.qname
            type_requete = question.qtype

            # Mapper les types
            types = {1: "A", 28: "AAAA", 5: "CNAME", 15: "MX", 16: "TXT", 2: "NS"}
            type_nom = types.get(type_requete, f"Type{type_requete}")

            print(f"[{timestamp}] REQUÊTE: {domaine} ({type_nom})")

    else:  # Réponse
        # Afficher les réponses
        if dns_paquet.an:
            for answer in dns_paquet.an:
                nom = answer.rrname.decode('utf-8') if isinstance(answer.rrname, bytes) else answer.rrname
                rdata = str(answer.rdata)
                ttl = answer.ttl

                print(f"[{timestamp}] RÉPONSE: {nom} -> {rdata} (TTL: {ttl})")

def main():
    verifier_privileges()

    print("Capture du trafic DNS (UDP port 53)")
    print("Ctrl+C pour arrêter\n")

    sniff(
        prn=analyser_dns,
        filter="udp port 53",
        count=20,
        store=False
    )

    print("\nCapture terminée!")

if __name__ == "__main__":
    main()
```
```

Exécution:
```bash
sudo python3 solution_2.py
```

Points clés:
- Utiliser filter="udp port 53" dans sniff()
- Vérifier qr==0 pour requête, qr==1 pour réponse
- Accéder aux questions avec dns_paquet.questions
- Accéder aux réponses avec dns_paquet.an
- Décoder les noms de domaine en UTF-8

==============================
SOLUTION 3: ANALYSEUR TCP
==============================

Code complet:

```python
#!/usr/bin/env python3
```python
from scapy.all import sniff, IP, TCP
import os
import sys
from datetime import datetime

def verifier_privileges():
    if os.geteuid() != 0:
        print("Erreur: Privilèges root requis!")
        sys.exit(1)

def analyser_tcp(paquet):
    """Analyse les paquets TCP et les flags."""
    if IP not in paquet or TCP not in paquet:
        return

    ip_paquet = paquet[IP]
    tcp_paquet = paquet[TCP]
    timestamp = datetime.now().strftime("%H:%M:%S")

    # Construire la chaîne des flags
    flags_actifs = []
    if tcp_paquet.flags.F:
        flags_actifs.append("FIN")
    if tcp_paquet.flags.S:
        flags_actifs.append("SYN")
    if tcp_paquet.flags.R:
        flags_actifs.append("RST")
    if tcp_paquet.flags.P:
        flags_actifs.append("PSH")
    if tcp_paquet.flags.A:
        flags_actifs.append("ACK")
    if tcp_paquet.flags.U:
        flags_actifs.append("URG")

    flags_str = "-".join(flags_actifs) if flags_actifs else "NONE"

    # Afficher les informations
    src_port = tcp_paquet.sport
    dst_port = tcp_paquet.dport
    seq = tcp_paquet.seq
    ack = tcp_paquet.ack

    print(f"[{timestamp}] [{flags_str}] {ip_paquet.src}:{src_port} -> {ip_paquet.dst}:{dst_port}")
    print(f"  SEQ={seq} ACK={ack}")

def main():
    verifier_privileges()

    print("Capture du trafic TCP")
    print("Ctrl+C pour arrêter\n")

    sniff(
        prn=analyser_tcp,
        filter="tcp",
        count=50,
        store=False
    )

    print("\nCapture terminée!")

if __name__ == "__main__":
    main()
```
```

Exécution:
```bash
sudo python3 solution_3.py
```

Points clés:
- Filtrer avec filter="tcp"
- Accéder aux flags avec tcp_paquet.flags.S, .A, .R, .F, .P, .U
- Construire une chaîne des flags actifs
- Afficher les ports (sport/dport) et numéros (seq/ack)
- Utiliser des tirets pour séparer les flags

==============================
SOLUTION 4: ANALYSEUR HTTP
==============================

Code complet:

```python
#!/usr/bin/env python3
```python
from scapy.all import sniff, IP, TCP, Raw
import os
import sys
from datetime import datetime

def verifier_privileges():
    if os.geteuid() != 0:
        print("Erreur: Privilèges root requis!")
        sys.exit(1)

def analyser_http(paquet):
    """Analyse les paquets HTTP."""
    if IP not in paquet or TCP not in paquet or Raw not in paquet:
        return

    try:
        donnees_brutes = paquet[Raw].load

        # Essayer de décoder en UTF-8
        contenu = donnees_brutes.decode('utf-8', errors='ignore')

        # Vérifier que c'est du HTTP
        if "HTTP/" not in contenu:
            return

        timestamp = datetime.now().strftime("%H:%M:%S")
        ip_src = paquet[IP].src
        ip_dst = paquet[IP].dst
        port_src = paquet[TCP].sport
        port_dst = paquet[TCP].dport

        # Splitter par lignes
        lignes = contenu.split('\r\n')
        premiere_ligne = lignes[0]

        print(f"[{timestamp}] {ip_src}:{port_src} -> {ip_dst}:{port_dst}")
        print(f"  {premiere_ligne}")

        # Afficher les en-têtes importants
        for ligne in lignes[1:]:
            if not ligne:
                break

            if any(x in ligne.lower() for x in ['host:', 'user-agent:', 'content-type:']):
                print(f"  {ligne}")

        print()

    except Exception as e:
        pass

def main():
    verifier_privileges()

    print("Capture du trafic HTTP (TCP port 80)")
    print("Ctrl+C pour arrêter\n")

    sniff(
        prn=analyser_http,
        filter="tcp port 80",
        count=10,
        store=False
    )

    print("Capture terminée!")

if __name__ == "__main__":
    main()
```
```

Exécution:
```bash
sudo python3 solution_4.py
```

Points clés:
- Filtrer avec filter="tcp port 80"
- Vérifier que Raw est présent
- Décoder les données brutes en UTF-8
- Vérifier la présence de "HTTP/"
- Splitter par "\r\n" pour obtenir les lignes
- Afficher la première ligne (requête/réponse) et les en-têtes importants

==============================
SOLUTION 5: STATISTIQUES RÉSEAU
==============================

Code complet:

```python
#!/usr/bin/env python3
```python
from scapy.all import sniff, IP, TCP, UDP, ICMP
import os
import sys
from datetime import datetime

def verifier_privileges():
    if os.geteuid() != 0:
        print("Erreur: Privilèges root requis!")
        sys.exit(1)

class StatsReseau:
    def __init__(self):
        self.total_paquets = 0
        self.paquets_tcp = 0
        self.paquets_udp = 0
        self.paquets_icmp = 0
        self.ips_sources = {}
        self.ports_tcp = {}
        self.ports_udp = {}
        self.bytes_total = 0

def analyser_paquet(paquet, stats):
    """Analyse un paquet et met à jour les statistiques."""
    stats.total_paquets += 1
    stats.bytes_total += len(paquet)

    if IP not in paquet:
        return

    ip_paquet = paquet[IP]
    src_ip = ip_paquet.src

    # Compter les IPs sources
    stats.ips_sources[src_ip] = stats.ips_sources.get(src_ip, 0) + 1

    # Compter les protocoles
    if TCP in paquet:
        stats.paquets_tcp += 1
        port = paquet[TCP].dport
        stats.ports_tcp[port] = stats.ports_tcp.get(port, 0) + 1

    elif UDP in paquet:
        stats.paquets_udp += 1
        port = paquet[UDP].dport
        stats.ports_udp[port] = stats.ports_udp.get(port, 0) + 1

    elif ICMP in paquet:
        stats.paquets_icmp += 1

def afficher_statistiques(stats):
    """Affiche les statistiques accumulées."""
    print(f"\n{'='*50}")
    print("STATISTIQUES")
    print(f"{'='*50}")
    print(f"Total paquets: {stats.total_paquets}")
    print(f"Trafic total: {stats.bytes_total / (1024*1024):.2f} MB")
    print(f"\nPar protocole:")
    print(f"  TCP: {stats.paquets_tcp}")
    print(f"  UDP: {stats.paquets_udp}")
    print(f"  ICMP: {stats.paquets_icmp}")

    # Top 5 IPs sources
    print(f"\nTop 5 IPs sources:")
    ips_triees = sorted(stats.ips_sources.items(), key=lambda x: x[1], reverse=True)
    for ip, count in ips_triees[:5]:
        print(f"  {ip}: {count} paquets")

    # Top 5 ports TCP
    if stats.ports_tcp:
        print(f"\nTop 5 ports TCP:")
        ports_tries = sorted(stats.ports_tcp.items(), key=lambda x: x[1], reverse=True)
        for port, count in ports_tries[:5]:
            print(f"  Port {port}: {count} paquets")

    # Top 5 ports UDP
    if stats.ports_udp:
        print(f"\nTop 5 ports UDP:")
        ports_tries = sorted(stats.ports_udp.items(), key=lambda x: x[1], reverse=True)
        for port, count in ports_tries[:5]:
            print(f"  Port {port}: {count} paquets")

def main():
    verifier_privileges()

    print("Capture du trafic réseau pendant 60 secondes")
    print("Ctrl+C pour arrêter\n")

    stats = StatsReseau()

    try:
        # Créer un wrapper pour passer les stats
        def callback(p):
            analyser_paquet(p, stats)

        sniff(
            prn=callback,
            timeout=60,
            store=False
        )

    except KeyboardInterrupt:
        print("\nCapture interrompue!")

    finally:
        afficher_statistiques(stats)

if __name__ == "__main__":
    main()
```
```

Exécution:
```bash
sudo python3 solution_5.py
```

Points clés:
- Créer une classe pour stocker les statistiques
- Utiliser un dictionnaire pour compter les occurrences
- Trier avec sorted() et key=lambda
- Calculer les MB avec bytes / (1024 * 1024)
- Utiliser timeout pour arrêter après 60 secondes
- Afficher les résultats à la fin avec finally

==============================
SOLUTION 6: DÉTECTION D'ANOMALIES
==============================

Code complet:

```python
#!/usr/bin/env python3
```python
from scapy.all import sniff, IP, TCP
import os
import sys
from datetime import datetime, timedelta
from collections import defaultdict

def verifier_privileges():
    if os.geteuid() != 0:
        print("Erreur: Privilèges root requis!")
        sys.exit(1)

class DetecteurAnomalies:
    def __init__(self):
        # Track des connexions SYN pour détecter les scans
        self.syn_paquets = defaultdict(list)  # {ip_src: [(timestamp, port), ...]}
        # Track des connexions pour détection RST
        self.connexions = {}  # {(src_ip, dst_ip, port): timestamp}
        self.alerte_count = 0

    def afficher_alerte(self, message):
        """Affiche une alerte avec timestamp."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.alerte_count += 1
        print(f"\n[ALERTE #{self.alerte_count} {timestamp}] {message}")

    def detecter_anomalies(self, paquet):
        """Analyse un paquet pour détecter les anomalies."""
        if IP not in paquet or TCP not in paquet:
            return

        ip_paquet = paquet[IP]
        tcp_paquet = paquet[TCP]

        ip_src = ip_paquet.src
        ip_dst = ip_paquet.dst
        port_dst = tcp_paquet.dport
        timestamp = datetime.now()

        # Détection 1: Scan de ports (SYN sans ACK)
        if tcp_paquet.flags.S and not tcp_paquet.flags.A:
            self.syn_paquets[ip_src].append((timestamp, port_dst))

            # Nettoyer les vieilles entrées (> 5 secondes)
            cutoff = timestamp - timedelta(seconds=5)
            self.syn_paquets[ip_src] = [
                (t, p) for t, p in self.syn_paquets[ip_src]
                if t > cutoff
            ]

            # Si plus de 5 SYN sur des ports différents en 5 sec
            ports_uniques = set(p for _, p in self.syn_paquets[ip_src])
            if len(ports_uniques) >= 5:
                self.afficher_alerte(
                    f"SCAN DE PORTS: {ip_src} a tenté {len(ports_uniques)} ports en 5 sec"
                )

        # Détection 2: Paquet fragmenté
        if ip_paquet.flags.MF:  # More Fragments flag
            self.afficher_alerte(
                f"PAQUET FRAGMENTÉ: {ip_src} -> {ip_dst} (fragment ID={ip_paquet.id})"
            )

        # Détection 3: TTL anormal (< 30)
        if ip_paquet.ttl < 30:
            self.afficher_alerte(
                f"TTL ANORMAL: {ip_src} -> {ip_dst} TTL={ip_paquet.ttl} (suspicieux!)"
            )

        # Détection 4: Connexion échouée (RST)
        if tcp_paquet.flags.R:
            self.afficher_alerte(
                f"CONNEXION ÉCHOUÉE: {ip_src}:{tcp_paquet.sport} -> {ip_dst}:{port_dst} (RST)"
            )

def main():
    verifier_privileges()

    print("Détecteur d'anomalies réseau")
    print("Capture pendant 120 secondes")
    print("Ctrl+C pour arrêter\n")

    detecteur = DetecteurAnomalies()

    try:
        sniff(
            prn=lambda p: detecteur.detecter_anomalies(p),
            timeout=120,
            store=False
        )

    except KeyboardInterrupt:
        print("\n\nCapture interrompue!")

    finally:
        print(f"\nTotal d'alertes: {detecteur.alerte_count}")

if __name__ == "__main__":
    main()
```
```

Exécution:
```bash
sudo python3 solution_6.py
```

Points clés:
- Créer une classe pour gérer l'état
- Utiliser defaultdict pour tracker les SYN
- Vérifier les flags avec flags.S, .A, .R, .MF
- Vérifier TTL avec paquet[IP].ttl
- Nettoyer les données anciennes (> 5 secondes)
- Afficher les alertes avec timestamp

==============================
SOLUTION 7: ANALYSEUR MULTI-PROTOCOLE AVANCÉ
==============================

Code complet:

```python
#!/usr/bin/env python3
```python
from scapy.all import sniff, IP, TCP, UDP, Raw, DNS, DNSQR
import os
import sys
import json
from datetime import datetime

def verifier_privileges():
    if os.geteuid() != 0:
        print("Erreur: Privilèges root requis!")
        sys.exit(1)

class AnalyseurMultiProto:
    def __init__(self):
        self.resultats = {
            "timestamp": datetime.now().isoformat(),
            "total_packets": 0,
            "dns_queries": [],
            "http_requests": [],
            "ssh_connections": [],
            "ftp_commands": []
        }

    def analyser_http(self, donnees, ip_src, ip_dst, port_src, port_dst):
        """Analyse le trafic HTTP."""
        try:
            contenu = donnees.decode('utf-8', errors='ignore')
            if "HTTP/" not in contenu:
                return

            lignes = contenu.split('\r\n')
            if not lignes:
                return

            premiere_ligne = lignes[0].split()
            if len(premiere_ligne) < 3:
                return

            # Extraire la méthode et l'URL
            methode = premiere_ligne[0]
            url = premiere_ligne[1]

            # Extraire le Host
            host = ""
            for ligne in lignes[1:]:
                if ligne.lower().startswith("host:"):
                    host = ligne.split(":", 1)[1].strip()
                    break

            self.resultats["http_requests"].append({
                "timestamp": datetime.now().isoformat(),
                "src": ip_src,
                "dst": ip_dst,
                "method": methode,
                "url": url,
                "host": host
            })
        except:
            pass

    def analyser_ssh(self, donnees, ip_src, ip_dst, port_src, port_dst):
        """Analyse les connexions SSH."""
        try:
            contenu = donnees.decode('utf-8', errors='ignore')
            if not contenu.startswith("SSH-"):
                return

            version = contenu.split('\r\n')[0].strip()

            self.resultats["ssh_connections"].append({
                "timestamp": datetime.now().isoformat(),
                "src": ip_src,
                "dst": ip_dst,
                "version": version
            })
        except:
            pass

    def analyser_dns(self, paquet):
        """Analyse les requêtes DNS."""
        try:
            if DNS not in paquet:
                return

            dns_pkt = paquet[DNS]

            if dns_pkt.qr == 0:  # Requête
                for question in dns_pkt.questions:
                    domaine = question.qname.decode('utf-8') if isinstance(question.qname, bytes) else question.qname
                    self.resultats["dns_queries"].append({
                        "timestamp": datetime.now().isoformat(),
                        "domain": domaine,
                        "type": question.qtype
                    })
        except:
            pass

    def analyser_paquet(self, paquet):
        """Analyse un paquet selon son type."""
        self.resultats["total_packets"] += 1

        if IP not in paquet or TCP not in paquet:
            return

        ip_pkt = paquet[IP]
        tcp_pkt = paquet[TCP]

        ip_src = ip_pkt.src
        ip_dst = ip_pkt.dst
        port_src = tcp_pkt.sport
        port_dst = tcp_pkt.dport

        # Analyser DNS
        self.analyser_dns(paquet)

        # Analyser les données brutes
        if Raw not in paquet:
            return

        donnees = paquet[Raw].load

        # HTTP
        if port_dst in [80, 8080, 8081]:
            self.analyser_http(donnees, ip_src, ip_dst, port_src, port_dst)

        # SSH
        if port_dst == 22:
            self.analyser_ssh(donnees, ip_src, ip_dst, port_src, port_dst)

def main():
    verifier_privileges()

    print("Analyseur Multi-Protocole Avancé")
    print("Capture pendant 3 minutes")
    print("Ctrl+C pour arrêter\n")

    analyseur = AnalyseurMultiProto()

    try:
        sniff(
            prn=lambda p: analyseur.analyser_paquet(p),
            timeout=180,
            store=False
        )

    except KeyboardInterrupt:
        print("\n\nCapture interrompue!")

    finally:
        # Sauvegarder les résultats
        with open('resultats.json', 'w') as f:
            json.dump(analyseur.resultats, f, indent=2)

        print(f"\nRésultats sauvegardés dans resultats.json")
        print(f"Total paquets: {analyseur.resultats['total_packets']}")
        print(f"Requêtes DNS: {len(analyseur.resultats['dns_queries'])}")
        print(f"Requêtes HTTP: {len(analyseur.resultats['http_requests'])}")
        print(f"Connexions SSH: {len(analyseur.resultats['ssh_connections'])}")

if __name__ == "__main__":
    main()
```
```

Exécution:
```bash
sudo python3 solution_7.py
```

Points clés:
- Créer une classe pour organiser l'analyse
- Supporter plusieurs ports pour HTTP (80, 8080, 8081)
- Exporter les résultats en JSON
- Gérer les exceptions pour les différents protocoles
- Stocker les timestamps pour chaque détection

==============================
SOLUTION 8: SNIFFER PERSISTANT AVEC INTERFACE WEB
==============================

Fichier 1: database.py

```python
```python
import sqlite3
from datetime import datetime, timedelta

class DatabasePackets:
    def __init__(self, db_path="packets.db"):
        self.db_path = db_path
        self.init_db()

    def init_db(self):
        """Initialise la base de données."""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        c.execute('''
            CREATE TABLE IF NOT EXISTS packets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME,
                src_ip TEXT,
                dst_ip TEXT,
                protocol TEXT,
                src_port INTEGER,
                dst_port INTEGER,
                size INTEGER,
                flags TEXT
            )
        ''')

        c.execute('CREATE INDEX IF NOT EXISTS idx_timestamp ON packets(timestamp)')
        c.execute('CREATE INDEX IF NOT EXISTS idx_src_ip ON packets(src_ip)')
        c.execute('CREATE INDEX IF NOT EXISTS idx_protocol ON packets(protocol)')

        conn.commit()
        conn.close()

    def insert_packet(self, src_ip, dst_ip, protocol, src_port, dst_port, size, flags=""):
        """Insère un paquet dans la base."""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        timestamp = datetime.now().isoformat()
        c.execute('''
            INSERT INTO packets
            (timestamp, src_ip, dst_ip, protocol, src_port, dst_port, size, flags)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (timestamp, src_ip, dst_ip, protocol, src_port, dst_port, size, flags))

        conn.commit()
        conn.close()

    def get_packets(self, limit=100, offset=0):
        """Récupère les paquets avec pagination."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        c = conn.cursor()

        c.execute('''
            SELECT * FROM packets
            ORDER BY timestamp DESC
            LIMIT ? OFFSET ?
        ''', (limit, offset))

        packets = [dict(row) for row in c.fetchall()]
        conn.close()

        return packets

    def get_stats(self):
        """Retourne les statistiques globales."""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        c.execute('SELECT COUNT(*) FROM packets')
        total = c.fetchone()[0]

        c.execute('SELECT protocol, COUNT(*) FROM packets GROUP BY protocol')
        by_protocol = dict(c.fetchall())

        c.execute('SELECT dst_port, COUNT(*) FROM packets WHERE protocol="TCP" GROUP BY dst_port ORDER BY COUNT(*) DESC LIMIT 5')
        top_ports = dict(c.fetchall())

        conn.close()

        return {
            "total_packets": total,
            "by_protocol": by_protocol,
            "top_tcp_ports": top_ports
        }

    def cleanup_old_packets(self, hours=1):
        """Supprime les paquets plus vieux que le nombre d'heures spécifié."""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        cutoff = (datetime.now() - timedelta(hours=hours)).isoformat()
        c.execute('DELETE FROM packets WHERE timestamp < ?', (cutoff,))

        conn.commit()
        conn.close()
```
```

Fichier 2: sniffer.py

```python
#!/usr/bin/env python3
```python
from scapy.all import sniff, IP, TCP, UDP
import os
import sys
from database import DatabasePackets
import threading
from datetime import datetime

def verifier_privileges():
    if os.geteuid() != 0:
        print("Erreur: Privilèges root requis!")
        sys.exit(1)

class SnifferThread(threading.Thread):
    def __init__(self, db):
        threading.Thread.__init__(self)
        self.db = db
        self.daemon = True
        self.running = True

    def analyser_paquet(self, paquet):
        """Analyse un paquet et l'enregistre."""
        if IP not in paquet:
            return

        ip_pkt = paquet[IP]

        # Déterminer le protocole
        if TCP in paquet:
            protocol = "TCP"
            src_port = paquet[TCP].sport
            dst_port = paquet[TCP].dport
            flags = str(paquet[TCP].flags)
        elif UDP in paquet:
            protocol = "UDP"
            src_port = paquet[UDP].sport
            dst_port = paquet[UDP].dport
            flags = ""
        else:
            protocol = f"Proto{ip_pkt.proto}"
            src_port = 0
            dst_port = 0
            flags = ""

        # Enregistrer dans la base
        self.db.insert_packet(
            ip_pkt.src, ip_pkt.dst, protocol,
            src_port, dst_port, len(paquet), flags
        )

    def run(self):
        """Lance la capture en arrière-plan."""
        try:
            sniff(
                prn=self.analyser_paquet,
                store=False
            )
        except KeyboardInterrupt:
            pass

def main():
    verifier_privileges()

    db = DatabasePackets()

    print("Démarrage du sniffer persistant...")

    # Démarrer la capture en arrière-plan
    sniffer = SnifferThread(db)
    sniffer.start()

    print("Sniffer démarré! Vous pouvez lancer l'API...")

if __name__ == "__main__":
    main()
```
```

Fichier 3: api.py

```python
```python
from flask import Flask, jsonify, request
from database import DatabasePackets
import json

```
app = Flask(__name__)
db = DatabasePackets()

@app.route('/api/packets', methods=['GET'])
def get_packets():
```python
    """Retourne la liste des paquets."""
    limit = request.args.get('limit', default=100, type=int)
    offset = request.args.get('offset', default=0, type=int)

    packets = db.get_packets(limit, offset)
    return jsonify(packets)

```
@app.route('/api/packets/filter', methods=['GET'])
```python
def filter_packets():
    """Filtre les paquets par protocole et port."""
    protocol = request.args.get('protocol', type=str)
    port = request.args.get('port', type=int)

    packets = db.get_packets()

    # Filtrer en Python
    if protocol:
        packets = [p for p in packets if p['protocol'] == protocol]
    if port:
        packets = [p for p in packets if p['dst_port'] == port]

    return jsonify(packets)

```
@app.route('/api/stats', methods=['GET'])
def get_stats():
```python
    """Retourne les statistiques globales."""
    stats = db.get_stats()
    return jsonify(stats)

```
@app.route('/api/export', methods=['GET'])
```python
def export_packets():
    """Exporte les paquets en JSON."""
    packets = db.get_packets(limit=10000)

    response = app.response_class(
        response=json.dumps(packets, indent=2),
        status=200,
        mimetype='application/json'
    )
    response.headers["Content-Disposition"] = "attachment; filename=packets.json"
    return response

```
@app.route('/', methods=['GET'])
def index():
```python
    """Affiche l'interface web."""
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Packet Sniffer Web</title>
        <style>
            body { font-family: Arial; margin: 20px; }
            table { border-collapse: collapse; width: 100%; }
            th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
            th { background-color: #f2f2f2; }
        </style>
    </head>
    <body>
        <h1>Packet Sniffer Web Interface</h1>

        <div>
            <h2>Statistiques</h2>
            <div id="stats"></div>
        </div>

        <div>
            <h2>Paquets récents</h2>
            <table id="packets">
                <thead>
                    <tr>
                        <th>Timestamp</th>
                        <th>Protocole</th>
                        <th>Source</th>
                        <th>Destination</th>
                        <th>Taille</th>
                    </tr>
                </thead>
                <tbody></tbody>
            </table>
        </div>

        <script>
            function loadStats() {
                fetch('/api/stats')
                    .then(r => r.json())
                    .then(data => {
                        document.getElementById('stats').innerHTML =
                            '<p>Total: ' + data.total_packets + ' paquets</p>';
                    });
            }

            function loadPackets() {
                fetch('/api/packets?limit=50')
                    .then(r => r.json())
                    .then(packets => {
                        const tbody = document.querySelector('#packets tbody');
                        tbody.innerHTML = '';

                        packets.forEach(p => {
                            const row = tbody.insertRow();
                            row.innerHTML = `
                                <td>${p.timestamp}</td>
                                <td>${p.protocol}</td>
                                <td>${p.src_ip}:${p.src_port}</td>
                                <td>${p.dst_ip}:${p.dst_port}</td>
                                <td>${p.size}</td>
                            `;
                        });
                    });
            }

            // Charger les données toutes les 5 secondes
            loadStats();
            loadPackets();
            setInterval(loadStats, 5000);
            setInterval(loadPackets, 5000);
        </script>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
```
```

Exécution:

```bash
# Terminal 1: Lancer le sniffer
sudo python3 sniffer.py &

# Terminal 2: Lancer l'API
python3 api.py

# Terminal 3: Accéder à l'interface
open http://localhost:5000
```

Points clés:
- Utiliser SQLite avec index pour les performances
- Implémenter la pagination avec LIMIT/OFFSET
- Utiliser threading pour capturer en arrière-plan
- Créer une API RESTful avec Flask
- Implémenter une interface web simple
- Ajouter le nettoyage des données anciennes
- Supporter l'export en JSON et CSV
