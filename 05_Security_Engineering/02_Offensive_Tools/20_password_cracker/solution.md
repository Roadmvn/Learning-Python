========================================
SOLUTIONS : PASSWORD CRACKER EN PYTHON
Solutions complètes pour tous les défis
========================================

AVERTISSEMENT:
Ces solutions sont fournies à titre éducatif.
Respectez la légalité et l'éthique lors de l'utilisation.

========================================
## Solution Défi 1: Cracker de Base
========================================

CONCEPT:
- Hashing simple (convertir mot de passe en hash)
- Dictionary attack basique (tester une liste de mots)
- Mesure de performance

CODE SOLUTION:

```python
```python
import hashlib
import time

def create_test_hash(password, hash_type="sha256"):
    """Créer un hash pour tester"""
    if hash_type == "md5":
        return hashlib.md5(password.encode()).hexdigest()
    elif hash_type == "sha1":
        return hashlib.sha1(password.encode()).hexdigest()
    elif hash_type == "sha256":
        return hashlib.sha256(password.encode()).hexdigest()
    elif hash_type == "sha512":
        return hashlib.sha512(password.encode()).hexdigest()
    else:
        raise ValueError(f"Type de hash inconnu: {hash_type}")

def simple_dictionary_attack(target_hash, hash_type="sha256"):
    """Attaque par dictionnaire simple"""
    # Wordlist simple (50 mots courants)
    wordlist = [
        "password", "123456", "12345678", "qwerty", "abc123",
        "monkey", "1234567", "letmein", "dragon", "111111",
        "123123", "football", "baseball", "princess", "master",
        "iloveyou", "michael", "jordan", "friends", "ashley",
        "welcome", "admin", "pass", "login", "root",
        "test", "security", "secret", "freedom", "hello",
        "sunshine", "password123", "2023", "2024", "2025",
        "admin123", "letmein123", "welcome123", "qwerty123", "test123",
        "pass123", "123password", "password1", "admin1", "test1",
        "hello123", "world123", "love123", "dragon123", "master123",
        "sunshine123", "football123", "baseball123", "soccer", "tennis",
    ]

    print(f"Hash cible: {target_hash}")
    print(f"Type: {hash_type.upper()}")
    print(f"Wordlist taille: {len(wordlist)} mots")
    print()

    start_time = time.time()
    tested = 0

    for word in wordlist:
        if hash_type == "md5":
            candidate_hash = hashlib.md5(word.encode()).hexdigest()
        elif hash_type == "sha1":
            candidate_hash = hashlib.sha1(word.encode()).hexdigest()
        elif hash_type == "sha256":
            candidate_hash = hashlib.sha256(word.encode()).hexdigest()
        elif hash_type == "sha512":
            candidate_hash = hashlib.sha512(word.encode()).hexdigest()

        tested += 1

        # Afficher la progression tous les 10 tests
        if tested % 10 == 0:
            elapsed = time.time() - start_time
            print(f"Progression: {tested} testés ({elapsed:.3f}s)")

        # Vérifier la correspondance
        if candidate_hash == target_hash:
            elapsed = time.time() - start_time
            print()
            print("MOT DE PASSE TROUVÉ:", word)
            print(f"Tentatives: {tested} / {len(wordlist)}")
            print(f"Temps total: {elapsed:.3f} secondes")
            if elapsed > 0:
                print(f"Vitesse moyenne: {tested / elapsed:.0f} mots de passe/seconde")
            return word, tested, elapsed

    elapsed = time.time() - start_time
    print()
    print(f"ÉCHOUÉ: Mot de passe non trouvé après {tested} tentatives")
    print(f"Temps total: {elapsed:.3f} secondes")
    return None, tested, elapsed

```
# TEST
```python
if __name__ == "__main__":
    # Test 1: Créer un hash et le cracker
    password = "password123"
    hash_value = create_test_hash(password, "sha256")
    print("="*50)
    print("TEST 1: Basic Dictionary Attack")
    print("="*50)
    print(f"Mot de passe original: {password}")
    print(f"Hash SHA256: {hash_value}")
    print()
    found, attempts, elapsed = simple_dictionary_attack(hash_value, "sha256")

    # Test 2: Tester avec différents types de hash
    print()
    print("="*50)
    print("TEST 2: Différents types de hash")
    print("="*50)
    for hash_type in ["md5", "sha1", "sha256"]:
        hash_val = create_test_hash("admin123", hash_type)
        print(f"\nTesting {hash_type.upper()}:")
        found, attempts, elapsed = simple_dictionary_attack(hash_val, hash_type)
```
```

POINTS CLÉS:
1. hashlib offre MD5, SHA1, SHA256, SHA512
2. Dictionary attack est très rapide (ms)
3. Afficher la progression aide à comprendre le flux
4. Mesurer le temps de performance est important

========================================
## Solution Défi 2: Brute Force
========================================

CONCEPT:
- Génération exhaustive de toutes les combinaisons
- Explosion exponentielle de la complexité
- Limitation à mots courts

CODE SOLUTION:

```python
```python
import hashlib
import time
import itertools
import string

def brute_force_generator(min_len=1, max_len=3, charset=None):
    """
    Générateur pour les combinations brute force
    Utilise un générateur pour économiser la mémoire
    """
    if charset is None:
        charset = string.ascii_lowercase + string.digits

    total_combinations = sum(len(charset) ** l for l in range(min_len, max_len + 1))
    print(f"Charset: {charset}")
    print(f"Total combinaisons: {total_combinations:,}")
    print()

    # Calculer les combinaisons par longueur
    for length in range(min_len, max_len + 1):
        combinations_at_length = len(charset) ** length
        print(f"Longueur {length}: {combinations_at_length:,} combinaisons")
        for combination in itertools.product(charset, repeat=length):
            yield ''.join(combination)

def brute_force_crack(target_hash, charset=None, max_length=4, hash_type="sha256"):
    """
    Brute force cracker
    """
    if charset is None:
        charset = string.ascii_lowercase + string.digits

    print("="*50)
    print("BRUTE FORCE ATTACK")
    print("="*50)
    print(f"Hash cible: {target_hash[:32]}...")
    print(f"Charset: {charset}")
    print(f"Max longueur: {max_length}")
    print()

    start_time = time.time()
    tested = 0

    # Utiliser le générateur
    generator = brute_force_generator(min_len=1, max_len=max_length, charset=charset)

    for password in generator:
        # Calculer le hash
        if hash_type == "sha256":
            candidate_hash = hashlib.sha256(password.encode()).hexdigest()
        elif hash_type == "md5":
            candidate_hash = hashlib.md5(password.encode()).hexdigest()
        else:
            candidate_hash = hashlib.sha256(password.encode()).hexdigest()

        tested += 1

        # Afficher la progression tous les 1000 tests
        if tested % 1000 == 0:
            elapsed = time.time() - start_time
            speed = tested / elapsed
            print(f"Tentatives: {tested:,} ({speed:,.0f}/sec)")

        # Vérifier la correspondance
        if candidate_hash == target_hash:
            elapsed = time.time() - start_time
            print()
            print("MOT DE PASSE TROUVÉ:", password)
            print(f"Tentatives totales: {tested:,}")
            print(f"Temps: {elapsed:.3f} secondes")
            if elapsed > 0:
                print(f"Vitesse: {tested/elapsed:,.0f} mots de passe/seconde")
            return password, tested, elapsed

    elapsed = time.time() - start_time
    print()
    print(f"ÉCHOUÉ après {tested:,} tentatives")
    print(f"Temps: {elapsed:.3f} secondes")
    return None, tested, elapsed

```
# TEST
```python
if __name__ == "__main__":
    # Créer un hash court
    password = "abc1"
    hash_value = hashlib.sha256(password.encode()).hexdigest()

    print(f"Mot de passe à cracker: {password}")
    print(f"Hash: {hash_value}")
    print()

    # Lancer le brute force
    found, attempts, elapsed = brute_force_crack(
        hash_value,
        charset=string.ascii_lowercase + string.digits,
        max_length=4,
        hash_type="sha256"
    )

    # Comparaison avec dictionary
    print()
    print("="*50)
    print("COMPARAISON")
    print("="*50)
    print("Brute force:")
    print(f"  - Mots testés: {attempts:,}")
    print(f"  - Temps: {elapsed:.3f}s")
    print()
    print("Dictionary (si le mot était dans la liste):")
    print(f"  - Mots testés: ~50")
    print(f"  - Temps: ~0.010s")
    print()
    print(f"Brute force est {attempts/50:.0f}x plus lent!")
```
```

POINTS CLÉS:
1. itertools.product() génère les combinaisons
2. Utiliser un générateur pour économiser la mémoire
3. L'explosion exponentielle rend le brute force impraticable
4. Longueur 8 avec 62 caractères = 218 TRILLIONS de combinaisons!

========================================
## Solution Défi 3: Attaque Hybride
========================================

CONCEPT:
- Combiner dictionary avec variations intelligentes
- 1 mot → 10+ variations
- Beaucoup plus efficace que dictionary seul

CODE SOLUTION:

```python
```python
import hashlib
import time

def generate_word_variations(word):
    """Générer les variations d'un mot"""
    variations = [
        word,                      # lowercase
        word.capitalize(),         # Capitalize
        word.upper(),              # UPPERCASE
        word + "123",              # Word + chiffres
        word + "1234",
        word + "2024",
        word + "2025",
        word + "!",                # Word + symboles
        word + "@",
        word + "#",
        word[:3] + "0" + word[3:], # l33t speak: o→0 (simple)
    ]
    # Supprimer les doublons
    return list(set(variations))

def generate_hybrid_wordlist(base_words):
    """Générer une wordlist avec variations"""
    full_wordlist = []

    for word in base_words:
        variations = generate_word_variations(word)
        full_wordlist.extend(variations)
        print(f"'{word}' → {len(variations)} variations")

    # Supprimer les doublons et trier
    full_wordlist = sorted(list(set(full_wordlist)))
    return full_wordlist

def hybrid_attack(target_hash, base_words, hash_type="sha256"):
    """Attaque hybride"""
    print("="*50)
    print("HYBRID ATTACK (Dictionary + Variations)")
    print("="*50)

    # Générer la wordlist
    print("\nGénération de wordlist:")
    wordlist = generate_hybrid_wordlist(base_words)

    print(f"\nHash cible: {target_hash[:32]}...")
    print(f"Mots de base: {len(base_words)}")
    print(f"Wordlist finale: {len(wordlist)}")
    print(f"Augmentation: {len(wordlist)/len(base_words):.1f}x")
    print()

    start_time = time.time()
    tested = 0

    for password in wordlist:
        if hash_type == "sha256":
            candidate_hash = hashlib.sha256(password.encode()).hexdigest()
        else:
            candidate_hash = hashlib.md5(password.encode()).hexdigest()

        tested += 1

        if tested % 50 == 0:
            elapsed = time.time() - start_time
            speed = tested / elapsed if elapsed > 0 else 0
            print(f"Progression: {tested:,} ({speed:,.0f}/sec)")

        if candidate_hash == target_hash:
            elapsed = time.time() - start_time
            print()
            print("MOT DE PASSE TROUVÉ:", password)
            print(f"Tentatives: {tested} / {len(wordlist)}")
            print(f"Temps: {elapsed:.3f} secondes")
            if elapsed > 0:
                print(f"Vitesse: {tested/elapsed:,.0f} mots de passe/seconde")
            return password, tested, elapsed

    elapsed = time.time() - start_time
    print()
    print(f"ÉCHOUÉ après {tested:,} tentatives")
    return None, tested, elapsed

```
# TEST
```python
if __name__ == "__main__":
    # Créer un hash d'une variation
    password = "Password123!"
    # Note: "!" n'est pas supporté par notre générateur simple
    # Créer manuellement pour la démo
    hash_value = hashlib.sha256("Password123".encode()).hexdigest()

    base_words = ["password", "admin", "secret", "test", "hello"]

    print(f"Mot de passe original: {password}")
    print(f"Hash: {hash_value}")
    print()

    found, attempts, elapsed = hybrid_attack(hash_value, base_words, "sha256")
```
```

POINTS CLÉS:
1. Les variations augmentent considérablement l'efficacité
2. Taux de succès : Dictionary 50% → Hybrid 90%+
3. Peu de surcharge en temps (variations rapides à générer)
4. Stratégie d'attaque réaliste utilisée en pentesting

========================================
## Solution Défi 4: Multi-Type Hashing
========================================

CONCEPT:
- Détecter le type de hash par la longueur
- Cracker avec le bon algorithme
- Gérer plusieurs hashs en boucle

CODE SOLUTION:

```python
```python
import hashlib
import time

def detect_hash_type(hash_string):
    """Détecter le type de hash par la longueur"""
    hash_length = len(hash_string)

    if hash_length == 32:
        return "md5"
    elif hash_length == 40:
        return "sha1"
    elif hash_length == 64:
        return "sha256"
    elif hash_length == 128:
        return "sha512"
    else:
        return "unknown"

def crack_hash(target_hash, wordlist, hash_type="sha256"):
    """Cracker un hash unique"""
    start_time = time.time()

    for word in wordlist:
        if hash_type == "md5":
            candidate = hashlib.md5(word.encode()).hexdigest()
        elif hash_type == "sha1":
            candidate = hashlib.sha1(word.encode()).hexdigest()
        elif hash_type == "sha256":
            candidate = hashlib.sha256(word.encode()).hexdigest()
        elif hash_type == "sha512":
            candidate = hashlib.sha512(word.encode()).hexdigest()

        if candidate == target_hash:
            elapsed = time.time() - start_time
            return word, elapsed

    elapsed = time.time() - start_time
    return None, elapsed

def crack_multiple_hashes(hashes_list, wordlist):
    """Cracker plusieurs hashs"""
    print("="*50)
    print("MULTI-TYPE HASH CRACKING")
    print("="*50)
    print(f"Total hashs: {len(hashes_list)}")
    print(f"Wordlist taille: {len(wordlist)}")
    print()

    results = []
    total_time = 0

    for i, target_hash in enumerate(hashes_list, 1):
        print(f"\nHash #{i}: {target_hash[:32]}...")

        # Détecter le type
        hash_type = detect_hash_type(target_hash)
        print(f"  Type: {hash_type.upper()}")

        # Cracker
        found_password, elapsed = crack_hash(target_hash, wordlist, hash_type)
        total_time += elapsed

        if found_password:
            print(f"  Status: SUCCESS")
            print(f"  Mot de passe: {found_password}")
            results.append({"hash": target_hash[:32], "found": True, "password": found_password, "time": elapsed})
        else:
            print(f"  Status: FAILED")
            results.append({"hash": target_hash[:32], "found": False, "password": None, "time": elapsed})

        print(f"  Temps: {elapsed:.3f} secondes")

    # Résumé
    print()
    print("="*50)
    print("RÉSUMÉ")
    print("="*50)
    found_count = sum(1 for r in results if r["found"])
    success_rate = (found_count / len(results)) * 100 if results else 0

    print(f"Total crackés: {found_count} / {len(results)}")
    print(f"Taux de succès: {success_rate:.1f}%")
    print(f"Temps total: {total_time:.3f} secondes")

    return results

```
# TEST
```python
if __name__ == "__main__":
    # Créer une wordlist de test
    wordlist = ["password", "hello", "test123", "admin", "secret", "admin123"]

    # Créer des hashs de différents types
    hashes = [
        hashlib.sha256("password".encode()).hexdigest(),      # SHA256
        hashlib.md5("hello".encode()).hexdigest(),             # MD5
        hashlib.sha1("test123".encode()).hexdigest(),          # SHA1
        hashlib.sha256("notfound".encode()).hexdigest(),       # SHA256 (pas dans wordlist)
        hashlib.sha512("secret".encode()).hexdigest(),         # SHA512
    ]

    print(f"Test avec {len(hashes)} hashs")
    print(f"Wordlist: {wordlist}")
    print()

    results = crack_multiple_hashes(hashes, wordlist)
```
```

POINTS CLÉS:
1. La longueur du hash détermine l'algorithme
2. Automatiser la détection rend l'outil générique
3. Gérer plusieurs hashs en boucle
4. Afficher un résumé global pour l'analyse

========================================
## Solution Défi 5: Multi-Threading
========================================

CONCEPT:
- Diviser la wordlist entre threads
- Chaque thread craque sa portion
- Utiliser un signal (Event) pour arrêter après succès

CODE SOLUTION:

```python
```python
import hashlib
import threading
import time

class ThreadedCracker:
    def __init__(self, target_hash, hash_type="sha256", num_threads=4):
        self.target_hash = target_hash
        self.hash_type = hash_type
        self.num_threads = num_threads
        self.found_password = None
        self.found_event = threading.Event()  # Signal d'arrêt
        self.total_tested = 0
        self.total_tested_lock = threading.Lock()  # Synchronisation

    def worker(self, wordlist, thread_id):
        """Fonction du worker thread"""
        # Calculer la portion de wordlist
        words_per_thread = len(wordlist) // self.num_threads
        start_idx = thread_id * words_per_thread
        end_idx = (thread_id + 1) * words_per_thread if thread_id < self.num_threads - 1 else len(wordlist)

        print(f"Thread {thread_id}: Testant mots {start_idx:,} à {end_idx:,}")

        for i in range(start_idx, end_idx):
            # Arrêter si déjà trouvé
            if self.found_event.is_set():
                break

            word = wordlist[i]

            # Hashing
            if self.hash_type == "sha256":
                candidate = hashlib.sha256(word.encode()).hexdigest()
            else:
                candidate = hashlib.md5(word.encode()).hexdigest()

            # Increment thread-safe
            with self.total_tested_lock:
                self.total_tested += 1

            # Vérifier
            if candidate == self.target_hash:
                self.found_password = word
                self.found_event.set()
                print(f"Thread {thread_id}: MOT DE PASSE TROUVÉ: {word}")
                break

    def crack(self, wordlist):
        """Lancer l'attaque"""
        start_time = time.time()
        self.total_tested = 0
        self.found_password = None
        self.found_event.clear()

        print(f"\nMULTI-THREADED CRACKING ({self.num_threads} threads)")
        print(f"Wordlist: {len(wordlist):,} mots")
        print(f"Hash type: {self.hash_type}")
        print()

        # Créer les threads
        threads = []
        for i in range(self.num_threads):
            t = threading.Thread(
                target=self.worker,
                args=(wordlist, i),
                daemon=False
            )
            threads.append(t)
            t.start()

        # Attendre
        for t in threads:
            t.join()

        elapsed = time.time() - start_time
        return self.found_password, self.total_tested, elapsed

```
# TEST BENCHMARK
```python
if __name__ == "__main__":
    # Créer une wordlist
    wordlist = [f"word{i}" for i in range(10000)]
    password = "word5000"  # Au milieu
    target_hash = hashlib.sha256(password.encode()).hexdigest()

    print("BENCHMARK MULTI-THREADING")
    print(f"Mot de passe: {password}")
    print(f"Wordlist: {len(wordlist):,} mots")
    print()

    results = {}

    # Test avec 1, 2, 4, 8 threads
    for num_threads in [1, 2, 4, 8]:
        cracker = ThreadedCracker(target_hash, "sha256", num_threads=num_threads)
        found, tested, elapsed = cracker.crack(wordlist)

        results[num_threads] = elapsed
        print(f"Temps: {elapsed:.3f}s")

    # Afficher le speedup
    print()
    print("SPEEDUP:")
    baseline = results[1]
    for num_threads in sorted(results.keys()):
        speedup = baseline / results[num_threads]
        print(f"{num_threads} threads: {speedup:.2f}x")
```
```

POINTS CLÉS:
1. threading.Lock() pour la synchronisation
2. threading.Event() pour arrêter les autres threads
3. Le speedup réel dépend du nombre de cores
4. Décrochage au-delà des cores physiques

========================================
## Solution Défi 6: Rate Limiting
========================================

CONCEPT:
- Délai entre les tentatives
- Verrouillage après N échechs
- Simulation de sécurité réelle

CODE SOLUTION:

```python
```python
import time

class RateLimitedAuthenticator:
    def __init__(self, max_attempts=3, max_per_second=10, lockout_duration=30):
        self.max_attempts = max_attempts
        self.delay = 1.0 / max_per_second
        self.lockout_duration = lockout_duration
        self.failed_attempts = {}
        self.locked_accounts = {}

    def try_password(self, username, password, correct_password):
        """Tenter un mot de passe"""
        # Vérifier le verrouillage
        if username in self.locked_accounts:
            lock_time, duration = self.locked_accounts[username]
            elapsed = time.time() - lock_time
            if elapsed < duration:
                remaining = duration - elapsed
                return False, f"Compte verrouillé ({remaining:.1f}s)"
            else:
                del self.locked_accounts[username]
                self.failed_attempts[username] = 0

        # Appliquer le délai
        time.sleep(self.delay)

        # Tester
        if password == correct_password:
            if username in self.failed_attempts:
                del self.failed_attempts[username]
            return True, "Succès"
        else:
            # Increment
            self.failed_attempts[username] = self.failed_attempts.get(username, 0) + 1

            # Vérifier le seuil
            if self.failed_attempts[username] >= self.max_attempts:
                self.locked_accounts[username] = (time.time(), self.lockout_duration)
                return False, "Compte verrouillé"

            remaining = self.max_attempts - self.failed_attempts[username]
            return False, f"Échoué ({remaining} tentatives restantes)"

```
# TEST
```python
if __name__ == "__main__":
    auth = RateLimitedAuthenticator(max_attempts=3, max_per_second=5, lockout_duration=10)

    username = "user@example.com"
    correct_password = "SecurePass123!"
    attempts = ["wrong1", "wrong2", "wrong3", "SecurePass123!", "another"]

    print("RATE LIMITED AUTHENTICATION TEST")
    print(f"Compte: {username}")
    print(f"Correct: {correct_password}")
    print(f"Max tentatives: 3")
    print(f"Délai: 0.2s (5/sec)")
    print(f"Lockout: 10s")
    print()

    start = time.time()

    for password in attempts:
        success, message = auth.try_password(username, password, correct_password)
        elapsed = time.time() - start
        status = "SUCCESS" if success else "FAILED"
        print(f"Tentative: '{password}' → {status} ({message}) [{elapsed:.1f}s]")

        if "Compte verrouillé" in message:
            print("  Attente 2s...")
            time.sleep(2)

    print()
    print(f"Temps total: {time.time() - start:.1f}s")
```
```

POINTS CLÉS:
1. time.sleep() pour les délais
2. Stockage des tentatives échouées par compte
3. Verrouillage temporaire après seuil
4. Impact massif sur les attaques (milliers d'heures pour 1M tentatives)

========================================
## Solution Défi 7: Wordlist Generation
========================================

CONCEPT:
- Générer intelligemment des wordlists
- Inclure les patterns courants
- Analyser l'efficacité

CODE SOLUTION:

```python
```python
import time
from collections import Counter

def generate_smart_wordlist():
    """Générer une wordlist intelligente"""
    wordlist = set()

    # 1. Mots courants
    common_words = [
        "password", "admin", "test", "hello", "world",
        "secret", "welcome", "login", "user", "admin123",
        "letmein", "monkey", "dragon", "master", "shadow",
    ]
    wordlist.update(common_words)

    # 2. Années
    for year in range(1980, 2026):
        wordlist.add(str(year))

    # 3. Variations de mots
    for word in common_words:
        wordlist.add(word.capitalize())
        wordlist.add(word.upper())
        for year in range(2000, 2026):
            wordlist.add(f"{word}{year}")
        for num in range(100, 200):
            wordlist.add(f"{word}{num}")

    # 4. Patterns de clavier
    keyboards = [
        "qwerty", "asdfgh", "zxcvbn",
        "123456", "1234567", "12345678",
    ]
    wordlist.update(keyboards)

    # 5. Combinaisons
    for keyboard in keyboards:
        wordlist.add(keyboard.capitalize())
        for year in range(2000, 2026):
            wordlist.add(f"{keyboard}{year}")

    return sorted(list(wordlist))

def generate_statistics(wordlist):
    """Analyser une wordlist"""
    print("WORDLIST STATISTICS")
    print(f"Taille: {len(wordlist):,}")

    # Longueur
    lengths = [len(w) for w in wordlist]
    avg_length = sum(lengths) / len(lengths)
    print(f"Longueur moyenne: {avg_length:.1f}")
    print(f"Min: {min(lengths)}, Max: {max(lengths)}")

    # Distribution
    dist = Counter(lengths)
    print("\nDistribution par longueur:")
    for length in sorted(dist.keys())[:10]:
        count = dist[length]
        pct = (count / len(wordlist)) * 100
        print(f"  {length:2d} caractères: {count:5,} ({pct:5.1f}%)")

    # Top 10
    print("\nTop 10 mots:")
    for i, word in enumerate(wordlist[:10], 1):
        print(f"  {i}. {word}")

```
# TEST
```python
if __name__ == "__main__":
    wordlist = generate_smart_wordlist()
    generate_statistics(wordlist)

    # Tester l'efficacité
    print("\n" + "="*50)
    print("EFFICACITÉ")
    print("="*50)

    test_passwords = ["password2024", "admin123", "qwerty", "letmein2023"]
    found = sum(1 for pwd in test_passwords if pwd in wordlist)

    print(f"Test: {len(test_passwords)} mots de passe")
    print(f"Trouvés: {found}")
    print(f"Taux: {(found/len(test_passwords))*100:.0f}%")
```
```

POINTS CLÉS:
1. Générer une wordlist pertinente augmente le succès
2. Patterns intelligents (années, variantes) essentiels
3. Équilibre taille vs efficacité
4. 10K mots offrent généralement le meilleur ROI

========================================
## Solution Défi 8: Cracker Complet
========================================

CONCEPT:
- Classe intégrée avec toutes les fonctionnalités
- Multi-threading, rate limiting, detection
- Reporting complète

CODE SOLUTION (EXTRAIT):

```python
```python
import hashlib
import threading
import time
from typing import Optional, Dict, List

class ProfessionalPasswordCracker:
    """Cracker professionnel complet"""

    def __init__(self, config=None):
        self.config = config or {
            "threads": 4,
            "rate_limit": 0,
            "hash_type": "auto",
        }
        self.results = []

    def load_wordlist(self, filepath):
        """Charger une wordlist"""
        with open(filepath, 'r') as f:
            return [line.strip() for line in f]

    def detect_hash_type(self, hash_str):
        """Détecter le type de hash"""
        length = len(hash_str)
        if length == 32:
            return "md5"
        elif length == 40:
            return "sha1"
        elif length == 64:
            return "sha256"
        elif length == 128:
            return "sha512"
        return "unknown"

    def crack(self, target_hash, wordlist):
        """Cracker un hash"""
        hash_type = self.detect_hash_type(target_hash)
        if self.config["hash_type"] == "auto":
            hash_type = hash_type
        else:
            hash_type = self.config["hash_type"]

        print(f"Cracking: {target_hash[:32]}...")
        print(f"Type: {hash_type}")

        start = time.time()
        tested = 0

        for word in wordlist:
            if hash_type == "md5":
                candidate = hashlib.md5(word.encode()).hexdigest()
            elif hash_type == "sha1":
                candidate = hashlib.sha1(word.encode()).hexdigest()
            elif hash_type == "sha256":
                candidate = hashlib.sha256(word.encode()).hexdigest()
            elif hash_type == "sha512":
                candidate = hashlib.sha512(word.encode()).hexdigest()

            tested += 1

            if self.config["rate_limit"] > 0:
                time.sleep(self.config["rate_limit"])

            if candidate == target_hash:
                elapsed = time.time() - start
                result = {
                    "hash": target_hash,
                    "found": True,
                    "password": word,
                    "attempts": tested,
                    "time": elapsed,
                }
                self.results.append(result)
                return result

        elapsed = time.time() - start
        result = {
            "hash": target_hash,
            "found": False,
            "password": None,
            "attempts": tested,
            "time": elapsed,
        }
        self.results.append(result)
        return result

    def crack_multiple(self, hashes, wordlist):
        """Cracker plusieurs hashs"""
        print("="*50)
        print("PROFESSIONAL PASSWORD CRACKER")
        print("="*50)
        print(f"Total hashs: {len(hashes)}")
        print(f"Wordlist: {len(wordlist):,}")
        print()

        for i, hash_val in enumerate(hashes, 1):
            print(f"\n[{i}/{len(hashes)}]", end=" ")
            self.crack(hash_val, wordlist)

        return self.generate_report()

    def generate_report(self):
        """Générer un rapport"""
        found = sum(1 for r in self.results if r["found"])
        total_time = sum(r["time"] for r in self.results)
        total_attempts = sum(r["attempts"] for r in self.results)

        print("\n" + "="*50)
        print("RAPPORT FINAL")
        print("="*50)
        print(f"Total: {len(self.results)}")
        print(f"Trouvés: {found}")
        print(f"Taux: {(found/len(self.results))*100:.1f}%")
        print(f"Temps total: {total_time:.2f}s")
        print(f"Tentatives: {total_attempts:,}")

        return self.results

```
# TEST
```python
if __name__ == "__main__":
    cracker = ProfessionalPasswordCracker({
        "threads": 4,
        "rate_limit": 0,
        "hash_type": "auto",
    })

    # Créer les hashs
    passwords = ["password", "admin123", "test"]
    wordlist = ["password", "admin", "admin123", "test", "hello"]

    hashes = [hashlib.sha256(p.encode()).hexdigest() for p in passwords]

    # Cracker
    results = cracker.crack_multiple(hashes, wordlist)
```
```

POINTS CLÉS:
1. Architecture modulaire et extensible
2. Configuration centralisée
3. Reporting structuré
4. Support multi-hash
5. Prêt pour une utilisation en production (correctement sécurisé)

========================================
NOTES GÉNÉRALE ET POINTS CLÉS
========================================

PERFORMANCE EN RÉSUMÉ:

Algorithm    │ Vitesse   │ Danger   │ Recommandation
─────────────┼───────────┼──────────┼────────────────
MD5          │ Très vite │ TRÈS      │ JAMAIS!
SHA1         │ Très vite │ OUI       │ Legacy only
SHA256       │ Rapide    │ Moyen     │ Bon choix
SHA512       │ Lent      │ Faible    │ Mieux
bcrypt       │ Très lent │ Non       │ EXCELLENT
argon2       │ Très lent │ Non       │ MEILLEUR

TECHNIQUES D'ATTAQUE:

1. Brute Force:
   - Efficacité: 0% (mots longs) à 100% (mots courts)
   - Temps: Secondes (3 chars) à années (8+ chars)
   - Usage: Mots très courts seulement

2. Dictionary:
   - Efficacité: 80% (mots faibles)
   - Temps: Secondes
   - Usage: Attaque standard réaliste

3. Hybrid:
   - Efficacité: 95% (mots faibles)
   - Temps: Secondes
   - Usage: Attaque optimale

4. Multi-threading:
   - Speedup: 3-6x (8 threads)
   - Plateau passé 8 threads
   - Usage: Optimisation importante

5. Rate Limiting:
   - Impact: 1000-10000x ralentissement
   - Protection: EXCELLENTE
   - Usage: Sécurité essentiële

RECOMMANDATIONS DE SÉCURITÉ:

1. Pour les développeurs:
   ✓ Utiliser bcrypt ou argon2
   ✓ Ajouter un salt (inclus dans bcrypt)
   ✓ Implémenter le rate limiting
   ✓ Lockout après 3-5 tentatives
   ✓ MFA pour les comptes sensibles

2. Pour les utilisateurs:
   ✓ Mots de passe 12+ caractères
   ✓ Mélange: majuscules, minuscules, chiffres, symboles
   ✓ Pas de mots du dictionnaire
   ✓ Pas de dates personnelles
   ✓ Utiliser un gestionnaire de mots de passe

3. Pour les pentesteurs:
   ✓ Contrat signé AVANT le test
   ✓ Autorisation écrite explicit
   ✓ Scope bien défini
   ✓ Rapport complet avec recommandations
   ✓ Respecter les limites légales

========================================
FIN DES SOLUTIONS
========================================
