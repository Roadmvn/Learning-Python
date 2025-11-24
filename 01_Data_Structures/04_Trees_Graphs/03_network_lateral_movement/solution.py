from collections import deque

def find_attack_path(network_graph, start_node, target_node):
    """
    Trouve le chemin le plus court entre start_node et target_node (BFS).
    """
    if start_node not in network_graph or target_node not in network_graph:
        return None
        
    # File pour le BFS : contient (machine_actuelle, chemin_parcouru)
    queue = deque([ (start_node, [start_node]) ])
    visited = set([start_node])
    
    while queue:
        current_node, path = queue.popleft()
        
        # Si on a atteint la cible
        if current_node == target_node:
            return path
        
        # Exploration des voisins
        for neighbor in network_graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                queue.append((neighbor, new_path))
                
    return None

# --- Zone de Test ---
if __name__ == "__main__":
    network = {
        "Entry_Point": ["Web_Server", "Guest_Wifi"],
        "Guest_Wifi": ["Entry_Point"],
        "Web_Server": ["Entry_Point", "App_Server", "File_Share"],
        "File_Share": ["Web_Server", "Backup_Server"],
        "App_Server": ["Web_Server", "Database", "Admin_PC"],
        "Database": ["App_Server"],
        "Backup_Server": ["File_Share", "Domain_Controller"],
        "Admin_PC": ["App_Server", "Domain_Controller"],
        "Domain_Controller": ["Backup_Server", "Admin_PC"]
    }
    
    start = "Entry_Point"
    target = "Domain_Controller"
    
    print(f"[*] Recherche du chemin d'attaque : {start} -> {target}")
    path = find_attack_path(network, start, target)
    
    if path:
        print(f"[SUCCESS] Chemin trouvé ({len(path)-1} sauts) :")
        print(" -> ".join(path))
        
        if len(path) == 5:
            print("\n[INFO] C'est le chemin le plus court (Optimal). Bien joué !")
        else:
            print(f"\n[INFO] Chemin valide mais peut-être pas le plus court (Longueur: {len(path)}).")
    else:
        print("\n[FAIL] Aucun chemin trouvé.")
