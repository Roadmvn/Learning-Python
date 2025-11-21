"""
═══════════════════════════════════════════════════════════════
EXERCICE 06 : Boucles (for et while)
═══════════════════════════════════════════════════════════════

OBJECTIF :
- Maîtriser les boucles for avec range() et itérables
- Comprendre les boucles while et contrôle de flux
- Utiliser break et continue
- Créer des boucles imbriquées
- Appliquer aux contextes de cybersécurité
- Résoudre des problèmes d'énumération et bruteforce

EXÉCUTION : python main.py

═══════════════════════════════════════════════════════════════
"""

def main():
    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 1 : Boucle for basique avec range()
    # ═══════════════════════════════════════════════════════════

    print("=== Étape 1 : Boucle for avec range() ===\n")

    # range(stop) : génère 0, 1, 2, ..., stop-1
    print("--- range(5) génère : 0, 1, 2, 3, 4 ---")
    for i in range(5):
        print(f"Itération {i}")

    # range(start, stop) : génère start, start+1, ..., stop-1
    print("\n--- range(1, 6) génère : 1, 2, 3, 4, 5 ---")
    for i in range(1, 6):
        print(f"Nombre : {i}")

    # range(start, stop, step) : génère avec un pas
    print("\n--- range(0, 10, 2) génère : 0, 2, 4, 6, 8 ---")
    for i in range(0, 10, 2):
        print(f"Nombre pair : {i}")

    # Exemple pratique : énumération de ports
    print("\n--- Énumération de ports (simulation) ---")
    print("Scan de ports courants :\n")
    common_ports = {
        21: "FTP",
        22: "SSH",
        80: "HTTP",
        443: "HTTPS",
        3306: "MySQL",
    }

    # On iterate sur les ports (keys du dictionnaire)
    for port in common_ports:
        service = common_ports[port]
        print(f"Port {port:5} : {service}")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 2 : Boucle for avec itérables
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 2 : Boucle for avec itérables ===\n")

    # Itération sur une liste
    print("--- Itération sur une liste ---")
    usernames = ["admin", "user1", "user2", "guest"]
    for username in usernames:
        print(f"Nom d'utilisateur : {username}")

    # Itération sur une chaîne de caractères
    print("\n--- Itération sur une chaîne (caractère par caractère) ---")
    password = "secret123"
    for char in password:
        print(f"Caractère : {char}")

    # Itération sur un tuple
    print("\n--- Itération sur un tuple ---")
    ports_to_scan = (21, 22, 80, 443, 3306)
    for port in ports_to_scan:
        print(f"Scanning port {port}...")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 3 : enumerate() - Accéder à l'index ET la valeur
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 3 : enumerate() ===\n")

    print("--- Liste avec index et valeur ---")
    credentials = ["user1:pass1", "user2:pass2", "user3:pass3"]
    for index, credential in enumerate(credentials):
        print(f"Position {index} : {credential}")

    # Démarrer l'index à 1 au lieu de 0
    print("\n--- Démarrer l'énumération à 1 ---")
    for attempt_number, credential in enumerate(credentials, start=1):
        print(f"Tentative {attempt_number} : {credential}")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 4 : zip() - Combiner plusieurs itérables
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 4 : zip() ===\n")

    print("--- Combiner deux listes ---")
    ports = [21, 22, 80, 443]
    services = ["FTP", "SSH", "HTTP", "HTTPS"]

    for port, service in zip(ports, services):
        print(f"Port {port} : {service}")

    # Exemple de test de credentials
    print("\n--- Test de credentials (bruteforce) ---")
    usernames_list = ["admin", "root", "user"]
    passwords_list = ["password123", "admin123", "test123"]

    for username, password in zip(usernames_list, passwords_list):
        print(f"Tentative : {username}:{password}")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 5 : break - Arrêter une boucle
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 5 : break - Arrêter une boucle ===\n")

    print("--- Arrêt quand condition est vraie ---")
    for i in range(10):
        if i == 5:
            print(f"Stop atteint à i={i}")
            break  # Arrête la boucle immédiatement
        print(f"i = {i}")

    # Exemple : recherche d'un utilisateur
    print("\n--- Recherche d'un utilisateur dans une liste ---")
    users = ["alice", "bob", "charlie", "diana", "emma"]
    search_user = "charlie"
    found = False

    for user in users:
        print(f"Vérification : {user}")
        if user == search_user:
            print(f"[+] Utilisateur trouvé : {user}")
            found = True
            break
        print(f"[-] Pas {user}")

    if not found:
        print(f"[-] Utilisateur {search_user} non trouvé")

    # Exemple : scan de port avec succès
    print("\n--- Scan de port jusqu'au premier ouvert ---")
    ports_to_check = [22, 23, 80, 443, 8080]
    for port in ports_to_check:
        print(f"Tentative de connexion au port {port}...")
        if port == 80:
            print(f"[+] Port {port} OUVERT !")
            break
        else:
            print(f"[-] Port {port} fermé")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 6 : continue - Sauter une itération
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 6 : continue - Sauter une itération ===\n")

    print("--- Sauter les nombres pairs ---")
    for i in range(10):
        if i % 2 == 0:
            continue  # Saute cette itération
        print(f"Nombre impair : {i}")

    # Exemple : filtrer les ports critiques
    print("\n--- Filtrer les ports critiques ---")
    all_ports = [21, 22, 80, 443, 3306, 8080, 5432]
    critical_ports = [22, 3306, 5432]  # SSH, MySQL, PostgreSQL

    print("Ports NON critiques détectés :")
    for port in all_ports:
        if port in critical_ports:
            continue  # Saute les ports critiques
        print(f"Port {port}")

    # Exemple : valider les mots de passe acceptables
    print("\n--- Filtrer les mots de passe faibles ---")
    passwords = ["a", "password", "p@ssw0rd!", "weak", "SuperSecure123!"]
    min_length = 8

    print(f"Mots de passe acceptables (>= {min_length} caractères) :")
    for pwd in passwords:
        if len(pwd) < min_length:
            print(f"[X] '{pwd}' : Trop court ({len(pwd)} caractères)")
            continue  # Passe au mot de passe suivant
        print(f"[OK] '{pwd}' : Accepté ({len(pwd)} caractères)")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 7 : Boucle while - Itération conditionnelle
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 7 : Boucle while ===\n")

    print("--- Comptage simple avec while ---")
    count = 0
    while count < 5:
        print(f"Comptage : {count}")
        count += 1  # CRUCIAL : modifier la condition pour éviter boucle infinie

    # Exemple : tentatives d'authentification
    print("\n--- Tentatives d'authentification ---")
    correct_password = "secure123"
    attempts = 0
    max_attempts = 3

    test_passwords = ["admin", "password", "secure123"]

    while attempts < max_attempts and attempts < len(test_passwords):
        password_attempt = test_passwords[attempts]
        attempts += 1

        print(f"\nTentative {attempts}/{max_attempts}")
        print(f"Mot de passe testé : {password_attempt}")

        if password_attempt == correct_password:
            print("[+] Authentification réussie !")
            break
        else:
            print(f"[-] Mot de passe incorrect")
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"[!] Il vous reste {remaining} tentative(s)")
            else:
                print(f"[!] Compte bloqué après {max_attempts} tentatives")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 8 : Boucles imbriquées - for dans for
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 8 : Boucles imbriquées ===\n")

    print("--- Tableau d'itérations ---")
    for i in range(3):
        for j in range(3):
            print(f"({i}, {j})", end=" ")
        print()  # Nouvelle ligne après chaque ligne externe

    # Exemple : scan d'adresses IP et ports
    print("\n--- Scan d'adresses IP et ports (simulation) ---")
    ip_segments = ["192.168.1.1", "192.168.1.2"]
    ports_to_scan = [22, 80, 443]

    print("Scan de ports sur plusieurs hôtes :\n")
    for ip in ip_segments:
        print(f"Hôte {ip}:")
        for port in ports_to_scan:
            print(f"  Port {port:3} : [?] Vérification...")
        print()

    # Exemple : table de multiplication
    print("--- Tableau de multiplication ---")
    for i in range(1, 4):
        for j in range(1, 4):
            product = i * j
            print(f"{i}x{j}={product}", end=" | ")
        print()

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 9 : Boucles imbriquées - while dans while
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 9 : Boucles imbriquées avec while ===\n")

    print("--- Grille avec while ---")
    row = 0
    while row < 3:
        col = 0
        while col < 3:
            print(f"[{row},{col}]", end=" ")
            col += 1
        print()  # Nouvelle ligne
        row += 1

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 10 : Red Teaming - Scan de ports brute-force
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 10 : Red Teaming - Scan de ports ===\n")

    print("--- Scan de ports sur range simplifié ---")
    target_ip = "192.168.1.100"
    start_port = 20
    end_port = 30
    open_ports = [22, 25, 80]  # Ports présumés ouverts

    print(f"Scan de ports {start_port}-{end_port} sur {target_ip}\n")

    for port in range(start_port, end_port + 1):
        # Simulation : vérifier si port est "ouvert"
        if port in open_ports:
            print(f"[+] Port {port:3} : OUVERT")
        else:
            print(f"[-] Port {port:3} : Fermé/Filtré")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 11 : Red Teaming - Bruteforce d'authentification
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 11 : Red Teaming - Bruteforce ===\n")

    print("--- Attaque par force brute (simulation) ---")
    target_username = "admin"
    target_password = "admin123"
    wordlist = ["123456", "password", "admin", "admin123", "letmein", "welcome"]

    print(f"Attaque bruteforce contre {target_username}@target.com\n")

    for attempt_count, password_guess in enumerate(wordlist, 1):
        print(f"Tentative {attempt_count}/{len(wordlist)}: {password_guess}", end="")

        if password_guess == target_password:
            print(" ✓ [+] ACCÈS RÉUSSI !")
            print(f"[+] Identifiants trouvés : {target_username}:{target_password}")
            break
        else:
            print(" ✗")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 12 : Red Teaming - Énumération d'utilisateurs
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 12 : Red Teaming - Énumération d'utilisateurs ===\n")

    print("--- Énumération d'ID utilisateur (simulation) ---")
    valid_users = [101, 102, 105, 108]  # IDs valides
    start_id = 100
    end_id = 110

    print(f"Énumération d'utilisateurs (ID {start_id}-{end_id}):\n")

    found_users = []
    for user_id in range(start_id, end_id + 1):
        if user_id in valid_users:
            found_users.append(user_id)
            print(f"[+] Utilisateur trouvé : ID {user_id}")
        else:
            print(f"[-] ID {user_id} : Non trouvé")

    print(f"\n[!] Total utilisateurs énumérés : {len(found_users)}")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 13 : Red Teaming - Décodage de payload
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 13 : Red Teaming - Analyse de payload ===\n")

    print("--- Scan de caractères suspect dans payload ---")
    payload = "select * from users; DROP TABLE users;--"
    sql_keywords = ["SELECT", "DROP", "DELETE", "INSERT", "UPDATE", "UNION"]

    print(f"Analyse du payload : {payload}\n")
    print("Mots-clés SQL détectés :\n")

    found_keywords = []
    for keyword in sql_keywords:
        if keyword.lower() in payload.lower():
            found_keywords.append(keyword)
            print(f"[!] DANGER : Mot-clé trouvé : {keyword}")

    if found_keywords:
        print(f"\n[!] ALERTE : {len(found_keywords)} mot(s)-clé SQL détecté(s)")
        print("[!] Possible SQL Injection !")
    else:
        print("\n[+] Aucun mot-clé SQL détecté")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 14 : Red Teaming - Génération de rapport d'audit
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 14 : Red Teaming - Rapport d'audit ===\n")

    print("--- Log d'authentification suspect ---")
    failed_attempts = [
        ("192.168.1.50", "admin", 5),
        ("10.0.0.20", "root", 3),
        ("192.168.1.50", "user", 8),
    ]

    print("Adresses IP avec tentatives échouées suspectes :\n")

    threshold = 5  # Seuil de tentatives suspectes

    for ip, user, attempts in failed_attempts:
        if attempts >= threshold:
            print(f"[!] ALERTE : {ip} - {attempts} tentatives failed")
            print(f"    Utilisateur ciblé : {user}")
            print(f"    Risque : Attaque par force brute probable\n")
        else:
            print(f"[i] {ip} - {attempts} tentatives (normal)")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 15 : Combinaisons break, continue et boucles imbriquées
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 15 : Combinaisons avancées ===\n")

    print("--- Scan avec skip et stop ---")
    ports_to_scan = [20, 21, 22, 23, 80, 443, 3306, 8080, 9000]
    critical_ports = [22, 3306]
    first_open = None

    print("Scan (skip ports critiques, stop au premier ouvert) :\n")

    for idx, port in enumerate(ports_to_scan, 1):
        # Skip les ports critiques
        if port in critical_ports:
            print(f"{idx}. Port {port} : [SKIP] Port critique")
            continue

        # Simulation : certains ports sont "ouverts"
        if port in [80, 443]:
            print(f"{idx}. Port {port} : [+] OUVERT")
            first_open = port
            break
        else:
            print(f"{idx}. Port {port} : [-] Fermé")

    if first_open:
        print(f"\n[+] Scan arrêté : premier port ouvert trouvé (port {first_open})")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 16 : Exemple pratique - Validation d'adresse IP
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 16 : Validation d'adresse IP ===\n")

    test_ips = ["192.168.1.1", "10.0.0.1", "172.16.0.1", "8.8.8.8", "1.1.1.1"]
    private_ranges = ["192.168.", "10.", "172.16.", "172.31."]

    print("Analyse des adresses IP :\n")

    private_count = 0
    public_count = 0

    for ip in test_ips:
        is_private = False

        # Vérifier si l'IP commence par un range privé
        for private_prefix in private_ranges:
            if ip.startswith(private_prefix):
                print(f"[+] {ip} : IP PRIVÉE")
                is_private = True
                private_count += 1
                break

        if not is_private:
            print(f"[-] {ip} : IP PUBLIQUE")
            public_count += 1

    print(f"\nRésumé : {private_count} privée(s), {public_count} publique(s)")


# ═══════════════════════════════════════════════════════════════
# Point d'entrée
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("\n" + "═" * 60)
    print("EXERCICE 06 : BOUCLES (FOR ET WHILE)")
    print("═" * 60 + "\n")

    main()

    print("\n" + "═" * 60)
    print("FIN DE L'EXERCICE")
    print("═" * 60 + "\n")
