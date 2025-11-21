# Cours : Gestion de la Mémoire (Memory Management)

## 1. Introduction

La **gestion de la mémoire** concerne l'allocation, l'utilisation et la libération de la mémoire par les programmes. En Python, le garbage collector gère automatiquement la mémoire, mais comprendre les mécanismes sous-jacents est crucial.

### Pourquoi c'est important ?

- **Performance** : Optimiser l'usage mémoire
- **Éviter les fuites** : Libérer la mémoire inutilisée
- **Sécurité** : Buffer overflows, use-after-free
- **En sécurité** : Exploits mémoire, analysis forensique

## 2. Modèle Mémoire Python

### Architecture Mémoire

```
┌─────────────────────────┐
│   Stack (pile)          │  Variables locales, appels de fonction
├─────────────────────────┤
│   Heap (tas)            │  Objets Python, allocation dynamique
├─────────────────────────┤
│   Data Segment          │  Variables globales, constantes
├─────────────────────────┤
│   Code Segment          │  Bytecode Python
└─────────────────────────┘
```

### Références et Comptage

```python
import sys

# Chaque objet Python a un compteur de références
a = [1, 2, 3]
print(sys.getrefcount(a))  # 2 (a + argument de getrefcount)

b = a  # Nouvelle référence
print(sys.getrefcount(a))  # 3

del b  # Supprime une référence
print(sys.getrefcount(a))  # 2

# Quand refcount = 0 → garbage collector libère la mémoire
```

## 3. Garbage Collection en Python

### Reference Counting

```python
class MyClass:
    def __init__(self, name):
        self.name = name
        print(f"{name} créé")
    
    def __del__(self):
        print(f"{self.name} détruit")

obj = MyClass("Object1")
obj2 = obj  # refcount = 2
del obj     # refcount = 1
del obj2    # refcount = 0 → __del__() appelé
```

### Cycle Detection

```python
import gc

# Références circulaires
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

a = Node(1)
b = Node(2)
a.next = b
b.next = a  # Cycle!

# Sans cycle detector, fuite mémoire
# Python utilise un garbage collector générationnel

# Forcer le GC
gc.collect()

# Désactiver/activer
gc.disable()
gc.enable()
```

### Générations du GC

```python
import gc

# Python utilise 3 générations
print(gc.get_count())  # (objets_gen0, objets_gen1, objets_gen2)

# Seuils de collection
print(gc.get_threshold())  # (700, 10, 10)

# Statistiques
stats = gc.get_stats()
for i, stat in enumerate(stats):
    print(f"Génération {i}: {stat}")
```

## 4. Optimisation Mémoire

### Utiliser des Slots

```python
# ❌ Sans __slots__: chaque instance a un __dict__
class RegularClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# ✅ Avec __slots__: économise mémoire
class OptimizedClass:
    __slots__ = ['x', 'y']
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Comparaison
import sys
r = RegularClass(1, 2)
o = OptimizedClass(1, 2)
print(sys.getsizeof(r))  # ~48 bytes
print(sys.getsizeof(o))  # ~32 bytes (économie de 33%)
```

### Generators pour Grandes Données

```python
# ❌ Crée toute la liste en mémoire
def get_squares_list(n):
    return [i ** 2 for i in range(n)]

# ✅ Generator: génère à la demande
def get_squares_gen(n):
    for i in range(n):
        yield i ** 2

# Comparaison
import sys
list_obj = get_squares_list(1000)
gen_obj = get_squares_gen(1000)

print(sys.getsizeof(list_obj))  # ~9000 bytes
print(sys.getsizeof(gen_obj))   # ~128 bytes
```

### Objets Immuables et Interning

```python
# Python "interne" les petits entiers et strings
a = 256
b = 256
print(a is b)  # True (même objet)

a = 257
b = 257
print(a is b)  # False (objets différents)

# String interning
s1 = "hello"
s2 = "hello"
print(s1 is s2)  # True

# Forcer l'interning
import sys
s3 = sys.intern("hello world")
s4 = sys.intern("hello world")
print(s3 is s4)  # True
```

## 5. Profiling Mémoire

### memory_profiler

```python
from memory_profiler import profile

@profile
def my_function():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a

# Utilisation: python -m memory_profiler script.py
```

### tracemalloc (Built-in)

```python
import tracemalloc

tracemalloc.start()

# Code à profiler
data = [i for i in range(10**6)]

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("[ Top 10 ]")
for stat in top_stats[:10]:
    print(stat)

tracemalloc.stop()
```

### Mesurer la Taille d'Objets

```python
import sys

def get_size_deep(obj, seen=None):
    """Calcule la taille récursive d'un objet"""
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    
    seen.add(obj_id)
    
    if isinstance(obj, dict):
        size += sum([get_size_deep(v, seen) for v in obj.values()])
        size += sum([get_size_deep(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size_deep(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size_deep(i, seen) for i in obj])
    
    return size

data = {'a': [1, 2, 3], 'b': {'c': [4, 5]}}
print(f"Taille totale: {get_size_deep(data)} bytes")
```

## 6. Fuites Mémoire Courantes

### Fuite 1 : Références Globales

```python
# ❌ Liste globale qui grossit indéfiniment
cache = []

def process_data(data):
    cache.append(data)  # Fuite!
    return data * 2

# ✅ Limiter la taille
from collections import deque
cache = deque(maxlen=100)
```

### Fuite 2 : Closures

```python
# ❌ Closure garde une référence
def create_function():
    big_data = [0] * 10**6
    
    def inner():
        return big_data[0]  # Garde big_data en mémoire
    
    return inner

# ✅ Libérer explicitement
def create_function_fixed():
    big_data = [0] * 10**6
    value = big_data[0]
    del big_data
    
    def inner():
        return value
    
    return inner
```

### Fuite 3 : Event Listeners

```python
# ❌ Listeners pas désenregistrés
class EventSystem:
    def __init__(self):
        self.listeners = []
    
    def add_listener(self, callback):
        self.listeners.append(callback)

# ✅ Utiliser weak references
import weakref

class EventSystemFixed:
    def __init__(self):
        self.listeners = []
    
    def add_listener(self, callback):
        self.listeners.append(weakref.ref(callback))
    
    def trigger(self):
        # Nettoyer les références mortes
        self.listeners = [l for l in self.listeners if l() is not None]
        for listener_ref in self.listeners:
            listener = listener_ref()
            if listener:
                listener()
```

## 7. Applications en Sécurité

### Buffer Analysis

```python
def analyze_buffer(data, expected_size):
    """Analyse un buffer pour détecter des anomalies"""
    actual_size = len(data)
    
    if actual_size > expected_size:
        return {
            "status": "OVERFLOW",
            "expected": expected_size,
            "actual": actual_size,
            "overflow": actual_size - expected_size
        }
    
    # Vérifier patterns suspects
    suspicious_patterns = [
        b'\x90' * 10,  # NOP sled
        b'\x00' * 10,  # NULL bytes
        b'\xff' * 10   # 0xFF pattern
    ]
    
    for pattern in suspicious_patterns:
        if pattern in data:
            return {
                "status": "SUSPICIOUS_PATTERN",
                "pattern": pattern.hex()
            }
    
    return {"status": "OK"}
```

### Memory Dump Analysis

```python
def find_strings_in_memory(memory_dump, min_length=4):
    """Extrait les strings d'un dump mémoire"""
    strings = []
    current = b''
    
    for byte in memory_dump:
        if 32 <= byte <= 126:  # Caractères imprimables
            current += bytes([byte])
        else:
            if len(current) >= min_length:
                strings.append(current.decode('ascii'))
            current = b''
    
    return strings

# Exemple
dump = b'Hello\x00\x00World\x00\xff\xfeTest123'
print(find_strings_in_memory(dump))  # ['Hello', 'World', 'Test123']
```

### Secure Memory Clearing

```python
import ctypes

def secure_delete(data):
    """Efface de manière sécurisée une variable"""
    if isinstance(data, bytearray):
        # Écraser avec des zéros
        for i in range(len(data)):
            data[i] = 0
    elif isinstance(data, list):
        data.clear()
    
    # Forcer le GC
    import gc
    gc.collect()

# Pour des données sensibles (mots de passe, clés)
password = bytearray(b"secret123")
# ... utiliser le mot de passe ...
secure_delete(password)
```

## 8. Context Managers pour la Gestion Mémoire

```python
class MemoryMonitor:
    """Monitore l'usage mémoire d'un bloc de code"""
    
    def __enter__(self):
        import tracemalloc
        tracemalloc.start()
        self.start_snapshot = tracemalloc.take_snapshot()
        return self
    
    def __exit__(self, *args):
        import tracemalloc
        end_snapshot = tracemalloc.take_snapshot()
        top_stats = end_snapshot.compare_to(self.start_snapshot, 'lineno')
        
        print("\n[ Top 3 Memory Allocations ]")
        for stat in top_stats[:3]:
            print(stat)
        
        tracemalloc.stop()

# Utilisation
with MemoryMonitor():
    data = [i for i in range(10**6)]
```

## 9. Exercices

### Exercice 1 : Débutant
Créez une fonction qui détecte les fuites mémoire dans une boucle.

### Exercice 2 : Intermédiaire
Implémentez un pool d'objets pour réutiliser des objets coûteux.

### Exercice 3 : Intermédiaire
Créez un décorateur qui profile automatiquement la mémoire d'une fonction.

### Exercice 4 : Avancé
Implémentez un garbage collector simple pour comprendre son fonctionnement.

### Exercice 5 : Avancé
Créez un outil d'analyse forensique de dump mémoire.

## 10. Ressources

### Outils
- **memory_profiler** : Profiling ligne par ligne
- **objgraph** : Visualiser les références d'objets
- **pympler** : Mesures mémoire avancées
- **Valgrind** : Pour le C/C++

### Lectures
- *Python Memory Management* - Python Docs
- *High Performance Python* - O'Reilly
- *Memory Management in Python* - RealPython

---

**Prochaine étape** : Passez à `04_Object_Oriented_Design` pour les design patterns.
