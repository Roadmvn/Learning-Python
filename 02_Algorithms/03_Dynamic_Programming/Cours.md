# Cours : Programmation Dynamique (Dynamic Programming)

## 1. Introduction

La **programmation dynamique (DP)** est une technique d'optimisation qui résout des problèmes en les décomposant en sous-problèmes et en mémorisant leurs solutions pour éviter les calculs redondants.

### Pourquoi c'est important ?

- **Optimisation** : Transforme O(2^n) en O(n²) ou O(n)
- **Problèmes réels** : Optimisation de ressources, planification
- **Interviews** : Très fréquent dans les entretiens techniques
- **En sécurité** : Analyse de séquences, optimisation d'attaques

## 2. Quand Utiliser la DP ?

**Deux propriétés essentielles** :

### 1. Sous-structure Optimale
La solution optimale du problème contient les solutions optimales des sous-problèmes.

### 2. Sous-problèmes Qui Se Chevauchent
Les mêmes sous-problèmes sont résolus plusieurs fois.

```python
# Fibonacci illustre les deux propriétés
#
# fib(5) = fib(4) + fib(3)
#        = (fib(3) + fib(2)) + (fib(2) + fib(1))
#        = ((fib(2) + fib(1)) + (fib(1) + fib(0))) + ...
#
# fib(2) est calculé 3 fois! → Mémoriser!
```

## 3. Approches de la DP

### Top-Down (Mémorisation)

```python
def fib_memoization(n, memo={}):
    """Approche descendante avec mémo"""
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fib_memoization(n-1, memo) + fib_memoization(n-2, memo)
    return memo[n]
```

### Bottom-Up (Tabulation)

```python
def fib_tabulation(n):
    """Approche ascendante avec tableau"""
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]
```

### Optimisation de l'Espace

```python
def fib_optimized(n):
    """DP avec O(1) espace"""
    if n <= 1:
        return n
    
    prev2, prev1 = 0, 1
    
    for _ in range(2, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    
    return prev1
```

## 4. Problèmes Classiques

### Problème 1 : Climbing Stairs

```python
def climbing_stairs(n):
    """Nombre de façons de monter n marches (1 ou 2 à la fois)"""
    if n <= 2:
        return n
    
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

print(climbing_stairs(5))  # 8 façons
```

### Problème 2 : Coin Change (Problème du Rendu de Monnaie)

```python
def coin_change(coins, amount):
    """Nombre minimum de pièces pour faire amount"""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 0 pièces pour 0
    
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

print(coin_change([1, 2, 5], 11))  # 3 pièces (5+5+1)
```

### Problème 3 : Longest Common Subsequence (LCS)

```python
def lcs(text1, text2):
    """Plus longue sous-séquence commune"""
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

print(lcs("abcde", "ace"))  # 3 ("ace")
```

### Problème 4 : Knapsack (Sac à Dos)

```python
def knapsack(weights, values, capacity):
    """Problème du sac à dos 0-1"""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                # Prendre ou ne pas prendre l'objet i
                dp[i][w] = max(
                    values[i-1] + dp[i-1][w - weights[i-1]],  # Prendre
                    dp[i-1][w]  # Ne pas prendre
                )
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]

weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
print(knapsack(weights, values, 7))  # 9
```

### Problème 5 : Edit Distance (Levenshtein)

```python
def edit_distance(word1, word2):
    """Distance d'édition entre deux mots"""
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialisation
    for i in range(m + 1):
        dp[i][0] = i  # Supprimer tous
    for j in range(n + 1):
        dp[0][j] = j  # Insérer tous
    
    # Remplir la table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]  # Pas de coût
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # Supprimer
                    dp[i][j-1],    # Insérer
                    dp[i-1][j-1]   # Remplacer
                )
    
    return dp[m][n]

print(edit_distance("horse", "ros"))  # 3
```

### Problème 6 : Longest Increasing Subsequence

```python
def longest_increasing_subsequence(nums):
    """Plus longue sous-séquence croissante"""
    if not nums:
        return 0
    
    n = len(nums)
    dp = [1] * n  # Chaque élément forme une LIS de longueur 1
    
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

print(longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
```

### Problème 7 : Matrix Chain Multiplication

```python
def matrix_chain_order(dimensions):
    """Ordre optimal pour multiplier des matrices"""
    n = len(dimensions) - 1
    dp = [[0] * n for _ in range(n)]
    
    # L = longueur de la chaîne
    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            dp[i][j] = float('inf')
            
            for k in range(i, j):
                cost = (dp[i][k] + dp[k+1][j] + 
                       dimensions[i] * dimensions[k+1] * dimensions[j+1])
                dp[i][j] = min(dp[i][j], cost)
    
    return dp[0][n-1]

# Matrices: A(10x20), B(20x30), C(30x40)
dims = [10, 20, 30, 40]
print(matrix_chain_order(dims))  # 18000
```

## 5. Patterns de DP

### Pattern 1 : 1D DP (Séquence)
- Climbing Stairs
- House Robber
- Decode Ways

### Pattern 2 : 2D DP (Deux Séquences)
- Longest Common Subsequence
- Edit Distance
- Unique Paths

### Pattern 3 : Knapsack
- 0-1 Knapsack
- Subset Sum
- Partition Equal Subset Sum

### Pattern 4 : Intervalles
- Longest Palindromic Substring
- Matrix Chain Multiplication
- Burst Balloons

## 6. Applications en Sécurité

### Optimisation d'Attaque Brute Force

```python
def optimal_password_attack(char_sets, max_length, time_limit):
    """Trouve la stratégie optimale pour tester des mots de passe"""
    # char_sets = [(charset, time_per_char), ...]
    # DP pour maximiser la couverture dans le temps imparti
    
    dp = [[0] * (time_limit + 1) for _ in range(len(char_sets) + 1)]
    
    for i in range(1, len(char_sets) + 1):
        charset, time_cost = char_sets[i-1]
        for t in range(1, time_limit + 1):
            if time_cost <= t:
                dp[i][t] = max(
                    dp[i-1][t],
                    len(charset) + dp[i-1][t - time_cost]
                )
            else:
                dp[i][t] = dp[i-1][t]
    
    return dp[len(char_sets)][time_limit]
```

### Détection de Patterns dans Logs

```python
def detect_attack_pattern(logs, pattern):
    """Détecte un pattern d'attaque dans les logs avec DP"""
    # Similar à LCS mais avec des conditions spécifiques
    m, n = len(logs), len(pattern)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if logs[i-1] == pattern[j-1]:
                dp[i][j] = dp[i-1][j-1] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    
    return dp[m][n]
```

## 7. Conseils pour Résoudre des Problèmes DP

### Étape 1 : Identifier la DP
- Sous-problèmes qui se chevauchent ?
- Sous-structure optimale ?

### Étape 2 : Définir l'État
- `dp[i]` = ?
- `dp[i][j]` = ?

### Étape 3 : Trouver la Relation de Récurrence
- Comment `dp[i]` se rapporte à `dp[i-1]`, `dp[i-2]`, etc.

### Étape 4 : Gérer les Cas de Base
- `dp[0]`, `dp[1]` = ?

### Étape 5 : Déterminer l'Ordre de Calcul
- Bottom-up : Quelle boucle en premier ?

### Étape 6 : Optimiser l'Espace (si possible)
- Peut-on réduire de 2D à 1D ?

## 8. Exercices

### Exercice 1 : Débutant
Résolvez le problème du "House Robber" (maisons adjacentes ne peuvent pas être cambriolées).

### Exercice 2 : Intermédiaire
Trouvez le nombre de façons de faire une somme avec des pièces données (avec répétition).

### Exercice 3 : Intermédiaire
Calculez le plus long palindrome dans une chaîne.

### Exercice 4 : Avancé
Résolvez le problème du "Wildcard Matching" avec `*` et `?`.

### Exercice 5 : Avancé
Implémentez le problème "Burst Balloons" pour maximiser les points.

## 9. Ressources

### Plateformes
- **LeetCode** : Tag "Dynamic Programming" (150+ problèmes)
- **HackerRank** : Dynamic Programming
- **CSES Problem Set** : DP section

### Lectures
- *Introduction to Algorithms* (CLRS) - Chapitre 15
- *Dynamic Programming for Coding Interviews*

### Patterns
- [DP Patterns](https://leetcode.com/discuss/general-discussion/458695/dynamic-programming-patterns)

---

**Prochaine étape** : Passez à `04_Bit_Manipulation` pour les opérations binaires.
