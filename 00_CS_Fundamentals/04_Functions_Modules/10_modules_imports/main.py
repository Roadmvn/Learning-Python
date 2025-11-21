"""
═══════════════════════════════════════════════════════════════════════════════
EXERCICE 10 : Modules et Imports
═══════════════════════════════════════════════════════════════════════════════

OBJECTIF :
- Maîtriser l'import et from...import
- Utiliser les modules standards (os, sys, time, datetime, random, hashlib)
- Créer ses propres modules
- Utiliser __name__ == "__main__"
- Appliquer aux contextes de cybersécurité et red teaming

EXÉCUTION : python main.py

═══════════════════════════════════════════════════════════════════════════════
"""

# ═════════════════════════════════════════════════════════════════════════════
# ÉTAPE 1 : import basique
# ═════════════════════════════════════════════════════════════════════════════

def etape1_import_basique():
    """Démonstration de l'import basique."""

    print("═" * 79)
    print("ÉTAPE 1 : import basique")
    print("═" * 79)
    print()

    # Quand on utilise 'import', on accède aux éléments via le nom du module
    import os

    # Afficher le répertoire courant
    repertoire_courant = os.getcwd()
    print(f"Répertoire courant : {repertoire_courant}")

    # Lister les fichiers du répertoire courant
    fichiers = os.listdir('.')
    print(f"Nombre de fichiers/dossiers : {len(fichiers)}")
    print(f"Premiers fichiers : {fichiers[:3]}")

    # Vérifier l'existence d'un chemin
    chemin = '.'
    existe = os.path.exists(chemin)
    print(f"Le chemin '{chemin}' existe : {existe}")

    # Obtenir le séparateur de chemin du système
    separateur = os.sep
    print(f"Séparateur du système : '{separateur}'")

    # Vérifier si c'est un fichier ou un répertoire
    est_dossier = os.path.isdir('.')
    est_fichier = os.path.isfile('main.py')
    print(f"'.' est un dossier : {est_dossier}")
    print(f"'main.py' est un fichier : {est_fichier}")

    print()


# ═════════════════════════════════════════════════════════════════════════════
# ÉTAPE 2 : from...import
# ═════════════════════════════════════════════════════════════════════════════

def etape2_from_import():
    """Démonstration de from...import."""

    print("═" * 79)
    print("ÉTAPE 2 : from...import")
    print("═" * 79)
    print()

    # from...import permet d'importer des éléments spécifiques
    # On peut les utiliser directement sans le nom du module
    from os import getcwd, listdir, path

    # Utilisation directe sans 'os.'
    rep = getcwd()
    print(f"Répertoire courant (direct) : {rep}")

    fichiers = listdir('.')
    print(f"Fichiers (direct) : {fichiers[:2]}")

    # path est maintenant disponible directement
    existe = path.exists('.')
    print(f"Chemin existe (direct) : {existe}")

    print()


# ═════════════════════════════════════════════════════════════════════════════
# ÉTAPE 3 : import avec alias
# ═════════════════════════════════════════════════════════════════════════════

def etape3_import_alias():
    """Démonstration de l'import avec alias."""

    print("═" * 79)
    print("ÉTAPE 3 : import avec alias (as)")
    print("═" * 79)
    print()

    # import ... as permet de renommer le module
    import os as system_os
    import sys as system_sys

    # Utilisation avec alias
    rep = system_os.getcwd()
    print(f"Répertoire via alias : {rep}")

    # Accès à sys
    version = system_sys.version
    print(f"Version Python : {version.split()[0]}")

    plateforme = system_sys.platform
    print(f"Plateforme système : {plateforme}")

    # from...import avec alias
    from os.path import join as path_join

    chemin = path_join('.', 'fichier.txt')
    print(f"Chemin joint avec alias : {chemin}")

    print()


# ═════════════════════════════════════════════════════════════════════════════
# ÉTAPE 4 : Module sys
# ═════════════════════════════════════════════════════════════════════════════

def etape4_module_sys():
    """Démonstration du module sys."""

    print("═" * 79)
    print("ÉTAPE 4 : Module sys (Système et Interpréteur)")
    print("═" * 79)
    print()

    import sys

    # Arguments en ligne de commande
    print(f"Arguments CLI : {sys.argv}")
    print(f"Nombre d'arguments : {len(sys.argv)}")

    # Version Python
    print(f"\nVersion Python : {sys.version}")
    print(f"Version (tuple) : {sys.version_info}")

    # Plateforme
    print(f"\nPlateforme : {sys.platform}")

    # Encodage par défaut
    print(f"Encodage par défaut : {sys.getdefaultencoding()}")

    # Chemin d'exécution du Python
    print(f"\nExécutable Python : {sys.executable}")

    # Modules chargés (premier et dernier)
    modules_charges = list(sys.modules.keys())
    print(f"Nombre de modules chargés : {len(modules_charges)}")
    print(f"Premiers modules : {modules_charges[:3]}")

    print()


# ═════════════════════════════════════════════════════════════════════════════
# ÉTAPE 5 : Module time (Temps simple)
# ═════════════════════════════════════════════════════════════════════════════

def etape5_module_time():
    """Démonstration du module time."""

    print("═" * 79)
    print("ÉTAPE 5 : Module time (Gestion du temps)")
    print("═" * 79)
    print()

    import time

    # Timestamp Unix (secondes depuis 1970-01-01)
    timestamp = time.time()
    print(f"Timestamp Unix actuel : {timestamp}")
    print(f"Type : {type(timestamp)}")

    # Temps local structuré
    temps_local = time.localtime()
    print(f"\nTemps local (structuré) : {temps_local}")
    print(f"Année : {temps_local.tm_year}")
    print(f"Mois : {temps_local.tm_mon}")
    print(f"Jour : {temps_local.tm_mday}")
    print(f"Heure : {temps_local.tm_hour}")
    print(f"Minute : {temps_local.tm_min}")
    print(f"Seconde : {temps_local.tm_sec}")

    # Formatage du temps
    temps_formate = time.strftime("%Y-%m-%d %H:%M:%S", temps_local)
    print(f"\nTemps formaté : {temps_formate}")

    # Pause (sleep) - ATTENTION : bloque l'exécution
    print("\nPause de 1 seconde...")
    temps_avant = time.time()
    time.sleep(1)  # Pause 1 seconde
    temps_apres = time.time()
    duree = temps_apres - temps_avant
    print(f"Durée réelle de la pause : {duree:.2f} secondes")

    print()


# ═════════════════════════════════════════════════════════════════════════════
# ÉTAPE 6 : Module datetime (Dates avancées)
# ═════════════════════════════════════════════════════════════════════════════

def etape6_module_datetime():
    """Démonstration du module datetime."""

    print("═" * 79)
    print("ÉTAPE 6 : Module datetime (Dates et heures avancées)")
    print("═" * 79)
    print()

    from datetime import datetime, timedelta, date

    # Obtenir la date/heure actuelle
    maintenant = datetime.now()
    print(f"Date/Heure actuelle : {maintenant}")
    print(f"Type : {type(maintenant)}")

    # Extraire des composants
    print(f"\nAnnée : {maintenant.year}")
    print(f"Mois : {maintenant.month}")
    print(f"Jour : {maintenant.day}")
    print(f"Heure : {maintenant.hour}")
    print(f"Minute : {maintenant.minute}")
    print(f"Seconde : {maintenant.second}")

    # Convertir timestamp en datetime
    timestamp = 1609459200  # 2021-01-01 00:00:00
    dt = datetime.fromtimestamp(timestamp)
    print(f"\nDatetime du timestamp {timestamp} : {dt}")

    # Créer une date personnalisée
    date_personnalisee = datetime(2024, 12, 25, 15, 30, 0)
    print(f"Date personnalisée : {date_personnalisee}")

    # Différences de temps
    dans_7_jours = maintenant + timedelta(days=7)
    dans_2_heures = maintenant + timedelta(hours=2)
    hier = maintenant - timedelta(days=1)

    print(f"\nDans 7 jours : {dans_7_jours.date()}")
    print(f"Dans 2 heures : {dans_2_heures.strftime('%H:%M:%S')}")
    print(f"Hier : {hier.date()}")

    # Différence entre deux dates
    diff = datetime(2025, 1, 1) - maintenant
    print(f"\nJours avant 2025-01-01 : {diff.days}")
    print(f"Secondes : {diff.total_seconds():.0f}")

    # Formatage personnalisé
    formate = maintenant.strftime("%d/%m/%Y à %H:%M:%S")
    print(f"\nFormaté personnalisé : {formate}")

    print()


# ═════════════════════════════════════════════════════════════════════════════
# ÉTAPE 7 : Module random (Aléatoire)
# ═════════════════════════════════════════════════════════════════════════════

def etape7_module_random():
    """Démonstration du module random."""

    print("═" * 79)
    print("ÉTAPE 7 : Module random (Nombres et données aléatoires)")
    print("═" * 79)
    print()

    import random

    # Nombre entier aléatoire
    nombre = random.randint(1, 100)
    print(f"Nombre entier aléatoire (1-100) : {nombre}")

    # Nombre flottant aléatoire
    flottant = random.random()
    print(f"Nombre flottant (0.0-1.0) : {flottant:.4f}")

    # Nombre avec distribution
    nombre_skewed = random.gauss(100, 15)  # Moyenne 100, écart 15
    print(f"Nombre avec Gauss (moyenne=100) : {nombre_skewed:.2f}")

    # Choix dans une liste
    choix = random.choice(['apple', 'banana', 'cherry'])
    print(f"\nChoix aléatoire dans liste : {choix}")

    # Sélectionner plusieurs éléments
    plusieurs = random.sample(['a', 'b', 'c', 'd', 'e'], 3)
    print(f"3 choix sans remise : {plusieurs}")

    # Mélanger une liste
    liste = [1, 2, 3, 4, 5]
    random.shuffle(liste)
    print(f"Liste mélangée : {liste}")

    # Générer une chaîne aléatoire (utile pour red teaming)
    import string
    caracteres = string.ascii_letters + string.digits
    token = ''.join(random.choice(caracteres) for _ in range(16))
    print(f"\nToken aléatoire (16 caractères) : {token}")

    # Pondérations
    choix_pondere = random.choices(['commun', 'rare', 'epic'], weights=[70, 25, 5], k=10)
    print(f"10 choix pondérés : {choix_pondere}")

    print()


# ═════════════════════════════════════════════════════════════════════════════
# ÉTAPE 8 : Module hashlib (Hachage cryptographique)
# ═════════════════════════════════════════════════════════════════════════════

def etape8_module_hashlib():
    """Démonstration du module hashlib."""

    print("═" * 79)
    print("ÉTAPE 8 : Module hashlib (Hachage cryptographique)")
    print("═" * 79)
    print()

    import hashlib

    texte = "password123"
    texte_bytes = texte.encode('utf-8')  # Convertir en bytes

    # MD5 (ATTENTION : déprécié, ne pas utiliser pour sécurité)
    hash_md5 = hashlib.md5(texte_bytes).hexdigest()
    print(f"MD5('{texte}') : {hash_md5}")
    print(f"Longueur : {len(hash_md5)} caractères")

    # SHA1 (ATTENTION : déprécié pour cryptographie)
    hash_sha1 = hashlib.sha1(texte_bytes).hexdigest()
    print(f"\nSHA1('{texte}') : {hash_sha1}")

    # SHA256 (RECOMMANDÉ pour les mots de passe)
    hash_sha256 = hashlib.sha256(texte_bytes).hexdigest()
    print(f"\nSHA256('{texte}') : {hash_sha256}")
    print(f"Longueur : {len(hash_sha256)} caractères")

    # SHA512 (Pour sécurité maximale)
    hash_sha512 = hashlib.sha512(texte_bytes).hexdigest()
    print(f"\nSHA512('{texte}') : {hash_sha512}")
    print(f"Longueur : {len(hash_sha512)} caractères")

    # Algorithmes disponibles
    algos = hashlib.algorithms_available
    print(f"\nAlgorithmes disponibles : {sorted(list(algos))[:10]}")  # Affiche les 10 premiers

    # Hachage itératif (pour les fichiers volumineux)
    print("\nHachage itératif SHA256 :")
    h = hashlib.sha256()
    donnees_chunk1 = "Partie 1 ".encode()
    donnees_chunk2 = "Partie 2".encode()
    h.update(donnees_chunk1)
    h.update(donnees_chunk2)
    print(f"Résultat : {h.hexdigest()}")

    # Comparaison : même texte = même hash
    hash_test1 = hashlib.sha256(b"test").hexdigest()
    hash_test2 = hashlib.sha256(b"test").hexdigest()
    print(f"\nMême texte = même hash : {hash_test1 == hash_test2}")

    # Différence minime : hash complètement différent
    hash_A = hashlib.sha256(b"A").hexdigest()
    hash_B = hashlib.sha256(b"B").hexdigest()
    print(f"Hash('A') == Hash('B') : {hash_A == hash_B}")
    print(f"Hash('A') : {hash_A[:16]}...")
    print(f"Hash('B') : {hash_B[:16]}...")

    print()


# ═════════════════════════════════════════════════════════════════════════════
# ÉTAPE 9 : Créer ses propres modules
# ═════════════════════════════════════════════════════════════════════════════

def etape9_modules_personnalises():
    """Démonstration avec modules personnalisés."""

    print("═" * 79)
    print("ÉTAPE 9 : Créer et utiliser des modules personnalisés")
    print("═" * 79)
    print()

    # Dans un vrai projet, on créerait des fichiers séparés
    # Pour cette démo, on crée des fonctions ici

    # Module hypothétique : utils.py
    def saluer(nom):
        """Fonction simple de module."""
        return f"Bonjour, {nom}!"

    def additionner(a, b):
        """Additionne deux nombres."""
        return a + b

    # Module hypothétique : security.py
    def verifier_mot_de_passe(mdp):
        """Vérifie la force du mot de passe."""
        if len(mdp) < 8:
            return "Faible"
        elif len(mdp) < 12:
            return "Moyen"
        else:
            return "Fort"

    # Utilisation
    print(f"saluer('Alice') : {saluer('Alice')}")
    print(f"additionner(5, 3) : {additionner(5, 3)}")
    print(f"verifier_mot_de_passe('abc') : {verifier_mot_de_passe('abc')}")
    print(f"verifier_mot_de_passe('securePass123!') : {verifier_mot_de_passe('securePass123!')}")

    # En vrai, on ferait :
    # import utils
    # from security import verifier_mot_de_passe

    print()
    print("[INFO] Dans un vrai projet :")
    print("  - Créer utils.py avec les fonctions")
    print("  - Créer security.py avec les fonctions de sécurité")
    print("  - Importer avec : import utils, from security import verifier_mot_de_passe")

    print()


# ═════════════════════════════════════════════════════════════════════════════
# ÉTAPE 10 : __name__ == "__main__"
# ═════════════════════════════════════════════════════════════════════════════

def etape10_name_main():
    """Démonstration de __name__ == "__main__"."""

    print("═" * 79)
    print("ÉTAPE 10 : __name__ == \"__main__\"")
    print("═" * 79)
    print()

    # __name__ est une variable spéciale Python
    print(f"Valeur de __name__ dans ce script : {__name__}")
    print()

    # Explication
    print("[INFO] Quand ce fichier est exécuté directement :")
    print("  __name__ = '__main__'")
    print()
    print("[INFO] Quand ce fichier est importé comme module :")
    print("  __name__ = 'nom_du_module'")
    print()

    # Exemple d'utilisation
    def fonction_principale():
        """Fonction que l'on peut importer ou exécuter directement."""
        print("[+] Fonction principale exécutée")
        return "Résultat"

    # On exécute seulement si c'est le programme principal
    if __name__ == "__main__":
        print("[+] Ce code s'exécute car main.py est lancé directement")
    else:
        print("[-] Ce code NE s'exécute PAS car main.py est importé")

    print()


# ═════════════════════════════════════════════════════════════════════════════
# ÉTAPE 11 : Red Teaming - Cas d'usage pratiques
# ═════════════════════════════════════════════════════════════════════════════

def etape11_red_teaming():
    """Démonstration pour contextes de cybersécurité et red teaming."""

    print("═" * 79)
    print("ÉTAPE 11 : Red Teaming - Cas d'usage pratiques")
    print("═" * 79)
    print()

    import os
    import sys
    import time
    from datetime import datetime
    import random
    import hashlib

    # 1. Énumération système avec os
    print("[*] 1. ÉNUMÉRATION SYSTÈME (os)")
    print("-" * 79)
    print(f"Répertoire courant : {os.getcwd()}")
    print(f"Utilisateur : {os.getenv('USER') or 'N/A'}")
    print(f"Plateforme : {sys.platform}")
    print(f"Variables d'environnement clés : {list(os.environ.keys())[:5]}")
    print()

    # 2. Timing d'attaques (time/datetime)
    print("[*] 2. TIMING D'ATTAQUES (time/datetime)")
    print("-" * 79)
    debut = time.time()
    # Simulation d'une brute force
    for i in range(1000000):
        pass
    fin = time.time()
    duree = fin - debut
    print(f"Temps écoulé : {duree:.4f} secondes")

    timestamp = datetime.now()
    print(f"Timestamp d'attaque : {timestamp.isoformat()}")
    print()

    # 3. Génération de payloads aléatoires
    print("[*] 3. GÉNÉRATION DE PAYLOADS ALÉATOIRES (random)")
    print("-" * 79)

    # Payload SQL injection
    payload_sql = f"admin' OR '1'='1"
    print(f"Payload SQL : {payload_sql}")

    # Token de session aléatoire
    import string
    session_token = ''.join(random.choices(string.hexdigits[:-6], k=32))
    print(f"Session Token : {session_token}")

    # User-Agent aléatoire
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0)",
        "Mozilla/5.0 (Linux; Android 10)",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14)"
    ]
    user_agent = random.choice(user_agents)
    print(f"User-Agent aléatoire : {user_agent}")
    print()

    # 4. Hachage pour traces et empreintes
    print("[*] 4. HACHAGE POUR TRACES ET EMPREINTES (hashlib)")
    print("-" * 79)

    # Hash du payload pour vérification
    payload = b"attaque_payload_xyz"
    hash_payload = hashlib.sha256(payload).hexdigest()
    print(f"Payload : {payload.decode()}")
    print(f"SHA256 : {hash_payload}")

    # Hash d'une réponse serveur
    reponse_serveur = "HTTP/1.1 200 OK\nContent-Type: text/html"
    hash_reponse = hashlib.md5(reponse_serveur.encode()).hexdigest()
    print(f"\nRéponse : {reponse_serveur[:30]}...")
    print(f"MD5 empreinte : {hash_reponse}")

    # Vérifier l'intégrité
    reponse_modifiee = "HTTP/1.1 200 OK\nContent-Type: text/plain"
    hash_modifiee = hashlib.md5(reponse_modifiee.encode()).hexdigest()
    print(f"Empreinte correspondante : {hash_modifiee == hash_reponse}")
    print()

    # 5. Obfuscation avec os.urandom
    print("[*] 5. GÉNÉRATION DE DONNÉES CRYPTOGRAPHIQUES (os.urandom)")
    print("-" * 79)
    donnees_aleatoires = os.urandom(16)
    print(f"16 octets aléatoires cryptographiques : {donnees_aleatoires.hex()}")

    nonce = os.urandom(8).hex()
    print(f"Nonce pour anti-replay : {nonce}")
    print()

    # 6. Arguments de ligne de commande
    print("[*] 6. ARGUMENTS DE LIGNE DE COMMANDE (sys.argv)")
    print("-" * 79)
    print(f"Nombre d'arguments : {len(sys.argv)}")
    if len(sys.argv) > 1:
        print(f"Arguments : {sys.argv[1:]}")
    else:
        print("(Aucun argument fourni)")
    print()

    print("[+] Red teaming - Modules utilisés :")
    print("  - os : énumération système, urandom pour crypto")
    print("  - sys : récupération d'arguments d'attaque")
    print("  - time : mesure de timing, logs d'attaques")
    print("  - datetime : timestamps d'événements")
    print("  - random : génération de payloads")
    print("  - hashlib : vérification d'intégrité, empreintes")

    print()


# ═════════════════════════════════════════════════════════════════════════════
# ÉTAPE 12 : Packages et organisation
# ═════════════════════════════════════════════════════════════════════════════

def etape12_packages():
    """Démonstration des packages."""

    print("═" * 79)
    print("ÉTAPE 12 : Packages et organisation modulaire")
    print("═" * 79)
    print()

    print("[INFO] Structure d'un projet organisé :")
    print()
    print("mon_projet/")
    print("├── main.py              # Point d'entrée")
    print("├── __init__.py          # (optionnel) rend le dossier un package")
    print("├── config/")
    print("│   ├── __init__.py      # Rend config un package")
    print("│   ├── settings.py      # Configuration générale")
    print("│   └── secrets.py       # Secrets et clés")
    print("├── utils/")
    print("│   ├── __init__.py")
    print("│   ├── helpers.py       # Fonctions utilitaires")
    print("│   ├── validators.py    # Validation d'entrées")
    print("│   └── formatters.py    # Formatage de sorties")
    print("├── security/")
    print("│   ├── __init__.py")
    print("│   ├── crypto.py        # Cryptographie")
    print("│   ├── auth.py          # Authentification")
    print("│   └── hash_utils.py    # Hachage")
    print("└── tests/")
    print("    ├── test_utils.py")
    print("    └── test_security.py")
    print()

    print("[INFO] Imports possibles :")
    print()
    print("from config.settings import DATABASE_URL")
    print("from utils.validators import valider_email")
    print("from security.crypto import chiffrer")
    print("import config.secrets as secrets")
    print()

    print("[+] Avantages des packages :")
    print("  - Meilleure organisation du code")
    print("  - Séparation des responsabilités")
    print("  - Réutilisabilité")
    print("  - Facilité de maintenance")

    print()


# ═════════════════════════════════════════════════════════════════════════════
# FONCTION PRINCIPALE
# ═════════════════════════════════════════════════════════════════════════════

def main():
    """Fonction principale qui exécute toutes les étapes."""

    print("\n")
    print("█" * 79)
    print("█" + " " * 77 + "█")
    print("█" + "  EXERCICE 10 : MODULES ET IMPORTS EN PYTHON".center(77) + "█")
    print("█" + " " * 77 + "█")
    print("█" * 79)
    print()

    # Exécuter toutes les étapes
    etape1_import_basique()
    etape2_from_import()
    etape3_import_alias()
    etape4_module_sys()
    etape5_module_time()
    etape6_module_datetime()
    etape7_module_random()
    etape8_module_hashlib()
    etape9_modules_personnalises()
    etape10_name_main()
    etape11_red_teaming()
    etape12_packages()

    print("█" * 79)
    print("█" + " " * 77 + "█")
    print("█" + "  FIN DE LA DÉMONSTRATION".center(77) + "█")
    print("█" + " " * 77 + "█")
    print("█" * 79)
    print()
    print("[+] Concepts maîtrisés :")
    print("  ✓ import et from...import")
    print("  ✓ Modules standards (os, sys, time, datetime, random, hashlib)")
    print("  ✓ Création de modules personnalisés")
    print("  ✓ __name__ == '__main__'")
    print("  ✓ Organisation en packages")
    print("  ✓ Red teaming avec modules")
    print()


# ═════════════════════════════════════════════════════════════════════════════
# POINT D'ENTRÉE
# ═════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    # Ce code s'exécute SEULEMENT si main.py est lancé directement
    # Il ne s'exécute PAS si main.py est importé comme module
    main()
