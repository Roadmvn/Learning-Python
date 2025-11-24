# Cours : ROR Encoding & API Hashing

## 1. Le Problème de l'Import Table

Quand vous développez un malware en C/C++ (ou même Python compilé), votre binaire contient une **Import Table** listant toutes les fonctions système utilisées :

```
kernel32.dll:
  - CreateProcessW
  - VirtualAllocEx
  - WriteProcessMemory
kernel32.dll`, `CreateProcessW`), l'analyse statique ne voit **rien**. L'Import Table est vide pour ces fonctions.

## 2. Le Hash API

Au lieu de chercher par nom, on cherche par **hash**.

### Principe
1. On parcourt toutes les fonctions exportées par une DLL.
2. Pour chaque nom de fonction, on calcule son hash.
3. On compare avec le hash recherché.
4. Si match → on a trouvé l'adresse de la fonction !

```python
# Au lieu de :
CreateProcess = GetProcAddress(kernel32, "CreateProcessW")

# On fait :
target_hash = 0x16B3FE72  # Hash de "CreateProcessW"
for function in kernel32.exports:
    if hash_function_name(function.name) == target_hash:
        CreateProcess = function.address
        break
```

## 3. ROR13 Hash : L'Algorithme Star

L'algorithme le plus utilisé est **ROR13** (Rotate Right 13 bits). Il a été popularisé par **Metasploit** et est devenu un standard.

### Algorithme
```python
def ror13_hash(name):
    hash_value = 0
    for char in name.upper():  # Insensible à la casse
        hash_value = ror(hash_value, 13)  # Rotation de 13 bits
        hash_value += ord(char)
    return hash_value & 0xFFFFFFFF  # Tronquer à 32 bits
```

### Rotation à Droite (ROR)
```python
def ror(value, count):
    """Rotate Right : décale les bits vers la droite avec wraparound"""
    count %= 32  # Assurer que count < 32
    return ((value >> count) | (value << (32 - count))) & 0xFFFFFFFF
```

Exemple visuel :
```
Valeur   : 11010110 (8 bits pour simplifier)
ROR 3    : 11011010 (les 3 bits de droite vont à gauche)
         : ↑↑↑     ← wraparound
```

## 4. Implémentation Complète

```python
def ror(value, count):
    count %= 32
    return ((value >> count) | (value << (32 - count))) & 0xFFFFFFFF

def ror13_hash(name):
    hash_value = 0
    for char in name.upper():
        hash_value = ror(hash_value, 13)
        hash_value += ord(char)
        hash_value &= 0xFFFFFFFF  # Garder 32 bits
    return hash_value

# Test
print(hex(ror13_hash("CreateProcessW")))  # 0x16b3fe72
print(hex(ror13_hash("VirtualAlloc")))    # 0x91afca54
```

## 5. Utilisation dans un Malware

### Phase 1 : Pré-calcul (Offline)
Avant de compiler le malware, on calcule les hash des fonctions dont on aura besoin :

```python
api_hashes = {
    "CreateProcessW":     0x16b3fe72,
    "VirtualAllocEx":     0x3f9287ae,
    "WriteProcessMemory": 0x0fd5d907,
}
```

### Phase 2 : Runtime (Malware)
Le malware parcourt les exports de `kernel32.dll` et cherche les hash :

```python
def find_api_by_hash(dll_base, target_hash):
    """Trouve une fonction par son hash ROR13"""
    exports = get_exports(dll_base)  # Liste des fonctions exportées
    
    for export in exports:
        if ror13_hash(export.name) == target_hash:
            return export.address
    
    return None

# Dans le malware
kernel32 = get_module_handle("kernel32.dll")
CreateProcess_addr = find_api_by_hash(kernel32, 0x16b3fe72)
```

## 6. Avantages & Inconvénients

### ✅ Avantages
- **Évasion de signatures** : Pas de strings "CreateProcessW" dans le binaire
- **Compact** : Un hash = 4 bytes (vs ~15 bytes pour le nom)
- **Difficile à analyser** : Un analyste doit reverse-engineer l'algo de hash

### ❌ Inconvénients
- **Collisions** : Deux noms différents peuvent avoir le même hash (rare mais possible)
- **Détectable au runtime** : Si un EDR surveille la parcours des exports, c'est louche

## 7. Détection (Blue Team)

Un EDR moderne détecte l'API hashing en cherchant :
1. Code qui parcourt toutes les fonctions exportées d'une DLL
2. Code qui ne fait aucun appel à `GetProcAddress` (car remplacé par du hash)
3. Algorithmes de rotation de bits + comparaison de hash

## 8. Variantes

### FNV Hash
```python
def fnv1a_hash(data):
    hash_value = 0x811c9dc5
    for byte in data:
        hash_value ^= byte
        hash_value *= 0x01000193
        hash_value &= 0xFFFFFFFF
    return hash_value
```

### DJB2 Hash
```python
def djb2_hash(data):
    hash_value = 5381
    for char in data:
        hash_value = ((hash_value << 5) + hash_value) + ord(char)
    return hash_value & 0xFFFFFFFF
```

Certains malwares créent même leur propre algorithme de hash pour être uniques !
