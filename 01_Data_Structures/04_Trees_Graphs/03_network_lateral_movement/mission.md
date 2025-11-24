# Mission : Mouvement Latéral (Network Worm)

## Objectif
Comprendre comment naviguer dans un **Graphe (Graph)** pour trouver le chemin le plus court vers une cible. C'est le principe du **Mouvement Latéral** et du routage réseau.

## Contexte
Un réseau informatique est un **Graphe** :
- Les ordinateurs sont des sommets (Vertices).
- Les connexions réseau sont des arêtes (Edges).

Un malware de type "Ver" (Worm) ou un attaquant humain veut aller de sa machine compromise (Patient Zero) jusqu'au **Contrôleur de Domaine (DC)**, en sautant de machine en machine.

## Votre Mission
Vous devez compléter `worm_logic.py` pour :
1.  Implémenter un algorithme de recherche de chemin (BFS - Breadth-First Search).
2.  Trouver le chemin le plus court entre `PC_Infecté` et `Domain_Controller`.
3.  Retourner la liste des machines à traverser.

## Données
Le réseau est représenté par un dictionnaire d'adjacence :
```python
network = {
    "PC_Infecté": ["Serveur_Web", "Imprimante"],
    "Serveur_Web": ["PC_Infecté", "Base_de_Données"],
    "Imprimante": ["PC_Infecté", "PC_Secretaire"],
    "Base_de_Données": ["Serveur_Web", "Domain_Controller"],
    "PC_Secretaire": ["Imprimante"],
    "Domain_Controller": ["Base_de_Données"]
}
```

## Algorithme Recommandé : BFS (Breadth-First Search)
Le BFS est idéal pour trouver le chemin le plus court dans un graphe non pondéré.
1.  Utilisez une file (Queue).
2.  Gardez une trace des nœuds visités pour éviter les boucles.
3.  Pour chaque nœud, mémorisez d'où vous venez pour reconstruire le chemin à la fin.

## Lancement
1.  Lancez `python3 worm_logic.py`.
2.  Vérifiez si vous atteignez le DC en un minimum de sauts.
