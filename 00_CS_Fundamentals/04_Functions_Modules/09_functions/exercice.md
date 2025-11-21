# Exercice 09: Fonctions - Défis

## Défi 1: Fonction de conversion de température

Créez une fonction qui :
1. Prend en paramètre une température en Celsius
2. Retourne la température convertie en Fahrenheit
3. Utilise la formule : F = (C × 9/5) + 32

Exemples d'utilisation :
- celsius_to_fahrenheit(0) doit retourner 32.0
- celsius_to_fahrenheit(100) doit retourner 212.0
- celsius_to_fahrenheit(-40) doit retourner -40.0

Bonus : Écrivez une docstring pour documenter votre fonction.

## Défi 2: Calculatrice avec *args

Créez une fonction qui :
1. Accepte un nombre variable de nombres avec *args
2. Retourne la somme, la moyenne, le min et le max

Signature : calculs(*nombres)
Retour : tuple (somme, moyenne, min, max)

Exemples :
- calculs(1, 2, 3) doit retourner (6, 2.0, 1, 3)
- calculs(10, 20, 30, 40, 50) doit retourner (150, 30.0, 10, 50)

Bonus : Gestion des cas limites (nombre d'arguments = 0)

## Défi 3: Configurateur d'outil de scan avec **kwargs

Créez une fonction qui :
1. Accepte les configurations via **kwargs
2. Affiche une configuration par défaut
3. Affiche les configurations personnalisées

Signature : configurer_scanner(**options)

Options par défaut :
- timeout: 5
- retries: 3
- verbose: False
- threads: 1

Exemples :
- configurer_scanner()
  Doit afficher les valeurs par défaut

- configurer_scanner(timeout=10, verbose=True)
  Doit afficher timeout=10, verbose=True, retries=3 (défaut), threads=1 (défaut)

## Défi 4: Vérificateur de force de mot de passe avancé

Créez une fonction qui :
1. Prend un mot de passe en paramètre
2. Retourne un score de force de 0 à 100
3. Affiche un rapport détaillé

Critères (points) :
- Longueur >= 8 : +10 points
- Longueur >= 12 : +10 points
- Longueur >= 16 : +10 points
- Contient majuscules : +15 points
- Contient minuscules : +15 points
- Contient chiffres : +15 points
- Contient caractères spéciaux : +15 points
- Sans caractères répétés : +10 points

Exemples :
- "password" : Faible (score < 40)
- "MyPassword123" : Moyen (40-70)
- "P@ssw0rd!Complex#2024" : Fort (> 70)

## Défi 5: Analyseur de logs avec filtrage

Créez une fonction qui :
1. Accepte une liste de logs
2. Accepte un type de filtrage via lambda
3. Retourne les logs filtrés

Signature : analyser_logs(logs, filtre_fonction)

Exemple de logs :
logs = [
```python
    "[INFO] Utilisateur Alice connecté",
    "[ERROR] Erreur de connexion",
    "[WARNING] Tentative d'accès non autorisé",
    "[INFO] Scan complété",
    "[ERROR] Service indisponible"
```
]

Utilisations :
- logs_erreurs = analyser_logs(logs, lambda x: "[ERROR]" in x)
- logs_info = analyser_logs(logs, lambda x: "[INFO]" in x)
- logs_longs = analyser_logs(logs, lambda x: len(x) > 30)

## Défi 6: Décorateur de fonction (advanced)

Créez une fonction wrapper qui :
1. Accepte une fonction en paramètre
2. Affiche le message "[*] Exécution de fonction_name"
3. Exécute la fonction
4. Affiche "[+] Fonction_name terminée"
5. Retourne le résultat

Signature : executer_avec_log(fonction, *args, **kwargs)

Exemple :
```python
def greet(nom):
    return f"Bonjour {nom}"

```
resultat = executer_avec_log(greet, "Alice")
# Doit afficher :
# [*] Exécution de greet
# [+] greet terminée
# Et retourner "Bonjour Alice"

## Défi 7: Générateur de signatures de requête HTTP

Créez une fonction qui :
1. Accepte une URL
2. Accepte une méthode HTTP (GET, POST, etc.) par défaut GET
3. Accepte des headers via **kwargs
4. Retourne la signature formatée

Signature : generer_signature(url, methode="GET", **headers)

Exemple :
generer_signature("http://example.com/api", "POST",
```python
                  User-Agent="CustomBot/1.0",
                  Authorization="Bearer token123")

```
Doit retourner :
"POST http://example.com/api\nUser-Agent: CustomBot/1.0\nAuthorization: Bearer token123"

## Défi 8: Scanner de vulnérabilités avec red teaming

Créez un système complet de scanning qui :
1. Crée une fonction scan_service(host, *ports, severity="CRITICAL", **options)
2. Simule le scan de ports
3. Vérifie les vulnérabilités par port
4. Retourne un rapport formaté

Cas de test :
- host: "192.168.1.100"
- ports: 22, 80, 443
- severity: "HIGH"
- options: timeout=10, verbose=True

Le rapport doit inclure :
- Ports scannés
- Services identifiés (SSH pour 22, HTTP pour 80, HTTPS pour 443)
- Vulnérabilités trouvées
- Score de risque global

Indices :
- Utilisez *args pour les ports
- Utilisez **kwargs pour les options de scan
- Combinez les deux pour une solution flexible
- Retournez un dictionnaire avec les résultats

