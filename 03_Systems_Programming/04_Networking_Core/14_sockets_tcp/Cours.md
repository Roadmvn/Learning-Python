# Exercice 14 - Sockets TCP

## Objectifs d'Apprentissage

Maîtriser les sockets TCP en Python pour la communication réseau et comprendre leur utilisation en cybersécurité et red teaming :

- Comprendre le protocole TCP/IP et le modèle client-serveur
- Créer et manipuler des sockets avec le module `socket`
- Implémenter un client TCP pour se connecter à des services distants
- Implémenter un serveur TCP pour écouter des connexions entrantes
- Gérer les connexions, l'envoi et la réception de données
- Appliquer les sockets aux techniques de reconnaissance réseau
- Développer des outils simples pour le red teaming

## Avertissement Éthique

**IMPORTANT** : Les techniques présentées dans cet exercice sont destinées uniquement à des fins éducatives et de sécurité défensive. L'utilisation de ces outils pour :

- Scanner des systèmes sans autorisation écrite préalable
- Accéder à des services ou réseaux sans permission
- Compromettre la disponibilité de services
- Collecter des informations sur des cibles non autorisées

est **ILLÉGALE** et peut entraîner des poursuites judiciaires. Utilisez ces connaissances uniquement :

- Sur vos propres systèmes et réseaux
- Dans des environnements de test autorisés (labs, CTF, bug bounty)
- Avec une autorisation écrite explicite du propriétaire du système
- Dans le cadre de missions professionnelles légitimes de sécurité

## Concepts Clés

### Module socket

Le module `socket` de Python fournit une interface pour la programmation réseau :

```python
import socket

# Création d'un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

**Paramètres principaux** :
- `AF_INET` : Famille d'adresses IPv4
- `AF_INET6` : Famille d'adresses IPv6
- `SOCK_STREAM` : Socket TCP (connexion fiable)
- `SOCK_DGRAM` : Socket UDP (sans connexion)

### Protocole TCP/IP

TCP (Transmission Control Protocol) est un protocole de transport fiable :

```
Modèle OSI - Couches Réseau:
┌─────────────────────────────────────┐
│ Application (HTTP, FTP, SSH, etc.)  │ ← Couche 7
├─────────────────────────────────────┤
│ Présentation                        │ ← Couche 6
├─────────────────────────────────────┤
│ Session                             │ ← Couche 5
├─────────────────────────────────────┤
│ Transport (TCP/UDP)                 │ ← Couche 4 (Sockets)
├─────────────────────────────────────┤
│ Réseau (IP)                         │ ← Couche 3
├─────────────────────────────────────┤
│ Liaison de données                  │ ← Couche 2
├─────────────────────────────────────┤
│ Physique                            │ ← Couche 1
└─────────────────────────────────────┘
```

**Caractéristiques TCP** :
- Connexion établie avant transmission (handshake 3-way)
- Fiabilité : retransmission des paquets perdus
- Ordre garanti : les données arrivent dans l'ordre d'envoi
- Contrôle de flux et de congestion

**Three-Way Handshake** :
```
Client                    Serveur
  |                          |
  |-------- SYN ------------>|  (1) Client demande connexion
  |                          |
  |<------ SYN-ACK ----------|  (2) Serveur accepte
  |                          |
  |-------- ACK ------------>|  (3) Client confirme
  |                          |
  |<==== Connexion établie ==>|
```

### Socket Client TCP

Un client TCP se connecte à un serveur distant :

```python
# Création du socket client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur (host, port)
client.connect(("192.168.1.100", 80))

# Envoi de données
client.send(b"GET / HTTP/1.1\r\n\r\n")

# Réception de données
response = client.recv(4096)

# Fermeture
client.close()
```

**Méthodes principales** :
- `connect(address)` : Établit la connexion au serveur
- `send(data)` : Envoie des données (bytes)
- `sendall(data)` : Envoie toutes les données (préféré)
- `recv(bufsize)` : Reçoit des données (max bufsize octets)
- `close()` : Ferme la connexion

### Socket Serveur TCP

Un serveur TCP écoute et accepte les connexions entrantes :

```python
# Création du socket serveur
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liaison à une adresse et un port
server.bind(("0.0.0.0", 9999))

# Écoute des connexions (backlog=5)
server.listen(5)

# Acceptation d'une connexion
client_socket, client_address = server.accept()

# Communication avec le client
data = client_socket.recv(1024)
client_socket.send(b"Response")

# Fermeture
client_socket.close()
server.close()
```

**Méthodes principales** :
- `bind(address)` : Lie le socket à une adresse/port
- `listen(backlog)` : Écoute les connexions (backlog = file d'attente)
- `accept()` : Accepte une connexion (bloquant)
- `close()` : Ferme le socket

### Fonctions bind, listen, accept, connect

**Cycle de vie d'une connexion TCP** :

```
Serveur                          Client
  |                                |
socket()                        socket()
  |                                |
bind()                             |
  |                                |
listen()                           |
  |                                |
accept() [BLOQUE]                  |
  |                            connect()
  |<-------- SYN --------------- |
  |------- SYN-ACK ----------->  |
  |<-------- ACK --------------- |
accept() [RETOURNE]                |
  |                                |
recv()/send() <-------------> send()/recv()
  |                                |
close()                        close()
```

**Explications détaillées** :

1. `bind(address)` : Associe le socket à une adresse IP et un port
   - `("0.0.0.0", port)` : Écoute sur toutes les interfaces
   - `("127.0.0.1", port)` : Écoute uniquement en local
   - Nécessite des privilèges pour les ports < 1024

2. `listen(backlog)` : Met le socket en mode écoute
   - `backlog` : Nombre max de connexions en attente
   - Le socket devient un "listening socket"

3. `accept()` : Accepte une connexion entrante
   - Bloque jusqu'à l'arrivée d'une connexion
   - Retourne un nouveau socket et l'adresse du client
   - Le nouveau socket gère la communication avec ce client

4. `connect(address)` : Initie une connexion au serveur
   - Lance le three-way handshake
   - Bloque jusqu'à établissement ou timeout
   - Lève une exception en cas d'échec

### Envoi et Réception de Données (send/recv)

**Envoi de données** :

```python
# send() - peut envoyer moins que demandé
bytes_sent = sock.send(b"Hello")

# sendall() - envoie tout ou lève une exception
sock.sendall(b"Complete message")

# Envoi de texte (encode en bytes)
message = "GET / HTTP/1.1\r\n"
sock.sendall(message.encode('utf-8'))
```

**Réception de données** :

```python
# recv() - reçoit jusqu'à bufsize octets
data = sock.recv(4096)

# Réception en boucle jusqu'à fermeture
all_data = b""
while True:
    chunk = sock.recv(4096)
    if not chunk:  # Connexion fermée
        break
    all_data += chunk

# Décodage en texte
text = data.decode('utf-8')
```

**Points importants** :
- Les sockets TCP transmettent des flux d'octets (bytes)
- `recv()` ne garantit pas de recevoir tout ce qui a été envoyé
- Une boucle est souvent nécessaire pour recevoir toutes les données
- `recv()` retourne `b""` quand la connexion est fermée

### Fermeture des Sockets

**Méthodes de fermeture** :

```python
# Fermeture complète
sock.close()

# Fermeture partielle (shutdown)
sock.shutdown(socket.SHUT_WR)   # Plus d'envoi
sock.shutdown(socket.SHUT_RD)   # Plus de réception
sock.shutdown(socket.SHUT_RDWR) # Plus d'envoi ni réception

# Utilisation avec context manager (recommandé)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(("example.com", 80))
    # ... utilisation ...
    # Fermeture automatique en sortie du bloc
```

**Bonnes pratiques** :
- Toujours fermer les sockets après utilisation
- Utiliser `try/finally` ou context managers
- `shutdown()` avant `close()` pour connexions propres

### Banner Grabbing

Le banner grabbing consiste à récupérer les informations d'identification d'un service :

```python
def grab_banner(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        sock.connect((ip, port))

        # Certains services envoient un banner automatiquement
        banner = sock.recv(1024)

        sock.close()
        return banner.decode('utf-8', errors='ignore')
    except:
        return None
```

**Applications en reconnaissance** :
- Identification des services et versions
- Détection de vulnérabilités connues
- Fingerprinting de systèmes
- Collecte d'informations pour l'exploitation

**Services courants avec banners** :
- FTP (port 21) : Version du serveur FTP
- SSH (port 22) : Version OpenSSH
- Telnet (port 23) : Système d'exploitation
- SMTP (port 25) : Serveur de mail
- HTTP (port 80) : Serveur web
- POP3 (port 110) : Serveur mail
- IMAP (port 143) : Serveur mail

## Applications en Red Teaming

### Reconnaissance Réseau

```python
# Scanner de ports simple
for port in range(1, 1024):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((target_ip, port))
    if result == 0:
        print(f"Port {port} ouvert")
    sock.close()
```

### Clients Personnalisés

```python
# Client HTTP basique pour requêtes manuelles
def http_request(host, port, path):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    request = f"GET {path} HTTP/1.1\r\n"
    request += f"Host: {host}\r\n"
    request += "Connection: close\r\n\r\n"

    sock.sendall(request.encode())
    response = sock.recv(4096)
    sock.close()

    return response.decode('utf-8', errors='ignore')
```

### Reverse Shell (Éducatif)

```python
# Serveur de reverse shell (handler)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 4444))
server.listen(1)
print("[*] En attente de connexion...")
client, addr = server.accept()
print(f"[+] Connexion reçue de {addr}")

while True:
    command = input("shell> ")
    if command.lower() == "exit":
        break
    client.send(command.encode())
    output = client.recv(4096)
    print(output.decode('utf-8', errors='ignore'))

client.close()
server.close()
```

## Structure des Fichiers

```
14_sockets_tcp/
├── README.md        # Ce fichier (théorie et concepts)
├── main.py          # Exemples et démonstrations
├── exercice.txt     # 8 défis progressifs
└── solution.txt     # Solutions complètes
```

## Prérequis

- Compréhension des réseaux TCP/IP (bases)
- Connaissance des adresses IP et des ports
- Maîtrise des exceptions Python
- Compréhension du modèle client-serveur

## Commandes Utiles

```bash
# Tester un serveur TCP local
python3 main.py  # Lance les exemples

# Scanner réseau avec nmap (comparaison)
nmap -sT -p 1-1000 192.168.1.1

# Écouter sur un port avec netcat
nc -l -p 4444

# Se connecter à un service avec netcat
nc 192.168.1.100 80

# Afficher les connexions réseau actives
netstat -ant | grep LISTEN

# Vérifier si un port est ouvert
telnet 192.168.1.100 80
```

## Ressources Supplémentaires

- Documentation Python socket : https://docs.python.org/3/library/socket.html
- RFC 793 (TCP) : https://www.rfc-editor.org/rfc/rfc793
- OWASP Testing Guide : https://owasp.org/www-project-web-security-testing-guide/
- Black Hat Python (livre) : Techniques de sécurité avec Python

## Prochaines Étapes

Après avoir maîtrisé les sockets TCP, vous pourrez explorer :

- **Threading** (Exercice 15) : Serveurs multi-clients simultanés
- **Subprocess** (Exercice 16) : Exécution de commandes à distance
- **Sockets UDP** : Communication sans connexion
- **SSL/TLS** : Sockets sécurisés (module `ssl`)
- **Scapy** : Manipulation de paquets réseau
- **Frameworks** : Twisted, asyncio pour programmation réseau avancée
