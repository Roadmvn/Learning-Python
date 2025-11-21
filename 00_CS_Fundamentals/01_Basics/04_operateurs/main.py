"""
═══════════════════════════════════════════════════════════════
EXERCICE 04 : Opérateurs
═══════════════════════════════════════════════════════════════

OBJECTIF :
- Maîtriser les opérateurs arithmétiques (+, -, *, /, //, %, **)
- Comprendre les opérateurs de comparaison (==, !=, <, >, <=, >=)
- Utiliser les opérateurs logiques (and, or, not)
- Créer des expressions complexes

INSTRUCTIONS :
1. Lisez attentivement le fichier Cours.md (950 lignes de théorie)
2. Consultez example.py pour voir des exemples guidés
3. Complétez ce fichier en suivant les TODO
4. Testez votre code avec : python main.py
5. Vérifiez vos solutions avec solution.py si besoin

EXÉCUTION : python main.py

═══════════════════════════════════════════════════════════════
"""

def main():
    print("="*60)
    print("EXERCICE 04 : Opérateurs en Python")
    print("="*60)
    
    # ═══════════════════════════════════════════════════════════
    # PARTIE 1 : Opérateurs arithmétiques basiques
    # ═══════════════════════════════════════════════════════════
    
    print("\n=== PARTIE 1 : Arithmétiques Basiques ===\n")
    
    # TODO 1.1 : Créez deux variables a et b avec les valeurs 15 et 4
    # a = ?
    # b = ?
    
    # TODO 1.2 : Calculez et affichez l'addition de a et b
    # Format : "15 + 4 = 19"
    
    # TODO 1.3 : Calculez et affichez la soustraction
    
    # TODO 1.4 : Calculez et affichez la multiplication
    
    # TODO 1.5 : Calculez et affichez la division (avec 2 décimales)
    # Utilisez : print(f"{a} / {b} = {resultat:.2f}")
    
    
    # ═══════════════════════════════════════════════════════════
    # PARTIE 2 : Opérateurs arithmétiques avancés
    # ═══════════════════════════════════════════════════════════
    
    print("\n=== PARTIE 2 : Arithmétiques Avancés ===\n")
    
    # TODO 2.1 : Division entière de a par b
    # Utilisez l'opérateur //
    
    # TODO 2.2 : Modulo de a par b (reste de la division)
    # Utilisez l'opérateur %
    
    # TODO 2.3 : a à la puissance b
    # Utilisez l'opérateur **
    
    # TODO 2.4 : Calculez 2^10 (utile pour calculs réseau)
    # Affichez : "2^10 = 1024"
    
    
    # ═══════════════════════════════════════════════════════════
    # PARTIE 3 : Opérateurs de comparaison
    # ═══════════════════════════════════════════════════════════
    
    print("\n=== PARTIE 3 : Comparaisons ===\n")
    
    # TODO 3.1 : Comparez si a est égal à b
    # Affichez : "15 == 4 : False"
    
    # TODO 3.2 : Comparez si a est différent de b
    
    # TODO 3.3 : Comparez si a est supérieur à b
    
    # TODO 3.4 : Comparez si a est inférieur ou égal à 20
    # Utilisez : a <= 20
    
    # TODO 3.5 : Comparaison chaînée
    # Vérifiez si 0 < a < 20
    # Affichez le résultat
    
    
    # ═══════════════════════════════════════════════════════════
    # PARTIE 4 : Opérateurs logiques
    # ═══════════════════════════════════════════════════════════
    
    print("\n=== PARTIE 4 : Logique ===\n")
    
    # TODO 4.1 : Vérifiez si a > 10 ET b < 10
    # Utilisez l'opérateur and
    
    # TODO 4.2 : Vérifiez si a == 15 OU b == 10
    # Utilisez l'opérateur or
    
    # TODO 4.3 : Inversez le résultat de (a > b)
    # Utilisez l'opérateur not
    
    
    # ═══════════════════════════════════════════════════════════
    # DÉFI 1 : Vérificateur de nombre pair/impair
    # ═══════════════════════════════════════════════════════════
    
    print("\n=== DÉFI 1 : Pair ou Impair ? ===\n")
    
    # TODO : Créez une variable 'nombre' avec la valeur 42
    # TODO : Utilisez le modulo (%) pour vérifier s'il est pair
    # TODO : Affichez "42 est pair" ou "42 est impair"
    # HINT : Un nombre est pair si nombre % 2 == 0
    
    
    # ═══════════════════════════════════════════════════════════
    # DÉFI 2 : Validateur de port réseau
    # ═══════════════════════════════════════════════════════════
    
    print("\n=== DÉFI 2 : Validateur de Port ===\n")
    
    # TODO : Créez une variable 'port' avec la valeur 8080
    # TODO : Vérifiez si le port est valide (1 <= port <= 65535)
    # TODO : Vérifiez s'il est privilégié (< 1024)
    # TODO : Affichez les résultats
    # Format attendu :
    #   Port 8080 : Valide
    #   Port privilégié : Non
    
    
    # ═══════════════════════════════════════════════════════════
    # DÉFI 3 : Calculateur de sous-réseau simple
    # ═══════════════════════════════════════════════════════════
    
    print("\n=== DÉFI 3 : Calcul Sous-Réseau ===\n")
    
    # TODO : Calculez le nombre d'hôtes disponibles pour un /24
    # Formule : 2^(32 - masque) - 2
    # masque = 24
    # TODO : Affichez "Hôtes disponibles en /24 : 254"
    
    # TODO : Faites la même chose pour un /16
    
    
    # ═══════════════════════════════════════════════════════════
    # DÉFI 4 : Vérificateur de mot de passe (simplifié)
    # ═══════════════════════════════════════════════════════════
    
    print("\n=== DÉFI 4 : Vérification Mot de Passe ===\n")
    
    # TODO : Créez deux variables :
    #   correct_password = "Admin123"
    #   user_password = "Admin123"
    
    # TODO : Vérifiez si le mot de passe est correct
    # TODO : Vérifiez aussi que la longueur est >= 8 caractères
    # TODO : Utilisez AND pour combiner les deux conditions
    # TODO : Affichez "✅ Accès autorisé" ou "❌ Accès refusé"
    
    
    # ═══════════════════════════════════════════════════════════
    # DÉFI 5 : Manipulation de bits (avancé)
    # ═══════════════════════════════════════════════════════════
    
    print("\n=== DÉFI 5 : Opérations Binaires ===\n")
    
    # TODO : Créez une variable permissions = 0o755 (rwxr-xr-x)
    # TODO : Extrayez les permissions utilisateur avec >> et &
    # HINT : user_perms = (permissions >> 6) & 0b111
    # TODO : Affichez en binaire : "User perms: 111 (rwx)"
    
    
    print("\n" + "="*60)
    print("FIN DE L'EXERCICE")
    print("="*60)
    print("\n💡 AIDE :")
    print("  - Consultez Cours.md pour la théorie complète")
    print("  - Regardez example.py pour des exemples guidés")
    print("  - Vérifiez solution.py pour les réponses")
    print("\n🎯 PROCHAINE ÉTAPE :")
    print("  - Exercice 05 : Structures Conditionnelles (if/else)")


if __name__ == "__main__":
    main()
