# Exercice 10: Modules et Imports - Défis

## Défi 1: Explorateur de répertoires

Créez un programme qui :
1. Importe le module os
2. Affiche le répertoire courant
3. Liste les fichiers du répertoire courant
4. Compte le nombre de fichiers et dossiers
5. Affiche le séparateur de chemin du système

Exemple de sortie :
  Répertoire courant : /Users/tudygbaguidi/Desktop
  Nombre de fichiers : 12
  Séparateur : /
  Fichiers : [main.py, README.md, ...]

## Défi 2: Informations système

Créez un programme qui utilise sys pour afficher :
1. La version Python
2. La plateforme (Windows/Linux/Mac)
3. Les arguments en ligne de commande
4. L'encodage par défaut
5. Le chemin de l'exécutable Python

Utilisez from...import pour importer uniquement ce dont vous avez besoin.

Exemple de sortie :
  Version Python : 3.10.5
  Plateforme : darwin
  Encodage : utf-8
  Exécutable : /usr/bin/python3

## Défi 3: Gestionnaire de temps (Mesure de performance)

Créez un programme qui :
1. Importe time
2. Mesure le temps qu'une opération prend
3. Affiche le temps en secondes avec 4 décimales
4. Affiche le timestamp Unix actuel
5. Affiche l'heure locale formatée (HH:MM:SS)

Opération à mesurer :
  - Créer une liste de 10 millions de nombres et les additionner

Exemple de sortie :
  Opération prise : 1.2345 secondes
  Timestamp Unix : 1699347600
  Heure locale : 14:30:45

## Défi 4: Calculatrice de dates

Créez un programme qui utilise datetime pour :
1. Afficher la date/heure actuelle
2. Calculer le nombre de jours jusqu'à Noël (25 décembre)
3. Afficher une date personnalisée formatée (JJ/MM/AAAA HH:MM:SS)
4. Convertir un timestamp Unix en date lisible
5. Calculer la différence de temps entre deux dates

Étapes :
1. Créer une date spécifique (ex: 2025-06-15)
2. Calculer les jours, heures, minutes jusqu'à celle-ci
3. Afficher le résultat

Exemple de sortie :
  Aujourd'hui : 2024-11-07 14:30:45
  Jours jusqu'à Noël : 48
  Différence personnalisée : 220 jours, 4 heures, 30 minutes

## Défi 5: Générateur de mots de passe aléatoires

Créez un programme qui utilise random pour :
1. Générer un mot de passe de 12 caractères aléatoires
2. Générer 5 tokens de session (32 caractères hexadécimaux)
3. Mélanger une liste de mots
4. Sélectionner aléatoirement 3 mots d'une liste
5. Générer un numéro d'attaque entre 1 et 1000

Utiliser :
  - string.ascii_letters
  - string.digits
  - string.punctuation
  - random.choice()
  - random.shuffle()
  - random.sample()

Exemple de sortie :
  Mot de passe : aB3!xPqR#mNp
  Tokens : [abc123def456..., ...]
  Mots mélangés : [word3, word1, word2, ...]
  Sélection : [python, security, network]
  Numéro : 742

## Défi 6: Calculateur de hashes de sécurité

Créez un programme qui utilise hashlib pour :
1. Demander un mot de passe à l'utilisateur
2. Calculer MD5, SHA1, SHA256 et SHA512
3. Afficher tous les hashes avec leur longueur
4. Comparer si deux entrées produisent le même hash
5. Afficher les premiers 16 caractères de chaque hash

Exemple de sortie :
  Mot de passe : password123
  MD5 (32 char) : 482c811da5d5b4b...
  SHA1 (40 char) : 482c811da5d5b4b...
  SHA256 (64 char) : 482c811da5d5b4b...
  SHA512 (128 char) : 482c811da5d5b4b...

  Vérification intégrité : SHA256(password123) == SHA256(password123) = True

## Défi 7: Créer un module personnalisé (security_utils.py)

Créez un fichier security_utils.py qui contient :
1. Une fonction verifier_mot_de_passe(mdp) qui retourne "Faible/Moyen/Fort"
2. Une fonction generer_token(longueur=32) qui retourne un token aléatoire
3. Une fonction hacher_mdp(mdp, algo="sha256") qui retourne le hash
4. Une fonction verifier_hash(texte, hash_expected, algo="sha256") qui retourne True/False
5. Ajouter __name__ == "__main__" pour tester les fonctions

Puis créez main.py qui :
1. Importe le module avec "import security_utils"
2. Teste chaque fonction
3. Affiche les résultats

Exemple de sortie :
  Force de 'abc' : Faible
  Force de 'MySecurePass123!' : Fort
  Token généré : a1b2c3d4e5f6...
  Hash : 482c811da5d5b4b...
  Vérification : True

## Défi 8: Red Teaming - Scanner de système complet

Créez un programme complet de red teaming qui utilise TOUS les modules pour :

1. ÉNUMÉRATION (os/sys)
   - Répertoire courant
   - Utilisateur actuel
   - Plateforme
   - Variables d'environnement clés

2. TIMING (time)
   - Mesurer le temps d'exécution d'une brute force simulée
   - Afficher le timestamp de l'attaque

3. TIMESTAMPS (datetime)
   - Afficher la date/heure d'attaque formatée
   - Calculer la durée depuis le dernier boot (simulation)

4. PAYLOADS ALÉATOIRES (random)
   - Générer des tokens de session
   - Générer des User-Agents aléatoires
   - Générer des payloads SQL injection variables

5. HACHAGE (hashlib)
   - Hash de chaque payload généré (SHA256)
   - Vérification d'intégrité des réponses

6. GÉNÉRATION CRYPTOGRAPHIQUE (os.urandom)
   - Générer des nonces

7. ARGUMENTS (sys.argv)
   - Accepter un target en argument
   - Accepter un nombre de tentatives en argument

Structure du programme :
  usage: python scanner.py <target> <attempts>

  Exemple:
  python scanner.py 192.168.1.1 10

Sortie attendue :
  ═══════════════════════════════════════════════════
  RED TEAMING SCANNER
  ═══════════════════════════════════════════════════

  [*] Énumération système
  Plateforme : darwin
  Utilisateur : tudygbaguidi
  Répertoire : /Users/tudygbaguidi

  [*] Timing d'attaque
  Début : 2024-11-07 14:30:45
  Durée préalable : 2.3456 secondes

  [*] Payloads générés
  Payload 1 : a1b2c3d4e5f6...
  Hash SHA256 : 482c811da5d5b4b...

  [*] Tentatives : 10
  [+] Attaque complétée avec succès
  ═══════════════════════════════════════════════════

## Conseils DE RÉSOLUTION

1. Lisez les sections concernées dans main.py
2. Testez chaque défi indépendamment
3. Utilisez print() pour déboguer
4. Consultez la documentation officielle si besoin
5. Pour le défi 7, créez un vrai fichier .py
6. Pour le défi 8, combinez tous les concepts

