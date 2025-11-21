# Exercice 03 : Input et Output

## Objectifs

- Utiliser la fonction input() pour recevoir des données utilisateur
- Convertir les inputs en types appropriés
- Créer des programmes interactifs
- Maîtriser le formatage avancé avec f-strings
- Gérer les entrées utilisateur

## Concepts

### La fonction input()

```python
nom = input("Entrez votre nom : ")
# L'utilisateur tape son nom
# La valeur est stockée dans la variable nom
```

**Important :** input() retourne TOUJOURS une chaîne de caractères (str), même si l'utilisateur tape un nombre.

### Conversion des inputs

```python
age_str = input("Votre âge : ")
age = int(age_str)  # Conversion str → int
```

### Formatage avancé

```python
# f-strings avec formatage
nombre = 3.14159
print(f"{nombre:.2f}")  # 2 décimales : 3.14
```

## Instructions

1. Lisez le fichier `main.py`
2. Exécutez : `python main.py`
3. Interagissez avec le programme
4. Modifiez le code pour vos propres questions
5. Essayez les défis dans `exercice.txt`

## Durée estimée

2-3 heures

## Prérequis

- Exercice 01 : Hello Print
- Exercice 02 : Variables et Types

## Concepts clés à retenir

- input() retourne toujours une chaîne (str)
- Utilisez int(), float() pour convertir les inputs numériques
- f-strings permettent un formatage puissant
- Les programmes interactifs sont plus engageants

## Prochaine étape

Exercice 04 : Opérateurs
