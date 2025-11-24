# Cours : Chiffrement XOR & Évasion d'Antivirus

## 1. Le XOR : L'Arme Secrète du Malware Dev

Le **XOR (eXclusive OR)** est l'opération la plus utilisée en malware development pour :
- Encoder des payloads
- Obfusquer du code
- Implémenter du chiffrement simple

### Pourquoi XOR ?
1. **Réversible** : `A XOR B XOR B = A` (le chiffrement et déchiffrement utilisent la même opération)
2. **Rapide** : Une seule opération CPU par byte
3. **Simple** : Facile à implémenter sans bibliothèque

## 2. Théorie du XOR

### Table de Vérité
```
A | B | A ^ B
--|---|------
0 | 0 |  0
0 | 1 |  1
1 | 0 |  1
1 | 1 |  0
```

### Propriétés Magiques
```python
# Propriété 1 : Réversibilité
A ^ B ^ B = A

# Propriété 2 : Identité
A ^ 0 = A

# Propriété 3 : Auto-annulation
A ^ A = 0

# Propriété 4 : Commutativité
A ^ B = B ^ A
```

## 3. XOR Encryption en Python

### Chiffrement Single-Byte Key
```python
def xor_encrypt(data, key):
    """Chiffre data avec une clé XOR d'un seul byte"""
    return bytes([b ^ key for b in data])

message = b"ATTACK AT DAWN"
key = 0x42

encrypted = xor_encrypt(message, key)
print(encrypted.hex())  # Données chiffrées

# Déchiffrement (même fonction !)
decrypted = xor_encrypt(encrypted, key)
print(decrypted)  # b"ATTACK AT DAWN"
```

### Chiffrement Multi-Byte Key
```python
def xor_encrypt_multibyte(data, key):
    """Chiffre data avec une clé multi-byte"""
    key_len = len(key)
    return bytes([data[i] ^ key[i % key_len] for i in range(len(data))])

message = b"SECRET_PAYLOAD"
key = b"K3Y"

encrypted = xor_encrypt_multibyte(message, key)
decrypted = xor_encrypt_multibyte(encrypted, key)
```

## 4. Application en Malware Development

### Problème : Les Signatures Antivirus
Les antivirus détectent les malwares en cherchant des **signatures** (séquences de bytes connues).

**Exemple** : Si votre malware contient la string `"cmd.exe"`, l'antivirus peut la détecter.

**Solution** : XOR-encoder ces strings !

### Avant (Détecté)
```python
import subprocess
subprocess.run(["cmd.exe", "/c", "whoami"])
```

L'antivirus voit `"cmd.exe"` dans le binaire → **BLOQUÉ**.

### Après (Évadé)
```python
# Pré-calculé : "cmd.exe" XOR 0x42
encrypted_cmd = bytes([0x25, 0x2f, 0x26, 0x04, 0x27, 0x2d, 0x27])

# Au runtime, on décode
key = 0x42
cmd = bytes([b ^ key for b in encrypted_cmd])  # b"cmd.exe"

import subprocess
subprocess.run([cmd.decode(), "/c", "whoami"])
```

L'antivirus ne voit **jamais** la string `"cmd.exe"` en clair dans le fichier → **ÉVADÉ**.

## 5. Techniques Avancées

### Rolling XOR (Clé qui change)
```python
def rolling_xor_encrypt(data, initial_key):
    """XOR avec clé qui évolue"""
    result = bytearray()
    key = initial_key
    for b in data:
        result.append(b ^ key)
        key = (key + 1) % 256  # La clé change à chaque byte
    return bytes(result)
```

### XOR avec Shellcode
```python
# Shellcode original (détecté)
shellcode = b"\x90\x90\x90..."  # NOP sled détectable

# Shellcode encodé
encoded_shellcode = xor_encrypt(shellcode, 0xAA)

# Dans le malware, on décode au runtime
decoded = xor_encrypt(encoded_shellcode, 0xAA)
# Puis on exécute le shellcode décodé
```

## 6. Détection et Contre-Mesures

### Comment les AV Détectent XOR
1. **Analyse d'entropie** : Un fichier XOR-encodé a une entropie inhabituelle
2. **Analyse comportementale** : Décodage de données suivi d'exécution = suspect
3. **Émulation** : L'AV exécute le code dans un sandbox et voit le décodage

### Améliorer l'Évasion
- Combiner XOR avec d'autres techniques (compression, multi-couches)
- Utiliser des clés variables
- Ajouter du "bruit" (padding aléatoire)

## 7. Cas Réel : WannaCry

Le ransomware **WannaCry** utilisait XOR pour obfusquer ses strings de configuration (IP des C2, clés de chiffrement).

Cela a retardé l'analyse initiale de plusieurs heures.
