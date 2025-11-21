# Exercice 06: Boucles - Solutions

## Solution Défi 1: Comptage simple avec for et range()

# Afficher 1 à 10
```python
print("Nombres de 1 à 10 :")
for i in range(1, 11):
    print(i)

```
# Afficher 10 à 1
```python
print("\nNombres de 10 à 1 :")
for i in range(10, 0, -1):
    print(i)

```
# Afficher les pairs de 0 à 20
```python
print("\nNombres pairs de 0 à 20 :")
for i in range(0, 21, 2):
    print(i)

## Solution Défi 2: Itération sur une liste

```
ports = {
    21: "FTP",
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL"
}

```python
print("Ports et services :\n")
for port, service in ports.items():
    print(f"Port {port:5} : {service}")

```
# Alternative avec liste d'accès direct
ports_list = [21, 22, 80, 443, 3306]
```python
for port in ports_list:
    service = ports[port]
    print(f"Port {port:5} : {service}")

## Solution Défi 3: enumerate() - Numéroter les éléments

```
users = ["alice", "bob", "charlie"]

```python
print("Liste d'utilisateurs :\n")
for num, user in enumerate(users, start=1):
    print(f"{num}. {user}")

```
# Alternative avec index manuel
```python
print("\nAlternative :")
for index, user in enumerate(users):
    print(f"{index + 1}. {user}")

## Solution Défi 4: zip() - Combiner deux listes

```
usernames = ["admin", "user1", "guest"]
passwords = ["admin123", "pass456", "guest789"]

```python
print("Identifiants :\n")
for username, password in zip(usernames, passwords):
    print(f"{username}:{password}")

## Solution Défi 5: break - Arrêter la boucle

```
wordlist = ["123456", "password", "admin123", "letmein"]
correct_password = "admin123"

```python
print("Attaque bruteforce :\n")

```
attempt = 0
```python
for password_guess in wordlist:
    attempt += 1
    print(f"Tentative {attempt} : {password_guess}", end="")

    if password_guess == correct_password:
        print(" ✓ TROUVÉ !")
        print(f"\n[+] Mot de passe trouvé en {attempt} tentative(s)")
        break
    else:
        print(" ✗")

## Solution Défi 6: continue - Sauter une itération

```
ports = [21, 22, 80, 443, 3306, 8080, 5432]
critical_ports = [22, 3306, 5432]

```python
print("Analyse des ports :\n")

for port in ports:
    if port in critical_ports:
        print(f"[!] Port {port} : CRITIQUE (skipped)")
        continue

    print(f"[i] Port {port} : Non critique")

## Solution Défi 7: while - Tentatives d'authentification

```
correct_password = "secret123"
max_attempts = 3
attempts = 0

# Simulation avec une liste de mots de passe à tester
password_list = ["wrong1", "wrong2", "secret123"]
password_index = 0

```python
print("Système d'authentification\n")

while attempts < max_attempts:
    attempts += 1
    password_attempt = password_list[password_index]
    password_index += 1

    print(f"Tentative {attempts}/{max_attempts} : {password_attempt}", end="")

    if password_attempt == correct_password:
        print(" ✓")
        print(f"\n[+] ACCÈS AUTORISÉ !")
        break
    else:
        print(" ✗")
        if attempts < max_attempts:
            remaining = max_attempts - attempts
            print(f"[-] Incorrect. {remaining} tentative(s) restante(s)\n")
        else:
            print(f"\n[-] COMPTE BLOQUÉ après {max_attempts} tentatives")

## Solution Défi 8: Boucles imbriquées - Table de multiplication

print("Table de multiplication 5x5 :\n")

for i in range(1, 6):
    for j in range(1, 6):
        product = i * j
        print(f"{product:3}", end=" ")
    print()  # Nouvelle ligne après chaque ligne

```
# Alternative avec formatage
```python
print("\n\nAvec formatage :")
for i in range(1, 6):
    for j in range(1, 6):
        product = i * j
        print(f"{i}x{j}={product:2}", end=" | ")
    print()

## Solution Défi 9: Boucles imbriquées - Scan de ports

```
hosts = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
ports = [22, 80, 443]

# Ports "ouverts" simulés
open_ports = {
```python
    "192.168.1.1": [80, 443],
    "192.168.1.2": [22, 80],
    "192.168.1.3": [443],
```
}

```python
print("Scan de ports :\n")

for host in hosts:
    print(f"Hôte {host}:")
    for port in ports:
        if port in open_ports[host]:
            print(f"  Port {port:3} : [+] OUVERT")
        else:
            print(f"  Port {port:3} : [-] FERMÉ")
    print()

## Solution Défi 10: Combinaison avancée - Audit de sécurité

```
logs = [
```python
    ("192.168.1.50", "admin", 7),
    ("10.0.0.20", "root", 2),
    ("192.168.1.50", "user", 10),
    ("172.16.0.5", "admin", 4),
```
]

# Dictionnaire pour accumuler par IP
ip_attempts = {}

# Agrégation des tentatives par IP
```python
for ip, user, attempts in logs:
    if ip not in ip_attempts:
        ip_attempts[ip] = 0
    ip_attempts[ip] += attempts

```
# Analyse et affichage
```python
print("Audit de sécurité - Tentatives d'authentification échouées\n")

```
threshold = 5
alert_count = 0

```python
for ip, total_attempts in ip_attempts.items():
    if total_attempts >= threshold:
        print(f"[!] ALERTE : {ip} - {total_attempts} tentatives échouées")
        alert_count += 1
    else:
        print(f"[i] NORMAL : {ip} - {total_attempts} tentatives")

print(f"\n[!] Nombre total d'alertes : {alert_count}")

```
SOLUTION DÉFI BONUS : Énumération d'utilisateurs avec pattern

valid_users = ["user2", "user5", "user7", "user15"]

```python
print("Énumération d'utilisateurs :\n")

```
found_count = 0

```python
for i in range(1, 21):
    username = f"user{i}"

    if username in valid_users:
        print(f"[+] {username} existe !")
        found_count += 1
    else:
        print(f"[-] {username} n'existe pas")

print(f"\n[!] Nombre d'utilisateurs énumérés : {found_count}")

```
SOLUTION DÉFI BONUS 2 : Validation de plage IP privée

test_ips = [
    "192.168.1.1",
    "10.0.0.5",
    "172.16.5.10",
    "8.8.8.8",
    "1.1.1.1",
```python
    "172.31.255.255",
```
]

private_ranges = ["10.", "192.168.", "172.16.", "172.31."]

```python
print("Validation d'adresses IP privées :\n")

```
private_count = 0
public_count = 0

for ip in test_ips:
```python
    is_private = False

    for private_prefix in private_ranges:
        if ip.startswith(private_prefix):
            print(f"[+] {ip} : PRIVÉE")
            is_private = True
            private_count += 1
            break

    if not is_private:
        print(f"[-] {ip} : PUBLIQUE")
        public_count += 1

print(f"\nRésumé : {private_count} IP(s) privée(s), {public_count} IP(s) publique(s)")

```
RÉCAPITULATIF DES CONCEPTS

1. for i in range(n) :
   - Itère de 0 à n-1
   - range(1, 11) : de 1 à 10
   - range(10, 0, -1) : de 10 à 1 (décrémentant)
   - range(0, 20, 2) : 0, 2, 4, ..., 18

2. for element in list :
   - Itère sur chaque élément de la liste
   - Compatible avec les strings, tuples, dicts, etc.

3. enumerate(list, start=1) :
   - Retourne l'index et l'élément
   - start=1 commence la numérotation à 1 au lieu de 0

4. zip(list1, list2) :
   - Combine deux listes élement par élément
   - S'arrête à la fin de la plus courte liste

5. while condition :
   - Itère tant que condition est True
   - IMPORTANT : modifier la condition pour éviter boucle infinie

6. break :
   - Arrête immédiatement la boucle
   - Continueexécution après la boucle

7. continue :
   - Saute à la prochaine itération
   - N'exécute pas le reste du code de la boucle actuelle

8. Boucles imbriquées :
   - Une boucle dans une boucle
   - Génère O(n²) itérations ou plus
   - Très utilisées en cybersécurité (énumération, scan)

