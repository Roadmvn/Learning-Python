# Exercice 12: GESTION D'EXCEPTIONS - DÉFIS PROGRESSIFS

DÉFIS PROGRESSIFS :

## Défi 1: Conversion sécurisée (Facile)

Créez une fonction `convertir_en_nombre()` qui :
- Prend une chaîne comme paramètre
- Tente de la convertir en entier
- Retourne l'entier si succès
- Retourne None si ValueError (chaîne non valide)
- Affiche un message d'erreur explicite en cas d'échec

Testez avec : "42", "abc", "3.14", "-100", "999999999"

Exemple de résultat attendu :
```python
    convertir_en_nombre("42") → 42
    convertir_en_nombre("abc") → Erreur: 'abc' n'est pas un nombre entier → None

## Défi 2: Accès sécurisé à une liste (Moyen)

```
Créez une fonction `obtenir_element_liste()` qui :
- Prend une liste et un index comme paramètres
- Retourne l'élément à cet index si valide
- Gère IndexError si l'index est en dehors
- Gère TypeError si le type d'index est invalide
- Affiche un message d'erreur spécifique pour chaque cas
- Retourne None en cas d'erreur

Testez avec :
```python
    liste = [10, 20, 30, 40, 50]
    obtenir_element_liste(liste, 2) → 30
    obtenir_element_liste(liste, 10) → Erreur d'index → None
    obtenir_element_liste(liste, "abc") → Erreur de type → None

## Défi 3: Validation d'un dictionnaire (Moyen)

```
Créez une fonction `obtenir_donnees_utilisateur()` qui :
- Prend un dictionnaire et une clé comme paramètres
- Retourne la valeur si la clé existe
- Gère KeyError si la clé manque
- Gère TypeError si le dictionnaire n'est pas du bon type
- Affiche un message personnalisé
- Retourne une valeur par défaut si erreur

Testez avec :
```python
    utilisateurs = {"alice": 25, "bob": 30, "charlie": 28}
    obtenir_donnees_utilisateur(utilisateurs, "alice") → 25
    obtenir_donnees_utilisateur(utilisateurs, "david") → Clé manquante → None
    obtenir_donnees_utilisateur("pas_un_dictionnaire", "alice") → Erreur type → None

## Défi 4: Validation d'email avec exceptions personnalisées (Moyen-Difficile)

```
Créez :
1. Une exception personnalisée `EmailInvalide` avec un message descriptif
2. Une fonction `valider_email()` qui :
   - Vérifie que l'email contient "@"
   - Vérifie qu'il y a du texte avant et après "@"
   - Lève EmailInvalide si validation échoue
   - Retourne True si valide

Testez avec :
```python
    "alice@example.com" → Valide ✓
    "bob@" → Invalide ✗
    "@example.com" → Invalide ✗
    "charlie_sans_arobase.com" → Invalide ✗
    "dave@domain.co.uk" → Valide ✓

```
Affichage attendu :
```python
    alice@example.com : ✓ Email valide
    bob@ : ✗ Email invalide : partie après @ manquante
    ...

## Défi 5: Parser JSON robuste avec gestion d'erreurs (Difficile)

```
Créez une fonction `parser_reponse_api()` qui :
- Prend une chaîne JSON comme paramètre
- Utilise json.loads() pour parser
- Gère json.JSONDecodeError si syntaxe invalide
- Extrait les clés "statut" et "donnees" obligatoires
- Gère KeyError si clés manquantes
- Retourne un dictionnaire {"succès": True/False, "contenu": ...}
- Affiche des messages d'erreur contextuels

Testez avec :
```python
    '{"statut": "ok", "donnees": [1, 2, 3]}' → Succès
    '{"statut": "erreur"}'  → Clé manquante → Erreur
    '{"statut": "ok", donnees: []}' → Syntaxe JSON invalide → Erreur

## Défi 6: Scanner de ports simulé avec retry (Difficile)

```
Créez un système de scan de port robuste avec :

1. Exceptions personnalisées :
   - `ErreurScan` (classe de base)
   - `PortFerme` (hérite de ErreurScan)
   - `PortTimeout` (hérite de ErreurScan)
   - `PortInvalide` (hérite de ErreurScan)

2. Fonction `scanner_port_securise()` qui :
   - Valide que le port est entre 1 et 65535 (lève PortInvalide sinon)
   - Lève PortFerme si la tentative de connexion échoue
   - Lève PortTimeout si timeout
   - Retourne {"port": port, "statut": "ouvert"} si succès

3. Fonction `scanner_multiple_ports()` qui :
   - Scanne une liste de ports
   - Continue même si certains ports échouent
   - Retourne une liste de résultats
   - Affiche un résumé (ports ouverts, fermés, timeouts)

Affichage attendu :
```python
    Scan de 192.168.1.1:
    [22] ouvert
    [80] fermé
    [443] timeout
    [8080] erreur

    Résumé : 1 ouvert, 2 fermés, 1 timeout

## Défi 7: Gestion d'authentification avec try/except/else/finally (Difficile)

```
Créez une fonction `authentifier_utilisateur()` qui :

PARTIE TRY :
- Reçoit un dictionnaire contenant "username" et "password"
- Valide que les deux clés existent (KeyError possible)
- Vérifie que username n'est pas vide (ValueError possible)
- Cherche l'utilisateur dans une base de données simulée

PARTIE EXCEPT :
- Gère KeyError si clés manquantes
- Gère ValueError si données invalides
- Affiche messages d'erreur spécifiques

PARTIE ELSE :
- S'exécute si authentification réussit
- Affiche "Authentification réussie pour <username>"
- Incrémente un compteur de connexions

PARTIE FINALLY :
- S'exécute toujours
- Affiche "Fin du processus d'authentification"
- Nettoie les données sensibles

Testez avec plusieurs utilisateurs et cas d'erreur.

## Défi 8: Système de logging d'erreurs avec exception chaining (Très Difficile)

Créez un système complet de gestion d'erreurs pour un "outils de pentesting" :

1. Créez une hiérarchie d'exceptions :
   - `ErreurPentesting` (classe de base)
   - `ErreurReseau` (hérite de ErreurPentesting)
   - `ErreurAuthentification` (hérite de ErreurPentesting)
   - `ErreurCible` (hérite de ErreurPentesting)

2. Créez une classe `LoggerErreurs` qui :
   - Stocke les erreurs dans une liste avec timestamp
   - Peut générer un rapport d'erreurs
   - Affiche les statistiques (nombre d'erreurs par type)

3. Créez une fonction `executer_operation()` qui :
   - Exécute une opération de pentesting
   - Lève des exceptions appropriées selon le scénario
   - Capture avec try/except
   - Utilise le logger pour enregistrer
   - Gère les erreurs avec retry (max 3 tentatives)
   - Affiche un rapport final

Affichage attendu :
```python
    Tentative 1 : ErreurReseau - Connexion échouée
    Tentative 2 : ErreurReseau - Connexion échouée
    Tentative 3 : Succès !

    ═══ RAPPORT D'ERREURS ═══
    Total erreurs : 2
    - ErreurReseau : 2

    Opération complétée (réussie après 3 tentatives)

## Conseils POUR TOUS LES DÉFIS

```
1. SPÉCIFICITÉ : Toujours capturer les exceptions spécifiques, pas générique Exception
2. MESSAGES : Afficher des messages clairs et utiles pour le débogage
3. NETTOYAGE : Utiliser finally pour nettoyer les ressources
4. VALIDATIONS : Utiliser raise pour valider les paramètres
5. PERSONNALISÉES : Créer des exceptions adaptées au domaine (réseau, auth, etc.)
6. CHAINING : Utiliser "from" pour préserver le contexte d'erreur
7. TESTS : Tester les cas nominaux ET les cas d'erreur

EXEMPLE DE STRUCTURE :

```python
def fonction():
    try:
        # Valider les entrées
        # Exécuter la logique
    except TypeErreur1 as e:
        # Gestion spécifique
    except (TypeErreur2, TypeErreur3) as e:
        # Gestion pour plusieurs types
    except Exception as e:
        # Fallback (rare)
    else:
        # Code si succès
    finally:
        # Nettoyage

    return resultat

```