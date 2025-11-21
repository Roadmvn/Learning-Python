# Cours : Récursivité (Recursion)

## 1. Introduction

La **récursivité** est une technique où une fonction s'appelle elle-même pour résoudre un problème en le décomposant en sous-problèmes plus petits.

### Pourquoi c'est important ?

- **Simplicité** : Code plus court et élégant
- **Arbres/Graphes** : Parcours naturel de structures récursives
- **Diviser pour régner** : Base de nombreux algorithmes
- **En sécurité** : Analyse de malware, traversée de systèmes de fichiers

## 2. Anatomie d'une Fonction Récursive

```python
def recursion(parameters):
    # 1. CAS DE BASE (condition d'arrêt)
    if condition_base:
        return valeur_simple
    
    # 2. APPEL RÉCURSIF (vers le cas de base)
    return recursion(parameters_modifies)
```

### Exemple : Factorielle

```python
def factorial(n):
    """Calcule n! récursivement"""
    # Cas de base
    if n == 0 or n == 1:
        return 1
    
    # Appel récursif
    return n * factorial(n - 1)

# factorial(5) = 5 * factorial(4)
#              = 5 * 4 * factorial(3)
#              = 5 * 4 * 3 * factorial(2)
#              = 5 * 4 * 3 * 2 * factorial(1)
#              = 5 * 4 * 3 * 2 * 1 = 120
```

## 3. Types de Récursivité

### Récursivité Simple (Linéaire)

```python
def sum_list(arr):
    """Somme d'une liste - récursion linéaire"""
    if not arr:
        return 0
    return arr[0] + sum_list(arr[1:])

def countdown(n):
    """Compte à rebours"""
    if n <= 0:
        print("Go!")
        return
    print(n)
    countdown(n - 1)
```

### Récursivité Multiple

```python
def fibonacci(n):
    """Suite de Fibonacci - deux appels récursifs"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Arbre d'appels pour fib(5):
#                fib(5)
#              /        \
#         fib(4)        fib(3)
#         /    \        /    \
#     fib(3)  fib(2)  fib(2) fib(1)
#     /   \    /  \    /  \
# fib(2) fib(1) ... ...  ...
```

### Récursivité Terminale (Tail Recursion)

```python
def factorial_tail(n, accumulator=1):
    """Factorielle avec récursion terminale"""
    if n == 0:
        return accumulator
    return factorial_tail(n - 1, n * accumulator)

# Optimisable en boucle par le compilateur
```

## 4. Récursivité vs Itération

```python
# RÉCURSIF
def sum_recursive(n):
    if n == 0:
        return 0
    return n + sum_recursive(n - 1)

# ITÉRATIF
def sum_iterative(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Avantages Récursivité:
# - Code plus élégant
# - Naturel pour structures récursives
# 
# Inconvénients:
# - Overhead de la pile d'appels
# - Risque de stack overflow
# - Moins performant
```

## 5. Problèmes Classiques

### Problème 1 : Tours de Hanoï

```python
def hanoi(n, source, target, auxiliary):
    """Tours de Hanoï - O(2^n)"""
    if n == 1:
        print(f"Déplacer disque 1 de {source} vers {target}")
        return
    
    # Déplacer n-1 disques vers auxiliaire
    hanoi(n - 1, source, auxiliary, target)
    
    # Déplacer le plus grand vers target
    print(f"Déplacer disque {n} de {source} vers {target}")
    
    # Déplacer n-1 disques d'auxiliaire vers target
    hanoi(n - 1, auxiliary, target, source)

hanoi(3, 'A', 'C', 'B')
```

### Problème 2 : Permutations

```python
def permutations(arr):
    """Génère toutes les permutations - O(n!)"""
    if len(arr) <= 1:
        return [arr]
    
    result = []
    for i in range(len(arr)):
        rest = arr[:i] + arr[i+1:]
        for perm in permutations(rest):
            result.append([arr[i]] + perm)
    
    return result

print(permutations([1, 2, 3]))
# [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
```

### Problème 3 : Subsets (Ensembles de Parties)

```python
def subsets(arr):
    """Génère tous les sous-ensembles - O(2^n)"""
    if not arr:
        return [[]]
    
    first = arr[0]
    rest_subsets = subsets(arr[1:])
    
    # Ajouter le premier élément à chaque subset
    new_subsets = [[first] + subset for subset in rest_subsets]
    
    return rest_subsets + new_subsets

print(subsets([1, 2, 3]))
# [[], [3], [2], [2,3], [1], [1,3], [1,2], [1,2,3]]
```

### Problème 4 : Backtracking - N-Queens

```python
def solve_n_queens(n):
    """Résout le problème des N reines"""
    def is_safe(board, row, col):
        # Vérifier la colonne
        for i in range(row):
            if board[i] == col:
                return False
            # Vérifier les diagonales
            if abs(board[i] - col) == abs(i - row):
                return False
        return True
    
    def solve(board, row):
        if row == n:
            solutions.append(board[:])
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve(board, row + 1)
                board[row] = -1  # Backtrack
    
    solutions = []
    solve([-1] * n, 0)
    return solutions

print(f"Solutions pour 4 reines: {len(solve_n_queens(4))}")  # 2
```

### Problème 5 : Génération de Parenthèses

```python
def generate_parentheses(n):
    """Génère toutes les combinaisons valides de n paires de parenthèses"""
    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:
            result.append(current)
            return
        
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)
        
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)
    
    result = []
    backtrack('', 0, 0)
    return result

print(generate_parentheses(3))
# ['((()))', '(()())', '(())()', '()(())', '()()()']
```

## 6. Mémorisation (Memoization)

```python
# ❌ Fibonacci naïf - O(2^n) très lent
def fib_slow(n):
    if n <= 1:
        return n
    return fib_slow(n - 1) + fib_slow(n - 2)

# ✅ Fibonacci avec mémorisation - O(n)
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

# ✅ Avec décorateur Python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_cached(n):
    if n <= 1:
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)

print(fib_cached(100))  # Instantané!
```

## 7. Applications en Sécurité

### Traversée de Système de Fichiers

```python
import os

def find_suspicious_files(directory, patterns=['.exe', '.dll', '.bat']):
    """Trouve récursivement les fichiers suspects"""
    suspicious = []
    
    def search(path):
        try:
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                
                if os.path.isdir(item_path):
                    search(item_path)  # Récursion
                elif any(item.endswith(p) for p in patterns):
                    suspicious.append(item_path)
        except PermissionError:
            pass
    
    search(directory)
    return suspicious
```

### Analyse de JSON Imbriqué (Malware Config)

```python
def extract_urls_recursive(data):
    """Extrait récursivement toutes les URLs d'une structure JSON"""
    urls = []
    
    if isinstance(data, dict):
        for key, value in data.items():
            if key == 'url' and isinstance(value, str):
                urls.append(value)
            else:
                urls.extend(extract_urls_recursive(value))
    
    elif isinstance(data, list):
        for item in data:
            urls.extend(extract_urls_recursive(item))
    
    return urls

# Exemple: config de malware
malware_config = {
    "c2_servers": [
        {"url": "http://evil1.com", "port": 443},
        {"url": "http://evil2.com", "backup": {"url": "http://evil3.com"}}
    ]
}

print(extract_urls_recursive(malware_config))
```

## 8. Pièges Courants

### 1. Pas de Cas de Base

```python
# ❌ Récursion infinie!
def infinite():
    return infinite()

# ✅ Toujours avoir un cas de base
def correct(n):
    if n == 0:  # Cas de base
        return
    correct(n - 1)
```

### 2. Stack Overflow

```python
# ❌ Python limite la profondeur de récursion
import sys
print(sys.getrecursionlimit())  # 1000 par défaut

def deep_recursion(n):
    if n == 0:
        return
    deep_recursion(n - 1)

# deep_recursion(2000)  # RecursionError!

# ✅ Augmenter la limite (avec précaution)
sys.setrecursionlimit(5000)

# ✅ Ou mieux: convertir en itératif
def iterative_version(n):
    while n > 0:
        n -= 1
```

### 3. Création Inutile d'Objets

```python
# ❌ Inefficace - crée beaucoup de listes
def sum_list_bad(arr):
    if not arr:
        return 0
    return arr[0] + sum_list_bad(arr[1:])  # Copie O(n)

# ✅ Utiliser des indices
def sum_list_good(arr, index=0):
    if index >= len(arr):
        return 0
    return arr[index] + sum_list_good(arr, index + 1)
```

## 9. Exercices

### Exercice 1 : Débutant
Calculez la puissance x^n en utilisant la récursivité.

### Exercice 2 : Intermédiaire
Inversez une liste chaînée de manière récursive.

### Exercice 3 : Intermédiaire
Implémentez le tri fusion (merge sort) récursivement.

### Exercice 4 : Avancé
Résolvez le problème du Sudoku avec backtracking.

### Exercice 5 : Avancé
Implémentez un interpréteur d'expressions arithmétiques récursif.

## 10. Ressources

### Plateformes
- **LeetCode** : Tag "Recursion", "Backtracking"
- **HackerRank** : Recursion section
- **CodeWars** : Recursion Katas

### Lectures
- *Introduction to Algorithms* (CLRS) - Chapitre 4
- *Structure and Interpretation of Computer Programs* (SICP)

### Visualisations
- [Python Tutor](http://pythontutor.com/) - Visualiser la pile d'appels
- [Recursion Tree Visualizer](https://recursion.now.sh/)

---

**Prochaine étape** : Passez à `03_Dynamic_Programming` pour optimiser les problèmes récursifs.
