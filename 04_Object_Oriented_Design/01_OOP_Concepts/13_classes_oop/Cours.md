# Exercice 13 : Classes et Programmation Orientée Objet (OOP)

## Objectifs

- Maîtriser la définition de classes avec `class`
- Comprendre le constructeur `__init__` et l'initialisation des attributs
- Utiliser `self` pour accéder aux attributs et méthodes d'instance
- Créer des méthodes d'instance et des attributs de classe
- Implémenter l'héritage entre classes
- Comprendre l'encapsulation (public, privé, protégé)
- Utiliser les méthodes spéciales `__str__`, `__repr__`, `__eq__`, `__lt__`
- Appliquer le polymorphisme
- Maîtriser les méthodes statiques et de classe
- Appliquer aux contextes de cybersécurité (scanning, exploits, payloads)

## Concepts

### Définition basique d'une classe

```python
class Animal:
    """Classe représentant un animal"""

    def __init__(self, nom, espece):
        """Constructeur - appelé automatiquement à la création"""
        self.nom = nom          # Attribut d'instance
        self.espece = espece

    def faire_bruit(self):
        """Méthode d'instance"""
        print(f"{self.nom} fait du bruit")

# Créer une instance (objet)
chien = Animal("Rex", "Chien")
chien.faire_bruit()  # Rex fait du bruit
```

### Le constructeur __init__

```python
class Personne:
    def __init__(self, nom, age):
        """
        Le constructeur est appelé lors de la création d'un objet.
        C'est ici qu'on initialise les attributs.
        """
        self.nom = nom
        self.age = age

# Créer une instance
alice = Personne("Alice", 25)
print(alice.nom)    # Alice
print(alice.age)    # 25
```

### self - Référence à l'instance

```python
class Compte:
    def __init__(self, solde):
        self.solde = solde  # self fait référence à l'instance

    def deposer(self, montant):
        """self permet d'accéder aux attributs de l'objet"""
        self.solde += montant
        return f"Nouveau solde: {self.solde}"

compte = Compte(1000)
print(compte.deposer(500))  # Nouveau solde: 1500
```

### Attributs et méthodes

```python
class Robot:
    # Attribut de classe (partagé par tous les robots)
    nombre_robots = 0

    def __init__(self, nom):
        # Attributs d'instance (uniques par robot)
        self.nom = nom
        self.energie = 100
        Robot.nombre_robots += 1

    def recharger(self):
        """Méthode d'instance"""
        self.energie = 100
        print(f"{self.nom} rechargé!")

robot1 = Robot("R2D2")
robot2 = Robot("C3PO")
print(Robot.nombre_robots)  # 2
```

### Héritage

```python
class Vehicule:
    """Classe parente"""
    def __init__(self, marque):
        self.marque = marque

    def demarrer(self):
        print(f"{self.marque} démarre")

class Voiture(Vehicule):
    """Classe enfant - hérite de Vehicule"""
    def __init__(self, marque, nb_portes):
        super().__init__(marque)  # Appelle le constructeur parent
        self.nb_portes = nb_portes

    def ouvrir_portes(self):
        print(f"Ouverture des {self.nb_portes} portes")

voiture = Voiture("Toyota", 4)
voiture.demarrer()  # Hérité de Vehicule
voiture.ouvrir_portes()  # Méthode propre à Voiture
```

### Encapsulation

```python
class BanqueSecurisee:
    def __init__(self, solde):
        self.__solde = solde  # __ = privé (name mangling)
        self._log = []        # _ = protégé (convention)

    def deposer(self, montant):
        """Méthode publique pour accéder aux données privées"""
        if montant > 0:
            self.__solde += montant
            self._log.append(f"Dépôt: {montant}")
            return True
        return False

    def get_solde(self):
        """Getter public"""
        return self.__solde

compte = BanqueSecurisee(1000)
compte.deposer(500)
print(compte.get_solde())  # 1500
```

### Méthodes spéciales (__str__, __repr__)

```python
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def __str__(self):
        """Retourne une chaîne lisible pour l'utilisateur"""
        return f"{self.nom} ({self.age} ans)"

    def __repr__(self):
        """Retourne une représentation technique"""
        return f"Personne('{self.nom}', {self.age})"

    def __eq__(self, autre):
        """Compare deux personnes"""
        return self.nom == autre.nom and self.age == autre.age

p1 = Personne("Alice", 25)
print(str(p1))   # Alice (25 ans)
print(repr(p1))  # Personne('Alice', 25)
```

### Polymorphisme

```python
class Animal:
    def faire_bruit(self):
        pass

class Chien(Animal):
    def faire_bruit(self):
        return "Woof!"

class Chat(Animal):
    def faire_bruit(self):
        return "Miaou!"

def jouer_avec_animal(animal):
    """Fonctionne avec n'importe quel animal"""
    print(animal.faire_bruit())

chien = Chien()
chat = Chat()
jouer_avec_animal(chien)  # Woof!
jouer_avec_animal(chat)   # Miaou!
```

### Méthodes statiques et de classe

```python
class Utilitaires:
    pi = 3.14159

    @staticmethod
    def ajouter(a, b):
        """Méthode statique - pas d'accès à self ou cls"""
        return a + b

    @classmethod
    def creer_depuis_string(cls, valeur):
        """Méthode de classe - accès à la classe"""
        return cls(int(valeur))

print(Utilitaires.ajouter(5, 3))  # 8 (pas besoin d'instance)
```

## Instructions

1. Lisez le fichier `main.py`
2. Exécutez : `python main.py`
3. Observez comment les classes et les objets fonctionnent
4. Modifiez le code pour expérimenter
5. Essayez les défis dans `exercice.txt`

## Durée estimée

5-6 heures

## Prérequis

- Exercice 01 : Hello Print
- Exercice 02 : Variables et Types
- Exercice 03 : Input et Output
- Exercice 04 : Opérateurs
- Exercice 05 : if/else
- Exercice 06 : Boucles
- Exercice 07 : Listes et Tuples
- Exercice 08 : Dictionnaires
- Exercice 09 : Fonctions
- Exercice 10 : Modules et Imports
- Exercice 11 : Fichiers
- Exercice 12 : Exceptions

## Concepts clés à retenir

- `class` définit une classe
- `__init__` est le constructeur appelé à la création de l'objet
- `self` fait référence à l'instance courante
- Les attributs stockent l'état de l'objet
- Les méthodes sont des fonctions attachées à la classe
- L'héritage permet de réutiliser le code d'une classe parente
- L'encapsulation protège les données avec les modificateurs _/__
- Les méthodes spéciales (__str__, __eq__) personnalisent le comportement
- Le polymorphisme permet différentes implémentations selon le type
- Les méthodes statiques (@staticmethod) ne dépendent pas de l'instance
- Les méthodes de classe (@classmethod) accèdent à la classe elle-même
- L'OOP facilite la modularité, la réutilisabilité et la maintenabilité

## Prochaine étape

Exercice 14 : Décorateurs et Métaprogrammation
