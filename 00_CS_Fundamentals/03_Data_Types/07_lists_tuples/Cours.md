# Exercice 07 : Listes et Tuples

## Objectifs

- Maîtriser les listes (type mutable)
- Maîtriser les tuples (type immutable)
- Comprendre l'indexing et le slicing
- Utiliser les méthodes de liste (append, extend, remove, pop, sort, etc.)
- Maîtriser la list comprehension
- Appliquer aux contextes de cybersécurité/red teaming

## Concepts

### Listes : collections mutables

```python
# Création de listes
ips = ["192.168.1.1", "10.0.0.5", "172.16.0.1"]
ports = [22, 80, 443, 3306]
mixed = [1, "texte", 3.14, True]
empty = []

# Accès par index (commence à 0)
premier = ips[0]  # "192.168.1.1"
dernier = ips[-1]  # "172.16.0.1"

# Modification
ips[0] = "192.168.1.100"
```

### Tuples : collections immutables

```python
# Création de tuples
credentials = ("admin", "password123")
point = (x, y, z)
singleton = (42,)  # Important : virgule pour tuple d'1 élément
empty = ()

# Accès par index (comme les listes)
username = credentials[0]  # "admin"

# Pas de modification possible
# credentials[0] = "root"  # ERREUR !
```

### Indexing

```python
liste = ["a", "b", "c", "d", "e"]
#          0    1    2    3    4    (indices positifs)
#         -5   -4   -3   -2   -1    (indices négatifs)

premier = liste[0]   # "a"
dernier = liste[-1]  # "e"
second_dernier = liste[-2]  # "d"
```

### Slicing (découpage)

```python
liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

slice1 = liste[0:5]      # [0, 1, 2, 3, 4] (jusqu'à 5, non inclus)
slice2 = liste[2:7]      # [2, 3, 4, 5, 6]
slice3 = liste[::2]      # [0, 2, 4, 6, 8] (tous les 2)
slice4 = liste[::-1]     # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (inversé)
slice5 = liste[1:8:2]    # [1, 3, 5, 7] (du 1 au 8, tous les 2)
```

### Méthodes de liste

```python
# append(x) : ajoute x à la fin
liste = [1, 2, 3]
liste.append(4)  # [1, 2, 3, 4]

# extend(iterable) : ajoute tous les éléments d'iterable
liste.extend([5, 6])  # [1, 2, 3, 4, 5, 6]

# insert(index, x) : insère x à la position index
liste.insert(0, 0)  # [0, 1, 2, 3, 4, 5, 6]

# remove(x) : supprime le premier x trouvé
liste.remove(3)  # [0, 1, 2, 4, 5, 6]

# pop(index) : supprime et retourne l'élément à index (-1 par défaut)
element = liste.pop()  # 6 (suppression du dernier)
element = liste.pop(0)  # 0 (suppression du premier)

# sort() : trie sur place
nombres = [3, 1, 4, 1, 5, 9]
nombres.sort()  # [1, 1, 3, 4, 5, 9]

# reverse() : inverse l'ordre
nombres.reverse()  # [9, 5, 4, 3, 1, 1]

# index(x) : retourne l'index du premier x
index = nombres.index(3)

# count(x) : compte les occurrences de x
count = nombres.count(1)  # 2

# copy() : crée une copie
copie = nombres.copy()
```

### List Comprehension

```python
# Syntaxe : [expression for item in iterable if condition]

# Créer une liste de carrés
carrés = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# Avec condition
pairs = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# Transformation
mots = ["hello", "world"]
majuscules = [m.upper() for m in mots]  # ["HELLO", "WORLD"]

# Imbriquée
matrice = [[i*j for j in range(3)] for i in range(3)]
```

## Instructions

1. Lisez le fichier `main.py`
2. Exécutez : `python main.py`
3. Observez la manipulation de listes et tuples
4. Comprenez indexing, slicing, et les méthodes
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

## Concepts clés à retenir

- Les listes sont mutables (modifiables)
- Les tuples sont immutables (non modifiables)
- L'indexing commence à 0 (et va de -1 en arrière)
- Le slicing utilise [start:stop:step]
- append() ajoute un élément ; extend() ajoute plusieurs
- remove() supprime une valeur ; pop() supprime un index
- list comprehension est une syntaxe compacte pour créer des listes
- Les listes peuvent contenir n'importe quel type d'objet

## Prochaine étape

Exercice 08 : Dictionnaires
