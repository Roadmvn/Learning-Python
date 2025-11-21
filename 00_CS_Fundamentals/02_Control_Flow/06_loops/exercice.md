# Exercice 06: Boucles - Défis

## Défi 1: Comptage simple avec for et range()

Créez un programme qui :
1. Affiche les nombres de 1 à 10 avec for et range()
2. Affiche les nombres de 10 à 1 (ordre inverse)
3. Affiche les nombres pairs de 0 à 20

Indices :
- range(1, 11) pour 1 à 10
- range(10, 0, -1) pour 10 à 1
- range(0, 21, 2) pour les pairs

## Défi 2: Itération sur une liste

Créez un programme qui :
1. Crée une liste de ports : [21, 22, 80, 443, 3306]
2. Itère sur chaque port avec for
3. Pour chaque port, affiche : "Port 21 : FTP" (etc.)
4. Utilisez un dictionnaire pour mapper ports -> services

Exemple de dictionnaire :
ports = {21: "FTP", 22: "SSH", 80: "HTTP", ...}

## Défi 3: enumerate() - Numéroter les éléments

Créez un programme qui :
1. Crée une liste d'utilisateurs : ["alice", "bob", "charlie"]
2. Affiche chaque utilisateur avec son numéro de position (1, 2, 3)
3. Format : "1. alice", "2. bob", etc.

Indices :
- Utilisez enumerate(liste, start=1)
- for index, user in enumerate(...)

## Défi 4: zip() - Combiner deux listes

Créez un programme qui :
1. Crée deux listes :
   - usernames = ["admin", "user1", "guest"]
   - passwords = ["admin123", "pass456", "guest789"]
2. Combine les deux avec zip()
3. Affiche : "admin:admin123", "user1:pass456", etc.

## Défi 5: break - Arrêter la boucle

Créez un programme qui :
1. Simule une attaque bruteforce
2. Essaie les mots de passe : ["123456", "password", "admin123", "letmein"]
3. Le mot de passe correct est "admin123"
4. Arrête immédiatement dès qu'il le trouve avec break
5. Affiche le nombre de tentatives

Format :
Tentative 1 : 123456 ✗
Tentative 2 : password ✗
Tentative 3 : admin123 ✓ TROUVÉ en 3 tentatives!

## Défi 6: continue - Sauter une itération

Créez un programme qui :
1. Crée une liste de ports : [21, 22, 80, 443, 3306, 8080, 5432]
2. Les ports critiques sont : [22, 3306, 5432]
3. Affiche uniquement les ports NON critiques
4. Utilisez continue pour sauter les critiques

Format :
[i] Port 21 : Non critique
[!] Port 22 : CRITIQUE (skipped)
[i] Port 80 : Non critique
...

## Défi 7: while - Tentatives d'authentification

Créez un système d'authentification qui :
1. Définit un mot de passe correct : "secret123"
2. Permet 3 tentatives maximum
3. Utilise une boucle while
4. Demande le mot de passe à chaque tentative (simule avec une liste)
5. Affiche :
   - "Accès autorisé" dès qu'il est trouvé
   - "Tentative X/3 : Incorrect" après chaque échec
   - "Compte bloqué" après 3 échecs

Wordlist : ["wrong1", "wrong2", "secret123"]

## Défi 8: Boucles imbriquées - Table de multiplication

Créez un programme qui :
1. Affiche une table de multiplication 5x5
2. Utilisez deux boucles for imbriquées
3. Format :
   1x1=1   1x2=2   1x3=3   ...
   2x1=2   2x2=4   2x3=6   ...
   ...

## Défi 9: Boucles imbriquées - Scan de ports sur plusieurs hôtes

Créez un scanner de ports qui :
1. Scanne 3 adresses IP : ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
2. Scanne 3 ports : [22, 80, 443]
3. Utilisez deux boucles imbriquées
4. Simulez l'état : certains ports sont ouverts, d'autres fermés

Exemple de résultat simulé :
Hôte 192.168.1.1:
  Port 22  : FERMÉ
  Port 80  : OUVERT
  Port 443 : OUVERT

Hôte 192.168.1.2:
  Port 22  : OUVERT
  ...

## Défi 10: Combinaison avancée - Audit de sécurité

Créez un programme d'audit de logs d'authentification qui :
1. Analyse les tentatives d'authentification :
   logs = [
```python
       ("192.168.1.50", "admin", 7),
       ("10.0.0.20", "root", 2),
       ("192.168.1.50", "user", 10),
       ("172.16.0.5", "admin", 4),
```
   ]

2. Pour chaque IP, compte le nombre de tentatives échouées
3. Affiche une alerte si >= 5 tentatives
4. Format :
   [!] ALERTE : 192.168.1.50 - 17 tentatives échouées
   [i] NORMAL : 10.0.0.20 - 2 tentatives

5. Calculez le nombre total d'alertes

Indices :
- Utilisez une boucle pour itérer sur les logs
- Accumulez le total par IP
- Utilisez un dictionnaire pour stocker les totaux par IP
- Utilisez if/else pour vérifier le seuil

DÉFI BONUS : Énumération d'utilisateurs avec pattern

Créez un programme d'énumération d'utilisateurs qui :
1. Génère des usernames basés sur un pattern
2. Pattern : user1, user2, user3, ... user20
3. Utilisez range() pour générer les nombres
4. Testez contre une liste d'utilisateurs valides :
   valid_users = ["user2", "user5", "user7", "user15"]
5. Affiche :
   [+] user2 existe !
   [-] user1 n'existe pas
   ...
6. Compte le nombre d'utilisateurs énumérés

DÉFI BONUS 2 : Validation de plage IP privée

Créez un programme qui valide les plages IP privées :
1. Crée une liste d'IPs à tester
2. Les plages privées sont :
   - 10.0.0.0 à 10.255.255.255 (commence par "10.")
   - 172.16.0.0 à 172.31.255.255 (commence par "172.16." à "172.31.")
   - 192.168.0.0 à 192.168.255.255 (commence par "192.168.")
3. Pour chaque IP, détermine si elle est privée ou publique
4. Affiche :
   [+] 192.168.1.1 : PRIVÉE
   [-] 8.8.8.8 : PUBLIQUE
5. Résumé final du nombre d'IPs privées/publiques

## Conseils

1. for itère sur une séquence (liste, range, string, etc.)
2. while itère tant que condition est True (attention : boucle infinie !)
3. range(stop) génère 0 à stop-1
4. range(start, stop, step) contrôle le début, fin et pas
5. break arrête immédiatement la boucle
6. continue saute à la prochaine itération
7. enumerate() donne l'index et la valeur
8. zip() combine plusieurs listes
9. Boucles imbriquées : une boucle dans une boucle (O(n²) attention !)
10. En cybersécurité : énumération, bruteforce, scan, audit utilisent les boucles

