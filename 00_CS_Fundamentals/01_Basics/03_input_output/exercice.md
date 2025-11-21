# Exercice 03: Input et Output - Défis

## Défi 1: Calculatrice simple

Créez une calculatrice qui :
1. Demande deux nombres à l'utilisateur
2. Affiche les résultats de :
   - Addition
   - Soustraction
   - Multiplication
   - Division

Format attendu :
---
Nombre 1 : 10
Nombre 2 : 3

Résultats :
10 + 3 = 13
10 - 3 = 7
10 × 3 = 30
10 ÷ 3 = 3.33
---

## Défi 2: Configurateur de scan réseau

Créez un programme qui demande :
- IP cible
- Plage de ports (début et fin)
- Timeout en secondes
- Mode agressif (oui/non)

Puis affiche un résumé élégant de la configuration.

## Défi 3: Générateur de mot de passe

Créez un programme qui demande :
- Longueur souhaitée du mot de passe
- Inclure des majuscules ? (o/n)
- Inclure des chiffres ? (o/n)
- Inclure des symboles ? (o/n)

Affichez les paramètres choisis (pas besoin de générer vraiment
le mot de passe pour l'instant, on verra ça plus tard).

## Défi 4: Convertisseur d'unités

Créez un convertisseur qui demande :
- Valeur en octets (bytes)

Et affiche les conversions en :
- Kilooctets (KB) - divisé par 1024
- Mégaoctets (MB) - divisé par 1024²
- Gigaoctets (GB) - divisé par 1024³

Exemple :
Entrez la taille en octets : 1073741824

Conversions :
1073741824 bytes
1048576.00 KB
1024.00 MB
1.00 GB

## Défi 5: Profil d'attaquant

Créez un questionnaire pour créer un profil :
- Pseudo
- Niveau (débutant/intermédiaire/expert)
- Spécialité (web/réseau/système/autre)
- Années d'expérience
- Certifications (combien)

Affichez un profil formaté comme une carte d'identité.

## Défi 6: Simulateur de connexion

Créez un simulateur de connexion SSH :
1. Demander l'IP
2. Demander le port (défaut 22)
3. Demander le nom d'utilisateur
4. Demander le mot de passe (s'affiche normalement, on verra
   comment le cacher plus tard)

Affichez un message de connexion réussie avec un résumé.

Exemple :
[*] Connexion à 192.168.1.100:22...
[*] Utilisateur : admin
[+] Connexion établie avec succès !

## Défi 7: Menu avec boucle

Créez un menu qui :
1. Affiche les options
2. Demande le choix de l'utilisateur
3. Affiche un message selon le choix
4. Demande si l'utilisateur veut continuer (o/n)
5. Si oui, réaffiche le menu
6. Si non, quitte le programme

DÉFI BONUS : Encodeur de texte

Créez un programme qui :
1. Demande un texte à encoder
2. Demande le type d'encodage :
   - [1] Base64 (simulé)
   - [2] ROT13 (simulé)
   - [3] Hexadécimal (simulé)

Pour l'instant, affichez juste les paramètres choisis.
On implémentera vraiment l'encodage dans les exercices suivants.

Format :
╔═══════════════════════════════════════╗
║        ENCODEUR DE TEXTE              ║
╠═══════════════════════════════════════╣
║ Texte original : Hello World          ║
║ Méthode : Base64                      ║
║                                       ║
║ [Encodage sera implémenté plus tard] ║
╚═══════════════════════════════════════╝

## Conseils

1. input() retourne TOUJOURS une chaîne (str)
2. Convertissez avec int() ou float() pour les nombres
3. Utilisez .lower() ou .upper() pour comparer les strings
4. Utilisez or pour les valeurs par défaut : input("Port [80] : ") or "80"
5. Formatez avec f-strings : f"{variable:.2f}"
6. Gérez les erreurs potentielles (on verra ça mieux plus tard)

