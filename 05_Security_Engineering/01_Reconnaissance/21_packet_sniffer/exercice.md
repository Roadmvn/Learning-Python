EXERCICE 21 - PACKET SNIFFER
============================

AVERTISSEMENT CRITIQUE:
- Cette exercice nécessite des privilèges root/administrateur
- À utiliser UNIQUEMENT sur votre propre réseau ou avec permission explicite
- L'interception non-autorisée de trafic réseau est ILLÉGALE
- Vous êtes entièrement responsable de l'usage et des conséquences légales

==============================
DÉFI 1: SNIFFER BASIQUE
==============================

Objectif: Créer un sniffer simple qui capture et affiche les 10 premiers paquets.

Contraintes:
- Utiliser sniff() de Scapy
- Afficher la source et destination IP pour chaque paquet
- Afficher le protocole (TCP, UDP, ICMP, etc.)
- Afficher la taille du paquet
- Arrêter après 10 paquets

Exemple de sortie attendue:
[1] 192.168.1.100 -> 8.8.8.8 | TCP | 54 bytes
[2] 192.168.1.100 -> 8.8.8.8 | TCP | 1460 bytes
[3] 192.168.1.100 -> 1.1.1.1 | UDP | 56 bytes

Indices:
- La couche IP est accessible avec paquet[IP]
- Les protocoles sont en paquet[TCP], paquet[UDP], paquet[ICMP]
- La longueur est len(paquet)

==============================
DÉFI 2: FILTRE BPF
==============================

Objectif: Implémenter un filtre pour ne capturer que le trafic DNS (UDP port 53).

Contraintes:
- Utiliser les filtres BPF de Scapy
- Capturer les requêtes et réponses DNS
- Afficher les domaines queryés
- Afficher les réponses (adresses IP)
- Capturer pendant 30 secondes ou 20 paquets

Exemple de sortie attendue:
[1] REQUÊTE: google.com (type A)
[2] RÉPONSE: google.com -> 142.251.41.14 (TTL: 300)
[3] REQUÊTE: example.com (type A)

Indices:
- Le filtre pour DNS est "udp port 53"
- La couche DNS est paquet[DNS]
- Les questions sont paquet[DNS].questions
- Les réponses sont paquet[DNS].an

==============================
DÉFI 3: ANALYSEUR TCP
==============================

Objectif: Créer un analyseur TCP qui capture les connexions établies.

Contraintes:
- Filtrer uniquement le trafic TCP
- Détecter les SYN (début de connexion)
- Détecter les ACK (confirmation)
- Détecter les FIN/RST (fin de connexion)
- Afficher les ports source et destination
- Afficher les numéros de séquence et ACK
- Capturer 50 paquets TCP

Exemple de sortie attendue:
[SYN] 192.168.1.100:45678 -> 10.0.0.1:443 (seq=1234567890)
[ACK] 10.0.0.1:443 -> 192.168.1.100:45678 (ack=1234567891)
[PSH-ACK] 192.168.1.100:45678 -> 10.0.0.1:443 (data=100 bytes)
[FIN] 192.168.1.100:45678 -> 10.0.0.1:443 (seq=1234568890)

Indices:
- Le filtre est "tcp"
- Les flags sont dans paquet[TCP].flags
- Les ports sont paquet[TCP].sport et paquet[TCP].dport
- Les numéros de séquence sont paquet[TCP].seq et paquet[TCP].ack

==============================
DÉFI 4: ANALYSEUR HTTP
==============================

Objectif: Capturer et décoder le trafic HTTP (non chiffré).

Contraintes:
- Filtrer le trafic HTTP (TCP port 80)
- Extraire les méthodes HTTP (GET, POST, etc.)
- Extraire les URLs demandées
- Extraire les en-têtes HTTP importants (Host, User-Agent, etc.)
- Extraire le corps des requêtes (si présent)
- Afficher les codes de réponse HTTP (200, 404, etc.)
- Capturer 10 requêtes/réponses HTTP

Exemple de sortie attendue:
[HTTP REQUEST] GET /search?q=python HTTP/1.1
  Host: www.example.com
  User-Agent: Mozilla/5.0
  Accept: text/html

[HTTP RESPONSE] HTTP/1.1 200 OK
  Content-Type: text/html
  Content-Length: 5678

Indices:
- Le filtre est "tcp port 80"
- Les données brutes sont dans paquet[Raw].load
- Décoder en UTF-8 pour obtenir du texte lisible
- Les lignes HTTP sont séparées par \r\n
- La première ligne contient la méthode, l'URL et la version

==============================
DÉFI 5: STATISTIQUES RÉSEAU
==============================

Objectif: Créer un analyseur qui recueille et affiche les statistiques globales.

Contraintes:
- Capturer tous les paquets sans filtre pendant 60 secondes
- Compter le total de paquets par protocole (TCP, UDP, ICMP)
- Compter le nombre d'adresses IP uniques (source et destination)
- Compter les ports TCP et UDP les plus utilisés
- Calculer le trafic total en bytes et MB
- Afficher les adresses MAC uniques
- Afficher un résumé détaillé à la fin

Exemple de sortie attendue:
[STATISTIQUES APRÈS 60 SECONDES]
Total paquets: 1234
- TCP: 567 paquets
- UDP: 456 paquets
- ICMP: 23 paquets

Adresses IP sources uniques: 12
  - 192.168.1.100 (234 paquets)
  - 192.168.1.101 (156 paquets)
  ... 10 autres

Ports TCP top 5:
  - 443: 234 paquets
  - 80: 156 paquets
  - 22: 45 paquets

Trafic total: 5.67 MB

Indices:
- Accumuler les statistiques dans une classe ou dictionnaire
- Compter les IPs avec un set et len()
- Trier les ports avec sorted()
- Calculer les MB avec bytes / (1024 * 1024)

==============================
DÉFI 6: DÉTECTION D'ANOMALIES
==============================

Objectif: Créer un détecteur d'activités suspectes ou anormales.

Contraintes:
- Détecter les scans de ports (SYN sans ACK dans les 5 secondes)
- Détecter les connexions échouées (RST après SYN)
- Détecter les requêtes répétées (même IP/port plusieurs fois)
- Détecter les paquets fragmentés (IP flags avec MF=1)
- Détecter les connexions avec TTL anormal (< 30)
- Détecter les paquets avec options IP inhabituelles
- Afficher les alertes en temps réel avec timestamp
- Capturer pendant 2 minutes

Exemple de sortie attendue:
[ALERTE 09:45:32] SCAN DE PORTS: 192.168.1.50 tente SYN sur 10 ports différents en 5 sec
[ALERTE 09:46:15] CONNEXION ÉCHOUÉE: 192.168.1.50:45678 -> 8.8.8.8:443 (RST reçu)
[ALERTE 09:47:02] PAQUET FRAGMENTÉ: 192.168.1.100 -> 8.8.8.8 (7 fragments)
[ALERTE 09:47:45] TTL ANORMAL: 192.168.1.100 -> 8.8.8.8 TTL=15 (trop bas)

Indices:
- Utiliser un dictionnaire pour tracker les connexions récentes
- Vérifier les flags TCP avec paquet[TCP].flags.S, .A, .R
- Vérifier la fragmentation avec paquet[IP].flags
- Vérifier le TTL avec paquet[IP].ttl
- Stocker les timestamps avec datetime.now()

==============================
DÉFI 7: ANALYSEUR MULTI-PROTOCOLE AVANCÉ
==============================

Objectif: Créer un analyseur complet supportant DNS, HTTP, HTTPS (inspection TLS), SSH, FTP.

Contraintes:
- Analyser le handshake DNS complètement (QNAME, QTYPE, RCODE)
- Analyser les en-têtes HTTP et HTTPS (certificat SNI)
- Analyser les données SSH (version du serveur)
- Analyser les réponses FTP (codes de réponse)
- Identifier les protocoles même si le port est non-standard
- Créer un rapport JSON avec tous les résultats
- Supporter les filtres personnalisés
- Capturer pendant 3 minutes

Format JSON attendu:
{
  "timestamp": "2024-01-01T12:00:00",
  "total_packets": 500,
  "dns_queries": [
```python
    {"domain": "google.com", "type": "A", "response": "142.251.41.14"}
```
  ],
  "http_requests": [
```python
    {"method": "GET", "url": "/", "host": "example.com"}
```
  ],
  "ssh_connections": [
```python
    {"src": "192.168.1.100", "dst": "10.0.0.1", "version": "SSH-2.0-OpenSSH"}
```
  ]
}

Indices:
- Créer des classes séparées pour chaque protocole
- Exporter les résultats en JSON avec json.dump()
- Supporter plusieurs ports pour chaque protocole (80, 8080, 8081 pour HTTP)
- Utiliser une machine à états pour les handshakes (SYN -> ACK -> DATA)

==============================
DÉFI 8: SNIFFER PERSISTANT AVEC INTERFACE WEB
==============================

Objectif: Créer un sniffer qui persiste les données et expose une interface web.

Contraintes:
- Sauvegarder les paquets capturés en base de données SQLite
- Enregistrer tous les métadonnées (timestamp, IPs, ports, protocoles)
- Créer une API Flask/FastAPI qui expose:
  - GET /api/packets - Liste tous les paquets
  - GET /api/packets/filters?protocol=tcp&port=80 - Filtrer les paquets
  - GET /api/stats - Statistiques globales
  - GET /api/export - Exporter en CSV/JSON
- Créer une interface web simple pour visualiser les données
- Supporter la suppression des données anciennes (> 1 heure)
- Gérer les requêtes concurrentes
- Capturer en arrière-plan pendant que l'API tourne

Structure attendue:
/exercice_8/
├── sniffer.py - Capture des paquets
├── database.py - Gestion SQLite
├── api.py - API Flask/FastAPI
├── web/
│   └── index.html - Interface web
└── requirements.txt

Indices:
- Utiliser SQLite avec sqlite3
- Créer une table: CREATE TABLE packets (id, timestamp, src_ip, dst_ip, protocol, port, data)
- Utiliser threading pour capturer en arrière-plan
- Utiliser Flask ou FastAPI pour l'API
- Implémenter la pagination avec LIMIT et OFFSET
- Ajouter des index sur les colonnes fréquemment filtrées
