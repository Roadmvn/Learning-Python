# Privilèges Windows (Simulés avec Bit Flags)
SE_DEBUG_PRIVILEGE       = 1 << 0  # 0x01 - Peut attacher debugger
SE_BACKUP_PRIVILEGE      = 1 << 1  # 0x02 - Peut lire fichiers protégés
SE_RESTORE_PRIVILEGE     = 1 << 2  # 0x04 - Peut écrire fichiers protégés
SE_SHUTDOWN_PRIVILEGE    = 1 << 3  # 0x08 - Peut éteindre système
SE_LOAD_DRIVER_PRIVILEGE = 1 << 4  # 0x10 - Peut charger drivers

def has_privilege(token, privilege):
    """
    Vérifie si un token possède un privilège spécifique.
    
    Args:
        token (int): Token de sécurité (bit flags)
        privilege (int): Privilège à vérifier
        
    Returns:
        bool: True si le privilège est présent
    """
    # ============================================================
    # ÉTAPE 1 : Utiliser l'opérateur AND (&) pour vérifier
    # ============================================================
    # L'opérateur & permet de "filtrer" un bit spécifique
    # Si le bit est activé, le résultat sera != 0
    
    # Exemple : token = 0b0101 (5), privilege = 0b0001 (1)
    #           token & privilege = 0b0001 (non-zero) → True
    
    # TODO: return (token & privilege) != 0
    pass

def add_privilege(token, privilege):
    """
    Ajoute un privilège à un token.
    
    Args:
        token (int): Token actuel
        privilege (int): Privilège à ajouter
        
    Returns:
        int: Nouveau token avec le privilège ajouté
    """
    # ============================================================
    # ÉTAPE 1 : Utiliser l'opérateur OR (|) pour ajouter
    # ============================================================
    # L'opérateur | "active" un bit sans affecter les autres
    
    # Exemple : token = 0b0100 (4), privilege = 0b0001 (1)
    #           token | privilege = 0b0101 (5)
    
    # TODO: return token | privilege
    pass

def remove_privilege(token, privilege):
    """
    Retire un privilège d'un token.
    
    Args:
        token (int): Token actuel
        privilege (int): Privilège à retirer
        
    Returns:
        int: Nouveau token sans le privilège
    """
    # ============================================================
    # ÉTAPE 1 : Créer un masque avec NOT (~)
    # ============================================================
    # ~privilege inverse tous les bits du privilège
    # Exemple : privilege = 0b0010, ~privilege = ...11111101
    
    # ============================================================
    # ÉTAPE 2 : Appliquer AND avec le masque
    # ============================================================
    # token & ~privilege "éteint" uniquement le bit du privilège
    
    # TODO: return token & ~privilege
    pass

def can_dump_lsass(token):
    """Vérifie si on peut dumper lsass.exe (dump credentials)"""
    # ============================================================
    # RÈGLE : Besoin de SE_DEBUG_PRIVILEGE
    # ============================================================
    # Utilisez la fonction has_privilege que vous avez créée
    
    # TODO: return has_privilege(token, SE_DEBUG_PRIVILEGE)
    pass

def can_load_rootkit(token):
    """Vérifie si on peut charger un driver malveillant"""
    # ============================================================
    # RÈGLE : Besoin de SE_LOAD_DRIVER_PRIVILEGE
    # ============================================================
    
    # TODO: return has_privilege(token, SE_LOAD_DRIVER_PRIVILEGE)
    pass

def can_backup_system(token):
    """Vérifie si on peut backup tout le système"""
    # ============================================================
    # RÈGLE : Besoin de SE_BACKUP_PRIVILEGE ET SE_RESTORE_PRIVILEGE
    # ============================================================
    # Il faut DEUX privilèges en même temps, utilisez 'and'
    
    # TODO: return (has_privilege(token, SE_BACKUP_PRIVILEGE) and 
    #              has_privilege(token, SE_RESTORE_PRIVILEGE))
    pass

# --- Zone de Test ---
if __name__ == "__main__":
    print("=== Test 1 : Vérification de Privilèges ===")
    token = SE_DEBUG_PRIVILEGE | SE_BACKUP_PRIVILEGE
    print(f"Token actuel : {bin(token)} (0x{token:02x})")
    
    if has_privilege:
        print(f"  Has SE_DEBUG_PRIVILEGE?  {has_privilege(token, SE_DEBUG_PRIVILEGE)}")
        print(f"  Has SE_LOAD_DRIVER?      {has_privilege(token, SE_LOAD_DRIVER_PRIVILEGE)}")
    else:
        print("  [FAIL] Fonction non implémentée.\n")
    
    print("\n=== Test 2 : Ajout de Privilège ===")
    if add_privilege:
        token = add_privilege(token, SE_LOAD_DRIVER_PRIVILEGE)
        print(f"Token après ajout : {bin(token)} (0x{token:02x})")
        print(f"  Has SE_LOAD_DRIVER?  {has_privilege(token, SE_LOAD_DRIVER_PRIVILEGE)}")
    else:
        print("  [FAIL] Fonction non implémentée.\n")
    
    print("\n=== Test 3 : Retrait de Privilège ===")
    if remove_privilege:
        token = remove_privilege(token, SE_BACKUP_PRIVILEGE)
        print(f"Token après retrait : {bin(token)} (0x{token:02x})")
        print(f"  Has SE_BACKUP?  {has_privilege(token, SE_BACKUP_PRIVILEGE)}")
    else:
        print("  [FAIL] Fonction non implémentée.\n")
    
    print("\n=== Test 4 : Actions Malveillantes ===")
    # Token standard utilisateur
    user_token = 0
    print(f"[User Token] : {bin(user_token)}")
    if can_dump_lsass:
        print(f"  Peut dumper lsass? {can_dump_lsass(user_token)}")
    
    # Token avec SE_DEBUG
    debug_token = SE_DEBUG_PRIVILEGE
    print(f"\n[Debug Token] : {bin(debug_token)}")
    if can_dump_lsass:
        print(f"  Peut dumper lsass? {can_dump_lsass(debug_token)}")
    
    # Token admin complet
    admin_token = SE_DEBUG_PRIVILEGE | SE_BACKUP_PRIVILEGE | SE_RESTORE_PRIVILEGE | SE_LOAD_DRIVER_PRIVILEGE
    print(f"\n[Admin Token] : {bin(admin_token)}")
    if can_dump_lsass and can_load_rootkit and can_backup_system:
        print(f"  Peut dumper lsass?     {can_dump_lsass(admin_token)}")
        print(f"  Peut charger rootkit?  {can_load_rootkit(admin_token)}")
        print(f"  Peut backup système?   {can_backup_system(admin_token)}")
