import os

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
    
    # ============================================================
    # ÉTAPE 1 : Lister le contenu du dossier
    # ============================================================
    # Utilisez os.listdir(directory) pour obtenir la liste des éléments
    # Astuce : Gérez l'exception PermissionError avec try/except
    
    try:
        contenu = None  # TODO: Remplacez None par os.listdir(...)
    except PermissionError:
        # Si on n'a pas la permission, on retourne une liste vide
        return []
    
    # ============================================================
    # ÉTAPE 2 : Parcourir chaque élément
    # ============================================================
    # Utilisez une boucle for pour parcourir 'contenu'
    
    # TODO: for element in contenu:
        
        # --------------------------------------------------------
        # ÉTAPE 2.1 : Construire le chemin complet
        # --------------------------------------------------------
        # Combinez 'directory' et 'element' avec os.path.join()
        
        # TODO: chemin_complet = os.path.join(...)
        
        # --------------------------------------------------------
        # ÉTAPE 2.2 : Vérifier si c'est un dossier
        # --------------------------------------------------------
        # Utilisez os.path.isdir(chemin_complet)
        # Si OUI → Appel récursif (on plonge dedans)
        
        # TODO: if os.path.isdir(...):
            # Appel récursif : find_secrets(chemin_complet)
            # Ajoutez les résultats à found_files avec .extend()
            # TODO: found_files.extend(...)
        
        # --------------------------------------------------------
        # ÉTAPE 2.3 : Vérifier si c'est un fichier .secret
        # --------------------------------------------------------
        # Utilisez os.path.isfile(chemin_complet)
        # ET vérifiez si le nom se termine par '.secret'
        
        # TODO: elif os.path.isfile(...):
            # TODO: if chemin_complet.endswith('.secret'):
                # Ajoutez le chemin ABSOLU à found_files
                # TODO: found_files.append(os.path.abspath(...))
    
    return found_files


# --- Zone de Test ---
if __name__ == "__main__":
    # Création d'un environnement de test temporaire si nécessaire
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
        
    # Vérification simple
    if len(secrets) == 2:
        print("\n[SUCCESS] Bravo ! Vous avez trouvé tous les fichiers secrets.")
    else:
        print(f"\n[FAIL] Attendu : 2 fichiers. Trouvé : {len(secrets)}.")
