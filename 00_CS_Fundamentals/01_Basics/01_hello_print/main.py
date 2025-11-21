"""
═══════════════════════════════════════════════════════════════
EXERCICE 01 : Hello Print
═══════════════════════════════════════════════════════════════

OBJECTIF :
- Apprendre à utiliser la fonction print()
- Comprendre les commentaires
- Pratiquer l'indentation
- Exécuter votre premier programme Python

EXÉCUTION : python main.py

═══════════════════════════════════════════════════════════════
"""

def main():
    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 1 : Premier print basique
    # ═══════════════════════════════════════════════════════════

    print("=== Étape 1 : Premier print ===")

    # La fonction print() affiche du texte dans le terminal
    # Le texte doit être entre guillemets (simples ' ou doubles ")
    print("Hello, World!")

    # Vous pouvez utiliser des guillemets simples ou doubles
    print('Bonjour Python!')

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 2 : Print avec plusieurs lignes
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 2 : Plusieurs lignes ===")

    # Chaque print() crée une nouvelle ligne automatiquement
    print("Ligne 1")
    print("Ligne 2")
    print("Ligne 3")

    # Pour afficher une ligne vide, utilisez print() sans argument
    print()
    print("Une ligne vide au-dessus")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 3 : Caractères spéciaux
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 3 : Caractères spéciaux ===")

    # \n = nouvelle ligne (newline)
    print("Première ligne\nDeuxième ligne")

    # \t = tabulation
    print("Colonne 1\tColonne 2\tColonne 3")

    # \\ = backslash littéral
    print("Chemin Windows : C:\\Users\\Python")

    # \' et \" = guillemets littéraux
    print("Il a dit : \"Python est génial!\"")
    print('L\'apostrophe fonctionne aussi')

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 4 : Print avec plusieurs arguments
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 4 : Plusieurs arguments ===")

    # print() peut prendre plusieurs arguments séparés par des virgules
    # Par défaut, ils sont séparés par un espace
    print("Python", "est", "fantastique")

    # Vous pouvez changer le séparateur avec le paramètre sep
    print("Python", "est", "fantastique", sep="-")
    print("Python", "est", "fantastique", sep=" | ")

    # Vous pouvez changer la fin de ligne avec le paramètre end
    print("Cette ligne ", end="")
    print("continue ici")  # Pas de retour à la ligne entre les deux

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 5 : Commentaires
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 5 : Commentaires ===")

    # Ceci est un commentaire sur une ligne
    # Les commentaires ne sont pas exécutés
    # Ils servent à expliquer le code

    print("Ce code s'exécute")  # Commentaire en fin de ligne

    # print("Ce code ne s'exécute pas car il est commenté")

    """
    Ceci est un commentaire sur plusieurs lignes
    (techniquement c'est une chaîne de caractères non assignée)

    Utilisé pour :
    - Documentation de fonctions
    - Commentaires longs
    - Désactiver temporairement du code
    """

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 6 : Créer des affichages formatés
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 6 : Affichages formatés ===")

    # Créer des séparateurs visuels
    print("=" * 50)
    print("Titre Important")
    print("=" * 50)

    # Créer des boîtes
    print("╔" + "═" * 48 + "╗")
    print("║" + " " * 15 + "BIENVENUE" + " " * 24 + "║")
    print("╚" + "═" * 48 + "╝")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 7 : Exemple pratique - Banner d'application
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 7 : Exemple pratique ===")

    # Créons un banner pour une application de hacking éthique
    print()
    print("═" * 60)
    print("║" + " " * 58 + "║")
    print("║" + " " * 15 + "PYTHON RED TEAM TOOLKIT" + " " * 20 + "║")
    print("║" + " " * 58 + "║")
    print("║" + " " * 10 + "Apprentissage de Python pour le Red Teaming" + " " * 5 + "║")
    print("║" + " " * 58 + "║")
    print("═" * 60)
    print()
    print("[*] Initialisation du programme...")
    print("[+] Python version : OK")
    print("[+] Modules chargés : OK")
    print("[!] Mode éthique activé")
    print()
    print("═" * 60)


# ═══════════════════════════════════════════════════════════════
# Point d'entrée du programme
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    # Cette condition vérifie si le script est exécuté directement
    # (et non importé comme module)
    # C'est une bonne pratique en Python

    main()  # Appel de la fonction principale
