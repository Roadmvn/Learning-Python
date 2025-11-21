# Cours : Design Patterns (Modèles de Conception)

## 1. Introduction

Les **design patterns** sont des solutions réutilisables à des problèmes récurrents en conception logicielle. Ils représentent les meilleures pratiques développées par des développeurs expérimentés.

### Pourquoi c'est important ?

- **Réutilisabilité** : Solutions éprouvées
- **Communication** : Vocabulaire commun
- **Maintenabilité** : Code plus structuré
- **En sécurité** : Patterns sécurisés (Proxy, Factory)

## 2. Catégories de Patterns

### Créationnels (Creational)
- Singleton, Factory, Builder, Prototype

### Structurels (Structural)
- Adapter, Decorator, Proxy, Facade

### Comportementaux (Behavioral)
- Observer, Strategy, Command, Iterator

## 3. Patterns Créationnels

### Singleton

Garantit qu'une classe n'a qu'une seule instance.

```python
class Singleton:
    """Pattern Singleton"""
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Test
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True

# Avec décorateur
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Database:
    def __init__(self):
        print("Connexion à la DB")

db1 = Database()
db2 = Database()  # Pas de nouvelle connexion
```

### Factory

Crée des objets sans spécifier leur classe exacte.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    """Factory pour créer des animaux"""
    
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

# Utilisation
factory = AnimalFactory()
dog = factory.create_animal("dog")
cat = factory.create_animal("cat")
print(dog.speak())  # "Woof!"
print(cat.speak())  # "Meow!"
```

### Builder

Construit des objets complexes étape par étape.

```python
class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.gpu = None
    
    def __str__(self):
        return f"Computer(CPU={self.cpu}, RAM={self.ram}GB, Storage={self.storage}GB, GPU={self.gpu})"

class ComputerBuilder:
    """Builder pour construire un ordinateur"""
    
    def __init__(self):
        self.computer = Computer()
    
    def add_cpu(self, cpu):
        self.computer.cpu = cpu
        return self
    
    def add_ram(self, ram):
        self.computer.ram = ram
        return self
    
    def add_storage(self, storage):
        self.computer.storage = storage
        return self
    
    def add_gpu(self, gpu):
        self.computer.gpu = gpu
        return self
    
    def build(self):
        return self.computer

# Utilisation (chaînage)
pc = (ComputerBuilder()
      .add_cpu("Intel i7")
      .add_ram(16)
      .add_storage(512)
      .add_gpu("RTX 3080")
      .build())

print(pc)
```

## 4. Patterns Structurels

### Adapter

Permet à des interfaces incompatibles de travailler ensemble.

```python
class EuropeanSocket:
    def voltage(self):
        return 230

class USASocket:
    def voltage(self):
        return 110

class SocketAdapter:
    """Adaptateur EU → USA"""
    
    def __init__(self, socket):
        self.socket = socket
    
    def voltage(self):
        return self.socket.voltage() / 2

# Utilisation
eu_socket = EuropeanSocket()
adapter = SocketAdapter(eu_socket)
print(adapter.voltage())  # 115 (230 / 2)
```

### Decorator

Ajoute des fonctionnalités à un objet dynamiquement.

```python
def log_execution(func):
    """Décorateur pour logger l'exécution"""
    def wrapper(*args, **kwargs):
        print(f"Exécution de {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} terminé")
        return result
    return wrapper

def time_execution(func):
    """Décorateur pour mesurer le temps"""
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} a pris {end - start:.4f}s")
        return result
    return wrapper

@log_execution
@time_execution
def process_data(n):
    total = sum(range(n))
    return total

process_data(1000000)
```

### Proxy

Contrôle l'accès à un objet.

```python
class RealDatabase:
    def query(self, sql):
        print(f"Exécution: {sql}")
        return [{"id": 1, "name": "Data"}]

class DatabaseProxy:
    """Proxy avec contrôle d'accès et cache"""
    
    def __init__(self, real_db):
        self.real_db = real_db
        self.cache = {}
    
    def query(self, sql):
        # Vérification permission (sécurité)
        if "DROP" in sql or "DELETE" in sql:
            print("⚠️ Opération dangereuse bloquée")
            return None
        
        # Cache
        if sql in self.cache:
            print("📦 Résultat du cache")
            return self.cache[sql]
        
        # Exécution réelle
        result = self.real_db.query(sql)
        self.cache[sql] = result
        return result

# Utilisation
db = DatabaseProxy(RealDatabase())
db.query("SELECT * FROM users")  # Exécution réelle
db.query("SELECT * FROM users")  # Depuis le cache
db.query("DROP TABLE users")     # Bloqué!
```

## 5. Patterns Comportementaux

### Observer

Notifie les observateurs lors d'un changement d'état.

```python
class Subject:
    """Sujet observé"""
    
    def __init__(self):
        self._observers = []
        self._state = None
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)
    
    def notify(self):
        for observer in self._observers:
            observer.update(self._state)
    
    def set_state(self, state):
        self._state = state
        self.notify()

class Observer:
    """Observateur"""
    
    def __init__(self, name):
        self.name = name
    
    def update(self, state):
        print(f"{self.name} notifié: état = {state}")

# Utilisation
subject = Subject()
observer1 = Observer("Observer1")
observer2 = Observer("Observer2")

subject.attach(observer1)
subject.attach(observer2)

subject.set_state("État A")
# Observer1 notifié: état = État A
# Observer2 notifié: état = État A
```

### Strategy

Définit une famille d'algorithmes interchangeables.

```python
from abc import ABC, abstractmethod

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass

class BubbleSort(SortStrategy):
    def sort(self, data):
        print("Tri à bulles")
        return sorted(data)  # Simplifié

class QuickSort(SortStrategy):
    def sort(self, data):
        print("Tri rapide")
        return sorted(data)  # Simplifié

class Sorter:
    """Context qui utilise une stratégie"""
    
    def __init__(self, strategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy):
        self.strategy = strategy
    
    def sort(self, data):
        return self.strategy.sort(data)

# Utilisation
sorter = Sorter(BubbleSort())
sorter.sort([3, 1, 2])

sorter.set_strategy(QuickSort())
sorter.sort([3, 1, 2])
```

### Command

Encapsule une requête comme un objet.

```python
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def undo(self):
        pass

class Light:
    def on(self):
        print("💡 Lumière allumée")
    
    def off(self):
        print("⚫ Lumière éteinte")

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.on()
    
    def undo(self):
        self.light.off()

class RemoteControl:
    """Invocateur"""
    
    def __init__(self):
        self.history = []
    
    def execute_command(self, command):
        command.execute()
        self.history.append(command)
    
    def undo_last(self):
        if self.history:
            command = self.history.pop()
            command.undo()

# Utilisation
light = Light()
light_on = LightOnCommand(light)

remote = RemoteControl()
remote.execute_command(light_on)  # Allume
remote.undo_last()  # Éteint
```

## 6. Applications en Sécurité

### Factory pour Malware Detection

```python
class MalwareDetector(ABC):
    @abstractmethod
    def scan(self, file):
        pass

class SignatureDetector(MalwareDetector):
    def scan(self, file):
        return "Détection par signature"

class BehaviorDetector(MalwareDetector):
    def scan(self, file):
        return "Détection comportementale"

class DetectorFactory:
    @staticmethod
    def get_detector(detector_type):
        if detector_type == "signature":
            return SignatureDetector()
        elif detector_type == "behavior":
            return BehaviorDetector()
        else:
            raise ValueError("Unknown detector")

# Utilisation
detector = DetectorFactory.get_detector("signature")
print(detector.scan("malware.exe"))
```

### Chain of Responsibility (Firewall)

```python
class Handler(ABC):
    def __init__(self):
        self.next_handler = None
    
    def set_next(self, handler):
        self.next_handler = handler
        return handler
    
    @abstractmethod
    def handle(self, request):
        pass

class IPFilter(Handler):
    def handle(self, request):
        if request["ip"] in ["192.168.1.100"]:
            print("🚫 IP bloquée")
            return False
        
        if self.next_handler:
            return self.next_handler.handle(request)
        return True

class RateLimiter(Handler):
    def handle(self, request):
        if request.get("requests", 0) > 100:
            print("🚫 Rate limit dépassé")
            return False
        
        if self.next_handler:
            return self.next_handler.handle(request)
        return True

class ContentFilter(Handler):
    def handle(self, request):
        if "<script>" in request.get("content", ""):
            print("🚫 Contenu malveillant détecté")
            return False
        
        if self.next_handler:
            return self.next_handler.handle(request)
        return True

# Chaîne de filtres
ip_filter = IPFilter()
rate_limiter = RateLimiter()
content_filter = ContentFilter()

ip_filter.set_next(rate_limiter).set_next(content_filter)

# Test
request = {"ip": "192.168.1.50", "requests": 50, "content": "Hello"}
ip_filter.handle(request)  # ✅ Passe
```

## 7. Anti-Patterns (À Éviter)

### God Object

```python
# ❌ MAUVAIS: Classe qui fait tout
class SystemManager:
    def manage_users(self):
        pass
    def manage_database(self):
        pass
    def manage_network(self):
        pass
    def manage_files(self):
        pass
    # ... 50 autres méthodes

# ✅ BON: Responsabilités séparées
class UserManager:
    def manage_users(self):
        pass

class DatabaseManager:
    def manage_database(self):
        pass
```

### Spaghetti Code

```python
# ❌ MAUVAIS: Code enchevêtré
def process():
    if condition1:
        if condition2:
            if condition3:
                # ...
                pass

# ✅ BON: Guard clauses
def process():
    if not condition1:
        return
    if not condition2:
        return
    if not condition3:
        return
    # ...
```

## 8. Exercices

### Exercice 1 : Débutant
Implémentez le pattern Factory pour créer différents types de loggers.

### Exercice 2 : Intermédiaire
Créez un système de plugins avec le pattern Strategy.

### Exercice 3 : Intermédiaire
Implémentez un système d'undo/redo avec le pattern Command.

### Exercice 4 : Avancé
Créez un framework de sécurité avec Chain of Responsibility.

### Exercice 5 : Avancé
Implémentez un cache distribué avec les patterns Singleton et Proxy.

## 9. Ressources

### Livres
- *Design Patterns* (Gang of Four)
- *Head First Design Patterns*
- *Python Design Patterns* - Brandon Rhodes

### Sites
- [Refactoring Guru](https://refactoring.guru/design-patterns)
- [SourceMaking](https://sourcemaking.com/design_patterns)

---

**Félicitations !** Vous avez complété tous les modules de cours.
