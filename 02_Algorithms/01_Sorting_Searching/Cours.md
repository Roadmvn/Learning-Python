# Cours : Tri & Recherche (Sorting & Searching)

## 1. Introduction

Les **algorithmes de tri** organisent les données dans un ordre spécifique, tandis que les **algorithmes de recherche** localisent des éléments dans des collections. Ces opérations sont fondamentales en informatique.

### Pourquoi c'est important ?

- **Optimisation** : Données triées = recherche plus rapide
- **Prétraitement** : Beaucoup d'algorithmes nécessitent des données triées
- **Performance** : Choix du bon algorithme = gain énorme
- **En sécurité** : Analyse de logs, détection d'anomalies, forensics

## 2. Algorithmes de Tri

### Tri à Bulles (Bubble Sort) - O(n²)

```python
def bubble_sort(arr):
    """Tri à bulles - Simple mais inefficace"""
    n = len(arr)
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # Optimisation : arrêter si déjà trié
        if not swapped:
            break
    
    return arr

# Test
print(bubble_sort([64, 34, 25, 12, 22]))  # [12, 22, 25, 34, 64]
```

### Tri par Sélection (Selection Sort) - O(n²)

```python
def selection_sort(arr):
    """Sélectionne le minimum et le place au début"""
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr
```

### Tri par Insertion (Insertion Sort) - O(n²)

```python
def insertion_sort(arr):
    """Insère chaque élément à sa place dans la partie triée"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Décaler les éléments > key vers la droite
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr
```

### Tri Fusion (Merge Sort) - O(n log n)

```python
def merge_sort(arr):
    """Tri par fusion - Diviser pour régner"""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    """Fusionne deux tableaux triés"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Test
print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
```

### Tri Rapide (Quick Sort) - O(n log n) moyen

```python
def quick_sort(arr):
    """Tri rapide - Très performant en pratique"""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Version en place (plus efficace en mémoire)
def quick_sort_inplace(arr, low=0, high=None):
    """Quick sort en place - O(log n) espace"""
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort_inplace(arr, low, pivot_index - 1)
        quick_sort_inplace(arr, pivot_index + 1, high)
    
    return arr

def partition(arr, low, high):
    """Partitionne autour du pivot"""
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
```

### Tri par Tas (Heap Sort) - O(n log n)

```python
def heap_sort(arr):
    """Tri par tas - Utilise une heap binaire"""
    n = len(arr)
    
    # Construire max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extraire éléments un par un
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap
        heapify(arr, i, 0)
    
    return arr

def heapify(arr, n, i):
    """Maintient la propriété de max heap"""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
```

### Tri par Comptage (Counting Sort) - O(n + k)

```python
def counting_sort(arr):
    """Tri par comptage - Efficace pour petites valeurs entières"""
    if not arr:
        return arr
    
    # Trouver min et max
    min_val, max_val = min(arr), max(arr)
    range_size = max_val - min_val + 1
    
    # Compter les occurrences
    count = [0] * range_size
    for num in arr:
        count[num - min_val] += 1
    
    # Reconstruire le tableau trié
    result = []
    for i, freq in enumerate(count):
        result.extend([i + min_val] * freq)
    
    return result

# Test
print(counting_sort([4, 2, 2, 8, 3, 3, 1]))  # [1, 2, 2, 3, 3, 4, 8]
```

## 3. Comparaison des Algorithmes de Tri

| Algorithme | Temps (moyen) | Temps (pire) | Espace | Stable | Utilisation |
|-----------|--------------|--------------|--------|--------|-------------|
| Bubble Sort | O(n²) | O(n²) | O(1) | Oui | Pédagogique uniquement |
| Selection Sort | O(n²) | O(n²) | O(1) | Non | Petits tableaux |
| Insertion Sort | O(n²) | O(n²) | O(1) | Oui | Presque trié |
| Merge Sort | O(n log n) | O(n log n) | O(n) | Oui | Usage général |
| Quick Sort | O(n log n) | O(n²) | O(log n) | Non | Usage général (rapide) |
| Heap Sort | O(n log n) | O(n log n) | O(1) | Non | Garantie temps |
| Counting Sort | O(n + k) | O(n + k) | O(k) | Oui | Entiers limités |

**Stable** = L'ordre relatif des éléments égaux est préservé

## 4. Algorithmes de Recherche

### Recherche Linéaire - O(n)

```python
def linear_search(arr, target):
    """Recherche simple - Fonctionne sur tout tableau"""
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

# Test
print(linear_search([3, 1, 4, 1, 5], 4))  # 2
```

### Recherche Binaire - O(log n)

```python
def binary_search(arr, target):
    """Recherche binaire - Nécessite tableau trié"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Version récursive
def binary_search_recursive(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Test
print(binary_search([1, 3, 5, 7, 9, 11], 7))  # 3
```

### Recherche de la Première/Dernière Occurrence

```python
def find_first_occurrence(arr, target):
    """Trouve la première occurrence - O(log n)"""
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continuer à chercher à gauche
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

def find_last_occurrence(arr, target):
    """Trouve la dernière occurrence - O(log n)"""
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Continuer à chercher à droite
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

# Test
arr = [1, 2, 2, 2, 3, 4]
print(find_first_occurrence(arr, 2))  # 1
print(find_last_occurrence(arr, 2))   # 3
```

### Recherche dans un Tableau Rotaté

```python
def search_rotated(arr, target):
    """Recherche dans un tableau trié puis rotaté - O(log n)"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        
        # Déterminer quel côté est trié
        if arr[left] <= arr[mid]:  # Gauche est trié
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Droite est trié
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

# Test
print(search_rotated([4, 5, 6, 7, 0, 1, 2], 0))  # 4
```

## 5. Problèmes Classiques

### Problème 1 : Trouver le K-ième Plus Grand Élément

```python
import heapq

def find_kth_largest(nums, k):
    """Trouve le k-ième plus grand élément - O(n log k)"""
    # Utiliser min heap de taille k
    heap = nums[:k]
    heapq.heapify(heap)
    
    for num in nums[k:]:
        if num > heap[0]:
            heapq.heapreplace(heap, num)
    
    return heap[0]

# Test
print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))  # 5
```

### Problème 2 : Fusionner K Listes Triées

```python
def merge_k_sorted_lists(lists):
    """Fusionne k listes triées - O(n log k)"""
    import heapq
    
    result = []
    heap = []
    
    # Initialiser heap avec premier élément de chaque liste
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))
    
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        
        # Ajouter le prochain élément de la même liste
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
    
    return result

# Test
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
print(merge_k_sorted_lists(lists))  # [1, 1, 2, 3, 4, 4, 5, 6]
```

### Problème 3 : Recherche de Pic

```python
def find_peak_element(arr):
    """Trouve un pic (élément > voisins) - O(log n)"""
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] < arr[mid + 1]:
            left = mid + 1  # Pic est à droite
        else:
            right = mid  # Pic est à gauche ou mid
    
    return left

# Test
print(find_peak_element([1, 2, 3, 1]))  # 2 (pic = 3)
```

## 6. Applications en Sécurité

### Analyse de Logs (Recherche Temporelle)

```python
def find_log_entries_in_timerange(logs, start_time, end_time):
    """Trouve les logs dans une plage de temps - O(log n + k)"""
    # logs = liste triée de (timestamp, message)
    
    def find_first_ge(target):
        """Trouve le premier >= target"""
        left, right = 0, len(logs) - 1
        result = len(logs)
        
        while left <= right:
            mid = (left + right) // 2
            if logs[mid][0] >= target:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result
    
    start_idx = find_first_ge(start_time)
    end_idx = find_first_ge(end_time + 1)
    
    return logs[start_idx:end_idx]
```

### Détection d'Anomalies (Médiane Glissante)

```python
from sortedcontainers import SortedList

def median_of_sliding_window(nums, k):
    """Calcule la médiane de chaque fenêtre - O(n log k)"""
    window = SortedList(nums[:k])
    medians = []
    
    def get_median():
        mid = k // 2
        if k % 2 == 0:
            return (window[mid - 1] + window[mid]) / 2
        return window[mid]
    
    medians.append(get_median())
    
    for i in range(k, len(nums)):
        window.remove(nums[i - k])
        window.add(nums[i])
        medians.append(get_median())
    
    return medians
```

## 7. Exercices

### Exercice 1 : Débutant
Implémentez le tri par insertion de manière optimale pour les tableaux presque triés.

### Exercice 2 : Intermédiaire
Trouvez la médiane de deux tableaux triés en O(log(min(m, n))).

### Exercice 3 : Intermédiaire
Triez un tableau de 0, 1, et 2 en un seul parcours (Dutch National Flag).

### Exercice 4 : Avancé
Trouvez le plus petit intervalle couvrant au moins un nombre de chaque liste.

### Exercice 5 : Avancé
Implémentez le tri externe pour des données plus grandes que la mémoire disponible.

## 8. Ressources

### Plateformes
- **LeetCode** : Tags "Sorting", "Binary Search"
- **HackerRank** : Sorting, Searching
- **Visualgo** : [https://visualgo.net/en/sorting](https://visualgo.net/en/sorting)

### Lectures
- *Introduction to Algorithms* (CLRS) - Chapitres 2, 6-8
- *The Algorithm Design Manual* - Steven Skiena

---

**Prochaine étape** : Passez à `02_Recursion` pour maîtriser la récursivité.
