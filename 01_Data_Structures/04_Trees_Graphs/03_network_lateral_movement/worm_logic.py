from collections import deque

def find_attack_path(network_graph, start_node, target_node):
    """
    Trouve le chemin le plus court entre start_node et target_node (BFS).
    
    Args:
        network_graph (dict): Dictionnaire d'adjacence du réseau
        start_node (str): Nom de la machine de départ
        target_node (str): Nom de la machine cible
        
    Returns:
        list: Liste des machines du chemin (ex: ["A", "B", "C"]) ou None si impossible
    """
    # Vérification préliminaire
    if start_node not in network_graph or target_node not in network_graph:
        return None
    
    # ============================================================
    # ÉTAPE 1 : Initialiser la file (Queue) pour le BFS
    # ============================================================
    # La file contient des tuples : (machine_actuelle, chemin_parcouru)
    # Utilisez deque de collections (déjà importé en haut)
    
    # TODO: queue = deque([ (start_node, [start_node]) ])
    
    # ============================================================
    # ÉTAPE 2 : Initialiser l'ensemble des machines visitées
    # ============================================================
    # Pour éviter les cycles (tourner en rond), on garde trace des machines déjà visitées
    
    # TODO: visited = set([start_node])
    
    # ============================================================
    # ÉTAPE 3 : Boucle BFS
    # ============================================================
    # Tant que la file n'est pas vide, continuer à explorer
    
    # TODO: while queue:
        
        # --------------------------------------------------------
        # ÉTAPE 3.1 : Sortir le premier élément de la file
        # --------------------------------------------------------
        # Utilisez .popleft() pour sortir de la gauche
        
        # TODO: current_node, path = queue.popleft()
        
        # --------------------------------------------------------
        # ÉTAPE 3.2 : Vérifier si on a atteint la cible
        # --------------------------------------------------------
        # TODO: if current_node == target_node:
            # BRAVO ! On a trouvé le chemin le plus court
            # TODO: return path
        
        # --------------------------------------------------------
        # ÉTAPE 3.3 : Explorer tous les voisins
        # --------------------------------------------------------
        # Pour chaque voisin de current_node dans le graphe
        
        # TODO: for neighbor in network_graph[current_node]:
            
            # Vérifier si le voisin n'a pas déjà été visité
            # TODO: if neighbor not in visited:
                
                # Marquer le voisin comme visité
                # TODO: visited.add(neighbor)
                
                # Créer le nouveau chemin (ancien chemin + voisin)
                # TODO: new_path = list(path)
                # TODO: new_path.append(neighbor)
                
                # Ajouter à la file pour exploration future
                # TODO: queue.append((neighbor, new_path))
    
    # Si on sort de la boucle, aucun chemin trouvé
    return None

# --- Zone de Test ---
if __name__ == "__main__":
    # Cartographie du réseau (Graphe)
    network = {
        "Entry_Point": ["Web_Server", "Guest_Wifi"],
        "Guest_Wifi": ["Entry_Point"],
        "Web_Server": ["Entry_Point", "App_Server", "File_Share"],
        "File_Share": ["Web_Server", "Backup_Server"],
        "App_Server": ["Web_Server", "Database", "Admin_PC"],
        "Database": ["App_Server"],
        "Backup_Server": ["File_Share", "Domain_Controller"],  # Chemin long
        "Admin_PC": ["App_Server", "Domain_Controller"],       # Chemin court !
        "Domain_Controller": ["Backup_Server", "Admin_PC"]
    }
    
    start = "Entry_Point"
    target = "Domain_Controller"
    
    print(f"[*] Recherche du chemin d'attaque : {start} -> {target}")
    path = find_attack_path(network, start, target)
    
    if path:
        print(f"[SUCCESS] Chemin trouvé ({len(path)-1} sauts) :")
        print(" -> ".join(path))
        
        # Vérification du chemin optimal
        if len(path) == 5: # Entry -> Web -> App -> Admin -> DC
            print("\n[INFO] C'est le chemin le plus court (Optimal). Bien joué !")
        else:
            print(f"\n[INFO] Chemin valide mais peut-être pas le plus court (Longueur: {len(path)}).")
    else:
        print("\n[FAIL] Aucun chemin trouvé ou fonction non implémentée.")
