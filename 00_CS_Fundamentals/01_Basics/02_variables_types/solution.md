# Exercice 02: Variables et Types - Solutions

## Solution Défi 1: Profil de pentester

pseudo = "DarkH4x0r"
annees_experience = 7
taux_reussite = 0.89
certification_oscp = True
specialite = "Web Application Security"

```python
print("═" * 50)
print("PROFIL DU PENTESTER")
print("═" * 50)
print(f"Pseudo : {pseudo}")
print(f"Expérience : {annees_experience} ans")
print(f"Taux de réussite : {taux_reussite * 100:.1f}%")
print(f"Certification OSCP : {'Oui' if certification_oscp else 'Non'}")
print(f"Spécialité : {specialite}")
print("═" * 50)

## Solution Défi 2: Configuration de scan

```
ip_debut = "192.168.1.1"
ip_fin = "192.168.1.254"
port_debut = 1
port_fin = 1024
timeout = 0.5
scan_agressif = False

```python
print("╔═════════════════════════════════════════╗")
print("║     CONFIGURATION DU SCAN RÉSEAU        ║")
print("╠═════════════════════════════════════════╣")
print(f"║ Plage IP : {ip_debut} - {ip_fin}")
print(f"║ Plage ports : {port_debut} - {port_fin}")
print(f"║ Timeout : {timeout}s")
print(f"║ Mode agressif : {'Activé' if scan_agressif else 'Désactivé'}")
print("╚═════════════════════════════════════════╝")

## Solution Défi 3: Conversions de types

```
# 1. str → int
port_str = "443"
port_int = int(port_str)
```python
print(f"1. '{port_str}' → {port_int} (type: {type(port_int)})")

```
# 2. float → int (tronque, ne pas arrondir)
pi = 3.14159
pi_int = int(pi)
```python
print(f"2. {pi} → {pi_int} (type: {type(pi_int)})")

```
# 3. int → str
nombre = 192
nombre_str = str(nombre)
```python
print(f"3. {nombre} → '{nombre_str}' (type: {type(nombre_str)})")

```
# 4. str → bool (PIÈGE : toute chaîne non vide est True !)
texte = "True"
texte_bool = bool(texte)
```python
print(f"4. '{texte}' → {texte_bool} (type: {type(texte_bool)})")
print("   ⚠️  ATTENTION : bool('True') = True, mais bool('False') = True aussi !")
print(f"   bool('False') = {bool('False')}")
print("   Seule la chaîne vide donne False : bool('') = {bool('')}")

```
# 5. int → bool
zero = 0
zero_bool = bool(zero)
```python
print(f"5. {zero} → {zero_bool} (type: {type(zero_bool)})")
print(f"   bool(1) = {bool(1)}")
print(f"   bool(-1) = {bool(-1)}")

## Solution Défi 4: Calculs avec variables

```
nombre_cibles = 50
pourcentage_vulnerable = 0.35

# Calcul
nombre_cibles_vulnerables = int(nombre_cibles * pourcentage_vulnerable)

# Affichage
```python
print(f"{nombre_cibles_vulnerables} cibles sur {nombre_cibles} sont vulnérables ({pourcentage_vulnerable * 100:.0f}%)")

```
# Version plus élaborée
```python
print()
print("╔═════════════════════════════════════════╗")
print("║      ANALYSE DE VULNÉRABILITÉS          ║")
print("╠═════════════════════════════════════════╣")
print(f"║ Cibles scannées : {nombre_cibles:<22}║")
print(f"║ Cibles vulnérables : {nombre_cibles_vulnerables:<18}║")
print(f"║ Taux de vulnérabilité : {pourcentage_vulnerable * 100:.1f}%{' ' * 11}║")
print("╚═════════════════════════════════════════╝")

## Solution Défi 5: Rapport de scan

```
date_scan = "2024-01-15"
heure_debut = "14:30:00"
heure_fin = "15:45:00"
hotes_scannes = 254
hotes_up = 42
ports_ouverts = 187
vulnerabilites_trouvees = 12

```python
print("╔═══════════════════════════════════════╗")
print("║      RAPPORT DE SCAN DE RÉSEAU        ║")
print("╠═══════════════════════════════════════╣")
print(f"║ Date : {date_scan:<27}║")
print(f"║ Début : {heure_debut:<26}║")
print(f"║ Fin : {heure_fin:<28}║")
print("║                                       ║")
print(f"║ Hôtes scannés : {hotes_scannes:<19}║")
print(f"║ Hôtes actifs : {hotes_up:<20}║")
print(f"║ Ports ouverts : {ports_ouverts:<18}║")
print(f"║ Vulnérabilités : {vulnerabilites_trouvees:<17}║")
print("╚═══════════════════════════════════════╝")

## Solution Défi 6: Types de données avancés

```
# None
variable_none = None
```python
print(f"None : {variable_none} → Type : {type(variable_none)}")

```
# Hexadécimal
hex_number = 0xFF
```python
print(f"Hexadécimal 0xFF : {hex_number} → Type : {type(hex_number)}")

```
# Binaire
bin_number = 0b1010
```python
print(f"Binaire 0b1010 : {bin_number} → Type : {type(bin_number)}")

```
# Notation scientifique
scientific = 1.5e3
```python
print(f"Scientifique 1.5e3 : {scientific} → Type : {type(scientific)}")

```
# Conversions utiles
```python
print(f"\nConversions :")
print(f"255 en hexadécimal : {hex(255)}")
print(f"10 en binaire : {bin(10)}")
print(f"0xFF en décimal : {0xFF}")

```
SOLUTION BONUS : Simulateur de bruteforce

mot_de_passe_cible = "admin123"
tentative_actuelle = 15847
tentatives_max = 1000000
tentatives_par_seconde = 1500
temps_ecoule = 10.56

# Calculs
pourcentage = (tentative_actuelle / tentatives_max) * 100
tentatives_restantes = tentatives_max - tentative_actuelle
temps_restant = tentatives_restantes / tentatives_par_seconde
vitesse_moyenne = tentative_actuelle / temps_ecoule

```python
print("╔═══════════════════════════════════════════════════════╗")
print("║         ATTAQUE PAR FORCE BRUTE EN COURS             ║")
print("╠═══════════════════════════════════════════════════════╣")
print(f"║ Cible : {mot_de_passe_cible:<43}║")
print("║                                                       ║")
print(f"║ Tentatives : {tentative_actuelle:>10} / {tentatives_max:<10}     ║")
print(f"║ Progression : {pourcentage:>6.2f}%{' ' * 29}║")
print("║                                                       ║")
print(f"║ Temps écoulé : {temps_ecoule:>8.2f}s{' ' * 24}║")
print(f"║ Temps restant estimé : {temps_restant:>8.2f}s{' ' * 15}║")
print("║                                                       ║")
print(f"║ Vitesse : {vitesse_moyenne:>8.0f} tentatives/s{' ' * 15}║")
print("╚═══════════════════════════════════════════════════════╝")

```
# Barre de progression
longueur_barre = 40
rempli = int((tentative_actuelle / tentatives_max) * longueur_barre)
barre = "█" * rempli + "░" * (longueur_barre - rempli)
```python
print(f"\n[{barre}] {pourcentage:.1f}%")

```
POINTS CLÉS

1. Python a un typage dynamique - pas besoin de déclarer les types
2. Les types de base : int, float, str, bool, None
3. Utilisez type() pour vérifier le type d'une variable
4. Les conversions : int(), float(), str(), bool()
5. f-strings sont la méthode moderne pour afficher des variables
6. Nommez vos variables de façon descriptive (snake_case)
7. Attention aux pièges de conversion (bool("False") = True !)

