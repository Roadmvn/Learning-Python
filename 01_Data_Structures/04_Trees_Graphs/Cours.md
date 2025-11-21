# Cours : Arbres & Graphes (Trees & Graphs)

## 1. Introduction

Les **arbres** et **graphes** sont des structures de données non-linéaires qui représentent des relations hiérarchiques et relationnelles. Ils sont essentiels pour modéliser des systèmes complexes.

### Pourquoi c'est important ?

- **Hiérarchies** : Systèmes de fichiers, DOM HTML, organigrammes
- **Réseaux** : Internet, réseaux sociaux, routage
- **Algorithmes** : Recherche, optimisation, IA
- **En sécurité** : Analyse de malware, graphes d'attaque, arbres de décision

## 2. Concepts Clés - Arbres

### Structure d'un Arbre

```
        1          ← racine (root)
       / \
      2   3        ← nœuds internes
     / \   \
    4   5   6      ← feuilles (leaves)
```

**Terminologie** :
- **Nœud (Node)** : Élément contenant des données
- **Racine (Root)** : Nœud de départ (pas de parent)
- **Feuille (Leaf)** : Nœud sans enfants
- **Hauteur** : Distance maximale racine → feuille
- **Profondeur** : Distance racine → nœud donné
- **Arête (Edge)** : Connexion entre deux nœuds

### Arbre Binaire (Binary Tree)

Chaque nœud a **au maximum 2 enfants** (gauche et droit).

```python
class TreeNode:
    """Nœud d'un arbre binaire"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __repr__(self):
        return f"TreeNode({self.value})"
```

### Arbre Binaire de Recherche (BST)

**Propriété** : Pour chaque nœud :
- Sous-arbre gauche : valeurs < nœud
- Sous-arbre droit : valeurs > nœud

```
        8
       / \
      3   10
     / \    \
    1   6   14
       / \  /
      4  7 13
```

```python
class BST:
    """Arbre Binaire de Recherche"""
    
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        """Insère une valeur - O(log n) moyen, O(n) pire cas"""
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)
    
    def search(self, value):
        """Recherche une valeur - O(log n) moyen"""
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)
```

### Parcours d'Arbres (Tree Traversal)

#### In-Order (Gauche → Racine → Droit)
```python
def inorder(node):
    """Pour BST: donne les valeurs triées"""
    if node:
        inorder(node.left)
        print(node.value, end=" ")
        inorder(node.right)
# Résultat: 1 3 4 6 7 8 10 13 14
```

#### Pre-Order (Racine → Gauche → Droit)
```python
def preorder(node):
    """Utile pour copier un arbre"""
    if node:
        print(node.value, end=" ")
        preorder(node.left)
        preorder(node.right)
# Résultat: 8 3 1 6 4 7 10 14 13
```

#### Post-Order (Gauche → Droit → Racine)
```python
def postorder(node):
    """Utile pour supprimer un arbre"""
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end=" ")
# Résultat: 1 4 7 6 3 13 14 10 8
```

#### Level-Order (BFS - Par niveaux)
```python
from collections import deque

def level_order(root):
    """Parcours en largeur - O(n)"""
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        result.append(node.value)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result
# Résultat: [8, 3, 10, 1, 6, 14, 4, 7, 13]
```

### Arbres Équilibrés (AVL, Red-Black)

**Problème du BST** : Peut devenir déséquilibré (liste chaînée) → O(n)

```
# BST déséquilibré (pire cas)
1
 \
  2
   \
    3
     \
      4
```

**Solution** : Arbres auto-équilibrés (AVL, Red-Black) garantissent O(log n).

## 3. Concepts Clés - Graphes

### Structure d'un Graphe

```
# Graphe orienté
  1 → 2
  ↓   ↓
  3 → 4

# Graphe non-orienté
  1 - 2
  |   |
  3 - 4
```

**Terminologie** :
- **Sommet (Vertex)** : Nœud du graphe
- **Arête (Edge)** : Connexion entre sommets
- **Orienté/Non-orienté** : Arêtes avec/sans direction
- **Pondéré** : Arêtes avec poids/coût
- **Cycle** : Chemin fermé
- **Connexe** : Tout sommet accessible depuis n'importe quel autre

### Représentations

#### Liste d'Adjacence (Recommandé)
```python
graph = {
    1: [2, 3],
    2: [4],
    3: [4],
    4: []
}
```

#### Matrice d'Adjacence
```python
# Pour n sommets: matrice n×n
graph = [
    [0, 1, 1, 0],  # 1 → 2, 3
    [0, 0, 0, 1],  # 2 → 4
    [0, 0, 0, 1],  # 3 → 4
    [0, 0, 0, 0]   # 4 → rien
]
```

### Implémentation d'un Graphe

```python
class Graph:
    """Graphe avec liste d'adjacence"""
    
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed
    
    def add_vertex(self, vertex):
        """Ajoute un sommet"""
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, from_vertex, to_vertex, weight=1):
        """Ajoute une arête"""
        if from_vertex not in self.graph:
            self.add_vertex(from_vertex)
        if to_vertex not in self.graph:
            self.add_vertex(to_vertex)
        
        self.graph[from_vertex].append((to_vertex, weight))
        
        if not self.directed:
            self.graph[to_vertex].append((from_vertex, weight))
    
    def get_neighbors(self, vertex):
        """Retourne les voisins d'un sommet"""
        return self.graph.get(vertex, [])
    
    def __str__(self):
        result = []
        for vertex, edges in self.graph.items():
            result.append(f"{vertex}: {edges}")
        return "\n".join(result)
```

## 4. Algorithmes de Parcours

### DFS (Depth-First Search - Profondeur)

```python
def dfs_recursive(graph, start, visited=None):
    """DFS récursif - O(V + E)"""
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start, end=" ")
    
    for neighbor, _ in graph.get_neighbors(start):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
    
    return visited

def dfs_iterative(graph, start):
    """DFS itératif avec stack - O(V + E)"""
    visited = set()
    stack = [start]
    
    while stack:
        vertex = stack.pop()
        
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=" ")
            
            for neighbor, _ in graph.get_neighbors(vertex):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return visited
```

### BFS (Breadth-First Search - Largeur)

```python
from collections import deque

def bfs(graph, start):
    """BFS avec queue - O(V + E)"""
    visited = set([start])
    queue = deque([start])
    
    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")
        
        for neighbor, _ in graph.get_neighbors(vertex):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return visited
```

## 5. Algorithmes Avancés

### Dijkstra (Plus Court Chemin)

```python
import heapq

def dijkstra(graph, start):
    """Algorithme de Dijkstra - O((V + E) log V)"""
    distances = {vertex: float('inf') for vertex in graph.graph}
    distances[start] = 0
    
    pq = [(0, start)]  # (distance, sommet)
    visited = set()
    
    while pq:
        current_dist, current = heapq.heappop(pq)
        
        if current in visited:
            continue
        
        visited.add(current)
        
        for neighbor, weight in graph.get_neighbors(current):
            distance = current_dist + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances
```

### Détection de Cycle

```python
def has_cycle_directed(graph):
    """Détecte un cycle dans un graphe orienté"""
    visited = set()
    rec_stack = set()
    
    def dfs(vertex):
        visited.add(vertex)
        rec_stack.add(vertex)
        
        for neighbor, _ in graph.get_neighbors(vertex):
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True  # Cycle détecté!
        
        rec_stack.remove(vertex)
        return False
    
    for vertex in graph.graph:
        if vertex not in visited:
            if dfs(vertex):
                return True
    
    return False
```

### Tri Topologique

```python
def topological_sort(graph):
    """Tri topologique - O(V + E)"""
    visited = set()
    stack = []
    
    def dfs(vertex):
        visited.add(vertex)
        
        for neighbor, _ in graph.get_neighbors(vertex):
            if neighbor not in visited:
                dfs(neighbor)
        
        stack.append(vertex)
    
    for vertex in graph.graph:
        if vertex not in visited:
            dfs(vertex)
    
    return stack[::-1]  # Inverser
```

## 6. Problèmes Classiques

### Problème 1 : Valider un BST

```python
def is_valid_bst(root, min_val=float('-inf'), max_val=float('inf')):
    """Vérifie si l'arbre est un BST valide"""
    if not root:
        return True
    
    if root.value <= min_val or root.value >= max_val:
        return False
    
    return (is_valid_bst(root.left, min_val, root.value) and
            is_valid_bst(root.right, root.value, max_val))
```

### Problème 2 : Ancêtre Commun le Plus Bas (LCA)

```python
def lowest_common_ancestor(root, p, q):
    """Trouve le LCA dans un BST"""
    if not root:
        return None
    
    if p.value < root.value and q.value < root.value:
        return lowest_common_ancestor(root.left, p, q)
    elif p.value > root.value and q.value > root.value:
        return lowest_common_ancestor(root.right, p, q)
    else:
        return root
```

### Problème 3 : Clone d'un Graphe

```python
def clone_graph(node):
    """Clone un graphe - O(V + E)"""
    if not node:
        return None
    
    clones = {}
    
    def dfs(node):
        if node in clones:
            return clones[node]
        
        clone = Node(node.value)
        clones[node] = clone
        
        for neighbor in node.neighbors:
            clone.neighbors.append(dfs(neighbor))
        
        return clone
    
    return dfs(node)
```

## 7. Applications en Sécurité

### Analyse de Graphe d'Attaque

```python
class AttackGraph:
    """Modélise les chemins d'attaque possibles"""
    
    def __init__(self):
        self.graph = Graph(directed=True)
    
    def add_vulnerability(self, from_state, to_state, exploit, severity):
        """Ajoute une vulnérabilité exploitable"""
        self.graph.add_edge(from_state, to_state, weight=severity)
    
    def find_attack_paths(self, start, target):
        """Trouve tous les chemins d'attaque vers une cible"""
        paths = []
        
        def dfs(current, path):
            if current == target:
                paths.append(path[:])
                return
            
            for neighbor, severity in self.graph.get_neighbors(current):
                if neighbor not in path:  # Éviter cycles
                    path.append(neighbor)
                    dfs(neighbor, path)
                    path.pop()
        
        dfs(start, [start])
        return paths
```

### Arbre de Décision pour Détection d'Intrusion

```python
class IDSDecisionTree:
    """Arbre de décision pour système de détection d'intrusion"""
    
    def __init__(self, feature, threshold=None):
        self.feature = feature
        self.threshold = threshold
        self.left = None   # condition False
        self.right = None  # condition True
        self.prediction = None  # pour feuilles
    
    def classify(self, packet):
        """Classifie un paquet réseau"""
        if self.prediction is not None:
            return self.prediction
        
        value = packet.get(self.feature)
        
        if value < self.threshold:
            return self.left.classify(packet) if self.left else "NORMAL"
        else:
            return self.right.classify(packet) if self.right else "ATTACK"

# Construction d'un arbre simple
root = IDSDecisionTree("packet_size", threshold=1500)
root.left = IDSDecisionTree("port", threshold=1024)
root.left.left = IDSDecisionTree(None)
root.left.left.prediction = "NORMAL"
root.left.right = IDSDecisionTree(None)
root.left.right.prediction = "SCAN"
```

## 8. Complexité

| Opération | BST moyen | BST pire | Graphe (liste adj) |
|-----------|-----------|----------|-------------------|
| Insertion | O(log n) | O(n) | O(1) |
| Recherche | O(log n) | O(n) | O(V + E) |
| Suppression | O(log n) | O(n) | O(E) |
| DFS/BFS | - | - | O(V + E) |
| Dijkstra | - | - | O((V+E) log V) |

## 9. Exercices

### Exercice 1 : Débutant
Calculez la hauteur maximale d'un arbre binaire.

### Exercice 2 : Intermédiaire
Vérifiez si un graphe est biparti (peut être coloré avec 2 couleurs).

### Exercice 3 : Intermédiaire
Trouvez le diamètre d'un arbre binaire (plus long chemin entre deux feuilles).

### Exercice 4 : Avancé
Implémentez l'algorithme de Kruskal pour l'arbre couvrant minimal.

### Exercice 5 : Avancé
Trouvez tous les chemins de la racine aux feuilles dont la somme égale une valeur donnée.

## 10. Ressources

### Plateformes
- **LeetCode** : Trees, Graphs, BFS, DFS
- **HackerRank** : Trees, Graph Theory
- **CodeWars** : Tree/Graph Katas

### Lectures
- *Introduction to Algorithms* (CLRS) - Chapitres 10, 12, 22
- *Algorithms* de Robert Sedgewick

### Visualisations
- [VisuAlgo](https://visualgo.net/) - BST, Graphe, Dijkstra
- [Graph Online](https://graphonline.ru/) - Créer et visualiser graphes

---

**Prochaine étape** : Passez à `05_Hash_Maps` pour le stockage clé-valeur efficace.
