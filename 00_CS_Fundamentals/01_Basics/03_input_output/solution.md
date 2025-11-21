# Exercice 03: Input et Output - Solutions

## Solution Défi 1: Calculatrice simple

nombre1 = float(input("Nombre 1 : "))
nombre2 = float(input("Nombre 2 : "))

```python
print("\nRésultats :")
print(f"{nombre1} + {nombre2} = {nombre1 + nombre2}")
print(f"{nombre1} - {nombre2} = {nombre1 - nombre2}")
print(f"{nombre1} × {nombre2} = {nombre1 * nombre2}")
print(f"{nombre1} ÷ {nombre2} = {nombre1 / nombre2:.2f}")

## Solution Défi 2: Configurateur de scan réseau

print("═" * 50)
print("CONFIGURATEUR DE SCAN RÉSEAU")
print("═" * 50 + "\n")

```
ip_cible = input("IP cible : ")
port_debut = int(input("Port de début : "))
port_fin = int(input("Port de fin : "))
timeout = float(input("Timeout (secondes) : "))
agressif = input("Mode agressif (o/n) : ").lower() == 'o'

```python
print("\n╔════════════════════════════════════════╗")
print("║    CONFIGURATION DU SCAN ENREGISTRÉE   ║")
print("╠════════════════════════════════════════╣")
print(f"║ IP cible   : {ip_cible:<24}║")
print(f"║ Ports      : {port_debut} - {port_fin}{' ' * (25 - len(str(port_debut)) - len(str(port_fin)) - 3)}║")
print(f"║ Timeout    : {timeout}s{' ' * (24 - len(str(timeout)) - 1)}║")
print(f"║ Agressif   : {'Oui' if agressif else 'Non'}{' ' * 21}║")
print(f"║ Nb ports   : {port_fin - port_debut + 1}{' ' * (24 - len(str(port_fin - port_debut + 1)))}║")
print("╚════════════════════════════════════════╝")

## Solution Défi 3: Générateur de mot de passe

print("╔═══════════════════════════════════════╗")
print("║    GÉNÉRATEUR DE MOT DE PASSE         ║")
print("╚═══════════════════════════════════════╝\n")

```
longueur = int(input("Longueur du mot de passe : "))
majuscules = input("Inclure des majuscules (o/n) : ").lower() == 'o'
chiffres = input("Inclure des chiffres (o/n) : ").lower() == 'o'
symboles = input("Inclure des symboles (o/n) : ").lower() == 'o'

```python
print("\n═" * 50)
print("PARAMÈTRES DU MOT DE PASSE")
print("═" * 50)
print(f"Longueur    : {longueur} caractères")
print(f"Majuscules  : {'✓' if majuscules else '✗'}")
print(f"Chiffres    : {'✓' if chiffres else '✗'}")
print(f"Symboles    : {'✓' if symboles else '✗'}")
print("═" * 50)

```
# Construction de l'alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"
if majuscules:
```python
    alphabet += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if chiffres:
    alphabet += "0123456789"
if symboles:
    alphabet += "!@#$%^&*()_+-=[]{}|;:,.<>?"

print(f"Alphabet : {alphabet}")

## Solution Défi 4: Convertisseur d'unités

```
taille_bytes = int(input("Entrez la taille en octets : "))

kb = taille_bytes / 1024
mb = taille_bytes / (1024 ** 2)
gb = taille_bytes / (1024 ** 3)

```python
print("\nConversions :")
print(f"{taille_bytes} bytes")
print(f"{kb:.2f} KB")
print(f"{mb:.2f} MB")
print(f"{gb:.2f} GB")

```
# Version avec formatage automatique
```python
if gb >= 1:
    print(f"\nTaille optimale : {gb:.2f} GB")
elif mb >= 1:
    print(f"\nTaille optimale : {mb:.2f} MB")
elif kb >= 1:
    print(f"\nTaille optimale : {kb:.2f} KB")
else:
    print(f"\nTaille optimale : {taille_bytes} bytes")

## Solution Défi 5: Profil d'attaquant

print("╔═══════════════════════════════════════╗")
print("║    CRÉATION DE PROFIL D'ATTAQUANT     ║")
print("╚═══════════════════════════════════════╝\n")

```
pseudo = input("Pseudo : ")
niveau = input("Niveau (débutant/intermédiaire/expert) : ")
specialite = input("Spécialité (web/réseau/système/autre) : ")
experience = int(input("Années d'expérience : "))
certifications = int(input("Nombre de certifications : "))

```python
print("\n╔═══════════════════════════════════════════════════════╗")
print("║              CARTE D'IDENTITÉ PENTESTER               ║")
print("╠═══════════════════════════════════════════════════════╣")
print(f"║ Pseudo         : {pseudo:<36}║")
print(f"║ Niveau         : {niveau:<36}║")
print(f"║ Spécialité     : {specialite:<36}║")
print(f"║ Expérience     : {experience} ans{' ' * (32 - len(str(experience)))}║")
print(f"║ Certifications : {certifications}{' ' * (36 - len(str(certifications)))}║")
print("╚═══════════════════════════════════════════════════════╝")

## Solution Défi 6: Simulateur de connexion

print("╔═══════════════════════════════════════╗")
print("║       SIMULATEUR DE CONNEXION SSH     ║")
print("╚═══════════════════════════════════════╝\n")

```
ip = input("IP cible : ")
port = input("Port [22] : ") or "22"
port = int(port)
username = input("Nom d'utilisateur : ")
password = input("Mot de passe : ")

```python
print(f"\n[*] Connexion à {ip}:{port}...")
print(f"[*] Utilisateur : {username}")
print("[*] Authentification en cours...")
print("[+] Connexion établie avec succès !")
print("\n╔═══════════════════════════════════════════════════════╗")
print("║                 SESSION SSH ACTIVE                    ║")
print("╠═══════════════════════════════════════════════════════╣")
print(f"║ Serveur  : {ip}:{port}{' ' * (39 - len(ip) - len(str(port)))}║")
print(f"║ Utilisateur : {username}{' ' * (37 - len(username))}║")
print("╚═══════════════════════════════════════════════════════╝")

## Solution Défi 7: Menu avec boucle

```
continuer = True

```python
while continuer:
    print("\n╔════════════════════════════════════════╗")
    print("║         RED TEAM TOOLKIT               ║")
    print("╠════════════════════════════════════════╣")
    print("║ [1] Scanner de ports                   ║")
    print("║ [2] Cracker de mots de passe           ║")
    print("║ [3] Générateur de payload              ║")
    print("║ [4] Quitter                            ║")
    print("╚════════════════════════════════════════╝\n")

    choix = input("Votre choix : ")

    if choix == "1":
        print("\n[*] Lancement du scanner de ports...")
        print("[+] Scan terminé")
    elif choix == "2":
        print("\n[*] Lancement du cracker...")
        print("[+] Cracking terminé")
    elif choix == "3":
        print("\n[*] Génération du payload...")
        print("[+] Payload généré")
    elif choix == "4":
        print("\n[*] Au revoir !")
        continuer = False
        break
    else:
        print("\n[-] Choix invalide")

    if continuer:
        reponse = input("\nContinuer ? (o/n) : ")
        if reponse.lower() != 'o':
            continuer = False
            print("[*] Au revoir !")

```
SOLUTION BONUS : Encodeur de texte

```python
print("╔═══════════════════════════════════════╗")
print("║        ENCODEUR DE TEXTE              ║")
print("╚═══════════════════════════════════════╝\n")

```
texte = input("Texte à encoder : ")

```python
print("\nMéthodes d'encodage :")
print("[1] Base64")
print("[2] ROT13")
print("[3] Hexadécimal")

```
choix = input("\nVotre choix : ")

methodes = {
    "1": "Base64",
    "2": "ROT13",
```python
    "3": "Hexadécimal"
```
}

methode = methodes.get(choix, "Inconnue")

```python
print("\n╔═══════════════════════════════════════╗")
print("║        ENCODEUR DE TEXTE              ║")
print("╠═══════════════════════════════════════╣")
print(f"║ Texte original : {texte:<20}║")
print(f"║ Méthode : {methode:<27}║")
print("║                                       ║")
print("║ [Encodage sera implémenté plus tard] ║")
print("╚═══════════════════════════════════════╝")

```
POINTS CLÉS

1. input() retourne TOUJOURS une chaîne (str)
2. Convertissez avec int(), float() pour les calculs
3. Utilisez or pour les valeurs par défaut
4. .lower() et .upper() pour comparer les chaînes
5. f-strings pour formater l'affichage
6. Créez des interfaces utilisateur claires et intuitives

