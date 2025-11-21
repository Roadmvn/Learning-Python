"""
═══════════════════════════════════════════════════════════════
EXERCICE 04 : Opérateurs
═══════════════════════════════════════════════════════════════

OBJECTIF :
- Maîtriser les opérateurs arithmétiques (+, -, *, /, //, %, **)
- Comprendre les opérateurs de comparaison (==, !=, <, >, <=, >=)
- Utiliser les opérateurs logiques (and, or, not)
- Créer des expressions complexes

EXÉCUTION : python main.py

═══════════════════════════════════════════════════════════════
"""

def main():
    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 1 : Opérateurs arithmétiques basiques
    # ═══════════════════════════════════════════════════════════

    print("=== Étape 1 : Opérateurs arithmétiques basiques ===\n")

    a = 10
    b = 3

    # Addition
    addition = a + b
    print(f"{a} + {b} = {addition}")

    # Soustraction
    soustraction = a - b
    print(f"{a} - {b} = {soustraction}")

    # Multiplication
    multiplication = a * b
    print(f"{a} * {b} = {multiplication}")

    # Division (résultat float)
    division = a / b
    print(f"{a} / {b} = {division:.2f}")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 2 : Opérateurs arithmétiques avancés
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 2 : Opérateurs avancés ===\n")

    # Division entière (floor division)
    # Résultat entier, arrondi vers le bas
    division_entiere = a // b
    print(f"{a} // {b} = {division_entiere}")
    print(f"Type : {type(division_entiere)}")  # int

    # Modulo (reste de la division)
    # Très utile pour vérifier si un nombre est pair/impair
    modulo = a % b
    print(f"\n{a} % {b} = {modulo}")
    print("Le reste de 10 ÷ 3 est 1 (car 3×3=9, reste 1)")

    # Vérifier si un nombre est pair
    nombre = 42
    est_pair = (nombre % 2 == 0)
    print(f"\n{nombre} est pair : {est_pair}")

    nombre = 43
    est_pair = (nombre % 2 == 0)
    print(f"{nombre} est pair : {est_pair}")

    # Puissance
    puissance = a ** b
    print(f"\n{a} ** {b} = {puissance}")
    print(f"(10 puissance 3 = 10×10×10 = {puissance})")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 3 : Opérateurs de comparaison
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 3 : Opérateurs de comparaison ===\n")

    # Les opérateurs de comparaison retournent un booléen (True/False)

    x = 10
    y = 5

    # Égal à
    print(f"{x} == {y} : {x == y}")  # False

    # Différent de
    print(f"{x} != {y} : {x != y}")  # True

    # Inférieur à
    print(f"{x} < {y} : {x < y}")    # False

    # Supérieur à
    print(f"{x} > {y} : {x > y}")    # True

    # Inférieur ou égal à
    print(f"{x} <= {y} : {x <= y}")  # False

    # Supérieur ou égal à
    print(f"{x} >= {y} : {x >= y}")  # True

    # Comparaison de chaînes
    print(f"\n'admin' == 'admin' : {'admin' == 'admin'}")  # True
    print(f"'Admin' == 'admin' : {'Admin' == 'admin'}")    # False (sensible à la casse)

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 4 : Opérateurs logiques (and, or, not)
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 4 : Opérateurs logiques ===\n")

    # AND (et) - True si les DEUX conditions sont vraies
    print("Opérateur AND :")
    print(f"True and True = {True and True}")      # True
    print(f"True and False = {True and False}")    # False
    print(f"False and False = {False and False}")  # False

    # OR (ou) - True si AU MOINS UNE condition est vraie
    print("\nOpérateur OR :")
    print(f"True or True = {True or True}")        # True
    print(f"True or False = {True or False}")      # True
    print(f"False or False = {False or False}")    # False

    # NOT (non) - Inverse la valeur
    print("\nOpérateur NOT :")
    print(f"not True = {not True}")    # False
    print(f"not False = {not False}")  # True

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 5 : Combinaison d'opérateurs
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 5 : Combinaison d'opérateurs ===\n")

    age = 25
    a_permis = True

    # Peut conduire si age >= 18 ET a un permis
    peut_conduire = (age >= 18) and a_permis
    print(f"Âge : {age}, Permis : {a_permis}")
    print(f"Peut conduire : {peut_conduire}")

    # Accès autorisé si admin OU root
    username = "admin"
    acces_autorise = (username == "admin") or (username == "root")
    print(f"\nUsername : {username}")
    print(f"Accès autorisé : {acces_autorise}")

    # Port non standard (pas 80, 443, ou 22)
    port = 8080
    port_non_standard = not (port == 80 or port == 443 or port == 22)
    print(f"\nPort : {port}")
    print(f"Port non standard : {port_non_standard}")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 6 : Priorité des opérateurs
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 6 : Priorité des opérateurs ===\n")

    # L'ordre d'évaluation des opérateurs :
    # 1. ()       Parenthèses
    # 2. **       Puissance
    # 3. *, /, //, %  Multiplication, Division
    # 4. +, -     Addition, Soustraction
    # 5. ==, !=, <, >, <=, >=  Comparaison
    # 6. not      NON logique
    # 7. and      ET logique
    # 8. or       OU logique

    resultat = 2 + 3 * 4
    print(f"2 + 3 * 4 = {resultat}")  # 14, pas 20 !
    print("(multiplication avant addition)")

    resultat = (2 + 3) * 4
    print(f"(2 + 3) * 4 = {resultat}")  # 20
    print("(parenthèses en premier)")

    # Exemple avec puissance
    resultat = 2 ** 3 ** 2
    print(f"\n2 ** 3 ** 2 = {resultat}")  # 512 (pas 64 !)
    print("(évalué de droite à gauche : 2 ** (3 ** 2) = 2 ** 9)")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 7 : Opérateurs d'assignation composés
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 7 : Opérateurs d'assignation composés ===\n")

    # Raccourcis pour modifier une variable
    compteur = 10
    print(f"Compteur initial : {compteur}")

    compteur += 5  # Équivalent à : compteur = compteur + 5
    print(f"Après += 5 : {compteur}")

    compteur -= 3  # Équivalent à : compteur = compteur - 3
    print(f"Après -= 3 : {compteur}")

    compteur *= 2  # Équivalent à : compteur = compteur * 2
    print(f"Après *= 2 : {compteur}")

    compteur //= 4  # Équivalent à : compteur = compteur // 4
    print(f"Après //= 4 : {compteur}")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 8 : Exemple pratique - Vérification de port
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 8 : Exemple pratique ===\n")

    # Vérification si un port est dans une plage valide
    port = 8080

    # Un port est valide s'il est entre 1 et 65535
    port_valide = (port >= 1) and (port <= 65535)

    # Un port est privilégié s'il est < 1024
    port_privilegie = port < 1024

    # Un port est bien connu s'il est dans cette liste
    ports_bien_connus = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306]
    est_bien_connu = port in ports_bien_connus

    print(f"Port : {port}")
    print(f"Valide : {port_valide}")
    print(f"Privilégié (< 1024) : {port_privilegie}")
    print(f"Bien connu : {est_bien_connu}")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 9 : Exemple pratique - Calculateur de sous-réseau
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 9 : Calculs réseau ===\n")

    # Calcul du nombre d'hôtes dans un sous-réseau
    # Formule : 2^(32 - masque) - 2

    masque = 24
    nombre_hotes = (2 ** (32 - masque)) - 2

    print(f"Masque : /{masque}")
    print(f"Nombre d'hôtes disponibles : {nombre_hotes}")

    # Calcul pour différents masques
    print("\nNombre d'hôtes par masque :")
    for m in [8, 16, 24, 26, 28, 30]:
        hotes = (2 ** (32 - m)) - 2
        print(f"/{m:2d} : {hotes:>10} hôtes")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 10 : Exemple pratique - Temps de bruteforce
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 10 : Calcul temps de bruteforce ===\n")

    # Estimation du temps pour bruteforce un mot de passe
    longueur_mdp = 8
    taille_alphabet = 62  # a-z, A-Z, 0-9
    tentatives_par_seconde = 1000000  # 1 million

    # Nombre de combinaisons possibles
    combinaisons = taille_alphabet ** longueur_mdp

    # Temps en secondes (dans le pire cas)
    temps_secondes = combinaisons / tentatives_par_seconde

    # Conversions
    temps_minutes = temps_secondes / 60
    temps_heures = temps_minutes / 60
    temps_jours = temps_heures / 24
    temps_annees = temps_jours / 365

    print(f"Longueur du mot de passe : {longueur_mdp}")
    print(f"Taille de l'alphabet : {taille_alphabet}")
    print(f"Tentatives par seconde : {tentatives_par_seconde:,}")
    print(f"\nCombinaisons possibles : {combinaisons:,}")
    print(f"\nTemps de bruteforce (pire cas) :")
    print(f"  {temps_secondes:,.0f} secondes")
    print(f"  {temps_minutes:,.0f} minutes")
    print(f"  {temps_heures:,.0f} heures")
    print(f"  {temps_jours:,.0f} jours")
    print(f"  {temps_annees:,.0f} années")


# ═══════════════════════════════════════════════════════════════
# Point d'entrée
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("\n" + "═" * 60)
    print("EXERCICE 04 : OPÉRATEURS")
    print("═" * 60 + "\n")

    main()

    print("\n" + "═" * 60)
    print("FIN DE L'EXERCICE")
    print("═" * 60 + "\n")
