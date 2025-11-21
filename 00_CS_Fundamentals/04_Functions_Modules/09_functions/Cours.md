# Exercice 09 : Fonctions (Functions)

## Objectifs

- Maîtriser la définition de fonctions avec `def`
- Comprendre les paramètres et les arguments
- Utiliser `return` pour retourner des valeurs
- Exploiter les arguments par défaut
- Manier `*args` pour un nombre variable de paramètres
- Manier `**kwargs` pour les arguments nommés variables
- Utiliser les fonctions lambda
- Comprendre la portée des variables (scope local/global)
- Écrire et utiliser les docstrings
- Appliquer aux contextes de cybersécurité (scanning, encoding, vulnerabilities)

## Concepts

### Définition de fonction basique

```python
def ma_fonction():
    """Description de la fonction"""
    print("Exécution de la fonction")

ma_fonction()  # Appel
```

### Paramètres et arguments

```python
def saluer(nom, age):
    print(f"Bonjour {nom}, vous avez {age} ans")

saluer("Alice", 25)  # Appel avec arguments positionnels
saluer(age=30, nom="Bob")  # Appel avec arguments nommés
```

### Valeur de retour

```python
def additionner(a, b):
    return a + b

resultat = additionner(5, 3)
print(resultat)  # 8
```

### Arguments par défaut

```python
def greet(nom, salutation="Bonjour"):
    return f"{salutation}, {nom}"

print(greet("Alice"))  # "Bonjour, Alice"
print(greet("Bob", "Salut"))  # "Salut, Bob"
```

### *args (nombre variable de paramètres positionnels)

```python
def somme(*nombres):
    """Additionne un nombre variable d'arguments"""
    total = 0
    for n in nombres:
        total += n
    return total

print(somme(1, 2, 3))  # 6
print(somme(1, 2, 3, 4, 5))  # 15
```

### **kwargs (arguments nommés variables)

```python
def afficher_config(**options):
    """Affiche la configuration selon les options fournies"""
    for cle, valeur in options.items():
        print(f"{cle}: {valeur}")

afficher_config(host="localhost", port=8080, ssl=True)
# host: localhost
# port: 8080
# ssl: True
```

### Fonctions lambda

```python
# Lambda simple
carre = lambda x: x ** 2
print(carre(5))  # 25

# Avec map
nombres = [1, 2, 3, 4, 5]
carres = list(map(lambda x: x ** 2, nombres))
print(carres)  # [1, 4, 9, 16, 25]

# Avec filter
pairs = list(filter(lambda x: x % 2 == 0, nombres))
print(pairs)  # [2, 4]
```

### Portée des variables (Scope)

```python
variable_globale = 100

def ma_fonction():
    variable_locale = 50
    print(variable_globale)  # Accès à la variable globale (100)
    print(variable_locale)  # Accès à la variable locale (50)

print(variable_globale)  # 100
# print(variable_locale)  # Erreur : variable_locale n'existe pas ici

# Modifier une variable globale
compteur = 0

def incrementer():
    global compteur
    compteur += 1

incrementer()
print(compteur)  # 1
```

### Docstrings

```python
def scan_port(host, port):
    """
    Simule un scan de port.

    Arguments:
        host (str): Adresse IP ou domaine
        port (int): Numéro de port

    Retour:
        bool: True si port ouvert, False sinon
    """
    # Code...
    return True
```

## Instructions

1. Lisez le fichier `main.py`
2. Exécutez : `python main.py`
3. Observez comment les fonctions et les paramètres fonctionnent
4. Modifiez le code pour expérimenter
5. Essayez les défis dans `exercice.txt`

## Durée estimée

4-5 heures

## Prérequis

- Exercice 01 : Hello Print
- Exercice 02 : Variables et Types
- Exercice 03 : Input et Output
- Exercice 04 : Opérateurs
- Exercice 05 : if/else
- Exercice 06 : Boucles
- Exercice 07 : Listes et Tuples
- Exercice 08 : Dictionnaires

## Concepts clés à retenir

- `def` définit une fonction
- Les paramètres sont déclarés dans les parenthèses
- `return` retourne une valeur
- Les arguments par défaut simplifient les appels
- `*args` accepte un nombre variable d'arguments
- `**kwargs` accepte des arguments nommés variables
- Les lambdas sont des fonctions anonymes
- Scope local vs global : important pour éviter les erreurs
- Les docstrings documentent les fonctions
- Les fonctions cybersécurité doivent être bien paramétrées

## Prochaine étape

Exercice 10 : Modules et Imports
