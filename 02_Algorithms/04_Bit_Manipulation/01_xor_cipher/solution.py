def xor_cipher_single(data, key):
    """Chiffre/Déchiffre data avec une clé XOR single-byte."""
    return bytes([b ^ key for b in data])

def xor_cipher_multibyte(data, key):
    """Chiffre/Déchiffre data avec une clé XOR multi-byte."""
    key_len = len(key)
    return bytes([data[i] ^ key[i % key_len] for i in range(len(data))])

def rolling_xor(data, initial_key):
    """BONUS : Chiffre avec une clé XOR qui évolue."""
    result = bytearray()
    current_key = initial_key
    
    for byte in data:
        result.append(byte ^ current_key)
        current_key = (current_key + 1) % 256  # Incrémente et wraparound
    
    return bytes(result)

# --- Zone de Test ---
if __name__ == "__main__":
    print("=== Test 1 : XOR Single-Byte ===")
    message = b"cmd.exe"
    key = 0x42
    
    encrypted = xor_cipher_single(message, key)
    print(f"Message original : {message}")
    print(f"Clé             : 0x{key:02x}")
    print(f"Chiffré (hex)   : {encrypted.hex()}")
    
    decrypted = xor_cipher_single(encrypted, key)
    print(f"Déchiffré       : {decrypted}")
    
    if decrypted == message:
        print("[SUCCESS] Le décodage fonctionne !\n")
    else:
        print("[FAIL] Erreur de décodage.\n")
    
    print("=== Test 2 : XOR Multi-Byte ===")
    message = b"ATTACK_AT_DAWN"
    key = b"SECRET"
    
    encrypted = xor_cipher_multibyte(message, key)
    print(f"Message original : {message}")
    print(f"Clé             : {key}")
    print(f"Chiffré (hex)   : {encrypted.hex()}")
    
    decrypted = xor_cipher_multibyte(encrypted, key)
    print(f"Déchiffré       : {decrypted}")
    
    if decrypted == message:
        print("[SUCCESS] XOR multi-byte fonctionne !\n")
    else:
        print("[FAIL] Erreur.\n")
    
    print("=== Test 3 : Rolling XOR (BONUS) ===")
    message = b"PAYLOAD"
    initial_key = 0xAA
    
    encrypted = rolling_xor(message, initial_key)
    print(f"Message original : {message}")
    print(f"Clé initiale    : 0x{initial_key:02x}")
    print(f"Chiffré (hex)   : {encrypted.hex()}")
    
    # Pour vérifier le rolling : chaque byte devrait utiliser key+i
    print("\n[INFO] Vérification du Rolling :")
    for i, (orig, enc) in enumerate(zip(message, encrypted)):
        expected_key = (initial_key + i) % 256
        calculated = orig ^ expected_key
        print(f"  Byte {i} : {orig:02x} ^ {expected_key:02x} = {calculated:02x} (attendu: {enc:02x}) {'✓' if calculated == enc else '✗'}")
