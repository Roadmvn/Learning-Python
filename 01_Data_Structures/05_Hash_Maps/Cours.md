# Cours : Tables de Hachage (Hash Maps)

## 1. Introduction

Les **tables de hachage** (hash maps, dictionnaires en Python) sont des structures de données qui associent des **clés** à des **valeurs**, offrant un accès en temps constant O(1) en moyenne.

### Pourquoi c'est important ?

- **Performance** : Accès/insertion/suppression en O(1) moyen
- **Omniprésent** : Bases de données, caches, indexation
- **Problèmes** : Comptage, groupement, mémorisation
- **En sécurité** : Rainbow tables, caches d'attaque, stockage de credentials

## 2. Concepts Clés

### Fonctionnement d'une Hash Map

```
Clé → Fonction de Hachage → Index → Valeur

"john" → hash("john") % 10 → 3 → "john@email.com"
```

#### Processus
1. **Clé** : Donnée d'entrée (ex: "john")
2. **Hash Function** : Convertit la clé en nombre
3. **Index** : `hash(clé) % taille_table`
4. **Bucket** : Emplacement pour stocker la valeur

```
Index:  0    1    2    3         4    5
Table: [ ]  [ ]  [ ]  [john:..] [ ]  [ ]
```

### Fonction de Hachage

**Propriétés essentielles** :
- **Déterministe** : Même clé → même hash
- **Uniforme** : Distribution équilibrée
- **Rapide** : Calcul en O(1)

```python
# Fonction de hachage simple (exemple pédagogique)
def simple_hash(key, size):
    """Hache une chaîne vers un index"""
    hash_value = 0
    for char in str(key):
        hash_value += ord(char)
    return hash_value % size

print(simple_hash("john", 10))  # Ex: 3
print(simple_hash("jane", 10))  # Ex: 7
```

### Collisions

**Problème** : Deux clés différentes → même index

```
hash("john") % 10 = 3
hash("jane") % 10 = 3  ← Collision!
```

**Solutions** :

#### 1. Chaînage (Chaining)
```
Index 3: [john:email1] → [jane:email2] → None
         (liste chaînée)
```

#### 2. Adressage Ouvert (Open Addressing)
```
Index 3: [john:email1]  ← occupé
Index 4: [jane:email2]  ← placé au suivant disponible
```

## 3. Implémentation en Python

### Utilisation des Dictionnaires Python

```python
# Création
hash_map = {}
hash_map = dict()
hash_map = {"key1": "value1", "key2": "value2"}

# Insertion/Mise à jour
hash_map["name"] = "John"
hash_map["age"] = 30
hash_map.update({"city": "Paris", "country": "France"})

# Accès
name = hash_map["name"]  # Lève KeyError si inexistant
age = hash_map.get("age")  # Retourne None si inexistant
age = hash_map.get("weight", 70)  # Valeur par défaut

# Suppression
del hash_map["age"]
removed = hash_map.pop("city")  # Retire et retourne
hash_map.clear()  # Vide tout

# Vérification
exists = "name" in hash_map
exists = hash_map.has_key("name")  # Python 2 seulement

# Itération
for key in hash_map:
    print(key, hash_map[key])

for key, value in hash_map.items():
    print(f"{key}: {value}")

# Méthodes utiles
keys = hash_map.keys()      # Vue des clés
values = hash_map.values()  # Vue des valeurs
items = hash_map.items()    # Vue des paires (clé, valeur)
```

### Implémentation Personnalisée (avec Chaînage)

```python
class HashMap:
    """Table de hachage simple avec chaînage"""
    
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0
    
    def _hash(self, key):
        """Fonction de hachage"""
        return hash(key) % self.size
    
    def put(self, key, value):
        """Insère ou met à jour - O(1) moyen"""
        index = self._hash(key)
        bucket = self.table[index]
        
        # Mettre à jour si clé existe
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        # Sinon, ajouter
        bucket.append((key, value))
        self.count += 1
        
        # Redimensionner si facteur de charge > 0.7
        if self.count / self.size > 0.7:
            self._resize()
    
    def get(self, key):
        """Récupère une valeur - O(1) moyen"""
        index = self._hash(key)
        bucket = self.table[index]
        
        for k, v in bucket:
            if k == key:
                return v
        
        raise KeyError(f"Key '{key}' not found")
    
    def remove(self, key):
        """Supprime une paire - O(1) moyen"""
        index = self._hash(key)
        bucket = self.table[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.count -= 1
                return v
        
        raise KeyError(f"Key '{key}' not found")
    
    def _resize(self):
        """Double la taille de la table"""
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0
        
        for bucket in old_table:
            for key, value in bucket:
                self.put(key, value)
    
    def __contains__(self, key):
        """Support pour 'in' operator"""
        try:
            self.get(key)
            return True
        except KeyError:
            return False
    
    def __len__(self):
        return self.count
```

## 4. Collections Spécialisées

### defaultdict

```python
from collections import defaultdict

# Dictionnaire avec valeur par défaut
word_count = defaultdict(int)  # Défaut: 0
for word in ["apple", "banana", "apple"]:
    word_count[word] += 1  # Pas besoin de vérifier si existe

print(word_count)  # {'apple': 2, 'banana': 1}

# Grouper des éléments
groups = defaultdict(list)
groups["fruits"].append("apple")
groups["fruits"].append("banana")
```

### Counter

```python
from collections import Counter

# Comptage automatique
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counter = Counter(words)

print(counter)  # Counter({'apple': 3, 'banana': 2, 'cherry': 1})
print(counter.most_common(2))  # [('apple', 3), ('banana', 2)]

# Opérations
counter["apple"] += 1
counter.update(["apple", "date"])
total = sum(counter.values())
```

### OrderedDict

```python
from collections import OrderedDict

# Maintient l'ordre d'insertion (dict le fait aussi en Python 3.7+)
ordered = OrderedDict()
ordered["first"] = 1
ordered["second"] = 2
ordered["third"] = 3

# Déplacer à la fin
ordered.move_to_end("first")
```

## 5. Problèmes Classiques

### Problème 1 : Two Sum

```python
def two_sum(nums, target):
    """Trouve deux indices dont la somme = target - O(n)"""
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    return None

print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
```

### Problème 2 : Anagrammes

```python
def group_anagrams(words):
    """Groupe les anagrammes - O(n * k log k)"""
    from collections import defaultdict
    
    groups = defaultdict(list)
    
    for word in words:
        key = ''.join(sorted(word))  # Signature
        groups[key].append(word)
    
    return list(groups.values())

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
```

### Problème 3 : Longueur de la Plus Longue Sous-séquence

```python
def longest_consecutive(nums):
    """Plus longue séquence consécutive - O(n)"""
    num_set = set(nums)
    max_length = 0
    
    for num in num_set:
        # Seulement commencer si c'est le début d'une séquence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            
            max_length = max(max_length, current_length)
    
    return max_length

print(longest_consecutive([100, 4, 200, 1, 3, 2]))  # 4 (1,2,3,4)
```

### Problème 4 : Sous-tableau de Somme Nulle

```python
def subarray_sum_zero(arr):
    """Trouve si un sous-tableau a une somme nulle - O(n)"""
    sum_map = {0: -1}  # somme → index
    current_sum = 0
    
    for i, num in enumerate(arr):
        current_sum += num
        
        if current_sum in sum_map:
            return True, (sum_map[current_sum] + 1, i)
        
        sum_map[current_sum] = i
    
    return False, None

print(subarray_sum_zero([4, 2, -3, 1, 6]))  # True, (1, 2)
```

### Problème 5 : LRU Cache

```python
from collections import OrderedDict

class LRUCache:
    """Cache avec politique Least Recently Used"""
    
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
    
    def get(self, key):
        """Récupère une valeur - O(1)"""
        if key not in self.cache:
            return -1
        
        # Marquer comme récemment utilisé
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key, value):
        """Insère/met à jour - O(1)"""
        if key in self.cache:
            self.cache.move_to_end(key)
        
        self.cache[key] = value
        
        # Supprimer le moins récemment utilisé si plein
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# Utilisation
cache = LRUCache(2)
cache.put(1, "one")
cache.put(2, "two")
print(cache.get(1))    # "one"
cache.put(3, "three")  # Évince 2
print(cache.get(2))    # -1 (évincé)
```

## 6. Applications en Sécurité

### Rainbow Table (Crack de Mots de Passe)

```python
import hashlib

class RainbowTable:
    """Table arc-en-ciel simplifiée pour cracker des hashs"""
    
    def __init__(self):
        self.table = {}
    
    def generate(self, wordlist):
        """Pré-calcule les hashs - O(n)"""
        for password in wordlist:
            hash_value = hashlib.md5(password.encode()).hexdigest()
            self.table[hash_value] = password
    
    def crack(self, hash_value):
        """Tente de retrouver le mot de passe - O(1)"""
        return self.table.get(hash_value, "Not found")

# Exemple
wordlist = ["password", "123456", "admin", "letmein"]
rainbow = RainbowTable()
rainbow.generate(wordlist)

# Cracker un hash
target_hash = hashlib.md5("admin".encode()).hexdigest()
print(rainbow.crack(target_hash))  # "admin"
```

### Détection de Duplicata (Malware Analysis)

```python
def find_duplicate_files(file_hashes):
    """Trouve les fichiers dupliqués via hash - O(n)"""
    hash_map = defaultdict(list)
    
    for file_path, file_hash in file_hashes.items():
        hash_map[file_hash].append(file_path)
    
    # Retourner seulement les doublons
    duplicates = {h: files for h, files in hash_map.items() if len(files) > 1}
    return duplicates

# Exemple
files = {
    "/path/malware1.exe": "abc123",
    "/path/malware2.exe": "abc123",  # Duplicata!
    "/path/tool.exe": "def456"
}
print(find_duplicate_files(files))
```

### Cache d'Attaques (Bruteforce Optimization)

```python
class AttackCache:
    """Cache pour éviter de retester les mêmes credentials"""
    
    def __init__(self):
        self.tested = {}
        self.successful = {}
    
    def try_login(self, username, password, login_func):
        """Teste un login avec cache"""
        key = (username, password)
        
        # Vérifier si déjà testé
        if key in self.tested:
            return self.tested[key]
        
        # Tester
        success = login_func(username, password)
        self.tested[key] = success
        
        if success:
            self.successful[username] = password
        
        return success
    
    def get_stats(self):
        """Statistiques de l'attaque"""
        return {
            "total_attempts": len(self.tested),
            "successful": len(self.successful),
            "success_rate": len(self.successful) / len(self.tested) if self.tested else 0
        }
```

## 7. Complexité & Performance

| Opération | Hash Map (moyen) | Hash Map (pire) | Remarque |
|-----------|------------------|-----------------|----------|
| Insertion | O(1) | O(n) | Pire cas = toutes collisions |
| Recherche | O(1) | O(n) | - |
| Suppression | O(1) | O(n) | - |
| Espace | O(n) | O(n) | - |

**Facteur de charge** : `λ = n / m` (éléments / buckets)
- λ < 0.7 : Performance optimale
- λ > 1.0 : Beaucoup de collisions

## 8. Pièges Courants

### 1. Clés Modifiables
```python
# ❌ ERREUR : Liste n'est pas hashable
hash_map = {}
hash_map[[1, 2]] = "value"  # TypeError!

# ✅ Utiliser un tuple
hash_map[(1, 2)] = "value"
```

### 2. Clés Inexistantes
```python
# ❌ Lève KeyError
value = hash_map["missing_key"]

# ✅ Utiliser get() ou vérifier
value = hash_map.get("missing_key", "default")
if "key" in hash_map:
    value = hash_map["key"]
```

### 3. Modification Pendant Itération
```python
# ❌ RuntimeError possible
for key in hash_map:
    if key == "bad":
        del hash_map[key]

# ✅ Créer une copie des clés
for key in list(hash_map.keys()):
    if key == "bad":
        del hash_map[key]
```

## 9. Exercices

### Exercice 1 : Débutant
Écrivez une fonction qui compte la fréquence de chaque caractère dans une chaîne.

### Exercice 2 : Intermédiaire
Trouvez le premier caractère non répété dans une chaîne.

### Exercice 3 : Intermédiaire
Implémentez une fonction qui détecte si deux chaînes sont des anagrammes.

### Exercice 4 : Avancé
Trouvez tous les sous-tableaux dont la somme est égale à k.

### Exercice 5 : Avancé
Implémentez une structure de données qui supporte insert, delete, et getRandom en O(1).

## 10. Ressources

### Plateformes
- **LeetCode** : Tag "Hash Table"
- **HackerRank** : Hash Tables
- **CodeWars** : Dictionary/Map Katas

### Lectures
- *Introduction to Algorithms* (CLRS) - Chapitre 11
- *Python Cookbook* - Dictionaries chapter

### Visualisations
- [VisuAlgo](https://visualgo.net/en/hashtable) - Visualisation Hash Table
- [Python Tutor](http://pythontutor.com/) - Exécution pas-à-pas

---

**Prochaine étape** : Passez aux sections **Algorithms** pour apprendre les algorithmes de tri et de recherche.
