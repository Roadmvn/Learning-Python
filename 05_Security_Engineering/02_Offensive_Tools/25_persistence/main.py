#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICE 25: TECHNIQUES DE PERSISTENCE
=======================================

DERNIER EXERCICE - AVERTISSEMENT CRITIQUE:
Ce code implémente des techniques de persistence système.
Usage STRICTEMENT éducatif et autorisé UNIQUEMENT.
Ne JAMAIS déployer sans autorisation explicite écrite.

Félicitations pour avoir atteint le dernier exercice!
Utilisez ces connaissances de manière éthique et professionnelle.

Auteur: Formation Cybersécurité
Date: 2025
"""

import subprocess
import platform
import os
import shutil
import json
import time
from pathlib import Path
from typing import List, Dict, Optional
from datetime import datetime


# ============================================================================
# AVERTISSEMENT FINAL
# ============================================================================

def afficher_avertissement_final():
    """Affiche l'avertissement final pour le dernier exercice."""
    print("""
    ╔══════════════════════════════════════════════════════════════════════╗
    ║              EXERCICE FINAL - TECHNIQUES DE PERSISTENCE              ║
    ║                                                                      ║
    ║  CECI EST LE DERNIER EXERCICE DE LA FORMATION RED TEAMING           ║
    ║                                                                      ║
    ║  Vous avez acquis des connaissances sensibles sur:                   ║
    ║  - Compromission de systèmes                                         ║
    ║  - Exploitation de vulnérabilités                                    ║
    ║  - Maintien d'accès persistant                                       ║
    ║                                                                      ║
    ║  RESPONSABILITÉ PROFESSIONNELLE:                                     ║
    ║  Utilisez ces compétences UNIQUEMENT pour:                           ║
    ║  - Tests de pénétration autorisés                                    ║
    ║  - Amélioration de la sécurité                                       ║
    ║  - Formation d'équipes de défense                                    ║
    ║  - Contribution éthique à la communauté                              ║
    ║                                                                      ║
    ║  JAMAIS pour nuire, compromettre ou attaquer sans autorisation       ║
    ║                                                                      ║
    ║  Votre réputation et liberté dépendent de l'usage éthique            ║
    ╚══════════════════════════════════════════════════════════════════════╝
    """)

    response = input("\nJ'accepte la responsabilité éthique de ces connaissances (OUI): ")
    if response.upper() != "OUI":
        print("\n[!] Exercice annulé. Réfléchissez à vos intentions.")
        exit(0)


# ============================================================================
# DÉFI 1: PERSISTENCE WINDOWS REGISTRY
# ============================================================================

class WindowsRegistryPersistence:
    """Gère la persistence via Windows Registry."""

    @staticmethod
    def install_hkcu_persistence(payload_path: str, key_name: str) -> bool:
        """
        Installe persistence via HKCU Registry.

        Args:
            payload_path: Chemin du payload
            key_name: Nom de la clé Registry

        Returns:
            True si installation réussie
        """
        # TODO: Vérifier qu'on est sur Windows
        # TODO: Copier payload vers emplacement discret
        # TODO: Utiliser winreg pour ajouter clé Run
        # TODO: Path: HKCU\Software\Microsoft\Windows\CurrentVersion\Run
        # TODO: Retourner statut
        pass

    @staticmethod
    def install_hklm_persistence(payload_path: str, key_name: str) -> bool:
        """
        Installe persistence via HKLM Registry (nécessite admin).

        Args:
            payload_path: Chemin du payload
            key_name: Nom de la clé Registry

        Returns:
            True si installation réussie
        """
        # TODO: Vérifier privilèges admin
        # TODO: Copier payload
        # TODO: Ajouter clé HKLM Run
        # TODO: Gérer les erreurs de permissions
        pass

    @staticmethod
    def check_persistence_exists(key_name: str) -> bool:
        """
        Vérifie si persistence Registry existe.

        Args:
            key_name: Nom de la clé à vérifier

        Returns:
            True si existe
        """
        # TODO: Lire Registry Run key
        # TODO: Vérifier si key_name existe
        pass

    @staticmethod
    def remove_persistence(key_name: str) -> bool:
        """
        Supprime persistence Registry.

        Args:
            key_name: Nom de la clé à supprimer

        Returns:
            True si suppression réussie
        """
        # TODO: Supprimer clé de HKCU et HKLM
        # TODO: Supprimer payload copié
        pass


# ============================================================================
# DÉFI 2: SCHEDULED TASKS (WINDOWS)
# ============================================================================

class WindowsScheduledTask:
    """Gère les scheduled tasks Windows."""

    @staticmethod
    def create_task_logon(payload_path: str, task_name: str) -> bool:
        """
        Crée scheduled task déclenchée au logon.

        Args:
            payload_path: Chemin du payload
            task_name: Nom de la task

        Returns:
            True si création réussie
        """
        # TODO: Utiliser schtasks.exe ou PowerShell
        # TODO: Créer task avec trigger AtLogon
        # TODO: Configurer pour exécution SYSTEM si possible
        # TODO: Commande: schtasks /create /tn NAME /tr PATH /sc onlogon
        pass

    @staticmethod
    def create_task_periodic(payload_path: str, task_name: str, interval_minutes: int) -> bool:
        """
        Crée scheduled task périodique.

        Args:
            payload_path: Chemin du payload
            task_name: Nom de la task
            interval_minutes: Intervalle en minutes

        Returns:
            True si création réussie
        """
        # TODO: Créer task avec intervalle
        # TODO: Ex: schtasks /create /tn NAME /tr PATH /sc minute /mo 30
        pass

    @staticmethod
    def remove_task(task_name: str) -> bool:
        """
        Supprime scheduled task.

        Args:
            task_name: Nom de la task

        Returns:
            True si suppression réussie
        """
        # TODO: schtasks /delete /tn NAME /f
        pass


# ============================================================================
# DÉFI 3: SYSTEMD SERVICE (LINUX)
# ============================================================================

class SystemdService:
    """Gère les services systemd."""

    @staticmethod
    def create_service(payload_path: str, service_name: str, user_service: bool = False) -> bool:
        """
        Crée service systemd.

        Args:
            payload_path: Chemin du payload
            service_name: Nom du service
            user_service: Si True, user service, sinon system service

        Returns:
            True si création réussie
        """
        # TODO: Générer fichier .service
        # TODO: Emplacement:
        #   - System: /etc/systemd/system/
        #   - User: ~/.config/systemd/user/
        # TODO: Contenu:
        #   [Unit]
        #   Description=...
        #   [Service]
        #   ExecStart=...
        #   Restart=always
        #   [Install]
        #   WantedBy=multi-user.target
        # TODO: systemctl daemon-reload
        # TODO: systemctl enable service_name
        pass

    @staticmethod
    def start_service(service_name: str) -> bool:
        """
        Démarre service systemd.

        Args:
            service_name: Nom du service

        Returns:
            True si démarrage réussi
        """
        # TODO: systemctl start service_name
        pass

    @staticmethod
    def remove_service(service_name: str) -> bool:
        """
        Supprime service systemd.

        Args:
            service_name: Nom du service

        Returns:
            True si suppression réussie
        """
        # TODO: systemctl stop service_name
        # TODO: systemctl disable service_name
        # TODO: Supprimer fichier .service
        # TODO: systemctl daemon-reload
        pass


# ============================================================================
# DÉFI 4: CRON JOBS (LINUX/MACOS)
# ============================================================================

class CronPersistence:
    """Gère la persistence via cron."""

    @staticmethod
    def install_reboot_cron(payload_path: str, user_cron: bool = True) -> bool:
        """
        Installe cron job @reboot.

        Args:
            payload_path: Chemin du payload
            user_cron: Si True, user crontab, sinon system

        Returns:
            True si installation réussie
        """
        # TODO: Si user_cron:
        #   - Lire crontab actuel avec crontab -l
        #   - Ajouter ligne: @reboot /path/to/payload &
        #   - Réinstaller avec crontab -
        # TODO: Si system:
        #   - Ajouter à /etc/crontab
        pass

    @staticmethod
    def install_periodic_cron(payload_path: str, timing: str, user_cron: bool = True) -> bool:
        """
        Installe cron job périodique.

        Args:
            payload_path: Chemin du payload
            timing: Timing cron (ex: "*/5 * * * *")
            user_cron: User ou system cron

        Returns:
            True si installation réussie
        """
        # TODO: Ajouter ligne avec timing spécifié
        # TODO: Ex: */5 * * * * /path/to/payload
        pass

    @staticmethod
    def remove_cron(payload_path: str) -> bool:
        """
        Supprime cron jobs contenant payload.

        Args:
            payload_path: Chemin du payload

        Returns:
            True si suppression réussie
        """
        # TODO: Lire crontab
        # TODO: Filtrer lignes contenant payload_path
        # TODO: Réinstaller crontab sans ces lignes
        pass


# ============================================================================
# DÉFI 5: LAUNCH AGENTS (MACOS)
# ============================================================================

class LaunchAgentPersistence:
    """Gère les Launch Agents macOS."""

    @staticmethod
    def create_launch_agent(payload_path: str, label: str) -> bool:
        """
        Crée Launch Agent.

        Args:
            payload_path: Chemin du payload
            label: Label du LaunchAgent (ex: com.system.agent)

        Returns:
            True si création réussie
        """
        # TODO: Créer fichier plist
        # TODO: Emplacement: ~/Library/LaunchAgents/{label}.plist
        # TODO: Contenu XML:
        #   <?xml version="1.0" encoding="UTF-8"?>
        #   <plist version="1.0">
        #   <dict>
        #       <key>Label</key><string>{label}</string>
        #       <key>ProgramArguments</key>
        #       <array><string>{payload_path}</string></array>
        #       <key>RunAtLoad</key><true/>
        #       <key>KeepAlive</key><true/>
        #   </dict>
        #   </plist>
        # TODO: launchctl load ~/Library/LaunchAgents/{label}.plist
        pass

    @staticmethod
    def remove_launch_agent(label: str) -> bool:
        """
        Supprime Launch Agent.

        Args:
            label: Label du LaunchAgent

        Returns:
            True si suppression réussie
        """
        # TODO: launchctl unload plist
        # TODO: Supprimer fichier plist
        pass


# ============================================================================
# DÉFI 6: MODIFICATION SHELL INITIALIZATION
# ============================================================================

class ShellInitPersistence:
    """Modifie fichiers d'initialisation shell."""

    @staticmethod
    def modify_shell_init(command: str, shell_file: str = '.bashrc') -> bool:
        """
        Modifie fichier init shell.

        Args:
            command: Commande à injecter
            shell_file: Fichier à modifier (.bashrc, .zshrc, etc.)

        Returns:
            True si modification réussie
        """
        # TODO: Localiser fichier (HOME directory)
        # TODO: Backup du fichier original
        # TODO: Lire contenu actuel
        # TODO: Injecter commande au MILIEU (pas fin pour être discret)
        # TODO: Optionnel: obfusquer la commande
        # TODO: Écrire fichier modifié
        pass

    @staticmethod
    def restore_shell_init(shell_file: str = '.bashrc') -> bool:
        """
        Restaure fichier init depuis backup.

        Args:
            shell_file: Fichier à restaurer

        Returns:
            True si restauration réussie
        """
        # TODO: Vérifier existence du backup
        # TODO: Restaurer depuis backup
        pass


# ============================================================================
# DÉFI 7: SURVEILLANCE ET AUTO-RÉPARATION
# ============================================================================

class PersistenceMonitor:
    """Monitore et répare la persistence."""

    def __init__(self, mechanisms: List[Dict]):
        """
        Initialise le monitor.

        Args:
            mechanisms: Liste des mécanismes installés
        """
        self.mechanisms = mechanisms
        self.repair_count = {}

    def check_mechanism(self, mechanism: Dict) -> bool:
        """
        Vérifie qu'un mécanisme existe.

        Args:
            mechanism: Mécanisme à vérifier

        Returns:
            True si existe
        """
        # TODO: Selon le type:
        #   - registry: vérifier clé existe
        #   - systemd: vérifier service enabled
        #   - cron: vérifier entrée existe
        #   - etc.
        pass

    def repair_mechanism(self, mechanism: Dict) -> bool:
        """
        Répare un mécanisme supprimé.

        Args:
            mechanism: Mécanisme à réparer

        Returns:
            True si réparation réussie
        """
        # TODO: Réinstaller le mécanisme
        # TODO: Logger la réparation
        # TODO: Incrémenter repair_count
        pass

    def monitor_loop(self, interval: int = 300, max_repairs: int = 3):
        """
        Boucle de monitoring avec auto-réparation.

        Args:
            interval: Intervalle en secondes
            max_repairs: Nombre max de réparations par mécanisme
        """
        # TODO: Boucle infinie:
        #   - Vérifier chaque mécanisme
        #   - Si manquant et repairs < max:
        #     * Réparer
        #     * Logger
        #   - Attendre intervalle
        pass


# ============================================================================
# DÉFI 8: FRAMEWORK COMPLET DE PERSISTENCE
# ============================================================================

class PersistenceFramework:
    """Framework complet de gestion de persistence."""

    PROFILES = {
        'stealth': {
            'mechanisms': ['systemd'],  # Un seul, discret
            'monitoring': False,
            'auto_repair': False
        },
        'resilient': {
            'mechanisms': ['systemd', 'cron', 'shell_init'],
            'monitoring': True,
            'auto_repair': True
        },
        'aggressive': {
            'mechanisms': ['systemd', 'cron', 'shell_init', 'registry'],
            'monitoring': True,
            'auto_repair': True
        }
    }

    def __init__(self, profile: str = 'resilient'):
        """
        Initialise le framework.

        Args:
            profile: Profil de persistence
        """
        # TODO: Charger configuration du profil
        # TODO: Détecter OS
        # TODO: Initialiser liste de mécanismes
        pass

    def install_full_persistence(self, payload_path: str, config: Optional[Dict] = None) -> Dict:
        """
        Installe persistence complète.

        Args:
            payload_path: Chemin du payload
            config: Configuration optionnelle

        Returns:
            Rapport d'installation
        """
        # TODO: Détecter OS
        # TODO: Pour chaque mécanisme du profil:
        #   - Installer si compatible avec OS
        #   - Logger succès/échec
        # TODO: Si monitoring activé:
        #   - Démarrer thread de monitoring
        # TODO: Retourner rapport
        pass

    def cleanup_all(self) -> bool:
        """
        Supprime TOUTE la persistence installée.

        Returns:
            True si nettoyage complet réussi
        """
        # TODO: Pour chaque mécanisme installé:
        #   - Arrêter monitoring
        #   - Supprimer mécanisme
        #   - Restaurer fichiers modifiés
        #   - Supprimer payload
        # TODO: Vérifier suppression complète
        # TODO: Retourner statut
        pass

    def generate_report(self) -> str:
        """
        Génère rapport d'installation.

        Returns:
            Rapport textuel
        """
        # TODO: Compiler infos sur:
        #   - Mécanismes installés
        #   - Statut de chaque mécanisme
        #   - Monitoring actif ou non
        #   - Recommandations
        pass

    def verify_persistence(self) -> List[Dict]:
        """
        Vérifie que tous les mécanismes fonctionnent.

        Returns:
            Liste des statuts
        """
        # TODO: Tester chaque mécanisme
        # TODO: Retourner statuts
        pass


# ============================================================================
# FONCTION PRINCIPALE ET CLI
# ============================================================================

def main():
    """Fonction principale - Dernier exercice."""

    afficher_avertissement_final()

    print("\n" + "="*70)
    print("EXERCICE 25: TECHNIQUES DE PERSISTENCE")
    print("="*70)
    print("\n*** DERNIER EXERCICE DE LA FORMATION RED TEAMING ***\n")
    print("Modules disponibles:")
    print("  1. Windows Registry Persistence")
    print("  2. Windows Scheduled Tasks")
    print("  3. Linux Systemd Services")
    print("  4. Cron Jobs (Linux/macOS)")
    print("  5. macOS Launch Agents")
    print("  6. Shell Initialization Modification")
    print("  7. Persistence Monitoring & Auto-Repair")
    print("  8. Complete Persistence Framework")

    # TODO: Implémenter CLI complète avec argparse
    # TODO: Supporter toutes les commandes
    # TODO: Mode dry-run pour simulation
    # TODO: Fonction cleanup accessible facilement

    print("\n[*] FÉLICITATIONS pour avoir atteint le dernier exercice!")
    print("[*] Implémentations complètes dans solution.txt")
    print("\n[!] RAPPEL FINAL: Usage éthique et autorisé UNIQUEMENT")
    print("[!] Toujours implémenter cleanup avant installation")
    print("[!] Ne JAMAIS laisser persistence après tests")

    print("\n" + "="*70)
    print("FIN DE LA FORMATION - 25 EXERCICES COMPLÉTÉS")
    print("="*70)
    print("\nUtilisez ces connaissances pour protéger, pas attaquer.")
    print("Devenez un professionnel de la sécurité respecté et éthique.")
    print("\nBonne continuation dans votre carrière en cybersécurité!")


if __name__ == "__main__":
    main()
