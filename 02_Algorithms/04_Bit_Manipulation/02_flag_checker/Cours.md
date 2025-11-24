# Cours : Bit Flags & Vérification de Privilèges

## 1. Les Flags : Plusieurs Booléens en Un Seul Nombre

Un **bit flag** est une technique pour stocker plusieurs booléens (True/False) dans un seul nombre entier. Chaque bit représente un état différent.

### Pourquoi Utiliser des Flags ?
- **Économie de mémoire** : 32 booléens dans un seul `int32`
- **Performance** : Opérations bitwise ultra-rapides
- **Standard** : Utilisé partout (Unix permissions, Windows ACL, flags de processus)

## 2. Exemple Concret : Permissions Unix

Sur Linux/Mac, les permissions de fichiers (`rwx`) sont des bit flags :

```
rwx r-x r--
111 101 100  (en binaire)
7   5   4    (en octal)
```

- Bit 2 (READ)    : 100 = 4
- Bit 1 (WRITE)   : 010 = 2
- Bit 0 (EXECUTE) : 001 = 1

```python
READ    = 1 << 2  # 4 (100)
WRITE   = 1 << 1  # 2 (010)
EXECUTE = 1 << 0  # 1 (001)

# rwx = 111 = 7
permissions = READ | WRITE | EXECUTE
```

## 3. Opérations sur les Flags

### Vérifier si un Flag est Activé (AND)
```python
def has_permission(perms, flag):
    return (perms & flag) != 0

perms = 0b110  # rw- (6)
print(has_permission(perms, READ))   # True
print(has_permission(perms, WRITE))  # True
print(has_permission(perms, EXECUTE))# False
```

### Activer un Flag (OR)
```python
def add_permission(perms, flag):
    return perms | flag

perms = 0b100  # r--
perms = add_permission(perms, WRITE)  # rw-
print(bin(perms))  # 0b110
```

### Désactiver un Flag (AND + NOT)
```python
def remove_permission(perms, flag):
    return perms & ~flag

perms = 0b111  # rwx
perms = remove_permission(perms, WRITE)  # r-x
print(bin(perms))  # 0b101
```

### Basculer un Flag (XOR)
```python
def toggle_permission(perms, flag):
    return perms ^ flag

perms = 0b100  # r--
perms = toggle_permission(perms, WRITE)  # rw-
perms = toggle_permission(perms, WRITE)  # r-- (retour)
```

## 4. Application en Sécurité : Privilèges Windows

Windows utilise des **tokens** de sécurité avec des flags pour les privilèges.

### Privilèges Importants
```python
SE_DEBUG_PRIVILEGE       = 1 << 0  # Peut attacher un debugger
SE_BACKUP_PRIVILEGE      = 1 << 1  # Peut lire n'importe quel fichier
SE_RESTORE_PRIVILEGE     = 1 << 2  # Peut écrire n'importe où
SE_SHUTDOWN_PRIVILEGE    = 1 << 3  # Peut éteindre le système
SE_LOAD_DRIVER_PRIVILEGE = 1 << 4  # Peut charger des drivers (TRÈS dangereux)
SE_TCB_PRIVILEGE         = 1 << 5  # Privilège système (like SYSTEM)
```

### Cas d'Usage : Privilege Escalation
Un attaquant qui obtient `SE_DEBUG_PRIVILEGE` peut :
- Injecter du code dans n'importe quel processus (y compris SYSTEM)
- Dumper la mémoire de processus protégés (`lsass.exe` pour voler des credentials)

```python
def can_inject_processes(privileges):
    """Vérifie si on peut injecter dans des processus"""
    return (privileges & SE_DEBUG_PRIVILEGE) != 0

def can_load_malicious_driver(privileges):
    """Vérifie si on peut charger un rootkit"""
    return (privileges & SE_LOAD_DRIVER_PRIVILEGE) != 0
```

## 5. Exemple Réel : Mimikatz

L'outil **Mimikatz** (dump de credentials Windows) vérifie d'abord s'il a `SE_DEBUG_PRIVILEGE`. Si oui, il peut lire la mémoire de `lsass.exe` (qui stocke les mots de passe en RAM).

```python
# Pseudo-code de Mimikatz
if has_privilege(current_token, SE_DEBUG_PRIVILEGE):
    # Ouvrir lsass.exe
    # Lire la mémoire
    # Extraire les mots de passe
else:
    print("Erreur : besoin de SE_DEBUG_PRIVILEGE")
```

## 6. Masques de Bits (Bitmasks)

Un **masque** permet d'extraire ou de comparer plusieurs bits en une fois.

```python
# Vérifier plusieurs permissions à la fois
ADMIN_PERMS = READ | WRITE | EXECUTE

def is_admin(perms):
    return (perms & ADMIN_PERMS) == ADMIN_PERMS

perms = 0b111  # rwx
print(is_admin(perms))  # True

perms = 0b110  # rw-
print(is_admin(perms))  # False (manque EXECUTE)
```

## 7. Flags en C2 / Malware

Les implants malveillants utilisent des flags pour configurer leur comportement :

```python
# Configuration d'un implant
STEALTH_MODE       = 1 << 0  # Mode furtif
KEYLOGGER_ENABLED  = 1 << 1  # Keylogger actif
PERSIST_ON_REBOOT  = 1 << 2  # Persistence
EXFILTRATE_DATA    = 1 << 3  # Exfiltration auto

config = STEALTH_MODE | PERSIST_ON_REBOOT

if config & KEYLOGGER_ENABLED:
    start_keylogger()

if config & EXFILTRATE_DATA:
    exfiltrate_to_c2()
```

Avantage : Tout passe dans un seul `int`, facile à transmettre via le réseau.
