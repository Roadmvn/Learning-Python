"""
═══════════════════════════════════════════════════════════════
EXERCICE 09 : Fonctions (Functions)
═══════════════════════════════════════════════════════════════

OBJECTIF :
- Maîtriser la définition et l'utilisation de fonctions
- Comprendre les paramètres et les arguments
- Utiliser return pour retourner des valeurs
- Manier les arguments par défaut
- Exploiter *args et **kwargs
- Utiliser les fonctions lambda
- Comprendre la portée des variables (scope)
- Écrire des docstrings
- Appliquer à la cybersécurité (scanning, encoding, vulnerabilities)

EXÉCUTION : python main.py

═══════════════════════════════════════════════════════════════
"""


def main():
    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 1 : Définition basique de fonction
    # ═══════════════════════════════════════════════════════════

    print("=== Étape 1 : Définition basique de fonction ===\n")

    # Une fonction est un bloc de code réutilisable
    # Syntaxe : def nom_fonction():
    #               code
    #
    # Avantages :
    # - Réutilisabilité
    # - Modularité
    # - Maintenabilité
    # - Clarté

    def saluer():
        """Une fonction sans paramètre"""
        print("[+] Bonjour depuis une fonction!")

    saluer()  # Appel de la fonction
    saluer()  # On peut l'appeler plusieurs fois

    # Exemple en cybersécurité : fonction de vérification
    def verifier_port_ouvert():
        """Vérifie si un port est ouvert (simplifié)"""
        print("[*] Vérification du port 22...")
        print("[+] Port 22 (SSH) : OUVERT")

    verifier_port_ouvert()

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 2 : Paramètres et arguments
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 2 : Paramètres et arguments ===\n")

    # Les paramètres sont des variables dans la définition de fonction
    # Les arguments sont les valeurs passées lors de l'appel

    def greet(nom):
        """Fonction avec un paramètre"""
        print(f"Bonjour {nom}!")

    greet("Alice")  # Argument : "Alice"
    greet("Bob")
    greet("Charlie")

    # Plusieurs paramètres
    def afficher_info_port(port, service):
        """Affiche les informations d'un port"""
        print(f"[*] Port {port} : Serveur {service}")

    afficher_info_port(22, "SSH")
    afficher_info_port(80, "HTTP")
    afficher_info_port(443, "HTTPS")

    # Arguments positionnels vs arguments nommés
    print("\n[Info] Arguments positionnels :")
    afficher_info_port(8080, "Tomcat")

    print("\n[Info] Arguments nommés :")
    afficher_info_port(service="FTP", port=21)

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 3 : Return - Retourner des valeurs
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 3 : Return - Retourner des valeurs ===\n")

    # return arrête la fonction et retourne une valeur

    def additionner(a, b):
        """Retourne la somme de deux nombres"""
        return a + b

    resultat = additionner(5, 3)
    print(f"5 + 3 = {resultat}")

    def verifier_credentials(username, password):
        """Vérifie les identifiants (exemple simplifié)"""
        if username == "admin" and password == "secure_pass_123":
            return True
        else:
            return False

    authentification = verifier_credentials("admin", "secure_pass_123")
    if authentification:
        print("\n[+] Authentification réussie")
    else:
        print("\n[-] Authentification échouée")

    # Retourner plusieurs valeurs
    def analyser_port(port):
        """Retourne le statut et le type d'un port"""
        if port == 22:
            return True, "SSH"
        elif port == 80:
            return True, "HTTP"
        elif port == 443:
            return True, "HTTPS"
        else:
            return False, "Inconnu"

    ouvert, service = analyser_port(22)
    print(f"Port 22 : Ouvert={ouvert}, Service={service}")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 4 : Arguments par défaut
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 4 : Arguments par défaut ===\n")

    # Les arguments par défaut fournissent des valeurs si non spécifiées

    def se_connecter(host, port=22, protocole="SSH"):
        """Se connecte à un serveur avec des paramètres par défaut"""
        print(f"[*] Connexion à {host}:{port} via {protocole}")

    se_connecter("192.168.1.100")  # Utilise les valeurs par défaut
    se_connecter("10.0.0.1", 2222)  # Surcharge port
    se_connecter("attacker.com", 443, "SSH")  # Surcharge tous les paramètres

    # Cas réel : configuration d'un scanner
    def scanner_port(target, port_range=(1, 1024), timeout=5):
        """Scanne les ports d'une cible"""
        print(f"[*] Scan de {target}")
        print(f"    Range : {port_range}")
        print(f"    Timeout : {timeout}s")

    scanner_port("192.168.1.1")
    scanner_port("10.0.0.1", port_range=(1, 65535))
    scanner_port("attacker.com", timeout=10)

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 5 : *args - Nombre variable d'arguments positionnels
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 5 : *args ===\n")

    # *args permet de passer un nombre variable d'arguments
    # Les arguments sont reçus sous forme de tuple

    def somme(*nombres):
        """Additionne un nombre quelconque d'arguments"""
        total = 0
        for n in nombres:
            total += n
        return total

    print(f"somme(1, 2, 3) = {somme(1, 2, 3)}")
    print(f"somme(10, 20, 30, 40) = {somme(10, 20, 30, 40)}")
    print(f"somme(5) = {somme(5)}")

    # Exemple cybersécurité : enregistrer plusieurs logs
    def enregistrer_logs(*messages):
        """Enregistre plusieurs messages de log"""
        for i, msg in enumerate(messages, 1):
            print(f"[LOG {i}] {msg}")

    enregistrer_logs(
        "[+] Port 22 détecté",
        "[+] Service SSH identifié",
        "[!] Version obsolète détectée",
        "[-] Exploit disponible"
    )

    # Combiner paramètres réguliers et *args
    def cracker_mdp(target, *tentatives):
        """Essaie de craquer un mot de passe avec plusieurs tentatives"""
        print(f"[*] Tentative de craquage de {target}")
        for mdp in tentatives:
            print(f"    [-] Essai : {mdp}")
        print(f"[!] {len(tentatives)} tentatives effectuées")

    cracker_mdp("admin@example.com", "password123", "123456", "admin", "qwerty")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 6 : **kwargs - Arguments nommés variables
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 6 : **kwargs ===\n")

    # **kwargs permet de passer des arguments nommés variables
    # Les arguments sont reçus sous forme de dictionnaire

    def afficher_config(**options):
        """Affiche une configuration avec des options variables"""
        for cle, valeur in options.items():
            print(f"  {cle}: {valeur}")

    print("[*] Configuration 1:")
    afficher_config(host="localhost", port=8080)

    print("\n[*] Configuration 2:")
    afficher_config(
        host="192.168.1.1",
        port=443,
        ssl=True,
        timeout=30,
        retries=3
    )

    # Cas réel : configuration d'une requête réseau
    def envoyer_requete(url, **parametres):
        """Envoie une requête HTTP avec des paramètres variables"""
        print(f"[*] Requête vers : {url}")
        for param, valeur in parametres.items():
            print(f"    {param}: {valeur}")

    envoyer_requete(
        "http://target.com/api",
        method="POST",
        headers={"User-Agent": "Mozilla/5.0"},
        data={"username": "admin"},
        timeout=10
    )

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 7 : Combinaison *args et **kwargs
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 7 : Combinaison *args et **kwargs ===\n")

    # Ordre : paramètres réguliers, *args, **kwargs

    def logger(niveau, *messages, **options):
        """Enregistre un message avec niveau et options"""
        print(f"[{niveau}]", end=" ")
        for msg in messages:
            print(msg, end=" ")
        print()
        if options:
            print("  Options:", options)

    logger("INFO", "Port ouvert", "Service identifié")
    logger("WARNING", "Accès non autorisé", "Tentative de connexion", retry=3, timeout=10)
    logger("ERROR", "Erreur critique détectée", timestamp="2024-01-15 10:30:45", severity="HIGH")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 8 : Fonctions Lambda
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 8 : Fonctions Lambda ===\n")

    # Les lambda sont des fonctions anonymes sur une ligne
    # Syntaxe : lambda paramètres: expression
    # Retourne le résultat de l'expression

    # Lambda simple
    carre = lambda x: x ** 2
    print(f"carre(5) = {carre(5)}")

    # Lambda avec plusieurs paramètres
    additionner_lambda = lambda a, b: a + b
    print(f"additionner(10, 20) = {additionner_lambda(10, 20)}")

    # Lambda avec map
    nombres = [1, 2, 3, 4, 5]
    carres = list(map(lambda x: x ** 2, nombres))
    print(f"\nMap - Carres de {nombres} = {carres}")

    # Lambda avec filter
    pairs = list(filter(lambda x: x % 2 == 0, nombres))
    print(f"Filter - Nombres pairs : {pairs}")

    # Lambda avec sorted
    utilisateurs = [
        {"nom": "Alice", "score": 85},
        {"nom": "Bob", "score": 92},
        {"nom": "Charlie", "score": 78}
    ]
    tries = sorted(utilisateurs, key=lambda u: u["score"], reverse=True)
    print(f"\nTri par score (décroissant):")
    for user in tries:
        print(f"  {user['nom']}: {user['score']}")

    # Exemple cybersécurité : filtrer les ports
    tous_les_ports = [21, 22, 23, 25, 80, 443, 3306, 5432, 8080]
    ports_ouverts = list(filter(lambda p: p in [22, 80, 443], tous_les_ports))
    print(f"\n[*] Ports ouverts détectés : {ports_ouverts}")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 9 : Portée des variables (Scope)
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 9 : Portée des variables (Scope) ===\n")

    # Scope global vs local
    # Variable globale : accessible partout
    # Variable locale : accessible uniquement dans la fonction

    variable_globale = "Je suis global"

    def fonction_avec_scope():
        """Démontre la portée des variables"""
        variable_locale = "Je suis local"
        print(f"À l'intérieur : {variable_globale}")  # Accès global OK
        print(f"À l'intérieur : {variable_locale}")   # Accès local OK

    fonction_avec_scope()
    print(f"À l'extérieur : {variable_globale}")      # Accès global OK
    # print(variable_locale)  # ERREUR : variable_locale n'existe pas ici

    print()

    # Portée des variables : SCOPE
    print()

    # Approche 1 : Utiliser une liste (mutable, modifiable dans le scope enfant)
    compteur = [0]

    def incrementer():
        """Modifie une variable en accédant à sa référence"""
        # Les objets mutables (listes, dicts) peuvent être modifiés sans 'global'
        compteur[0] += 1

    print(f"Compteur initial : {compteur[0]}")
    incrementer()
    incrementer()
    incrementer()
    print(f"Compteur final : {compteur[0]}")

    # Approche 2 : Démonstration avec nonlocal pour la scope enclosing
    print()

    def creer_compteur_local():
        """Crée une fonction avec une variable dans la scope enclosing"""
        count = 0

        def incrementer_local():
            nonlocal count  # nonlocal : accède à la variable de la fonction parent
            count += 1
            return count

        print(f"Appel 1 : {incrementer_local()}")
        print(f"Appel 2 : {incrementer_local()}")
        print(f"Appel 3 : {incrementer_local()}")

    creer_compteur_local()

    # Approche 3 : Comprendre le piège des variables locales
    print()

    print("[*] Piège classique avec les variables locales :")
    print("    Si on assigne à une variable dans une fonction,")
    print("    Python la traite comme LOCALE dans toute la fonction,")
    print("    même avant l'assignation!")
    print()

    def exemple_lecture_avant_assignation():
        """Démontre le piège UnboundLocalError"""
        x = 100  # variable locale x
        try:
            print(x + 1)  # Lecture OK, x est local mais assigné avant
            x = x + 10    # Modification OK
        except:
            pass

        try:
            # Cette partie causerait une erreur si on n'avait pas assigné x avant
            y = y + 1  # Erreur : y n'existe pas localement ET n'est pas global
        except UnboundLocalError:
            print("    [!] UnboundLocalError : y est traitée comme locale")
            print("        mais n'a pas été assignée avant sa lecture")

    exemple_lecture_avant_assignation()

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 10 : Docstrings
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 10 : Docstrings ===\n")

    # Les docstrings documentent une fonction
    # Accessibles via help() ou __doc__

    def scan_port(host, port):
        """
        Simule un scan de port pour vérifier son statut.

        Arguments:
            host (str): L'adresse IP ou le domaine à scanner
            port (int): Le numéro du port (1-65535)

        Retour:
            bool: True si le port est ouvert, False sinon

        Exemple:
            >>> scan_port("192.168.1.1", 22)
            True
        """
        # Simulation d'un scan
        ports_ouverts = [22, 80, 443, 3306]
        return port in ports_ouverts

    print("Docstring de scan_port:")
    print(scan_port.__doc__)

    print("\nUtilisation de help():")
    help(scan_port)

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 11 : Fonctions cybersécurité - Red Teaming
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 11 : Fonctions cybersécurité ===\n")

    # Fonction 1 : Scanner de port
    def scan_port_detaille(host, ports, *args, verbose=True, **options):
        """
        Scanne des ports et retourne les résultats.

        Cette fonction est à usage éducatif uniquement.
        """
        print(f"[*] Scan de {host}")
        ports_ouverts = []

        for port in ports:
            # Simulation d'un scan (dans la réalité : socket ou nmap)
            is_open = port in [22, 80, 443, 3306, 8080]
            status = "OUVERT" if is_open else "FERMÉ"
            print(f"    Port {port}: {status}")
            if is_open:
                ports_ouverts.append(port)

        if verbose:
            print(f"[+] {len(ports_ouverts)} ports ouverts détectés")
        if options:
            print(f"[*] Options : {options}")

        return ports_ouverts

    print("[*] Résultat du scan :")
    resultats = scan_port_detaille(
        "192.168.1.100",
        [21, 22, 25, 80, 443, 3306, 8080],
        verbose=True,
        method="SYN",
        timeout=5
    )

    # Fonction 2 : Vérificateur de vulnérabilités
    def check_vulnerability(service, version, *args, severity_min=5):
        """
        Vérifie si un service a des vulnérabilités connues.
        """
        vulnerabilites = {
            ("SSH", "7.4"): {"id": "CVE-2018-15473", "score": 5.3},
            ("OpenSSH", "7.4"): {"id": "CVE-2018-15473", "score": 5.3},
            ("HTTP", "1.0"): {"id": "CVE-2001-1234", "score": 7.5},
        }

        cle = (service, version)
        if cle in vulnerabilites:
            vuln = vulnerabilites[cle]
            if vuln["score"] >= severity_min:
                print(f"[!] VULNÉRABILITÉ TROUVÉE")
                print(f"    Service: {service} {version}")
                print(f"    CVE: {vuln['id']}")
                print(f"    Score: {vuln['score']}/10")
                return True
        return False

    print("\n[*] Vérification des vulnérabilités :")
    check_vulnerability("SSH", "7.4", severity_min=5)
    check_vulnerability("HTTP", "1.0", severity_min=8)

    # Fonction 3 : Encodeur de payload
    def encode_payload(payload, *encodages, format="hex"):
        """
        Encode un payload de plusieurs façons.
        """
        print(f"[*] Encodage du payload : {payload[:30]}...")

        if format == "hex":
            encoded = payload.encode().hex()
            print(f"    Hex : {encoded[:50]}...")

        elif format == "base64":
            import base64
            encoded = base64.b64encode(payload.encode()).decode()
            print(f"    Base64 : {encoded[:50]}...")

        elif format == "ascii":
            encoded = " ".join(str(ord(c)) for c in payload)
            print(f"    ASCII : {encoded[:50]}...")

        return encoded

    print("\n[*] Encodage de payload :")
    encode_payload("ls -la /etc/passwd", format="hex")
    encode_payload("cat /etc/shadow", format="base64")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 12 : Chaîner les fonctions
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 12 : Chaîner les fonctions ===\n")

    def obtenir_ports_cibles():
        """Retourne une liste de ports à scanner"""
        return [22, 80, 443, 3306, 8080]

    def verifier_services(ports):
        """Vérifie les services sur les ports"""
        services = {
            22: "SSH",
            80: "HTTP",
            443: "HTTPS",
            3306: "MySQL",
            8080: "Tomcat"
        }
        return {p: services.get(p, "Inconnu") for p in ports}

    def generer_rapport(services):
        """Génère un rapport de scan"""
        print("[*] RAPPORT DE SCAN")
        for port, service in services.items():
            print(f"    Port {port}: {service}")

    # Chaîner les appels
    ports = obtenir_ports_cibles()
    services = verifier_services(ports)
    generer_rapport(services)

    # ═══════════════════════════════════════════════════════════
    # Fin
    # ═══════════════════════════════════════════════════════════

    print("\n" + "=" * 59)
    print("[+] Exercice 09 terminé!")
    print("=" * 59)


if __name__ == "__main__":
    main()
