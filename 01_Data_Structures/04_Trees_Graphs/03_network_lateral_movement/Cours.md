# Cours : Graphes & Mouvement Latéral

## 1. Le Réseau est un Graphe

Un réseau informatique se modélise parfaitement par un **Graphe**.
- **Sommets (Nodes)** : Ordinateurs, Serveurs, Utilisateurs.
- **Arêtes (Edges)** : Connexions possibles (câble, wifi, droits d'accès).

### Types de Graphes en Sécurité
1.  **Graphe Physique** : Qui est connecté à qui ? (Câbles, Switchs)
2.  **Graphe Logique** : Qui peut pinger qui ? (Firewalls, VLANs)
3.  **Graphe d'Identité (Active Directory)** : Qui a des droits sur quoi ? (Admin -> Serveur)

## 2. Le Mouvement Latéral

Une fois qu'un attaquant a compromis une machine (Patient Zero), il veut atteindre le "Joyau de la Couronne" (souvent le Contrôleur de Domaine ou la Base de Données).
Il doit "sauter" de machine en machine. C'est le **Mouvement Latéral**.

### Le Problème du Plus Court Chemin
Chaque saut comporte un risque de détection. L'attaquant veut donc le chemin le **plus court** et le **plus sûr**.

C'est un problème d'algorithmique classique : **Shortest Path Problem**.

## 3. Algorithme BFS (Breadth-First Search)

Pour trouver le chemin le plus court dans un graphe non pondéré (où chaque saut coûte 1), l'algorithme roi est le **BFS (Parcours en Largeur)**.

### Principe
Imaginez une vague qui part du point de départ.
1.  Elle touche tous les voisins directs (Distance 1).
2.  Puis les voisins des voisins (Distance 2).
3.  Etc.

Dès que la vague touche la cible, on a garanti d'avoir trouvé le chemin le plus court.

### Différence avec DFS (Profondeur)
Le DFS (utilisé pour les arbres de fichiers) fonce tête baissée le plus loin possible. Il peut trouver un chemin, mais souvent pas le plus court (il peut faire un détour énorme).

## 4. Outils Réels : BloodHound

Dans le monde professionnel (Red Team), l'outil **BloodHound** utilise exactement cette théorie.
1.  Il collecte toutes les relations Active Directory (Qui est admin de quoi ?).
2.  Il construit un Graphe géant (base de données Neo4j).
3.  Il permet à l'attaquant de demander : *"Quel est le chemin le plus court de 'Stagiaire' à 'Domain Admin' ?"*

Souvent, la réponse est complexe :
`Stagiaire` -> (a le mot de passe de) -> `PC_Compta` -> (où est connecté) -> `Admin_Reseau` -> (qui est Admin de) -> `Domain_Controller`.

C'est ce type de logique que nous allons implémenter dans l'exercice.
