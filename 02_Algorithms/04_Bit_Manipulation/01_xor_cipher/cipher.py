def xor_cipher_single(data, key):
    """
    Chiffre/Déchiffre data avec une clé XOR single-byte.
    
    Args:
        data (bytes): Données à chiffrer
        key (int): Clé XOR (0-255)
        
    Returns:
        bytes: Données chiffrées/déchiffrées
    """
    # ============================================================
    # ÉTAPE 1 : Appliquer XOR sur chaque byte
    # ============================================================
    # Pour chaque byte de 'data', appliquez l'opération XOR avec 'key'
    # Utilisez une list comprehension : [... for byte in data]
    
    # Indice 1 : L'opérateur XOR en Python est ^
    # Indice 2 : Pour chaque byte : byte ^ key
    # Indice 3 : Convertissez le résultat en bytes avec bytes([...])
    
    # TODO: return bytes([b ^ key for b in data])
    pass

def xor_cipher_multibyte(data, key):
    """
    Chiffre/Déchiffre data avec une clé XOR multi-byte.
    
    Args:
        data (bytes): Données à chiffrer
        key (bytes): Clé XOR (séquence de bytes)
        
    Returns:
        bytes: Données chiffrées/déchiffrées
    """
    # ============================================================
    # ÉTAPE 1 : Obtenir la longueur de la clé
    # ============================================================
    # TODO: key_len = len(key)
    
    # ============================================================
    # ÉTAPE 2 : Appliquer XOR avec répétition de la clé
    # ============================================================
    # Pour chaque position i dans data :
    #   - Trouvez la clé correspondante avec le modulo : key[i % key_len]
    #   - Appliquez XOR : data[i] ^ key[i % key_len]
    
    # Indice : Utilisez une list comprehension avec range(len(data))
    # TODO: return bytes([data[i] ^ key[i % key_len] for i in range(len(data))])
    pass

def rolling_xor(data, initial_key):
    """
    BONUS : Chiffre avec une clé XOR qui évolue.
    
    Args:
        data (bytes): Données à chiffrer
        initial_key (int): Clé initiale
        
    Returns:
        bytes: Données chiffrées
    """
    # ============================================================
    # ÉTAPE 1 : Créer un tableau pour le résultat
    # ============================================================
    # Utilisez bytearray() pour créer un tableau mutable
    # TODO: result = bytearray()
    
    # ============================================================
    # ÉTAPE 2 : Initialiser la clé courante
    # ============================================================
    # TODO: current_key = initial_key
    
    # ============================================================
    # ÉTAPE 3 : Parcourir chaque byte
    # ============================================================
    # TODO: for byte in data:
        
        # ÉTAPE 3.1 : Appliquer XOR avec la clé courante
        # TODO: result.append(byte ^ current_key)
        
        # ÉTAPE 3.2 : Incrémenter la clé (avec wraparound à 256)
        # TODO: current_key = (current_key + 1) % 256
    
    # TODO: return bytes(result)
    pass

# --- Zone de Test ---
if __name__ == "__main__":
    print("=== Test 1 : XOR Single-Byte ===")
    message = b"cmd.exe"
    key = 0x42
    
    encrypted = xor_cipher_single(message, key)
    if encrypted:
        print(f"Message original : {message}")
        print(f"Clé             : 0x{key:02x}")
        print(f"Chiffré (hex)   : {encrypted.hex()}")
        
        decrypted = xor_cipher_single(encrypted, key)
        print(f"Déchiffré       : {decrypted}")
        
        if decrypted == message:
            print("[SUCCESS] Le décodage fonctionne !\n")
        else:
            print("[FAIL] Erreur de décodage.\n")
    else:
        print("[FAIL] Fonction non implémentée.\n")
    
    print("=== Test 2 : XOR Multi-Byte ===")
    message = b"ATTACK_AT_DAWN"
    key = b"SECRET"
    
    encrypted = xor_cipher_multibyte(message, key)
    if encrypted:
        print(f"Message original : {message}")
        print(f"Clé             : {key}")
        print(f"Chiffré (hex)   : {encrypted.hex()}")
        
        decrypted = xor_cipher_multibyte(encrypted, key)
        print(f"Déchiffré       : {decrypted}")
        
        if decrypted == message:
            print("[SUCCESS] XOR multi-byte fonctionne !\n")
        else:
            print("[FAIL] Erreur.\n")
    else:
        print("[FAIL] Fonction non implémentée.\n")
    
    print("=== Test 3 : Rolling XOR (BONUS) ===")
    message = b"PAYLOAD"
    initial_key = 0xAA
    
    encrypted = rolling_xor(message, initial_key)
    if encrypted:
        print(f"Message original : {message}")
        print(f"Clé initiale    : 0x{initial_key:02x}")
        print(f"Chiffré (hex)   : {encrypted.hex()}")
        print("[INFO] Vérifiez manuellement si la clé évolue correctement.\n")
    else:
        print("[INFO] Rolling XOR non implémenté (bonus).\n")
