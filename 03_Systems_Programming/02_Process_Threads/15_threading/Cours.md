# Exercice 15 : Threading en Python

## Objectifs d'Apprentissage

- Comprendre le concept de programmation multi-thread
- Maîtriser le module `threading` de Python
- Créer et gérer des threads
- Utiliser la classe `Thread` et ses méthodes
- Synchroniser les threads avec Lock et Semaphore
- Comprendre et éviter les race conditions
- Connaître les limitations du GIL (Global Interpreter Lock)
- Appliquer le threading aux opérations de cybersécurité

## Concepts Clés

### Module threading

Le module `threading` permet d'exécuter plusieurs tâches simultanément dans un même processus.

```
Programme Principal
├── Thread 1 → Tâche A
├── Thread 2 → Tâche B
├── Thread 3 → Tâche C
└── Thread 4 → Tâche D
```

**Avantages** :
- Amélioration des performances pour les opérations I/O
- Meilleure utilisation des ressources
- Interface utilisateur réactive
- Parallélisation des tâches

**Cas d'usage en cybersécurité** :
- Scan de ports parallèle
- Bruteforce multi-threadé
- Énumération concurrente de services
- Fuzzing parallèle
- Analyse de vulnérabilités distribuée

### Créer des Threads

**Méthode 1 : Fonction cible**
```python
import threading

def ma_fonction():
    print("Thread en exécution")

thread = threading.Thread(target=ma_fonction)
thread.start()
```

**Méthode 2 : Classe héritée**
```python
class MonThread(threading.Thread):
    def run(self):
        print("Thread personnalisé en exécution")

thread = MonThread()
thread.start()
```

### Thread Class

**Attributs principaux** :
- `name` : Nom du thread
- `daemon` : Thread daemon (termine avec le programme principal)
- `ident` : Identifiant unique du thread

**Méthodes essentielles** :
- `start()` : Démarrer le thread
- `join(timeout)` : Attendre la fin du thread
- `is_alive()` : Vérifier si le thread est actif
- `run()` : Méthode exécutée par le thread

### Start et Join

**start()** : Lance l'exécution du thread
```python
thread.start()  # Démarre le thread
```

**join()** : Attend la fin du thread
```python
thread.join()  # Bloque jusqu'à la fin du thread
thread.join(timeout=5)  # Attend maximum 5 secondes
```

**Schéma d'exécution** :
```
Main Thread:    [====create====][====join====][====continue====]
Worker Thread:       [======start======run======end]
```

### Synchronisation : Lock

Les **Lock** (verrous) empêchent les accès concurrents aux ressources partagées.

```python
import threading

lock = threading.Lock()

lock.acquire()  # Acquérir le verrou
try:
    # Section critique
    pass
finally:
    lock.release()  # Libérer le verrou
```

**Avec context manager** :
```python
with lock:
    # Section critique automatiquement protégée
    pass
```

### Synchronisation : Semaphore

Les **Semaphore** limitent le nombre de threads accédant à une ressource.

```python
semaphore = threading.Semaphore(3)  # Max 3 threads simultanés

with semaphore:
    # Maximum 3 threads peuvent être ici en même temps
    pass
```

**Différence Lock vs Semaphore** :
```
Lock:      [1 thread maximum]
Semaphore: [N threads maximum]
```

### Race Conditions

Une **race condition** se produit quand plusieurs threads accèdent simultanément à une ressource partagée.

**Exemple de problème** :
```python
counter = 0

def increment():
    global counter
    for _ in range(100000):
        counter += 1  # Non thread-safe!
```

**Solution avec Lock** :
```python
counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1  # Thread-safe
```

### GIL (Global Interpreter Lock)

Le **GIL** est un verrou global dans CPython qui empêche l'exécution simultanée de bytecode Python.

**Implications** :
- Un seul thread Python exécuté à la fois
- Pas de parallélisme réel pour le code CPU-bound
- Le threading reste efficace pour les opérations I/O-bound
- Pour le vrai parallélisme CPU, utiliser `multiprocessing`

**Quand utiliser threading** :
- Opérations réseau (scan, requêtes HTTP)
- Opérations fichier
- Attentes I/O
- Amélioration de la réactivité

**Quand utiliser multiprocessing** :
- Calculs intensifs
- Traitement de données massives
- Cryptographie
- Analyse parallèle

## Applications en Cybersécurité

### Scan de Ports Parallèle

```
Scanner de Ports:
├── Thread 1 → Ports 1-100
├── Thread 2 → Ports 101-200
├── Thread 3 → Ports 201-300
└── Thread N → Ports X-Y
```

Amélioration significative des performances.

### Bruteforce Multi-threadé

```
Bruteforce:
├── Thread 1 → Passwords batch 1
├── Thread 2 → Passwords batch 2
├── Thread 3 → Passwords batch 3
└── Thread N → Passwords batch N
```

Distribution de la charge de travail.

### Énumération Concurrente

```
Énumération:
├── Thread 1 → Directories
├── Thread 2 → Subdomains
├── Thread 3 → Users
└── Thread 4 → Services
```

Collecte d'informations simultanée.

## Bonnes Pratiques

### Gestion des Threads

1. **Toujours joindre les threads**
```python
threads = []
for i in range(10):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for t in threads:
    t.join()  # Attendre tous les threads
```

2. **Utiliser des threads daemon si nécessaire**
```python
t = threading.Thread(target=worker, daemon=True)
t.start()
# Le programme peut se terminer sans attendre ce thread
```

3. **Limiter le nombre de threads**
```python
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=50) as executor:
    executor.map(worker, tasks)
```

### Synchronisation

1. **Protéger les ressources partagées**
```python
shared_data = []
lock = threading.Lock()

def add_data(item):
    with lock:
        shared_data.append(item)
```

2. **Éviter les deadlocks**
```python
# Toujours acquérir les locks dans le même ordre
lock1.acquire()
lock2.acquire()
# ...
lock2.release()
lock1.release()
```

3. **Utiliser des structures thread-safe**
```python
from queue import Queue

queue = Queue()  # Thread-safe par défaut
```

### Gestion des Erreurs

```python
def worker():
    try:
        # Code du thread
        pass
    except Exception as e:
        print(f"Erreur dans le thread: {e}")
```

## Outils Utiles

### threading Module

- `threading.Thread` : Classe de base pour les threads
- `threading.Lock` : Verrou exclusif
- `threading.RLock` : Verrou réentrant
- `threading.Semaphore` : Sémaphore
- `threading.Event` : Signal entre threads
- `threading.Condition` : Condition de synchronisation
- `threading.Timer` : Thread avec délai
- `threading.active_count()` : Nombre de threads actifs
- `threading.current_thread()` : Thread courant
- `threading.enumerate()` : Liste des threads actifs

### concurrent.futures

```python
from concurrent.futures import ThreadPoolExecutor, as_completed

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(task, arg) for arg in args]
    for future in as_completed(futures):
        result = future.result()
```

### queue Module

```python
from queue import Queue, LifoQueue, PriorityQueue

q = Queue()  # FIFO thread-safe
q.put(item)
item = q.get()
```

## Avertissements de Sécurité

### Utilisation Éthique

- Ne pas utiliser pour des attaques DDoS
- Respecter les limites de rate-limiting
- Obtenir les autorisations avant tout scan
- Utiliser uniquement dans un cadre légal

### Considérations Techniques

- Trop de threads peut dégrader les performances
- Surveillance de la consommation mémoire
- Gestion appropriée des timeouts
- Nettoyage des ressources

## Ressources

- Documentation Python threading : https://docs.python.org/3/library/threading.html
- PEP 8 : Style Guide for Python Code
- Real Python Threading Tutorial
- Understanding the Python GIL
