class ProcessNode:
    def __init__(self, pid, name):
        self.pid = pid
        self.name = name
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def __repr__(self):
        return f"{self.name} ({self.pid})"

def build_process_tree(process_list):
    nodes = {}
    root = None
    
    # 1. Création des nœuds
    for p in process_list:
        nodes[p["pid"]] = ProcessNode(p["pid"], p["name"])

    # 2. Liaison Parents-Enfants
    for p in process_list:
        pid = p["pid"]
        ppid = p["ppid"]
        current_node = nodes[pid]
        
        if ppid == 0:
            root = current_node
        elif ppid in nodes:
            parent_node = nodes[ppid]
            parent_node.add_child(current_node)
            
    return root

def detect_suspicious_activity(node):
    alerts = []
    
    if not node:
        return alerts
        
    # Liste des parents suspects (Office)
    suspicious_parents = ["word.exe", "excel.exe", "powerpnt.exe"]
    # Liste des enfants interdits pour ces parents
    suspicious_children = ["cmd.exe", "powershell.exe", "wscript.exe"]
    
    # Vérification de la règle
    if node.name in suspicious_parents:
        for child in node.children:
            if child.name in suspicious_children:
                alerts.append(f"Suspicious: {node.name} ({node.pid}) spawned {child.name} ({child.pid})")
    
    # Récursion sur tous les enfants
    for child in node.children:
        alerts.extend(detect_suspicious_activity(child))
    
    return alerts

# --- Zone de Test ---
if __name__ == "__main__":
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
        
    print("[*] Analyse de sécurité...")
    alerts = detect_suspicious_activity(root)
    
    if alerts:
        print(f"[ALERT] Activité malveillante détectée :")
        for alert in alerts:
            print(f"  -> {alert}")
    else:
        print("[OK] Aucune activité suspecte.")
        
    if len(alerts) == 1 and "word.exe" in alerts[0] and "cmd.exe" in alerts[0]:
        print("\n[SUCCESS] Bravo ! L'attaque a été détectée.")
    else:
        print("\n[FAIL] L'attaque n'a pas été détectée correctement.")
