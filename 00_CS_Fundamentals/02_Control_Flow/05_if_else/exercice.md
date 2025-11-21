# Exercice 05: Structures conditionnelles - Défis

## Défi 1: Vérificateur de majorité

Créez un programme qui :
1. Demande l'âge de l'utilisateur
2. Affiche "Vous êtes majeur" si âge >= 18
3. Affiche "Vous êtes mineur" si âge < 18

## Défi 2: Authentification simple

Créez un système d'authentification qui :
1. Demande un nom d'utilisateur
2. Demande un mot de passe
3. Vérifie si username == "admin" ET password == "secure123"
4. Affiche "[+] Accès autorisé" ou "[-] Accès refusé"

## Défi 3: Classificateur de ports

Créez un programme qui :
1. Demande un numéro de port
2. Classe le port selon ces critères :
   - 0 : "Port invalide"
   - 1-1023 : "Port privilégié"
   - 1024-49151 : "Port enregistré"
   - 49152-65535 : "Port dynamique/privé"
   - > 65535 : "Port invalide"

Utilisez if/elif/else.

## Défi 4: Analyseur de code HTTP

Créez un programme qui :
1. Demande un code de statut HTTP
2. Affiche sa signification :
   - 200 : "OK"
   - 301 : "Moved Permanently"
   - 400 : "Bad Request"
   - 401 : "Unauthorized"
   - 403 : "Forbidden"
   - 404 : "Not Found"
   - 500 : "Internal Server Error"
   - Autre : "Code inconnu"

Utilisez match/case (Python 3.10+) ou if/elif/else.

## Défi 5: Vérificateur de force de mot de passe

Créez un programme qui demande un mot de passe et évalue sa force :

FAIBLE si :
- Longueur < 8 caractères

MOYEN si :
- Longueur >= 8 ET < 12
- Contient au moins des lettres ET des chiffres

FORT si :
- Longueur >= 12
- Contient majuscules, minuscules, chiffres ET caractères spéciaux

Affichez le niveau de force.

Indices :
- len(password) pour la longueur
- any(c.isupper() for c in password) pour les majuscules
- any(c.islower() for c in password) pour les minuscules
- any(c.isdigit() for c in password) pour les chiffres
- any(not c.isalnum() for c in password) pour les spéciaux

## Défi 6: Détecteur de protocole sécurisé

Créez un programme qui :
1. Demande une URL complète
2. Vérifie si elle commence par "https://"
3. Si OUI : affiche "[+] Connexion sécurisée"
4. Si NON (http://) : affiche "[!] ATTENTION : Connexion non sécurisée"
5. Si ni l'un ni l'autre : affiche "[-] URL invalide"

Utilisez .startswith() pour vérifier le début de la chaîne.

## Défi 7: Système de tentatives d'authentification

Créez un système qui :
1. Définit un mot de passe correct (ex: "password123")
2. Demande le mot de passe à l'utilisateur (3 fois maximum)
3. À chaque tentative :
   - Si correct : affiche "Accès accordé" et arrête
   - Si incorrect : affiche "Incorrect, il reste X tentative(s)"
4. Après 3 échecs : affiche "Compte bloqué"

Utilisez une boucle for avec range(3).

## Défi 8: Analyseur de niveau de menace

Créez un programme qui :
1. Demande un score de menace (0-100)
2. Classe le niveau :
   - 90-100 : "CRITIQUE" - "Bloquer immédiatement"
   - 70-89 : "ÉLEVÉ" - "Isoler et analyser"
   - 40-69 : "MOYEN" - "Surveiller de près"
   - 10-39 : "FAIBLE" - "Logger uniquement"
   - 0-9 : "NÉGLIGEABLE" - "Ignorer"

Affichez le niveau ET l'action recommandée.

## Défi 9: Validateur d'adresse IP privée

Créez un programme qui :
1. Demande une adresse IP (format simple : 192.168.1.1)
2. Détermine si c'est une IP privée :
   - 10.x.x.x (commence par "10.")
   - 172.16.x.x à 172.31.x.x (commence par "172.16." à "172.31.")
   - 192.168.x.x (commence par "192.168.")
3. Affiche :
   - "[+] IP privée" si c'est le cas
   - "[-] IP publique" sinon

## Défi 10: Scanner de vulnérabilités basique

Créez un programme qui analyse une configuration serveur :

Demandez à l'utilisateur (réponses o/n) :
1. SSL activé ?
2. Firewall activé ?
3. Mot de passe par défaut changé ?
4. Mode debug désactivé ?
5. Mises à jour récentes ?

Calculez un score de sécurité :
- Chaque "oui" à 1, 2, 3, 5 : +20 points
- "oui" à 4 (debug désactivé) : +20 points
- "non" : +0 points

Score final :
- 100 : "EXCELLENT"
- 80-99 : "BON"
- 60-79 : "MOYEN"
- 40-59 : "FAIBLE"
- 0-39 : "CRITIQUE"

Affichez le score et le niveau de sécurité.

DÉFI BONUS : Système de contrôle d'accès multi-niveaux

Créez un système de contrôle d'accès complet :

1. Demandez :
   - Nom d'utilisateur
   - Mot de passe
   - Rôle (admin/user/guest)
   - Adresse IP
   - Heure (0-23)

2. Règles d'accès :

   ADMIN :
   - Username: "admin", Password: "admin123"
   - IP doit commencer par "192.168.1."
   - Accès 24h/24

   USER :
   - Username: "user", Password: "user123"
   - IP doit commencer par "192.168."
   - Accès de 8h à 18h

   GUEST :
   - Username: "guest", Password: "guest123"
   - Toute IP
   - Accès de 9h à 17h

3. Vérifiez dans l'ordre :
   - Identifiants corrects ?
   - Rôle valide ?
   - IP autorisée pour ce rôle ?
   - Horaire autorisé pour ce rôle ?

4. Affichez :
   - "[+] ACCÈS AUTORISÉ" si toutes les conditions sont remplies
   - "[-] ACCÈS REFUSÉ (raison)" sinon
   - Indiquez la raison précise du refus

Utilisez des conditions imbriquées (nested if).

## Conseils

1. if vérifie une condition et exécute du code si True
2. else s'exécute si la condition if est False
3. elif teste une autre condition si les précédentes sont False
4. and, or, not permettent de combiner des conditions
5. Opérateur ternaire : valeur_si_true if condition else valeur_si_false
6. match/case (Python 3.10+) est élégant pour tester une seule variable
7. Indentation = 4 espaces (obligatoire en Python)
8. Conditions imbriquées : un if dans un if
9. .startswith() vérifie le début d'une chaîne
10. any() vérifie si au moins un élément est True

