# Exercice 08 : Dictionnaires (Dictionaries)

## Objectifs

- Maîtriser la création et l'accès aux dictionnaires
- Comprendre les paires clé-valeur
- Modifier et mettre à jour les dictionnaires
- Utiliser les méthodes principales (keys, values, items, get, update)
- Implémenter la compréhension de dictionnaire (dict comprehension)
- Travailler avec les dictionnaires imbriqués
- Appliquer aux contextes de cybersécurité et red teaming

## Concepts

### Création et accès aux dictionnaires

```python
# Création simple
personne = {"nom": "Alice", "age": 30}

# Accès par clé
print(personne["nom"])  # "Alice"

# Accès sécurisé avec get()
print(personne.get("email"))  # None (clé inexistante)
print(personne.get("email", "non disponible"))  # "non disponible"
```

### Paires clé-valeur

```python
# Les clés doivent être immuables (str, int, tuple)
# Les valeurs peuvent être n'importe quel type

config = {
    "port": 8080,
    "debug": True,
    "tags": ["prod", "secure"],
    "settings": {"timeout": 30}
}
```

### Modification et mise à jour

```python
# Ajouter/modifier une clé
dictionnaire["nouvelle_cle"] = "valeur"

# Utiliser update() pour fusionner
dictionnaire.update({"cle1": "val1", "cle2": "val2"})

# Supprimer une clé
del dictionnaire["cle"]
dictionnaire.pop("cle")
```

### Méthodes principales

```python
# keys() : récupère toutes les clés
for cle in dictionnaire.keys():
    print(cle)

# values() : récupère toutes les valeurs
for valeur in dictionnaire.values():
    print(valeur)

# items() : récupère les paires clé-valeur
for cle, valeur in dictionnaire.items():
    print(f"{cle}: {valeur}")

# get() : accès sécurisé
valeur = dictionnaire.get("cle", "défaut")
```

### Dict comprehension

```python
# Créer un dictionnaire par compréhension
carres = {x: x**2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Avec condition
pairs = {x: x**2 for x in range(1, 11) if x % 2 == 0}
# {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# Transformer un dictionnaire existant
original = {"a": 1, "b": 2}
double = {k: v*2 for k, v in original.items()}
# {'a': 2, 'b': 4}
```

### Dictionnaires imbriqués

```python
# Dictionnaires contenant d'autres dictionnaires
utilisateurs = {
    "user1": {"nom": "Alice", "age": 30, "email": "alice@example.com"},
    "user2": {"nom": "Bob", "age": 25, "email": "bob@example.com"}
}

# Accès aux données imbriquées
print(utilisateurs["user1"]["nom"])  # "Alice"
print(utilisateurs["user1"]["email"])  # "alice@example.com"
```

## Instructions

1. Lisez le fichier `main.py`
2. Exécutez : `python main.py`
3. Observez la gestion des dictionnaires
4. Modifiez les exemples pour expérimenter
5. Essayez les défis dans `exercice.txt`

## Durée estimée

3-4 heures

## Prérequis

- Exercice 01 : Hello Print
- Exercice 02 : Variables et Types
- Exercice 03 : Input et Output
- Exercice 04 : Opérateurs
- Exercice 05 : Structures Conditionnelles
- Exercice 06 : Boucles
- Exercice 07 : Listes et Tuples

## Concepts clés à retenir

- Les dictionnaires stockent des paires clé-valeur
- Les clés doivent être immuables
- Utilisez get() pour un accès sécurisé
- Les méthodes keys(), values(), items() sont essentielles
- Dict comprehension pour créer des dictionnaires efficacement
- Les dictionnaires imbriqués permettent des structures complexes
- Les dictionnaires sont mutables et modifiables après création

## Prochaine étape

Exercice 09 : Fonctions (def, paramètres, retours)
