# Cours : Piles & Files (Stacks & Queues)

## 1. Introduction

Les **piles (stacks)** et **files (queues)** sont des structures de données linéaires avec des règles spécifiques d'ajout et de retrait d'éléments. Elles sont fondamentales dans de nombreux algorithmes et systèmes.

### Pourquoi c'est important ?

- **Gestion de l'exécution** : Call stack des programmes
- **Algorithmes classiques** : DFS (pile), BFS (file)
- **Systèmes d'exploitation** : Gestion de processus, buffers
- **En sécurité** : Stack overflows, buffer analysis, shellcode execution

## 2. Concepts Clés

### Stack (Pile) - LIFO

**LIFO** = Last In, First Out (Dernier Entré, Premier Sorti)

```
    push(5)         push(3)         pop()
      ↓               ↓               ↑
    ┌───┐         ┌───┐         ┌───┐
    │   │         │ 3 │ ← top   │   │
    ├───┤         ├───┤         ├───┤
    │   │         │ 5 │         │ 5 │ ← top
    ├───┤         ├───┤         ├───┤
    │   │         │ 1 │         │ 1 │
    └───┘         └───┘         └───┘
```

**Opérations principales** :
- `push(item)` : Ajouter au sommet - O(1)
- `pop()` : Retirer du sommet - O(1)
- `peek()`/`top()` : Voir le sommet sans retirer - O(1)
- `is_empty()` : Vérifier si vide - O(1)

### Queue (File) - FIFO

**FIFO** = First In, First Out (Premier Entré, Premier Sorti)

```
    enqueue(5)      enqueue(3)      dequeue()
       ↓               ↓               ↑
    ┌───┬───┬───┐  ┌───┬───┬───┐  ┌───┬───┬───┐
    │ 5 │   │   │  │ 5 │ 3 │   │  │ 3 │   │   │
    └───┴───┴───┘  └───┴───┴───┘  └───┴───┴───┘
     ↑                ↑               ↑
    front           front           front
```

**Opérations principales** :
- `enqueue(item)` : Ajouter à la fin - O(1)
- `dequeue()` : Retirer du début - O(1)
- `front()`/`peek()` : Voir le premier sans retirer - O(1)
- `is_empty()` : Vérifier si vide - O(1)

## 3. Implémentation en Python

### Stack avec Liste Python

```python
class Stack:
    """Pile (LIFO) implémentée avec une liste Python"""
    
    def __init__(self):
        self._items = []
    
    def push(self, item):
        """Ajoute un élément au sommet - O(1)"""
        self._items.append(item)
    
    def pop(self):
        """Retire et retourne l'élément du sommet - O(1)"""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self._items.pop()
    
    def peek(self):
        """Retourne l'élément du sommet sans le retirer - O(1)"""
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self._items[-1]
    
    def is_empty(self):
        """Vérifie si la pile est vide - O(1)"""
        return len(self._items) == 0
    
    def size(self):
        """Retourne la taille de la pile - O(1)"""
        return len(self._items)
    
    def __str__(self):
        return f"Stack({self._items})"

# Utilisation
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # 3
print(stack.peek()) # 2
```

### Stack avec collections.deque (plus performant)

```python
from collections import deque

class StackDeque:
    """Stack optimisé avec deque"""
    
    def __init__(self):
        self._items = deque()
    
    def push(self, item):
        self._items.append(item)
    
    def pop(self):
        if not self._items:
            raise IndexError("Pop from empty stack")
        return self._items.pop()
    
    def peek(self):
        if not self._items:
            raise IndexError("Peek from empty stack")
        return self._items[-1]
    
    def is_empty(self):
        return len(self._items) == 0
```

### Queue avec Liste (inefficace)

```python
class QueueList:
    """File simple (FIFO) - INEFFICACE pour grandes données"""
    
    def __init__(self):
        self._items = []
    
    def enqueue(self, item):
        """Ajoute à la fin - O(1)"""
        self._items.append(item)
    
    def dequeue(self):
        """Retire du début - O(n) ⚠️ LENT"""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self._items.pop(0)  # O(n) car décalage
    
    def front(self):
        if self.is_empty():
            raise IndexError("Front from empty queue")
        return self._items[0]
    
    def is_empty(self):
        return len(self._items) == 0
```

### Queue avec collections.deque (optimal)

```python
from collections import deque

class Queue:
    """File (FIFO) optimale avec deque"""
    
    def __init__(self):
        self._items = deque()
    
    def enqueue(self, item):
        """Ajoute à la fin - O(1)"""
        self._items.append(item)
    
    def dequeue(self):
        """Retire du début - O(1)"""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self._items.popleft()  # O(1) avec deque!
    
    def front(self):
        """Voir le premier élément - O(1)"""
        if self.is_empty():
            raise IndexError("Front from empty queue")
        return self._items[0]
    
    def is_empty(self):
        return len(self._items) == 0
    
    def size(self):
        return len(self._items)

# Utilisation
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # 1
print(queue.front())    # 2
```

### Queue avec deux Stacks

```python
class QueueWithTwoStacks:
    """File implémentée avec deux piles"""
    
    def __init__(self):
        self._stack_in = []   # Pour enqueue
        self._stack_out = []  # Pour dequeue
    
    def enqueue(self, item):
        """O(1)"""
        self._stack_in.append(item)
    
    def dequeue(self):
        """O(1) amortisé"""
        if not self._stack_out:
            # Transférer tous les éléments de stack_in vers stack_out
            while self._stack_in:
                self._stack_out.append(self._stack_in.pop())
        
        if not self._stack_out:
            raise IndexError("Dequeue from empty queue")
        
        return self._stack_out.pop()
    
    def is_empty(self):
        return not self._stack_in and not self._stack_out
```

## 4. Variantes Spéciales

### Min Stack (Pile avec minimum en O(1))

```python
class MinStack:
    """Pile qui retourne le minimum en O(1)"""
    
    def __init__(self):
        self._stack = []
        self._min_stack = []
    
    def push(self, item):
        self._stack.append(item)
        
        # Mettre à jour la pile des minimums
        if not self._min_stack or item <= self._min_stack[-1]:
            self._min_stack.append(item)
    
    def pop(self):
        if not self._stack:
            raise IndexError("Pop from empty stack")
        
        item = self._stack.pop()
        
        # Si c'était le minimum, le retirer aussi
        if item == self._min_stack[-1]:
            self._min_stack.pop()
        
        return item
    
    def get_min(self):
        """Retourne le minimum en O(1)"""
        if not self._min_stack:
            raise IndexError("Stack is empty")
        return self._min_stack[-1]
```

### Priority Queue (File de Priorité)

```python
import heapq

class PriorityQueue:
    """File de priorité avec heap"""
    
    def __init__(self):
        self._heap = []
        self._counter = 0  # Pour gérer les égalités
    
    def enqueue(self, item, priority):
        """Ajoute avec priorité (plus petit = plus prioritaire)"""
        # Utiliser counter pour maintenir l'ordre FIFO pour même priorité
        heapq.heappush(self._heap, (priority, self._counter, item))
        self._counter += 1
    
    def dequeue(self):
        """Retire l'élément avec la plus haute priorité"""
        if not self._heap:
            raise IndexError("Dequeue from empty priority queue")
        return heapq.heappop(self._heap)[2]  # Retourner item uniquement
    
    def is_empty(self):
        return len(self._heap) == 0

# Utilisation
pq = PriorityQueue()
pq.enqueue("task1", priority=3)
pq.enqueue("task2", priority=1)
pq.enqueue("task3", priority=2)
print(pq.dequeue())  # "task2" (priorité 1)
```

### Circular Queue (File Circulaire)

```python
class CircularQueue:
    """File circulaire avec taille fixe"""
    
    def __init__(self, capacity):
        self._queue = [None] * capacity
        self._capacity = capacity
        self._front = 0
        self._rear = 0
        self._size = 0
    
    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("Queue is full")
        
        self._queue[self._rear] = item
        self._rear = (self._rear + 1) % self._capacity
        self._size += 1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        
        item = self._queue[self._front]
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return item
    
    def is_empty(self):
        return self._size == 0
    
    def is_full(self):
        return self._size == self._capacity
```

## 5. Problèmes Classiques

### Problème 1 : Parenthèses Équilibrées

```python
def is_balanced(expression):
    """Vérifie si les parenthèses sont équilibrées - O(n)"""
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in expression:
        if char in pairs:  # Ouvrante
            stack.append(char)
        elif char in pairs.values():  # Fermante
            if not stack:
                return False
            if pairs[stack.pop()] != char:
                return False
    
    return len(stack) == 0

# Tests
print(is_balanced("()[]{}"))      # True
print(is_balanced("([{}])"))      # True
print(is_balanced("([)]"))        # False
print(is_balanced("((()"))        # False
```

### Problème 2 : Évaluation d'Expression Postfixe

```python
def evaluate_postfix(expression):
    """Évalue une expression postfixe (RPN) - O(n)"""
    stack = []
    operators = {'+', '-', '*', '/'}
    
    for token in expression.split():
        if token not in operators:
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                result = a / b
            
            stack.append(result)
    
    return stack[0]

# Test
print(evaluate_postfix("3 4 + 2 * 7 /"))  # ((3+4)*2)/7 = 2.0
```

### Problème 3 : Conversion Infixe → Postfixe

```python
def infix_to_postfix(expression):
    """Convertit notation infixe en postfixe - O(n)"""
    stack = []
    output = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    
    for token in expression.split():
        if token.isalnum():  # Opérande
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Retirer '('
        else:  # Opérateur
            while (stack and stack[-1] != '(' and
                   precedence.get(stack[-1], 0) >= precedence.get(token, 0)):
                output.append(stack.pop())
            stack.append(token)
    
    while stack:
        output.append(stack.pop())
    
    return ' '.join(output)

# Test
print(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 )"))  # 3 4 2 * 1 5 - / +
```

### Problème 4 : Stock Span Problem

```python
def calculate_span(prices):
    """Calcule le span de chaque jour - O(n)"""
    stack = []  # Stock (index, price)
    spans = []
    
    for i, price in enumerate(prices):
        # Retirer tous les jours avec prix <= actuel
        while stack and stack[-1][1] <= price:
            stack.pop()
        
        # Calculer le span
        if not stack:
            span = i + 1  # Tous les jours précédents
        else:
            span = i - stack[-1][0]
        
        spans.append(span)
        stack.append((i, price))
    
    return spans

# Test
prices = [100, 80, 60, 70, 60, 75, 85]
print(calculate_span(prices))  # [1, 1, 1, 2, 1, 4, 6]
```

### Problème 5 : Sliding Window Maximum

```python
from collections import deque

def max_sliding_window(arr, k):
    """Trouve le max de chaque fenêtre de taille k - O(n)"""
    dq = deque()  # Stocke les indices
    result = []
    
    for i in range(len(arr)):
        # Retirer les indices hors de la fenêtre
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        # Retirer les éléments plus petits (inutiles)
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
        
        dq.append(i)
        
        # Ajouter le max au résultat (après la première fenêtre)
        if i >= k - 1:
            result.append(arr[dq[0]])
    
    return result

# Test
print(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))
# [3, 3, 5, 5, 6, 7]
```

## 6. Applications en Sécurité

### Call Stack Analysis (Buffer Overflow)

```python
class CallStack:
    """Simulation simple d'une call stack pour analyse"""
    
    def __init__(self, max_depth=100):
        self._stack = []
        self._max_depth = max_depth
    
    def push_frame(self, function_name, buffer_size, input_data):
        """Simule l'ajout d'une stack frame"""
        if len(self._stack) >= self._max_depth:
            raise OverflowError("Stack overflow detected!")
        
        # Vérifier buffer overflow
        if len(input_data) > buffer_size:
            print(f"⚠️ ALERT: Buffer overflow in {function_name}!")
            print(f"   Buffer: {buffer_size} bytes, Input: {len(input_data)} bytes")
            return False
        
        frame = {
            'function': function_name,
            'buffer_size': buffer_size,
            'input_size': len(input_data),
            'return_address': id(self)  # Simulation
        }
        
        self._stack.append(frame)
        return True
    
    def pop_frame(self):
        """Simule le retour d'une fonction"""
        if not self._stack:
            raise IndexError("Stack underflow!")
        return self._stack.pop()
    
    def get_backtrace(self):
        """Retourne la trace d'appel"""
        return [frame['function'] for frame in reversed(self._stack)]

# Utilisation
stack = CallStack()
stack.push_frame("main", 256, "A" * 100)
stack.push_frame("process_input", 64, "B" * 100)  # Alerte!
```

### Request Queue (DDoS Protection)

```python
import time
from collections import deque

class RateLimitedQueue:
    """File avec limitation de débit pour protection DDoS"""
    
    def __init__(self, max_requests_per_second=10):
        self._queue = deque()
        self._timestamps = deque()
        self._max_rate = max_requests_per_second
    
    def enqueue(self, request):
        """Ajoute une requête si sous la limite"""
        current_time = time.time()
        
        # Nettoyer les timestamps anciens (> 1 seconde)
        while self._timestamps and current_time - self._timestamps[0] > 1.0:
            self._timestamps.popleft()
        
        # Vérifier la limite de débit
        if len(self._timestamps) >= self._max_rate:
            return False, "Rate limit exceeded"
        
        self._queue.append(request)
        self._timestamps.append(current_time)
        return True, "Request accepted"
    
    def dequeue(self):
        if not self._queue:
            return None
        return self._queue.popleft()

# Utilisation
rate_limiter = RateLimitedQueue(max_requests_per_second=5)
for i in range(10):
    success, msg = rate_limiter.enqueue(f"Request {i}")
    print(f"{msg}: Request {i}")
```

### Undo/Redo avec Deux Stacks

```python
class UndoRedoManager:
    """Gestionnaire d'annulation/rétablissement pour éditeur"""
    
    def __init__(self):
        self._undo_stack = []
        self._redo_stack = []
        self._current_state = ""
    
    def execute(self, action):
        """Exécute une action et l'ajoute à l'historique"""
        self._undo_stack.append(self._current_state)
        self._current_state = action(self._current_state)
        self._redo_stack.clear()  # Invalider redo après nouvelle action
    
    def undo(self):
        """Annule la dernière action"""
        if not self._undo_stack:
            return False
        
        self._redo_stack.append(self._current_state)
        self._current_state = self._undo_stack.pop()
        return True
    
    def redo(self):
        """Rétablit une action annulée"""
        if not self._redo_stack:
            return False
        
        self._undo_stack.append(self._current_state)
        self._current_state = self._redo_stack.pop()
        return True
    
    def get_state(self):
        return self._current_state

# Utilisation
manager = UndoRedoManager()
manager.execute(lambda s: s + "Hello ")
manager.execute(lambda s: s + "World")
print(manager.get_state())  # "Hello World"
manager.undo()
print(manager.get_state())  # "Hello "
manager.redo()
print(manager.get_state())  # "Hello World"
```

## 7. Complexité & Performance

| Opération | Stack (list) | Stack (deque) | Queue (list) | Queue (deque) |
|-----------|--------------|---------------|--------------|---------------|
| push/enqueue | O(1) | O(1) | O(1) | O(1) |
| pop/dequeue | O(1) | O(1) | **O(n)** ⚠️ | O(1) ✓ |
| peek/front | O(1) | O(1) | O(1) | O(1) |
| Espace | O(n) | O(n) | O(n) | O(n) |

**Recommandation** : Toujours utiliser `collections.deque` pour les queues en Python !

## 8. Pièges Courants

### 1. Pop sur Stack Vide
```python
# ❌ MAUVAIS
stack = []
item = stack.pop()  # IndexError!

# ✅ BON
if stack:
    item = stack.pop()
```

### 2. Queue avec Liste
```python
# ❌ INEFFICACE
queue = []
queue.append(1)
queue.pop(0)  # O(n) - décalage!

# ✅ EFFICACE
from collections import deque
queue = deque()
queue.append(1)
queue.popleft()  # O(1)
```

### 3. Confusion LIFO vs FIFO
```python
# Stack = LIFO (dernier entré, premier sorti)
stack = [1, 2, 3]
stack.pop()  # Retourne 3

# Queue = FIFO (premier entré, premier sorti)
queue = deque([1, 2, 3])
queue.popleft()  # Retourne 1
```

## 9. Exercices

### Exercice 1 : Débutant
Implémentez une fonction qui inverse une string en utilisant une stack.

### Exercice 2 : Intermédiaire
Créez une fonction qui simplifie un chemin Unix (ex: `/a/./b/../../c/` → `/c`).

### Exercice 3 : Intermédiaire
Implémentez un algorithme pour trouver l'élément suivant plus grand pour chaque élément d'un tableau.

### Exercice 4 : Avancé
Créez une structure de données qui supporte push, pop, et getMin en O(1).

### Exercice 5 : Avancé
Implémentez un évaluateur d'expressions mathématiques avec support des parenthèses et des opérateurs.

## 10. Ressources

### Plateformes de pratique
- **LeetCode** : Tags "Stack" et "Queue"
- **HackerRank** : Stacks and Queues
- **CodeWars** : Stack/Queue Katas

### Lectures complémentaires
- *Introduction to Algorithms* (CLRS) - Chapitre 10
- *Data Structures and Algorithms in Python* - Goodrich

### Visualisations
- [VisuAlgo](https://visualgo.net/en/list) - Visualisation Stack/Queue
- [Python Tutor](http://pythontutor.com/) - Exécution pas-à-pas

---

**Prochaine étape** : Passez à `04_Trees_Graphs` pour explorer les structures hiérarchiques et relationnelles.
