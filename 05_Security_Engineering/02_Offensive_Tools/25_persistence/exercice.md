EXERCICE 25: TECHNIQUES DE PERSISTENCE
======================================

AVERTISSEMENT FINAL CRITIQUE:
Ceci est le DERNIER exercice de la formation red teaming.
Les techniques de persistence sont parmi les plus sensibles.
Usage STRICTEMENT éducatif et autorisé UNIQUEMENT.
Ne JAMAIS implémenter sans autorisation explicite écrite.

Objectif Final:
---------------
Implémenter un framework complet de persistence multi-plateformes avec techniques
de survie, détection, et suppression. Comprendre comment les APT maintiennent l'accès
pour mieux les détecter et s'en défendre.

CECI EST LE DERNIER EXERCICE - SYNTHÈSE DE TOUTES LES CONNAISSANCES ACQUISES.

Défis à Implémenter:
--------------------

1. PERSISTENCE WINDOWS REGISTRY
   - Implémenter persistence via Registry Run keys
   - Supporter HKCU et HKLM (si admin)
   - Copier payload dans emplacement discret
   - Utiliser noms innocents
   - Vérifier et réparer si supprimé
   Input: Chemin du payload, nom de la clé
   Output: Confirmation d'installation

2. SCHEDULED TASKS (WINDOWS)
   - Créer scheduled task pour exécution au logon
   - Créer task pour exécution périodique
   - Supporter déclencheurs multiples:
     * At logon
     * At startup
```python
     * Toutes les X minutes
```
   - Configurer pour exécution avec privilèges SYSTEM
   - Nom de task innocent
   Input: Payload, trigger type, intervalle
   Output: Task créée et planifiée

3. SYSTEMD SERVICE (LINUX)
   - Créer service systemd personnalisé
   - Configurer auto-démarrage (enable)
   - Restart automatique si crash
   - Masquer comme service système légitime
   - Supporter user et system services
   Input: Payload, nom du service
   Output: Service installé et activé

4. CRON JOBS (LINUX/MACOS)
   - Installer cron job @reboot
   - Installer cron job périodique
   - Supporter user et system crontabs
   - Gérer permissions appropriées
   - Vérifier existence et réparer
   Input: Payload, timing (@reboot, */5 * * * *)
   Output: Cron job installé

5. LAUNCH AGENTS (MACOS)
   - Créer plist Launch Agent
   - Installer dans ~/Library/LaunchAgents/
   - Configurer RunAtLoad et KeepAlive
   - Charger avec launchctl
   - Noms de bundle ID légitimes
   Input: Payload, label
   Output: Launch Agent installé et chargé

6. MODIFICATION SHELL INITIALIZATION
   - Modifier .bashrc / .zshrc / .profile
   - Injecter commande discrètement
   - Placer au milieu du fichier (pas fin)
   - Utiliser obfuscation basique
   - Backup du fichier original
   Input: Commande à injecter
   Output: Shell init modifié

7. SURVEILLANCE ET AUTO-RÉPARATION
   - Vérifier périodiquement que persistence existe
   - Réparer automatiquement si supprimée
   - Monitoring multi-mécanismes
   - Alertes si tentative de suppression détectée
   - Fallback vers mécanismes alternatifs
   Input: Liste des mécanismes installés
   Output: Statut et réparations effectuées

8. FRAMEWORK COMPLET DE PERSISTENCE
   - Intégrer tous les mécanismes
   - Installation multi-couches:
```python
     * Primary: systemd/scheduled task
     * Fallback 1: cron/registry
     * Fallback 2: shell init
```
   - Détection automatique de plateforme
   - Mode stealth avec noms légitimes
   - Suppression complète (cleanup)
   - Rapport d'installation
   Input: Configuration de persistence
   Output: Système de persistence multi-couches installé

Exemples d'Utilisation:
-----------------------

# Défi 1: Windows Registry
python main.py install-registry --payload C:\malware.exe --key "SystemUpdate" --hive HKCU

# Défi 2: Scheduled Task
python main.py install-task --payload C:\malware.exe --name "Maintenance" --trigger logon

# Défi 3: Systemd Service
python main.py install-systemd --payload /usr/local/bin/malware --name system-monitor

# Défi 4: Cron Job
python main.py install-cron --payload /usr/local/bin/malware --timing "@reboot"

# Défi 5: Launch Agent (macOS)
python main.py install-launchagent --payload /usr/local/bin/malware --label com.system.agent

# Défi 6: Shell Init
python main.py modify-shell --command "/usr/local/bin/malware &"

# Défi 7: Auto-Repair
python main.py monitor-persistence --interval 300

# Défi 8: Full Framework
python main.py install-full --payload /path/to/payload --profile stealth
python main.py cleanup-all  # Suppression complète

Contraintes:
------------
1. Environnement de TEST ISOLÉ obligatoire
2. Autorisation ÉCRITE requise avant installation
3. Ne JAMAIS installer sur systèmes de production
4. Backup de tous les fichiers modifiés
5. Code commenté en FRANÇAIS
6. Fonction de cleanup complète implémentée
7. Logging de toutes les modifications
8. Mode dry-run pour simulation

Tests de Validation:
--------------------
1. Persistence survit au redémarrage système
2. Auto-réparation fonctionne si mécanisme supprimé
3. Cleanup supprime TOUTES les traces
4. Multi-couches fournit redondance
5. Noms et emplacements discrets
6. Pas d'impact sur performance système
7. Détection minimale par outils de sécurité
8. Réversibilité complète garantie

Configurations de Persistence:
------------------------------

STEALTH (discret):
- Un mécanisme primary (systemd/task)
- Noms très légitimes
- Pas de logging
- Exécution espacée
- Focus: passer inaperçu

RESILIENT (résilient):
- 3+ mécanismes redondants
- Auto-réparation agressive
- Multiple points de persistence
- Vérification fréquente
- Focus: survie maximale

AGGRESSIVE (agressif):
- Tous les mécanismes disponibles
- Kernel-level si possible
- DLL hijacking
- WMI events
- Focus: persistence garantie

Exemple de Configuration JSON:
------------------------------

{
```python
    "profile": "resilient",
    "payload": "/usr/local/bin/malware",
    "mechanisms": [
        {
            "type": "systemd",
            "name": "system-monitor",
            "priority": 1,
            "auto_repair": true
        },
        {
            "type": "cron",
            "timing": "@reboot",
            "priority": 2,
            "auto_repair": true
        },
        {
            "type": "shell_init",
            "file": ".bashrc",
            "priority": 3,
            "auto_repair": false
        }
    ],
    "monitoring": {
        "enabled": true,
        "interval": 300,
        "repair_attempts": 3
    },
    "stealth": {
        "legitimate_names": true,
        "hide_payload": true,
        "clean_logs": false
    }
```
}

Mécanismes de Persistence par OS:
---------------------------------

WINDOWS:
Priority 1: Scheduled Tasks (discret, flexible)
Priority 2: Registry Run Keys (simple, efficace)
Priority 3: Services (nécessite admin, très persistant)
Priority 4: Startup Folder (facile à détecter)
Advanced: WMI Event Subscriptions, DLL Hijacking

LINUX:
Priority 1: systemd services (moderne, standard)
Priority 2: Cron jobs (universel, fiable)
Priority 3: rc.local (legacy mais fonctionne)
Priority 4: .bashrc modification (user-level)
Advanced: kernel modules, LD_PRELOAD

MACOS:
Priority 1: Launch Agents (standard macOS)
Priority 2: Launch Daemons (system-level, requires root)
Priority 3: Login Items (facile mais visible)
Priority 4: .zshrc modification (user-level)
Advanced: Dylib hijacking, Kernel extensions

Script d'Auto-Réparation:
-------------------------

# Exemple de monitoring loop
while True:
```python
    # Vérifier chaque mécanisme
    for mechanism in installed_mechanisms:
        if not check_mechanism_exists(mechanism):
            log_alert(f"Mechanism {mechanism} missing!")
            repair_mechanism(mechanism)

    # Vérifier payload
    if not payload_exists():
        restore_payload_from_backup()

    # Attendre intervalle
    time.sleep(monitoring_interval)

```
Suppression Complète (Cleanup):
-------------------------------

```python
def cleanup_all_persistence():
    """Supprime TOUTES les traces de persistence."""

    # 1. Supprimer services/tasks
    remove_systemd_services()
    remove_scheduled_tasks()
    remove_cron_jobs()
    remove_launch_agents()

    # 2. Nettoyer Registry (Windows)
    remove_registry_keys()

    # 3. Restaurer fichiers modifiés
    restore_shell_init_files()

    # 4. Supprimer payload
    remove_payload_files()

    # 5. Nettoyer logs
    clean_installation_logs()

    # 6. Vérifier suppression complète
    verify_complete_removal()

    print("[+] Persistence complètement supprimée")

```
Détection de Vos Mécanismes:
----------------------------

Après implémentation, créez aussi des détecteurs:

1. Registry Monitor (Windows):
   - Monitor HKCU/HKLM Run keys
   - Alert sur nouvelles entrées

2. Systemd Monitor (Linux):
   - List enabled services
   - Detect suspicious service names

3. Cron Monitor:
   - Parse all crontabs
   - Detect suspicious commands

4. Baseline Comparison:
   - Create baseline of legitimate persistence
   - Alert on deviations

5. File Integrity:
   - Monitor shell init files
   - Detect modifications

Ressources:
-----------
- MITRE ATT&CK: Persistence Techniques (T1543, T1053, etc.)
- Windows Sysinternals: Autoruns
- systemd documentation
- Apple launchd documentation
- Incident Response playbooks

Notes Importantes:
------------------
- TOUJOURS avoir fonction de cleanup
- JAMAIS laisser persistence après tests
- Documenter TOUTES les modifications
- Tester cleanup avant installation
- Backup de tout fichier modifié
- Environnement de test ISOLÉ obligatoire

RAPPEL ÉTHIQUE FINAL:
=====================

Ceci est le DERNIER exercice de cette formation intensive.

Vous avez maintenant les connaissances pour:
- Compromettre des systèmes (exercices 1-15)
- Exploiter des vulnérabilités (exercices 16-21)
- Maintenir l'accès de manière persistante (exercices 22-25)

GRANDE RESPONSABILITÉ:
- Utilisez ces connaissances pour PROTÉGER, pas ATTAQUER
- Toujours de manière ÉTHIQUE et LÉGALE
- Avec AUTORISATION explicite
- Pour AMÉLIORER la sécurité

Votre carrière professionnelle dépend de l'usage éthique de ces compétences.

Félicitations pour avoir complété les 25 exercices!
Devenez un professionnel de la sécurité respecté et éthique.

La formation est terminée.
La responsabilité commence maintenant.
