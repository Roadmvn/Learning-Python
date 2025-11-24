# Mission : Vérificateur de Privilèges Windows

## Objectif
Créer un système de vérification de privilèges Windows en utilisant des bit flags. Comprendre comment un malware vérifie s'il a les droits nécessaires pour ses actions.

## Contexte
Sur Windows, chaque processus possède un **Access Token** contenant ses privilèges. Pour effectuer certaines actions dangereuses (injecter du code, dumper des credentials, charger un driver), le malware doit d'abord vérifier s'il possède les privilèges nécessaires.

### Privilèges Windows Simulés
```python
SE_DEBUG_PRIVILEGE       = 1 << 0  # 0001 (Injecter dans processus)
SE_BACKUP_PRIVILEGE      = 1 << 1  # 0010 (Lire fichiers protégés)
SE_RESTORE_PRIVILEGE     = 1 << 2  # 0100 (Écrire fichiers protégés)
SE_SHUTDOWN_PRIVILEGE    = 1 << 3  # 1000 (Éteindre le système)
SE_LOAD_DRIVER_PRIVILEGE = 1 << 4  # ... (Charger driver/rootkit)
```

## Votre Mission
Complétez `checker.py` pour :
1. Vérifier si un token possède un privilège spécifique.
2. Ajouter un privilège à un token.
3. Retirer un privilège d'un token.
4. Vérifier si un malware peut effectuer une action donnée.

## Contraintes
- Utilisez uniquement les opérations bit à bit (`&`, `|`, `~`, `^`, `<<`).
- Un privilège est représenté par un bit unique.
- Un token peut avoir plusieurs privilèges en même temps.

## Actions Malveillantes à Vérifier
```python
# Pour dumper lsass.exe (Mimikatz)
privileges_needed = SE_DEBUG_PRIVILEGE

# Pour installer un rootkit
privileges_needed = SE_LOAD_DRIVER_PRIVILEGE

# Pour backup complet du système
privileges_needed = SE_BACKUP_PRIVILEGE | SE_RESTORE_PRIVILEGE
```

## Exemple
```python
token = SE_DEBUG_PRIVILEGE | SE_BACKUP_PRIVILEGE  # 0011

can_dump_lsass(token)      # True (a SE_DEBUG)
can_load_rootkit(token)    # False (manque SE_LOAD_DRIVER)
```

## Lancement
1. Lancez `python3 checker.py`.
2. Vérifiez que les différents scénarios fonctionnent.
