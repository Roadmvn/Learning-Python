# Exercice 06 : Boucles (for et while)

## Objectifs

- Maîtriser les boucles for (itération sur séquences)
- Maîtriser les boucles while (itération conditionnelle)
- Comprendre range() pour générer des séquences numériques
- Utiliser break et continue pour contrôler les boucles
- Créer des boucles imbriquées
- Appliquer aux contextes de cybersécurité (scan de ports, bruteforce, énumération)

## Concepts

### Boucle for - Itération sur une séquence

```python
# Syntaxe basique
for variable in sequence:
    # Code exécuté pour chaque élément
    print(variable)

# Exemple
for fruit in ["pomme", "banane", "orange"]:
    print(fruit)
```

### range() - Générer des séquences numériques

```python
# range(stop) : 0 à stop-1
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

# range(start, stop) : start à stop-1
for i in range(1, 6):  # 1, 2, 3, 4, 5
    print(i)

# range(start, stop, step) : start à stop-1, par pas de step
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)
```

### Boucle while - Itération conditionnelle

```python
# Exécute tant que condition est True
while condition:
    # Code exécuté tant que condition est True
    # IMPORTANT : modifier la condition pour éviter boucle infinie
    counter += 1

# Exemple
count = 0
while count < 5:
    print(count)
    count += 1  # Modification cruciale
```

### break - Arrêter une boucle

```python
for i in range(10):
    if i == 5:
        break  # Arrête la boucle immédiatement
    print(i)  # Affiche 0, 1, 2, 3, 4
```

### continue - Sauter une itération

```python
for i in range(5):
    if i == 2:
        continue  # Saute cette itération
    print(i)  # Affiche 0, 1, 3, 4
```

### Boucles imbriquées

```python
# Une boucle dans une boucle
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")  # Affiche 9 combinaisons
```

### enumerate() - Accéder à l'index et la valeur

```python
fruits = ["pomme", "banane", "orange"]
for index, fruit in enumerate(fruits):
    print(f"Index {index} : {fruit}")
```

### zip() - Combiner deux séquences

```python
noms = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for nom, age in zip(noms, ages):
    print(f"{nom} : {age} ans")
```

## Instructions

1. Lisez le fichier `main.py`
2. Exécutez : `python main.py`
3. Observez les différents types de boucles
4. Modifiez les valeurs pour expérimenter
5. Essayez les défis dans `exercice.txt`

## Durée estimée

4-5 heures

## Prérequis

- Exercice 01 : Hello Print
- Exercice 02 : Variables et Types
- Exercice 03 : Input et Output
- Exercice 04 : Opérateurs
- Exercice 05 : Structures Conditionnelles

## Concepts clés à retenir

- for itère sur une séquence (liste, string, range, etc.)
- while itère tant qu'une condition est True
- range() génère des nombres : range(start, stop, step)
- break arrête la boucle
- continue saute à l'itération suivante
- Les boucles imbriquées permettent les combinaisons
- enumerate() donne accès à l'index et la valeur
- zip() combine plusieurs séquences
- Les boucles sont cruciales en cybersécurité (énumération, bruteforce, scan)

## Prochaine étape

Exercice 07 : Listes et Tuples
