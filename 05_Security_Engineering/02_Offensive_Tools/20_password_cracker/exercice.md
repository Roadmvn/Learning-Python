========================================
# Exercice 20: PASSWORD CRACKER EN PYTHON
Défis progressifs avec focus cybersécurité
========================================

AVERTISSEMENT LÉGAL ET ÉTHIQUE:
Ces exercices sont destinés à l'apprentissage dans un environnement contrôlé.
L'utilisation sur des systèmes sans autorisation explicite est ILLÉGALE.

Utilisez UNIQUEMENT sur:
- Vos propres mots de passe oubliés
- Des machines virtuelles de test
- Des environnements autorisés par écrit
- Des systèmes pour lesquels vous avez une autorisation écrite

Violation = Responsabilité légale et poursuites criminelles.

========================================
## Défi 1: Cracker de Base - Hash Simple
========================================

Objectif : Implémenter un cracker basique utilisant dictionary attack

Créez un script qui :
1. Définit une fonction `create_test_hash(password, hash_type="sha256")`
   - Prend un mot de passe en entrée
   - Retourne le hash du mot de passe
   - Support MD5, SHA1, SHA256, SHA512

2. Définit une fonction `simple_dictionary_attack(target_hash, hash_type="sha256")`
   - Prend un hash cible en entrée
   - Utilise une liste simple de mots courants
   - Teste chaque mot jusqu'à trouver une correspondance
   - Retourne (mot_de_passe, nombre_tentatives, temps_secondes)

3. Test le cracker:
   - Créer un hash à partir du mot de passe "password123"
   - Cracker le hash
   - Afficher les résultats

Contraintes:
- Utiliser hashlib pour le hashing
- Utiliser une liste simple (min 50 mots)
- Gérer les types de hash différents
- Mesurer le temps d'exécution
- Afficher la progression tous les 10 tests

Indications:
- hashlib.sha256(password.encode()).hexdigest()
- Boucle simple for word in wordlist
- time.time() pour mesurer
- Comparaison simple de strings

Exemple de sortie attendue:
=====================================
Hash cible: 482c811da5d5b4bc6d497ffa98491e38...
Type: SHA256
Wordlist taille: 50 mots

Progression:
  10 testés - 0.012s
  20 testés - 0.023s
  30 testés - 0.035s

MOT DE PASSE TROUVÉ: password123
Tentatives: 42 / 50
Temps total: 0.052 secondes
Vitesse moyenne: 808 mots de passe/seconde
=====================================

Bonus:
- Ajouter des statistiques (tentatives, vitesse)
- Tester avec 3 types de hash différents
- Comparer les vitesses de cracking

========================================
## Défi 2: Brute Force Exhaustive
========================================

Objectif : Implémenter une attaque brute force pure

Créez un script qui :
1. Définit une fonction `brute_force_generator(min_len=1, max_len=3, charset=None)`
   - Génère tous les mots de passe possibles
   - Support personnalisation charset (a-z, 0-9, majuscules, etc.)
   - Retourne un générateur (pas une liste) pour économiser la mémoire

2. Définit une fonction `brute_force_crack(target_hash, charset, max_length=4)`
   - Utilise le générateur de brute force
   - Teste les mots de passe générés
   - Retourne (mot_de_passe, tentatives, temps)

3. Teste le cracker:
   - Créer un hash à partir d'un mot de passe court (3-4 caractères)
   - Lancer une attaque brute force
   - Mesurer le nombre de tentatives

Contraintes:
- JAMAIS stocker toute la liste en mémoire (utiliser un générateur)
- Utiliser itertools.product() pour les combinaisons
- Support multiple charsets (minuscules, majuscules, chiffres)
- Afficher le nombre de combinaisons possibles
- Montrer l'explosion exponentielle de la complexité

Indications:
- itertools.product(charset, repeat=length)
- yield pour créer un générateur
- Montrer: longueur 3 = 36^3, longueur 4 = 36^4
- Les charsets: string.ascii_lowercase, string.digits, etc.

Exemple de sortie attendue:
=====================================
BRUTE FORCE ATTACK
Hash cible: abc1234567890...
Charset: a-z, 0-9 (36 caractères)

Complexité:
- Longueur 1: 36 combinaisons
- Longueur 2: 1,296 combinaisons
- Longueur 3: 46,656 combinaisons
- Longueur 4: 1,679,616 combinaisons

Attaque:
- Testant longueur 1...
- Testant longueur 2...
- Testant longueur 3...
- MOT DE PASSE TROUVÉ: abc1

Statistiques:
- Tentatives totales: 47,952
- Temps: 0.876 secondes
- Vitesse: 54,759 mots de passe/seconde
=====================================

Bonus:
- Comparer avec dictionary attack (beaucoup plus rapide)
- Montrer pourquoi brute force est limité à mots courts
- Calculer le temps estimé pour longueur 8 (des millions de secondes!)

========================================
## Défi 3: Attaque Hybride (Dictionary + Variations)
========================================

Objectif : Combiner dictionary attack avec variations de mots

Créez un script qui :
1. Définit une fonction `generate_word_variations(word)`
   - Prend un mot de base
   - Retourne toutes les variations:
```python
     * Minuscules: password
     * Capitalisé: Password
     * MAJUSCULES: PASSWORD
     * Minuscules + chiffres: password123
     * Minuscules + symboles: password!
     * Variante l33t: p4ssw0rd
```
   - Résultat: 1 mot → 10-15 variations

2. Définit une fonction `generate_hybrid_wordlist(base_words)`
   - Prend une liste de mots de base
   - Génère les variations pour chaque
   - Retourne une wordlist complète et organisée

3. Définit une fonction `hybrid_attack(target_hash, base_words, hash_type="sha256")`
   - Utilise la wordlist hybride
   - Teste chaque variation
   - Affiche la progression (mot actuel et ses variations)
   - Retourne (mot_de_passe, tentatives, temps)

4. Teste le cracker:
   - Créer un hash à partir de "Password123!"
   - Attaquer avec la wordlist hybride
   - Comparer avec dictionary seul

Contraintes:
- Générer MIN 8 variations par mot
- La wordlist finale doit avoir 5x+ mots que la liste de base
- Afficher les variations générées pour le mot trouvé
- Comparer vitesse: dictionary vs hybrid

Indications:
- Boucles imbriquées pour les variations
- Listes de chaînes pour les modifications (123, 2024, !, @, etc.)
- set() pour supprimer les doublons
- Métriques: tentatives, temps, vitesse

Exemple de sortie attendue:
=====================================
HYBRID ATTACK (Dictionary + Variations)

Mots de base: 20 mots
Variations par mot: 8 en moyenne
Wordlist finale: 178 mots

Hash cible: 7c6a180b36898...

Testant variations de 'password':
  password
  Password
  PASSWORD
  password123
  password2024
  password!
  Password123
  p4ssw0rd

MOT DE PASSE TROUVÉ: Password123

Statistiques:
- Tentatives: 87 / 178
- Temps: 0.108 secondes
- Vitesse: 806 mots de passe/seconde

Comparaison avec Dictionary seul:
- Dictionary: 50 tentatives (not found)
- Hybrid: 87 tentatives (FOUND!)
- Succès: La variante était cruciale!
=====================================

Bonus:
- Ajouter des variations de dates (2023, 2024, 2025)
- Ajouter des patterns courants (1234, 1111, 2020)
- Comparer avec rockyou.txt (simulation avec 1000 mots)

========================================
## Défi 4: Hash Cracking Multi-Type
========================================

Objectif : Cracker des hashs de différents types simultanément

Créez un script qui :
1. Définit une fonction `detect_hash_type(hash_string)`
   - Détermine le type de hash basé sur la longueur
   - MD5: 32 caractères
   - SHA1: 40 caractères
   - SHA256: 64 caractères
   - SHA512: 128 caractères
   - Retourne le type détecté ou "unknown"

2. Définit une fonction `crack_multiple_hashes(hashes_list, wordlist)`
   - Prend une liste de hashs
   - Pour chaque hash:
```python
     * Détecte le type
     * Lance une attaque appropriée
     * Retourne les résultats
```
   - Affiche un résumé des résultats

3. Teste avec 5 hashs:
   - 1 hash MD5
   - 1 hash SHA1
   - 2 hashes SHA256 (1 trouvé, 1 non trouvé)
   - 1 hash SHA512

Contraintes:
- Utiliser hashlib pour tous les types
- Afficher le type de hash détecté
- Mesurer le temps par type
- Afficher un résumé final (success rate)
- Gérer les hashs invalides

Indications:
- Longueur == fait (MD5 = 32, etc.)
- Boucle sur les hashs
- Dictionary attack pour chaque
- format() ou f-strings pour l'affichage

Exemple de sortie attendue:
=====================================
MULTI-TYPE HASH CRACKING

Total hashs: 5
Wordlist taille: 100 mots

Hash #1: abc4def...
  Type détecté: SHA256
  Cracking...
  SUCCÈS: password123

Hash #2: 5d41402...
  Type détecté: MD5
  Cracking...
  SUCCÈS: hello

Hash #3: aaf4c61...
  Type détecté: SHA1
  Cracking...
  ÉCHOUÉ

Hash #4: e3b0c44...
  Type détecté: SHA256
  Cracking...
  SUCCÈS: test123

Hash #5: cf83e13...
  Type détecté: SHA512
  Cracking...
  SUCCÈS: admin

RÉSUMÉ:
- Total crackés: 4 / 5
- Taux de succès: 80%
- Temps total: 0.523 secondes
=====================================

Bonus:
- Créer une liste de hashs depuis un fichier
- Exporter les résultats en CSV
- Paralléliser les crackings (multi-threading)

========================================
## Défi 5: Multi-Threading pour Performance
========================================

Objectif : Utiliser le multi-threading pour accélérer le cracking

Créez un script qui :
1. Créez une classe `ThreadedCracker`:
   - Initialiser avec: hash cible, nombre de threads, wordlist
   - Diviser la wordlist en portions égales
   - Chaque thread teste sa portion

2. Implémentez la méthode `crack()`:
   - Créer N threads workers
   - Chaque worker teste sa portion de wordlist
   - Partager un signal de "trouvé" entre threads
   - Retourner (mot_de_passe, tentatives_totales, temps, speedup)

3. Testez les performances:
   - Benchmark avec 1, 2, 4, et 8 threads
   - Utiliser une wordlist de 10,000+ mots
   - Calculer le speedup (temps_mono / temps_multi)
   - Afficher les résultats comparatifs

Contraintes:
- Utiliser threading.Thread()
- Utiliser threading.Lock() pour synchronisation
- Utiliser threading.Event() pour arrêter les autres threads
- Gérer les race conditions
- Afficher l'assignment de travail par thread

Indications:
- threading.Thread(target=worker_function)
- Lock pour protéger les variables partagées
- Event pour signaler l'arrêt
- Diviser: words_per_thread = len(wordlist) // num_threads

Exemple de sortie attendue:
=====================================
MULTI-THREADED PASSWORD CRACKING

Hash cible: 5baa61e4...
Wordlist: 10,000 mots
Hash type: SHA256

Benchmark:
Threads │ Temps    │ Tentatives │ Speedup
─────────┼──────────┼────────────┼────────
1       │ 2.345s   │ 5,231      │ 1.0x
2       │ 1.234s   │ 5,231      │ 1.9x
4       │ 0.632s   │ 5,231      │ 3.7x
8       │ 0.398s   │ 5,231      │ 5.9x

Thread #0: Testant mots 0-1,250
Thread #1: Testant mots 1,250-2,500
Thread #2: Testant mots 2,500-3,750
Thread #3: Testant mots 3,750-5,000

MOT DE PASSE TROUVÉ PAR THREAD #2: testpassword

Performance:
- Meilleur config: 8 threads (5.9x speedup)
- Limitation: Décrochage au-delà de 8 (limite d'I/O)
=====================================

Bonus:
- Implémenter avec multiprocessing.Pool() aussi
- Comparer threading vs multiprocessing
- Afficher l'utilisation CPU par config

========================================
## Défi 6: Rate Limiting Éthique
========================================

Objectif : Implémenter un rate limiting réaliste avec lockout

Créez un script qui :
1. Créez une classe `RateLimitedAuthenticator`:
   - Propriétés:
```python
     * max_attempts: 3
     * max_attempts_per_second: 10 (0.1s par tentative)
     * lockout_duration: 60 secondes (ou 30 pour la démo)
```
   - Méthodes:
```python
     * try_password(username, password, correct_password)
     * is_account_locked(username)
     * get_remaining_lockout_time(username)

```
2. Implémentez la logique:
   - Incrémenter les tentatives échouées
   - Après 3 échechs: verrouiller le compte
   - Pendant verrouillage: refuser toute tentative
   - Appliquer les délais (0.1s par tentative)
   - Reset après succès

3. Testez avec:
   - 5 tentatives de mots de passe incorrects
   - Vérification du verrouillage
   - Attente du déverrouillage
   - Succès final

Contraintes:
- Afficher le statut à chaque tentative
- Mesurer le temps total
- Montrer l'impact du rate limiting
- Sans rate limiting: 1 tentative = ~0s
- Avec rate limiting: 1 tentative = 0.1s
- Afficher le nombre de tentatives restantes

Indications:
- time.sleep() pour les délais
- Dictionnaire pour stocker les tentatives par compte
- Tuple (timestamp, duration) pour le lockout
- time.time() pour vérifier le déverrouillage

Exemple de sortie attendue:
=====================================
RATE LIMITED AUTHENTICATION

Configuration:
- Max tentatives: 3
- Délai entre tentatives: 0.1s
- Durée de lockout: 30s
- Mot de passe correct: SecurePass123!

Tentative 1: 'wrongpass1'
  Status: FAILED
  Tentatives restantes: 2
  Temps écoulé: 0.1s

Tentative 2: 'wrongpass2'
  Status: FAILED
  Tentatives restantes: 1
  Temps écoulé: 0.2s

Tentative 3: 'wrongpass3'
  Status: FAILED - COMPTE VERROUILLÉ!
  Temps écoulé: 0.3s

Tentative 4 (pendant verrouillage): 'SecurePass123!'
  Status: ACCOUNT LOCKED
  Temps de déverrouillage restant: 28.5s
  Temps écoulé: 0.4s

ATTENTE... (30 secondes)

Tentative 5 (après déverrouillage): 'SecurePass123!'
  Status: SUCCESS!
  Temps écoulé: 30.5s

STATISTIQUES:
- Temps total: 30.5s (si sans rate limiting: ~0.01s)
- Impact du rate limiting: 3,050x plus lent
- Conclusion: Le rate limiting rend les attaques impratiquables
=====================================

Bonus:
- Implémenter des délais croissants (1s, 5s, 1min, etc.)
- Ajouter un exponential backoff
- Implémenter CAPTCHA après 2 tentatives
- Ajouter une notification d'accès suspect

========================================
## Défi 7: Wordlist Generation et Optimization
========================================

Objectif : Générer des wordlists intelligentes basées sur patterns

Créez un script qui :
1. Définissez une fonction `generate_smart_wordlist()`:
   - Années courantes (2020-2025)
   - Mois et jours
   - Noms courants + chiffres
   - Mots courants + variations
   - Patterns de clavier (qwerty, asdfgh)
   - Résultat: 50,000+ mots sans doublons

2. Implémentez `generate_statistics(wordlist)`:
   - Taille de la wordlist
   - Longueur moyenne des mots
   - Distribution (% par longueur)
   - Top 10 mots les plus courants
   - Estimations de temps de cracking

3. Testez l'efficacité:
   - Générer 3 wordlists de taille croissante
   - Tester chacune contre 10 hashs
   - Calculer le taux de succès
   - Mesurer le temps nécessaire
   - Afficher ROI (return on investment)

Contraintes:
- MIN 10,000 mots dans la wordlist finale
- Pas de doublons
- Variations (capitales, chiffres)
- Patterns intelligents (dates, années)
- Afficher la composition de la wordlist

Indications:
- Listes de mots de base
- itertools.product() pour combinaisons
- set() pour supprimer doublons
- len() et Counter pour les statistiques

Exemple de sortie attendue:
=====================================
SMART WORDLIST GENERATION

Wordlist Taille 1: 5,000 mots
- Mots de base: 1,000
- Avec variations: 5,000 (5x)
- Temps d'attaque: ~1-5 secondes

Wordlist Taille 2: 15,000 mots
- Mots de base: 2,000
- Avec variations: 15,000 (7.5x)
- Temps d'attaque: ~3-15 secondes

Wordlist Taille 3: 50,000 mots
- Mots de base: 5,000
- Avec variations: 50,000 (10x)
- Temps d'attaque: ~10-50 secondes

Composition Wordlist 3:
- Mots courants: 5,000 (10%)
- Variations (maj): 5,000 (10%)
- Variations (chiffres): 15,000 (30%)
- Années/dates: 10,000 (20%)
- Patterns clavier: 15,000 (30%)

Statistiques:
- Longueur moyenne: 7.2 caractères
- Plus court: 1 ("a")
- Plus long: 12 ("qwertyuiopasdfghjkl")

Efficacité:
Wordlist │ Hashs Crackés │ Taux  │ Temps
─────────┼───────────────┼───────┼───────
5,000    │ 6 / 10        │ 60%   │ 2.3s
15,000   │ 8 / 10        │ 80%   │ 7.8s
50,000   │ 9 / 10        │ 90%   │ 25.1s

Conclusion:
- Wordlist 15,000 offre le meilleur ROI
- Augmenter à 50,000 = 3x plus lent pour 10% de succès supplémentaire
=====================================

Bonus:
- Importer rockyou.txt (simulation)
- Analyser les patterns des mots de passe compromis
- Créer une wordlist personnalisée par secteur (finance, tech, etc.)

========================================
## Défi 8: Cracker Professionnel Complet
========================================

Objectif : Créer un cracker professionnel avec stats complètes

Créez un script qui :
1. Créez une classe `ProfessionalPasswordCracker`:
   - Initializer avec: config (threads, rate_limit, hash_type)
   - Methods:
```python
     * load_wordlist(filepath)
     * add_custom_words(words_list)
     * crack(target_hash)
     * crack_multiple(hashes_list)
     * generate_report()

```
2. Implémentez `crack()`:
   - Détection automatique du hash type
   - Multi-threading (si configuré)
   - Rate limiting (si configuré)
   - Statistiques détaillées:
```python
     * Mot de passe trouvé ou non
     * Nombre de tentatives
     * Temps total
     * Vitesse (mots/seconde)
     * Efficacité (% trouvé)

```
3. Implémentez `crack_multiple()`:
   - Attaquer plusieurs hashs
   - Résumé global:
     * Total hashs
     * Hashs crackés
```python
     * Taux de succès
     * Temps moyen par hash
     * Vitesse globale

```
4. Créez un rapport (`generate_report()`):
   - Détails complets en format texte
   - Export possible en JSON/CSV
   - Graphique ASCII (si possible)

Contraintes:
- Support MD5, SHA1, SHA256, SHA512
- Support multi-threading (1-8 threads)
- Support rate limiting configurable
- Gestion des erreurs complète
- Code bien commenté
- Fonctions modulaires et réutilisables

Indications:
- Classe avec __init__, méthodes privées, publiques
- Configuration (dictionnaire ou dataclass)
- Logging pour debug
- Séparation concerns (cracking, reporting, etc.)
- Gestion des exceptions

Exemple de sortie attendue:
=====================================
PROFESSIONAL PASSWORD CRACKER v1.0

Configuration:
- Threads: 4
- Rate limiting: Désactivé
- Hash type: AUTO-DETECT
- Wordlist: custom_wordlist.txt (50,000 mots)

ATTAQUE 1 : e3b0c44...
  [████████░░] 87%
  Hash type: SHA256 (détecté)
  Status: SUCCESS
  Mot de passe: SuperSecret2024!
  Tentatives: 4,287 / 50,000
  Temps: 0.54 secondes
  Vitesse: 7,938 mots de passe/seconde

ATTAQUE 2 : 5d41402...
  [██████████] 100%
  Hash type: MD5 (détecté)
  Status: FAILED
  Tentatives: 50,000 / 50,000
  Temps: 1.23 secondes
  Vitesse: 40,650 mots de passe/seconde

ATTAQUE 3 : aaf4c61...
  [██████████] 100%
  Hash type: SHA1 (détecté)
  Status: SUCCESS
  Mot de passe: password123
  Tentatives: 12 / 50,000
  Temps: 0.15 secondes
  Vitesse: 80,000 mots de passe/seconde

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RAPPORT FINAL:
- Total attaques: 3
- Succès: 2
- Échechs: 1
- Taux de succès: 66.7%
- Temps total: 1.92 secondes
- Vitesse moyenne: 42,861 mots de passe/seconde
- Tentatives totales: 54,299

Statistiques par type:
- SHA256: 1 succès (0.54s)
- MD5: 1 échec (1.23s)
- SHA1: 1 succès (0.15s)

Conclusions:
- SHA1 et MD5 sont TRÈS rapides (DANGEREUX!)
- SHA256 offre un bon équilibre
- Même avec 50K wordlist: 33% des hashs non crackés
- Recommandation: Utiliser bcrypt/argon2
=====================================

Bonus:
- Implémenter un GUI simple (Tkinter)
- Exporter les résultats en HTML
- Créer un dashboard avec matplotlib
- Ajouter des patterns d'attaque supplémentaires
- Implémenter GPU acceleration (simulation)

========================================
FIN DES DÉFIS
========================================

Pour valider votre compréhension:

1. Tester tous les défis sans regarder les solutions
2. Créer votre propre cracker personnalisé
3. Analyser les performances réelles
4. Documenter vos résultats
5. Proposer des améliorations

Ressources pour aller plus loin:
- Hashcat (GPU cracking)
- John the Ripper
- rockyou.txt (vrai wordlist 14M mots)
- CyberDefenders CTF
- TryHackMe Password Cracking Room

REMINDER: Utilisation UNIQUEMENT autorisée!
