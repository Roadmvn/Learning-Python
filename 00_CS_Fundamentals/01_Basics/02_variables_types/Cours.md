# Exercice 02 : Variables et Types

## Objectifs

- Comprendre les variables en Python
- Maîtriser les types de données de base
- Effectuer des conversions de types
- Utiliser la fonction type()
- Apprendre les conventions de nommage

## Concepts

### Variables

Une variable est un conteneur pour stocker des données.

```python
nom = "Alice"
age = 25
```

### Types de données de base

- **int** : Nombres entiers (ex: 42, -10)
- **float** : Nombres décimaux (ex: 3.14, -0.5)
- **str** : Chaînes de caractères (ex: "Hello")
- **bool** : Booléens (True ou False)

### Conversion de types (Casting)

```python
nombre = int("42")      # Chaîne → Entier
decimal = float("3.14") # Chaîne → Float
texte = str(100)        # Entier → Chaîne
```

### Conventions de nommage

- Utilisez des noms descriptifs : `age_utilisateur` plutôt que `a`
- snake_case pour les variables : `nom_complet`
- Évitez les mots réservés : `class`, `for`, `if`
- Les variables sont sensibles à la casse : `Age` ≠ `age`

## Instructions

1. Lisez le fichier `main.py`
2. Exécutez : `python main.py`
3. Observez les différents types de données
4. Expérimentez avec vos propres variables
5. Essayez les défis dans `exercice.txt`

## Durée estimée

2-3 heures

## Prérequis

Exercice 01 : Hello Print

## Concepts clés à retenir

- Les variables stockent des données
- Python a un typage dynamique (pas besoin de déclarer le type)
- Les types principaux : int, float, str, bool
- Utilisez type() pour connaître le type d'une variable
- Les conversions de types sont fréquentes

## Prochaine étape

Exercice 03 : Input et Output
