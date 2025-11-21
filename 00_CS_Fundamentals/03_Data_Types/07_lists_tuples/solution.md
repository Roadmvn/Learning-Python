# Exercice 07: Listes et Tuples - Solutions

## Solution Défi 1: Création et indexing

ips = ["192.168.1.1", "10.0.0.5", "172.16.0.1", "8.8.8.8", "1.1.1.1"]

```python
print("IP à l'index 0 :", ips[0])      # 192.168.1.1
print("IP à l'index -1 :", ips[-1])    # 1.1.1.1
print("IP à l'index 2 :", ips[2])      # 172.16.0.1
print("Nombre d'IPs :", len(ips))      # 5

## Solution Défi 2: Slicing de listes

```
ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 465, 993, 995]

```python
print("3 premiers ports :", ports[0:3])       # [21, 22, 23]
print("3 derniers ports :", ports[-3:])       # [465, 993, 995]
print("Ports indices 2 à 5 :", ports[2:6])    # [23, 25, 53, 80]
print("Ports paires :", ports[::2])           # [21, 23, 53, 110, 443, 993]
print("Ports inversés :", ports[::-1])
```
# [995, 993, 465, 443, 143, 110, 80, 53, 25, 23, 22, 21]

## Solution Défi 3: Modification de listes

targets = []

# Ajouter 3 IPs avec append()
targets.append("192.168.1.1")
targets.append("192.168.1.2")
targets.append("192.168.1.3")

# Ajouter 2 IPs avec extend()
targets.extend(["10.0.0.1", "10.0.0.2"])

# Insérer à la position 2
targets.insert(2, "172.16.0.1")

```python
print("Liste finale :", targets)
```
# ['192.168.1.1', '192.168.1.2', '172.16.0.1', '192.168.1.3', '10.0.0.1', '10.0.0.2']

```python
print("Nombre d'IPs :", len(targets))  # 6

## Solution Défi 4: Suppression d'éléments

```
services = ["SSH", "HTTP", "HTTPS", "FTP", "Telnet", "SMTP"]

# Supprimer "Telnet" avec remove()
services.remove("Telnet")
```python
print("Après remove('Telnet') :", services)
```
# ['SSH', 'HTTP', 'HTTPS', 'FTP', 'SMTP']

# Supprimer le premier élément avec pop(0)
first = services.pop(0)
```python
print(f"pop(0) supprime : {first}")
print("Après pop(0) :", services)
```
# ['HTTP', 'HTTPS', 'FTP', 'SMTP']

# Supprimer le dernier élément avec pop()
last = services.pop()
```python
print(f"pop() supprime : {last}")
print("Après pop() :", services)
```
# ['HTTP', 'HTTPS', 'FTP']

# Supprimer l'index 1 avec del
del services[1]
```python
print("Après del services[1] :", services)
```
# ['HTTP', 'FTP']

## Solution Défi 5: Recherche et tri

scores = [45, 23, 89, 12, 56, 78, 34, 92]

```python
print("Score maximum :", max(scores))        # 92
print("Score minimum :", min(scores))        # 12
print("Somme :", sum(scores))                # 429

```
# Trie croissant
scores_asc = scores.copy()
scores_asc.sort()
```python
print("Tri croissant :", scores_asc)
```
# [12, 23, 34, 45, 56, 78, 89, 92]

# Trie décroissant
scores_desc = scores.copy()
scores_desc.sort(reverse=True)
```python
print("Tri décroissant :", scores_desc)
```
# [92, 89, 78, 56, 45, 34, 23, 12]

# Recherche de 89
index_89 = scores.index(89)
```python
print(f"Index de 89 : {index_89}")            # 2

```
# Compte de 78
count_78 = scores.count(78)
```python
print(f"Occurrences de 78 : {count_78}")     # 1

## Solution Défi 6: Tuples et unpacking

```
# Créer un tuple
credentials = ("admin", "password123", "192.168.1.100")

# Unpacking
username, password, ip = credentials

```python
print(f"Utilisateur : {username}")      # admin
print(f"Mot de passe : {password}")     # password123
print(f"IP : {ip}")                     # 192.168.1.100

```
# Tuple vide
empty_tuple = ()
```python
print(f"Tuple vide : {empty_tuple}")

```
# Tuple d'un seul élément
single = (42,)  # ATTENTION : virgule !
```python
print(f"Tuple d'un élément : {single}")

```
# Essayer de modifier un tuple
try:
```python
    credentials[0] = "root"
except TypeError as e:
    print(f"[!] ERREUR : {e}")
    print("Les tuples ne peuvent pas être modifiés")

## Solution Défi 7: List Comprehension - Filtrage

```
nombres = list(range(1, 21))

# Nombres pairs
pairs = [x for x in nombres if x % 2 == 0]
```python
print("Nombres pairs :", pairs)
```
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Nombres impairs
impairs = [x for x in nombres if x % 2 != 0]
```python
print("Nombres impairs :", impairs)
```
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Nombres > 10
greater_than_10 = [x for x in nombres if x > 10]
```python
print("Nombres > 10 :", greater_than_10)
```
# [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Carrés de 1 à 10
carres = [x**2 for x in range(1, 11)]
```python
print("Carrés (1 à 10) :", carres)
```
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

## Solution Défi 8: List Comprehension - Cybersécurité

scan_data = [(22, "open"), (23, "closed"), (80, "open"),
```python
             (443, "open"), (3306, "filtered"), (8080, "open")]

```
# Ports ouverts
open_ports = [port for port, status in scan_data if status == "open"]
```python
print("Ports ouverts :", open_ports)
```
# [22, 80, 443, 8080]

# Ports fermés
closed_ports = [port for port, status in scan_data if status == "closed"]
```python
print("Ports fermés :", closed_ports)
```
# [23]

# Chaînes formatées
port_names = {22: "SSH", 23: "Telnet", 80: "HTTP", 443: "HTTPS",
```python
              3306: "MySQL", 8080: "HTTP-Alt"}

```
formatted = [f"Port {port} ({port_names.get(port, 'Unknown')}) : {status}"
```python
             for port, status in scan_data]

print("\nRésultats formatés :")
for result in formatted:
    print(result)

```
# Résultat :
# Port 22 (SSH) : open
# Port 23 (Telnet) : closed
# Port 80 (HTTP) : open
# Port 443 (HTTPS) : open
# Port 3306 (MySQL) : filtered
# Port 8080 (HTTP-Alt) : open

SOLUTION BONUS : Gestion de liste noire d'IP

blacklist = []

suspicious = ["203.0.113.10", "198.51.100.20", "203.0.113.10", "192.0.2.30"]

```python
print("Traitement des IPs suspectes :\n")

for ip in suspicious:
    if ip not in blacklist:
        blacklist.append(ip)
        print(f"[+] IP {ip} ajoutée à la liste noire")
    else:
        print(f"[!] IP {ip} déjà listée")

print(f"\nListe noire après ajout : {blacklist}")
print(f"Total d'IPs : {len(blacklist)}")

```
# Blanchiment d'une IP
ip_to_whitelist = blacklist[0]
blacklist.remove(ip_to_whitelist)
```python
print(f"\n[*] IP {ip_to_whitelist} supprimée de la liste noire")

print(f"Liste noire finale : {blacklist}")
print(f"Total d'IPs en liste noire : {len(blacklist)}")

```
# Résultat :
# Traitement des IPs suspectes :
#
# [+] IP 203.0.113.10 ajoutée à la liste noire
# [+] IP 198.51.100.20 ajoutée à la liste noire
# [!] IP 203.0.113.10 déjà listée
# [+] IP 192.0.2.30 ajoutée à la liste noire
#
# Liste noire après ajout : ['203.0.113.10', '198.51.100.20', '192.0.2.30']
# Total d'IPs : 3
#
# [*] IP 203.0.113.10 supprimée de la liste noire
# Liste noire finale : ['198.51.100.20', '192.0.2.30']
# Total d'IPs en liste noire : 2

EXPLICATIONS COMPLÉMENTAIRES

DIFFÉRENCES CLÉS LISTES vs TUPLES :

Listes (mutables) :
  - Syntaxe : [1, 2, 3]
  - Modifiables : liste[0] = 5
  - Méthodes : append(), remove(), sort(), etc.
  - Usage : données qui changent
  - Cas d'usage : listes d'IPs, ports scannés, services

Tuples (immutables) :
  - Syntaxe : (1, 2, 3)
  - Non modifiables : tuple[0] = 5 → ERREUR
  - Unpacking : a, b, c = tuple
  - Usage : données constantes / clés de dictionnaire
  - Cas d'usage : credentials (user, password), coordonnées (x, y)

SLICING RECAP :

liste = [0, 1, 2, 3, 4, 5]

liste[start:stop:step]
  - start : index de départ (inclus)
  - stop : index de fin (EXCLUS)
  - step : intervalle (1 = tous, 2 = tous les 2, -1 = inversé)

Exemples :
  liste[1:4]     → [1, 2, 3]       (du 1 au 4 exclu)
  liste[::2]     → [0, 2, 4]       (tous les 2)
  liste[::-1]    → [5, 4, 3, 2, 1, 0] (inversé)
  liste[2:]      → [2, 3, 4, 5]    (du 2 à la fin)
  liste[:3]      → [0, 1, 2]       (du début au 3 exclu)

LIST COMPREHENSION RECAP :

Syntaxe :
  [expression for item in iterable if condition]

Exemples :
  [x*2 for x in range(5)]          → [0, 2, 4, 6, 8]
  [x for x in range(10) if x % 2 == 0]  → [0, 2, 4, 6, 8]
  [x.upper() for x in words]       → majuscules

Équivalent à :
  result = []
  for x in range(5):
```python
      result.append(x*2)

```
OPÉRATIONS COURANTES :

Ajouter :
  append(x)      → ajoute UN élément
  extend([x,y])  → ajoute PLUSIEURS éléments
  insert(i, x)   → ajoute à l'index i

Supprimer :
  remove(x)      → supprime la 1ère occurrence de x
  pop()          → supprime et retourne le dernier
  pop(i)         → supprime et retourne l'index i
  del liste[i]   → supprime sans retourner

Chercher :
  x in liste     → booléen
  index(x)       → position du 1er x
  count(x)       → nombre d'occurrences de x

Trier/Organiser :
  sort()         → trie sur place (croissant)
  sort(reverse=True)  → trie décroissant
  reverse()      → inverse l'ordre
  sorted(liste)  → retourne une copie triée

