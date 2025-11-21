"""
═══════════════════════════════════════════════════════════════════════════════
EXERCICE 11 : Gestion de Fichiers
═══════════════════════════════════════════════════════════════════════════════

OBJECTIF :
- Maîtriser open/read/write/close
- Utiliser le context manager with
- Comprendre les modes de fichiers
- Travailler avec JSON
- Gérer les chemins (os.path, pathlib)
- Appliquer aux contextes de cybersécurité et red teaming

EXÉCUTION : python main.py

═══════════════════════════════════════════════════════════════════════════════
"""

import os
import json
from pathlib import Path
from datetime import datetime


# ═════════════════════════════════════════════════════════════════════════════
# ÉTAPE 1 : Ouverture et fermeture de fichiers basique
# ═════════════════════════════════════════════════════════════════════════════

def etape1_ouverture_basique():
    """Démonstration de l'ouverture et fermeture basique."""

    print("═" * 79)
    print("ÉTAPE 1 : Ouverture et fermeture basique")
    print("═" * 79)
    print()

    # DANGER : Ancien style (ne pas oublier le close)
    print("[!] ANCIEN STYLE (pas recommandé) :")
    try:
        f = open('temp_test.txt', 'w')
        f.write("Ceci est un test\n")
        f.write("Deuxième ligne\n")
        f.close()  # IMPORTANT : Ne pas oublier !
        print(f"  Fichier créé et fermé manuellement")
        print(f"  État du fichier fermé : {f.closed}")  # True après close()
    except Exception as e:
        print(f"  Erreur : {e}")

    print()

    # BON : Utiliser with (recommandé)
    print("[+] BON STYLE (recommandé avec 'with') :")
    try:
        with open('temp_test.txt', 'r') as f:
            contenu = f.read()
            print(f"  Contenu du fichier :")
            for ligne in contenu.split('\n')[:2]:
                print(f"    {ligne}")
        # Fichier fermé automatiquement après le bloc with
        print(f"  Fichier fermé automatiquement après 'with'")
    except FileNotFoundError:
        print(f"  Fichier non trouvé")
    except Exception as e:
        print(f"  Erreur : {e}")

    print()


# ═════════════════════════════════════════════════════════════════════════════
# ÉTAPE 2 : Modes de fichiers
# ═════════════════════════════════════════════════════════════════════════════

def etape2_modes_fichiers():
    """Démonstration des différents modes de fichiers."""

    print("═" * 79)
    print("ÉTAPE 2 : Modes de fichiers")
    print("═" * 79)
    print()

    # MODE 'w' : Écriture (crée ou écrase)
    print("[*] Mode 'w' : Écriture (crée ou écrase)")
    with open('mode_w.txt', 'w') as f:
        f.write("Première version\n")
        f.write("Ligne 2\n")
    print(f"  Fichier mode_w.txt créé avec 'w'")

    # Écrase le fichier
    with open('mode_w.txt', 'w') as f:
        f.write("Deuxième version (écrasé)\n")
    print(f"  Fichier écrasé avec 'w'")

    print()

    # MODE 'r' : Lecture
    print("[*] Mode 'r' : Lecture")
    with open('mode_w.txt', 'r') as f:
        contenu = f.read()
        print(f"  Contenu : {contenu.strip()}")
    print(f"  Fichier lu avec 'r'")

    print()

    # MODE 'a' : Ajout (ajoute à la fin)
    print("[*] Mode 'a' : Ajout (ajoute à la fin)")
    with open('mode_w.txt', 'a') as f:
        f.write("Ligne ajoutée\n")
        f.write("Autre ligne\n")
    print(f"  Contenu ajouté avec 'a'")

    with open('mode_w.txt', 'r') as f:
        lignes = f.readlines()
        print(f"  Nombre de lignes : {len(lignes)}")

    print()

    # MODE 'x' : Création exclusive
    print("[*] Mode 'x' : Création exclusive (erreur si existe)")
    try:
        with open('mode_x.txt', 'x') as f:
            f.write("Création exclusive\n")
        print(f"  Fichier créé avec 'x'")
    except FileExistsError:
        print(f"  Fichier mode_x.txt existe déjà (normal si run précédent)")

    print()

    # MODE 'r+' : Lecture et Écriture
    print("[*] Mode 'r+' : Lecture ET Écriture")
    try:
        with open('mode_w.txt', 'r+') as f:
            contenu_original = f.read()
            f.seek(0)  # Retour au début
            f.write("DÉBUT MODIFIÉ\n")
        print(f"  Fichier modifié en mode 'r+'")
    except Exception as e:
        print(f"  Erreur : {e}")

    print()

    # Nettoyage
    for fichier in ['temp_test.txt', 'mode_w.txt', 'mode_x.txt']:
        if os.path.exists(fichier):
            os.remove(fichier)

    print()


# ═════════════════════════════════════════════════════════════════════════════
# ÉTAPE 3 : Lecture de fichiers
# ═════════════════════════════════════════════════════════════════════════════

def etape3_lecture_fichiers():
    """Démonstration de la lecture de fichiers."""

    print("═" * 79)
    print("ÉTAPE 3 : Lecture de fichiers")
    print("═" * 79)
    print()

    # Créer un fichier de test
    print("[*] Création d'un fichier de test")
    with open('fichier_test.txt', 'w') as f:
        f.write("Ligne 1 : Data de test\n")
        f.write("Ligne 2 : Plus de données\n")
        f.write("Ligne 3 : Fin du fichier\n")
    print(f"  Fichier créé : fichier_test.txt")
    print()

    # read() : Lire tout
    print("[*] Méthode read() : Lire le fichier entier")
    with open('fichier_test.txt', 'r') as f:
        contenu = f.read()
        print(f"  Contenu complet :")
        print(f"  {repr(contenu)}")  # repr pour voir les \n
        print(f"  Longueur : {len(contenu)} caractères")
    print()

    # readline() : Lire ligne par ligne
    print("[*] Méthode readline() : Lire une ligne à la fois")
    with open('fichier_test.txt', 'r') as f:
        ligne1 = f.readline()
        ligne2 = f.readline()
        print(f"  Ligne 1 : {ligne1.strip()}")
        print(f"  Ligne 2 : {ligne2.strip()}")
    print()

    # readlines() : Lire toutes les lignes dans une liste
    print("[*] Méthode readlines() : Lire toutes les lignes")
    with open('fichier_test.txt', 'r') as f:
        lignes = f.readlines()
        print(f"  Type : {type(lignes)}")
        print(f"  Nombre de lignes : {len(lignes)}")
        for i, ligne in enumerate(lignes, 1):
            print(f"    Ligne {i} : {ligne.strip()}")
    print()

    # Itération directe
    print("[*] Itération directe sur le fichier")
    with open('fichier_test.txt', 'r') as f:
        for i, ligne in enumerate(f, 1):
            print(f"    Ligne {i} : {ligne.strip()}")
    print()

    # Nettoyer
    os.remove('fichier_test.txt')

    print()


# ═════════════════════════════════════════════════════════════════════════════
# ÉTAPE 4 : Écriture de fichiers
# ═════════════════════════════════════════════════════════════════════════════

def etape4_ecriture_fichiers():
    """Démonstration de l'écriture de fichiers."""

    print("═" * 79)
    print("ÉTAPE 4 : Écriture de fichiers")
    print("═" * 79)
    print()

    # write() : Écrire du texte
    print("[*] Méthode write() : Écrire du texte")
    with open('ecriture_test.txt', 'w') as f:
        f.write("Première ligne écrite\n")
        f.write("Deuxième ligne écrite\n")
    print(f"  Fichier créé avec write()")

    with open('ecriture_test.txt', 'r') as f:
        print(f"  Contenu :\n    {f.read().replace(chr(10), chr(10) + '    ')}")
    print()

    # writelines() : Écrire plusieurs lignes
    print("[*] Méthode writelines() : Écrire plusieurs lignes")
    lignes = ["Ligne 1 via writelines\n", "Ligne 2 via writelines\n", "Ligne 3\n"]
    with open('writelines_test.txt', 'w') as f:
        f.writelines(lignes)
    print(f"  Fichier créé avec writelines()")

    with open('writelines_test.txt', 'r') as f:
        contenu = f.read()
        print(f"  Contenu : {repr(contenu)}")
    print()

    # Ajout avec mode 'a'
    print("[*] Ajout de contenu avec mode 'a'")
    with open('ecriture_test.txt', 'a') as f:
        f.write("Ligne ajoutée après\n")

    with open('ecriture_test.txt', 'r') as f:
        print(f"  Lignes après ajout : {len(f.readlines())}")
    print()

    # Nettoyer
    os.remove('ecriture_test.txt')
    os.remove('writelines_test.txt')

    print()


# ═════════════════════════════════════════════════════════════════════════════
# ÉTAPE 5 : Context Manager (with)
# ═════════════════════════════════════════════════════════════════════════════

def etape5_context_manager():
    """Démonstration du context manager 'with'."""

    print("═" * 79)
    print("ÉTAPE 5 : Context Manager (with)")
    print("═" * 79)
    print()

    print("[INFO] Le context manager 'with' garantit la fermeture du fichier")
    print()

    # Créer un fichier
    with open('context_test.txt', 'w') as f:
        f.write("Données du context manager\n")

    # Lire avec with
    print("[*] Lecture avec 'with'")
    with open('context_test.txt', 'r') as f:
        print(f"  Fichier ouvert")
        print(f"  État du fichier : fermé = {f.closed}")
        contenu = f.read()
        print(f"  Contenu lu : {contenu.strip()}")
    print(f"  Après 'with' : fermé = True")
    print(f"  (Fichier fermé automatiquement)")
    print()

    # Avantage : Gestion automatique des exceptions
    print("[*] Gestion automatique des exceptions")
    try:
        with open('context_test.txt', 'r') as f:
            # Même s'il y a une erreur, le fichier sera fermé
            contenu = f.read()
            # ... traitement ...
    except Exception as e:
        print(f"  Erreur capturée : {e}")
    print(f"  Fichier fermé même après l'erreur")
    print()

    # Multiple context managers
    print("[*] Plusieurs fichiers avec 'with'")
    with open('source.txt', 'w') as src:
        src.write("Contenu source\n")

    with open('source.txt', 'r') as src, open('destination.txt', 'w') as dst:
        contenu = src.read()
        dst.write(contenu)
    print(f"  Fichier copié de source.txt à destination.txt")

    # Nettoyer
    for f in ['context_test.txt', 'source.txt', 'destination.txt']:
        if os.path.exists(f):
            os.remove(f)

    print()


# ═════════════════════════════════════════════════════════════════════════════
# ÉTAPE 6 : Travail avec JSON
# ═════════════════════════════════════════════════════════════════════════════

def etape6_json():
    """Démonstration du travail avec JSON."""

    print("═" * 79)
    print("ÉTAPE 6 : Travail avec JSON")
    print("═" * 79)
    print()

    # Écrire JSON dans un fichier
    print("[*] Écriture de JSON dans un fichier")
    donnees = {
        "nom": "Scanner Sécurité",
        "version": "1.0.0",
        "cibles": ["192.168.1.1", "192.168.1.2"],
        "resultats": {
            "ports_ouverts": [80, 443, 22],
            "vulnerabilites": 3
        }
    }

    with open('config.json', 'w') as f:
        json.dump(donnees, f, indent=2)
    print(f"  Fichier config.json créé")
    print()

    # Afficher le contenu
    print("[*] Contenu du fichier JSON")
    with open('config.json', 'r') as f:
        contenu_json = f.read()
        print(f"  {contenu_json}")
    print()

    # Lire JSON depuis un fichier
    print("[*] Lecture de JSON depuis un fichier")
    with open('config.json', 'r') as f:
        donnees_chargees = json.load(f)

    print(f"  Type chargé : {type(donnees_chargees)}")
    print(f"  Nom : {donnees_chargees['nom']}")
    print(f"  Version : {donnees_chargees['version']}")
    print(f"  Cibles : {donnees_chargees['cibles']}")
    print(f"  Vulnérabilités trouvées : {donnees_chargees['resultats']['vulnerabilites']}")
    print()

    # json.dumps() et json.loads()
    print("[*] Conversion JSON - Chaîne - Objet")

    # Objet Python -> Chaîne JSON
    chaine_json = json.dumps({"test": "valeur", "nombre": 42}, indent=2)
    print(f"  Chaîne JSON : {type(chaine_json)}")
    print(f"  {chaine_json}")

    # Chaîne JSON -> Objet Python
    objet = json.loads('{"nom": "Alice", "age": 30}')
    print(f"  Objet Python : {type(objet)}")
    print(f"  Nom : {objet['nom']}, Age : {objet['age']}")
    print()

    # Nettoyer
    os.remove('config.json')

    print()


# ═════════════════════════════════════════════════════════════════════════════
# ÉTAPE 7 : Gestion des chemins avec os.path
# ═════════════════════════════════════════════════════════════════════════════

def etape7_chemins_os():
    """Démonstration de la gestion des chemins avec os.path."""

    print("═" * 79)
    print("ÉTAPE 7 : Gestion des chemins avec os.path")
    print("═" * 79)
    print()

    # Répertoire courant
    print("[*] Répertoire courant")
    rep_courant = os.getcwd()
    print(f"  Répertoire : {rep_courant}")
    print()

    # Rejoindre des chemins
    print("[*] Jointure de chemins (os.path.join)")
    chemin = os.path.join(rep_courant, 'dossier', 'fichier.txt')
    print(f"  Chemin joint : {chemin}")
    print(f"  Séparateur : '{os.sep}'")
    print()

    # Vérifier existence
    print("[*] Vérification d'existence")
    # Créer un fichier temporaire
    chemin_temp = os.path.join(rep_courant, 'temp_chemin.txt')
    with open(chemin_temp, 'w') as f:
        f.write("test")

    existe = os.path.exists(chemin_temp)
    print(f"  Fichier existe : {existe}")

    nexiste_pas = os.path.exists('/chemin/inexistant/fichier.txt')
    print(f"  Chemin inexistant existe : {nexiste_pas}")
    print()

    # Vérifier type
    print("[*] Vérification du type")
    est_fichier = os.path.isfile(chemin_temp)
    est_dossier = os.path.isdir(chemin_temp)
    print(f"  Est un fichier : {est_fichier}")
    print(f"  Est un dossier : {est_dossier}")
    est_dossier_rep = os.path.isdir(rep_courant)
    print(f"  Répertoire courant est un dossier : {est_dossier_rep}")
    print()

    # Extraire nom et répertoire
    print("[*] Extraction du nom et du répertoire")
    chemin_test = '/home/user/documents/fichier.txt'
    nom = os.path.basename(chemin_test)
    rep = os.path.dirname(chemin_test)
    print(f"  Chemin complet : {chemin_test}")
    print(f"  Nom du fichier : {nom}")
    print(f"  Répertoire : {rep}")
    print()

    # Chemin absolu
    print("[*] Chemin absolu")
    chemin_absolu = os.path.abspath('.')
    print(f"  Chemin absolu de '.' : {chemin_absolu}")
    print()

    # Nettoyer
    os.remove(chemin_temp)

    print()


# ═════════════════════════════════════════════════════════════════════════════
# ÉTAPE 8 : Gestion des chemins avec pathlib
# ═════════════════════════════════════════════════════════════════════════════

def etape8_chemins_pathlib():
    """Démonstration de la gestion des chemins avec pathlib."""

    print("═" * 79)
    print("ÉTAPE 8 : Gestion des chemins avec pathlib")
    print("═" * 79)
    print()

    # Créer un objet Path
    print("[*] Créer un objet Path")
    p = Path('fichier_pathlib.txt')
    print(f"  Type : {type(p)}")
    print(f"  Chemin : {p}")
    print()

    # Créer et lire avec pathlib
    print("[*] Écrire avec pathlib")
    p.write_text("Contenu écrit avec pathlib\n")
    print(f"  Fichier créé")

    print("[*] Lire avec pathlib")
    contenu = p.read_text()
    print(f"  Contenu : {contenu.strip()}")
    print()

    # Vérifier existence
    print("[*] Vérifier existence et type")
    existe = p.exists()
    est_fichier = p.is_file()
    est_dossier = p.is_dir()
    print(f"  Fichier existe : {existe}")
    print(f"  Est un fichier : {est_fichier}")
    print(f"  Est un dossier : {est_dossier}")
    print()

    # Extraire composants
    print("[*] Extraire composants du chemin")
    chemin_complet = Path('/home/user/documents/rapport.txt')
    print(f"  Chemin complet : {chemin_complet}")
    print(f"  Nom du fichier (.name) : {chemin_complet.name}")
    print(f"  Extension (.suffix) : {chemin_complet.suffix}")
    print(f"  Répertoire parent (.parent) : {chemin_complet.parent}")
    print()

    # Jointure de chemins
    print("[*] Jointure de chemins avec pathlib")
    dossier = Path('/home/user')
    nouveau_chemin = dossier / 'documents' / 'nouveau.txt'
    print(f"  Chemin joint : {nouveau_chemin}")
    print()

    # Avantage : Portabilité
    print("[*] Avantage de pathlib : Portabilité")
    print(f"  os.path.join : {os.path.join('dossier', 'fichier.txt')}")
    print(f"  pathlib : {Path('dossier') / 'fichier.txt'}")
    print("  (Fonctionne identiquement sur Windows/Linux/Mac)")
    print()

    # Nettoyer
    p.unlink()  # Supprimer le fichier

    print()


# ═════════════════════════════════════════════════════════════════════════════
# ÉTAPE 9 : Red Teaming - Logs d'attaques
# ═════════════════════════════════════════════════════════════════════════════

def etape9_red_teaming_logs():
    """Démonstration pour logs de red teaming."""

    print("═" * 79)
    print("ÉTAPE 9 : Red Teaming - Logs d'attaques")
    print("═" * 79)
    print()

    # Créer un fichier de log
    print("[*] Création d'un fichier de log d'attaque")

    logs = []
    timestamp = datetime.now().isoformat()

    # Simulation de logs d'attaque
    logs.append(f"[{timestamp}] [INFO] Démarrage du scanner")
    logs.append(f"[{timestamp}] [ENUM] Cible : 192.168.1.1")
    logs.append(f"[{timestamp}] [SCAN] Port 22 : OUVERT (SSH)")
    logs.append(f"[{timestamp}] [SCAN] Port 80 : OUVERT (HTTP)")
    logs.append(f"[{timestamp}] [SCAN] Port 443 : OUVERT (HTTPS)")
    logs.append(f"[{timestamp}] [VULN] Service outdated détecté")
    logs.append(f"[{timestamp}] [EXPLOIT] Tentative d'exploitation en cours...")
    logs.append(f"[{timestamp}] [SUCCESS] Accès obtenu !")

    # Écrire les logs
    with open('attack_logs.txt', 'w') as f:
        for log in logs:
            f.write(log + '\n')

    print(f"  Fichier attack_logs.txt créé")
    print(f"  Nombre d'entrées : {len(logs)}")
    print()

    # Lire les logs
    print("[*] Lecture des logs")
    with open('attack_logs.txt', 'r') as f:
        for i, ligne in enumerate(f, 1):
            print(f"  {ligne.strip()}")
    print()

    # Analyser les logs
    print("[*] Analyse des logs")
    with open('attack_logs.txt', 'r') as f:
        contenu = f.read()

    succès = contenu.count('[SUCCESS]')
    vulns = contenu.count('[VULN]')
    enumeration = contenu.count('[ENUM]')

    print(f"  Énumérations : {enumeration}")
    print(f"  Vulnérabilités trouvées : {vulns}")
    print(f"  Succès : {succès}")
    print()

    # Nettoyer
    os.remove('attack_logs.txt')

    print()


# ═════════════════════════════════════════════════════════════════════════════
# ÉTAPE 10 : Red Teaming - Configuration stockée en JSON
# ═════════════════════════════════════════════════════════════════════════════

def etape10_red_teaming_config():
    """Démonstration pour configuration de red teaming."""

    print("═" * 79)
    print("ÉTAPE 10 : Red Teaming - Configuration en JSON")
    print("═" * 79)
    print()

    # Configuration d'attaque
    print("[*] Configuration d'attaque sauvegardée en JSON")

    config_attaque = {
        "nom_campagne": "Pentest Client XYZ",
        "date_debut": "2024-11-07",
        "scope": {
            "cibles_ip": ["192.168.1.0/24", "10.0.0.0/8"],
            "domaines": ["example.com", "corp.example.com"],
            "exclusions": ["192.168.1.1"]
        },
        "techniques": {
            "reconnaissance": ["nmap", "whois", "dns_enumeration"],
            "scanning": ["port_scan", "service_detection"],
            "exploitation": ["sql_injection", "rce", "privilege_escalation"]
        },
        "resultats": {
            "ports_ouverts": [22, 80, 443, 3306, 5432],
            "services": ["SSH", "HTTP", "HTTPS", "MySQL", "PostgreSQL"],
            "vulnerabilites": [
                {"id": "CVE-2024-1234", "severite": "CRITICAL"},
                {"id": "CVE-2024-5678", "severite": "HIGH"},
                {"id": "CVE-2024-9999", "severite": "MEDIUM"}
            ]
        },
        "timestamps": {
            "scan_debut": "2024-11-07T10:00:00",
            "scan_fin": "2024-11-07T14:30:00"
        }
    }

    # Sauvegarder en JSON
    with open('pentest_config.json', 'w') as f:
        json.dump(config_attaque, f, indent=2)

    print(f"  Fichier pentest_config.json créé")
    print()

    # Afficher structure
    print("[*] Structure de la configuration")
    print(f"  Campagne : {config_attaque['nom_campagne']}")
    print(f"  Cibles : {config_attaque['scope']['cibles_ip']}")
    print(f"  Techniques : {len(config_attaque['techniques'])} catégories")
    print(f"  Vulnérabilités trouvées : {len(config_attaque['resultats']['vulnerabilites'])}")
    print()

    # Charger et afficher
    print("[*] Chargement et affichage de la configuration")
    with open('pentest_config.json', 'r') as f:
        config_chargee = json.load(f)

    print(f"  Campagne chargée : {config_chargee['nom_campagne']}")
    print(f"  Ports ouverts : {config_chargee['resultats']['ports_ouverts']}")
    print()

    # Nettoyer
    os.remove('pentest_config.json')

    print()


# ═════════════════════════════════════════════════════════════════════════════
# ÉTAPE 11 : Red Teaming - Résultats de scan exportés
# ═════════════════════════════════════════════════════════════════════════════

def etape11_red_teaming_resultats():
    """Démonstration pour export de résultats de scan."""

    print("═" * 79)
    print("ÉTAPE 11 : Red Teaming - Export de résultats de scan")
    print("═" * 79)
    print()

    # Résultats de scan
    print("[*] Création d'un rapport de scan")

    resultats_scan = {
        "scan_id": "SCAN-20241107-001",
        "cible": "192.168.1.1",
        "timestamp": datetime.now().isoformat(),
        "statut": "COMPLET",
        "hosts_decouverts": [
            {
                "ip": "192.168.1.1",
                "mac": "00:11:22:33:44:55",
                "hostname": "router.local",
                "os": "Linux",
                "ports": {
                    "22": {"state": "open", "service": "ssh"},
                    "80": {"state": "open", "service": "http"},
                    "443": {"state": "open", "service": "https"}
                }
            },
            {
                "ip": "192.168.1.100",
                "mac": "AA:BB:CC:DD:EE:FF",
                "hostname": "workstation.local",
                "os": "Windows",
                "ports": {
                    "445": {"state": "open", "service": "smb"},
                    "3389": {"state": "open", "service": "rdp"}
                }
            }
        ],
        "vulnerabilites": [
            {"id": "CVE-2024-0001", "host": "192.168.1.1", "severity": "CRITICAL"},
            {"id": "CVE-2024-0002", "host": "192.168.1.100", "severity": "HIGH"}
        ]
    }

    # Sauvegarder les résultats
    with open('scan_results.json', 'w') as f:
        json.dump(resultats_scan, f, indent=2)

    print(f"  Fichier scan_results.json créé")
    print()

    # Créer un rapport texte
    print("[*] Création d'un rapport texte")
    rapport_texte = f"""
═══════════════════════════════════════════════════════════════════════════════
RAPPORT DE SCAN DE SÉCURITÉ
═══════════════════════════════════════════════════════════════════════════════

Scan ID : {resultats_scan['scan_id']}
Cible : {resultats_scan['cible']}
Date : {resultats_scan['timestamp']}
Statut : {resultats_scan['statut']}

HOSTS DÉCOUVERTS : {len(resultats_scan['hosts_decouverts'])}

VULNÉRABILITÉS : {len(resultats_scan['vulnerabilites'])}
- CVE-2024-0001 (CRITICAL)
- CVE-2024-0002 (HIGH)

═══════════════════════════════════════════════════════════════════════════════
"""

    with open('scan_report.txt', 'w') as f:
        f.write(rapport_texte)

    print(f"  Fichier scan_report.txt créé")
    print()

    # Afficher le rapport
    print("[*] Contenu du rapport")
    with open('scan_report.txt', 'r') as f:
        print(f.read())
    print()

    # Nettoyer
    os.remove('scan_results.json')
    os.remove('scan_report.txt')

    print()


# ═════════════════════════════════════════════════════════════════════════════
# ÉTAPE 12 : Gestion d'erreurs avec fichiers
# ═════════════════════════════════════════════════════════════════════════════

def etape12_gestion_erreurs():
    """Démonstration de la gestion d'erreurs avec fichiers."""

    print("═" * 79)
    print("ÉTAPE 12 : Gestion d'erreurs avec fichiers")
    print("═" * 79)
    print()

    # Erreur 1 : Fichier non trouvé
    print("[*] Erreur 1 : Fichier non trouvé")
    try:
        with open('/chemin/inexistant/fichier.txt', 'r') as f:
            contenu = f.read()
    except FileNotFoundError:
        print(f"  ✗ Fichier non trouvé (FileNotFoundError)")
    except Exception as e:
        print(f"  ✗ Erreur : {type(e).__name__}: {e}")
    print()

    # Erreur 2 : Permission refusée (simulation)
    print("[*] Erreur 2 : Permission refusée (exemple)")
    try:
        # Créer un fichier en lecture seule
        f = open('readonly.txt', 'w')
        f.write("test")
        f.close()

        # Rendre le fichier en lecture seule
        os.chmod('readonly.txt', 0o444)

        # Tenter d'écrire
        with open('readonly.txt', 'a') as f:
            f.write("Nouvelle ligne")
    except PermissionError:
        print(f"  ✗ Permission refusée (PermissionError)")
    except Exception as e:
        print(f"  ✗ Erreur : {type(e).__name__}")
    finally:
        # Nettoyer
        os.chmod('readonly.txt', 0o644)
        os.remove('readonly.txt')
    print()

    # Erreur 3 : Mauvais encodage
    print("[*] Erreur 3 : Mauvais encodage")
    try:
        # Créer un fichier binaire
        with open('binary_test.bin', 'wb') as f:
            f.write(b'\x80\x81\x82\x83')

        # Tenter de le lire en UTF-8
        with open('binary_test.bin', 'r', encoding='utf-8') as f:
            contenu = f.read()
    except UnicodeDecodeError:
        print(f"  ✗ Erreur d'encodage (UnicodeDecodeError)")
    except Exception as e:
        print(f"  ✗ Erreur : {type(e).__name__}")
    finally:
        if os.path.exists('binary_test.bin'):
            os.remove('binary_test.bin')
    print()

    # Bonne pratique : Gestion complète
    print("[*] Bonne pratique : Gestion d'erreurs complète")

    def lire_fichier_securise(chemin):
        """Lire un fichier de façon sécurisée."""
        try:
            with open(chemin, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print(f"  ✗ Fichier '{chemin}' non trouvé")
            return None
        except PermissionError:
            print(f"  ✗ Permission refusée pour '{chemin}'")
            return None
        except UnicodeDecodeError:
            print(f"  ✗ Problème d'encodage pour '{chemin}'")
            return None
        except IOError as e:
            print(f"  ✗ Erreur E/S : {e}")
            return None
        except Exception as e:
            print(f"  ✗ Erreur inattendue : {type(e).__name__}: {e}")
            return None

    # Tester
    print(f"  Résultat : {lire_fichier_securise('/inexistant.txt')}")
    print()

    print()


# ═════════════════════════════════════════════════════════════════════════════
# FONCTION PRINCIPALE
# ═════════════════════════════════════════════════════════════════════════════

def main():
    """Fonction principale qui exécute toutes les étapes."""

    print("\n")
    print("█" * 79)
    print("█" + " " * 77 + "█")
    print("█" + "  EXERCICE 11 : GESTION DE FICHIERS EN PYTHON".center(77) + "█")
    print("█" + " " * 77 + "█")
    print("█" * 79)
    print()

    # Exécuter toutes les étapes
    etape1_ouverture_basique()
    etape2_modes_fichiers()
    etape3_lecture_fichiers()
    etape4_ecriture_fichiers()
    etape5_context_manager()
    etape6_json()
    etape7_chemins_os()
    etape8_chemins_pathlib()
    etape9_red_teaming_logs()
    etape10_red_teaming_config()
    etape11_red_teaming_resultats()
    etape12_gestion_erreurs()

    print("█" * 79)
    print("█" + " " * 77 + "█")
    print("█" + "  FIN DE LA DÉMONSTRATION".center(77) + "█")
    print("█" + " " * 77 + "█")
    print("█" * 79)
    print()
    print("[+] Concepts maîtrisés :")
    print("  ✓ Ouverture et fermeture de fichiers")
    print("  ✓ Modes de fichiers (r, w, a, b)")
    print("  ✓ Context manager (with)")
    print("  ✓ Lecture de fichiers (read, readline, readlines)")
    print("  ✓ Écriture de fichiers (write, writelines)")
    print("  ✓ Travail avec JSON (load, dump, loads, dumps)")
    print("  ✓ Gestion des chemins (os.path, pathlib)")
    print("  ✓ Red teaming avec fichiers et JSON")
    print("  ✓ Gestion d'erreurs (FileNotFoundError, PermissionError, etc.)")
    print()


# ═════════════════════════════════════════════════════════════════════════════
# POINT D'ENTRÉE
# ═════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    # Ce code s'exécute SEULEMENT si main.py est lancé directement
    main()
