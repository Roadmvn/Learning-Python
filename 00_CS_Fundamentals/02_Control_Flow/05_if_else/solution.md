# Exercice 05: Structures conditionnelles - Solutions

## Solution Défi 1: Vérificateur de majorité

age = int(input("Entrez votre âge : "))

```python
if age >= 18:
    print("Vous êtes majeur")
else:
    print("Vous êtes mineur")

## Solution Défi 2: Authentification simple

```
username = input("Nom d'utilisateur : ")
password = input("Mot de passe : ")

```python
if username == "admin" and password == "secure123":
    print("[+] Accès autorisé")
else:
    print("[-] Accès refusé")

## Solution Défi 3: Classificateur de ports

```
port = int(input("Numéro de port : "))

```python
if port == 0:
    print("Port invalide")
elif port >= 1 and port <= 1023:
    print(f"Port {port} : Privilégié")
elif port >= 1024 and port <= 49151:
    print(f"Port {port} : Enregistré")
elif port >= 49152 and port <= 65535:
    print(f"Port {port} : Dynamique/Privé")
else:
    print("Port invalide (> 65535)")

## Solution Défi 4: Analyseur de code HTTP

```
# Version avec match/case (Python 3.10+)
code = int(input("Code de statut HTTP : "))

match code:
```python
    case 200:
        print("200 : OK")
    case 301:
        print("301 : Moved Permanently")
    case 400:
        print("400 : Bad Request")
    case 401:
        print("401 : Unauthorized")
    case 403:
        print("403 : Forbidden")
    case 404:
        print("404 : Not Found")
    case 500:
        print("500 : Internal Server Error")
    case _:
        print(f"{code} : Code inconnu")

```
# Version avec if/elif/else (compatible toutes versions)
code = int(input("Code de statut HTTP : "))

```python
if code == 200:
    print("200 : OK")
elif code == 301:
    print("301 : Moved Permanently")
elif code == 400:
    print("400 : Bad Request")
elif code == 401:
    print("401 : Unauthorized")
elif code == 403:
    print("403 : Forbidden")
elif code == 404:
    print("404 : Not Found")
elif code == 500:
    print("500 : Internal Server Error")
else:
    print(f"{code} : Code inconnu")

## Solution Défi 5: Vérificateur de force de mot de passe

```
password = input("Entrez un mot de passe : ")

longueur = len(password)
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_special = any(not c.isalnum() for c in password)

if longueur < 8:
```python
    force = "FAIBLE"
elif longueur >= 12 and has_upper and has_lower and has_digit and has_special:
    force = "FORT"
elif longueur >= 8 and (has_upper or has_lower) and has_digit:
    force = "MOYEN"
else:
    force = "FAIBLE"

print(f"\nMot de passe : {password}")
print(f"Force : {force}")

## Solution Défi 6: Détecteur de protocole sécurisé

```
url = input("Entrez une URL : ")

```python
if url.startswith("https://"):
    print("[+] Connexion sécurisée")
elif url.startswith("http://"):
    print("[!] ATTENTION : Connexion non sécurisée")
else:
    print("[-] URL invalide")

## Solution Défi 7: Système de tentatives d'authentification

```
correct_password = "password123"
max_attempts = 3

```python
for attempt in range(1, max_attempts + 1):
    password = input(f"Tentative {attempt}/{max_attempts} - Mot de passe : ")

    if password == correct_password:
        print("[+] Accès accordé")
        break
    else:
        remaining = max_attempts - attempt
        if remaining > 0:
            print(f"[-] Incorrect, il reste {remaining} tentative(s)\n")
        else:
            print("[!] Compte bloqué après 3 tentatives échouées")

## Solution Défi 8: Analyseur de niveau de menace

```
score = int(input("Score de menace (0-100) : "))

```python
if score >= 90 and score <= 100:
    niveau = "CRITIQUE"
    action = "Bloquer immédiatement"
elif score >= 70 and score <= 89:
    niveau = "ÉLEVÉ"
    action = "Isoler et analyser"
elif score >= 40 and score <= 69:
    niveau = "MOYEN"
    action = "Surveiller de près"
elif score >= 10 and score <= 39:
    niveau = "FAIBLE"
    action = "Logger uniquement"
elif score >= 0 and score <= 9:
    niveau = "NÉGLIGEABLE"
    action = "Ignorer"
else:
    niveau = "INVALIDE"
    action = "Score hors limites"

print(f"\nScore : {score}")
print(f"Niveau : {niveau}")
print(f"Action : {action}")

## Solution Défi 9: Validateur d'adresse IP privée

```
ip = input("Adresse IP : ")

# Vérification pour les plages d'IP privées
```python
if ip.startswith("10."):
    print(f"[+] {ip} est une IP privée (Classe A)")
elif ip.startswith("192.168."):
    print(f"[+] {ip} est une IP privée (Classe C)")
elif ip.startswith("172."):
    # Vérifier si c'est dans la plage 172.16.x.x à 172.31.x.x
    second_octet = int(ip.split('.')[1])
    if second_octet >= 16 and second_octet <= 31:
        print(f"[+] {ip} est une IP privée (Classe B)")
    else:
        print(f"[-] {ip} est une IP publique")
else:
    print(f"[-] {ip} est une IP publique")

## Solution Défi 10: Scanner de vulnérabilités basique

print("═══════════════════════════════════════")
print("  SCANNER DE VULNÉRABILITÉS")
print("═══════════════════════════════════════\n")

```
ssl = input("SSL activé ? (o/n) : ").lower()
firewall = input("Firewall activé ? (o/n) : ").lower()
password_changed = input("Mot de passe par défaut changé ? (o/n) : ").lower()
debug_disabled = input("Mode debug désactivé ? (o/n) : ").lower()
updates = input("Mises à jour récentes ? (o/n) : ").lower()

# Calcul du score
score = 0

if ssl == 'o':
```python
    score += 20
if firewall == 'o':
    score += 20
if password_changed == 'o':
    score += 20
if debug_disabled == 'o':
    score += 20
if updates == 'o':
    score += 20

```
# Classification
if score == 100:
```python
    niveau = "EXCELLENT"
elif score >= 80:
    niveau = "BON"
elif score >= 60:
    niveau = "MOYEN"
elif score >= 40:
    niveau = "FAIBLE"
else:
    niveau = "CRITIQUE"

print("\n═══════════════════════════════════════")
print("  RÉSULTAT DE L'ANALYSE")
print("═══════════════════════════════════════")
print(f"Score de sécurité : {score}/100")
print(f"Niveau : {niveau}")
print("═══════════════════════════════════════")

```
SOLUTION BONUS : Système de contrôle d'accès multi-niveaux

```python
print("╔════════════════════════════════════════════════╗")
print("║    SYSTÈME DE CONTRÔLE D'ACCÈS SÉCURISÉ        ║")
print("╚════════════════════════════════════════════════╝\n")

```
# Saisie des informations
username = input("Nom d'utilisateur : ")
password = input("Mot de passe : ")
role = input("Rôle (admin/user/guest) : ").lower()
ip = input("Adresse IP : ")
heure = int(input("Heure actuelle (0-23) : "))

# Variable pour stocker la raison du refus
acces_refuse = False
raison = ""

# Vérification des identifiants selon le rôle
```python
if role == "admin":
    if username != "admin" or password != "admin123":
        acces_refuse = True
        raison = "Identifiants incorrects"
    elif not ip.startswith("192.168.1."):
        acces_refuse = True
        raison = "IP non autorisée pour admin (doit commencer par 192.168.1.)"
    # Admin a accès 24h/24, pas de vérification d'horaire

elif role == "user":
    if username != "user" or password != "user123":
        acces_refuse = True
        raison = "Identifiants incorrects"
    elif not ip.startswith("192.168."):
        acces_refuse = True
        raison = "IP non autorisée pour user (doit commencer par 192.168.)"
    elif heure < 8 or heure > 18:
        acces_refuse = True
        raison = f"Horaire non autorisé pour user (8h-18h) - Heure actuelle : {heure}h"

elif role == "guest":
    if username != "guest" or password != "guest123":
        acces_refuse = True
        raison = "Identifiants incorrects"
    # Guest peut se connecter depuis n'importe quelle IP
    elif heure < 9 or heure > 17:
        acces_refuse = True
        raison = f"Horaire non autorisé pour guest (9h-17h) - Heure actuelle : {heure}h"

else:
    acces_refuse = True
    raison = "Rôle invalide"

```
# Affichage du résultat
```python
print("\n" + "═" * 50)
if not acces_refuse:
    print("[+] ACCÈS AUTORISÉ")
    print(f"[+] Bienvenue {username} ({role})")
    print(f"[+] IP : {ip}")
    print(f"[+] Heure : {heure}h")
else:
    print("[-] ACCÈS REFUSÉ")
    print(f"[-] Raison : {raison}")
    print(f"[-] Utilisateur : {username}")
    print(f"[-] Rôle : {role}")
    print(f"[-] IP : {ip}")
    print(f"[-] Heure : {heure}h")
print("═" * 50)

```
POINTS CLÉS

1. if : exécute un bloc si la condition est True
2. else : exécute un bloc si la condition if est False
3. elif : teste une autre condition si les précédentes sont False
4. and : toutes les conditions doivent être True
5. or : au moins une condition doit être True
6. not : inverse la condition
7. Opérateur ternaire : valeur_if_true if condition else valeur_if_false
8. match/case : élégant pour tester une variable (Python 3.10+)
9. Conditions imbriquées : if dans un if
10. Indentation obligatoire (4 espaces)

BONNES PRATIQUES

1. Utilisez elif au lieu de multiples if quand les conditions sont exclusives
2. Mettez les conditions les plus probables en premier
3. Utilisez l'opérateur ternaire pour les assignations simples uniquement
4. Préférez match/case pour les tests multiples d'une même variable
5. Évitez les conditions imbriquées trop profondes (max 3 niveaux)
6. Utilisez des variables booléennes pour clarifier les conditions complexes
7. Commentez les conditions non évidentes
8. Groupez les vérifications liées ensemble
9. Validez toujours les entrées utilisateur
10. Pensez à tous les cas possibles (edge cases)

ERREURS COURANTES À ÉVITER

1. Oublier les deux-points (:) après if/elif/else
2. Mauvaise indentation (doit être cohérente)
3. Utiliser = au lieu de == pour la comparaison
4. Confondre and/or dans les conditions
5. Oublier les parenthèses dans les conditions complexes
6. Ne pas gérer le cas else/default
7. Tester les conditions dans le mauvais ordre
8. Comparer des types différents (int vs string)
9. Conditions imbriquées trop complexes (refactoriser)
10. Ne pas valider les entrées utilisateur

ASTUCES AVANCÉES

1. Utilisez .lower() ou .upper() pour les comparaisons de texte
2. .startswith() et .endswith() pour vérifier le début/fin de chaînes
3. in pour vérifier si une valeur est dans une liste
4. any() et all() pour vérifier plusieurs conditions
5. try/except pour gérer les erreurs de conversion (int(), float())
6. Variables booléennes pour rendre les conditions lisibles
7. Dictionnaires pour remplacer de longs if/elif
8. Fonctions pour éviter la répétition de conditions
9. Early return pour sortir rapidement des fonctions
10. Guard clauses pour valider les conditions en premier

