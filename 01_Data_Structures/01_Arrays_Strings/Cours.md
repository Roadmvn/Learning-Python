# Cours : Tableaux & Chaînes de Caractères

## 1. Introduction

Les **tableaux (arrays)** et **chaînes de caractères (strings)** sont des structures de données fondamentales qui stockent des éléments en mémoire contiguë. En Python, les listes servent de tableaux dynamiques, tandis que les strings sont des séquences immuables de caractères.

### Pourquoi c'est important ?

- **Accès direct O(1)** : Accès instantané à n'importe quel élément via son index
- **Cache-friendly** : Mémoire contiguë = meilleure performance CPU
- **Fondation** : Base de presque toutes les autres structures de données
- **En sécurité** : Buffer overflows, injection SQL, XSS exploitent ces structures

## 2. Concepts Clés

### Tableaux (Arrays/Lists en Python)

#### Caractéristiques
```
Index:  0    1    2    3    4
Array: [10, 20, 30, 40, 50]
        ↑                  ↑
      début              fin
```

- **Indexation** : Commence à 0
- **Taille dynamique** en Python (contrairement au C)
- **Types mixtes** possibles : `[1, "hello", 3.14]`
- **Slicing** puissant : `arr[start:end:step]`

#### Complexité Temporelle

| Opération | Complexité | Explication |
|-----------|-----------|-------------|
| Accès `arr[i]` | O(1) | Calcul direct : base + i × taille_element |
| Recherche | O(n) | Doit parcourir tous les éléments |
| Insertion début | O(n) | Doit décaler tous les éléments |
| Insertion fin | O(1) amortisé | Redimensionnement occasionnel |
| Suppression début | O(n) | Décalage nécessaire |
| Suppression fin | O(1) | Pas de décalage |

### Chaînes de Caractères (Strings)

#### Caractéristiques
```python
s = "Hello"
# Index:  0  1  2  3  4
#        'H' 'e' 'l' 'l' 'o'
# Négatif: -5 -4 -3 -2 -1
```

- **Immuables** : Toute modification crée une nouvelle string
- **Encodage** : UTF-8 par défaut en Python 3
- **Itérables** : Peuvent être parcourues caractère par caractère

## 3. Opérations Essentielles en Python

### Manipulation de Listes

```python
# Création
arr = [1, 2, 3, 4, 5]
arr_empty = []
arr_repeat = [0] * 10  # [0, 0, 0, ..., 0]

# Accès
premier = arr[0]     # 1
dernier = arr[-1]    # 5
milieu = arr[len(arr)//2]  # 3

# Slicing
sous_liste = arr[1:4]     # [2, 3, 4]
inverse = arr[::-1]       # [5, 4, 3, 2, 1]
pairs = arr[::2]          # [1, 3, 5]

# Modification
arr[0] = 100             # [100, 2, 3, 4, 5]
arr.append(6)            # Ajouter à la fin
arr.insert(0, 99)        # Insérer au début
arr.extend([7, 8])       # Concaténer une liste
arr.remove(3)            # Supprimer première occurrence de 3
popped = arr.pop()       # Retirer et retourner le dernier
del arr[1]               # Supprimer par index

# Recherche
index = arr.index(4)     # Trouve l'index de 4
existe = 5 in arr        # True/False
compte = arr.count(2)    # Nombre d'occurrences

# Tri
arr.sort()               # Tri en place
sorted_arr = sorted(arr) # Retourne nouvelle liste triée
arr.reverse()            # Inverse en place
```

### Manipulation de Strings

```python
s = "Hello World"

# Accès
premiere = s[0]          # 'H'
derniere = s[-1]         # 'd'

# Slicing
sous_str = s[0:5]        # "Hello"
inverse = s[::-1]        # "dlroW olleH"

# Méthodes courantes
upper = s.upper()        # "HELLO WORLD"
lower = s.lower()        # "hello world"
titre = s.title()        # "Hello World"
strip = "  test  ".strip()  # "test"

# Recherche
index = s.find("World")  # 6 (ou -1 si non trouvé)
existe = "Hello" in s    # True
compte = s.count("l")    # 3

# Division/Jonction
mots = s.split(" ")      # ['Hello', 'World']
joint = "-".join(mots)   # "Hello-World"

# Remplacement
remplace = s.replace("World", "Python")  # "Hello Python"

# Vérifications
s.startswith("Hello")    # True
s.endswith("World")      # True
"123".isdigit()          # True
"abc".isalpha()          # True
```

## 4. Techniques Avancées

### Two Pointers (Deux Pointeurs)

Technique puissante pour résoudre des problèmes en O(n) au lieu de O(n²).

```python
def is_palindrome(s):
    """Vérifie si une string est un palindrome - O(n)"""
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

def remove_duplicates(arr):
    """Supprime les doublons d'un tableau trié en place - O(n)"""
    if not arr:
        return 0
    
    write = 1  # Position d'écriture
    
    for read in range(1, len(arr)):
        if arr[read] != arr[read-1]:
            arr[write] = arr[read]
            write += 1
    
    return write  # Nouvelle longueur
```

### Sliding Window (Fenêtre Glissante)

Pour problèmes de sous-séquences/sous-tableaux.

```python
def max_sum_subarray(arr, k):
    """Somme maximale d'un sous-tableau de taille k - O(n)"""
    if len(arr) < k:
        return None
    
    # Calculer somme de la première fenêtre
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Faire glisser la fenêtre
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

def longest_substring_without_repeating(s):
    """Longueur de la plus longue sous-string sans répétition - O(n)"""
    char_index = {}
    max_length = 0
    start = 0
    
    for end, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        
        char_index[char] = end
        max_length = max(max_length, end - start + 1)
    
    return max_length
```

### Manipulation de Matrices (2D Arrays)

```python
# Créer une matrice 3x3
matrix = [[0]*3 for _ in range(3)]

# Parcourir une matrice
def traverse_matrix(matrix):
    """Parcours ligne par ligne"""
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=" ")
        print()

def rotate_90(matrix):
    """Rotation de 90° dans le sens horaire - O(n²)"""
    n = len(matrix)
    
    # Transposer (échanger matrix[i][j] et matrix[j][i])
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Inverser chaque ligne
    for row in matrix:
        row.reverse()

def spiral_order(matrix):
    """Parcours en spirale - O(m×n)"""
    result = []
    
    while matrix:
        result += matrix.pop(0)  # Première ligne
        
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())  # Dernière colonne
        
        if matrix:
            result += matrix.pop()[::-1]  # Dernière ligne inversée
        
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))  # Première colonne (bas vers haut)
    
    return result
```

## 5. Problèmes Classiques

### Problème 1 : Trouver les doublons

```python
def find_duplicates(arr):
    """Trouve tous les doublons - O(n) temps, O(n) espace"""
    seen = set()
    duplicates = set()
    
    for num in arr:
        if num in seen:
            duplicates.add(num)
        seen.add(num)
    
    return list(duplicates)

# Version O(1) espace pour array de [1..n]
def find_duplicates_constant_space(arr):
    """Utilise les indices comme marqueurs"""
    duplicates = []
    
    for num in arr:
        index = abs(num) - 1
        if arr[index] < 0:
            duplicates.append(abs(num))
        else:
            arr[index] = -arr[index]
    
    return duplicates
```

### Problème 2 : Réorganisation

```python
def move_zeros(arr):
    """Déplace tous les 0 à la fin - O(n)"""
    write = 0
    
    for read in range(len(arr)):
        if arr[read] != 0:
            arr[write], arr[read] = arr[read], arr[write]
            write += 1

def dutch_flag_problem(arr):
    """Trie un tableau de 0, 1, 2 - O(n), O(1) espace"""
    low, mid, high = 0, 0, len(arr) - 1
    
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
```

### Problème 3 : Sous-tableaux

```python
def max_subarray_sum(arr):
    """Algorithme de Kadane - O(n)"""
    max_current = max_global = arr[0]
    
    for num in arr[1:]:
        max_current = max(num, max_current + num)
        max_global = max(max_global, max_current)
    
    return max_global

def product_except_self(arr):
    """Produit de tous les éléments sauf soi-même - O(n)"""
    n = len(arr)
    result = [1] * n
    
    # Produits à gauche
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= arr[i]
    
    # Produits à droite
    right_product = 1
    for i in range(n-1, -1, -1):
        result[i] *= right_product
        right_product *= arr[i]
    
    return result
```

## 6. Applications en Sécurité

### Buffer Overflow Detection

```python
def check_buffer_overflow(input_data, buffer_size):
    """Vérifie si l'input risque de causer un buffer overflow"""
    if len(input_data) > buffer_size:
        return True, f"Risque: {len(input_data)} bytes > {buffer_size} bytes"
    
    # Vérifier caractères dangereux
    dangerous_chars = ['\x00', '\xff', '\x90']  # NULL, 0xFF, NOP sled
    for char in dangerous_chars:
        if char in input_data:
            return True, f"Caractère dangereux détecté: {repr(char)}"
    
    return False, "Input sûr"
```

### String Injection Prevention

```python
import re

def sanitize_sql_input(user_input):
    """Nettoie l'input pour prévenir les injections SQL"""
    # Échapper les caractères spéciaux
    dangerous_patterns = [
        r"('\s*OR\s*'1'\s*=\s*'1)",  # ' OR '1'='1
        r"(--)",                      # Commentaire SQL
        r"(;)",                       # Séparateur de commandes
        r"(UNION\s+SELECT)",          # Union attack
    ]
    
    for pattern in dangerous_patterns:
        if re.search(pattern, user_input, re.IGNORECASE):
            return None, "Input dangereux détecté"
    
    # Échapper les apostrophes
    sanitized = user_input.replace("'", "''")
    
    return sanitized, "OK"

def detect_xss(input_string):
    """Détecte les tentatives de Cross-Site Scripting"""
    xss_patterns = [
        r"<script",
        r"javascript:",
        r"onerror=",
        r"onclick=",
    ]
    
    for pattern in xss_patterns:
        if re.search(pattern, input_string, re.IGNORECASE):
            return True
    
    return False
```

### Pattern Matching (KMP Algorithm)

```python
def kmp_search(text, pattern):
    """Algorithme KMP pour recherche de motif - O(n+m)"""
    def compute_lps(pattern):
        """Calcule le tableau Longest Proper Prefix which is also Suffix"""
        lps = [0] * len(pattern)
        length = 0
        i = 1
        
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        return lps
    
    lps = compute_lps(pattern)
    matches = []
    
    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        
        if j == len(pattern):
            matches.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return matches
```

## 7. Pièges Courants

### 1. Modification pendant l'itération
```python
# ❌ MAUVAIS
arr = [1, 2, 3, 4]
for i in range(len(arr)):
    arr.append(i)  # Boucle infinie!

# ✅ BON
arr = [1, 2, 3, 4]
original_length = len(arr)
for i in range(original_length):
    arr.append(i)
```

### 2. Slicing crée des copies
```python
# ❌ Inefficace pour grandes listes
def process(arr):
    while arr:
        element = arr[0]
        arr = arr[1:]  # O(n) à chaque itération!

# ✅ Utiliser un index
def process(arr):
    i = 0
    while i < len(arr):
        element = arr[i]
        i += 1
```

### 3. Strings immuables
```python
# ❌ O(n²) - crée n strings intermédiaires
result = ""
for char in "hello":
    result += char

# ✅ O(n) - utiliser une liste
result = []
for char in "hello":
    result.append(char)
final = "".join(result)
```

## 8. Exercices

### Exercice 1 : Débutant
Écrivez une fonction qui inverse un tableau sans utiliser de tableau auxiliaire.

### Exercice 2 : Intermédiaire
Trouvez les trois nombres dans un tableau dont la somme est la plus proche d'une cible donnée.

### Exercice 3 : Intermédiaire
Implémentez une fonction qui compresse une string : `"aaabbc" → "a3b2c1"`.

### Exercice 4 : Avancé
Trouvez le plus petit sous-tableau dont la somme est supérieure ou égale à un nombre donné.

### Exercice 5 : Avancé
Implémentez l'algorithme de Rabin-Karp pour la recherche de motif dans un texte.

## 9. Ressources

### Plateformes de pratique
- **LeetCode** : Sections "Array" et "String"
- **HackerRank** : Data Structures - Arrays
- **CodeWars** : Katas sur les tableaux

### Lectures complémentaires
- *Introduction to Algorithms* (CLRS) - Chapitre 2
- *Cracking the Coding Interview* - Chapitres Arrays et Strings

### Outils de visualisation
- [Python Tutor](http://pythontutor.com/) - Visualisation d'exécution
- [VisuAlgo](https://visualgo.net/) - Visualisation d'algorithmes

---

**Prochaine étape** : Passez à `02_Linked_Lists` pour voir comment gérer la mémoire de manière dynamique.
