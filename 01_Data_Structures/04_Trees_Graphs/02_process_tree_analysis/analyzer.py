class ProcessNode:
    def __init__(self, pid, name):
        self.pid = pid
        self.name = name
        self.children = []  # Liste des enfants

    def add_child(self, node):
        self.children.append(node)

    def __repr__(self):
        return f"{self.name} ({self.pid})"

def build_process_tree(process_list):
    """
    Construit un arbre de processus à partir d'une liste plate.
    
    Args:
        process_list (list): Liste de dicts {"pid": int, "ppid": int, "name": str}
        
    Returns:
        ProcessNode: La racine de l'arbre (PID 1)
    """
    nodes = {}
    root = None
    
    # ============================================================
    # ÉTAPE 1 : Créer tous les nœuds
    # ============================================================
    # Pour chaque processus, créez un ProcessNode et stockez-le dans 'nodes'
    # Clé = PID, Valeur = ProcessNode(pid, name)
    
    for p in process_list:
        # TODO: Créez un ProcessNode et ajoutez-le au dictionnaire
        # nodes[p["pid"]] = ProcessNode(p["pid"], p["name"])
        pass

    # ============================================================
    # ÉTAPE 2 : Lier les parents et les enfants
    # ============================================================
    # Pour chaque processus, trouvez son parent et ajoutez-le comme enfant
    
    for p in process_list:
        pid = p["pid"]
        ppid = p["ppid"]
        current_node = nodes[pid]  # Le nœud actuel
        
        # --------------------------------------------------------
        # CAS 1 : Si ppid == 0, c'est la racine
        # --------------------------------------------------------
        # TODO: if ppid == 0:
            # TODO: root = current_node
        
        # --------------------------------------------------------
        # CAS 2 : Sinon, trouvez le parent et liez
        # --------------------------------------------------------
        # TODO: elif ppid in nodes:
            # Trouvez le nœud parent dans 'nodes'
            # TODO: parent_node = nodes[ppid]
            # Ajoutez current_node comme enfant du parent
            # TODO: parent_node.add_child(current_node)
            pass
            
    return root

def detect_suspicious_activity(node):
    """
    Parcourt l'arbre pour trouver des relations suspectes.
    Règle : Si 'word.exe' ou 'excel.exe' lance 'cmd.exe' ou 'powershell.exe' -> ALERTE
    """
    alerts = []
    
    # Vérifier si node existe
    if not node:
        return alerts
    
    # ============================================================
    # ÉTAPE 1 : Définir les listes de suspects
    # ============================================================
    suspicious_parents = ["word.exe", "excel.exe", "powerpnt.exe"]
    suspicious_children = ["cmd.exe", "powershell.exe", "wscript.exe"]
    
    # ============================================================
    # ÉTAPE 2 : Vérifier si le nœud actuel est un parent suspect
    # ============================================================
    # TODO: if node.name in suspicious_parents:
        # Parcourez tous les enfants de ce nœud
        # TODO: for child in node.children:
            # Vérifiez si l'enfant est dans la liste des enfants interdits
            # TODO: if child.name in suspicious_children:
                # Ajoutez une alerte
                # alert_msg = f"Suspicious: {node.name} ({node.pid}) spawned {child.name} ({child.pid})"
                # TODO: alerts.append(alert_msg)
    
    # ============================================================
    # ÉTAPE 3 : Appel récursif sur tous les enfants
    # ============================================================
    # Pour chaque enfant, appelez récursivement cette fonction
    
    # TODO: for child in node.children:
        # Appelez detect_suspicious_activity sur l'enfant
        # Ajoutez les résultats à alerts
        # TODO: alerts.extend(detect_suspicious_activity(child))
    
    return alerts

# --- Zone de Test ---
if __name__ == "__main__":
    # Simulation de processus
    data = [
        {"pid": 1, "ppid": 0, "name": "system"},
        {"pid": 100, "ppid": 1, "name": "explorer.exe"},
        {"pid": 101, "ppid": 1, "name": "services.exe"},
        {"pid": 200, "ppid": 100, "name": "firefox.exe"},
        {"pid": 201, "ppid": 100, "name": "word.exe"},
        {"pid": 300, "ppid": 201, "name": "cmd.exe"},      # SUSPECT !
        {"pid": 301, "ppid": 300, "name": "whoami.exe"},
        {"pid": 400, "ppid": 101, "name": "svchost.exe"}
    ]
    
    print("[*] Construction de l'arbre de processus...")
    root = build_process_tree(data)
    
    if root:
        print(f"    Racine trouvée : {root}")
    else:
        print("    [ERREUR] Pas de racine trouvée !")
        
    print("[*] Analyse de sécurité...")
    alerts = detect_suspicious_activity(root)
    
    if alerts:
        print(f"[ALERT] Activité malveillante détectée :")
        for alert in alerts:
            print(f"  -> {alert}")
    else:
        print("[OK] Aucune activité suspecte.")
        
    # Vérification
    if len(alerts) == 1 and "word.exe" in alerts[0] and "cmd.exe" in alerts[0]:
        print("\n[SUCCESS] Bravo ! L'attaque a été détectée.")
    else:
        print("\n[FAIL] L'attaque n'a pas été détectée correctement.")
