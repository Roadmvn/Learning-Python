def ror(value, count):
    """Rotation à droite (Rotate Right)."""
    count %= 32  # Normaliser
    return ((value >> count) | (value << (32 - count))) & 0xFFFFFFFF

def ror13_hash(name):
    """Calcule le hash ROR13 d'un nom de fonction."""
    hash_value = 0
    
    for char in name.upper():  # Insensible à la casse
        hash_value = ror(hash_value, 13)
        hash_value += ord(char)
        hash_value &= 0xFFFFFFFF  # Garder 32 bits
    
    return hash_value

# --- Zone de Test ---
if __name__ == "__main__":
    print("=== Test 1 : Rotation ROR ===")
    test_value = 0b11010110
    result = ror(test_value, 3)
    print(f"ROR({bin(test_value)}, 3) = {bin(result)}")
    
    print("\n=== Test 2 : ROR13 Hash ===")
    
    # Hash connus de Metasploit (référence)
    known_hashes = {
        "CreateProcessW":     0x16b3fe72,
        "VirtualAlloc":       0x91afca54,
        "WriteProcessMemory": 0xd83d6aa1,
        "LoadLibraryA":       0x0726774c,
        "GetProcAddress":     0x7c0dfcaa,
    }
    
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
        print("\n[FAIL] Certains hash ne correspondent pas.")
    
    print("\n=== Bonus : Générer des Hash pour Vos Malwares ===")
    custom_apis = [
        "WinExec",
        "ShellExecuteA",
        "URLDownloadToFileA",
        "RegSetValueExA",
    ]
    
    print("\nAPIs Utiles pour Malware :")
    for api in custom_apis:
        hash_val = ror13_hash(api)
        print(f"  {api:25} -> 0x{hash_val:08x}")
