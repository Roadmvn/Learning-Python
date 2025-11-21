========================================
# Exercice 15: THREADING EN PYTHON
Défis progressifs avec focus cybersécurité
========================================

Complétez ces exercices pour maîtriser le threading en Python.
Testez votre code et vérifiez les résultats.

========================================
## Défi 1: Scan de Ports Simple
========================================

Objectif : Créer un scanner de ports multi-threadé basique

Créez un script qui :
- Définit une fonction scan_port(host, port) qui tente une connexion TCP
- Utilise socket pour tester si un port est ouvert
- Scanne une liste de 20 ports communs (21, 22, 23, 25, 80, 443, etc.)
- Crée un thread pour chaque port
- Affiche les ports ouverts trouvés
- Utilise un Lock pour protéger la liste des résultats

Contraintes :
- Timeout de 1 seconde pour chaque connexion
- Scanner localhost (127.0.0.1)
- Afficher le temps total d'exécution
- Comparer avec une version séquentielle

Indications :
- socket.socket(socket.AF_INET, socket.SOCK_STREAM)
- sock.connect_ex((host, port))
- sock.settimeout(timeout)
- threading.Lock() pour synchronisation

Exemple de sortie attendue :
Scan séquentiel de 127.0.0.1...
Temps: 20.5s
Ports ouverts: []

Scan multi-threadé de 127.0.0.1...
Port 80 : fermé
Port 443 : fermé
[...]
Temps: 1.2s
Ports ouverts: []
Amélioration: 17.1x plus rapide

========================================
## Défi 2: Bruteforce SSH Simulé
========================================

Objectif : Créer un outil de bruteforce multi-threadé

Créez un script qui :
- Définit une fonction check_password(username, password) simulée
- Le mot de passe correct est "S3cur3P@ss2024"
- Charge une wordlist de 100 mots de passe
- Utilise ThreadPoolExecutor avec 10 workers
- S'arrête dès qu'un mot de passe est trouvé
- Utilise un Event pour signaler la découverte
- Compte le nombre de tentatives effectuées

Contraintes :
- Simuler un délai de 0.1s par tentative
- Utiliser threading.Event() pour arrêter les threads
- Thread-safe pour le compteur de tentatives
- Afficher le mot de passe trouvé et le nombre de tentatives

Wordlist de test :
admin, password, 123456, qwerty, letmein, welcome,
monkey, dragon, master, sunshine, S3cur3P@ss2024, ...

Indications :
- concurrent.futures.ThreadPoolExecutor
- threading.Event() avec set() et is_set()
- Lock pour protéger le compteur
- time.sleep() pour simuler le délai réseau

Exemple de sortie attendue :
Bruteforce en cours...
[Thread-1] Tentative: admin:admin
[Thread-2] Tentative: admin:password
[Thread-3] Tentative: admin:123456
...
[Thread-7] SUCCESS! Mot de passe trouvé: S3cur3P@ss2024
Arrêt des threads...

Statistiques:
- Tentatives: 47
- Temps: 5.2s
- Mot de passe: S3cur3P@ss2024

========================================
## Défi 3: Énumération de Répertoires Web
========================================

Objectif : Créer un outil d'énumération de répertoires multi-threadé

Créez un script qui :
- Définit une fonction check_directory(url) simulée
- Teste une liste de 50 chemins communs (/admin, /backup, etc.)
- Utilise une Queue pour distribuer le travail
- Crée 5 threads workers qui consomment la queue
- Simule des codes HTTP (200, 404, 403, 301, 500)
- Affiche uniquement les répertoires trouvés (200, 301, 302)
- Compte les résultats par code de statut

Contraintes :
- Utiliser queue.Queue()
- Pattern producer-consumer
- Gérer proprement l'arrêt des workers
- Afficher une barre de progression (pourcentage)

Répertoires à tester :
/admin, /backup, /config, /uploads, /api, /test, /dev,
/login, /dashboard, /panel, /wp-admin, /administrator,
/phpmyadmin, /sql, /database, /files, /images, /css,
/js, /includes, /logs, /temp, /cache, /old, /new,
/hidden, /secret, /private, /public, /data, /downloads,
/docs, /documentation, /help, /support, /contact,
/about, /profile, /settings, /search, /register,
/forgot, /reset, /verify, /confirm, /activate,
/newsletter, /subscribe, /unsubscribe, /shop, /cart

Indications :
- Queue.put() et Queue.get()
- Queue.task_done() et Queue.join()
- None comme signal de fin pour les workers

Exemple de sortie attendue :
Énumération de http://example.com (50 chemins, 5 workers)
================================================
Progression: [##########          ] 50%

[+] 200 - /admin
[+] 200 - /api
[+] 301 - /uploads
[!] 403 - /config
[+] 200 - /dashboard
...

Progression: [####################] 100%

Résultats:
==========
Total scanné: 50
200 OK: 8
301 Redirect: 3
403 Forbidden: 2
404 Not Found: 35
500 Error: 2

Chemins accessibles:
- /admin
- /api
- /uploads (redirect)
- /dashboard
...

========================================
## Défi 4: Download Manager Concurrent
========================================

Objectif : Créer un gestionnaire de téléchargements multi-threadé

Créez un script qui :
- Simule le téléchargement de 10 fichiers
- Chaque fichier a une taille aléatoire (1-10 MB)
- Utilise ThreadPoolExecutor avec 3 workers
- Affiche la progression de chaque téléchargement
- Calcule la vitesse de téléchargement globale
- Utilise Lock pour les statistiques partagées

Contraintes :
- Simuler le téléchargement par chunks de 1MB
- Délai de 0.5s par chunk (simuler I/O réseau)
- Afficher progression en pourcentage pour chaque fichier
- Calculer et afficher la vitesse moyenne (MB/s)

Informations :
- Files: file1.zip, file2.iso, file3.tar.gz, etc.
- Tailles aléatoires entre 1 et 10 MB

Indications :
- random.randint(1, 10) pour taille
- Boucle sur les chunks
- Lock pour statistiques globales
- time.time() pour calcul de vitesse

Exemple de sortie attendue :
Téléchargement de 10 fichiers (3 workers simultanés)
====================================================

[Worker-1] file1.zip (5 MB)
  Progression: [####                ] 20% (1/5 MB)
[Worker-2] file2.iso (8 MB)
  Progression: [##                  ] 10% (1/8 MB)
[Worker-3] file3.tar.gz (3 MB)
  Progression: [#######             ] 33% (1/3 MB)

[Worker-3] file3.tar.gz (3 MB) - TERMINÉ
[Worker-3] file4.bin (7 MB)
  Progression: [###                 ] 14% (1/7 MB)

...

Statistiques finales:
====================
Total téléchargé: 52 MB
Temps total: 26.3s
Vitesse moyenne: 1.98 MB/s
Fichiers: 10
Succès: 10

========================================
## Défi 5: Fuzzer HTTP Multi-threadé
========================================

Objectif : Créer un fuzzer HTTP simple avec threading

Créez un script qui :
- Génère des payloads de fuzzing (100 payloads)
- Types: SQLi, XSS, Path Traversal, Command Injection
- Teste chaque payload sur un endpoint simulé
- Utilise 10 threads pour tester en parallèle
- Détecte les réponses anormales (erreurs, codes spéciaux)
- Sauvegarde les payloads qui déclenchent des erreurs

Contraintes :
- Simuler des requêtes HTTP avec délai aléatoire (0.1-0.5s)
- Détecter codes 500, temps de réponse > 2s, messages d'erreur
- Thread-safe pour écriture des résultats
- Afficher statistiques en temps réel

Payloads de test :
SQLi: ' OR '1'='1, " OR "1"="1, ' AND 1=1--, ...
XSS: <script>alert(1)</script>, <img src=x onerror=alert(1)>, ...
Path Traversal: ../../etc/passwd, ..\..\windows\system32\, ...
Command Injection: ; ls -la, | cat /etc/passwd, ...

Indications :
- Créer une classe Payload avec type et contenu
- random.uniform() pour délai aléatoire
- Détecter patterns d'erreur dans réponse simulée
- Sauvegarder dans fichier results.txt

Exemple de sortie attendue :
Fuzzing HTTP - 100 payloads, 10 threads
========================================

[Thread-1] Testing: ' OR '1'='1
[Thread-2] Testing: <script>alert(1)</script>
[Thread-3] Testing: ../../etc/passwd
...

[!] ANOMALY DETECTED!
```python
    Payload: ' AND 1=1--
    Type: SQLi
    Response: 500 Internal Server Error
    Time: 2.5s

```
[!] ANOMALY DETECTED!
```python
    Payload: ../../../../etc/passwd
    Type: Path Traversal
    Response: Error: File not found in /etc/passwd
    Time: 0.3s

```
...

Progression: [####################] 100/100

Résultats:
==========
Total payloads: 100
Tests effectués: 100
Anomalies détectées: 12
Temps total: 5.8s
Taux: 17.2 tests/s

Anomalies par type:
- SQLi: 5
- XSS: 2
- Path Traversal: 3
- Command Injection: 2

Résultats sauvegardés dans: results.txt

========================================
## Défi 6: Scanner de Vulnérabilités Concurrent
========================================

Objectif : Créer un scanner de vulnérabilités multi-modules

Créez un script qui :
- Scanne une cible avec plusieurs modules en parallèle
- Modules: Port Scanner, Directory Enum, SSL Check, DNS Enum
- Chaque module s'exécute dans son propre thread
- Utilise Queue pour communication inter-threads
- Agrège tous les résultats dans un rapport final
- Affiche progression de chaque module

Contraintes :
- 4 modules s'exécutant simultanément
- Chaque module envoie ses findings dans une Queue
- Thread principal collecte et affiche les résultats
- Format de rapport structuré

Modules :
1. Port Scanner: Scan top 20 ports
2. Directory Enum: Test 30 répertoires communs
3. SSL Check: Vérifier certificat et ciphers
4. DNS Enum: Énumérer 10 sous-domaines communs

Indications :
- Classe Module avec méthode run()
- Queue pour centraliser les résultats
- Thread pour chaque module
- Format JSON pour rapport final

Exemple de sortie attendue :
Scanner de Vulnérabilités Multi-Modules
Target: example.com
=======================================

[Port Scanner] Démarrage...
[Directory Enum] Démarrage...
[SSL Check] Démarrage...
[DNS Enum] Démarrage...

[Port Scanner] Scan de 20 ports... 50%
[Directory Enum] Test de 30 chemins... 30%
[SSL Check] Analyse SSL/TLS...
[DNS Enum] Énumération DNS... 70%

[Port Scanner] FINDING: Port 80 ouvert
[Port Scanner] FINDING: Port 443 ouvert
[Directory Enum] FINDING: /admin accessible (200)
[SSL Check] FINDING: Certificat expire dans 30 jours
[DNS Enum] FINDING: Sous-domaine trouvé: mail.example.com

[Port Scanner] Terminé (2 findings)
[Directory Enum] Terminé (1 finding)
[SSL Check] Terminé (1 finding)
[DNS Enum] Terminé (1 finding)

Rapport Final
=============
Target: example.com
Date: 2024-01-15 14:30:00
Durée: 8.5s

Port Scanner:
  - Port 80/tcp ouvert (HTTP)
  - Port 443/tcp ouvert (HTTPS)

Directory Enumeration:
  - /admin (200 OK)

SSL/TLS Analysis:
  - Certificat expire: 2024-02-15 (30 jours)

DNS Enumeration:
  - mail.example.com (192.168.1.10)

Total Findings: 5
Sévérité: MOYENNE

========================================
## Défi 7: Rate-Limited API Scraper
========================================

Objectif : Créer un scraper avec rate limiting et retry

Créez un script qui :
- Scrape 200 URLs via une API simulée
- Rate limit: 10 requêtes par seconde maximum
- Utilise Semaphore pour limiter concurrence
- Implémente retry avec backoff exponentiel
- Gère les erreurs et timeouts
- Affiche statistiques en temps réel

Contraintes :
- Semaphore(10) pour limiter à 10 threads simultanés
- Retry jusqu'à 3 fois en cas d'échec
- Backoff: 1s, 2s, 4s entre retries
- Thread-safe pour compteurs
- Sauvegarder résultats dans fichier JSON

Indications :
- threading.Semaphore(10)
- time.sleep() pour respecter rate limit
- Boucle de retry avec try/except
- Lock pour statistiques partagées

Exemple de sortie attendue :
API Scraper avec Rate Limiting
===============================
URLs: 200
Rate Limit: 10 req/s
Max Retries: 3

[00:01] Progression: 10/200 (5%) | Succès: 9 | Erreurs: 1
[00:02] Progression: 22/200 (11%) | Succès: 20 | Erreurs: 2
[00:03] Progression: 35/200 (17%) | Succès: 32 | Erreurs: 3

[!] URL 15: Erreur 500, retry 1/3 dans 1s...
[+] URL 15: Succès après retry
[!] URL 28: Erreur timeout, retry 1/3 dans 1s...
[!] URL 28: Erreur timeout, retry 2/3 dans 2s...
[+] URL 28: Succès après retry

[00:20] Progression: 200/200 (100%) | Succès: 195 | Erreurs: 5

Statistiques Finales:
====================
Total URLs: 200
Succès: 195 (97.5%)
Échecs: 5 (2.5%)
Retries total: 23
Temps total: 20.5s
Taux moyen: 9.8 req/s

Résultats sauvegardés: results.json

========================================
## Défi 8: Framework de Pentesting Modulaire
========================================

Objectif : Créer un mini-framework de pentest multi-threadé

Créez un framework complet qui :
- Architecture modulaire avec plugins
- Plusieurs modules de scan en parallèle
- Système de priorités pour les tâches
- Dashboard en temps réel (thread séparé)
- Export de rapport complet

Fonctionnalités :
1. Module Manager: Charge et exécute les modules
2. Task Queue: Gère priorités et distribution
3. Result Collector: Agrège résultats
4. Dashboard Thread: Affiche stats en direct
5. Report Generator: Génère rapport final

Modules à implémenter :
- Port Scanner (priorité: HIGH)
- Service Detection (priorité: HIGH)
- Vulnerability Scan (priorité: MEDIUM)
- Directory Enumeration (priorité: MEDIUM)
- SSL/TLS Check (priorité: LOW)
- DNS Enumeration (priorité: LOW)

Contraintes :
- PriorityQueue pour tâches
- ThreadPoolExecutor pour workers
- Thread séparé pour dashboard
- Lock/Event pour synchronisation
- Gestion propre de l'arrêt

Structure du code :
- Classe Framework: Coordonne tout
- Classe Module: Interface pour modules
- Classe Task: Représente une tâche
- Classe Result: Stocke résultats
- Fonction dashboard: Affichage en temps réel

Indications :
- queue.PriorityQueue()
- concurrent.futures.ThreadPoolExecutor
- threading.Event() pour signaux
- Ordre d'exécution basé sur priorité

Exemple de sortie attendue :
===================================================
```python
    PENTEST FRAMEWORK v1.0
    Target: example.com
```
===================================================

Chargement des modules...
[+] Module chargé: PortScanner (HIGH)
[+] Module chargé: ServiceDetection (HIGH)
[+] Module chargé: VulnerabilityScan (MEDIUM)
[+] Module chargé: DirectoryEnum (MEDIUM)
[+] Module chargé: SSLCheck (LOW)
[+] Module chargé: DNSEnum (LOW)

Configuration:
- Threads: 5
- Timeout: 10s
- Verbosité: INFO

Démarrage du scan...

===================================================
```python
                    DASHBOARD
```
===================================================
Temps écoulé: 00:05
Progression globale: [########            ] 42%

Modules actifs:
  [RUNNING] PortScanner (85%)
  [RUNNING] ServiceDetection (45%)
  [QUEUED] VulnerabilityScan

Findings: 12
  - Critical: 2
  - High: 3
  - Medium: 5
  - Low: 2

Derniers findings:
  [CRITICAL] Port 22: SSH avec bannière vulnérable
  [HIGH] Port 80: Apache 2.2.15 (vulnérable CVE-2021-XXXX)
  [MEDIUM] Directory /admin accessible sans auth
===================================================

[PortScanner] Terminé - 5 findings
[ServiceDetection] Terminé - 4 findings
[VulnerabilityScan] Terminé - 8 findings
[DirectoryEnum] Terminé - 3 findings
[SSLCheck] Terminé - 2 findings
[DNSEnum] Terminé - 1 finding

Génération du rapport...

===================================================
```python
              RAPPORT DE PENTEST
```
===================================================
Target: example.com (192.168.1.100)
Date: 2024-01-15 15:45:00
Durée: 15m 32s

RÉSUMÉ:
-------
Total findings: 23
  - Critical: 2
  - High: 5
  - Medium: 10
  - Low: 6

DÉTAILS PAR MODULE:
-------------------

[1] PORT SCANNER
Ports ouverts: 5
  - 22/tcp (SSH) - OpenSSH 7.4
  - 80/tcp (HTTP) - Apache 2.2.15
  - 443/tcp (HTTPS) - Apache 2.2.15
  - 3306/tcp (MySQL) - MySQL 5.5.62
  - 8080/tcp (HTTP) - Tomcat 8.5.0

[2] SERVICE DETECTION
Services identifiés: 5
  - SSH: OpenSSH 7.4 (vulnérable)
  - HTTP: Apache 2.2.15 (obsolète)
  - MySQL: 5.5.62 (non sécurisé)

[3] VULNERABILITY SCAN
Vulnérabilités: 8
  [CRITICAL] CVE-2021-1234: SSH Remote Code Execution
  [CRITICAL] CVE-2022-5678: Apache HTTP Server Buffer Overflow
  [HIGH] CVE-2020-9999: MySQL Authentication Bypass
  ...

[4] DIRECTORY ENUMERATION
Répertoires trouvés: 3
  - /admin (200 OK) - Pas d'authentification
  - /backup (403 Forbidden)
  - /uploads (200 OK) - Directory listing activé

[5] SSL/TLS CHECK
Problèmes SSL: 2
  - Certificat auto-signé
  - Support TLS 1.0 (obsolète)

[6] DNS ENUMERATION
Sous-domaines: 1
  - mail.example.com (192.168.1.10)

RECOMMANDATIONS:
----------------
1. [URGENT] Patcher SSH (CVE-2021-1234)
2. [URGENT] Mettre à jour Apache (CVE-2022-5678)
3. [HIGH] Sécuriser /admin avec authentification
4. [MEDIUM] Désactiver directory listing sur /uploads
5. [MEDIUM] Mettre à niveau MySQL
6. [LOW] Renouveler certificat SSL

===================================================
Rapport sauvegardé: pentest_report_example.com.json
===================================================

========================================
## Conseils GÉNÉRAUX
========================================

1. Gestion des threads:
   - Toujours joindre les threads créés
   - Utiliser context managers (with) quand possible
   - Gérer proprement les exceptions dans threads

2. Synchronisation:
   - Identifier les ressources partagées
   - Utiliser Lock pour données critiques
   - Éviter les deadlocks (ordre cohérent des locks)

3. Performance:
   - Ne pas créer trop de threads
   - ThreadPoolExecutor pour limiter concurrence
   - Threads pour I/O-bound, multiprocessing pour CPU-bound

4. Red Teaming:
   - Rate limiting pour éviter détection
   - Timeout appropriés
   - Gestion des erreurs réseau
   - Logging pour audit trail

5. Debugging:
   - Nommer les threads pour traçabilité
   - Logger les exceptions
   - Utiliser thread.is_alive() pour debug
   - threading.enumerate() pour lister threads actifs

6. Sécurité:
   - Toujours obtenir autorisation avant scan
   - Respecter les rate limits
   - Ne pas surcharger les cibles
   - Usage éthique uniquement

========================================
VALIDATION
========================================

Pour chaque défi:
1. Le code s'exécute sans erreur
2. Les threads se terminent proprement
3. Pas de race conditions
4. Performance améliorée vs séquentiel
5. Gestion correcte des exceptions
6. Output clair et informatif
7. Code commenté en français
8. Respect des contraintes spécifiées

Bon courage!
