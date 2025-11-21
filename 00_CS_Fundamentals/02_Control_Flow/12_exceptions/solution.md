# Exercice 12: SOLUTIONS COMPLÈTES

## Solution Défi 1: Conversion sécurisée

```python
def convertir_en_nombre(texte):
    """Convertir une chaîne en nombre de façon sécurisée."""
    try:
        numero = int(texte)
        return numero
    except ValueError:
        print(f"Erreur : '{texte}' n'est pas un nombre entier valide")
        return None

```
# Tests
exemples = ["42", "abc", "3.14", "-100", "999999999"]
```python
for exemple in exemples:
    resultat = convertir_en_nombre(exemple)
    print(f"convertir_en_nombre('{exemple}') → {resultat}")

## Solution Défi 2: Accès sécurisé à une liste

def obtenir_element_liste(liste, index):
    """Obtenir un élément d'une liste de façon sécurisée."""
    try:
        element = liste[index]
        return element
    except IndexError:
        print(f"Erreur d'index : {index} est en dehors de la liste (taille: {len(liste)})")
        return None
    except TypeError:
        print(f"Erreur de type : l'index doit être un entier, pas {type(index).__name__}")
        return None

```
# Tests
liste = [10, 20, 30, 40, 50]
```python
print(obtenir_element_liste(liste, 2))      # → 30
print(obtenir_element_liste(liste, 10))     # → None, message d'erreur
print(obtenir_element_liste(liste, "abc"))  # → None, message d'erreur

## Solution Défi 3: Validation d'un dictionnaire

def obtenir_donnees_utilisateur(dictionnaire, cle):
    """Obtenir une valeur d'un dictionnaire de façon sécurisée."""
    try:
        valeur = dictionnaire[cle]
        return valeur
    except KeyError:
        print(f"Erreur : la clé '{cle}' n'existe pas dans le dictionnaire")
        return None
    except TypeError:
        print(f"Erreur : le paramètre doit être un dictionnaire, pas {type(dictionnaire).__name__}")
        return None

```
# Tests
utilisateurs = {"alice": 25, "bob": 30, "charlie": 28}
```python
print(obtenir_donnees_utilisateur(utilisateurs, "alice"))    # → 25
print(obtenir_donnees_utilisateur(utilisateurs, "david"))    # → None
print(obtenir_donnees_utilisateur("pas_dict", "alice"))      # → None

## Solution Défi 4: Validation d'email avec exceptions personnalisées

class EmailInvalide(Exception):
    """Exception levée quand un email est invalide."""
    pass

def valider_email(email):
    """Valider un email avec exceptions personnalisées."""
    try:
        # Vérifier que email est une chaîne
        if not isinstance(email, str):
            raise TypeError(f"L'email doit être une chaîne, pas {type(email).__name__}")

        # Vérifier que email contient @
        if "@" not in email:
            raise EmailInvalide("L'email doit contenir un '@'")

        # Séparer les parties
        parties = email.split("@")
        if len(parties) != 2:
            raise EmailInvalide("L'email ne peut contenir qu'un seul '@'")

        avant, apres = parties

        # Vérifier les parties
        if not avant:
            raise EmailInvalide("L'email ne peut pas commencer par '@'")
        if not apres:
            raise EmailInvalide("L'email ne peut pas se terminer par '@'")

        # Vérifier que apres contient un point
        if "." not in apres:
            raise EmailInvalide("Le domaine doit contenir un '.'")

        return True

    except EmailInvalide as e:
        return (False, str(e))
    except TypeError as e:
        return (False, str(e))

```
# Tests
emails = [
```python
    "alice@example.com",
    "bob@",
    "@example.com",
    "charlie_sans_arobase.com",
    "dave@domain.co.uk"
```
]

```python
for email in emails:
    try:
        resultat = valider_email(email)
        print(f"✓ {email} : Email valide")
    except EmailInvalide as e:
        print(f"✗ {email} : Email invalide - {e}")

## Solution Défi 5: Parser JSON robuste

import json

def parser_reponse_api(json_texte):
    """Parser une réponse API JSON robuste."""
    try:
        # Étape 1 : Parser le JSON
        donnees = json.loads(json_texte)

        # Étape 2 : Valider la structure
        if "statut" not in donnees:
            raise KeyError("Clé 'statut' manquante")
        if "donnees" not in donnees:
            raise KeyError("Clé 'donnees' manquante")

        # Succès
        return {
            "succès": True,
            "contenu": donnees
        }

    except json.JSONDecodeError as e:
        print(f"Erreur de syntaxe JSON : {e}")
        return {
            "succès": False,
            "erreur": f"JSON invalide : {e}"
        }

    except KeyError as e:
        print(f"Erreur de structure : {e} - réponse incomplète")
        return {
            "succès": False,
            "erreur": f"Clé manquante : {e}"
        }

    except Exception as e:
        print(f"Erreur inattendue : {e}")
        return {
            "succès": False,
            "erreur": f"Erreur inattendue : {e}"
        }

```
# Tests
tests_json = [
```python
    '{"statut": "ok", "donnees": [1, 2, 3]}',
    '{"statut": "erreur"}',
    '{"statut": "ok", donnees: []}'
```
]

```python
for test in tests_json:
    print(f"Parsing : {test}")
    resultat = parser_reponse_api(test)
    print(f"Résultat : {resultat}\n")

## Solution Défi 6: Scanner de ports simulé

class ErreurScan(Exception):
    """Classe de base pour les erreurs de scan."""
    pass

class PortFerme(ErreurScan):
    """Le port est fermé."""
    pass

class PortTimeout(ErreurScan):
    """Timeout lors de la connexion au port."""
    pass

class PortInvalide(ErreurScan):
    """Le numéro de port est invalide."""
    pass

def scanner_port_securise(hote, port):
    """Scanner un port de façon sécurisée."""
    import random

    try:
        # Validation du port
        if not isinstance(port, int) or port < 1 or port > 65535:
            raise PortInvalide(f"Port invalide : {port} (doit être entre 1 et 65535)")

        # Simulation du scan
        rand = random.random()
        if rand < 0.3:
            raise PortFerme(f"Port {port} fermé")
        elif rand < 0.5:
            raise PortTimeout(f"Timeout sur port {port}")

        return {"port": port, "statut": "ouvert"}

    except (PortFerme, PortTimeout, PortInvalide) as e:
        raise

def scanner_multiple_ports(hote, ports):
    """Scanner plusieurs ports."""
    resultats = []
    stats = {"ouverts": 0, "fermes": 0, "timeouts": 0, "erreurs": 0}

    print(f"Scan de {hote}:")

    for port in ports:
        try:
            resultat = scanner_port_securise(hote, port)
            resultats.append(resultat)
            print(f"[{port}] ouvert")
            stats["ouverts"] += 1

        except PortFerme:
            print(f"[{port}] fermé")
            resultats.append({"port": port, "statut": "fermé"})
            stats["fermes"] += 1

        except PortTimeout:
            print(f"[{port}] timeout")
            resultats.append({"port": port, "statut": "timeout"})
            stats["timeouts"] += 1

        except PortInvalide as e:
            print(f"[{port}] erreur : {e}")
            stats["erreurs"] += 1

        except Exception as e:
            print(f"[{port}] erreur inattendue : {e}")
            stats["erreurs"] += 1

    # Afficher le résumé
    print(f"\nRésumé : {stats['ouverts']} ouvert(s), {stats['fermes']} fermé(s), "
          f"{stats['timeouts']} timeout(s), {stats['erreurs']} erreur(s)")

    return resultats

```
# Test
scanner_multiple_ports("192.168.1.1", [22, 80, 443, 8080, 3306])

## Solution Défi 7: Gestion d'authentification

```python
def authentifier_utilisateur(credentials):
    """Authentifier un utilisateur avec gestion complète d'erreurs."""

    # Simulated user database
    base_utilisateurs = {
        "alice": {"password": "pass123", "connexions": 0},
        "bob": {"password": "secret456", "connexions": 0},
        "charlie": {"password": "secure789", "connexions": 0}
    }

    try:
        # Partie TRY : Extraire et valider les données
        username = credentials["username"]  # KeyError possible
        password = credentials["password"]  # KeyError possible

        if not username or len(username) == 0:
            raise ValueError("Le username ne peut pas être vide")

        if not password or len(password) == 0:
            raise ValueError("Le password ne peut pas être vide")

        # Vérifier les credentials
        if username not in base_utilisateurs:
            raise ValueError(f"Utilisateur '{username}' introuvable")

        utilisateur = base_utilisateurs[username]
        if utilisateur["password"] != password:
            raise ValueError("Mot de passe incorrect")

    except KeyError as e:
        # Partie EXCEPT 1 : Clé manquante
        print(f"Erreur : Clé manquante - {e}")

    except ValueError as e:
        # Partie EXCEPT 2 : Donnée invalide
        print(f"Erreur : {e}")

    else:
        # Partie ELSE : Authentification réussie
        print(f"✓ Authentification réussie pour '{username}'")
        base_utilisateurs[username]["connexions"] += 1

    finally:
        # Partie FINALLY : Nettoyage toujours exécuté
        print("Fin du processus d'authentification\n")

```
# Tests
test_cases = [
```python
    {"username": "alice", "password": "pass123"},
    {"username": "alice", "password": "mauvais"},
    {"username": "david", "password": "pass123"},
    {"username": "bob"},  # Clé manquante
    {},  # Tout manquant
```
]

```python
for test in test_cases:
    print(f"Tentative : {test}")
    authentifier_utilisateur(test)

## Solution Défi 8: Système de logging d'erreurs

import time
from datetime import datetime
import random

```
# Hiérarchie d'exceptions
```python
class ErreurPentesting(Exception):
    """Classe de base pour les erreurs de pentesting."""
    pass

class ErreurReseau(ErreurPentesting):
    """Erreur réseau."""
    pass

class ErreurAuthentification(ErreurPentesting):
    """Erreur d'authentification."""
    pass

class ErreurCible(ErreurPentesting):
    """Erreur liée à la cible."""
    pass

```
# Logger d'erreurs
class LoggerErreurs:
```python
    """Logger pour tracer les erreurs."""

    def __init__(self):
        self.erreurs = []

    def enregistrer(self, type_erreur, message):
        """Enregistrer une erreur."""
        self.erreurs.append({
            "timestamp": datetime.now(),
            "type": type_erreur.__name__,
            "message": message
        })

    def rapport(self):
        """Générer un rapport d'erreurs."""
        if not self.erreurs:
            return "Aucune erreur enregistrée"

        # Compter par type
        compteurs = {}
        for erreur in self.erreurs:
            type_err = erreur["type"]
            compteurs[type_err] = compteurs.get(type_err, 0) + 1

        # Générer le rapport
        rapport = "═══ RAPPORT D'ERREURS ═══\n"
        rapport += f"Total erreurs : {len(self.erreurs)}\n"
        for type_err, count in compteurs.items():
            rapport += f"- {type_err} : {count}\n"

        return rapport

```
# Fonction d'exécution
```python
def executer_operation(nom_operation, logger):
    """Exécuter une opération avec retry."""

    max_tentatives = 3

    for tentative in range(1, max_tentatives + 1):
        try:
            # Simuler une opération qui peut échouer
            rand = random.random()

            if rand < 0.4:
                raise ErreurReseau("Connexion échouée")
            elif rand < 0.7:
                raise ErreurAuthentification("Authentification échouée")
            elif rand < 0.85:
                raise ErreurCible("Cible indisponible")

            print(f"Tentative {tentative} : Succès !")
            return True

        except ErreurPentesting as e:
            print(f"Tentative {tentative} : {type(e).__name__} - {e}")
            logger.enregistrer(type(e), str(e))

            if tentative < max_tentatives:
                print(f"  Retry en cours...\n")
            else:
                print(f"  Échec après {max_tentatives} tentatives\n")

    return False

```
# Exécution complète
```python
print("═" * 60)
print("SYSTÈME DE LOGGING D'ERREURS - PENTESTING")
print("═" * 60)
print()

```
logger = LoggerErreurs()
success = executer_operation("Scanner de vulnérabilités", logger)

```python
print(logger.rapport())

if success:
    print("Opération complétée avec succès")
else:
    print("Opération échouée après plusieurs tentatives")

```
POINTS CLÉS DES SOLUTIONS

1. DÉFI 1 : Utiliser except ValueError pour capturer la conversion échouée

2. DÉFI 2 : Capturer à la fois IndexError ET TypeError pour deux cas d'erreur

3. DÉFI 3 : Distinguer entre KeyError (clé manquante) et TypeError (mauvais type)

4. DÉFI 4 : Créer une exception personnalisée EmailInvalide qui hérite d'Exception

5. DÉFI 5 : Gérer json.JSONDecodeError, KeyError, et Exception de fallback

6. DÉFI 6 : Utiliser une hiérarchie d'exceptions pour classifier les erreurs de scan
```python
            Continuer le scan même si certains ports échouent

```
7. DÉFI 7 : Combiner try/except/else/finally dans une structure complète
```python
            else s'exécute si aucune exception
            finally s'exécute toujours

```
8. DÉFI 8 : Créer une hiérarchie d'exceptions personnalisées
```python
            Logger les erreurs dans une classe dédiée
            Implémenter un système de retry avec un nombre max de tentatives
            Générer un rapport d'erreurs

```
COMMANDES DE TEST

# Créer un fichier solution_defi1.py contenant la solution du défi 1
python solution_defi1.py

# Créer un fichier solution_defi8.py pour le système complet
python solution_defi8.py

# Exécuter et observer les résultats
# Modifier les tests pour couvrir tous les cas d'erreur

RAPPEL DES BONNES PRATIQUES

✓ Capturer les exceptions spécifiques, pas Exception générique
✓ Afficher des messages clairs et utiles pour le débogage
✓ Utiliser finally pour nettoyer les ressources
✓ Utiliser raise pour valider les paramètres
✓ Créer des exceptions personnalisées pour la sémantique du domaine
✓ Utiliser "from" pour préserver le contexte d'erreur (exception chaining)
✓ Tester à la fois les cas nominaux et les cas d'erreur
✓ En cybersécurité : robustesse > crash (ne jamais laisser un outil crash)
✓ Documenter quelles exceptions une fonction peut lever
✓ Utiliser try/except/else/finally pour une gestion complète

