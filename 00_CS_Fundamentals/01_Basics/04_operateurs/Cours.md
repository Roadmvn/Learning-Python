# Cours 04 : Opérateurs en Python

## Table des Matières

1. [Introduction et Fondamentaux](#1-introduction-et-fondamentaux)
2. [Opérateurs Arithmétiques](#2-opérateurs-arithmétiques)
3. [Opérateurs de Comparaison](#3-opérateurs-de-comparaison)
4. [Opérateurs Logiques](#4-opérateurs-logiques)
5. [Opérateurs d'Affectation](#5-opérateurs-daffectation)
6. [Opérateurs Bit à Bit](#6-opérateurs-bit-à-bit)
7. [Opérateurs d'Appartenance et d'Identité](#7-opérateurs-dappartenance-et-didentité)
8. [Priorité des Opérateurs](#8-priorité-des-opérateurs)
9. [Cas Pratiques en Cybersécurité](#9-cas-pratiques-en-cybersécurité)
10. [Pièges Courants et Bonnes Pratiques](#10-pièges-courants-et-bonnes-pratiques)

---

## 1. Introduction et Fondamentaux

### Qu'est-ce qu'un Opérateur ?

Un **opérateur** est un symbole qui indique à Python d'effectuer une opération spécifique sur une ou plusieurs valeurs (appelées **opérandes**).

```python
# Structure d'une opération
résultat = opérande1 opérateur opérande2
exemple  = 5 + 3  # 5 et 3 sont les opérandes, + est l'opérateur
```

### Pourquoi les Opérateurs sont Cruciaux ?

En cybersécurité et en programmation système, les opérateurs permettent de :
- **Manipuler des données** : Calculer des adresses mémoire, des offsets
- **Analyser des conditions** : Vérifier des permissions, valider des entrées
- **Traiter des bits** : Manipulation de flags, masques réseau, chiffrement
- **Optimiser le code** : Opérations rapides sur les données

### Types d'Opérateurs en Python

| Catégorie | Opérateurs | Usage Principal |
|-----------|------------|-----------------|
| Arithmétiques | `+`, `-`, `*`, `/`, `//`, `%`, `**` | Calculs mathématiques |
| Comparaison | `==`, `!=`, `<`, `>`, `<=`, `>=` | Tests et conditions |
| Logiques | `and`, `or`, `not` | Logique booléenne |
| Affectation | `=`, `+=`, `-=`, `*=`, etc. | Attribution de valeurs |
| Bit à bit | `&`, `|`, `^`, `~`, `<<`, `>>` | Manipulation binaire |
| Appartenance | `in`, `not in` | Test de présence |
| Identité | `is`, `is not` | Test d'identité objet |

---

## 2. Opérateurs Arithmétiques

### 2.1 Addition (+)

L'opérateur `+` additionne deux nombres.

```python
# Addition de base
a = 5
b = 3
resultat = a + b  # 8
```

**Comportements selon les types :**

```python
# Nombres entiers
10 + 5          # 15

# Nombres flottants
10.5 + 3.2      # 13.7

# Mélange int et float → résultat float
10 + 3.5        # 13.5

# Concaténation de strings
"Hello" + " " + "World"  # "Hello World"

# Addition de listes
[1, 2] + [3, 4]  # [1, 2, 3, 4]
```

**⚠️ Attention aux Types :**

```python
# ERREUR : Types incompatibles
"10" + 5  # TypeError: can only concatenate str (not "int") to str

# CORRECT : Conversion explicite
"10" + str(5)   # "105"
int("10") + 5   # 15
```

**Cas d'Usage en Cybersécurité :**

```python
# Calcul d'adresses mémoire
base_address = 0x1000
offset = 0x50
target_address = base_address + offset  # 0x1050

# Calcul de taille de payload
header_size = 20
data_size = 100
total_packet_size = header_size + data_size  # 120 bytes
```

### 2.2 Soustraction (-)

```python
# Soustraction simple
10 - 3  # 7

# Nombres négatifs
5 - 10  # -5

# Flottants
10.5 - 3.2  # 7.3
```

**Cas Pratique : Calcul de TTL (Time To Live)**

```python
# TTL dans les paquets réseau
initial_ttl = 64
hops_passed = 15
current_ttl = initial_ttl - hops_passed  # 49
print(f"Paquets restants avant expiration : {current_ttl}")
```

### 2.3 Multiplication (*)

```python
# Multiplication de base
5 * 3  # 15

# Multiplication avec flottants
2.5 * 4  # 10.0

# Répétition de strings
"A" * 10  # "AAAAAAAAAA"

# Répétition de listes
[0] * 5  # [0, 0, 0, 0, 0]
```

**Cas Pratique : Génération de Patterns**

```python
# Créer un pattern pour buffer overflow testing
pattern = "A" * 100  # 100 'A' pour tester un buffer
print(f"Pattern de test : {pattern}")

# Créer un tableau d'octets initialisé
buffer = [0x00] * 256  # 256 octets à zéro
```

### 2.4 Division (/)

**⚠️ IMPORTANT : Toujours un résultat flottant en Python 3**

```python
# Division classique
10 / 2  # 5.0 (float, pas int!)
10 / 3  # 3.3333333333333335

# Même avec des entiers, résultat = float
100 / 10  # 10.0
```

**Pourquoi c'est Important en Sécu :**

```python
# Calcul de bande passante moyenne
total_bytes = 1024000  # 1 Mo
time_seconds = 5
bandwidth = total_bytes / time_seconds  # 204800.0 bytes/sec
print(f"Vitesse : {bandwidth / 1024:.2f} KB/s")  # 200.00 KB/s
```

### 2.5 Division Entière (//)

**Retourne la partie entière du résultat (arrondi vers le bas)**

```python
# Division entière
10 // 3  # 3 (pas 3.333...)
17 // 5  # 3

# Avec nombres négatifs (attention!)
-10 // 3  # -4 (arrondi vers -∞, pas vers 0)

# Résultat toujours du même type que les opérandes
10 // 3    # 3 (int)
10.0 // 3  # 3.0 (float)
```

**Représentation Mathématique :**

```
10 / 3 = 3.333... 
       └─> floor(3.333...) = 3

-10 / 3 = -3.333...
        └─> floor(-3.333...) = -4 (vers -∞)
```

**Cas Pratique : Pagination et Indexation**

```python
# Calcul du nombre de pages
total_items = 127
items_per_page = 10
total_pages = (total_items + items_per_page - 1) // items_per_page  # 13 pages

# Convertir bytes en KB
bytes_size = 5678
kilobytes = bytes_size // 1024  # 5 KB
```

### 2.6 Modulo (%)

**Retourne le reste de la division**

```python
# Reste de la division
10 % 3   # 1 (car 10 = 3*3 + 1)
17 % 5   # 2 (car 17 = 5*3 + 2)
100 % 7  # 2

# Nombre pair ou impair
5 % 2    # 1 (impair)
6 % 2    # 0 (pair)
```

**Formule Mathématique :**

```
a % b = a - (a // b) * b

Exemple : 17 % 5
17 - (17 // 5) * 5
17 - (3) * 5
17 - 15
= 2
```

**Applications Essentielles :**

#### 1. Vérifier si un nombre est pair/impair

```python
def est_pair(n):
    return n % 2 == 0

def est_impair(n):
    return n % 2 != 0

print(est_pair(42))   # True
print(est_impair(17)) # True
```

#### 2. Rotation circulaire (très utilisé en crypto)

```python
# Rotation dans un tableau
index = 0
taille = 10

# Avancer dans un buffer circulaire
index = (index + 1) % taille  # Reste toujours entre 0 et 9
```

#### 3. Vérification de checksum simple

```python
def calculate_simple_checksum(data):
    """Checksum modulo 256"""
    checksum = 0
    for byte in data:
        checksum = (checksum + byte) % 256
    return checksum

data = [0x48, 0x65, 0x6C, 0x6C, 0x6F]  # "Hello"
print(f"Checksum: {calculate_simple_checksum(data)}")
```

#### 4. Formatage et alignement

```python
# Formater en colonnes
for i in range(20):
    print(f"{i:02d}", end="  ")
    if (i + 1) % 5 == 0:  # Nouvelle ligne tous les 5 éléments
        print()

# Output:
# 00  01  02  03  04
# 05  06  07  08  09
# 10  11  12  13  14
# 15  16  17  18  19
```

### 2.7 Puissance (**)

**Élève un nombre à une puissance**

```python
# Puissance de base
2 ** 3   # 8 (2*2*2)
10 ** 2  # 100
5 ** 0   # 1 (tout nombre^0 = 1)

# Racine carrée avec puissance fractionnaire
9 ** 0.5   # 3.0 (racine carrée)
27 ** (1/3)  # 3.0 (racine cubique)

# Nombres négatifs
(-2) ** 3  # -8
```

**Applications en Cybersécurité :**

#### 1. Calcul de l'espace d'adressage

```python
# IPv4 : 32 bits
total_ipv4_addresses = 2 ** 32  # 4,294,967,296 adresses

# Calcul de sous-réseau
subnet_mask = 24  # /24
hosts_available = (2 ** (32 - subnet_mask)) - 2  # 254 hôtes
print(f"Hôtes disponibles en /24 : {hosts_available}")

# IPv6 : 128 bits
total_ipv6_addresses = 2 ** 128  # 340 undécillion d'adresses!
```

#### 2. Calcul de complexité bruteforce

```python
# Nombre de combinaisons pour un mot de passe
def combinations_bruteforce(longueur, charset_size):
    """
    longueur: longueur du mot de passe
    charset_size: taille du jeu de caractères
    - Chiffres seulement: 10
    - Lettres minuscules: 26
    - Alphanumerique: 62
    - Avec symboles: 95
    """
    return charset_size ** longueur

# Mot de passe de 8 caractères alphanumériques
combos = combinations_bruteforce(8, 62)
print(f"Combinaisons possibles : {combos:,}")
# 218,340,105,584,896 combinaisons

# Temps estimé à 1 million de tentatives/sec
temps_secondes = combos / 1_000_000
temps_annees = temps_secondes / (60 * 60 * 24 * 365)
print(f"Temps de crack : {temps_annees:.0f} années")
```

#### 3. Croissance exponentielle

```python
# Propagation d'un ver informatique
infected_initial = 1
infection_rate = 2  # Double à chaque cycle
cycles = 10

total_infected = infected_initial * (infection_rate ** cycles)
print(f"Machines infectées après {cycles} cycles : {total_infected}")
# 1024 machines
```

---

## 3. Opérateurs de Comparaison

Les opérateurs de comparaison **retournent toujours un booléen** (`True` ou `False`).

### 3.1 Égalité (==) et Différence (!=)

```python
# Égalité
5 == 5     # True
5 == 3     # False
"abc" == "abc"  # True

# Différence
5 != 3     # True
5 != 5     # False

# ⚠️ Attention aux types
5 == "5"   # False (int ≠ string)
5 == 5.0   # True (conversion automatique)
```

**⚠️ Piège Majeur : == vs is**

```python
# == compare les VALEURS
a = [1, 2, 3]
b = [1, 2, 3]
a == b  # True (mêmes valeurs)

# is compare les IDENTITÉS (adresses mémoire)
a is b  # False (objets différents en mémoire)
```

**Cas Pratique : Validation de Credentials**

```python
def verify_login(username, password):
    """Vérification simple de connexion"""
    correct_username = "admin"
    correct_password = "P@ssw0rd123"
    
    if username == correct_username and password == correct_password:
        return True
    return False

# Test
if verify_login("admin", "P@ssw0rd123"):
    print("✅ Accès autorisé")
else:
    print("❌ Accès refusé")
```

### 3.2 Comparaisons Numériques (<, >, <=, >=)

```python
# Inférieur / Supérieur
5 < 10   # True
10 > 5   # True
5 > 10   # False

# Inférieur ou égal / Supérieur ou égal
5 <= 5   # True
5 >= 10  # False
```

**Comparaisons Chaînées (Feature Puissante de Python) :**

```python
# Au lieu de :
age = 25
if age >= 18 and age <= 65:
    print("Âge valide")

# Python permet :
if 18 <= age <= 65:
    print("Âge valide")

# Plusieurs comparaisons
x = 5
if 0 < x < 10 < y < 100:
    print("Toutes les conditions respectées")
```

**Cas Pratique : Validation de Ports**

```python
def validate_port(port):
    """
    Valide un numéro de port
    Ports valides : 1 - 65535
    Ports privilégiés : 1 - 1023
    Ports enregistrés : 1024 - 49151
    Ports dynamiques : 49152 - 65535
    """
    if not (1 <= port <= 65535):
        return "❌ Port invalide"
    
    if 1 <= port <= 1023:
        return "🔐 Port privilégié (nécessite root)"
    elif 1024 <= port <= 49151:
        return "📝 Port enregistré"
    else:
        return "🔓 Port dynamique"

# Tests
print(validate_port(80))     # Port privilégié (HTTP)
print(validate_port(8080))   # Port enregistré
print(validate_port(50000))  # Port dynamique
print(validate_port(70000))  # Invalide
```

**Cas Pratique : Vérification d'Adresse IP**

```python
def validate_ip_octet(octet):
    """Valide un octet d'adresse IPv4 (0-255)"""
    return 0 <= octet <= 255

# Vérification d'une IP complète
def validate_ipv4(ip_string):
    """Valide une adresse IPv4"""
    try:
        octets = ip_string.split('.')
        if len(octets) != 4:
            return False
        
        for octet in octets:
            num = int(octet)
            if not validate_ip_octet(num):
                return False
        
        return True
    except ValueError:
        return False

# Tests
print(validate_ipv4("192.168.1.1"))   # True
print(validate_ipv4("256.1.1.1"))     # False
print(validate_ipv4("192.168.1"))     # False
```

---

## 4. Opérateurs Logiques

Les opérateurs logiques combinent des expressions booléennes.

### 4.1 AND (et)

**Retourne True seulement si TOUS les conditions sont True**

```python
# Table de vérité AND
True and True    # True
True and False   # False
False and True   # False
False and False  # False
```

**Court-Circuit :** Si la première condition est False, Python n'évalue PAS la seconde.

```python
# Évite une erreur de division par zéro
x = 0
if x != 0 and 10 / x > 2:  # 10/x n'est jamais évalué si x==0
    print("OK")
```

**Cas Pratique : Authentification Multi-Facteurs**

```python
def authenticate_user(username, password, otp_code, ip_whitelist):
    """Authentification avec multiples vérifications"""
    valid_user = username == "admin"
    valid_pass = password == "SecureP@ss"
    valid_otp = otp_code == "123456"
    valid_ip = ip_whitelist

    # Toutes les conditions doivent être vraies
    if valid_user and valid_pass and valid_otp and valid_ip:
        return "✅ Authentification réussie"
    else:
        return "❌ Authentification échouée"

result = authenticate_user("admin", "SecureP@ss", "123456", True)
print(result)
```

### 4.2 OR (ou)

**Retourne True si AU MOINS UNE condition est True**

```python
# Table de vérité OR
True or True    # True
True or False   # True
False or True   # True
False or False  # False
```

**Court-Circuit :** Si la première condition est True, Python n'évalue PAS la seconde.

**Cas Pratique : Détection de Ports Communs**

```python
def is_common_port(port):
    """Vérifie si c'est un port commun"""
    return (port == 80 or    # HTTP
            port == 443 or   # HTTPS
            port == 22 or    # SSH
            port == 21 or    # FTP
            port == 25)      # SMTP

# Version plus propre avec 'in'
def is_common_port_v2(port):
    common_ports = [80, 443, 22, 21, 25]
    return port in common_ports

print(is_common_port(80))    # True
print(is_common_port(8080))  # False
```

### 4.3 NOT (non)

**Inverse la valeur booléenne**

```python
# Table de vérité NOT
not True   # False
not False  # True

# Exemples pratiques
not (5 > 10)  # True (car 5 > 10 est False)
not ""        # True (string vide est False)
not [1, 2]    # False (liste non-vide est True)
```

**Cas Pratique : Vérification de Liste Noire**

```python
def is_allowed_ip(ip, blacklist):
    """Vérifie si l'IP n'est PAS dans la liste noire"""
    return not (ip in blacklist)

blacklist = ["192.168.1.100", "10.0.0.50"]

if is_allowed_ip("192.168.1.1", blacklist):
    print("✅ IP autorisée")
else:
    print("🚫 IP bloquée")
```

### 4.4 Combinaisons Complexes

```python
# Exemple complexe : Règle de pare-feu
def check_firewall_rule(source_ip, dest_port, protocol, is_internal):
    """
    Autoriser SI :
    - (IP interne ET port < 1024) OU
    - (IP externe ET port >= 1024 ET protocol == 'TCP')
    """
    rule1 = is_internal and dest_port < 1024
    rule2 = (not is_internal) and dest_port >= 1024 and protocol == "TCP"
    
    return rule1 or rule2

# Tests
print(check_firewall_rule("192.168.1.10", 80, "TCP", True))    # True
print(check_firewall_rule("8.8.8.8", 8080, "TCP", False))      # True
print(check_firewall_rule("8.8.8.8", 80, "TCP", False))        # False
```

---

## 5. Opérateurs d'Affectation

### 5.1 Affectation Simple (=)

```python
x = 10  # Affecte 10 à x
y = x   # Copie la valeur de x dans y
```

### 5.2 Affectations Composées

```python
# Forme longue → Forme courte
x = x + 5   →   x += 5
x = x - 3   →   x -= 3
x = x * 2   →   x *= 2
x = x / 4   →   x /= 4
x = x // 2  →   x //= 2
x = x % 3   →   x %= 3
x = x ** 2  →   x **= 2
```

**Cas Pratique : Compteur de Paquets**

```python
# Analyse de trafic réseau
packet_count = 0
bytes_received = 0

# Simulation de réception de paquets
for _ in range(100):
    packet_count += 1           # Incrémente le compteur
    bytes_received += 64        # Ajoute la taille du paquet

print(f"Paquets reçus : {packet_count}")
print(f"Total bytes : {bytes_received}")
```

---

## 6. Opérateurs Bit à Bit

**Opèrent directement sur les bits (représentation binaire)**

### 6.1 AND Bit à Bit (&)

```python
# Comparaison bit par bit avec AND
#   5 = 0101
#   3 = 0011
# ──────────
# 5&3 = 0001 = 1

print(5 & 3)  # 1
```

**Usage : Masquage de Bits**

```python
# Extraire les permissions Unix (rwx)
permissions = 0o755  # rwxr-xr-x
user_perms = (permissions >> 6) & 0b111  # 111 (rwx)
print(f"User permissions: {user_perms:03b}")
```

### 6.2 OR Bit à Bit (|)

```python
# Comparaison bit par bit avec OR
#   5 = 0101
#   3 = 0011
# ──────────
# 5|3 = 0111 = 7

print(5 | 3)  # 7
```

**Usage : Combiner des Flags**

```python
# Flags de fichier
FLAG_READ = 0b001   # 1
FLAG_WRITE = 0b010  # 2
FLAG_EXEC = 0b100   # 4

# Combiner plusieurs permissions
permissions = FLAG_READ | FLAG_WRITE  # 0b011 = 3 (rw-)
print(f"Permissions: {permissions:03b}")
```

### 6.3 XOR Bit à Bit (^)

```python
# XOR : 1 si bits différents
#   5 = 0101
#   3 = 0011
# ──────────
# 5^3 = 0110 = 6

print(5 ^ 3)  # 6
```

**Usage Crucial : Chiffrement Simple**

```python
def xor_encrypt(data, key):
    """Chiffrement XOR simple"""
    return bytes([byte ^ key for byte in data])

message = b"SECRET"
key = 42

encrypted = xor_encrypt(message, key)
print(f"Chiffré : {encrypted.hex()}")

# Déchiffrement (même opération!)
decrypted = xor_encrypt(encrypted, key)
print(f"Déchiffré : {decrypted.decode()}")  # "SECRET"
```

### 6.4 Décalages (<<, >>)

```python
# Décalage à gauche (multiplication par 2)
5 << 1  # 10 (0101 → 1010)
5 << 2  # 20 (0101 → 10100)

# Décalage à droite (division par 2)
20 >> 1  # 10 (10100 → 1010)
20 >> 2  # 5  (10100 → 00101)
```

**Usage : Calculs Rapides**

```python
# Multiplier/diviser par puissances de 2 (très rapide)
x = 15
x << 3  # x * 8 = 120
x >> 2  # x / 4 = 3
```

---

## 7. Opérateurs d'Appartenance et d'Identité

### 7.1 Opérateur IN

```python
# Vérifier présence dans une séquence
"a" in "abc"      # True
5 in [1, 2, 5]    # True
"key" in {"key": "value"}  # True (vérifie les clés)
```

**Cas Pratique : Validation d'Input**

```python
def validate_command(command):
    """Valide une commande"""
    allowed_commands = ["ls", "pwd", "whoami", "help"]
    
    if command in allowed_commands:
        return f"✅ Exécution de '{command}'"
    else:
        return "❌ Commande non autorisée"

print(validate_command("ls"))     # Autorisée
print(validate_command("rm"))     # Non autorisée
```

### 7.2 Opérateur IS

```python
# Vérifie l'identité (même objet en mémoire)
a = [1, 2, 3]
b = [1, 2, 3]
c = a

a is b  # False (objets différents)
a is c  # True (même objet)
a == b  # True (valeurs identiques)
```

**Usage Principal : Vérifier None**

```python
result = None

if result is None:  # ✅ CORRECT
    print("Pas de résultat")

if result == None:  # ⚠️ Marche mais déconseillé
    print("Pas de résultat")
```

---

## 8. Priorité des Opérateurs

**De la plus haute à la plus basse priorité :**

| Priorité | Opérateurs | Description |
|----------|------------|-------------|
| 1 | `()` | Parenthèses |
| 2 | `**` | Puissance |
| 3 | `+x`, `-x`, `~x` | Unaires |
| 4 | `*`, `/`, `//`, `%` | Multiplication, Division |
| 5 | `+`, `-` | Addition, Soustraction |
| 6 | `<<`, `>>` | Décalages binaires |
| 7 | `&` | AND binaire |
| 8 | `^` | XOR binaire |
| 9 | `|` | OR binaire |
| 10 | `==`, `!=`, `<`, `>`, `<=`, `>=`, `is`, `in` | Comparaisons |
| 11 | `not` | NOT logique |
| 12 | `and` | AND logique |
| 13 | `or` | OR logique |

### Exemples de Priorité

```python
# Sans parenthèses
result = 2 + 3 * 4  # 14 (pas 20!)
# Évaluation : 2 + (3 * 4) = 2 + 12 = 14

# Avec parenthèses
result = (2 + 3) * 4  # 20
# Évaluation : 5 * 4 = 20

# Comparaisons complexes
x = 5
result = x > 3 and x < 10  # True
# Évaluation : (x > 3) and (x < 10)
```

**⚠️ Conseil : En cas de doute, utilisez des parenthèses !**

---

## 9. Cas Pratiques en Cybersécurité

### 9.1 Calculateur de Sous-Réseau

```python
def calculate_subnet(ip, mask):
    """
    Calcule les informations d'un sous-réseau
    """
    # Conversion IP en entier
    octets = [int(x) for x in ip.split('.')]
    ip_int = (octets[0] << 24) | (octets[1] << 16) | (octets[2] << 8) | octets[3]
    
    # Calcul du masque
    mask_int = (0xFFFFFFFF << (32 - mask)) & 0xFFFFFFFF
    
    # Adresse réseau
    network = ip_int & mask_int
    
    # Adresse broadcast
    broadcast = network | (~mask_int & 0xFFFFFFFF)
    
    # Nombre d'hôtes
    hosts = (2 ** (32 - mask)) - 2
    
    def int_to_ip(n):
        return f"{(n>>24)&0xFF}.{(n>>16)&0xFF}.{(n>>8)&0xFF}.{n&0xFF}"
    
    return {
        "réseau": int_to_ip(network),
        "broadcast": int_to_ip(broadcast),
        "hôtes": hosts,
        "première_ip": int_to_ip(network + 1),
        "dernière_ip": int_to_ip(broadcast - 1)
    }

# Test
info = calculate_subnet("192.168.1.100", 24)
for key, value in info.items():
    print(f"{key}: {value}")
```

### 9.2 Analyseur de Permissions Unix

```python
def analyze_permissions(mode):
    """
    Analyse les permissions Unix (ex: 0o755)
    """
    # Extraire les permissions
    user = (mode >> 6) & 0b111
    group = (mode >> 3) & 0b111
    others = mode & 0b111
    
    def decode_perms(perms):
        r = 'r' if perms & 0b100 else '-'
        w = 'w' if perms & 0b010 else '-'
        x = 'x' if perms & 0b001 else '-'
        return r + w + x
    
    return f"{decode_perms(user)}{decode_perms(group)}{decode_perms(others)}"

# Tests
print(analyze_permissions(0o755))  # rwxr-xr-x
print(analyze_permissions(0o644))  # rw-r--r--
print(analyze_permissions(0o600))  # rw-------
```

### 9.3 Validateur de Mot de Passe Fort

```python
def is_strong_password(password):
    """
    Vérifie si un mot de passe est fort :
    - Au moins 8 caractères
    - Contient majuscules ET minuscules
    - Contient au moins un chiffre
    - Contient au moins un symbole
    """
    length_ok = len(password) >= 8
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)
    
    # Toutes les conditions doivent être vraies
    is_strong = length_ok and has_upper and has_lower and has_digit and has_symbol
    
    # Feedback détaillé
    if not is_strong:
        issues = []
        if not length_ok:
            issues.append("❌ Trop court (min 8 caractères)")
        if not has_upper:
            issues.append("❌ Pas de majuscule")
        if not has_lower:
            issues.append("❌ Pas de minuscule")
        if not has_digit:
            issues.append("❌ Pas de chiffre")
        if not has_symbol:
            issues.append("❌ Pas de symbole")
        
        return False, issues
    
    return True, ["✅ Mot de passe fort"]

# Tests
passwords = ["password", "Password1", "P@ssw0rd", "P@ssw0rd123"]
for pwd in passwords:
    strong, feedback = is_strong_password(pwd)
    print(f"\n'{pwd}':")
    for msg in feedback:
        print(f"  {msg}")
```

---

## 10. Pièges Courants et Bonnes Pratiques

### 10.1 Division par Zéro

```python
# ❌ ERREUR
x = 10 / 0  # ZeroDivisionError

# ✅ VÉRIFICATION
denominator = 0
if denominator != 0:
    result = 10 / denominator
else:
    print("Erreur : division par zéro")

# ✅ GESTION D'EXCEPTION
try:
    result = 10 / denominator
except ZeroDivisionError:
    print("Division par zéro détectée")
```

### 10.2 Comparaison de Flottants

```python
# ❌ PROBLÈME : Imprécision des flottants
0.1 + 0.2 == 0.3  # False (!!)

# ✅ SOLUTION : Tolérance
import math
def float_equals(a, b, tolerance=1e-9):
    return abs(a - b) < tolerance

float_equals(0.1 + 0.2, 0.3)  # True
```

### 10.3 Mutation vs Réaffectation

```python
# Liste (mutable)
x = [1, 2, 3]
y = x
y.append(4)  # Modifie aussi x!
print(x)  # [1, 2, 3, 4]

# Pour copier : utiliser .copy() ou list()
y = x.copy()
```

### 10.4 Court-Circuit et Effets de Bord

```python
# ❌ DANGER si fonction a un effet de bord
def increment_counter():
    global counter
    counter += 1
    return True

counter = 0
if False and increment_counter():  # increment_counter() jamais appelé!
    pass
print(counter)  # 0

# ✅ Appeler la fonction avant
result = increment_counter()
if False and result:
    pass
```

### 10.5 Priorité des Opérateurs

```python
# ❌ CONFUSION
result = 5 + 3 * 2  # 11 ou 16 ?

# ✅ EXPLICITE
result = 5 + (3 * 2)  # 11 - Clair!
result = (5 + 3) * 2  # 16 - Clair!
```

---

## 📚 Résumé et Checklist

### Concepts Clés à Maîtriser

- [ ] Différence entre `/` (float) et `//` (int)
- [ ] Usage du modulo `%` pour cycles et vérifications
- [ ] Comparaisons chaînées : `0 < x < 10`
- [ ] Court-circuit de `and` et `or`
- [ ] Différence entre `==` (valeur) et `is` (identité)
- [ ] Opérateurs bit à bit pour manipulation binaire
- [ ] Priorité des opérateurs
- [ ] Vérification de `None` avec `is None`

### Points de Vigilance

⚠️ **Division par zéro** : Toujours vérifier avant de diviser
⚠️ **Comparaison de types** : `5 != "5"`
⚠️ **Flottants** : Ne pas comparer avec `==` directement
⚠️ **Priorité** : Utiliser des parenthèses pour la clarté

### Applications en Cybersécurité

✅ Calculs réseau (masques, sous-réseaux)
✅ Validation d'entrées (ports, IPs, credentials)
✅ Manipulation de bits (flags, permissions)
✅ Analyse de données binaires
✅ Implémentation de logique de sécurité

---

## 🎯 Exercices Pratiques

Maintenant que vous maîtrisez les opérateurs, passez au fichier `exercice.md` pour mettre en pratique vos connaissances avec des défis progressifs !

Les exemples de code sont disponibles dans `example.py` et les solutions complètes dans `solution.py`.

---

**Prochaine étape** : Exercice 05 - Structures Conditionnelles (if/else)
