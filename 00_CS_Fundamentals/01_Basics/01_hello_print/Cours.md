# Exercice 01 : Hello Print

## Objectifs

- Écrire votre premier programme Python
- Comprendre la fonction `print()`
- Utiliser les commentaires
- Comprendre l'indentation en Python
- Exécuter un script Python

## Concepts

### La fonction print()

`print()` est une fonction qui affiche du texte dans le terminal.

```python
print("Hello, World!")
```

### Les commentaires

Les commentaires permettent d'expliquer le code sans l'exécuter.

```python
# Ceci est un commentaire sur une ligne

"""
Ceci est un commentaire
sur plusieurs lignes
"""
```

### L'indentation

Python utilise l'indentation (espaces ou tabulations) pour structurer le code.
Contrairement à d'autres langages qui utilisent des accolades `{}`, Python utilise l'indentation pour définir les blocs de code.

```python
# Indentation correcte
if True:
    print("Ceci est indenté")
    print("Ceci aussi")

# Indentation incorrecte (erreur)
if True:
print("Erreur!")  # IndentationError
```

### Exécution d'un script

Pour exécuter un script Python :

```bash
python main.py
# ou
python3 main.py
```

## Instructions

1. Lisez le fichier `main.py` attentivement
2. Exécutez le script : `python main.py`
3. Observez la sortie dans le terminal
4. Modifiez le code pour afficher votre propre message
5. Essayez les exercices dans `exercice.txt`

## Durée estimée

1-2 heures

## Prérequis

Aucun - C'est le premier exercice !

## Concepts clés à retenir

- `print()` affiche du texte dans le terminal
- Les commentaires commencent par `#`
- L'indentation est importante en Python
- Les chaînes de caractères sont entourées de guillemets `"` ou `'`

## Prochaine étape

Une fois cet exercice maîtrisé, passez à l'exercice 02 : Variables et Types.
