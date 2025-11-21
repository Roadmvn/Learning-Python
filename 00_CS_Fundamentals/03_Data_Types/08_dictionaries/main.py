"""
═══════════════════════════════════════════════════════════════
EXERCICE 08 : Dictionnaires (Dictionaries)
═══════════════════════════════════════════════════════════════

OBJECTIF :
- Maîtriser la création et l'accès aux dictionnaires
- Comprendre les paires clé-valeur
- Modifier et mettre à jour les dictionnaires
- Utiliser les méthodes principales (keys, values, items, get, update)
- Implémenter la compréhension de dictionnaire (dict comprehension)
- Travailler avec les dictionnaires imbriqués
- Appliquer aux contextes de cybersécurité et red teaming

EXÉCUTION : python main.py

═══════════════════════════════════════════════════════════════
"""

def main():
    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 1 : Créer et accéder aux dictionnaires
    # ═══════════════════════════════════════════════════════════

    print("=== Étape 1 : Créer et accéder aux dictionnaires ===\n")

    # Création simple d'un dictionnaire
    # Structure : {cle: valeur, cle2: valeur2, ...}
    # Les dictionnaires stockent des paires clé-valeur

    personne = {
        "nom": "Alice",
        "age": 30,
        "email": "alice@example.com"
    }

    print("Dictionnaire personne:")
    print(personne)
    print()

    # Accès aux valeurs par clé
    # Utilisez des crochets [] pour accéder

    print(f"Nom : {personne['nom']}")
    print(f"Âge : {personne['age']}")
    print(f"Email : {personne['email']}")
    print()

    # Exemple cybersécurité : résultats de scan de ports
    scan_resultat = {
        "cible": "192.168.1.100",
        "timestamp": "2024-11-07T10:30:00",
        "port_22": "open",
        "port_80": "open",
        "port_443": "open",
        "port_3306": "closed"
    }

    print("Résultats de scan de ports:")
    print(f"Cible : {scan_resultat['cible']}")
    print(f"Port 22 (SSH) : {scan_resultat['port_22']}")
    print(f"Port 80 (HTTP) : {scan_resultat['port_80']}")
    print(f"Port 443 (HTTPS) : {scan_resultat['port_443']}")
    print()

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 2 : Accès sécurisé avec get()
    # ═══════════════════════════════════════════════════════════

    print("=== Étape 2 : Accès sécurisé avec get() ===\n")

    # Problème : accès direct avec [] peut lever une KeyError
    # Solution : utiliser get() qui retourne None si la clé n'existe pas

    print("Accès direct avec [] :")
    try:
        # Cette ligne lèverait une erreur : print(personne["telephone"])
        print("(on évite l'erreur)")
    except KeyError:
        print("Erreur : clé non trouvée!")
    print()

    print("Accès avec get() - clé existante:")
    nom = personne.get("nom")
    print(f"Nom : {nom}")
    print()

    print("Accès avec get() - clé inexistante (retourne None):")
    telephone = personne.get("telephone")
    print(f"Téléphone : {telephone}")
    print()

    print("Accès avec get() - valeur par défaut:")
    telephone = personne.get("telephone", "Non disponible")
    print(f"Téléphone : {telephone}")
    print()

    # Exemple cybersécurité : configuration avec valeurs par défaut
    config_serveur = {
        "host": "localhost",
        "port": 8080,
        "ssl": True
    }

    print("Configuration serveur :")
    print(f"Host : {config_serveur.get('host')}")
    print(f"Port : {config_serveur.get('port', 5000)}")
    print(f"Debug : {config_serveur.get('debug', False)}")
    print()

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 3 : Modifier et ajouter des clés
    # ═══════════════════════════════════════════════════════════

    print("=== Étape 3 : Modifier et ajouter des clés ===\n")

    # Ajouter une nouvelle clé-valeur
    # Utilisez la syntaxe : dictionnaire[nouvelle_cle] = valeur

    utilisateur = {"nom": "Bob", "age": 25}
    print(f"Avant : {utilisateur}")

    # Ajouter une nouvelle clé
    utilisateur["email"] = "bob@example.com"
    print(f"Après ajout de email : {utilisateur}")

    # Modifier une clé existante
    utilisateur["age"] = 26
    print(f"Après modification d'age : {utilisateur}")
    print()

    # Exemple cybersécurité : base de données d'exploits
    exploit = {
        "nom": "CVE-2024-1234",
        "severite": "haute",
        "type": "RCE"
    }

    print(f"Exploit avant : {exploit}")

    # Ajouter des informations
    exploit["date_decouverte"] = "2024-01-15"
    exploit["patchs_disponibles"] = True
    exploit["cvss_score"] = 9.8

    print(f"Exploit après mise à jour : {exploit}")
    print()

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 4 : Supprimer des clés
    # ═══════════════════════════════════════════════════════════

    print("=== Étape 4 : Supprimer des clés ===\n")

    donnees = {"a": 1, "b": 2, "c": 3, "d": 4}
    print(f"Avant suppression : {donnees}")

    # Méthode 1 : del
    del donnees["b"]
    print(f"Après del donnees['b'] : {donnees}")

    # Méthode 2 : pop() - retourne la valeur supprimée
    valeur_c = donnees.pop("c")
    print(f"pop('c') a retourné : {valeur_c}")
    print(f"Après pop : {donnees}")

    # pop() avec valeur par défaut (pas d'erreur si clé inexistante)
    valeur_z = donnees.pop("z", "inexistante")
    print(f"pop('z', 'inexistante') a retourné : {valeur_z}")
    print()

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 5 : Méthode keys() - récupérer toutes les clés
    # ═══════════════════════════════════════════════════════════

    print("=== Étape 5 : Méthode keys() ===\n")

    serveur = {
        "hostname": "server01",
        "ip": "192.168.1.50",
        "os": "Linux",
        "ram": "16GB",
        "disque": "500GB"
    }

    print("Dictionnaire serveur :")
    print(serveur)
    print()

    print("Toutes les clés avec keys() :")
    cles = serveur.keys()
    print(cles)
    print()

    print("Itération sur les clés :")
    for cle in serveur.keys():
        print(f"  - {cle}")
    print()

    # Vérifier si une clé existe
    print("Vérifications :")
    print(f"'hostname' dans serveur : {'hostname' in serveur}")
    print(f"'cpu' dans serveur : {'cpu' in serveur}")
    print()

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 6 : Méthode values() - récupérer toutes les valeurs
    # ═══════════════════════════════════════════════════════════

    print("=== Étape 6 : Méthode values() ===\n")

    scores = {
        "alice": 95,
        "bob": 87,
        "charlie": 92,
        "diana": 88
    }

    print("Dictionnaire scores :")
    print(scores)
    print()

    print("Toutes les valeurs avec values() :")
    valeurs = scores.values()
    print(valeurs)
    print()

    print("Itération sur les valeurs :")
    for valeur in scores.values():
        print(f"  - {valeur}")
    print()

    print(f"Maximum : {max(scores.values())}")
    print(f"Minimum : {min(scores.values())}")
    print(f"Somme : {sum(scores.values())}")
    print(f"Moyenne : {sum(scores.values()) / len(scores.values()):.2f}")
    print()

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 7 : Méthode items() - paires clé-valeur
    # ═══════════════════════════════════════════════════════════

    print("=== Étape 7 : Méthode items() ===\n")

    produits = {
        "laptop": 1200,
        "souris": 25,
        "clavier": 75,
        "moniteur": 350
    }

    print("Dictionnaire produits :")
    print(produits)
    print()

    print("Paires clé-valeur avec items() :")
    paires = produits.items()
    print(paires)
    print()

    print("Itération avec unpacking :")
    for nom_produit, prix in produits.items():
        print(f"  {nom_produit}: {prix}€")
    print()

    # Exemple cybersécurité : résultats de vulnérabilités
    vulnerabilites = {
        "injection_sql": "critique",
        "xss": "haute",
        "csrf": "moyenne",
        "path_traversal": "haute"
    }

    print("Vulnérabilités détectées :")
    for vuln_type, niveau in vulnerabilites.items():
        print(f"  [{niveau}] {vuln_type}")
    print()

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 8 : Méthode update() - fusionner des dictionnaires
    # ═══════════════════════════════════════════════════════════

    print("=== Étape 8 : Méthode update() ===\n")

    config_defaut = {
        "debug": False,
        "timeout": 30,
        "max_connexions": 100
    }

    config_utilisateur = {
        "debug": True,
        "port": 8080
    }

    print(f"Config par défaut : {config_defaut}")
    print(f"Config utilisateur : {config_utilisateur}")
    print()

    # update() fusionne les dictionnaires
    # Les clés du second écrasent celles du premier
    config_defaut.update(config_utilisateur)
    print(f"Après update() : {config_defaut}")
    print()

    # Exemple cybersécurité : fusion de résultats de scan
    scan_port1 = {
        "192.168.1.100": {"port_22": "open", "port_80": "open"}
    }

    scan_port2 = {
        "192.168.1.100": {"port_443": "open"},
        "192.168.1.101": {"port_22": "open"}
    }

    # À noter : pour les valeurs complexes, update() n'est pas profond
    # (voir section sur dictionnaires imbriqués)

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 9 : Dict comprehension (création simplifiée)
    # ═══════════════════════════════════════════════════════════

    print("=== Étape 9 : Dict comprehension ===\n")

    # Dict comprehension : créer un dictionnaire avec une expression concise
    # Syntaxe : {cle: valeur for element in iterable}

    print("Créer un dict des carrés :")
    carres = {x: x**2 for x in range(1, 6)}
    print(carres)
    print()

    print("Créer un dict des puissances de 2 :")
    puissances_2 = {x: 2**x for x in range(1, 6)}
    print(puissances_2)
    print()

    # Dict comprehension avec condition
    print("Dict comprehension avec condition (nombres pairs) :")
    pairs = {x: x**2 for x in range(1, 11) if x % 2 == 0}
    print(pairs)
    print()

    # Transformer un dictionnaire existant
    print("Doubler les valeurs d'un dict :")
    original = {"a": 1, "b": 2, "c": 3}
    double = {k: v * 2 for k, v in original.items()}
    print(f"Original : {original}")
    print(f"Doublé : {double}")
    print()

    # Dict comprehension avec deux boucles
    print("Dict comprehension avec deux boucles :")
    pairs_coords = {
        f"{i}-{j}": i * j
        for i in range(1, 4)
        for j in range(1, 4)
    }
    print(pairs_coords)
    print()

    # Exemple cybersécurité : générer une liste de ports à scanner
    print("Dict comprehension : ports à scanner avec services")
    ports_communs = {
        22: "SSH",
        80: "HTTP",
        443: "HTTPS",
        3306: "MySQL",
        5432: "PostgreSQL",
        6379: "Redis",
        27017: "MongoDB"
    }

    # Créer un dict de ports avec statut initial "unknown"
    ports_a_scanner = {port: "unknown" for port, service in ports_communs.items()}
    print(ports_a_scanner)
    print()

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 10 : Dictionnaires imbriqués (nested dicts)
    # ═══════════════════════════════════════════════════════════

    print("=== Étape 10 : Dictionnaires imbriqués ===\n")

    # Dictionnaires contenant d'autres dictionnaires
    # Structure hiérarchique pour données complexes

    utilisateurs = {
        "user1": {
            "nom": "Alice",
            "age": 30,
            "email": "alice@example.com"
        },
        "user2": {
            "nom": "Bob",
            "age": 25,
            "email": "bob@example.com"
        },
        "user3": {
            "nom": "Charlie",
            "age": 35,
            "email": "charlie@example.com"
        }
    }

    print("Dictionnaire imbriqué utilisateurs :")
    print(utilisateurs)
    print()

    # Accès aux données imbriquées
    print("Accès aux données imbriquées :")
    print(f"Nom de user1 : {utilisateurs['user1']['nom']}")
    print(f"Email de user2 : {utilisateurs['user2']['email']}")
    print(f"Âge de user3 : {utilisateurs['user3']['age']}")
    print()

    # Itération sur dictionnaire imbriqué
    print("Afficher tous les utilisateurs :")
    for user_id, infos in utilisateurs.items():
        print(f"\n{user_id}:")
        for cle, valeur in infos.items():
            print(f"  {cle}: {valeur}")
    print()

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 11 : Exemple cybersécurité - Base de données d'exploits
    # ═══════════════════════════════════════════════════════════

    print("=== Étape 11 : Exemple cybersécurité - Base d'exploits ===\n")

    base_exploits = {
        "CVE-2024-1234": {
            "description": "Remote Code Execution in WebApp",
            "severite": "critique",
            "cvss_score": 9.8,
            "affected_versions": ["1.0", "1.1", "1.2"],
            "patch_disponible": True,
            "date_decouverte": "2024-01-15"
        },
        "CVE-2024-5678": {
            "description": "SQL Injection in Login Form",
            "severite": "haute",
            "cvss_score": 8.9,
            "affected_versions": ["2.0", "2.1"],
            "patch_disponible": False,
            "date_decouverte": "2024-02-20"
        },
        "CVE-2024-9999": {
            "description": "Cross-Site Scripting (XSS)",
            "severite": "moyenne",
            "cvss_score": 6.1,
            "affected_versions": ["1.5", "2.0"],
            "patch_disponible": True,
            "date_decouverte": "2024-03-10"
        }
    }

    print("Base de données d'exploits :")
    print()

    # Afficher un exploit spécifique
    print("Détails de CVE-2024-1234 :")
    exploit = base_exploits["CVE-2024-1234"]
    print(f"  Description : {exploit['description']}")
    print(f"  Sévérité : {exploit['severite']}")
    print(f"  CVSS Score : {exploit['cvss_score']}")
    print(f"  Versions affectées : {exploit['affected_versions']}")
    print(f"  Patch disponible : {exploit['patch_disponible']}")
    print()

    # Trouver les exploits critiques
    print("Exploits critiques :")
    for cve, info in base_exploits.items():
        if info["severite"] == "critique":
            print(f"  {cve}: {info['description']}")
    print()

    # Trouver les exploits sans patch
    print("Exploits sans patch disponible :")
    for cve, info in base_exploits.items():
        if not info["patch_disponible"]:
            print(f"  {cve}: {info['description']}")
    print()

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 12 : Exemple cybersécurité - Résultats de scan avancé
    # ═══════════════════════════════════════════════════════════

    print("=== Étape 12 : Exemple cybersécurité - Résultats de scan ===\n")

    resultats_scan = {
        "192.168.1.100": {
            "hostname": "web-server-01",
            "os": "Linux Ubuntu 22.04",
            "ports_ouverts": {
                22: {"service": "SSH", "version": "OpenSSH 8.9"},
                80: {"service": "HTTP", "version": "Apache 2.4.52"},
                443: {"service": "HTTPS", "version": "Apache 2.4.52"},
                3306: {"service": "MySQL", "version": "8.0.35"}
            },
            "vulnerabilites": ["CVE-2024-1234", "CVE-2024-5678"],
            "firewall_detected": True
        },
        "192.168.1.101": {
            "hostname": "db-server-01",
            "os": "Linux CentOS 7",
            "ports_ouverts": {
                22: {"service": "SSH", "version": "OpenSSH 7.4"},
                5432: {"service": "PostgreSQL", "version": "12.0"}
            },
            "vulnerabilites": [],
            "firewall_detected": True
        }
    }

    print("Résultats du scan de réseau :\n")

    # Itération sur les hôtes et leurs infos
    for ip, infos in resultats_scan.items():
        print(f"Hôte : {ip} ({infos['hostname']})")
        print(f"  OS : {infos['os']}")
        print(f"  Firewall : {'Détecté' if infos['firewall_detected'] else 'Non détecté'}")

        print(f"  Ports ouverts :")
        for port, details in infos['ports_ouverts'].items():
            print(f"    - Port {port}: {details['service']} v{details['version']}")

        if infos['vulnerabilites']:
            print(f"  Vulnérabilités trouvées : {', '.join(infos['vulnerabilites'])}")
        else:
            print(f"  Aucune vulnérabilité connue")

        print()

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 13 : Manipulation de dictionnaires imbriqués
    # ═══════════════════════════════════════════════════════════

    print("=== Étape 13 : Manipulation de dictionnaires imbriqués ===\n")

    # Créer un dictionnaire imbriqué de zéro
    configuration_reseau = {
        "interfaces": {
            "eth0": {
                "ip": "192.168.1.1",
                "masque": "255.255.255.0",
                "gateway": "192.168.1.254"
            },
            "eth1": {
                "ip": "10.0.0.1",
                "masque": "255.255.0.0",
                "gateway": "10.0.0.254"
            }
        },
        "dns": {
            "primaire": "8.8.8.8",
            "secondaire": "8.8.4.4"
        },
        "routage": {
            "enable": True,
            "static_routes": {
                "10.20.0.0/16": "192.168.1.2",
                "10.30.0.0/16": "192.168.1.3"
            }
        }
    }

    print("Configuration réseau complète :")
    print()

    # Accès en profondeur
    print(f"IP eth0 : {configuration_reseau['interfaces']['eth0']['ip']}")
    print(f"DNS primaire : {configuration_reseau['dns']['primaire']}")
    print(f"Routage activé : {configuration_reseau['routage']['enable']}")
    print()

    # Modification en profondeur
    configuration_reseau['interfaces']['eth0']['ip'] = "192.168.1.2"
    print(f"Nouvelle IP eth0 : {configuration_reseau['interfaces']['eth0']['ip']}")
    print()

    # Ajouter une nouvelle route
    configuration_reseau['routage']['static_routes']['10.40.0.0/16'] = "192.168.1.4"
    print(f"Routes statiques : {configuration_reseau['routage']['static_routes']}")
    print()

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 14 : Utilitaires utiles pour dictionnaires
    # ═══════════════════════════════════════════════════════════

    print("=== Étape 14 : Utilitaires utiles pour dictionnaires ===\n")

    donnees = {
        "alice": 95,
        "bob": 87,
        "charlie": 92,
        "diana": 88,
        "eve": 90
    }

    print(f"Dictionnaire : {donnees}\n")

    # Nombre d'éléments
    print(f"Nombre d'entrées : {len(donnees)}")
    print()

    # Vérifier l'existence d'une clé
    print(f"'alice' existe : {'alice' in donnees}")
    print(f"'frank' existe : {'frank' in donnees}")
    print()

    # Vérifier l'existence d'une valeur
    print(f"95 comme valeur : {95 in donnees.values()}")
    print(f"100 comme valeur : {100 in donnees.values()}")
    print()

    # Obtenir la clé avec la valeur maximale
    meilleur = max(donnees, key=donnees.get)
    print(f"Meilleur score : {meilleur} ({donnees[meilleur]})")
    print()

    # Obtenir la clé avec la valeur minimale
    pire = min(donnees, key=donnees.get)
    print(f"Pire score : {pire} ({donnees[pire]})")
    print()

    # Trier les clés
    print(f"Clés triées : {sorted(donnees.keys())}")
    print()

    # Trier par valeur
    print(f"Triés par score (croissant) :")
    for personne in sorted(donnees.items(), key=lambda x: x[1]):
        print(f"  {personne[0]}: {personne[1]}")
    print()

    print(f"Triés par score (décroissant) :")
    for personne in sorted(donnees.items(), key=lambda x: x[1], reverse=True):
        print(f"  {personne[0]}: {personne[1]}")
    print()


if __name__ == "__main__":
    main()
