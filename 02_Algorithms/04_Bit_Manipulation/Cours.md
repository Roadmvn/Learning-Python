# Cours : Manipulation de Bits (Bit Manipulation)

## 1. Introduction

La **manipulation de bits** consiste à effectuer des opérations directement sur les représentations binaires des nombres. C'est une technique puissante pour l'optimisation et la cybersécurité.

### Pourquoi c'est important ?

- **Performance** : Opérations ultra-rapides
- **Optimisation mémoire** : Stocker plusieurs booléens dans un entier
- **Cryptographie** : XOR dans les chiffrements
- **En sécurité** : Analyse de binaires, shellcode, flags de permissions

## 2. Représentation Binaire

```python
# Décimal vers binaire
bin(10)  # '0b1010'
format(10, '08b')  # '00001010' (8 bits)

# Binaire vers décimal
int('1010', 2)  # 10
int('0b1010', 2)  # 10

# Hexadécimal
hex(255)  # '0xff'
int('0xff', 16)  # 255
```

## 3. Opérateurs Bit à Bit

### AND (&) - ET Logique
```python
# 1 & 1 = 1, sinon 0
print(5 & 3)  # 0101 & 0011 = 0001 = 1
print(12 & 5) # 1100 & 0101 = 0100 = 4
```

### OR (|) - OU Logique
```python
# 1 | 1 = 1, 1 | 0 = 1, 0 | 0 = 0
print(5 | 3)  # 0101 | 0011 = 0111 = 7
print(12 | 5) # 1100 | 0101 = 1101 = 13
```

### XOR (^) - OU Exclusif
```python
# 1 ^ 1 = 0, 1 ^ 0 = 1, 0 ^ 0 = 0
print(5 ^ 3)  # 0101 ^ 0011 = 0110 = 6
print(12 ^ 5) # 1100 ^ 0101 = 1001 = 9

# Propriétés utiles du XOR:
# a ^ a = 0
# a ^ 0 = a
# a ^ b ^ b = a
```

### NOT (~) - Complément
```python
# Inverse tous les bits
print(~5)  # -(5+1) = -6 (complément à deux)
print(bin(~5 & 0xFF))  # '0b11111010' (sur 8 bits)
```

### Décalages (Shifts)

```python
# Left Shift (<<) - Multiplie par 2^n
print(5 << 1)  # 0101 → 1010 = 10 (5 * 2)
print(5 << 2)  # 0101 → 10100 = 20 (5 * 4)

# Right Shift (>>) - Divise par 2^n
print(5 >> 1)  # 0101 → 0010 = 2 (5 / 2)
print(20 >> 2) # 10100 → 00101 = 5 (20 / 4)
```

## 4. Techniques Courantes

### Vérifier si un Bit est Activé

```python
def is_bit_set(num, position):
    """Vérifie si le bit à position est 1"""
    return (num & (1 << position)) != 0

print(is_bit_set(5, 0))  # True (0101, bit 0 = 1)
print(is_bit_set(5, 1))  # False (0101, bit 1 = 0)
print(is_bit_set(5, 2))  # True (0101, bit 2 = 1)
```

### Activer un Bit

```python
def set_bit(num, position):
    """Met le bit à position à 1"""
    return num | (1 << position)

print(bin(set_bit(5, 1)))  # 0101 → 0111 (5 → 7)
```

### Désactiver un Bit

```python
def clear_bit(num, position):
    """Met le bit à position à 0"""
    return num & ~(1 << position)

print(bin(clear_bit(7, 1)))  # 0111 → 0101 (7 → 5)
```

### Basculer un Bit (Toggle)

```python
def toggle_bit(num, position):
    """Inverse le bit à position"""
    return num ^ (1 << position)

print(bin(toggle_bit(5, 1)))  # 0101 → 0111 (5 → 7)
print(bin(toggle_bit(7, 1)))  # 0111 → 0101 (7 → 5)
```

### Extraire un Bit

```python
def get_bit(num, position):
    """Retourne la valeur du bit (0 ou 1)"""
    return (num >> position) & 1

print(get_bit(5, 0))  # 1
print(get_bit(5, 1))  # 0
print(get_bit(5, 2))  # 1
```

## 5. Problèmes Classiques

### Problème 1 : Compter les Bits à 1

```python
def count_bits(n):
    """Compte le nombre de bits à 1 - Brian Kernighan's Algorithm"""
    count = 0
    while n:
        n &= n - 1  # Retire le bit 1 le plus à droite
        count += 1
    return count

print(count_bits(7))   # 3 (0111)
print(count_bits(255)) # 8 (11111111)

# En Python (intégré)
print(bin(7).count('1'))  # 3
```

### Problème 2 : Nombre Unique (XOR)

```python
def single_number(nums):
    """Trouve le nombre qui apparaît une seule fois"""
    result = 0
    for num in nums:
        result ^= num  # a ^ a = 0, donc les pairs s'annulent
    return result

print(single_number([4, 1, 2, 1, 2]))  # 4
```

### Problème 3 : Puissance de 2

```python
def is_power_of_two(n):
    """Vérifie si n est une puissance de 2"""
    # Puissance de 2 : un seul bit à 1
    # Ex: 8 = 1000, 7 = 0111, 8 & 7 = 0
    return n > 0 and (n & (n - 1)) == 0

print(is_power_of_two(8))   # True
print(is_power_of_two(10))  # False
```

### Problème 4 : Inverser les Bits

```python
def reverse_bits(n):
    """Inverse les 32 bits d'un nombre"""
    result = 0
    for i in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result

print(bin(reverse_bits(0b00000000000000000000000000001011)))
# 0b11010000000000000000000000000000
```

### Problème 5 : Nombre de Bits à Changer

```python
def hamming_distance(x, y):
    """Nombre de bits différents entre x et y"""
    xor = x ^ y
    return bin(xor).count('1')

print(hamming_distance(1, 4))  # 2 (0001 vs 0100)
```

### Problème 6 : Sous-ensembles avec Bits

```python
def generate_subsets_bitwise(arr):
    """Génère tous les sous-ensembles avec manipulation de bits"""
    n = len(arr)
    subsets = []
    
    # 2^n combinaisons possibles
    for i in range(1 << n):  # 2^n
        subset = []
        for j in range(n):
            if i & (1 << j):  # Si le bit j est activé
                subset.append(arr[j])
        subsets.append(subset)
    
    return subsets

print(generate_subsets_bitwise([1, 2, 3]))
# [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
```

## 6. Applications en Sécurité

### Permissions Unix (rwx)

```python
# rwx = 111 (7), r-x = 101 (5), r-- = 100 (4)
READ = 1 << 2    # 100 = 4
WRITE = 1 << 1   # 010 = 2
EXECUTE = 1 << 0 # 001 = 1

def has_permission(permissions, flag):
    """Vérifie si une permission est accordée"""
    return (permissions & flag) != 0

def add_permission(permissions, flag):
    """Ajoute une permission"""
    return permissions | flag

def remove_permission(permissions, flag):
    """Retire une permission"""
    return permissions & ~flag

# Exemple
perms = READ | WRITE  # rw- = 110 = 6
print(has_permission(perms, READ))    # True
print(has_permission(perms, EXECUTE)) # False
perms = add_permission(perms, EXECUTE)  # rwx = 111 = 7
print(perms)  # 7
```

### XOR Encryption (Simple)

```python
def xor_encrypt(data, key):
    """Chiffrement XOR simple"""
    return bytes([b ^ key for b in data])

def xor_decrypt(encrypted, key):
    """Déchiffrement XOR (même opération)"""
    return xor_encrypt(encrypted, key)

# Exemple
message = b"SECRET"
key = 0x42
encrypted = xor_encrypt(message, key)
print(encrypted.hex())
decrypted = xor_decrypt(encrypted, key)
print(decrypted)  # b'SECRET'
```

### IPv4 Subnet Masking

```python
def ip_to_int(ip):
    """Convertit IP en entier"""
    parts = [int(p) for p in ip.split('.')]
    return (parts[0] << 24) | (parts[1] << 16) | (parts[2] << 8) | parts[3]

def int_to_ip(num):
    """Convertit entier en IP"""
    return f"{(num >> 24) & 0xFF}.{(num >> 16) & 0xFF}.{(num >> 8) & 0xFF}.{num & 0xFF}"

def get_network_address(ip, mask):
    """Calcule l'adresse réseau"""
    ip_int = ip_to_int(ip)
    mask_int = ip_to_int(mask)
    network = ip_int & mask_int
    return int_to_ip(network)

print(get_network_address("192.168.1.100", "255.255.255.0"))
# "192.168.1.0"
```

### Feature Flags (Fonctionnalités)

```python
class Features:
    """Gestion de features avec bits"""
    FEATURE_A = 1 << 0  # 0001
    FEATURE_B = 1 << 1  # 0010
    FEATURE_C = 1 << 2  # 0100
    FEATURE_D = 1 << 3  # 1000
    
    def __init__(self):
        self.enabled = 0
    
    def enable(self, feature):
        self.enabled |= feature
    
    def disable(self, feature):
        self.enabled &= ~feature
    
    def is_enabled(self, feature):
        return (self.enabled & feature) != 0

# Usage
features = Features()
features.enable(Features.FEATURE_A | Features.FEATURE_C)
print(features.is_enabled(Features.FEATURE_A))  # True
print(features.is_enabled(Features.FEATURE_B))  # False
```

## 7. Optimisations avec Bits

### Multiplication/Division Rapide

```python
# Multiplication par 2^n
x = 5
print(x << 1)  # 5 * 2 = 10
print(x << 3)  # 5 * 8 = 40

# Division par 2^n
x = 40
print(x >> 1)  # 40 / 2 = 20
print(x >> 3)  # 40 / 8 = 5
```

### Vérifier Parité

```python
def is_even(n):
    """Vérifie si n est pair"""
    return (n & 1) == 0

print(is_even(4))  # True
print(is_even(5))  # False
```

### Échanger Sans Variable Temporaire

```python
def swap_xor(a, b):
    """Échange a et b avec XOR"""
    a = a ^ b
    b = a ^ b  # b = (a ^ b) ^ b = a
    a = a ^ b  # a = (a ^ b) ^ a = b
    return a, b

print(swap_xor(5, 10))  # (10, 5)
```

## 8. Pièges Courants

### 1. Priorité des Opérateurs

```python
# ❌ ERREUR: & a priorité plus faible que ==
if n & 1 == 0:  # Interprété comme: n & (1 == 0)
    pass

# ✅ CORRECT
if (n & 1) == 0:
    pass
```

### 2. Complément à Deux (Nombres Négatifs)

```python
# Python utilise des entiers de taille illimitée
print(~5)  # -6 (pas 250 sur 8 bits)

# Pour simuler des bits fixes:
print(~5 & 0xFF)  # 250 (sur 8 bits)
```

### 3. Décalage de Nombres Négatifs

```python
# Comportement différent selon les langages
print(-4 >> 1)  # -2 en Python (arithmétique)
```

## 9. Exercices

### Exercice 1 : Débutant
Écrivez une fonction qui compte les bits à 0 dans un nombre.

### Exercice 2 : Intermédiaire
Trouvez le seul nombre manquant dans un tableau de 1 à n.

### Exercice 3 : Intermédiaire
Implémentez l'addition de deux nombres sans utiliser + ou -.

### Exercice 4 : Avancé
Trouvez les deux nombres qui apparaissent une seule fois (les autres deux fois).

### Exercice 5 : Avancé
Implémentez un compresseur de données simple avec manipulation de bits.

## 10. Ressources

### Plateformes
- **LeetCode** : Tag "Bit Manipulation"
- **HackerRank** : Bit Manipulation
- **Hackers Delight** - Livre de référence

### Outils
- [Bit Calculator](https://www.calculator.net/binary-calculator.html)
- [Bitwise Visualizer](https://bitwisecmd.com/)

---

**Prochaine étape** : Passez à `03_Systems_Programming` pour la programmation système.
