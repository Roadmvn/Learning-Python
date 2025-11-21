# Cours: Linked Lists (Listes Chaînées)

## 1. Introduction

Les **listes chaînées** sont une structure de données fondamentale où chaque élément (nœud) contient une valeur et une référence vers le nœud suivant. Contrairement aux tableaux, les listes chaînées permettent une insertion et suppression efficace sans déplacement de données.

### Pourquoi c'est important ?
- **Gestion dynamique de la mémoire** : Pas besoin de connaître la taille à l'avance
- **Insertion/suppression O(1)** : Quand on a la référence au nœud
- **Base de structures complexes** : Piles, files, graphes utilisent ce concept
- **En sécurité** : Gestion de buffers dynamiques, structures de données malware

## 2. Concepts Fondamentaux

### Types de Listes Chaînées

#### Singly Linked List (Liste simplement chaînée)
```
HEAD → [Data|Next] → [Data|Next] → [Data|None]
```
Chaque nœud pointe uniquement vers le suivant.

#### Doubly Linked List (Liste doublement chaînée)
```
None ← [Prev|Data|Next] ↔ [Prev|Data|Next] ↔ [Prev|Data|Next] → None
```
Chaque nœud pointe vers le suivant ET le précédent.

#### Circular Linked List (Liste circulaire)
```
      ┌─────────────────────────┐
      ↓                         ↑
[Data|Next] → [Data|Next] → [Data|Next]
```
Le dernier nœud pointe vers le premier.

### Complexité Temporelle

| Opération | Array | Linked List |
|-----------|-------|-------------|
| Accès i-ème élément | O(1) | O(n) |
| Insertion début | O(n) | O(1) |
| Insertion fin | O(1) | O(n)* |
| Suppression début | O(n) | O(1) |
| Recherche | O(n) | O(n) |

*O(1) si on maintient un pointeur tail

## 3. Implémentation en Python

### Structure de Nœud

```python
class Node:
    """Nœud d'une liste chaînée"""
    def __init__(self, data):
        self.data = data
        self.next = None  # Référence au nœud suivant
    
    def __repr__(self):
        return f"Node({self.data})"
```

### Singly Linked List

```python
class LinkedList:
    """Liste simplement chaînée"""
    
    def __init__(self):
        self.head = None  # Premier nœud
        self.size = 0
    
    def is_empty(self):
        """Vérifie si la liste est vide"""
        return self.head is None
    
    def append(self, data):
        """Ajoute un élément à la fin - O(n)"""
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Parcourir jusqu'au dernier
                current = current.next
            current.next = new_node
        
        self.size += 1
    
    def prepend(self, data):
        """Ajoute un élément au début - O(1)"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def insert_at(self, index, data):
        """Insère à une position donnée"""
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        
        if index == 0:
            self.prepend(data)
            return
        
        new_node = Node(data)
        current = self.head
        
        # Aller au nœud avant la position
        for _ in range(index - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self.size += 1
    
    def delete(self, data):
        """Supprime la première occurrence de data"""
        if self.is_empty():
            return False
        
        # Cas spécial: suppression du head
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return True
        
        # Chercher le nœud précédent
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        
        return False
    
    def search(self, data):
        """Recherche un élément - O(n)"""
        current = self.head
        position = 0
        
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        
        return -1
    
    def reverse(self):
        """Inverse la liste - O(n)"""
        prev = None
        current = self.head
        
        while current:
            next_node = current.next  # Sauvegarder le suivant
            current.next = prev       # Inverser le lien
            prev = current            # Avancer prev
            current = next_node       # Avancer current
        
        self.head = prev
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        """Représentation textuelle"""
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return " → ".join(result) + " → None"
```

### Doubly Linked List

```python
class DNode:
    """Nœud doublement chaîné"""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    """Liste doublement chaînée"""
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def append(self, data):
        """Ajoute à la fin - O(1) avec tail pointer"""
        new_node = DNode(data)
        
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1
    
    def prepend(self, data):
        """Ajoute au début - O(1)"""
        new_node = DNode(data)
        
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.size += 1
    
    def reverse_traverse(self):
        """Parcours inversé (de tail à head)"""
        result = []
        current = self.tail
        while current:
            result.append(current.data)
            current = current.prev
        return result
```

## 4. Complexité Temporelle et Spatiale

### Complexité Spatiale
- **Liste chaînée** : O(n) - un nœud par élément
- **Overhead** : Chaque nœud nécessite espace pour données + pointeur(s)
  - Singly: 2 références (data + next)
  - Doubly: 3 références (data + next + prev)

### Complexité Temporelle

| Opération | Singly | Doubly |
|-----------|--------|--------|
| Append (avec tail) | O(1) | O(1) |
| Prepend | O(1) | O(1) |
| Insert at i | O(n) | O(n) |
| Delete at i | O(n) | O(n) |
| Search | O(n) | O(n) |
| Reverse | O(n) | O(n) |

## 5. Exemples Pratiques

### Exemple 1: Détection de Cycle (Floyd's Algorithm)

```python
def has_cycle(head):
    """Détecte si la liste contient un cycle - O(n) temps, O(1) espace"""
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next         # Avance de 1
        fast = fast.next.next    # Avance de 2
        
        if slow == fast:         # Rencontre = cycle
            return True
    
    return False
```

### Exemple 2: Trouver le Milieu

```python
def find_middle(head):
    """Trouve le nœud du milieu - O(n)"""
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow  # slow est au milieu quand fast atteint la fin
```

### Exemple 3: Fusionner Deux Listes Triées

```python
def merge_sorted_lists(l1, l2):
    """Fusionne deux listes triées - O(n + m)"""
    dummy = Node(0)  # Nœud factice
    current = dummy
    
    while l1 and l2:
        if l1.data <= l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    # Attacher le reste
    current.next = l1 if l1 else l2
    
    return dummy.next
```

### Exemple 4: Inverser par Groupes de K

```python
def reverse_k_group(head, k):
    """Inverse la liste par groupes de k nœuds"""
    # Vérifie s'il y a au moins k nœuds
    count = 0
    current = head
    while current and count < k:
        current = current.next
        count += 1
    
    if count < k:
        return head
    
    # Inverse les k premiers nœuds
    prev = None
    current = head
    for _ in range(k):
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    # Récursion pour le reste
    head.next = reverse_k_group(current, k)
    
    return prev
```

## 6. Exercices

### Exercice 1: Débutant
Implémentez une méthode `get(index)` qui retourne l'élément à la position `index`.

### Exercice 2: Intermédiaire
Supprimez tous les doublons d'une liste chaînée non triée.

### Exercice 3: Intermédiaire
Implémentez une fonction qui détermine si une liste chaînée est un palindrome.

### Exercice 4: Avancé
Trouvez le n-ième nœud en partant de la fin en un seul parcours.

### Exercice 5: Avancé
Implémentez une méthode pour aplatir une liste chaînée multi-niveaux.

## 7. Applications en Sécurité

### Buffer Management en Malware
Les malwares utilisent souvent des listes chaînées pour :
- Gérer des buffers de données exfiltrées
- Maintenir des listes de processus à injecter
- Chaîner des shellcodes modulaires

### Rootkit Hook Chains
```python
# Exemple conceptuel de chaîne de hooks
class Hook:
    def __init__(self, function_address, replacement):
        self.original_addr = function_address
        self.replacement = replacement
        self.next_hook = None  # Chaînage

# Permet de "stacker" plusieurs hooks sur une fonction
```

### Memory Forensics
En analyse forensique, comprendre les listes chaînées aide à :
- Parcourir les structures kernel (process lists)
- Analyser les pools de mémoire
- Détecter les rootkits (hidden processes)

## 8. Pièges Courants

### 1. Oublier de Libérer la Mémoire
```python
# ❌ Mauvais: fuite mémoire en C/C++
# En Python, pas de problème (garbage collector)
```

### 2. Perdre la Référence au Head
```python
# ❌ Erreur classique
def wrong_insert(head, data):
    new_node = Node(data)
    head = new_node  # Ne modifie PAS la liste originale!
    
# ✅ Correct
def correct_insert(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
```

### 3. Cycle Infini
```python
# ❌ Oubli de condition d'arrêt
current = head
while current:  # Boucle infinie si cycle
    current = current.next
```

### 4. Off-by-One Errors
```python
# Attention aux cas limites: liste vide, 1 élément, dernier élément
```

## 9. Ressources

### Plateformes de Pratique
- **LeetCode**: Problems tagged "Linked List"
- **HackerRank**: Data Structures - Linked Lists
- **CodeWars**: LinkedList Katas

### Lectures Complémentaires
- *Introduction to Algorithms* (CLRS) - Chapter 10
- *Cracking the Coding Interview* - Linked Lists chapter

### Visualizations
- [VisuAlgo](https://visualgo.net/en/list) - Visualisation interactive
- [Python Tutor](http://pythontutor.com/) - Exécution pas-à-pas

---

**Prochaine Étape** : Passez à `03_Stacks_Queues` pour voir comment les listes chaînées sont utilisées pour implémenter ces structures.
