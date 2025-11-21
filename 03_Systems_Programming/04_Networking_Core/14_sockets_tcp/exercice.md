================================================================================
```python
                        EXERCICE 14 - SOCKETS TCP
                    8 Défis Progressifs de Maîtrise
```
================================================================================

AVERTISSEMENT ÉTHIQUE :
Tous les exercices doivent être réalisés uniquement sur vos propres systèmes
ou avec autorisation écrite. L'utilisation non autorisée de ces techniques
est ILLÉGALE.

================================================================================
## Défi 1: CLIENT TCP BASIQUE
================================================================================

Créez un programme qui :
1. Se connecte à un serveur web (exemple : example.com sur le port 80)
2. Envoie une requête HTTP GET pour la page d'accueil
3. Reçoit et affiche la réponse complète
4. Gère proprement les erreurs de connexion et timeout
5. Affiche le nombre total d'octets reçus

Contraintes :
- Utiliser socket.socket() pour créer le socket
- Définir un timeout de 5 secondes
- Recevoir les données par chunks de 4096 octets
- Fermer proprement le socket après utilisation

Format de sortie attendu :
---
Connexion à example.com:80...
Connecté avec succès !

Envoi de la requête GET...
Réception de la réponse...

[Réponse HTTP complète]

Total reçu : 1256 octets
Socket fermé
---

================================================================================
## Défi 2: SERVEUR ECHO TCP
================================================================================

Créez un serveur TCP qui :
1. Écoute sur 0.0.0.0:8888
2. Accepte les connexions entrantes
3. Reçoit les messages des clients
4. Renvoie chaque message en écho avec le préfixe "ECHO: "
5. Gère plusieurs clients séquentiellement (un à la fois)
6. Affiche l'adresse IP et le port de chaque client connecté
7. Continue d'écouter après chaque déconnexion
8. S'arrête proprement avec Ctrl+C

Contraintes :
- Utiliser bind() sur toutes les interfaces (0.0.0.0)
- Activer SO_REUSEADDR pour réutiliser le port
- Buffer de réception de 1024 octets
- Logger chaque connexion/déconnexion

Format de sortie attendu :
---
[*] Serveur echo démarré sur 0.0.0.0:8888
[*] En attente de connexions...

[+] Client connecté : 192.168.1.100:54321
[>] Reçu : "Hello Server"
[<] Envoyé : "ECHO: Hello Server"
[-] Client déconnecté

[+] Client connecté : 192.168.1.101:54322
[>] Reçu : "Test message"
[<] Envoyé : "ECHO: Test message"
[-] Client déconnecté

[*] Arrêt du serveur...
---

================================================================================
## Défi 3: BANNER GRABBER
================================================================================

Créez un outil de banner grabbing qui :
1. Prend en paramètre une adresse IP et un port
2. Se connecte au service
3. Récupère le banner (si disponible)
4. Détecte le type de service (SSH, FTP, HTTP, SMTP, etc.)
5. Extrait les informations de version si présentes
6. Affiche les résultats de manière structurée
7. Gère les timeouts et erreurs

Pour la détection, recherchez ces patterns :
- SSH : contient "SSH"
- FTP : contient "FTP"
- HTTP : contient "HTTP" ou "Server:"
- SMTP : commence par "220"
- POP3 : commence par "+OK"

Contraintes :
- Timeout de 3 secondes
- Gérer les services sans banner automatique
- Extraire le nom et la version du service

Format de sortie attendu :
---
=== BANNER GRABBING ===

Cible : 192.168.1.1:22
Timeout : 3s

[+] Port ouvert
[+] Banner récupéré :
SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.1

[*] Analyse :
    Service : SSH
```python
    Produit : OpenSSH
    Version : 8.9p1
    OS      : Ubuntu

```
Temps écoulé : 0.45s
---

================================================================================
## Défi 4: SCANNER DE PORTS MULTI-THREADING
================================================================================

Créez un scanner de ports qui :
1. Scanne une plage de ports sur une cible
2. Utilise le multithreading pour accélérer le scan
3. Détecte les ports ouverts
4. Tente de récupérer le banner pour chaque port ouvert
5. Affiche une barre de progression
6. Génère un rapport final avec tous les ports ouverts
7. Calcule et affiche le temps total de scan

Contraintes :
- Utiliser threading.Thread pour le parallélisme
- Maximum 50 threads simultanés
- Timeout de 0.5 secondes par port
- Ports communs à scanner : 21,22,23,25,53,80,110,143,443,445,3306,3389,8080

Format de sortie attendu :
---
=== SCANNER DE PORTS ===

Cible    : 192.168.1.1
Ports    : 1-1000
Threads  : 50
Timeout  : 0.5s

Scan en cours...
[████████████████████████████████████] 100% (1000/1000)

=== RÉSULTATS ===

Ports ouverts : 5

Port   Service    Banner
----   --------   --------------------------------------------------
22     SSH        SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.1
80     HTTP       HTTP/1.1 200 OK\r\nServer: nginx/1.18.0
443    HTTPS      [SSL/TLS]
3306   MySQL      5.7.40-0ubuntu0.18.04.1
8080   HTTP-Alt   HTTP/1.1 200 OK\r\nServer: Apache/2.4.41

Temps total : 12.34s
Ports/sec   : 81.03
---

================================================================================
## Défi 5: CLIENT HTTP PERSONNALISÉ
================================================================================

Créez un client HTTP bas niveau qui :
1. Effectue des requêtes HTTP GET, POST, PUT, DELETE
2. Permet de spécifier des headers personnalisés
3. Gère le body pour POST/PUT
4. Parse la réponse HTTP (status, headers, body)
5. Suit les redirections (301, 302)
6. Gère HTTPS avec le module ssl (optionnel)
7. Affiche la requête envoyée et la réponse reçue

Fonctionnalités :
- Méthode HTTP configurable
- Headers personnalisés (User-Agent, Cookie, etc.)
- Body pour POST/PUT
- Affichage détaillé du status code
- Extraction des headers de réponse

Contraintes :
- Construire manuellement la requête HTTP
- Parser manuellement la réponse
- Timeout de 10 secondes
- Support des codes de status courants

Format de sortie attendu :
---
=== CLIENT HTTP PERSONNALISÉ ===

URL    : http://example.com/api/users
Method : POST
Headers:
  User-Agent: CustomHTTPClient/1.0
  Content-Type: application/json
  Content-Length: 45

Body:
{"username": "test", "email": "test@test.com"}

--- REQUÊTE ENVOYÉE ---
POST /api/users HTTP/1.1
Host: example.com
User-Agent: CustomHTTPClient/1.0
Content-Type: application/json
Content-Length: 45

{"username": "test", "email": "test@test.com"}

--- RÉPONSE REÇUE ---
HTTP/1.1 201 Created
Server: nginx/1.18.0
Content-Type: application/json
Content-Length: 78
Date: Thu, 07 Nov 2024 14:30:00 GMT

{"id": 123, "username": "test", "email": "test@test.com", "created": "2024-11-07"}

Status : 201 Created
Temps  : 0.234s
---

================================================================================
## Défi 6: SERVEUR WEB MINIMAL
================================================================================

Créez un serveur web HTTP minimaliste qui :
1. Écoute sur le port 8080
2. Parse les requêtes HTTP (méthode, path, headers)
3. Sert des fichiers statiques depuis un dossier ./www/
4. Génère des réponses HTTP valides
5. Gère les codes d'erreur (404, 403, 500)
6. Détecte le Content-Type selon l'extension
7. Affiche les logs de chaque requête
8. Gère plusieurs clients simultanément avec threading

Fonctionnalités :
- GET pour récupérer des fichiers
- Index automatique (index.html)
- Types MIME : .html, .css, .js, .jpg, .png, .txt
- Codes HTTP : 200, 403, 404, 500
- Headers : Content-Type, Content-Length, Date

Contraintes :
- Parser manuellement les requêtes HTTP
- Construire les réponses HTTP conformes RFC
- Thread par client pour concurrence
- Logging format Apache-like

Format de sortie attendu :
---
=== SERVEUR WEB MINIMAL ===

Document root : ./www/
Adresse       : 0.0.0.0:8080

[*] Serveur démarré
[*] En attente de connexions...

[2024-11-07 14:30:15] 192.168.1.100 - "GET /index.html HTTP/1.1" 200 1534
[2024-11-07 14:30:16] 192.168.1.100 - "GET /style.css HTTP/1.1" 200 2341
[2024-11-07 14:30:17] 192.168.1.100 - "GET /script.js HTTP/1.1" 200 876
[2024-11-07 14:30:18] 192.168.1.101 - "GET /admin.html HTTP/1.1" 403 134
[2024-11-07 14:30:19] 192.168.1.102 - "GET /missing.html HTTP/1.1" 404 178

[*] Arrêt du serveur...
---

================================================================================
## Défi 7: REVERSE SHELL (ÉDUCATIF)
================================================================================

ATTENTION : Exercice uniquement pour environnements de test contrôlés !

Créez un système de reverse shell composé de :

1. HANDLER (serveur) qui :
   - Écoute sur un port configurable
   - Accepte une connexion reverse shell
   - Permet d'envoyer des commandes
   - Affiche les résultats d'exécution
   - Gère la déconnexion proprement

2. CLIENT (payload) qui :
   - Se connecte au handler
   - Reçoit les commandes
   - Exécute les commandes avec subprocess
   - Renvoie les résultats (stdout + stderr)
   - Gère les erreurs d'exécution

Contraintes :
- Handler : écoute sur 0.0.0.0:4444
- Client : se connecte à l'IP du handler
- Exécution des commandes avec subprocess.run()
- Gestion des erreurs et timeout
- Commandes : 'exit' pour quitter, 'clear' pour effacer

> [!IMPORTANT]
- Uniquement pour tests dans vos propres labs
- JAMAIS sur des systèmes non autorisés
- Inclure avertissement dans le code

Format de sortie attendu :

HANDLER :
---
=== REVERSE SHELL HANDLER ===

AVERTISSEMENT : Outil éducatif uniquement !

[*] Écoute sur 0.0.0.0:4444...
[+] Connexion reverse shell reçue de 192.168.1.100:54321

shell> whoami
testuser

shell> pwd
/home/testuser

shell> ls -la
total 48
drwxr-xr-x 5 testuser testuser 4096 Nov  7 14:30 .
drwxr-xr-x 3 root     root     4096 Nov  1 10:00 ..
-rw-r--r-- 1 testuser testuser  220 Nov  1 10:00 .bash_logout

shell> exit
[*] Session terminée
---

CLIENT :
---
=== REVERSE SHELL CLIENT ===

AVERTISSEMENT : Outil éducatif uniquement !

[*] Connexion au handler 192.168.1.1:4444...
[+] Connecté !
[*] En attente de commandes...

[>] Commande reçue : whoami
[<] Résultat envoyé (9 octets)

[>] Commande reçue : pwd
[<] Résultat envoyé (18 octets)

[>] Commande reçue : exit
[*] Déconnexion
---

================================================================================
## Défi 8: FRAMEWORK DE RECONNAISSANCE RÉSEAU
================================================================================

Créez un framework complet de reconnaissance réseau qui combine :

1. SCANNER DE RÉSEAU :
   - Découverte d'hôtes actifs (ping sweep)
   - Scan de ports sur chaque hôte
   - Banner grabbing automatique
   - Détection d'OS (basique)

2. COLLECTE D'INFORMATIONS :
   - Résolution DNS (forward et reverse)
   - Identification des services
   - Extraction des versions
   - Détection de vulnérabilités connues (CVE lookup basique)

3. RAPPORT :
   - Format JSON et texte
   - Tableau récapitulatif
   - Graphe de topologie (ASCII art)
   - Recommandations de sécurité

4. INTERFACE :
   - Menu interactif
   - Mode batch (fichier de cibles)
   - Options de configuration (threads, timeout, verbosité)
   - Barre de progression

Fonctionnalités avancées :
- Multithreading pour performance
- Sauvegarde/chargement de scans
- Comparaison de scans (diff)
- Export vers autres outils (Nmap XML)

Contraintes :
- Architecture modulaire (classes)
- Gestion robuste des erreurs
- Logging détaillé
- Configuration via fichier JSON
- Code commenté et documenté

Format de sortie attendu :
---
╔═══════════════════════════════════════════════════════════════╗
║          FRAMEWORK DE RECONNAISSANCE RÉSEAU v1.0              ║
╠═══════════════════════════════════════════════════════════════╣
║  AVERTISSEMENT : Utilisation autorisée uniquement !           ║
╚═══════════════════════════════════════════════════════════════╝

=== CONFIGURATION ===
Réseau cible  : 192.168.1.0/24
Ports         : 21,22,23,25,80,443,3306,3389,8080
Threads       : 50
Timeout       : 1s
Banner grab   : Activé
OS detection  : Activé

=== PHASE 1 : DÉCOUVERTE D'HÔTES ===
Scan du réseau 192.168.1.0/24...
[████████████████████████████████████] 100% (254/254)

Hôtes actifs : 12

=== PHASE 2 : SCAN DE PORTS ===
Scan des ports sur 12 hôtes...
[████████████████████████████████████] 100% (12/12)

Ports ouverts : 48

=== PHASE 3 : BANNER GRABBING ===
Collecte des banners...
[████████████████████████████████████] 100% (48/48)

Banners récupérés : 41

=== RÉSULTATS ===

┌─────────────────────────────────────────────────────────────────────┐
│ HÔTE          │ PORTS     │ SERVICES                               │
├─────────────────────────────────────────────────────────────────────┤
│ 192.168.1.1   │ 80, 443   │ HTTP (nginx 1.18.0), HTTPS            │
│ 192.168.1.10  │ 22, 80    │ SSH (OpenSSH 8.9p1), HTTP (Apache)   │
│ 192.168.1.50  │ 3306      │ MySQL (5.7.40)                        │
│ 192.168.1.100 │ 22, 3389  │ SSH, RDP (Windows Server 2019)        │
│ ...           │ ...       │ ...                                    │
└─────────────────────────────────────────────────────────────────────┘

=== VULNÉRABILITÉS POTENTIELLES ===

[!] CRITIQUE
```python
    • 192.168.1.10 : OpenSSH 8.9p1 - CVE-2023-XXXX (RCE)
    • 192.168.1.50 : MySQL 5.7.40 - Version obsolète

```
[!] ATTENTION
```python
    • 192.168.1.1 : nginx 1.18.0 - Mise à jour disponible
    • 192.168.1.100 : RDP exposé - Risque de bruteforce

```
=== RECOMMANDATIONS ===

1. Mettre à jour OpenSSH sur 192.168.1.10
2. Restreindre l'accès MySQL (192.168.1.50)
3. Activer NLA pour RDP (192.168.1.100)
4. Configurer un firewall pour filtrer les services exposés

=== STATISTIQUES ===

Durée totale      : 45.67s
Hôtes scannés     : 12
Ports testés      : 108
Taux de scan      : 2.36 ports/sec
Banners collectés : 41

=== EXPORTS ===

✓ Rapport JSON : scan_192.168.1.0_20241107_143045.json
✓ Rapport TXT  : scan_192.168.1.0_20241107_143045.txt
✓ Nmap XML     : scan_192.168.1.0_20241107_143045.xml

Scan terminé.
---

================================================================================
```python
                            FIN DES EXERCICES
```
================================================================================

Conseils pour réussir :
1. Testez d'abord sur localhost (127.0.0.1)
2. Utilisez toujours des timeouts pour éviter les blocages
3. Gérez TOUTES les exceptions possibles
4. Fermez proprement tous les sockets
5. Loggez les actions pour déboguer
6. Respectez TOUJOURS les lois et l'éthique
7. Documentez votre code
8. Testez dans un environnement isolé (VM, Docker)

Ressources utiles :
- Documentation Python socket : docs.python.org/3/library/socket.html
- RFC 793 (TCP) : www.rfc-editor.org/rfc/rfc793
- OWASP Testing Guide : owasp.org

> [!IMPORTANT] Ces exercices sont destinés à l'apprentissage de la cybersécurité
défensive. Toute utilisation malveillante est de votre seule responsabilité.
