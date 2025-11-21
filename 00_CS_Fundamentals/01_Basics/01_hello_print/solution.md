# Exercice 01: Hello Print - Solutions

> [!IMPORTANT] Essayez les défis par vous-même avant de regarder !

## Solution Défi 1: Présentation personnelle

```python
print("---")
print("Nom : Jean Dupont")
print("Âge : 25")
print("Ville : Paris")
print("Objectif : Devenir pentester professionnel")
print("---")

```
OU avec une seule ligne :

```python
print("---\nNom : Jean Dupont\nÂge : 25\nVille : Paris\nObjectif : Devenir pentester\n---")

## Solution Défi 2: Banner ASCII Art

print("""
```
 ____  _   _ _   _  ____ _  __ _____ ____
|  _ \| \ | | | | |/ ___| |/ /| ____|  _ \\
| | | |  \| | | | | |   | ' / |  _| | |_) |
| |_| | |\  | |_| | |___| . \ | |___|  _ <
|____/|_| \_|\___/ \____|_|\_\|_____|_| \_\\
""")

## Solution Défi 3: Menu d'application

```python
print("╔════════════════════════════════════════╗")
print("║         RED TEAM TOOLKIT v1.0          ║")
print("╠════════════════════════════════════════╣")
print("║                                        ║")
print("║  [1] Port Scanner                      ║")
print("║  [2] Password Cracker                  ║")
print("║  [3] Keylogger                         ║")
print("║  [4] Packet Sniffer                    ║")
print("║  [5] Exit                              ║")
print("║                                        ║")
print("╚════════════════════════════════════════╝")

```
OU plus élégamment avec des variables :

largeur = 42
titre = "RED TEAM TOOLKIT v1.0"
options = [
```python
    "[1] Port Scanner",
    "[2] Password Cracker",
    "[3] Keylogger",
    "[4] Packet Sniffer",
    "[5] Exit"
```
]

```python
print("╔" + "═" * largeur + "╗")
print("║" + titre.center(largeur) + "║")
print("╠" + "═" * largeur + "╣")
print("║" + " " * largeur + "║")
for option in options:
    print("║  " + option.ljust(largeur - 3) + "║")
print("║" + " " * largeur + "║")
print("╚" + "═" * largeur + "╝")

## Solution Défi 4: Affichage progressif

print("[*] Initializing...")
print("[*] Loading modules...")
print("[*] Connecting to target...")
print("[*] Scanning ports...")
print("[+] Scan complete!")

```
Avec des messages d'erreur et d'avertissement :

```python
print("[*] Starting attack...")
print("[!] Warning: Target may have IDS/IPS")
print("[*] Attempting connection...")
print("[-] Connection failed")
print("[*] Retrying...")
print("[+] Connection established!")

## Solution Défi 5: Table de données

print("+--------+----------+---------+----------+")
print("| PORT   | STATE    | SERVICE | VERSION  |")
print("+--------+----------+---------+----------+")
print("| 22     | open     | ssh     | OpenSSH  |")
print("| 80     | open     | http    | Apache   |")
print("| 443    | open     | https   | nginx    |")
print("| 3306   | closed   | mysql   | -        |")
print("+--------+----------+---------+----------+")

```
Avec formatage :

separateur = "+--------+----------+---------+----------+"
```python
print(separateur)
print("| {:<6} | {:<8} | {:<7} | {:<8} |".format("PORT", "STATE", "SERVICE", "VERSION"))
print(separateur)
print("| {:<6} | {:<8} | {:<7} | {:<8} |".format("22", "open", "ssh", "OpenSSH"))
print("| {:<6} | {:<8} | {:<7} | {:<8} |".format("80", "open", "http", "Apache"))
print("| {:<6} | {:<8} | {:<7} | {:<8} |".format("443", "open", "https", "nginx"))
print("| {:<6} | {:<8} | {:<7} | {:<8} |".format("3306", "closed", "mysql", "-"))
print(separateur)

## Solution Défi 6: Message d'avertissement

print("╔═══════════════════════════════════════════════════════════════╗")
print("║                       ⚠️  AVERTISSEMENT  ⚠️                     ║")
print("╠═══════════════════════════════════════════════════════════════╣")
print("║                                                               ║")
print("║  Cet outil est destiné à des fins éducatives uniquement.     ║")
print("║                                                               ║")
print("║  Utilisation non autorisée sur des systèmes tiers est        ║")
print("║  ILLÉGALE et peut entraîner des poursuites judiciaires.      ║")
print("║                                                               ║")
print("║  Assurez-vous d'avoir une autorisation écrite avant          ║")
print("║  d'utiliser cet outil sur tout système.                      ║")
print("║                                                               ║")
print("╚═══════════════════════════════════════════════════════════════╝")

```
SOLUTION BONUS : Programme complet

```python
def afficher_banner():
    print()
    print("╔════════════════════════════════════════════════════════════╗")
    print("║                                                            ║")
    print("║  ██████╗ ███████╗██████╗     ████████╗███████╗ █████╗ ███╗")
    print("║  ██╔══██╗██╔════╝██╔══██╗    ╚══██╔══╝██╔════╝██╔══██╗████║")
    print("║  ██████╔╝█████╗  ██║  ██║       ██║   █████╗  ███████║╚═██║")
    print("║  ██╔══██╗██╔══╝  ██║  ██║       ██║   ██╔══╝  ██╔══██║  ██║")
    print("║  ██║  ██║███████╗██████╔╝       ██║   ███████╗██║  ██║  ██║")
    print("║  ╚═╝  ╚═╝╚══════╝╚═════╝        ╚═╝   ╚══════╝╚═╝  ╚═╝  ╚═╝")
    print("║                                                            ║")
    print("║                 Python Security Toolkit v1.0              ║")
    print("║                                                            ║")
    print("╚════════════════════════════════════════════════════════════╝")
    print()

def afficher_menu():
    print("╔════════════════════════════════════════╗")
    print("║              MENU PRINCIPAL            ║")
    print("╠════════════════════════════════════════╣")
    print("║                                        ║")
    print("║  [1] Scanner de ports                  ║")
    print("║  [2] Cracker de mots de passe          ║")
    print("║  [3] Keylogger                         ║")
    print("║  [4] Sniffer de paquets                ║")
    print("║  [5] Quitter                           ║")
    print("║                                        ║")
    print("╚════════════════════════════════════════╝")
    print()

def afficher_statut():
    print("[*] Initialisation du système...")
    print("[+] Python : OK")
    print("[+] Modules : OK")
    print("[!] Mode éthique : ACTIVÉ")
    print("[*] Prêt à l'emploi")
    print()

def afficher_avertissement():
    print("╔═══════════════════════════════════════════════════════════════╗")
    print("║                       ⚠️  AVERTISSEMENT  ⚠️                     ║")
    print("╠═══════════════════════════════════════════════════════════════╣")
    print("║  Cet outil est à des fins éducatives UNIQUEMENT.             ║")
    print("║  Usage non autorisé = ILLÉGAL                                ║")
    print("║  Autorisation écrite requise avant toute utilisation         ║")
    print("╚═══════════════════════════════════════════════════════════════╝")
    print()

```
# Programme principal
afficher_banner()
afficher_avertissement()
afficher_statut()
afficher_menu()

## Points Clés

1. print() est votre outil principal pour afficher du texte

2. Utilisez des commentaires pour expliquer votre code

3. L'indentation compte en Python

4. Les caractères spéciaux (\n, \t) sont très utiles

5. Vous pouvez créer des interfaces visuelles avec print()

6. Organisez votre code en fonctions pour plus de clarté

7. Utilisez des variables pour éviter la répétition

8. Les chaînes multilignes (""") sont pratiques pour l'ASCII art

## Prochaine Étape

Maintenant que vous maîtrisez print(), passez à l'exercice 02
pour apprendre les variables et les types de données !

cd ../02_variables_types
cat README.md
python main.py
