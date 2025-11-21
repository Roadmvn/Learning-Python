# Exercice 12 : Gestion d'Exceptions

## Objectifs

- Comprendre le mécanisme des exceptions en Python
- Utiliser `try`, `except`, `else`, `finally`
- Gérer les types d'exceptions spécifiques (ValueError, KeyError, IOError, IndexError, TypeError, AttributeError)
- Lever des exceptions avec `raise`
- Créer des exceptions personnalisées
- Implémenter des stratégies robustes de gestion d'erreurs
- Appliquer les exceptions aux contextes de cybersécurité et red teaming

## Concepts

### Bloc try/except basique

```python
try:
    # Code qui peut générer une exception
    numero = int("abc")
except ValueError:
    # Traitement si ValueError est levée
    print("Erreur : valeur non valide")
```

### Bloc try/except/finally

```python
try:
    fichier = open("donnees.txt", "r")
    contenu = fichier.read()
except FileNotFoundError:
    print("Fichier non trouvé")
finally:
    # S'exécute TOUJOURS, même en cas d'exception
    if 'fichier' in locals():
        fichier.close()
```

### Bloc try/except/else

```python
try:
    numero = int(input("Entrez un nombre : "))
except ValueError:
    print("Ce n'est pas un nombre")
else:
    # S'exécute SEULEMENT si aucune exception
    print(f"Vous avez entré : {numero}")
```

### Bloc try/except/else/finally

```python
try:
    donnees = {"cle": "valeur"}
    resultat = donnees["cle"]
except KeyError as e:
    print(f"Clé manquante : {e}")
else:
    print(f"Succès : {resultat}")
finally:
    print("Nettoyage des ressources")
```

### Capture d'une exception spécifique

```python
try:
    liste = [1, 2, 3]
    element = liste[10]
except IndexError as e:
    print(f"Index invalide : {e}")
```

### Capture d'exceptions multiples

```python
try:
    numero = int(input("Nombre : "))
    division = 10 / numero
except (ValueError, ZeroDivisionError) as e:
    print(f"Erreur : {e}")
```

### Exceptions multiples avec handlers différents

```python
try:
    operation()
except ValueError:
    print("Erreur de valeur")
except TypeError:
    print("Erreur de type")
except IOError:
    print("Erreur d'entrée/sortie")
except Exception as e:
    print(f"Erreur inatttendue : {e}")
```

### Lever une exception avec `raise`

```python
def diviser(a, b):
    if b == 0:
        raise ValueError("Impossible de diviser par zéro")
    return a / b
```

### Exceptions personnalisées

```python
class UtilisateurInvalide(Exception):
    """Exception levée quand un utilisateur est invalide."""
    pass

def valider_utilisateur(nom):
    if not nom or len(nom) < 3:
        raise UtilisateurInvalide("Le nom doit avoir au moins 3 caractères")
    return f"Utilisateur valide : {nom}"
```

### Réélever une exception

```python
try:
    operation()
except ValueError as e:
    print(f"Erreur captée : {e}")
    raise  # Relève la même exception
```

### Chaîner des exceptions

```python
try:
    fichier = open("absent.txt")
except FileNotFoundError as e:
    raise IOError("Impossible de lire le fichier") from e
```

## Types d'exceptions standards

### Exception commune
```python
try:
    # code
except Exception:
    # Capture TOUTE exception (à éviter généralement)
```

### ValueError
```python
try:
    numero = int("pas_un_nombre")
except ValueError:
    print("La valeur fournie n'est pas valide")
```

### KeyError
```python
try:
    utilisateurs = {"alice": "123"}
    passwd = utilisateurs["bob"]
except KeyError:
    print("Clé non trouvée dans le dictionnaire")
```

### IndexError
```python
try:
    liste = [1, 2, 3]
    element = liste[100]
except IndexError:
    print("Index en dehors de la liste")
```

### TypeError
```python
try:
    resultat = "texte" + 42
except TypeError:
    print("Opération non compatible avec les types")
```

### FileNotFoundError / IOError
```python
try:
    with open("fichier_absent.txt") as f:
        contenu = f.read()
except FileNotFoundError:
    print("Fichier non trouvé")
except IOError as e:
    print(f"Erreur d'entrée/sortie : {e}")
```

### AttributeError
```python
try:
    objet = object()
    objet.attribut_inexistant
except AttributeError:
    print("L'attribut n'existe pas sur cet objet")
```

### ZeroDivisionError
```python
try:
    resultat = 10 / 0
except ZeroDivisionError:
    print("Division par zéro impossible")
```

## Contexte Cybersécurité et Red Teaming

La gestion robuste des exceptions est critique en cybersécurité car :

- **Prévention de crash** : Un outil qui crash révèle sa présence
- **Gestion de timeouts** : Reconnexion lors de pertes réseau
- **Parsing sécurisé** : Validation avant traitement de données
- **Gestion d'erreurs de scan** : Continuer le scan même si certaines cibles échouent
- **Logging d'erreurs** : Enregistrer les anomalies pour analyse
- **Exceptions personnalisées** : Classifier les types d'erreurs (erreur d'authentification, cible indisponible, etc.)

Exemple d'un scanner de ports avec gestion robuste :
```python
def scanner_securise(hote, ports):
    resultats = []
    for port in ports:
        try:
            # Tentative de connexion
            connexion = connecter(hote, port, timeout=3)
            resultats.append((port, "ouvert"))
        except ConnectionRefusedError:
            resultats.append((port, "fermé"))
        except socket.timeout:
            resultats.append((port, "timeout"))
        except Exception as e:
            resultats.append((port, "erreur"))
            logging.error(f"Erreur sur {hote}:{port}: {e}")
    return resultats
```

## Instructions

1. Lisez le fichier `main.py`
2. Exécutez : `python main.py`
3. Observez la gestion des exceptions
4. Créez vos propres exceptions personnalisées
5. Essayez les défis dans `exercice.txt`

## Durée estimée

4-5 heures

## Prérequis

- Exercice 01 : Hello Print
- Exercice 02 : Variables et Types
- Exercice 03 : Input et Output
- Exercice 04 : Opérateurs
- Exercice 05 : Structures Conditionnelles
- Exercice 06 : Boucles
- Exercice 07 : Listes et Tuples
- Exercice 08 : Dictionnaires
- Exercice 09 : Fonctions
- Exercice 10 : Modules et Imports
- Exercice 11 : Gestion des Fichiers

## Concepts clés à retenir

- `try/except` capture les exceptions levées
- `finally` s'exécute toujours, même en cas d'erreur
- `else` s'exécute seulement si aucune exception
- `raise` lève volontairement une exception
- Les exceptions personnalisées organisent la gestion d'erreurs
- Spécifier l'exception capturée plutôt que `Exception`
- Utiliser les exceptions personnalisées pour la sémantique métier
- La robustesse est essentielle en cybersécurité

## Prochaine étape

Exercice 13 : Programmation Orientée Objet et Classes
