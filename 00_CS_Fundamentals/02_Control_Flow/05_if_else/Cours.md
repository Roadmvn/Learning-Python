# Exercice 05 : Structures Conditionnelles (if/else)

## Objectifs

- Maîtriser les structures conditionnelles (if, elif, else)
- Créer des conditions multiples
- Utiliser l'opérateur ternaire
- Découvrir match/case (Python 3.10+)
- Créer des programmes avec logique de décision

## Concepts

### Structure if basique

```python
if condition:
    # Code exécuté si condition est True
    print("Condition vraie")
```

### Structure if/else

```python
if condition:
    # Code si True
    print("Vrai")
else:
    # Code si False
    print("Faux")
```

### Structure if/elif/else

```python
if condition1:
    # Code si condition1 est True
elif condition2:
    # Code si condition2 est True
else:
    # Code si toutes les conditions sont False
```

### Opérateur ternaire

```python
resultat = "Vrai" if condition else "Faux"
```

### match/case (Python 3.10+)

```python
match valeur:
    case 1:
        print("Un")
    case 2:
        print("Deux")
    case _:
        print("Autre")
```

## Instructions

1. Lisez le fichier `main.py`
2. Exécutez : `python main.py`
3. Observez la logique conditionnelle
4. Modifiez les conditions pour expérimenter
5. Essayez les défis dans `exercice.txt`

## Durée estimée

3-4 heures

## Prérequis

- Exercice 01 : Hello Print
- Exercice 02 : Variables et Types
- Exercice 03 : Input et Output
- Exercice 04 : Opérateurs

## Concepts clés à retenir

- if teste une condition
- elif permet plusieurs conditions (else if)
- else attrape tous les autres cas
- L'indentation est cruciale
- Opérateur ternaire pour conditions simples
- match/case pour de nombreux cas spécifiques

## Prochaine étape

Exercice 06 : Boucles (for et while)
