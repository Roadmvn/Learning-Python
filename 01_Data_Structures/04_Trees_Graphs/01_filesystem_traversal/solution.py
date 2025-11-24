import os

def find_secrets(directory):
    """
    Parcourt récursivement un dossier pour trouver les fichiers .secret
    
    Args:
        directory (str): Le chemin du dossier à scanner
        
    Returns:
        list: Une liste des chemins absolus des fichiers .secret trouvés
    """
    found_files = []
    
    try:
        # Liste tous les éléments du dossier
        items = os.listdir(directory)
    except PermissionError:
        # En sécurité, il faut toujours gérer les erreurs de permission !
        return []

    for item in items:
        # Construit le chemin complet
        full_path = os.path.join(directory, item)
        
        # Si c'est un dossier, on plonge dedans (Récursion - DFS)
        if os.path.isdir(full_path):
            # On ajoute les résultats du sous-dossier à notre liste
            found_files.extend(find_secrets(full_path))
            
        # Si c'est un fichier, on vérifie l'extension
        elif os.path.isfile(full_path):
            if full_path.endswith(".secret"):
                found_files.append(os.path.abspath(full_path))
                
    return found_files

# --- Zone de Test ---
if __name__ == "__main__":
    target_dir = "test_env"
    
    # Création automatique de l'environnement de test pour l'exercice
    if not os.path.exists(target_dir):
        print(f"[*] Création du dossier de test '{target_dir}'...")
        os.makedirs(os.path.join(target_dir, "docs", "work"))
        os.makedirs(os.path.join(target_dir, "photos"))
        
        with open(os.path.join(target_dir, "notes.txt"), "w") as f: f.write("rien")
        with open(os.path.join(target_dir, "config.secret"), "w") as f: f.write("TOP SECRET")
        with open(os.path.join(target_dir, "docs", "report.pdf"), "w") as f: f.write("rien")
        with open(os.path.join(target_dir, "docs", "work", "passwords.secret"), "w") as f: f.write("123456")
        with open(os.path.join(target_dir, "photos", "cat.jpg"), "w") as f: f.write("miaou")
    
    print(f"[*] Scan du dossier : {os.path.abspath(target_dir)}")
    secrets = find_secrets(target_dir)
    
    print(f"[*] Fichiers trouvés : {len(secrets)}")
    for s in secrets:
        print(f"  -> {s}")
        
    if len(secrets) == 2:
        print("\n[SUCCESS] Bravo ! Vous avez trouvé tous les fichiers secrets.")
    else:
        print(f"\n[FAIL] Attendu : 2 fichiers. Trouvé : {len(secrets)}.")
