# Exercice 04: Opérateurs - Solutions

## Solution Défi 1: Calculatrice avancée

n1 = float(input("Premier nombre : "))
n2 = float(input("Deuxième nombre : "))

```python
print(f"\n{n1} + {n2} = {n1 + n2}")
print(f"{n1} - {n2} = {n1 - n2}")
print(f"{n1} × {n2} = {n1 * n2}")
print(f"{n1} ÷ {n2} = {n1 / n2:.2f}")
print(f"{n1} ÷÷ {n2} = {n1 // n2}")
print(f"{n1} % {n2} = {n1 % n2}")
print(f"{n1} ^ {n2} = {n1 ** n2}")

## Solution Défi 2: Vérificateur pair/impair

```
nombre = int(input("Entrez un nombre : "))

```python
if nombre % 2 == 0:
    print(f"{nombre} est PAIR")
else:
    print(f"{nombre} est IMPAIR")

```
# Ou en une ligne avec opérateur ternaire
resultat = "PAIR" if nombre % 2 == 0 else "IMPAIR"
```python
print(f"{nombre} est {resultat}")

## Solution Défi 3: Validateur de port

```
port = int(input("Numéro de port : "))

valide = (port >= 1) and (port <= 65535)
privilegie = port < 1024
est_ssh = port == 22
est_http_https = (port == 80) or (port == 443)

```python
print(f"\nPort : {port}")
print(f"Valide : {valide}")
print(f"Privilégié : {privilegie}")
print(f"SSH : {est_ssh}")
print(f"HTTP/HTTPS : {est_http_https}")

## Solution Défi 4: Vérificateur d'authentification

```
username = input("Username : ")
password = input("Password : ")

acces_autorise = (username == "admin") and (password == "password123")

```python
if acces_autorise:
    print("\n[+] Accès autorisé")
else:
    print("\n[-] Accès refusé")

## Solution Défi 5: Calculateur de masque

```
masque = int(input("Masque de sous-réseau (ex: 24) : "))

nombre_hotes = (2 ** (32 - masque)) - 2

```python
print(f"\nMasque : /{masque}")
print(f"Nombre d'hôtes : {nombre_hotes}")

## Solution Défi 6: Comparateur d'IP

```
ip1 = int(input("IP 1 (notation décimale) : "))
ip2 = int(input("IP 2 (notation décimale) : "))

```python
if ip1 == ip2:
    print("Les deux IP sont identiques")
elif ip1 > ip2:
    print(f"IP 1 ({ip1}) est plus grande")
else:
    print(f"IP 2 ({ip2}) est plus grande")

## Solution Défi 7: Force du mot de passe

```
longueur = int(input("Longueur du mot de passe : "))

minuscules = input("Minuscules (o/n) : ").lower() == 'o'
majuscules = input("Majuscules (o/n) : ").lower() == 'o'
chiffres = input("Chiffres (o/n) : ").lower() == 'o'
symboles = input("Symboles (o/n) : ").lower() == 'o'

# Calcul de la taille de l'alphabet
alphabet = 0
if minuscules:
```python
    alphabet += 26
if majuscules:
    alphabet += 26
if chiffres:
    alphabet += 10
if symboles:
    alphabet += 32

```
# Calcul des combinaisons
combinaisons = alphabet ** longueur

```python
print(f"\n╔════════════════════════════════════════╗")
print(f"║   ANALYSE DE FORCE DU MOT DE PASSE     ║")
print(f"╠════════════════════════════════════════╣")
print(f"║ Longueur : {longueur:<28}║")
print(f"║ Taille alphabet : {alphabet:<19}║")
print(f"║ Combinaisons : {combinaisons:>23,} ║")
print(f"╚════════════════════════════════════════╝")

## Solution Défi 8: Vérificateur de plage IP

```
octet = int(input("Dernier octet de l'IP (1-254) : "))

```python
if octet >= 1 and octet <= 50:
    plage = "Plage réservée"
elif octet >= 51 and octet <= 100:
    plage = "Plage DHCP"
elif octet >= 101 and octet <= 200:
    plage = "Plage statique"
elif octet >= 201 and octet <= 254:
    plage = "Plage disponible"
else:
    plage = "Invalide"

print(f"192.168.1.{octet} → {plage}")

## Solution Défi 9: Estimateur de téléchargement

```
taille_mo = float(input("Taille du fichier (Mo) : "))
vitesse_mbps = float(input("Vitesse de connexion (Mbps) : "))

# Conversion : Mo → Mb (× 8), puis diviser par vitesse
temps_secondes = (taille_mo * 8) / vitesse_mbps

temps_minutes = temps_secondes / 60
temps_heures = temps_minutes / 60

```python
print(f"\n╔════════════════════════════════════════╗")
print(f"║  ESTIMATION DE TEMPS DE TÉLÉCHARGEMENT ║")
print(f"╠════════════════════════════════════════╣")
print(f"║ Taille : {taille_mo} Mo{' ' * (28 - len(str(taille_mo)))}║")
print(f"║ Vitesse : {vitesse_mbps} Mbps{' ' * (26 - len(str(vitesse_mbps)))}║")
print(f"║                                        ║")
print(f"║ Temps : {temps_secondes:.1f} secondes{' ' * (23 - len(str(int(temps_secondes))))}║")
print(f"║         {temps_minutes:.1f} minutes{' ' * (24 - len(str(int(temps_minutes))))}║")
print(f"║         {temps_heures:.1f} heures{' ' * (25 - len(str(int(temps_heures))))}║")
print(f"╚════════════════════════════════════════╝")

```
SOLUTION BONUS : Simulateur d'attaque bruteforce

```python
print("╔════════════════════════════════════════╗")
print("║  SIMULATEUR D'ATTAQUE BRUTEFORCE       ║")
print("╚════════════════════════════════════════╝\n")

```
longueur = int(input("Longueur du mot de passe : "))
alphabet = int(input("Taille de l'alphabet : "))
vitesse = int(input("Tentatives par seconde : "))

# Calculs
combinaisons = alphabet ** longueur
temps_pire_cas_sec = combinaisons / vitesse
temps_moyen_sec = temps_pire_cas_sec / 2

# Conversions pire cas
pire_min = temps_pire_cas_sec / 60
pire_heure = pire_min / 60
pire_jour = pire_heure / 24
pire_annee = pire_jour / 365

# Conversions moyen cas
moyen_min = temps_moyen_sec / 60
moyen_heure = moyen_min / 60
moyen_jour = moyen_heure / 24
moyen_annee = moyen_jour / 365

```python
print("\n╔════════════════════════════════════════════════════════╗")
print("║        ANALYSE DE L'ATTAQUE BRUTEFORCE                 ║")
print("╠════════════════════════════════════════════════════════╣")
print(f"║ Longueur mot de passe : {longueur:<30}║")
print(f"║ Taille alphabet       : {alphabet:<30}║")
print(f"║ Vitesse               : {vitesse:,} tentatives/s{' ' * (14 - len(str(vitesse)) - (len(str(vitesse)) // 4))}║")
print("║                                                        ║")
print(f"║ Combinaisons possibles : {combinaisons:,}{' ' * (28 - len(str(combinaisons)) - (len(str(combinaisons)) - 1) // 3)}║")
print("╠════════════════════════════════════════════════════════╣")
print("║ PIRE CAS (toutes les combinaisons)                    ║")
print(f"║   {temps_pire_cas_sec:,.0f} secondes{' ' * (40 - len(str(int(temps_pire_cas_sec))) - (len(str(int(temps_pire_cas_sec))) - 1) // 3)}║")
print(f"║   {pire_min:,.0f} minutes{' ' * (41 - len(str(int(pire_min))) - (len(str(int(pire_min))) - 1) // 3)}║")
print(f"║   {pire_heure:,.0f} heures{' ' * (42 - len(str(int(pire_heure))) - (len(str(int(pire_heure))) - 1) // 3)}║")
print(f"║   {pire_jour:,.0f} jours{' ' * (43 - len(str(int(pire_jour))) - (len(str(int(pire_jour))) - 1) // 3)}║")
print(f"║   {pire_annee:,.0f} années{' ' * (42 - len(str(int(pire_annee))) - (len(str(int(pire_annee))) - 1) // 3)}║")
print("║                                                        ║")
print("║ CAS MOYEN (50% des combinaisons)                      ║")
print(f"║   {temps_moyen_sec:,.0f} secondes{' ' * (40 - len(str(int(temps_moyen_sec))) - (len(str(int(temps_moyen_sec))) - 1) // 3)}║")
print(f"║   {moyen_annee:,.0f} années{' ' * (42 - len(str(int(moyen_annee))) - (len(str(int(moyen_annee))) - 1) // 3)}║")
print("╚════════════════════════════════════════════════════════╝")

```
POINTS CLÉS

1. Opérateurs arithmétiques : +, -, *, /, //, %, **
2. Opérateurs de comparaison : ==, !=, <, >, <=, >=
3. Opérateurs logiques : and, or, not
4. Priorité : () > ** > *, /, //, % > +, - > comparaison > not > and > or
5. Opérateurs d'assignation : +=, -=, *=, /=, //=, %=, **=

