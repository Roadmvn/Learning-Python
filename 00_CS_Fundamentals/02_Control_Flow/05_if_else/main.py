"""
═══════════════════════════════════════════════════════════════
EXERCICE 05 : Structures conditionnelles (if/else)
═══════════════════════════════════════════════════════════════

OBJECTIF :
- Maîtriser les structures if/else
- Comprendre if/elif/else pour conditions multiples
- Utiliser l'opérateur ternaire
- Découvrir match/case (Python 3.10+)
- Combiner conditions avec and, or, not
- Appliquer aux contextes de cybersécurité

EXÉCUTION : python main.py

═══════════════════════════════════════════════════════════════
"""

def main():
    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 1 : if basique
    # ═══════════════════════════════════════════════════════════

    print("=== Étape 1 : if basique ===\n")

    # Structure de base : if condition:
    # Exécute le bloc SEULEMENT si la condition est True

    age = 20

    if age >= 18:
        print("Vous êtes majeur")

    # Sans else, si la condition est False, rien ne se passe
    if age >= 21:
        print("Ce message ne s'affiche pas (condition False)")

    # Vérification de port ouvert
    port_status = "open"

    if port_status == "open":
        print(f"\n[+] Port détecté comme ouvert")

    # Vérification de permissions
    is_admin = True

    if is_admin:
        print("\n[+] Accès administrateur accordé")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 2 : if/else
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 2 : if/else ===\n")

    # Structure : if condition:
    #                 code si True
    #             else:
    #                 code si False

    password = "secret123"

    if password == "admin123":
        print("Connexion réussie")
    else:
        print("Mot de passe incorrect")

    # Vérification de port
    port = 22

    if port < 1024:
        print(f"\n[!] Port {port} : Privilégié (nécessite droits root)")
    else:
        print(f"\n[i] Port {port} : Non privilégié")

    # Détection de service
    service_response = "SSH-2.0-OpenSSH_8.9"

    if "OpenSSH" in service_response:
        print(f"\n[+] Service SSH détecté : {service_response}")
    else:
        print(f"\n[-] Service SSH non détecté")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 3 : if/elif/else (conditions multiples)
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 3 : if/elif/else ===\n")

    # elif = "else if"
    # Permet de tester plusieurs conditions en séquence
    # Dès qu'une condition est True, les autres ne sont pas testées

    status_code = 404

    if status_code == 200:
        print("Succès")
    elif status_code == 301:
        print("Redirection permanente")
    elif status_code == 404:
        print("Page non trouvée")
    elif status_code == 500:
        print("Erreur serveur")
    else:
        print("Code de statut inconnu")

    # Classification de ports
    print("\n--- Classification de ports ---")
    port_number = 8080

    if port_number < 1024:
        category = "Privilégié (Well-Known Ports)"
    elif port_number >= 1024 and port_number <= 49151:
        category = "Enregistré (Registered Ports)"
    elif port_number >= 49152 and port_number <= 65535:
        category = "Dynamique/Privé (Dynamic/Private Ports)"
    else:
        category = "Invalid"

    print(f"Port {port_number} : {category}")

    # Analyse de niveau de menace
    print("\n--- Analyse de niveau de menace ---")
    threat_score = 75

    if threat_score >= 90:
        threat_level = "CRITIQUE"
        action = "Bloquer immédiatement"
    elif threat_score >= 70:
        threat_level = "ÉLEVÉ"
        action = "Isoler et analyser"
    elif threat_score >= 40:
        threat_level = "MOYEN"
        action = "Surveiller"
    elif threat_score >= 10:
        threat_level = "FAIBLE"
        action = "Logger uniquement"
    else:
        threat_level = "NÉGLIGEABLE"
        action = "Ignorer"

    print(f"Score de menace : {threat_score}")
    print(f"Niveau : {threat_level}")
    print(f"Action recommandée : {action}")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 4 : Conditions multiples (and, or, not)
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 4 : Conditions multiples ===\n")

    # Opérateur AND : toutes les conditions doivent être True
    username = "admin"
    password = "password123"
    two_fa_code = "123456"

    if username == "admin" and password == "password123" and two_fa_code == "123456":
        print("[+] Authentification réussie (3 facteurs validés)")
    else:
        print("[-] Authentification échouée")

    # Opérateur OR : au moins une condition doit être True
    print("\n--- Vérification de ports critiques ---")
    port = 22

    if port == 22 or port == 23 or port == 3389:
        print(f"[!] Port {port} : Accès distant détecté (SSH/Telnet/RDP)")
    else:
        print(f"[i] Port {port} : Non critique")

    # Opérateur NOT : inverse la condition
    print("\n--- Vérification de connexion sécurisée ---")
    protocol = "http"

    if not protocol == "https":
        print(f"[!] ATTENTION : Protocole {protocol.upper()} non sécurisé")
        print("[!] Recommandation : Utiliser HTTPS")
    else:
        print(f"[+] Protocole {protocol.upper()} sécurisé")

    # Combinaison complexe
    print("\n--- Validation de complexité de mot de passe ---")
    password = "MyP@ssw0rd123"
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    if length >= 12 and has_upper and has_lower and has_digit and has_special:
        print(f"[+] Mot de passe '{password}' : FORT")
    elif length >= 8 and (has_upper or has_lower) and has_digit:
        print(f"[~] Mot de passe '{password}' : MOYEN")
    else:
        print(f"[-] Mot de passe '{password}' : FAIBLE")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 5 : Conditions imbriquées (nested if)
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 5 : Conditions imbriquées ===\n")

    # On peut imbriquer des if dans des if
    print("--- Contrôle d'accès multi-niveau ---")
    user_role = "admin"
    ip_address = "192.168.1.100"
    time_hour = 14

    if user_role == "admin":
        print(f"[+] Utilisateur : {user_role}")

        if ip_address.startswith("192.168.1."):
            print(f"[+] IP autorisée : {ip_address}")

            if time_hour >= 8 and time_hour <= 18:
                print(f"[+] Horaire autorisé : {time_hour}h")
                print("[+] ACCÈS AUTORISÉ")
            else:
                print(f"[-] Horaire non autorisé : {time_hour}h")
                print("[-] ACCÈS REFUSÉ (Horaire)")
        else:
            print(f"[-] IP non autorisée : {ip_address}")
            print("[-] ACCÈS REFUSÉ (IP)")
    else:
        print(f"[-] Rôle insuffisant : {user_role}")
        print("[-] ACCÈS REFUSÉ (Rôle)")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 6 : Opérateur ternaire (conditional expression)
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 6 : Opérateur ternaire ===\n")

    # Syntaxe : valeur_si_true if condition else valeur_si_false
    # Version compacte du if/else pour assignation

    port = 443
    status = "Sécurisé" if port == 443 else "Non sécurisé"
    print(f"Port {port} : {status}")

    # Équivalent en if/else classique :
    # if port == 443:
    #     status = "Sécurisé"
    # else:
    #     status = "Non sécurisé"

    # Autre exemple
    age = 25
    access = "AUTORISÉ" if age >= 18 else "REFUSÉ"
    print(f"Âge {age} ans : Accès {access}")

    # Avec opérations
    number = 42
    parity = "pair" if number % 2 == 0 else "impair"
    print(f"{number} est {parity}")

    # Attention : ne pas abuser de l'opérateur ternaire
    # Il est lisible pour des cas simples uniquement
    # Pour des conditions complexes, préférer if/else classique

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 7 : match/case (Python 3.10+)
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 7 : match/case (Python 3.10+) ===\n")

    # match/case est similaire au switch/case d'autres langages
    # Plus élégant que de multiples if/elif pour tester une même variable
    # NOTE : match/case nécessite Python 3.10+
    # Ici, nous utilisons if/elif/else pour la compatibilité

    print("--- Analyse de code de statut HTTP ---")
    status_code = 403

    # Version if/elif/else (compatible toutes versions Python)
    if status_code == 200:
        result = "OK - Succès"
    elif status_code == 201:
        result = "Created - Ressource créée"
    elif status_code == 301:
        result = "Moved Permanently - Redirection permanente"
    elif status_code == 400:
        result = "Bad Request - Requête invalide"
    elif status_code == 401:
        result = "Unauthorized - Non authentifié"
    elif status_code == 403:
        result = "Forbidden - Accès interdit"
    elif status_code == 404:
        result = "Not Found - Ressource introuvable"
    elif status_code == 500:
        result = "Internal Server Error - Erreur serveur"
    else:
        result = "Code inconnu"

    print(f"Code {status_code} : {result}")

    # Exemple avec match/case (commenté pour Python < 3.10)
    # Si vous avez Python 3.10+, décommentez ce code :
    """
    match status_code:
        case 200:
            result = "OK - Succès"
        case 403:
            result = "Forbidden - Accès interdit"
        case 404:
            result = "Not Found - Ressource introuvable"
        case _:
            result = "Code inconnu"
    """

    # Classification de ports
    print("\n--- Classification de ports ---")
    port = 3306

    if port == 21:
        service = "FTP"
    elif port == 22:
        service = "SSH"
    elif port == 23:
        service = "Telnet"
    elif port == 25:
        service = "SMTP"
    elif port == 53:
        service = "DNS"
    elif port == 80:
        service = "HTTP"
    elif port == 110:
        service = "POP3"
    elif port == 143:
        service = "IMAP"
    elif port == 443:
        service = "HTTPS"
    elif port == 3306:
        service = "MySQL"
    elif port == 3389:
        service = "RDP"
    elif port == 5432:
        service = "PostgreSQL"
    else:
        service = "Service inconnu ou personnalisé"

    print(f"Port {port} : {service}")

    # Analyse de port avec conditions
    print("\n--- Analyse de port avec conditions ---")
    port = 8080

    if port < 1024:
        print(f"Port {port} : Privilégié")
    elif 1024 <= port < 49152:
        print(f"Port {port} : Enregistré")
    elif 49152 <= port <= 65535:
        print(f"Port {port} : Dynamique/Privé")
    else:
        print(f"Port {port} : Invalid")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 8 : Exemple pratique - Vérificateur d'authentification
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 8 : Exemple pratique - Authentification ===\n")

    # Simulation d'un système d'authentification avec tentatives
    correct_password = "SuperSecure123!"
    max_attempts = 3
    attempts = 0

    print("Système d'authentification sécurisé")
    print(f"Vous avez {max_attempts} tentatives\n")

    # Simulation de 3 tentatives
    test_passwords = ["admin", "password", "SuperSecure123!"]

    for password_attempt in test_passwords:
        attempts += 1
        remaining = max_attempts - attempts

        print(f"Tentative {attempts}/{max_attempts}")
        print(f"Mot de passe testé : {password_attempt}")

        if password_attempt == correct_password:
            print("[+] Authentification réussie!")
            print(f"[+] Accès accordé après {attempts} tentative(s)")
            break
        else:
            if remaining > 0:
                print(f"[-] Mot de passe incorrect")
                print(f"[!] Il vous reste {remaining} tentative(s)\n")
            else:
                print(f"[-] Mot de passe incorrect")
                print(f"[!] Compte bloqué après {max_attempts} tentatives échouées")
                print(f"[!] Veuillez contacter l'administrateur")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 9 : Exemple pratique - Scanner de ports
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 9 : Exemple pratique - Scanner de ports ===\n")

    # Simulation d'un scan de ports avec classification
    print("Simulation de scan de ports sur 192.168.1.100\n")

    # Ports à scanner avec leur statut simulé
    scan_results = [
        (22, "open"),
        (23, "closed"),
        (80, "open"),
        (443, "filtered"),
        (3306, "open"),
        (8080, "open"),
    ]

    for port, status in scan_results:
        # Identification du service
        if port == 22:
            service = "SSH"
        elif port == 23:
            service = "Telnet"
        elif port == 80:
            service = "HTTP"
        elif port == 443:
            service = "HTTPS"
        elif port == 3306:
            service = "MySQL"
        elif port == 8080:
            service = "HTTP-Alt"
        else:
            service = "Unknown"

        # Analyse du statut
        if status == "open":
            icon = "[+]"
            risk = "ATTENTION"
        elif status == "closed":
            icon = "[-]"
            risk = "OK"
        elif status == "filtered":
            icon = "[~]"
            risk = "VÉRIFIER"
        else:
            icon = "[?]"
            risk = "UNKNOWN"

        # Affichage
        print(f"{icon} Port {port:5} : {status:8} | {service:10} | {risk}")

    # Résumé
    open_ports = [port for port, status in scan_results if status == "open"]
    print(f"\n[!] Résumé : {len(open_ports)} port(s) ouvert(s) détecté(s)")
    print(f"[!] Ports ouverts : {', '.join(map(str, open_ports))}")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 10 : Exemple pratique - Analyse de vulnérabilité
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 10 : Exemple pratique - Analyse de vulnérabilité ===\n")

    # Simulation d'analyse de configuration de serveur
    print("Analyse de configuration de serveur web\n")

    # Configuration du serveur
    server_config = {
        "ssl_enabled": True,
        "ssl_version": "TLSv1.3",
        "admin_panel_exposed": True,
        "directory_listing": False,
        "debug_mode": True,
        "default_credentials": False,
        "firewall_enabled": True,
        "ports_open": [80, 443, 8080],
    }

    vulnerability_score = 0
    vulnerabilities = []

    # Vérification SSL
    if not server_config["ssl_enabled"]:
        vulnerabilities.append("SSL/TLS non activé")
        vulnerability_score += 30
    elif server_config["ssl_version"] in ["SSLv3", "TLSv1.0", "TLSv1.1"]:
        vulnerabilities.append(f"Version SSL obsolète : {server_config['ssl_version']}")
        vulnerability_score += 20

    # Vérification du panneau d'administration
    if server_config["admin_panel_exposed"]:
        vulnerabilities.append("Panneau d'administration exposé publiquement")
        vulnerability_score += 15

    # Vérification du directory listing
    if server_config["directory_listing"]:
        vulnerabilities.append("Directory listing activé")
        vulnerability_score += 10

    # Vérification du mode debug
    if server_config["debug_mode"]:
        vulnerabilities.append("Mode debug activé en production")
        vulnerability_score += 25

    # Vérification des credentials par défaut
    if server_config["default_credentials"]:
        vulnerabilities.append("Identifiants par défaut détectés")
        vulnerability_score += 40

    # Vérification du firewall
    if not server_config["firewall_enabled"]:
        vulnerabilities.append("Pare-feu désactivé")
        vulnerability_score += 20

    # Vérification des ports non standard
    non_standard_ports = [p for p in server_config["ports_open"] if p not in [80, 443]]
    if non_standard_ports:
        vulnerabilities.append(f"Ports non standard ouverts : {non_standard_ports}")
        vulnerability_score += 5 * len(non_standard_ports)

    # Classification du niveau de risque
    if vulnerability_score >= 70:
        risk_level = "CRITIQUE"
        color = "ROUGE"
    elif vulnerability_score >= 40:
        risk_level = "ÉLEVÉ"
        color = "ORANGE"
    elif vulnerability_score >= 20:
        risk_level = "MOYEN"
        color = "JAUNE"
    elif vulnerability_score > 0:
        risk_level = "FAIBLE"
        color = "BLEU"
    else:
        risk_level = "AUCUN"
        color = "VERT"

    # Affichage du rapport
    print("╔════════════════════════════════════════════════════════╗")
    print("║         RAPPORT D'ANALYSE DE VULNÉRABILITÉ            ║")
    print("╠════════════════════════════════════════════════════════╣")
    print(f"║ Score de vulnérabilité : {vulnerability_score:3}/100{' ' * 28}║")
    print(f"║ Niveau de risque       : {risk_level:<28}║")
    print(f"║ Indicateur             : {color:<28}║")
    print("╠════════════════════════════════════════════════════════╣")

    if vulnerabilities:
        print("║ Vulnérabilités détectées :                            ║")
        for i, vuln in enumerate(vulnerabilities, 1):
            print(f"║ {i}. {vuln:<52}║")
    else:
        print("║ Aucune vulnérabilité détectée                         ║")

    print("╚════════════════════════════════════════════════════════╝")


# ═══════════════════════════════════════════════════════════════
# Point d'entrée
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("\n" + "═" * 60)
    print("EXERCICE 05 : STRUCTURES CONDITIONNELLES (IF/ELSE)")
    print("═" * 60 + "\n")

    main()

    print("\n" + "═" * 60)
    print("FIN DE L'EXERCICE")
    print("═" * 60 + "\n")
