# Privilèges Windows (Simulés avec Bit Flags)
SE_DEBUG_PRIVILEGE       = 1 << 0  # 0x01
SE_BACKUP_PRIVILEGE      = 1 << 1  # 0x02
SE_RESTORE_PRIVILEGE     = 1 << 2  # 0x04
SE_SHUTDOWN_PRIVILEGE    = 1 << 3  # 0x08
SE_LOAD_DRIVER_PRIVILEGE = 1 << 4  # 0x10

def has_privilege(token, privilege):
    """Vérifie si un token possède un privilège."""
    return (token & privilege) != 0

def add_privilege(token, privilege):
    """Ajoute un privilège à un token."""
    return token | privilege

def remove_privilege(token, privilege):
    """Retire un privilège d'un token."""
    return token & ~privilege

def can_dump_lsass(token):
    """Vérifie si on peut dumper lsass.exe (comme Mimikatz)"""
    return has_privilege(token, SE_DEBUG_PRIVILEGE)

def can_load_rootkit(token):
    """Vérifie si on peut charger un driver malveillant"""
    return has_privilege(token, SE_LOAD_DRIVER_PRIVILEGE)

def can_backup_system(token):
    """Vérifie si on peut backup tout le système"""
    # Besoin des DEUX privilèges
    return (has_privilege(token, SE_BACKUP_PRIVILEGE) and 
            has_privilege(token, SE_RESTORE_PRIVILEGE))

# --- Zone de Test ---
if __name__ == "__main__":
    print("=== Test 1 : Vérification de Privilèges ===")
    token = SE_DEBUG_PRIVILEGE | SE_BACKUP_PRIVILEGE
    print(f"Token actuel : {bin(token)} (0x{token:02x})")
    print(f"  Has SE_DEBUG_PRIVILEGE?  {has_privilege(token, SE_DEBUG_PRIVILEGE)}")
    print(f"  Has SE_LOAD_DRIVER?      {has_privilege(token, SE_LOAD_DRIVER_PRIVILEGE)}")
    
    print("\n=== Test 2 : Ajout de Privilège ===")
    token = add_privilege(token, SE_LOAD_DRIVER_PRIVILEGE)
    print(f"Token après ajout : {bin(token)} (0x{token:02x})")
    print(f"  Has SE_LOAD_DRIVER?  {has_privilege(token, SE_LOAD_DRIVER_PRIVILEGE)}")
    
    print("\n=== Test 3 : Retrait de Privilège ===")
    token = remove_privilege(token, SE_BACKUP_PRIVILEGE)
    print(f"Token après retrait : {bin(token)} (0x{token:02x})")
    print(f"  Has SE_BACKUP?  {has_privilege(token, SE_BACKUP_PRIVILEGE)}")
    
    print("\n=== Test 4 : Actions Malveillantes ===")
    # Token standard utilisateur
    user_token = 0
    print(f"[User Token] : {bin(user_token)}")
    print(f"  Peut dumper lsass? {can_dump_lsass(user_token)}")
    
    # Token avec SE_DEBUG
    debug_token = SE_DEBUG_PRIVILEGE
    print(f"\n[Debug Token] : {bin(debug_token)}")
    print(f"  Peut dumper lsass? {can_dump_lsass(debug_token)}")
    
    # Token admin complet
    admin_token = (SE_DEBUG_PRIVILEGE | SE_BACKUP_PRIVILEGE | 
                   SE_RESTORE_PRIVILEGE | SE_LOAD_DRIVER_PRIVILEGE)
    print(f"\n[Admin Token] : {bin(admin_token)} (0x{admin_token:02x})")
    print(f"  Peut dumper lsass?     {can_dump_lsass(admin_token)}")
    print(f"  Peut charger rootkit?  {can_load_rootkit(admin_token)}")
    print(f"  Peut backup système?   {can_backup_system(admin_token)}")
    
    print("\n[SUCCESS] Tous les tests ont passé !")
