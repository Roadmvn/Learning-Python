"""
═══════════════════════════════════════════════════════════════
EXERCICE 02 : Variables et Types
═══════════════════════════════════════════════════════════════

OBJECTIF :
- Comprendre les variables Python
- Maîtriser les types de données de base (int, float, str, bool)
- Effectuer des conversions de types
- Utiliser des f-strings pour afficher les variables

EXÉCUTION : python main.py

═══════════════════════════════════════════════════════════════
"""

def main():
    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 1 : Créer des variables
    # ═══════════════════════════════════════════════════════════

    print("=== Étape 1 : Créer des variables ===\n")

    # En Python, on crée une variable simplement en lui assignant une valeur
    # Pas besoin de déclarer le type (typage dynamique)

    nom = "Alice"
    age = 25
    taille = 1.68
    est_hacker = True

    # Affichons ces variables
    print(f"Nom : {nom}")
    print(f"Age : {age}")
    print(f"Taille : {taille}m")
    print(f"Est hacker : {est_hacker}")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 2 : Types de données (int)
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 2 : Type int (entiers) ===\n")

    # int = nombres entiers (positifs ou négatifs)
    port_ssh = 22
    port_http = 80
    port_https = 443
    tentatives_connexion = 0
    delta_temps = -5

    print(f"Port SSH : {port_ssh}")
    print(f"Port HTTP : {port_http}")
    print(f"Port HTTPS : {port_https}")
    print(f"Tentatives : {tentatives_connexion}")
    print(f"Delta temps : {delta_temps}")

    # Vérifier le type avec type()
    print(f"\nType de port_ssh : {type(port_ssh)}")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 3 : Types de données (float)
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 3 : Type float (décimaux) ===\n")

    # float = nombres à virgule flottante
    taux_reussite = 87.5
    temps_execution = 0.0023
    probabilite = 0.95
    pi = 3.14159

    print(f"Taux de réussite : {taux_reussite}%")
    print(f"Temps d'exécution : {temps_execution} secondes")
    print(f"Probabilité : {probabilite}")
    print(f"Pi : {pi}")

    print(f"\nType de taux_reussite : {type(taux_reussite)}")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 4 : Types de données (str)
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 4 : Type str (chaînes de caractères) ===\n")

    # str = chaînes de caractères (texte)
    # Peuvent être entre guillemets simples ' ou doubles "
    cible = "192.168.1.100"
    nom_utilisateur = 'admin'
    mot_de_passe = "P@ssw0rd123"
    hash_md5 = "5f4dcc3b5aa765d61d8327deb882cf99"

    print(f"Cible : {cible}")
    print(f"Utilisateur : {nom_utilisateur}")
    print(f"Mot de passe : {mot_de_passe}")
    print(f"Hash MD5 : {hash_md5}")

    print(f"\nType de cible : {type(cible)}")

    # Les chaînes peuvent être concaténées avec +
    prenom = "John"
    nom_famille = "Doe"
    nom_complet = prenom + " " + nom_famille
    print(f"\nNom complet : {nom_complet}")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 5 : Types de données (bool)
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 5 : Type bool (booléens) ===\n")

    # bool = booléens (True ou False)
    # Attention : majuscule obligatoire (True, pas true)
    systeme_vulnerable = True
    firewall_actif = False
    port_ouvert = True
    ssl_valide = False

    print(f"Système vulnérable : {systeme_vulnerable}")
    print(f"Firewall actif : {firewall_actif}")
    print(f"Port ouvert : {port_ouvert}")
    print(f"SSL valide : {ssl_valide}")

    print(f"\nType de systeme_vulnerable : {type(systeme_vulnerable)}")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 6 : Conversion de types (Casting)
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 6 : Conversion de types ===\n")

    # Souvent, on doit convertir un type en un autre

    # str → int
    port_str = "8080"
    port_int = int(port_str)
    print(f"Port (str) : {port_str} → Type : {type(port_str)}")
    print(f"Port (int) : {port_int} → Type : {type(port_int)}")

    # str → float
    version_str = "1.5"
    version_float = float(version_str)
    print(f"\nVersion (str) : {version_str} → Type : {type(version_str)}")
    print(f"Version (float) : {version_float} → Type : {type(version_float)}")

    # int → str
    nombre = 42
    nombre_str = str(nombre)
    print(f"\nNombre (int) : {nombre} → Type : {type(nombre)}")
    print(f"Nombre (str) : {nombre_str} → Type : {type(nombre_str)}")

    # float → int (arrondi vers le bas)
    decimal = 3.99
    entier = int(decimal)
    print(f"\nDécimal : {decimal}")
    print(f"Converti en int : {entier}")  # Donne 3, pas 4 !

    # int → bool (0 = False, tout le reste = True)
    print(f"\nbool(0) = {bool(0)}")
    print(f"bool(1) = {bool(1)}")
    print(f"bool(42) = {bool(42)}")
    print(f"bool(-5) = {bool(-5)}")

    # str → bool (chaîne vide = False, reste = True)
    print(f"\nbool('') = {bool('')}")
    print(f"bool('Hello') = {bool('Hello')}")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 7 : Affichage avec f-strings
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 7 : f-strings (formatage moderne) ===\n")

    # f-strings = façon moderne et puissante d'afficher des variables
    # Syntaxe : f"texte {variable}"

    ip = "10.0.0.1"
    port = 443
    protocole = "HTTPS"

    # Méthode ancienne (éviter)
    print("Connexion à " + ip + ":" + str(port))

    # Méthode moderne (recommandée)
    print(f"Connexion à {ip}:{port}")
    print(f"Protocole : {protocole}")

    # f-strings avec expressions
    longueur_mdp = 16
    print(f"Longueur du mot de passe : {longueur_mdp} caractères")
    print(f"Longueur sécurisée : {longueur_mdp >= 12}")

    # f-strings avec formatage
    pourcentage = 0.8765
    print(f"\nTaux de réussite : {pourcentage:.2%}")  # 2 décimales + %
    print(f"Taux de réussite : {pourcentage * 100:.1f}%")  # 1 décimale

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 8 : Conventions de nommage
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 8 : Conventions de nommage ===\n")

    # ✅ BON : noms descriptifs en snake_case
    adresse_ip_cible = "192.168.1.1"
    nombre_tentatives_max = 3
    delai_entre_requetes = 0.5

    # ❌ MAUVAIS : noms cryptiques
    # x = "192.168.1.1"
    # n = 3
    # d = 0.5

    print("✅ Utilisez des noms descriptifs et clairs")
    print(f"Adresse IP cible : {adresse_ip_cible}")
    print(f"Nombre de tentatives max : {nombre_tentatives_max}")
    print(f"Délai entre requêtes : {delai_entre_requetes}s")

    # Les variables sont sensibles à la casse
    Port = 80
    port = 443
    PORT = 8080
    print(f"\nPort (majuscule) : {Port}")
    print(f"port (minuscule) : {port}")
    print(f"PORT (tout en majuscule) : {PORT}")
    print("→ Ce sont 3 variables différentes !")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 9 : Exemple pratique - Scanner de ports
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 9 : Exemple pratique ===\n")

    # Simulons un résultat de scan de port
    ip_cible = "192.168.1.100"
    port_scanne = 22
    port_ouvert = True
    service_detecte = "SSH"
    version_service = "OpenSSH 8.2"
    temps_reponse = 0.0042

    print("═" * 50)
    print("RÉSULTAT DU SCAN DE PORT")
    print("═" * 50)
    print(f"Cible          : {ip_cible}")
    print(f"Port           : {port_scanne}")
    print(f"État           : {'OUVERT' if port_ouvert else 'FERMÉ'}")
    print(f"Service        : {service_detecte}")
    print(f"Version        : {version_service}")
    print(f"Temps réponse  : {temps_reponse * 1000:.2f}ms")
    print("═" * 50)


# ═══════════════════════════════════════════════════════════════
# Point d'entrée
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    main()
