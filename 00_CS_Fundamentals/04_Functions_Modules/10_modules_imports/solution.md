# Exercice 10: Modules et Imports - Solutions

SOLUTION 1 : Explorateur de répertoires

"""
Explorateur simple qui utilise le module os
"""

```python
import os

```
# Obtenir le répertoire courant
rep_courant = os.getcwd()
```python
print(f"Répertoire courant : {rep_courant}")

```
# Lister les fichiers
fichiers = os.listdir('.')
```python
print(f"\nNombre d'éléments : {len(fichiers)}")

```
# Compter fichiers et dossiers
nombre_fichiers = 0
nombre_dossiers = 0

```python
for element in fichiers:
    if os.path.isfile(element):
        nombre_fichiers += 1
    elif os.path.isdir(element):
        nombre_dossiers += 1

print(f"Fichiers : {nombre_fichiers}")
print(f"Dossiers : {nombre_dossiers}")

```
# Afficher le séparateur
```python
print(f"\nSéparateur du système : '{os.sep}'")

```
# Afficher les premiers fichiers
```python
print(f"\nPremiers fichiers : {fichiers[:5]}")

```
SOLUTION 2 : Informations système

"""
Affiche les informations système avec sys
"""

```python
from sys import version, platform, argv, executable, getdefaultencoding
import sys

print("[*] Informations système\n")

print(f"Version Python : {version.split()[0]}")
print(f"Plateforme : {platform}")
print(f"Encodage : {getdefaultencoding()}")
print(f"Exécutable : {executable}")

print(f"\nNombre d'arguments : {len(argv)}")
if len(argv) > 1:
    print(f"Arguments : {argv[1:]}")

```
# Afficher l'émoji de la plateforme
```python
if platform == "linux":
    print("Émoji : 🐧 Linux")
elif platform == "win32":
    print("Émoji : 🪟 Windows")
elif platform == "darwin":
    print("Émoji : 🍎 macOS")

```
SOLUTION 3 : Gestionnaire de temps (Mesure de performance)

"""
Mesure le temps d'exécution d'une opération
"""

```python
import time

print("[*] Mesure de performance\n")

```
# Obtenir le timestamp actuel
timestamp_debut = time.time()
```python
print(f"Timestamp Unix actuel : {timestamp_debut}")

```
# Formater l'heure locale
temps_local = time.localtime()
temps_formate = time.strftime("%H:%M:%S", temps_local)
```python
print(f"Heure locale : {temps_formate}")

```
# Mesurer une opération
```python
print("\n[*] Exécution d'une opération...\n")

```
debut = time.time()

# Opération : créer une liste de 10 millions et les additionner
liste = range(10000000)
somme = sum(liste)

fin = time.time()
duree = fin - debut

```python
print(f"Somme calculée : {somme}")
print(f"Temps d'exécution : {duree:.4f} secondes")
print(f"Durée formatée : {int(duree)} secondes {int((duree % 1) * 1000)} ms")

```
SOLUTION 4 : Calculatrice de dates

"""
Utilise datetime pour manipuler les dates
"""

```python
from datetime import datetime, timedelta

print("[*] Calculatrice de dates\n")

```
# Date actuelle
maintenant = datetime.now()
```python
print(f"Aujourd'hui : {maintenant.strftime('%Y-%m-%d %H:%M:%S')}")

```
# Jours jusqu'à Noël
annee_actuelle = maintenant.year
noel = datetime(annee_actuelle, 12, 25)

# Si Noël est passé, prendre l'année suivante
```python
if noel < maintenant:
    noel = datetime(annee_actuelle + 1, 12, 25)

```
diff_noel = noel - maintenant
jours_noel = diff_noel.days
```python
print(f"Jours jusqu'à Noël : {jours_noel}")

```
# Date personnalisée
date_cible = datetime(2025, 6, 15)
```python
print(f"\nDate cible : {date_cible.strftime('%d/%m/%Y')}")

```
# Différence
diff = date_cible - maintenant
```python
print(f"Différence : {diff.days} jours")

```
# Convertir timestamp en date
timestamp = 1609459200  # 2021-01-01
date_from_timestamp = datetime.fromtimestamp(timestamp)
```python
print(f"\nTimestamp {timestamp}")
print(f"Date convertie : {date_from_timestamp.strftime('%d/%m/%Y %H:%M:%S')}")

```
# Calculs détaillés
heures = (diff.seconds // 3600)
minutes = (diff.seconds % 3600) // 60

```python
print(f"\nJours, heures, minutes : {diff.days}j {heures}h {minutes}m")

```
SOLUTION 5 : Générateur de mots de passe aléatoires

"""
Génère des données aléatoires pour les mots de passe et tokens
"""

```python
import random
import string

print("[*] Générateur de données aléatoires\n")

```
# 1. Mot de passe aléatoire
caracteres = string.ascii_letters + string.digits + string.punctuation
mdp = ''.join(random.choice(caracteres) for _ in range(12))
```python
print(f"Mot de passe (12 car.) : {mdp}")

```
# 2. Tokens de session
```python
print("\nTokens de session (32 hex) :")
for i in range(5):
    token = ''.join(random.choice(string.hexdigits[:-6]) for _ in range(32))
    print(f"  Token {i+1} : {token}")

```
# 3. Mélanger une liste
mots = ['security', 'python', 'network', 'hacking', 'database']
mots_melanges = mots.copy()
random.shuffle(mots_melanges)
```python
print(f"\nMots originaux : {mots}")
print(f"Mots mélangés : {mots_melanges}")

```
# 4. Sélectionner aléatoirement 3 mots
selection = random.sample(mots, 3)
```python
print(f"Sélection aléatoire (3) : {selection}")

```
# 5. Numéro d'attaque
numero_attaque = random.randint(1, 1000)
```python
print(f"\nNuméro d'attaque : {numero_attaque}")

```
# Bonus : User-Agents
user_agents = [
```python
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Linux; Android 10)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14)",
```
]
ua = random.choice(user_agents)
```python
print(f"User-Agent aléatoire : {ua}")

```
SOLUTION 6 : Calculateur de hashes de sécurité

"""
Calcule les hashes de mots de passe avec hashlib
"""

```python
import hashlib

print("[*] Calculateur de hashes\n")

```
# Demander un mot de passe
mdp = input("Entrez un mot de passe : ")
mdp_bytes = mdp.encode('utf-8')

# Calculer les hashes
hash_md5 = hashlib.md5(mdp_bytes).hexdigest()
hash_sha1 = hashlib.sha1(mdp_bytes).hexdigest()
hash_sha256 = hashlib.sha256(mdp_bytes).hexdigest()
hash_sha512 = hashlib.sha512(mdp_bytes).hexdigest()

# Afficher les résultats
```python
print(f"\nMot de passe : {mdp}\n")

print(f"MD5 ({len(hash_md5)} car.)")
print(f"  Complet : {hash_md5}")
print(f"  Début  : {hash_md5[:16]}...")

print(f"\nSHA1 ({len(hash_sha1)} car.)")
print(f"  Complet : {hash_sha1}")
print(f"  Début  : {hash_sha1[:16]}...")

print(f"\nSHA256 ({len(hash_sha256)} car.)")
print(f"  Complet : {hash_sha256}")
print(f"  Début  : {hash_sha256[:16]}...")

print(f"\nSHA512 ({len(hash_sha512)} car.)")
print(f"  Complet : {hash_sha512}")
print(f"  Début  : {hash_sha512[:16]}...")

```
# Vérification d'intégrité
```python
print("\n[*] Vérification d'intégrité")
```
mdp2 = input("Entrez le même mot de passe : ")
mdp2_bytes = mdp2.encode('utf-8')
hash_mdp2 = hashlib.sha256(mdp2_bytes).hexdigest()

```python
if hash_sha256 == hash_mdp2:
    print("[+] Les hashes correspondent (même mot de passe)")
else:
    print("[-] Les hashes ne correspondent pas (mot de passe différent)")

```
SOLUTION 7 : Module personnalisé security_utils.py

FICHIER: security_utils.py

"""
Module de sécurité personnalisé
"""

```python
import random
import string
import hashlib

def verifier_mot_de_passe(mdp):
    """
    Vérifie la force du mot de passe.
    Retourne : 'Faible', 'Moyen' ou 'Fort'
    """
    if len(mdp) < 8:
        return "Faible"
    elif len(mdp) < 12:
        if any(c.isupper() for c in mdp) and any(c.isdigit() for c in mdp):
            return "Moyen"
        return "Faible"
    else:
        # Fort si 12+ caractères avec majuscules, chiffres et spéciaux
        has_upper = any(c.isupper() for c in mdp)
        has_digit = any(c.isdigit() for c in mdp)
        has_special = any(c in string.punctuation for c in mdp)

        if has_upper and has_digit:
            return "Fort"
        return "Moyen"

def generer_token(longueur=32):
    """
    Génère un token aléatoire en hexadécimal.
    """
    return ''.join(random.choice(string.hexdigits[:-6]) for _ in range(longueur))

def hacher_mdp(mdp, algo="sha256"):
    """
    Hache un mot de passe avec l'algorithme spécifié.
    """
    mdp_bytes = mdp.encode('utf-8')

    if algo == "md5":
        return hashlib.md5(mdp_bytes).hexdigest()
    elif algo == "sha1":
        return hashlib.sha1(mdp_bytes).hexdigest()
    elif algo == "sha256":
        return hashlib.sha256(mdp_bytes).hexdigest()
    elif algo == "sha512":
        return hashlib.sha512(mdp_bytes).hexdigest()
    else:
        raise ValueError(f"Algorithme inconnu : {algo}")

def verifier_hash(texte, hash_expected, algo="sha256"):
    """
    Vérifie si le hash du texte correspond au hash attendu.
    """
    hash_calcule = hacher_mdp(texte, algo)
    return hash_calcule == hash_expected

if __name__ == "__main__":
    # Tests du module
    print("[*] Tests du module security_utils\n")

    # Test 1 : Vérification de mot de passe
    test_mdps = ["abc", "Password1", "MySecurePass123!@#"]
    for mdp in test_mdps:
        force = verifier_mot_de_passe(mdp)
        print(f"Force de '{mdp}' : {force}")

    # Test 2 : Générer un token
    print(f"\nToken généré : {generer_token()}")
    print(f"Token court (16) : {generer_token(16)}")

    # Test 3 : Hacher un mot de passe
    mdp = "MyPassword123"
    hash256 = hacher_mdp(mdp, "sha256")
    print(f"\nMot de passe : {mdp}")
    print(f"SHA256 : {hash256}")

    # Test 4 : Vérifier un hash
    est_valide = verifier_hash(mdp, hash256, "sha256")
    print(f"Vérification du hash : {est_valide}")

    # Test 5 : Hash différent
    est_valide_wrong = verifier_hash("WrongPassword", hash256, "sha256")
    print(f"Vérification avec mauvais mdp : {est_valide_wrong}")

```
FICHIER: main.py (pour utiliser le module)

"""
Script principal qui utilise security_utils
"""

```python
import security_utils

print("[*] Utilisation du module security_utils\n")

```
# Utiliser verifier_mot_de_passe
mdp_faible = "abc"
mdp_fort = "SecurePass123!@"

```python
print(f"Force de '{mdp_faible}' : {security_utils.verifier_mot_de_passe(mdp_faible)}")
print(f"Force de '{mdp_fort}' : {security_utils.verifier_mot_de_passe(mdp_fort)}")

```
# Utiliser generer_token
token = security_utils.generer_token()
```python
print(f"\nToken généré : {token}")

```
# Utiliser hacher_mdp
hash_mdp = security_utils.hacher_mdp(mdp_fort)
```python
print(f"\nHash SHA256 de '{mdp_fort}' : {hash_mdp}")

```
# Utiliser verifier_hash
est_correct = security_utils.verifier_hash(mdp_fort, hash_mdp)
```python
print(f"Vérification du hash : {est_correct}")

```
SOLUTION 8 : Red Teaming - Scanner de système complet

FICHIER: scanner.py

"""
Scanner Red Teaming complet - Énumération et simulation d'attaque
Usage : python scanner.py <target> <attempts>
Exemple : python scanner.py 192.168.1.1 10
"""

```python
import os
import sys
import time
from datetime import datetime
import random
import hashlib
import string

def afficher_entete():
    """Affiche l'en-tête du scanner."""
    print("\n" + "═" * 70)
    print("█" + " " * 68 + "█")
    print("█" + "  RED TEAMING SECURITY SCANNER  ".center(68) + "█")
    print("█" + " " * 68 + "█")
    print("═" * 70 + "\n")

def enumeration_systeme():
    """Énumère les informations système."""
    print("[*] 1. ÉNUMÉRATION SYSTÈME")
    print("-" * 70)

    print(f"Plateforme : {sys.platform}")
    print(f"Utilisateur : {os.getenv('USER') or 'N/A'}")
    print(f"Répertoire courant : {os.getcwd()}")
    print(f"Python : {sys.version.split()[0]}")
    print(f"Encodage : {sys.getdefaultencoding()}")

    # Variables d'environnement importantes
    variables_importantes = ['HOME', 'PATH', 'SHELL']
    print("\nVariables d'environnement clés :")
    for var in variables_importantes:
        valeur = os.getenv(var, 'N/A')
        if len(valeur) > 40:
            valeur = valeur[:40] + "..."
        print(f"  {var} : {valeur}")

    print()

def timing_attaque():
    """Mesure le timing de l'attaque."""
    print("[*] 2. TIMING D'ATTAQUE")
    print("-" * 70)

    debut_attaque = datetime.now()
    print(f"Début d'attaque : {debut_attaque.strftime('%Y-%m-%d %H:%M:%S')}")

    # Simulation : brute force sur 1 million de tentatives
    print("Simulation brute force (1 million) en cours...")

    temps_debut = time.time()
    for i in range(1000000):
        pass
    temps_fin = time.time()

    duree = temps_fin - temps_debut
    print(f"Durée d'exécution : {duree:.4f} secondes")
    print(f"Tentatives/seconde : {1000000/duree:.0f}")

    print()

def generation_payloads(nombre_payloads=5):
    """Génère des payloads aléatoires."""
    print("[*] 3. GÉNÉRATIONS DE PAYLOADS")
    print("-" * 70)

    payloads = []

    for i in range(nombre_payloads):
        # Payload SQL injection
        payload = f"admin' OR '1'='1 -- {random.randint(0, 9999)}"
        payload_hash = hashlib.sha256(payload.encode()).hexdigest()

        payloads.append({
            'payload': payload,
            'hash': payload_hash
        })

        print(f"Payload {i+1} : {payload}")
        print(f"  SHA256 : {payload_hash[:32]}...")

    print()
    return payloads

def generer_tokens(nombre=3):
    """Génère des tokens de session."""
    print("[*] 4. TOKENS DE SESSION")
    print("-" * 70)

    for i in range(nombre):
        token = ''.join(random.choice(string.hexdigits[:-6]) for _ in range(32))
        print(f"Token {i+1} : {token}")

    print()

def nonce_cryptographique():
    """Génère un nonce cryptographique."""
    print("[*] 5. NONCE ANTI-REPLAY")
    print("-" * 70)

    nonce = os.urandom(16).hex()
    print(f"Nonce : {nonce}")
    print(f"Longueur : {len(nonce)} caractères")

    print()

def afficher_arguments(target, attempts):
    """Affiche les arguments passés."""
    print("[*] 6. PARAMÈTRES D'ATTAQUE")
    print("-" * 70)

    print(f"Cible : {target}")
    print(f"Tentatives : {attempts}")

    print()

def afficher_footer():
    """Affiche le pied de page."""
    print("═" * 70)
    print("[+] Scan complété avec succès")
    print("═" * 70 + "\n")

def main():
    """Fonction principale du scanner."""

    # Vérifier les arguments
    if len(sys.argv) < 3:
        print("Usage : python scanner.py <target> <attempts>")
        print("Exemple : python scanner.py 192.168.1.1 10")
        sys.exit(1)

    target = sys.argv[1]
    try:
        attempts = int(sys.argv[2])
    except ValueError:
        print("[-] Le nombre de tentatives doit être un nombre entier")
        sys.exit(1)

    # Afficher les informations
    afficher_entete()
    enumeration_systeme()
    timing_attaque()
    generation_payloads(attempts)
    generer_tokens(3)
    nonce_cryptographique()
    afficher_arguments(target, attempts)
    afficher_footer()

if __name__ == "__main__":
    main()

```
RÉSUMÉ DES SOLUTIONS

## Défi 1: os.getcwd(), os.listdir(), os.path.isfile(), os.path.isdir()
## Défi 2: sys.version, sys.platform, sys.argv, sys.executable, sys.getdefaultencoding()
## Défi 3: time.time(), time.localtime(), time.strftime(), mesure de performance
## Défi 4: datetime.now(), timedelta(), datetime.fromtimestamp(), calculs de durée
## Défi 5: random.choice(), random.shuffle(), random.sample(), string module
## Défi 6: hashlib.md5(), hashlib.sha256(), hashlib.sha512(), hexdigest()
## Défi 7: Créer un module .py, utiliser __name__ == "__main__", importer le module
## Défi 8: Combiner os, sys, time, datetime, random, hashlib, gestion d'arguments

CONCEPTS CLÉS UTILISÉS :
- import et from...import
- Modules standards Python
- Création de modules personnalisés
- __name__ == "__main__"
- Gestion des arguments CLI (sys.argv)
- Manipulation de date/heure
- Génération d'aléatoire
- Hachage cryptographique
- Énumération système pour red teaming

