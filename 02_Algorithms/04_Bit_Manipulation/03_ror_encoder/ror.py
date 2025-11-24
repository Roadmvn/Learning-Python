def ror(value, count):
    """
    Rotation à droite (Rotate Right).
    
    Args:
        value (int): Valeur à décaler
        count (int): Nombre de bits de rotation
        
    Returns:
        int: Valeur après rotation (32 bits)
    """
    # ============================================================
    # ÉTAPE 1 : Normaliser count (éviter count > 32)
    # ============================================================
    # TODO: count = count % 32
    
    # ============================================================
    # ÉTAPE 2 : Décaler à droite
    # ============================================================
    # Les bits de droite "tombent" à droite
    # TODO: right_part = value >> count
    
    # ============================================================
    # ÉTAPE 3 : Récupérer les bits perdus
    # ============================================================
    # Les bits qui "tombent" doivent revenir à gauche (wraparound)
    # TODO: left_part = value << (32 - count)
    
    # ============================================================
    # ÉTAPE 4 : Combiner avec OR et masquer à 32 bits
    # ============================================================
    # TODO: return (right_part | left_part) & 0xFFFFFFFF
    pass

def ror13_hash(name):
    """
    Calcule le hash ROR13 d'un nom de fonction.
    Algorithme utilisé par Metasploit.
    
    Args:
        name (str): Nom de la fonction API
        
    Returns:
        int: Hash sur 32 bits
    """
    # ============================================================
    # ÉTAPE 1 : Initialiser le hash
    # ============================================================
    # TODO: hash_value = 0
    
    # ============================================================
    # ÉTAPE 2 : Parcourir chaque caractère (EN MAJUSCULES)
    # ============================================================
    # Utilisez .upper() pour rendre insensible à la casse
    
    # TODO: for char in name.upper():
        
        # --------------------------------------------------------
        # ÉTAPE 2.1 : Appliquer ROR de 13 bits sur le hash actuel
        # --------------------------------------------------------
        # TODO: hash_value = ror(hash_value, 13)
        
        # --------------------------------------------------------
        # ÉTAPE 2.2 : Ajouter la valeur ASCII du caractère
        # --------------------------------------------------------
        # Utilisez ord(char) pour obtenir le code ASCII
        # TODO: hash_value += ord(char)
        
        # --------------------------------------------------------
        # ÉTAPE 2.3 : Masquer à 32 bits
        # --------------------------------------------------------
        # TODO: hash_value &= 0xFFFFFFFF
    
    # TODO: return hash_value
    pass

# --- Zone de Test ---
if __name__ == "__main__":
    print("=== Test 1 : Rotation ROR ===")
    if ror:
        result = ror(0b11010110, 3)  # Exemple simple
        print(f"ROR(0b11010110, 3) = {bin(result)}")
    else:
        print("[FAIL] Fonction non implémentée.\n")
    
    print("\n=== Test 2 : ROR13 Hash ===")
    
    # Hash connus de Metasploit (référence)
    known_hashes = {
        "CreateProcessW":     0x16b3fe72,
        "VirtualAlloc":       0x91afca54,
        "WriteProcessMemory": 0xd83d6aa1,
        "LoadLibraryA":       0x0726774c,
        "GetProcAddress":     0x7c0dfcaa,
    }
    
    if ror13_hash:
        print("Fonction API           | Hash Calculé | Hash Attendu | Match")
        print("-" * 70)
        
        for api_name, expected_hash in known_hashes.items():
            calculated = ror13_hash(api_name)
            match = "✓" if calculated == expected_hash else "✗"
            print(f"{api_name:22} | 0x{calculated:08x}   | 0x{expected_hash:08x}   | {match}")
        
        # Vérification finale
        all_match = all(ror13_hash(name) == hash_val for name, hash_val in known_hashes.items())
        if all_match:
            print("\n[SUCCESS] Tous les hash correspondent ! ROR13 correctement implémenté.")
        else:
            print("\n[FAIL] Certains hash ne correspondent pas. Vérifiez votre implémentation.")
    else:
        print("[FAIL] Fonction non implémentée.")
