#!/usr/bin/env python3
"""
Exercice 20 : Password Cracker en Python
Démonstration complète des techniques de cracking de mots de passe

AVERTISSEMENT LÉGAL ET ÉTHIQUE:
- Ces techniques sont destinées à l'apprentissage et aux tests autorisés uniquement
- Cracker uniquement vos propres mots de passe
- L'utilisation sur des systèmes sans autorisation explicite est ILLÉGALE
- Respecter les lois de votre juridiction
- Contrats de pentesting signés avant tout test externe
"""

import hashlib
import string
import itertools
import threading
import time
import queue
import secrets
from typing import List, Tuple, Dict, Optional
from datetime import datetime

# =============================================================================
# PARTIE 1 : CONCEPTS DE BASE DU HASHING
# =============================================================================

def introduction_hashing():
    """
    Introduction aux concepts de hashing cryptographique
    Démontre les propriétés fondamentales des hashes
    """
    print("\n" + "="*70)
    print("PARTIE 1 : CONCEPTS DE BASE DU HASHING")
    print("="*70)

    # 1. Propriété 1 : Déterminisme (même input = même output)
    print("\n1. DÉTERMINISME (même input = même output):")
    password = "password123"
    hash1 = hashlib.sha256(password.encode()).hexdigest()
    hash2 = hashlib.sha256(password.encode()).hexdigest()
    print(f"   Premier hash:  {hash1}")
    print(f"   Second hash:   {hash2}")
    print(f"   Identiques:    {hash1 == hash2}")

    # 2. Propriété 2 : Sensibilité au changement (petit changement = hash différent)
    print("\n2. SENSIBILITÉ AU CHANGEMENT (petit changement = hash différent):")
    password_a = "password123"
    password_b = "password124"  # Différence: 1 chiffre
    hash_a = hashlib.sha256(password_a.encode()).hexdigest()
    hash_b = hashlib.sha256(password_b.encode()).hexdigest()
    print(f"   Hash de 'password123': {hash_a}")
    print(f"   Hash de 'password124': {hash_b}")
    print(f"   Ressemblance: 0% (complètement différent!)")

    # 3. Propriété 3 : Non-réversibilité (impossible de retrouver le mot de passe du hash)
    print("\n3. NON-RÉVERSIBILITÉ (impossible de retrouver le mot de passe):")
    password = "secretpassword"
    hash_value = hashlib.sha256(password.encode()).hexdigest()
    print(f"   Mot de passe: {password}")
    print(f"   Hash: {hash_value}")
    print(f"   Peut-on retrouver le mot de passe du hash? NON!")
    print(f"   Solution: Cracker (essayer tous les mots de passe possibles)")

    # 4. Comparaison de différents hashes
    print("\n4. COMPARAISON DE DIFFÉRENTS HASH ALGORITHMS:")
    password = "test123"
    password_bytes = password.encode()

    # MD5 (DÉPRÉCIÉ - Ne plus utiliser!)
    md5_hash = hashlib.md5(password_bytes).hexdigest()
    print(f"   MD5 (DÉPRÉCIÉ):        {md5_hash}")
    print(f"      Taille: 32 caractères")
    print(f"      Problème: Collisions trouvées, non sûr")

    # SHA1 (DÉPRÉCIÉ)
    sha1_hash = hashlib.sha1(password_bytes).hexdigest()
    print(f"\n   SHA1 (DÉPRÉCIÉ):       {sha1_hash}")
    print(f"      Taille: 40 caractères")
    print(f"      Problème: Collisions théoriques trouvées")

    # SHA256 (BON CHOIX)
    sha256_hash = hashlib.sha256(password_bytes).hexdigest()
    print(f"\n   SHA256 (BON):          {sha256_hash}")
    print(f"      Taille: 64 caractères")
    print(f"      Avantage: Sûr et rapide")

    # SHA512 (TRÈS SÛRE)
    sha512_hash = hashlib.sha512(password_bytes).hexdigest()
    print(f"\n   SHA512 (TRÈS SÛRE):    {sha512_hash}")
    print(f"      Taille: 128 caractères")
    print(f"      Avantage: Très sûr, délibérément lent")


# =============================================================================
# PARTIE 2 : ATTAQUE PAR FORCE BRUTE (BRUTE FORCE)
# =============================================================================

def generate_brute_force_candidates(
    min_length: int = 1,
    max_length: int = 4,
    charset: str = string.ascii_lowercase + string.digits
) -> List[str]:
    """
    Générer tous les mots de passe possibles pour une attaque brute force

    Args:
        min_length: Longueur minimale des mots de passe (défaut: 1)
        max_length: Longueur maximale des mots de passe (défaut: 4)
        charset: Ensemble de caractères à utiliser (défaut: a-z + chiffres)

    Returns:
        Liste de tous les mots de passe candidats

    Note:
        La complexité augmente EXPONENTIELLEMENT:
        - 1 caractère: 36 tentatives
        - 2 caractères: 1,296 tentatives
        - 3 caractères: 46,656 tentatives
        - 4 caractères: 1,679,616 tentatives
    """
    candidates = []
    print(f"\n   Générant mots de passe (longueur {min_length}-{max_length})...")
    print(f"   Ensemble de caractères: {charset}")

    # Itérer sur toutes les longueurs
    for length in range(min_length, max_length + 1):
        # Générer toutes les combinaisons de cette longueur
        count_before = len(candidates)
        for combination in itertools.product(charset, repeat=length):
            candidates.append(''.join(combination))
        count_after = len(candidates)
        print(f"   Longueur {length}: {count_after - count_before:,} mots de passe")

    print(f"   Total: {len(candidates):,} mots de passe")
    return candidates


def brute_force_attack(target_hash: str, hash_type: str = "sha256") -> Optional[str]:
    """
    Attaque brute force pour cracker un hash
    Teste tous les mots de passe possibles jusqu'à trouver une correspondance

    Args:
        target_hash: Le hash à cracker
        hash_type: Type de hash (md5, sha1, sha256, sha512)

    Returns:
        Le mot de passe trouvé, ou None si pas trouvé

    Exemple:
        >>> password = "abc123"
        >>> hash_value = hashlib.sha256(password.encode()).hexdigest()
        >>> found_password = brute_force_attack(hash_value)
        >>> print(found_password)  # Affiche: abc123
    """
    print(f"\n--- ATTAQUE BRUTE FORCE ---")
    print(f"   Hash cible: {target_hash[:32]}...")
    print(f"   Type: {hash_type}")

    # Générer les candidats (limiter à 4 caractères pour la démo)
    candidates = generate_brute_force_candidates(
        min_length=1,
        max_length=4,
        charset=string.ascii_lowercase + string.digits
    )

    start_time = time.time()
    tested = 0

    # Tester chaque mot de passe candidat
    for password in candidates:
        # Calculer le hash du candidat
        if hash_type == "md5":
            candidate_hash = hashlib.md5(password.encode()).hexdigest()
        elif hash_type == "sha1":
            candidate_hash = hashlib.sha1(password.encode()).hexdigest()
        elif hash_type == "sha256":
            candidate_hash = hashlib.sha256(password.encode()).hexdigest()
        elif hash_type == "sha512":
            candidate_hash = hashlib.sha512(password.encode()).hexdigest()

        tested += 1

        # Vérifier s'il correspond au hash cible
        if candidate_hash == target_hash:
            elapsed = time.time() - start_time
            print(f"\n   SUCCESS! Mot de passe trouvé: {password}")
            print(f"   Tentatives: {tested:,}")
            print(f"   Temps: {elapsed:.2f} secondes")
            print(f"   Vitesse: {tested/elapsed:,.0f} mots de passe/seconde")
            return password

        # Afficher la progression tous les 10,000 tests
        if tested % 10000 == 0:
            elapsed = time.time() - start_time
            speed = tested / elapsed
            print(f"   Progression: {tested:,} testés ({speed:,.0f}/sec)")

    print(f"\n   ÉCHOUÉ: Mot de passe non trouvé après {tested:,} tentatives")
    return None


# =============================================================================
# PARTIE 3 : ATTAQUE PAR DICTIONNAIRE (DICTIONARY ATTACK)
# =============================================================================

def generate_simple_wordlist(size: int = 1000) -> List[str]:
    """
    Générer une simple wordlist pour la démo
    En production, vous utiliseriez rockyou.txt (14 millions de mots)

    Args:
        size: Nombre de mots à générer

    Returns:
        Liste de mots courants
    """
    # Les mots les plus courants selon les études
    common_words = [
        "password", "123456", "12345678", "qwerty", "abc123",
        "monkey", "1234567", "letmein", "dragon", "111111",
        "123123", "football", "baseball", "princess", "master",
        "iloveyou", "michael", "jordan", "friends", "ashley",
        "welcome", "admin", "pass", "login", "root",
        "test", "security", "secret", "freedom", "hello",
        "sunshine", "password123", "2023", "2024", "2025",
    ]

    # Ajouter des variations
    variations = []
    for word in common_words[:20]:  # Premiers 20 mots
        variations.append(word)
        variations.append(word.capitalize())
        variations.append(word.upper())
        variations.append(word + "123")
        variations.append(word + "!")
        variations.append("1" + word)

    # Ajouter des chiffres courants (années, dates)
    for year in range(2020, 2026):
        variations.append(str(year))
        variations.append("pass" + str(year))
        variations.append("password" + str(year))

    # Limiter au nombre demandé
    wordlist = list(set(variations))[:size]
    return sorted(wordlist)


def dictionary_attack(
    target_hash: str,
    wordlist: Optional[List[str]] = None,
    hash_type: str = "sha256",
    rate_limit: float = 0.0
) -> Optional[str]:
    """
    Attaque par dictionnaire: tester une liste prédéfinie de mots de passe
    Bien plus rapide et efficace contre les mots de passe courants

    Args:
        target_hash: Le hash à cracker
        wordlist: Liste de mots de passe à tester (défaut: générer simple list)
        hash_type: Type de hash (md5, sha1, sha256, sha512)
        rate_limit: Délai entre les tests en secondes (défaut: 0.0 = no limit)

    Returns:
        Le mot de passe trouvé, ou None si pas trouvé

    Efficacité réelle:
        - rockyou.txt (14M mots): Craque ~80% des mots de passe en 1-2 minutes
        - Avec variations: Craque ~95% en 5-10 minutes
        - Très rapide comparé au brute force
    """
    if wordlist is None:
        wordlist = generate_simple_wordlist(1000)

    print(f"\n--- ATTAQUE PAR DICTIONNAIRE ---")
    print(f"   Hash cible: {target_hash[:32]}...")
    print(f"   Type: {hash_type}")
    print(f"   Taille de wordlist: {len(wordlist):,} mots de passe")
    if rate_limit > 0:
        print(f"   Rate limiting: {1/rate_limit:.1f} mots de passe/seconde")

    start_time = time.time()
    tested = 0

    # Tester chaque mot de passe de la wordlist
    for password in wordlist:
        # Appliquer le rate limiting si configuré
        if rate_limit > 0:
            time.sleep(rate_limit)

        # Calculer le hash du candidat
        if hash_type == "md5":
            candidate_hash = hashlib.md5(password.encode()).hexdigest()
        elif hash_type == "sha1":
            candidate_hash = hashlib.sha1(password.encode()).hexdigest()
        elif hash_type == "sha256":
            candidate_hash = hashlib.sha256(password.encode()).hexdigest()
        elif hash_type == "sha512":
            candidate_hash = hashlib.sha512(password.encode()).hexdigest()

        tested += 1

        # Vérifier s'il correspond au hash cible
        if candidate_hash == target_hash:
            elapsed = time.time() - start_time
            print(f"\n   SUCCESS! Mot de passe trouvé: {password}")
            print(f"   Tentatives: {tested:,}/{len(wordlist):,}")
            print(f"   Temps: {elapsed:.2f} secondes")
            if elapsed > 0:
                print(f"   Vitesse: {tested/elapsed:,.0f} mots de passe/seconde")
            return password

        # Afficher la progression tous les 100 tests
        if tested % 100 == 0:
            elapsed = time.time() - start_time
            if elapsed > 0:
                speed = tested / elapsed
                progress = (tested / len(wordlist)) * 100
                print(f"   Progression: {progress:5.1f}% ({tested:,}/{len(wordlist):,}) "
                      f"- {speed:,.0f}/sec")

    elapsed = time.time() - start_time
    print(f"\n   ÉCHOUÉ: Mot de passe non trouvé après {tested:,} tentatives")
    if elapsed > 0:
        print(f"   Temps total: {elapsed:.2f} secondes")
    return None


# =============================================================================
# PARTIE 4 : HASH CRACKING AVEC HASHLIB
# =============================================================================

def crack_hash_with_wordlist(
    target_hash: str,
    wordlist: List[str],
    hash_type: str = "sha256"
) -> Tuple[Optional[str], int, float]:
    """
    Cracker un hash en utilisant une wordlist et hashlib
    Retourne le mot de passe et les statistiques

    Args:
        target_hash: Le hash à cracker
        wordlist: Liste de mots de passe à tester
        hash_type: Type de hash (md5, sha1, sha256, sha512)

    Returns:
        Tuple (mot_de_passe, tentatives, temps_secondes)

    Exemple:
        >>> wordlist = ['password', 'test123', 'admin']
        >>> password = 'test123'
        >>> hash_val = hashlib.sha256(password.encode()).hexdigest()
        >>> result, attempts, elapsed = crack_hash_with_wordlist(hash_val, wordlist)
        >>> print(result)  # Affiche: test123
    """
    start_time = time.time()
    tested = 0

    for word in wordlist:
        # Obtenir la fonction hash appropriée
        hash_func = getattr(hashlib, hash_type)
        candidate_hash = hash_func(word.encode()).hexdigest()

        tested += 1

        # Vérifier la correspondance
        if candidate_hash == target_hash:
            elapsed = time.time() - start_time
            return word, tested, elapsed

    elapsed = time.time() - start_time
    return None, tested, elapsed


# =============================================================================
# PARTIE 5 : MULTI-THREADING POUR ACCÉLÉRATION
# =============================================================================

class MultiThreadedCracker:
    """
    Classe pour cracker les mots de passe en utilisant le multi-threading
    Permet une parallélisation efficace des tests

    Architecture:
        - Main thread: Distribue les mots et collecte les résultats
        - Worker threads: Testent les mots de passe en parallèle
        - Queue thread-safe: Communication entre les threads

    Performance typique:
        - 1 thread: Baseline (1.0x)
        - 2 threads: ~1.9x speedup
        - 4 threads: ~3.7x speedup
        - 8 threads: ~6.5x speedup (décrochage limité par I/O)
    """

    def __init__(self, target_hash: str, hash_type: str = "sha256", num_threads: int = 4):
        """
        Initialiser le cracker multi-threadé

        Args:
            target_hash: Le hash à cracker
            hash_type: Type de hash (md5, sha1, sha256, sha512)
            num_threads: Nombre de threads à utiliser
        """
        self.target_hash = target_hash
        self.hash_type = hash_type
        self.num_threads = num_threads
        self.found_password = None
        self.found_event = threading.Event()  # Signal pour arrêter les autres threads
        self.total_tested = 0
        self.total_tested_lock = threading.Lock()  # Protéger l'accès à total_tested
        self.start_time = None

    def worker(self, wordlist: List[str], thread_id: int):
        """
        Fonction exécutée par chaque worker thread
        Teste une portion de la wordlist

        Args:
            wordlist: La liste complète de mots de passe
            thread_id: Identificateur du thread (pour le logging)
        """
        # Calculer quelle portion du wordlist ce thread doit tester
        words_per_thread = len(wordlist) // self.num_threads
        start_idx = thread_id * words_per_thread
        end_idx = (thread_id + 1) * words_per_thread if thread_id < self.num_threads - 1 else len(wordlist)

        print(f"   Thread {thread_id}: Testant mots {start_idx:,} à {end_idx:,}")

        # Tester les mots assignés à ce thread
        for i in range(start_idx, end_idx):
            # Si le mot de passe a déjà été trouvé, arrêter
            if self.found_event.is_set():
                break

            word = wordlist[i]

            # Calculer le hash
            hash_func = getattr(hashlib, self.hash_type)
            candidate_hash = hash_func(word.encode()).hexdigest()

            # Incrémenter le compteur de manière thread-safe
            with self.total_tested_lock:
                self.total_tested += 1

            # Vérifier la correspondance
            if candidate_hash == self.target_hash:
                self.found_password = word
                self.found_event.set()  # Signal aux autres threads d'arrêter
                print(f"   Thread {thread_id}: MOT DE PASSE TROUVÉ: {word}")
                break

    def crack(self, wordlist: List[str]) -> Tuple[Optional[str], int, float, Dict]:
        """
        Lancer l'attaque multi-threadée

        Args:
            wordlist: Liste de mots de passe à tester

        Returns:
            Tuple (mot_de_passe, tentatives, temps, statistiques)
        """
        self.start_time = time.time()
        self.total_tested = 0
        self.found_password = None
        self.found_event.clear()

        print(f"\n--- ATTAQUE MULTI-THREADED (HashType: {self.hash_type}) ---")
        print(f"   Nombre de threads: {self.num_threads}")
        print(f"   Taille de wordlist: {len(wordlist):,}")

        # Créer et démarrer les threads
        threads = []
        for i in range(self.num_threads):
            thread = threading.Thread(
                target=self.worker,
                args=(wordlist, i),
                daemon=False
            )
            threads.append(thread)
            thread.start()

        # Attendre que tous les threads se terminent
        for thread in threads:
            thread.join()

        elapsed = time.time() - self.start_time
        stats = {
            "threads_used": self.num_threads,
            "total_attempted": self.total_tested,
            "speedup": self.total_tested / elapsed / 100,  # Estimation rude
            "found": self.found_password is not None
        }

        return self.found_password, self.total_tested, elapsed, stats


# =============================================================================
# PARTIE 6 : RATE LIMITING ÉTHIQUE
# =============================================================================

class RateLimitedCracker:
    """
    Classe pour cracker les mots de passe avec rate limiting
    Simule les limites de sécurité des systèmes réels

    Exemple réel:
        - Sans rate limiting: 1 million mots de passe en 1 seconde (irréaliste)
        - Avec 0.1s par tentative: 1 million mots de passe en 100,000 secondes (~27h)

    Sécurité réelle:
        - Après 3-5 tentatives échouées: Compte verrouillé pendant 15-30 minutes
        - Délai croissant: 1s, 5s, 1min, 1h, 24h
        - MFA après 1-2 essais incorrects
    """

    def __init__(
        self,
        max_attempts_per_second: float = 10,
        lockout_threshold: int = 5,
        lockout_duration: float = 60
    ):
        """
        Initialiser le cracker avec rate limiting

        Args:
            max_attempts_per_second: Nombre max de tentatives par seconde
            lockout_threshold: Nombre d'échecs avant verrouillage
            lockout_duration: Durée du verrouillage en secondes
        """
        self.delay_between_attempts = 1.0 / max_attempts_per_second
        self.lockout_threshold = lockout_threshold
        self.lockout_duration = lockout_duration
        self.failed_attempts = {}
        self.locked_accounts = {}

    def try_password(
        self,
        username: str,
        password: str,
        correct_password: str
    ) -> Tuple[bool, str]:
        """
        Tenter un mot de passe avec rate limiting

        Args:
            username: Nom d'utilisateur
            password: Mot de passe à tester
            correct_password: Le mot de passe correct

        Returns:
            Tuple (succès, message)
        """
        # Vérifier si le compte est verrouillé
        if username in self.locked_accounts:
            lock_time, lock_duration = self.locked_accounts[username]
            if time.time() - lock_time < lock_duration:
                remaining = lock_duration - (time.time() - lock_time)
                return False, f"Compte verrouillé ({remaining:.1f}s restantes)"
            else:
                # Déverrouiller le compte
                del self.locked_accounts[username]
                self.failed_attempts[username] = 0

        # Appliquer le délai
        time.sleep(self.delay_between_attempts)

        # Tester le mot de passe
        if password == correct_password:
            # Succès: reset les tentatives échouées
            if username in self.failed_attempts:
                del self.failed_attempts[username]
            return True, "Authentification réussie"
        else:
            # Échec: incrémenter le compteur
            self.failed_attempts[username] = self.failed_attempts.get(username, 0) + 1

            # Vérifier le seuil de verrouillage
            if self.failed_attempts[username] >= self.lockout_threshold:
                self.locked_accounts[username] = (time.time(), self.lockout_duration)
                return False, f"Compte verrouillé ({self.lockout_duration:.0f}s)"

            remaining_attempts = self.lockout_threshold - self.failed_attempts[username]
            return False, f"Mot de passe incorrect ({remaining_attempts} tentatives restantes)"


def demonstrate_rate_limiting():
    """
    Démonstration du rate limiting éthique
    """
    print(f"\n--- DÉMONSTRATION DU RATE LIMITING ---")

    cracker = RateLimitedCracker(
        max_attempts_per_second=5,  # 5 tentatives par seconde = 0.2s par tentative
        lockout_threshold=3,         # Verrouillage après 3 échecs
        lockout_duration=10          # Verrouillage de 10 secondes
    )

    username = "user@example.com"
    correct_password = "SecurePass123!"
    test_passwords = ["wrong1", "wrong2", "wrong3", "SecurePass123!", "another"]

    print(f"   Compte: {username}")
    print(f"   Mot de passe correct: {correct_password}")
    print(f"   Max tentatives: {cracker.lockout_threshold}")
    print(f"   Délai par tentative: {cracker.delay_between_attempts:.3f}s\n")

    # Tenter chaque mot de passe
    for password in test_passwords:
        success, message = cracker.try_password(username, password, correct_password)
        status = "SUCCESS" if success else "FAILED"
        print(f"   Tentative: '{password}' → {status}: {message}")

        # Pas de délai supplémentaire pour la démo
        if status == "FAILED" and "verrouillé" in message.lower():
            print(f"   Attente de déverrouillage...")
            time.sleep(1)


# =============================================================================
# PARTIE 7 : WORDLIST GENERATION
# =============================================================================

def generate_comprehensive_wordlist(include_variations: bool = True) -> List[str]:
    """
    Générer une wordlist complète pour une attaque par dictionnaire

    Args:
        include_variations: Inclure les variations (majuscules, chiffres, etc.)

    Returns:
        Liste de mots de passe
    """
    # Mots de base (les plus courants selon les études)
    base_words = [
        "password", "123456", "12345678", "qwerty", "abc123",
        "monkey", "1234567", "letmein", "dragon", "111111",
        "123123", "football", "baseball", "princess", "master",
        "iloveyou", "welcome", "admin", "root", "test",
        "security", "secret", "freedom", "hello", "sunshine",
        "michael", "jordan", "ashley", "friends", "soccer",
    ]

    wordlist = []

    if include_variations:
        # Ajouter des variations pour chaque mot
        for word in base_words:
            wordlist.append(word)
            wordlist.append(word.capitalize())
            wordlist.append(word.upper())
            wordlist.append(word + "123")
            wordlist.append(word + "1234")
            wordlist.append(word + "!")
            wordlist.append(word + "2024")
            wordlist.append(word + "2025")

        # Ajouter des années couantes
        for year in range(2020, 2026):
            wordlist.append(str(year))
            wordlist.append("pass" + str(year))

        # Ajouter des patterns courants
        for num in [1, 12, 123, 1234, 12345]:
            wordlist.append(f"{num}")
            wordlist.append(f"pass{num}")
            wordlist.append(f"admin{num}")

    else:
        wordlist = base_words

    # Supprimer les doublons et trier
    wordlist = sorted(list(set(wordlist)))
    return wordlist


# =============================================================================
# PARTIE 8 : STATISTIQUES ET BENCHMARK
# =============================================================================

def benchmark_hash_algorithms():
    """
    Comparer la vitesse des différents algorithmes de hash
    Plus rapide = plus vulnérable aux attaques!
    """
    print(f"\n--- BENCHMARK DES ALGORITHMES DE HASH ---")

    # Mots de passe à tester
    passwords = [f"password{i}" for i in range(1000)]
    algorithms = ["md5", "sha1", "sha256", "sha512"]

    results = {}

    for algo in algorithms:
        start = time.time()
        for password in passwords:
            hash_func = getattr(hashlib, algo)
            hash_func(password.encode()).hexdigest()
        elapsed = time.time() - start

        speed = len(passwords) / elapsed
        results[algo] = {
            "time": elapsed,
            "speed": speed,
        }

        print(f"   {algo.upper():8} - Temps: {elapsed:.3f}s - Vitesse: {speed:,.0f} hashs/sec")

    # Comparaison relative
    md5_speed = results["md5"]["speed"]
    print(f"\n   Relativement à MD5 (1.0x):")
    for algo in algorithms[1:]:
        ratio = results[algo]["speed"] / md5_speed
        print(f"   {algo.upper()}: {ratio:.2f}x plus lent")

    print(f"\n   Conclusion:")
    print(f"   - MD5 est le plus rapide (VULNÉRABLE aux attaques)")
    print(f"   - SHA512 est ~10x plus lent (PLUS SÛRE)")
    print(f"   - Plus lent = Plus difficile à cracker")


def analyze_attack_efficiency():
    """
    Analyser l'efficacité relative des différentes techniques
    """
    print(f"\n--- ANALYSE D'EFFICACITÉ DES ATTAQUES ---")

    stats = {
        "Brute Force (4 chars)": {
            "attempts": 1_679_616,
            "time_sec": 25,
            "success_rate": "50% (si mot de passe dans la plage)",
        },
        "Dictionary (rockyou)": {
            "attempts": 14_000_000,
            "time_sec": 15,
            "success_rate": "80% (mots de passe faibles)",
        },
        "Dictionary + Variations": {
            "attempts": 42_000_000,
            "time_sec": 45,
            "success_rate": "95% (mots de passe normaux)",
        },
        "GPU Cracking (MD5)": {
            "attempts": 350_000_000,
            "time_sec": 1,
            "success_rate": "80% (MD5 seulement)",
        },
    }

    print(f"\n   Technique                          Tentatives    Temps    Succès")
    print(f"   {'─' * 75}")
    for technique, data in stats.items():
        attempts = f"{data['attempts']:,}".rjust(15)
        time_val = f"{data['time_sec']}s".rjust(8)
        success = data['success_rate'].rjust(25)
        print(f"   {technique:30} {attempts:>15} {time_val:>8} {success:>25}")

    print(f"\n   Recommandations de sécurité:")
    print(f"   - Utiliser bcrypt ou argon2 (résistent aux GPU)")
    print(f"   - Imposer des mots de passe forts (8+ caractères aléatoires)")
    print(f"   - Implémenter le rate limiting et le lockout")
    print(f"   - MFA pour les comptes sensibles")


# =============================================================================
# PARTIE 9 : FONCTION PRINCIPALE - DÉMO COMPLÈTE
# =============================================================================

def main():
    """
    Démonstration complète des techniques de password cracking
    """
    print("\n" + "="*70)
    print("EXERCICE 20 : PASSWORD CRACKER - DÉMONSTRATION COMPLÈTE")
    print("="*70)

    print("\n[AVERTISSEMENT LÉGAL]")
    print("Ces techniques sont destinées à l'apprentissage et aux tests autorisés.")
    print("Cracker uniquement vos propres mots de passe.")
    print("L'utilisation sans autorisation est ILLÉGALE et peut entraîner:")
    print("- Des poursuites criminelles")
    print("- Des amendes substantielles")
    print("- La prison")
    print("")

    # PARTIE 1 : Concepts de base du hashing
    introduction_hashing()

    # PARTIE 2 : Brute force simple
    input("\n[Appuyez sur Entrée pour passer à BRUTE FORCE ATTACK]")
    print("\nBrute force: Test exhaustif de tous les mots de passe possibles")
    password = "abc1"
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    print(f"Hash cible (SHA256 de '{password}'): {password_hash}")
    found = brute_force_attack(password_hash, "sha256")

    # PARTIE 3 : Dictionary attack
    input("\n[Appuyez sur Entrée pour passer à DICTIONARY ATTACK]")
    print("\nDictionary attack: Test d'une liste prédéfinie de mots de passe")
    password = "password123"
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    print(f"Hash cible (SHA256 de '{password}'): {password_hash}")
    wordlist = generate_comprehensive_wordlist(include_variations=True)
    found = dictionary_attack(password_hash, wordlist, "sha256")

    # PARTIE 4 : Multi-threading
    input("\n[Appuyez sur Entrée pour passer à MULTI-THREADING]")
    print("\nMulti-threading: Accélération par parallélisation")
    password = "secret"
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    print(f"Hash cible (SHA256 de '{password}'): {password_hash}")

    # Tester avec 1, 2, et 4 threads
    wordlist = generate_comprehensive_wordlist(include_variations=True)
    for num_threads in [1, 2, 4]:
        cracker = MultiThreadedCracker(password_hash, "sha256", num_threads=num_threads)
        found_pass, attempts, elapsed, stats = cracker.crack(wordlist)
        if found_pass:
            print(f"   ✓ Trouvé avec {num_threads} thread(s): {found_pass}")
        else:
            print(f"   ✗ Non trouvé avec {num_threads} thread(s)")

    # PARTIE 5 : Rate limiting
    input("\n[Appuyez sur Entrée pour passer à RATE LIMITING]")
    demonstrate_rate_limiting()

    # PARTIE 6 : Benchmark et analyse
    input("\n[Appuyez sur Entrée pour passer aux BENCHMARKS]")
    benchmark_hash_algorithms()
    analyze_attack_efficiency()

    print("\n" + "="*70)
    print("FIN DE LA DÉMONSTRATION")
    print("="*70)
    print("\nPour plus d'informations:")
    print("- Lire README.md pour les concepts détaillés")
    print("- Consulter exercice.txt pour les défis à relever")
    print("- Voir solution.txt pour les solutions proposées")


if __name__ == "__main__":
    main()
