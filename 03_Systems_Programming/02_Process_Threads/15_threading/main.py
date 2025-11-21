#!/usr/bin/env python3
"""
Exercice 15 : Threading en Python
Démonstration complète du module threading avec applications en cybersécurité
"""

import threading
import time
import socket
from queue import Queue
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Tuple, Optional
import itertools
import string

# =============================================================================
# PARTIE 1 : CONCEPTS DE BASE DU THREADING
# =============================================================================

def introduction_threading():
    """
    Introduction aux concepts de base du threading
    """
    print("\n" + "="*60)
    print("PARTIE 1 : CONCEPTS DE BASE DU THREADING")
    print("="*60)

    # Fonction simple pour un thread
    def tache_simple(nom: str, duree: int):
        """
        Fonction simple exécutée dans un thread

        Args:
            nom: Nom de la tâche
            duree: Durée de la tâche en secondes
        """
        print(f"[{nom}] Début de la tâche")
        time.sleep(duree)
        print(f"[{nom}] Fin de la tâche après {duree}s")

    # Création et démarrage d'un thread simple
    print("\n1. Création d'un thread simple:")
    thread1 = threading.Thread(target=tache_simple, args=("Thread-1", 2))
    print(f"   Thread créé: {thread1.name}")
    print(f"   Est vivant? {thread1.is_alive()}")

    # Démarrage du thread
    thread1.start()
    print(f"   Thread démarré, est vivant? {thread1.is_alive()}")

    # Attendre la fin du thread
    thread1.join()
    print(f"   Thread terminé, est vivant? {thread1.is_alive()}")

    # Création de plusieurs threads
    print("\n2. Création de plusieurs threads:")
    threads = []
    for i in range(3):
        t = threading.Thread(
            target=tache_simple,
            args=(f"Worker-{i+1}", i+1),
            name=f"CustomThread-{i+1}"
        )
        threads.append(t)
        t.start()

    # Attendre tous les threads
    print("   Attente de tous les threads...")
    for t in threads:
        t.join()
    print("   Tous les threads sont terminés")


def threading_avec_classe():
    """
    Démonstration de l'utilisation de la classe Thread
    """
    print("\n" + "="*60)
    print("PARTIE 2 : UTILISATION DE LA CLASSE THREAD")
    print("="*60)

    # Classe personnalisée héritant de Thread
    class MonThread(threading.Thread):
        """
        Thread personnalisé avec attributs et méthode run()
        """
        def __init__(self, nom: str, compteur: int):
            super().__init__()
            self.nom = nom
            self.compteur = compteur
            self.resultat = 0

        def run(self):
            """
            Méthode exécutée lors du démarrage du thread
            """
            print(f"[{self.nom}] Démarrage du comptage")
            for i in range(self.compteur):
                self.resultat += i
                time.sleep(0.1)
            print(f"[{self.nom}] Comptage terminé: {self.resultat}")

    # Création et utilisation de threads personnalisés
    print("\n1. Threads personnalisés:")
    threads = []
    for i in range(3):
        t = MonThread(f"Counter-{i+1}", (i+1)*5)
        threads.append(t)
        t.start()

    # Récupération des résultats
    for t in threads:
        t.join()
        print(f"   Résultat de {t.nom}: {t.resultat}")

    # Informations sur les threads
    print("\n2. Informations sur les threads:")
    print(f"   Thread courant: {threading.current_thread().name}")
    print(f"   Nombre de threads actifs: {threading.active_count()}")
    print(f"   Liste des threads actifs:")
    for thread in threading.enumerate():
        print(f"      - {thread.name} (daemon: {thread.daemon})")


# =============================================================================
# PARTIE 3 : ARGUMENTS ET PASSAGE DE DONNÉES
# =============================================================================

def arguments_et_donnees():
    """
    Démonstration du passage d'arguments aux threads
    """
    print("\n" + "="*60)
    print("PARTIE 3 : ARGUMENTS ET PASSAGE DE DONNÉES")
    print("="*60)

    # Fonction avec arguments positionnels et nommés
    def traiter_donnees(identifiant: int, nom: str, verbose: bool = False):
        """
        Fonction avec arguments variés
        """
        if verbose:
            print(f"[Thread-{identifiant}] Traitement de {nom}")
        time.sleep(0.5)
        return f"Résultat-{identifiant}"

    # Arguments positionnels
    print("\n1. Arguments positionnels:")
    t1 = threading.Thread(target=traiter_donnees, args=(1, "DataA", True))
    t1.start()
    t1.join()

    # Arguments nommés
    print("\n2. Arguments nommés:")
    t2 = threading.Thread(
        target=traiter_donnees,
        kwargs={"identifiant": 2, "nom": "DataB", "verbose": True}
    )
    t2.start()
    t2.join()

    # Mélange d'arguments
    print("\n3. Mélange d'arguments:")
    t3 = threading.Thread(
        target=traiter_donnees,
        args=(3, "DataC"),
        kwargs={"verbose": True}
    )
    t3.start()
    t3.join()


# =============================================================================
# PARTIE 4 : SYNCHRONISATION AVEC LOCK
# =============================================================================

def synchronisation_lock():
    """
    Démonstration de la synchronisation avec Lock
    """
    print("\n" + "="*60)
    print("PARTIE 4 : SYNCHRONISATION AVEC LOCK")
    print("="*60)

    # Problème : Race condition sans Lock
    print("\n1. Race condition (sans Lock):")
    compteur_unsafe = 0

    def incrementer_unsafe():
        """
        Incrémentation non thread-safe
        """
        nonlocal compteur_unsafe
        for _ in range(100000):
            compteur_unsafe += 1

    threads = []
    for _ in range(5):
        t = threading.Thread(target=incrementer_unsafe)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(f"   Compteur final (attendu: 500000): {compteur_unsafe}")
    print(f"   Différence: {500000 - compteur_unsafe}")

    # Solution : Utilisation de Lock
    print("\n2. Solution avec Lock:")
    compteur_safe = 0
    lock = threading.Lock()

    def incrementer_safe():
        """
        Incrémentation thread-safe avec Lock
        """
        nonlocal compteur_safe
        for _ in range(100000):
            with lock:  # Contexte manager pour acquérir/libérer le lock
                compteur_safe += 1

    threads = []
    for _ in range(5):
        t = threading.Thread(target=incrementer_safe)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(f"   Compteur final (attendu: 500000): {compteur_safe}")
    print(f"   Différence: {500000 - compteur_safe}")

    # Lock avec acquire/release manuel
    print("\n3. Lock avec acquire/release manuel:")
    ressource_partagee = []

    def ajouter_donnee(donnee: str):
        """
        Ajout thread-safe avec gestion manuelle du Lock
        """
        lock.acquire()
        try:
            ressource_partagee.append(donnee)
            print(f"   Ajouté: {donnee}")
        finally:
            lock.release()  # Toujours libérer le lock

    threads = []
    for i in range(5):
        t = threading.Thread(target=ajouter_donnee, args=(f"Item-{i}",))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(f"   Ressource finale: {ressource_partagee}")


# =============================================================================
# PARTIE 5 : SYNCHRONISATION AVEC SEMAPHORE
# =============================================================================

def synchronisation_semaphore():
    """
    Démonstration de la synchronisation avec Semaphore
    """
    print("\n" + "="*60)
    print("PARTIE 5 : SYNCHRONISATION AVEC SEMAPHORE")
    print("="*60)

    # Semaphore pour limiter les accès concurrents
    print("\n1. Limiter les accès concurrents:")
    semaphore = threading.Semaphore(3)  # Max 3 threads simultanés

    def acceder_ressource_limitee(identifiant: int):
        """
        Accès à une ressource avec nombre limité de connexions
        """
        print(f"   [Thread-{identifiant}] Tentative d'accès...")
        with semaphore:
            print(f"   [Thread-{identifiant}] Accès accordé")
            time.sleep(1)  # Simulation de travail
            print(f"   [Thread-{identifiant}] Libération de la ressource")

    threads = []
    for i in range(10):
        t = threading.Thread(target=acceder_ressource_limitee, args=(i,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    # BoundedSemaphore pour éviter les libérations excessives
    print("\n2. BoundedSemaphore:")
    bounded_sem = threading.BoundedSemaphore(2)

    def utiliser_bounded_semaphore(identifiant: int):
        """
        Utilisation de BoundedSemaphore
        """
        bounded_sem.acquire()
        print(f"   [Thread-{identifiant}] Ressource acquise")
        time.sleep(0.5)
        bounded_sem.release()
        print(f"   [Thread-{identifiant}] Ressource libérée")

    threads = []
    for i in range(5):
        t = threading.Thread(target=utiliser_bounded_semaphore, args=(i,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()


# =============================================================================
# PARTIE 6 : AUTRES PRIMITIVES DE SYNCHRONISATION
# =============================================================================

def autres_primitives():
    """
    Démonstration d'autres primitives de synchronisation
    """
    print("\n" + "="*60)
    print("PARTIE 6 : AUTRES PRIMITIVES DE SYNCHRONISATION")
    print("="*60)

    # Event : Signal entre threads
    print("\n1. Event (signalisation entre threads):")
    event = threading.Event()

    def attendre_signal(identifiant: int):
        """
        Thread qui attend un signal
        """
        print(f"   [Worker-{identifiant}] En attente du signal...")
        event.wait()  # Bloque jusqu'à ce que l'event soit set
        print(f"   [Worker-{identifiant}] Signal reçu, début du travail")

    # Créer les threads en attente
    threads = []
    for i in range(3):
        t = threading.Thread(target=attendre_signal, args=(i,))
        t.start()
        threads.append(t)

    time.sleep(1)
    print("   [Main] Envoi du signal...")
    event.set()  # Libérer tous les threads en attente

    for t in threads:
        t.join()

    # RLock : Lock réentrant
    print("\n2. RLock (Lock réentrant):")
    rlock = threading.RLock()

    def fonction_recursive(niveau: int):
        """
        Fonction récursive utilisant RLock
        """
        with rlock:
            print(f"   Niveau {niveau}")
            if niveau > 0:
                fonction_recursive(niveau - 1)

    t = threading.Thread(target=fonction_recursive, args=(3,))
    t.start()
    t.join()

    # Condition : Synchronisation complexe
    print("\n3. Condition (synchronisation complexe):")
    condition = threading.Condition()
    items = []

    def producteur():
        """
        Thread producteur
        """
        for i in range(5):
            time.sleep(0.5)
            with condition:
                items.append(f"Item-{i}")
                print(f"   [Producteur] Produit: Item-{i}")
                condition.notify()  # Notifier les consommateurs

    def consommateur(identifiant: int):
        """
        Thread consommateur
        """
        while True:
            with condition:
                while not items:
                    condition.wait()  # Attendre un item
                item = items.pop(0)
                print(f"   [Consommateur-{identifiant}] Consommé: {item}")
                if "Item-4" in item:
                    break

    prod = threading.Thread(target=producteur)
    cons1 = threading.Thread(target=consommateur, args=(1,))
    cons2 = threading.Thread(target=consommateur, args=(2,))

    cons1.start()
    cons2.start()
    prod.start()

    prod.join()
    cons1.join()
    cons2.join()


# =============================================================================
# PARTIE 7 : THREAD POOL ET CONCURRENT.FUTURES
# =============================================================================

def thread_pool_executor():
    """
    Démonstration de ThreadPoolExecutor
    """
    print("\n" + "="*60)
    print("PARTIE 7 : THREAD POOL ET CONCURRENT.FUTURES")
    print("="*60)

    def tache_longue(identifiant: int) -> int:
        """
        Tâche simulant un traitement long
        """
        time.sleep(1)
        resultat = identifiant * 2
        print(f"   [Tâche-{identifiant}] Résultat: {resultat}")
        return resultat

    # Utilisation basique de ThreadPoolExecutor
    print("\n1. ThreadPoolExecutor basique:")
    with ThreadPoolExecutor(max_workers=3) as executor:
        # Submit pour soumettre des tâches
        futures = [executor.submit(tache_longue, i) for i in range(5)]

        # Récupérer les résultats
        resultats = [f.result() for f in futures]

    print(f"   Résultats: {resultats}")

    # Map pour traiter une liste
    print("\n2. ThreadPoolExecutor avec map:")
    with ThreadPoolExecutor(max_workers=3) as executor:
        resultats = list(executor.map(tache_longue, range(5)))

    print(f"   Résultats: {resultats}")

    # as_completed pour traiter les résultats au fur et à mesure
    print("\n3. ThreadPoolExecutor avec as_completed:")
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = {executor.submit(tache_longue, i): i for i in range(5)}

        for future in as_completed(futures):
            original_id = futures[future]
            try:
                resultat = future.result()
                print(f"   Tâche {original_id} terminée avec résultat: {resultat}")
            except Exception as e:
                print(f"   Tâche {original_id} a échoué: {e}")


# =============================================================================
# PARTIE 8 : QUEUE THREAD-SAFE
# =============================================================================

def queue_thread_safe():
    """
    Démonstration de Queue pour la communication thread-safe
    """
    print("\n" + "="*60)
    print("PARTIE 8 : QUEUE THREAD-SAFE")
    print("="*60)

    # Queue FIFO
    print("\n1. Queue FIFO (First In First Out):")
    queue = Queue()

    def producteur_queue(identifiant: int, q: Queue):
        """
        Producteur qui ajoute des items dans la queue
        """
        for i in range(3):
            item = f"P{identifiant}-Item{i}"
            q.put(item)
            print(f"   [Producteur-{identifiant}] Ajouté: {item}")
            time.sleep(0.3)
        q.put(None)  # Signal de fin

    def consommateur_queue(identifiant: int, q: Queue):
        """
        Consommateur qui traite les items de la queue
        """
        while True:
            item = q.get()
            if item is None:
                q.task_done()
                break
            print(f"   [Consommateur-{identifiant}] Traité: {item}")
            time.sleep(0.5)
            q.task_done()

    # Créer producteurs et consommateurs
    producteurs = [
        threading.Thread(target=producteur_queue, args=(i, queue))
        for i in range(2)
    ]
    consommateurs = [
        threading.Thread(target=consommateur_queue, args=(i, queue))
        for i in range(2)
    ]

    # Démarrer tous les threads
    for p in producteurs:
        p.start()
    for c in consommateurs:
        c.start()

    # Attendre les producteurs
    for p in producteurs:
        p.join()

    # Attendre que la queue soit vide
    queue.join()

    # Arrêter les consommateurs
    for _ in consommateurs:
        queue.put(None)
    for c in consommateurs:
        c.join()


# =============================================================================
# PARTIE 9 : APPLICATIONS RED TEAMING - SCAN DE PORTS
# =============================================================================

def scanner_ports_multithread():
    """
    Scanner de ports multi-threadé
    ATTENTION: À utiliser uniquement sur des systèmes autorisés
    """
    print("\n" + "="*60)
    print("PARTIE 9 : SCANNER DE PORTS MULTI-THREADÉ")
    print("="*60)

    def scan_port(host: str, port: int, timeout: float = 0.5) -> Optional[int]:
        """
        Scanne un port spécifique

        Args:
            host: Adresse IP ou hostname
            port: Numéro de port
            timeout: Timeout de connexion

        Returns:
            Numéro de port si ouvert, None sinon
        """
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex((host, port))
            sock.close()

            if result == 0:
                return port
            return None
        except socket.error:
            return None

    def scanner_range(host: str, start_port: int, end_port: int, threads: int = 50):
        """
        Scanne une plage de ports avec threading

        Args:
            host: Adresse cible
            start_port: Port de début
            end_port: Port de fin
            threads: Nombre de threads
        """
        print(f"\n   Scan de {host}:{start_port}-{end_port} avec {threads} threads")
        ports_ouverts = []
        lock = threading.Lock()

        def worker(port: int):
            """
            Worker pour scanner un port
            """
            result = scan_port(host, port)
            if result:
                with lock:
                    ports_ouverts.append(result)
                    print(f"   [+] Port {result} ouvert")

        # Utiliser ThreadPoolExecutor pour gérer les threads
        with ThreadPoolExecutor(max_workers=threads) as executor:
            executor.map(worker, range(start_port, end_port + 1))

        return sorted(ports_ouverts)

    # Scan de ports locaux (exemple sûr)
    print("\n1. Scan de ports locaux (localhost):")
    ports_communs = [21, 22, 23, 25, 80, 443, 3306, 5432, 8080, 8443]

    ports_ouverts = []
    lock = threading.Lock()

    def scan_port_local(port: int):
        """
        Scanner de port local simplifié
        """
        result = scan_port("127.0.0.1", port, timeout=0.2)
        if result:
            with lock:
                ports_ouverts.append(result)

    threads = []
    for port in ports_communs:
        t = threading.Thread(target=scan_port_local, args=(port,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    if ports_ouverts:
        print(f"   Ports ouverts trouvés: {sorted(ports_ouverts)}")
    else:
        print("   Aucun port ouvert trouvé dans la liste")

    # Exemple avec ThreadPoolExecutor (démonstration seulement)
    print("\n2. Scan avec ThreadPoolExecutor (démonstration):")
    print("   Note: Scan désactivé pour éviter les problèmes réseau")
    print("   Dans un contexte réel et autorisé:")
    print("   ports = scanner_range('192.168.1.1', 1, 1000, threads=100)")


# =============================================================================
# PARTIE 10 : APPLICATIONS RED TEAMING - BRUTEFORCE
# =============================================================================

def bruteforce_multithread():
    """
    Bruteforce multi-threadé (démonstration)
    ATTENTION: À utiliser uniquement dans un cadre légal et autorisé
    """
    print("\n" + "="*60)
    print("PARTIE 10 : BRUTEFORCE MULTI-THREADÉ")
    print("="*60)

    # Fonction de vérification simulée
    def verifier_credential(username: str, password: str) -> bool:
        """
        Simule la vérification de credentials
        Dans un vrai cas: connexion SSH, HTTP, etc.
        """
        # Simulation d'un délai réseau
        time.sleep(0.01)

        # Credential fictif pour la démonstration
        return username == "admin" and password == "password123"

    # Bruteforce simple
    print("\n1. Bruteforce simple multi-threadé:")

    wordlist = [
        "admin", "password", "123456", "password123",
        "admin123", "root", "toor", "qwerty"
    ]

    found = threading.Event()
    found_credential = {"username": None, "password": None}
    lock = threading.Lock()

    def tester_password(username: str, password: str):
        """
        Teste un mot de passe
        """
        if found.is_set():
            return

        if verifier_credential(username, password):
            with lock:
                if not found.is_set():
                    found.set()
                    found_credential["username"] = username
                    found_credential["password"] = password
                    print(f"   [+] Credential trouvé: {username}:{password}")

    # Tester tous les mots de passe
    target_user = "admin"
    threads = []

    for password in wordlist:
        t = threading.Thread(target=tester_password, args=(target_user, password))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    if found.is_set():
        print(f"   Résultat: {found_credential['username']}:{found_credential['password']}")
    else:
        print("   Aucun credential trouvé")

    # Bruteforce avec générateur de combinaisons
    print("\n2. Bruteforce avec générateur (démonstration):")

    def generer_mots_passe(longueur: int, charset: str) -> List[str]:
        """
        Génère des mots de passe de longueur fixe

        Args:
            longueur: Longueur du mot de passe
            charset: Caractères à utiliser

        Returns:
            Liste de mots de passe
        """
        # Limiter le nombre pour la démonstration
        combinaisons = itertools.product(charset, repeat=longueur)
        passwords = [''.join(combo) for combo in itertools.islice(combinaisons, 100)]
        return passwords

    # Générer des mots de passe courts
    charset = string.ascii_lowercase[:5]  # Seulement 'abcde'
    passwords = generer_mots_passe(2, charset)

    print(f"   Génération de {len(passwords)} combinaisons")
    print(f"   Premiers exemples: {passwords[:10]}")

    # Bruteforce avec Queue
    print("\n3. Bruteforce avec Queue:")

    queue = Queue()
    found_queue = threading.Event()
    result = {"password": None}

    # Remplir la queue
    test_passwords = ["abc", "def", "xyz", "password123", "test"]
    for pwd in test_passwords:
        queue.put(pwd)

    def worker_bruteforce():
        """
        Worker qui teste les mots de passe depuis la queue
        """
        while not found_queue.is_set() and not queue.empty():
            try:
                password = queue.get(timeout=0.1)
                if verifier_credential("admin", password):
                    found_queue.set()
                    result["password"] = password
                    print(f"   [+] Password trouvé: {password}")
                queue.task_done()
            except:
                break

    # Créer les workers
    workers = []
    for _ in range(3):
        t = threading.Thread(target=worker_bruteforce)
        t.start()
        workers.append(t)

    # Attendre
    for w in workers:
        w.join()

    if result["password"]:
        print(f"   Résultat: {result['password']}")


# =============================================================================
# PARTIE 11 : APPLICATIONS RED TEAMING - ÉNUMÉRATION CONCURRENTE
# =============================================================================

def enumeration_concurrente():
    """
    Énumération concurrente de ressources
    ATTENTION: À utiliser uniquement dans un cadre légal et autorisé
    """
    print("\n" + "="*60)
    print("PARTIE 11 : ÉNUMÉRATION CONCURRENTE")
    print("="*60)

    # Simulation de vérification de ressources
    def verifier_ressource(url: str) -> Tuple[str, int]:
        """
        Simule la vérification d'une ressource web

        Returns:
            Tuple (url, code_status)
        """
        time.sleep(0.1)  # Simulation de requête réseau

        # Simulation de codes de statut
        import random
        codes = [200, 404, 403, 301, 500]
        return (url, random.choice(codes))

    # Énumération de répertoires
    print("\n1. Énumération de répertoires:")

    directories = [
        "/admin", "/backup", "/config", "/uploads",
        "/api", "/test", "/dev", "/login", "/dashboard"
    ]

    resultats = []
    lock = threading.Lock()

    def scanner_directory(base_url: str, directory: str):
        """
        Scanne un répertoire
        """
        url = f"{base_url}{directory}"
        url_complete, status = verifier_ressource(url)

        with lock:
            resultats.append((url_complete, status))
            if status in [200, 301, 302]:
                print(f"   [+] Trouvé: {url_complete} (Status: {status})")
            elif status == 403:
                print(f"   [!] Interdit: {url_complete} (Status: {status})")

    base_url = "http://example.com"
    threads = []

    for directory in directories:
        t = threading.Thread(target=scanner_directory, args=(base_url, directory))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(f"\n   Total de répertoires scannés: {len(resultats)}")

    # Énumération de sous-domaines
    print("\n2. Énumération de sous-domaines:")

    subdomains = [
        "www", "mail", "ftp", "admin", "api",
        "dev", "test", "staging", "blog", "shop"
    ]

    def verifier_subdomain(subdomain: str, domain: str) -> Optional[str]:
        """
        Simule la vérification d'un sous-domaine
        """
        time.sleep(0.05)

        # Simulation: certains sous-domaines existent
        if subdomain in ["www", "mail", "api"]:
            return f"{subdomain}.{domain}"
        return None

    domaine = "example.com"
    subdomains_trouves = []
    lock_sub = threading.Lock()

    def scanner_subdomain(subdomain: str):
        """
        Scanne un sous-domaine
        """
        result = verifier_subdomain(subdomain, domaine)
        if result:
            with lock_sub:
                subdomains_trouves.append(result)
                print(f"   [+] Sous-domaine trouvé: {result}")

    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(scanner_subdomain, subdomains)

    print(f"\n   Sous-domaines trouvés: {subdomains_trouves}")

    # Énumération d'utilisateurs
    print("\n3. Énumération d'utilisateurs:")

    usernames = [
        "admin", "root", "user", "test", "guest",
        "administrator", "support", "info", "sales"
    ]

    def verifier_user(username: str) -> bool:
        """
        Simule la vérification d'existence d'un utilisateur
        """
        time.sleep(0.05)
        return username in ["admin", "user", "support"]

    users_valides = []
    lock_user = threading.Lock()

    def enumerer_user(username: str):
        """
        Énumère un utilisateur
        """
        if verifier_user(username):
            with lock_user:
                users_valides.append(username)
                print(f"   [+] Utilisateur valide: {username}")

    threads = []
    for username in usernames:
        t = threading.Thread(target=enumerer_user, args=(username,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(f"\n   Utilisateurs valides: {users_valides}")


# =============================================================================
# PARTIE 12 : GESTION AVANCÉE ET BONNES PRATIQUES
# =============================================================================

def gestion_avancee():
    """
    Démonstration de gestion avancée des threads
    """
    print("\n" + "="*60)
    print("PARTIE 12 : GESTION AVANCÉE ET BONNES PRATIQUES")
    print("="*60)

    # Threads daemon
    print("\n1. Threads daemon:")

    def tache_normale():
        """
        Tâche normale qui s'exécute complètement
        """
        print("   [Normal] Début")
        time.sleep(2)
        print("   [Normal] Fin")

    def tache_daemon():
        """
        Tâche daemon qui peut être interrompue
        """
        print("   [Daemon] Début")
        time.sleep(5)
        print("   [Daemon] Fin (ne sera probablement pas affiché)")

    t_normal = threading.Thread(target=tache_normale)
    t_daemon = threading.Thread(target=tache_daemon, daemon=True)

    t_normal.start()
    t_daemon.start()

    t_normal.join()
    print("   Thread normal terminé, le daemon peut être interrompu")

    # Timeout sur join
    print("\n2. Timeout sur join:")

    def tache_longue():
        """
        Tâche qui prend du temps
        """
        time.sleep(3)

    t = threading.Thread(target=tache_longue)
    t.start()

    t.join(timeout=1)
    if t.is_alive():
        print("   Thread encore actif après timeout de 1s")

    t.join()  # Attendre la vraie fin
    print("   Thread finalement terminé")

    # Gestion des exceptions dans les threads
    print("\n3. Gestion des exceptions:")

    exceptions = []
    lock = threading.Lock()

    def tache_avec_erreur(identifiant: int):
        """
        Tâche qui peut générer des exceptions
        """
        try:
            if identifiant % 2 == 0:
                raise ValueError(f"Erreur dans thread {identifiant}")
            print(f"   [Thread-{identifiant}] Succès")
        except Exception as e:
            with lock:
                exceptions.append((identifiant, str(e)))
                print(f"   [Thread-{identifiant}] Exception capturée: {e}")

    threads = []
    for i in range(5):
        t = threading.Thread(target=tache_avec_erreur, args=(i,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(f"\n   Exceptions capturées: {len(exceptions)}")
    for tid, error in exceptions:
        print(f"      Thread {tid}: {error}")

    # Timer threads
    print("\n4. Timer threads:")

    def tache_retardee():
        """
        Tâche exécutée après un délai
        """
        print("   Timer déclenché!")

    timer = threading.Timer(2.0, tache_retardee)
    print("   Démarrage du timer (2 secondes)")
    timer.start()
    timer.join()


# =============================================================================
# PARTIE 13 : PERFORMANCE ET BENCHMARKING
# =============================================================================

def performance_threading():
    """
    Analyse des performances du threading
    """
    print("\n" + "="*60)
    print("PARTIE 13 : PERFORMANCE ET BENCHMARKING")
    print("="*60)

    # Tâche I/O-bound
    def tache_io_bound(n: int):
        """
        Tâche I/O-bound (bénéficie du threading)
        """
        time.sleep(0.1)  # Simulation I/O
        return n * 2

    # Tâche CPU-bound
    def tache_cpu_bound(n: int):
        """
        Tâche CPU-bound (limitée par le GIL)
        """
        result = 0
        for i in range(1000000):
            result += i
        return result

    # Test sans threading (I/O)
    print("\n1. Benchmark I/O-bound:")

    start = time.time()
    resultats = [tache_io_bound(i) for i in range(10)]
    temps_sequentiel = time.time() - start
    print(f"   Séquentiel: {temps_sequentiel:.2f}s")

    # Test avec threading (I/O)
    start = time.time()
    with ThreadPoolExecutor(max_workers=10) as executor:
        resultats = list(executor.map(tache_io_bound, range(10)))
    temps_parallel = time.time() - start
    print(f"   Parallèle (10 threads): {temps_parallel:.2f}s")
    print(f"   Amélioration: {temps_sequentiel/temps_parallel:.2f}x")

    # Test CPU-bound
    print("\n2. Benchmark CPU-bound:")

    start = time.time()
    resultats = [tache_cpu_bound(i) for i in range(4)]
    temps_seq_cpu = time.time() - start
    print(f"   Séquentiel: {temps_seq_cpu:.2f}s")

    start = time.time()
    with ThreadPoolExecutor(max_workers=4) as executor:
        resultats = list(executor.map(tache_cpu_bound, range(4)))
    temps_par_cpu = time.time() - start
    print(f"   Parallèle (4 threads): {temps_par_cpu:.2f}s")
    print(f"   Amélioration: {temps_seq_cpu/temps_par_cpu:.2f}x")
    print("   Note: Le GIL limite les performances CPU-bound")

    # Nombre optimal de threads
    print("\n3. Nombre optimal de threads (I/O-bound):")

    for num_threads in [1, 5, 10, 20, 50]:
        start = time.time()
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            list(executor.map(tache_io_bound, range(50)))
        duree = time.time() - start
        print(f"   {num_threads:2d} threads: {duree:.2f}s")


# =============================================================================
# FONCTION PRINCIPALE
# =============================================================================

def main():
    """
    Fonction principale - Exécute toutes les démonstrations
    """
    print("\n" + "="*60)
    print("EXERCICE 15 : THREADING EN PYTHON")
    print("Démonstration complète avec applications en cybersécurité")
    print("="*60)

    # Exécuter toutes les parties
    introduction_threading()
    threading_avec_classe()
    arguments_et_donnees()
    synchronisation_lock()
    synchronisation_semaphore()
    autres_primitives()
    thread_pool_executor()
    queue_thread_safe()
    scanner_ports_multithread()
    bruteforce_multithread()
    enumeration_concurrente()
    gestion_avancee()
    performance_threading()

    print("\n" + "="*60)
    print("FIN DE LA DÉMONSTRATION")
    print("="*60)


if __name__ == "__main__":
    main()
