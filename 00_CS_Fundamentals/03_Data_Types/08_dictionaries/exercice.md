# Exercice 08: Dictionnaires - Défis

## Défi 1: Créateur de profil utilisateur

Créez un programme qui :
1. Crée un dictionnaire représentant un profil utilisateur
2. Doit contenir au minimum : nom, email, age, username
3. Affiche le profil complet
4. Ajoute une clé "actif" avec la valeur True
5. Modifie l'âge de l'utilisateur
6. Affiche le profil mis à jour

Exemple de sortie :
Profil initial :
{'nom': 'Alice', 'email': 'alice@example.com', 'age': 30, 'username': 'alice_dev'}

Profil mis à jour :
{'nom': 'Alice', 'email': 'alice@example.com', 'age': 31, 'username': 'alice_dev', 'actif': True}

## Défi 2: Gestionnaire d'inventaire simple

Créez un programme qui :
1. Définit un dictionnaire d'articles et leurs quantités :
   {"laptop": 5, "souris": 20, "clavier": 15, "moniteur": 8}
2. Affiche le nombre total d'articles
3. Utilise get() pour afficher la quantité d'un article (sinon "Article introuvable")
4. Ajoute un nouvel article "cable_usb" avec 50 unités
5. Supprime l'article "laptop"
6. Affiche l'inventaire final

Utilise les méthodes appropriées pour manipuler le dictionnaire.

## Défi 3: Analyseur de résultats d'examen

Créez un programme qui :
1. Crée un dictionnaire des scores d'étudiants :
   {"alice": 95, "bob": 78, "charlie": 88, "diana": 92, "eve": 85}
2. Affiche tous les étudiants et leurs scores
3. Trouve et affiche le score maximum et minimum
4. Calcule la moyenne
5. Compte combien d'étudiants ont un score >= 85
6. Affiche les étudiants qui ont échoué (< 50)

Utilise keys(), values(), items() et des boucles.

## Défi 4: Dict comprehension - Générateur de table de multiplication

Créez un programme qui :
1. Utilise dict comprehension pour créer une table de multiplication
   pour les nombres 1 à 10 (10 * 10 = 100)
   Clé : "1x2", "1x3", ..., "10x10"
   Valeur : résultat de la multiplication

2. Affiche la table complète

3. Recherche toutes les multiplications qui donnent 12

4. Utilise dict comprehension pour créer un nouveau dictionnaire
   avec uniquement les multiplications >= 50

Exemple partiel :
{'1x1': 1, '1x2': 2, ..., '10x10': 100}

## Défi 5: Scanner de ports (cybersécurité)

Créez un programme qui :
1. Définit un dictionnaire de ports et services :
   {
     22: "SSH",
     80: "HTTP",
     443: "HTTPS",
     3306: "MySQL",
```python
     5432: "PostgreSQL"
```
   }

2. Crée un dictionnaire de résultats de scan :
   {
     22: "open",
     80: "open",
     443: "closed",
```python
     3306: "filtered",
     5432: "closed"
```
   }

3. Itère sur les résultats et affiche le statut avec le service :
   "Port 22 (SSH) : open"

4. Affiche uniquement les ports ouverts avec leur service

5. Affiche le nombre de ports ouverts, fermés et filtrés

## Défi 6: Base de données d'utilisateurs imbriquée

Créez un programme qui :
1. Crée une base de données d'utilisateurs imbriquée :
   {
```python
     "user1": {"nom": "Alice", "role": "admin", "email": "alice@example.com"},
     "user2": {"nom": "Bob", "role": "user", "email": "bob@example.com"},
     "user3": {"nom": "Charlie", "role": "user", "email": "charlie@example.com"}
```
   }

2. Affiche les informations de chaque utilisateur

3. Affiche uniquement les administrateurs

4. Ajoute un nouvel utilisateur "user4" avec ses informations

5. Modifie le rôle de "user2" pour le passer en "admin"

6. Affiche la base mise à jour

## Défi 7: Configuration d'application avancée

Créez un programme qui :
1. Définit une configuration par défaut :
   {
```python
     "app": {"nom": "MyApp", "version": "1.0.0", "debug": False},
     "serveur": {"host": "localhost", "port": 5000, "ssl": False},
     "base_donnees": {"type": "sqlite", "nom": "app.db"}
```
   }

2. Charge une configuration utilisateur (vous pouvez en hardcoder une) :
   {
```python
     "app": {"debug": True},
     "serveur": {"port": 8080}
```
   }

3. Fusionne les deux configurations (config utilisateur écrase par défaut)

4. Affiche la configuration finale complète

5. Affiche uniquement les paramètres du serveur

6. Modifie le port du serveur à 9000

7. Affiche la configuration finale

## Défi 8: Rapport de vulnérabilités (red teaming)

Créez un programme qui :
1. Crée une base de vulnérabilités détectées :
   {
```python
     "CVE-2024-1234": {
       "description": "RCE in WebApp",
       "severite": "critique",
       "cvss_score": 9.8,
       "patch": True
     },
     "CVE-2024-5678": {
       "description": "SQL Injection",
       "severite": "haute",
       "cvss_score": 8.9,
       "patch": False
     },
     "CVE-2024-9999": {
       "description": "XSS",
       "severite": "moyenne",
       "cvss_score": 6.1,
       "patch": True
     }
```
   }

2. Affiche un rapport avec toutes les vulnérabilités

3. Génère des statistiques :
   - Nombre de vulnérabilités par sévérité
   - Score CVSS moyen
   - Nombre de vulnérabilités avec/sans patch

4. Affiche uniquement les vulnérabilités critiques

5. Affiche les vulnérabilités sans patch (à corriger en priorité)

6. Trie les vulnérabilités par score CVSS (décroissant)
   et affiche le top 3

Utilise dict comprehension, items(), boucles et conditions.

