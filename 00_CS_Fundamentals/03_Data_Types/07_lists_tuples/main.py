"""
═══════════════════════════════════════════════════════════════
EXERCICE 07 : Listes et Tuples
═══════════════════════════════════════════════════════════════

OBJECTIF :
- Maîtriser les listes (type mutable)
- Maîtriser les tuples (type immutable)
- Comprendre l'indexing et le slicing
- Utiliser les méthodes de liste
- Utiliser la list comprehension
- Appliquer aux contextes de cybersécurité

EXÉCUTION : python main.py

═══════════════════════════════════════════════════════════════
"""

def main():
    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 1 : Création de listes
    # ═══════════════════════════════════════════════════════════

    print("=== Étape 1 : Création de listes ===\n")

    # Une liste est une collection ordonnée et mutable
    # Syntaxe : [élément1, élément2, élément3]

    # Liste d'adresses IP (cybersécurité)
    ips = ["192.168.1.1", "10.0.0.5", "172.16.0.1", "8.8.8.8"]
    print(f"Adresses IP : {ips}")

    # Liste de ports courants
    ports = [22, 80, 443, 3306, 5432, 8080]
    print(f"Ports : {ports}")

    # Liste de services
    services = ["SSH", "HTTP", "HTTPS", "MySQL", "PostgreSQL", "Tomcat"]
    print(f"Services : {services}")

    # Liste hétérogène (différents types)
    mixed = [1, "admin", 3.14, True, None]
    print(f"Liste hétérogène : {mixed}")

    # Liste vide
    empty = []
    print(f"Liste vide : {empty}")

    # Longueur d'une liste
    print(f"Nombre d'IPs : {len(ips)}")
    print(f"Nombre de ports : {len(ports)}\n")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 2 : Indexing (accès par position)
    # ═══════════════════════════════════════════════════════════

    print("=== Étape 2 : Indexing ===\n")

    # L'indexing commence à 0
    # ips = ["192.168.1.1", "10.0.0.5", "172.16.0.1", "8.8.8.8"]
    #          0                1            2            3
    # Indices négatifs : -4, -3, -2, -1

    print("--- Accès par indice positif ---")
    print(f"ips[0] = {ips[0]}")  # Premier élément
    print(f"ips[1] = {ips[1]}")
    print(f"ips[2] = {ips[2]}")
    print(f"ips[3] = {ips[3]}")

    print("\n--- Accès par indice négatif ---")
    print(f"ips[-1] = {ips[-1]}")  # Dernier élément
    print(f"ips[-2] = {ips[-2]}")  # Avant-dernier
    print(f"ips[-3] = {ips[-3]}")
    print(f"ips[-4] = {ips[-4]}")  # Premier élément

    print("\n--- Application cybersécurité ---")
    print(f"Port SSH : {ports[0]}")
    print(f"Port HTTP : {ports[1]}")
    print(f"Port HTTPS : {ports[2]}")
    print(f"Service le moins courant : {services[-1]}\n")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 3 : Slicing (découpage de listes)
    # ═══════════════════════════════════════════════════════════

    print("=== Étape 3 : Slicing ===\n")

    # Syntaxe : liste[start:stop:step]
    # start : inclus
    # stop : EXCLUS
    # step : intervalle (défaut = 1)

    nombres = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"Liste originale : {nombres}")

    print("\n--- Slicing simple ---")
    print(f"nombres[0:5] = {nombres[0:5]}")    # [0, 1, 2, 3, 4]
    print(f"nombres[2:7] = {nombres[2:7]}")    # [2, 3, 4, 5, 6]
    print(f"nombres[3:] = {nombres[3:]}")      # [3, 4, 5, 6, 7, 8, 9]
    print(f"nombres[:6] = {nombres[:6]}")      # [0, 1, 2, 3, 4, 5]

    print("\n--- Slicing avec step ---")
    print(f"nombres[::2] = {nombres[::2]}")    # Tous les 2
    print(f"nombres[1::2] = {nombres[1::2]}")  # À partir de 1, tous les 2
    print(f"nombres[::3] = {nombres[::3]}")    # Tous les 3
    print(f"nombres[::-1] = {nombres[::-1]}")  # Inversé

    print("\n--- Slicing sur des données réelles ---")
    print(f"Premiers 3 ports : {ports[0:3]}")
    print(f"Derniers 2 ports : {ports[-2:]}")
    print(f"Ports du milieu : {ports[2:4]}")

    print("\n--- Cas d'usage cybersécurité ---")
    # Scenario : scanner de ports, vérifier les premiers ports critiques
    critical_ports = [22, 80, 443, 3306]
    other_ports = [5432, 8080, 9000, 27017]
    common_ports = critical_ports + other_ports

    print(f"Ports critiques : {common_ports[:3]}")
    print(f"Ports secondaires : {common_ports[3:]}\n")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 4 : Modification de listes
    # ═══════════════════════════════════════════════════════════

    print("=== Étape 4 : Modification de listes ===\n")

    # Créer une copie pour ne pas modifier l'original
    target_ips = ips.copy()
    print(f"IPs cibles initiales : {target_ips}")

    print("\n--- Modification d'un élément ---")
    target_ips[0] = "192.168.1.100"
    print(f"Après changement de target_ips[0] : {target_ips}")

    print("\n--- Ajout avec append() ---")
    # append() ajoute UN élément à la fin
    target_ips.append("1.1.1.1")
    print(f"Après append('1.1.1.1') : {target_ips}")

    print("\n--- Ajout multiple avec extend() ---")
    # extend() ajoute PLUSIEURS éléments
    target_ips.extend(["8.8.8.8", "8.8.4.4"])
    print(f"Après extend(...) : {target_ips}")

    print("\n--- Insertion à une position avec insert() ---")
    # insert(index, élément)
    target_ips.insert(1, "10.10.10.10")
    print(f"Après insert(1, '10.10.10.10') : {target_ips}\n")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 5 : Suppression d'éléments
    # ═══════════════════════════════════════════════════════════

    print("=== Étape 5 : Suppression d'éléments ===\n")

    # Créer une liste de test
    vulns = ["SQL Injection", "XSS", "CSRF", "Auth Bypass", "RCE"]
    print(f"Vulnérabilités détectées : {vulns}")

    print("\n--- Suppression avec remove() (par valeur) ---")
    # remove() supprime la PREMIÈRE occurrence trouvée
    vulns.remove("CSRF")
    print(f"Après remove('CSRF') : {vulns}")

    print("\n--- Suppression avec pop() (par index) ---")
    # pop() supprime et retourne l'élément à cet index
    # Par défaut : pop() supprime le dernier élément
    last_vuln = vulns.pop()
    print(f"pop() supprime et retourne : {last_vuln}")
    print(f"Liste après pop() : {vulns}")

    print("\n--- Suppression avec pop(index) ---")
    first_vuln = vulns.pop(0)
    print(f"pop(0) supprime et retourne : {first_vuln}")
    print(f"Liste après pop(0) : {vulns}")

    print("\n--- Suppression avec del ---")
    # del supprime directement sans retourner la valeur
    test_list = ["a", "b", "c", "d"]
    print(f"Avant : {test_list}")
    del test_list[1]
    print(f"Après del test_list[1] : {test_list}")
    del test_list[1:3]
    print(f"Après del test_list[1:3] : {test_list}\n")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 6 : Recherche et tri
    # ═══════════════════════════════════════════════════════════

    print("=== Étape 6 : Recherche et tri ===\n")

    ports_scan = [22, 80, 443, 3306, 22, 443, 8080]
    print(f"Ports scannés : {ports_scan}")

    print("\n--- index() : trouve la position ---")
    pos = ports_scan.index(443)
    print(f"Port 443 à la position : {pos}")

    print("\n--- count() : compte les occurrences ---")
    count_443 = ports_scan.count(443)
    count_22 = ports_scan.count(22)
    print(f"Port 443 trouvé {count_443} fois")
    print(f"Port 22 trouvé {count_22} fois")

    print("\n--- sort() : trie sur place ---")
    scores = [75, 23, 89, 12, 56]
    print(f"Scores avant : {scores}")
    scores.sort()
    print(f"Scores après sort() : {scores}")

    print("\n--- sort(reverse=True) : tri décroissant ---")
    scores.sort(reverse=True)
    print(f"Scores en ordre décroissant : {scores}")

    print("\n--- reverse() : inverse l'ordre ---")
    ports_scan.reverse()
    print(f"Ports inversés : {ports_scan}\n")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 7 : Copie de listes
    # ═══════════════════════════════════════════════════════════

    print("=== Étape 7 : Copie de listes ===\n")

    # ATTENTION : le = ne copie pas, il crée une référence
    original = [1, 2, 3]
    reference = original  # Référence (pas de copie !)
    copie = original.copy()  # Véritable copie

    print(f"Original : {original}")
    print(f"Référence : {reference}")
    print(f"Copie : {copie}")

    print("\n--- Modification de la référence ---")
    reference.append(4)
    print(f"Après reference.append(4) :")
    print(f"  Original : {original}")      # Modifié !
    print(f"  Référence : {reference}")    # Modifié
    print(f"  Copie : {copie}")            # Non modifié

    print("\n--- Cas d'usage cybersécurité ---")
    # Garder une trace de l'IP originale en scan
    ip_original = ["192.168.1.1"]
    ip_modified = ip_original.copy()  # Copie pour sécurité
    ip_modified.append(":443")
    print(f"IP originale : {ip_original}")
    print(f"IP modifiée : {ip_modified}\n")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 8 : Tuples (collections immutables)
    # ═══════════════════════════════════════════════════════════

    print("=== Étape 8 : Tuples ===\n")

    # Un tuple est immuable (ne peut pas être modifié)
    # Syntaxe : (élément1, élément2)

    print("--- Création de tuples ---")
    credentials = ("admin", "password123")
    coordinates = (192, 168, 1, 1)
    single_element = (42,)  # IMPORTANT : virgule pour tuple d'1 élément !
    empty_tuple = ()

    print(f"Identifiants : {credentials}")
    print(f"Coordonnées : {coordinates}")
    print(f"Élément unique : {single_element}")
    print(f"Tuple vide : {empty_tuple}")

    print("\n--- Accès aux tuples (comme les listes) ---")
    print(f"Utilisateur : {credentials[0]}")
    print(f"Mot de passe : {credentials[1]}")
    print(f"Dernier octet IP : {coordinates[-1]}")

    print("\n--- Tuples sont immuables ---")
    print("Essai de modification d'un tuple :")
    try:
        credentials[0] = "root"
        print("[!] Modification réussie (ne devrait pas arriver ici)")
    except TypeError as e:
        print(f"[!] ERREUR : {e}")
        print("[!] Les tuples ne peuvent pas être modifiés")

    print("\n--- Unpacking de tuples ---")
    # Déballage : extraire les éléments d'un tuple
    username, password = credentials
    print(f"Username extrait : {username}")
    print(f"Password extrait : {password}")

    print("\n--- Unpacking partiel ---")
    x, y, *rest = coordinates
    print(f"x = {x}, y = {y}, rest = {rest}")

    print("\n--- Cas d'usage cybersécurité ---")
    # Tuples pour des données critiques qu'on ne veut pas modifier
    ssh_config = ("localhost", 22, "ssh-rsa", True)
    print(f"Config SSH : {ssh_config}")
    host, port, keytype, enabled = ssh_config
    print(f"Connexion : {host}:{port} (type: {keytype})\n")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 9 : List Comprehension
    # ═══════════════════════════════════════════════════════════

    print("=== Étape 9 : List Comprehension ===\n")

    # List comprehension : syntaxe compacte pour créer des listes
    # Syntaxe : [expression for item in iterable if condition]

    print("--- Création simple ---")
    squares = [x**2 for x in range(5)]
    print(f"Carrés de 0 à 4 : {squares}")

    cubes = [x**3 for x in range(1, 6)]
    print(f"Cubes de 1 à 5 : {cubes}")

    print("\n--- Avec condition (if) ---")
    evens = [x for x in range(10) if x % 2 == 0]
    print(f"Nombres pairs (0-9) : {evens}")

    odds = [x for x in range(10) if x % 2 != 0]
    print(f"Nombres impairs (0-9) : {odds}")

    print("\n--- Transformation de strings ---")
    words = ["hello", "world", "python", "security"]
    upper_words = [w.upper() for w in words]
    print(f"Originaux : {words}")
    print(f"Majuscules : {upper_words}")

    lengths = [len(w) for w in words]
    print(f"Longueurs : {lengths}")

    print("\n--- List comprehension imbriquée ---")
    # Créer une matrice 3x3
    matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
    print("Matrice multiplication :")
    for row in matrix:
        print(f"  {row}")

    print("\n--- Cas d'usage cybersécurité ---")
    # Scanner de ports : filtrer les ports ouverts
    all_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 465, 993, 995]
    critical_ports_list = [p for p in all_ports if p < 1024]
    web_ports = [p for p in all_ports if p in [80, 443, 8080, 8443]]

    print(f"Tous les ports : {all_ports}")
    print(f"Ports privilégiés : {critical_ports_list}")
    print(f"Ports web : {web_ports}")

    # Créer des tuples (IP:port)
    ips_list = ["192.168.1.1", "10.0.0.1"]
    endpoints = [(ip, 443) for ip in ips_list]
    print(f"Endpoints HTTPS : {endpoints}\n")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 10 : Opérations sur les listes
    # ═══════════════════════════════════════════════════════════

    print("=== Étape 10 : Opérations sur les listes ===\n")

    print("--- Concaténation avec + ---")
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    combined = list1 + list2
    print(f"{list1} + {list2} = {combined}")

    print("\n--- Répétition avec * ---")
    repeated = [0] * 5
    print(f"[0] * 5 = {repeated}")

    pattern = ["A", "B"] * 3
    print(f"['A', 'B'] * 3 = {pattern}")

    print("\n--- Vérification d'appartenance avec in ---")
    if 22 in ports:
        print("[+] Port 22 (SSH) trouvé dans la liste")

    if "HTTP" in services:
        print("[+] Service HTTP trouvé")

    if 9999 not in ports:
        print("[+] Port 9999 n'est pas dans la liste\n")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 11 : Exemple pratique - Scanner de ports
    # ═══════════════════════════════════════════════════════════

    print("=== Étape 11 : Exemple pratique - Scanner de ports ===\n")

    # Simulation d'un scan de ports avec résultats
    print("Scan de 192.168.1.100:\n")

    target = "192.168.1.100"
    scan_results = [
        (22, "open", "SSH"),
        (23, "closed", "Telnet"),
        (80, "open", "HTTP"),
        (443, "open", "HTTPS"),
        (3306, "filtered", "MySQL"),
        (5432, "closed", "PostgreSQL"),
        (8080, "open", "HTTP-Alt"),
    ]

    open_ports = []
    services_running = []

    for port, status, service in scan_results:
        icon = "[+]" if status == "open" else "[-]" if status == "closed" else "[~]"
        print(f"{icon} Port {port:5} | {status:8} | {service}")

        if status == "open":
            open_ports.append(port)
            services_running.append(service)

    print(f"\nRésumé :")
    print(f"Ports ouverts : {open_ports}")
    print(f"Services détectés : {services_running}")
    print(f"Total : {len(open_ports)} port(s) ouvert(s) sur {len(scan_results)}\n")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 12 : Exemple pratique - Gestion de liste noire
    # ═══════════════════════════════════════════════════════════

    print("=== Étape 12 : Exemple pratique - Gestion de liste noire ===\n")

    # Gestion d'une liste noire d'adresses IP suspectes
    blacklist = ["203.0.113.45", "198.51.100.12"]
    print(f"Liste noire initiale : {blacklist}")

    print("\n--- Signalement d'IPs malveillantes ---")
    suspicious_ips = ["203.0.113.45", "192.0.2.100", "198.51.100.50"]

    for ip in suspicious_ips:
        if ip not in blacklist:
            blacklist.append(ip)
            print(f"[+] IP {ip} ajoutée à la liste noire")
        else:
            print(f"[!] IP {ip} déjà dans la liste noire")

    print(f"\nListe noire mise à jour : {blacklist}")

    print("\n--- Suppression d'une IP ---")
    # Supposons qu'une IP a été blanchie après vérification
    ip_to_whitelist = "192.0.2.100"
    if ip_to_whitelist in blacklist:
        blacklist.remove(ip_to_whitelist)
        print(f"[+] IP {ip_to_whitelist} supprimée de la liste noire")

    print(f"Liste noire finale : {blacklist}\n")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 13 : Exemple pratique - Analyse de vulnérabilités
    # ═══════════════════════════════════════════════════════════

    print("=== Étape 13 : Exemple pratique - Analyse de vulnérabilités ===\n")

    # Base de données de vulnérabilités avec scores de sévérité
    vulnerabilities = [
        ("SQL Injection", 9.8),
        ("XSS (Stored)", 8.2),
        ("CSRF", 6.5),
        ("Auth Bypass", 9.1),
        ("Information Disclosure", 5.3),
        ("RCE", 10.0),
        ("Path Traversal", 7.2),
    ]

    print("Vulnérabilités détectées :")
    for vuln, score in vulnerabilities:
        if score >= 9.0:
            severity = "CRITIQUE"
            icon = "[CRIT]"
        elif score >= 7.0:
            severity = "ÉLEVÉ"
            icon = "[HIGH]"
        elif score >= 5.0:
            severity = "MOYEN"
            icon = "[MED]"
        else:
            severity = "FAIBLE"
            icon = "[LOW]"

        print(f"{icon} {vuln:25} | Score: {score:4.1f} | {severity}")

    # Extraire les vulnérabilités critiques
    print("\n--- Vulnérabilités CRITIQUES ---")
    critical_vulns = [vuln for vuln, score in vulnerabilities if score >= 9.0]
    for vuln in critical_vulns:
        print(f"[!] {vuln}")

    # Score moyen
    print("\n--- Analyse de sévérité ---")
    scores = [score for vuln, score in vulnerabilities]
    avg_score = sum(scores) / len(scores)
    max_score = max(scores)

    print(f"Score moyen : {avg_score:.2f}/10")
    print(f"Score maximum : {max_score:.2f}/10")
    print(f"Nombre de vulnérabilités : {len(vulnerabilities)}\n")


# ═══════════════════════════════════════════════════════════════
# Point d'entrée
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("\n" + "═" * 60)
    print("EXERCICE 07 : LISTES ET TUPLES")
    print("═" * 60 + "\n")

    main()

    print("═" * 60)
    print("FIN DE L'EXERCICE")
    print("═" * 60 + "\n")
