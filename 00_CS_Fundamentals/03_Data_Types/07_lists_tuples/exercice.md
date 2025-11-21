# Exercice 07: Listes et Tuples - Défis

## Défi 1: Création et indexing de liste

Créez un programme qui :
1. Créez une liste de 5 adresses IP : ["192.168.1.1", "10.0.0.5", "172.16.0.1", "8.8.8.8", "1.1.1.1"]
2. Affiche l'adresse IP à l'index 0
3. Affiche l'adresse IP à l'index -1 (dernière)
4. Affiche l'adresse IP à l'index 2
5. Affiche le nombre total d'adresses IP

## Défi 2: Slicing de listes

Créez un programme qui :
1. Créez une liste de ports : [21, 22, 23, 25, 53, 80, 110, 143, 443, 465, 993, 995]
2. Affiche les 3 premiers ports
3. Affiche les 3 derniers ports
4. Affiche les ports du 2ème au 5ème inclus (indices 2 à 5)
5. Affiche tous les ports paires (tous les 2)
6. Affiche tous les ports en ordre inversé

## Défi 3: Modification de listes (append, extend, insert)

Créez un programme qui :
1. Crée une liste vide : targets = []
2. Ajoute 3 IPs avec append() : "192.168.1.1", "192.168.1.2", "192.168.1.3"
3. Ajoute 2 IPs avec extend() : "10.0.0.1", "10.0.0.2"
4. Insère "172.16.0.1" à la position 2
5. Affiche la liste finale
6. Affiche le nombre total d'IPs

## Défi 4: Suppression d'éléments (remove, pop, del)

Créez un programme qui :
1. Crée une liste : services = ["SSH", "HTTP", "HTTPS", "FTP", "Telnet", "SMTP"]
2. Supprime "Telnet" avec remove()
3. Supprime le premier élément avec pop(0)
4. Supprime le dernier élément avec pop()
5. Supprime l'élément à l'index 1 avec del
6. Affiche la liste finale

## Défi 5: Recherche et tri

Créez un programme qui :
1. Crée une liste de scores de menace : [45, 23, 89, 12, 56, 78, 34, 92]
2. Affiche le score maximum avec max()
3. Affiche le score minimum avec min()
4. Affiche la somme avec sum()
5. Trie la liste en ordre croissant avec sort()
6. Trie la liste en ordre décroissant avec sort(reverse=True)
7. Trouve la position du score 89 avec index()
8. Compte combien de fois 78 apparaît avec count()

## Défi 6: Tuples et unpacking

Créez un programme qui :
1. Crée un tuple de credentials : ("admin", "password123", "192.168.1.100")
2. Extrait les 3 éléments avec unpacking : username, password, ip = credentials
3. Affiche username, password, ip
4. Crée un tuple vide
5. Crée un tuple avec un seul élément (ATTENTION : virgule!)
6. Essayez de modifier le 1er élément du tuple credentials (vous devez obtenir une erreur)

## Défi 7: List Comprehension - Filtrage

Créez un programme qui :
1. Crée une liste de nombres : range(1, 21)
2. Créez une liste de nombres PAIRS avec list comprehension
3. Créez une liste de nombres IMPAIRS avec list comprehension
4. Créez une liste de nombres > 10 avec list comprehension
5. Créez une liste de carrés de nombres 1 à 10

## Défi 8: List Comprehension - Cybersécurité

Créez un programme qui simule un scanneur de ports :
1. Crées une liste de ports scannés avec leur statut :
   scan_data = [(22, "open"), (23, "closed"), (80, "open"),
```python
                (443, "open"), (3306, "filtered"), (8080, "open")]
```
2. Utilisez list comprehension pour :
   a) Extraire seulement les ports OUVERTS
   b) Extraire seulement les ports FERMÉS
   c) Créer une liste de chaînes formatées :
```python
      "Port 22 (SSH) : open"
```
3. Affiche les résultats

Indice : utilisez la syntaxe [expression for item in list if condition]

DÉFI BONUS : Gestion de liste noire d'IP

Créez un système complet de gestion de liste noire :
1. Initialise une liste noire : blacklist = []
2. Définis une liste d'IPs suspectes :
   suspicious = ["203.0.113.10", "198.51.100.20", "203.0.113.10", "192.0.2.30"]
3. Pour chaque IP suspecte :
   - Si elle n'est pas dans blacklist : ajouter avec append()
   - Si elle est déjà dans blacklist : afficher "[!] Déjà listée"
4. Affiche la liste noire finale
5. Simule un blanchiment d'une IP : supprime la 1ère IP avec remove()
6. Affiche la liste noire mise à jour
7. Affiche le nombre total d'IPs en liste noire

## Conseils

1. LISTES vs TUPLES :
   - Listes : mutables, utilisez [] et modifiez librement
   - Tuples : immutables, utilisez () pour des données constantes

2. INDEXING :
   - Commence à 0 : liste[0] = premier élément
   - Négatif : liste[-1] = dernier élément
   - Hors limites : IndexError !

3. SLICING [start:stop:step] :
   - start : inclus (défaut = 0)
   - stop : EXCLUS (défaut = fin)
   - step : intervalle (défaut = 1)

4. MÉTHODES :
   - append(x) : ajoute UN élément (liste)
   - extend(x) : ajoute PLUSIEURS éléments (itérable)
   - insert(i, x) : insère à la position i
   - remove(x) : supprime le 1er x trouvé
   - pop(i) : supprime et retourne l'élément à i (-1 = dernier)
   - sort() : trie sur place
   - reverse() : inverse sur place

5. LIST COMPREHENSION :
   - Syntaxe : [expression for item in iterable if condition]
   - Compact et Pythonique !
   - Utile pour créer des listes filtrées/transformées

6. OPÉRATIONS :
   - + : concatène deux listes
   - * : répète une liste
   - in : vérifie appartenance
   - len() : compte les éléments
   - sum() : somme les nombres
   - max() / min() : maximum/minimum

7. COPY() IMPORTANT :
   - liste2 = liste1 : crée une RÉFÉRENCE (pas de copie)
   - liste2 = liste1.copy() : crée une VRAIE COPIE

8. CYBERSÉCURITÉ :
   - Utilisez les listes pour gérer des collections d'IPs, ports, services
   - Utilisez les tuples pour des données immuables (credentials)
   - List comprehension pour filtrer des données de scan

