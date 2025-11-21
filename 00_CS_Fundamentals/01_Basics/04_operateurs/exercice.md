# Exercice 04: Opérateurs - Défis

## Défi 1: Calculatrice avancée

Demandez deux nombres à l'utilisateur et affichez :
- Addition
- Soustraction
- Multiplication
- Division (avec 2 décimales)
- Division entière
- Modulo (reste)
- Puissance (premier nombre à la puissance du second)

## Défi 2: Vérificateur de nombre pair/impair

Créez un programme qui :
1. Demande un nombre à l'utilisateur
2. Vérifie s'il est pair ou impair
3. Affiche le résultat

Utilisez l'opérateur modulo (%).

## Défi 3: Validateur de port

Créez un programme qui demande un numéro de port et vérifie :
- Est-il valide ? (entre 1 et 65535)
- Est-il privilégié ? (< 1024)
- Est-il un port SSH ? (22)
- Est-il un port HTTP/HTTPS ? (80 ou 443)

Utilisez des opérateurs logiques (and, or, not).

## Défi 4: Vérificateur d'authentification

Créez un système qui :
1. Demande un username
2. Demande un mot de passe
3. Vérifie si c'est "admin" ET "password123"
4. Affiche "Accès autorisé" ou "Accès refusé"

Utilisez l'opérateur and.

## Défi 5: Calculateur de masque de sous-réseau

Créez un programme qui :
1. Demande un masque de sous-réseau (ex: 24 pour /24)
2. Calcule le nombre d'hôtes disponibles
   Formule : 2^(32 - masque) - 2
3. Affiche le résultat

Exemple :
Masque : /24
Nombre d'hôtes : 254

## Défi 6: Comparateur d'adresses IP

Créez un programme qui :
1. Demande deux adresses IP (en notation décimale simplifiée)
   Exemple : 192168001001 (pour 192.168.1.1)
2. Compare laquelle est "plus grande"
3. Vérifie si elles sont égales

## Défi 7: Calculateur de force de mot de passe

Créez un calculateur qui demande :
- Longueur du mot de passe
- Contient des minuscules ? (o/n) → ajoute 26 à l'alphabet
- Contient des majuscules ? (o/n) → ajoute 26 à l'alphabet
- Contient des chiffres ? (o/n) → ajoute 10 à l'alphabet
- Contient des symboles ? (o/n) → ajoute 32 à l'alphabet

Calcule et affiche :
- Taille de l'alphabet
- Nombre de combinaisons possibles (alphabet^longueur)

## Défi 8: Vérificateur de plage d'IP

Créez un programme qui :
1. Demande une adresse IP (dernier octet seulement, ex: 150)
2. Vérifie dans quelle plage elle se trouve :
   - 1-50 : Plage réservée
   - 51-100 : Plage DHCP
   - 101-200 : Plage statique
   - 201-254 : Plage disponible

Utilisez des opérateurs de comparaison et logiques.

## Défi 9: Estimateur de temps de téléchargement

Créez un programme qui :
1. Demande la taille du fichier (en Mo)
2. Demande la vitesse de connexion (en Mbps)
3. Calcule le temps de téléchargement
   Attention : 1 octet = 8 bits

Formule : (taille_mo * 8) / vitesse_mbps = temps en secondes

Affichez en secondes, minutes, et heures.

DÉFI BONUS : Simulateur d'attaque bruteforce

Créez un simulateur complet qui :
1. Demande la longueur du mot de passe cible
2. Demande le nombre de caractères possibles (alphabet)
3. Demande la vitesse d'attaque (tentatives/seconde)

Calcule et affiche :
- Nombre total de combinaisons
- Temps pour tester toutes les combinaisons (pire cas)
- Temps moyen pour trouver (pire cas / 2)
- Convertir en secondes, minutes, heures, jours, années

Affichez un rapport détaillé avec formatage élégant.

## Conseils

1. / donne un float, // donne un int
2. % (modulo) donne le reste de la division
3. ** est l'opérateur de puissance
4. and, or, not pour combiner des conditions
5. Utilisez des parenthèses pour clarifier les priorités
6. Les opérateurs de comparaison retournent True ou False

