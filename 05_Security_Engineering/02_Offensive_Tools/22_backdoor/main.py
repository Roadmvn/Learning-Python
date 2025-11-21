#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICE 22: BACKDOOR PERSISTANT
=================================

AVERTISSEMENT CRITIQUE:
Ce code est fourni EXCLUSIVEMENT à des fins éducatives et de recherche en sécurité.
L'utilisation de ces techniques sans autorisation explicite est ILLÉGALE.
Usage autorisé UNIQUEMENT dans des environnements de test isolés avec permission écrite.

Auteur: Formation Cybersécurité
Date: 2025
"""

import socket
import subprocess
import threading
import platform
import base64
import os
import sys
import time
import random
import json
from typing import Dict, List, Optional, Tuple
from pathlib import Path


# ============================================================================
# AVERTISSEMENT ET DISCLAIMERS
# ============================================================================

def afficher_avertissement():
    """Affiche l'avertissement légal et éthique avant toute utilisation."""
    avertissement = """
    ╔════════════════════════════════════════════════════════════════════╗
    ║                   AVERTISSEMENT CRITIQUE                           ║
    ║                                                                    ║
    ║  Ce programme contient des techniques de backdoor et persistance  ║
    ║  qui sont ILLÉGALES sans autorisation explicite.                  ║
    ║                                                                    ║
    ║  Usage STRICTEMENT ÉDUCATIF dans environnements isolés UNIQUEMENT ║
    ║                                                                    ║
    ║  L'utilisation malveillante entraîne:                             ║
    ║  - Poursuites pénales                                             ║
    ║  - Amendes importantes                                            ║
    ║  - Emprisonnement                                                 ║
    ║                                                                    ║
    ║  En continuant, vous confirmez:                                   ║
    ║  1. Avoir l'autorisation écrite pour ces tests                    ║
    ║  2. Être dans un environnement isolé et contrôlé                  ║
    ║  3. Comprendre les implications légales                           ║
    ║  4. Utiliser ces techniques de manière éthique                    ║
    ╚════════════════════════════════════════════════════════════════════╝
    """
    print(avertissement)

    reponse = input("\nConfirmez-vous avoir lu et compris cet avertissement? (OUI/non): ")
    if reponse.upper() != "OUI":
        print("\n[!] Utilisation annulée. Consultez un professionnel de la sécurité.")
        sys.exit(0)


# ============================================================================
# DÉFI 1: SIMPLE REVERSE SHELL
# ============================================================================

class ReverseShell:
    """
    Implémente un reverse shell avec reconnexion automatique.

    ATTENTION: Usage strictement éducatif et avec autorisation.
    """

    def __init__(self, host: str, port: int, reconnect_delay: int = 5):
        """
        Initialise le reverse shell.

        Args:
            host: IP du serveur C2
            port: Port du serveur C2
            reconnect_delay: Délai en secondes avant reconnexion
        """
        # TODO: Stocker les paramètres de connexion
        # TODO: Initialiser le socket
        pass

    def connect(self) -> bool:
        """
        Établit la connexion au serveur C2.

        Returns:
            True si connexion réussie, False sinon
        """
        # TODO: Créer un socket TCP
        # TODO: Se connecter au serveur C2
        # TODO: Gérer les erreurs de connexion
        # TODO: Retourner le statut de connexion
        pass

    def execute_command(self, command: str) -> str:
        """
        Exécute une commande shell et retourne le résultat.

        Args:
            command: Commande à exécuter

        Returns:
            Résultat de la commande
        """
        # TODO: Utiliser subprocess pour exécuter la commande
        # TODO: Capturer stdout et stderr
        # TODO: Gérer les erreurs d'exécution
        # TODO: Retourner le résultat encodé
        pass

    def start(self):
        """Démarre le reverse shell avec reconnexion automatique."""
        # TODO: Boucle de connexion/reconnexion
        # TODO: Recevoir les commandes du serveur
        # TODO: Exécuter et renvoyer les résultats
        # TODO: Gérer la déconnexion et reconnexion
        pass


# ============================================================================
# DÉFI 2: MÉCANISME DE PERSISTANCE
# ============================================================================

class PersistenceManager:
    """Gère les mécanismes de persistance multi-plateformes."""

    def __init__(self):
        """Initialise le gestionnaire de persistance."""
        self.os_type = platform.system()
        self.script_path = os.path.abspath(__file__)

    def install_windows_persistence(self) -> bool:
        """
        Installe la persistance sur Windows via Registry.

        Returns:
            True si installation réussie
        """
        # TODO: Détecter si on est sur Windows
        # TODO: Copier le script dans un emplacement discret
        # TODO: Ajouter une clé Registry Run
        # TODO: Utiliser winreg pour modifier la registry
        # EXEMPLE: HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
        pass

    def install_linux_persistence(self) -> bool:
        """
        Installe la persistance sur Linux via cron.

        Returns:
            True si installation réussie
        """
        # TODO: Détecter si on est sur Linux
        # TODO: Copier le script dans ~/.local/bin ou /tmp
        # TODO: Ajouter une entrée cron pour @reboot
        # TODO: Alternative: créer un service systemd
        pass

    def install_macos_persistence(self) -> bool:
        """
        Installe la persistance sur macOS via Launch Agent.

        Returns:
            True si installation réussie
        """
        # TODO: Détecter si on est sur macOS
        # TODO: Créer un fichier plist Launch Agent
        # TODO: Copier dans ~/Library/LaunchAgents/
        # TODO: Charger le Launch Agent avec launchctl
        pass

    def install(self) -> bool:
        """
        Installe la persistance selon le système d'exploitation.

        Returns:
            True si installation réussie
        """
        # TODO: Détecter l'OS
        # TODO: Appeler la méthode appropriée
        # TODO: Logger l'installation
        # TODO: Retourner le statut
        pass

    def remove(self) -> bool:
        """
        Supprime tous les mécanismes de persistance.

        Returns:
            True si suppression réussie
        """
        # TODO: Supprimer les entrées Registry/cron/LaunchAgent
        # TODO: Supprimer les copies du script
        # TODO: Nettoyer les traces
        # TODO: Retourner le statut
        pass


# ============================================================================
# DÉFI 3: HTTP BEACONING
# ============================================================================

class HTTPBeacon:
    """Implémente un système de beacon HTTP avec jitter."""

    def __init__(self, c2_url: str, interval: int, jitter: float = 0.3):
        """
        Initialise le beacon HTTP.

        Args:
            c2_url: URL du serveur C2
            interval: Intervalle de base entre beacons (secondes)
            jitter: Pourcentage de variation aléatoire (0.0-1.0)
        """
        # TODO: Stocker les paramètres
        # TODO: Initialiser le client HTTP (urllib ou requests)
        # TODO: Préparer les headers HTTP
        pass

    def calculate_jitter_interval(self) -> int:
        """
        Calcule l'intervalle avec jitter aléatoire.

        Returns:
            Intervalle en secondes avec variation aléatoire
        """
        # TODO: Calculer la variation aléatoire
        # TODO: Appliquer le jitter à l'intervalle de base
        # TODO: Retourner l'intervalle randomisé
        pass

    def send_beacon(self) -> Optional[str]:
        """
        Envoie un beacon au serveur C2 et récupère les commandes.

        Returns:
            Commande reçue du C2 ou None
        """
        # TODO: Préparer les données du beacon (hostname, IP, OS, etc.)
        # TODO: Envoyer une requête POST au C2
        # TODO: Parser la réponse pour extraire les commandes
        # TODO: Gérer les erreurs réseau
        # TODO: Retourner la commande ou None
        pass

    def exfiltrate_result(self, command_id: str, result: str) -> bool:
        """
        Exfiltre le résultat d'une commande vers le C2.

        Args:
            command_id: ID de la commande exécutée
            result: Résultat de l'exécution

        Returns:
            True si exfiltration réussie
        """
        # TODO: Encoder le résultat (Base64)
        # TODO: Envoyer au C2 via POST
        # TODO: Gérer les erreurs
        # TODO: Retourner le statut
        pass

    def start(self):
        """Démarre la boucle de beaconing."""
        # TODO: Boucle infinie de beacon
        # TODO: Envoyer beacon et récupérer commandes
        # TODO: Exécuter les commandes reçues
        # TODO: Exfiltrer les résultats
        # TODO: Attendre intervalle avec jitter
        pass


# ============================================================================
# DÉFI 4: COMMAND EXECUTION ENGINE
# ============================================================================

class CommandExecutor:
    """Moteur d'exécution de commandes multi-types."""

    COMMAND_TYPES = {
        'SHELL': 'execute_shell',
        'PYTHON': 'execute_python',
        'DOWNLOAD': 'download_file',
        'UPLOAD': 'upload_file',
        'SYSINFO': 'get_system_info'
    }

    def parse_command(self, command: str) -> Tuple[str, str]:
        """
        Parse une commande au format TYPE:PAYLOAD.

        Args:
            command: Commande au format "TYPE:PAYLOAD"

        Returns:
            Tuple (type, payload)
        """
        # TODO: Splitter la commande
        # TODO: Valider le format
        # TODO: Retourner type et payload
        pass

    def execute_shell(self, payload: str) -> str:
        """
        Exécute une commande shell.

        Args:
            payload: Commande shell à exécuter

        Returns:
            Résultat de la commande
        """
        # TODO: Utiliser subprocess.run()
        # TODO: Capturer stdout et stderr
        # TODO: Gérer les erreurs
        # TODO: Retourner le résultat
        pass

    def execute_python(self, payload: str) -> str:
        """
        Exécute du code Python arbitraire.

        Args:
            payload: Code Python à exécuter

        Returns:
            Résultat de l'exécution
        """
        # TODO: Utiliser exec() avec précaution
        # TODO: Capturer stdout
        # TODO: Gérer les exceptions
        # TODO: Retourner le résultat
        # ATTENTION: exec() est dangereux, valider le code si possible
        pass

    def download_file(self, payload: str) -> str:
        """
        Télécharge un fichier depuis le C2.

        Args:
            payload: URL du fichier à télécharger

        Returns:
            Chemin du fichier téléchargé
        """
        # TODO: Parser l'URL et le chemin destination
        # TODO: Télécharger le fichier
        # TODO: Sauvegarder localement
        # TODO: Retourner le chemin ou erreur
        pass

    def upload_file(self, payload: str) -> str:
        """
        Upload un fichier vers le C2.

        Args:
            payload: Chemin du fichier à uploader

        Returns:
            Confirmation d'upload
        """
        # TODO: Lire le fichier local
        # TODO: Encoder en Base64
        # TODO: Envoyer au C2
        # TODO: Retourner confirmation
        pass

    def get_system_info(self, payload: str = None) -> str:
        """
        Collecte les informations système.

        Returns:
            JSON des informations système
        """
        # TODO: Collecter OS, hostname, IP, user, etc.
        # TODO: Lister les processus en cours
        # TODO: Informations réseau
        # TODO: Retourner en JSON
        pass

    def execute(self, command: str) -> str:
        """
        Exécute une commande selon son type.

        Args:
            command: Commande au format TYPE:PAYLOAD

        Returns:
            Résultat de l'exécution
        """
        # TODO: Parser la commande
        # TODO: Identifier le type
        # TODO: Appeler la méthode appropriée
        # TODO: Retourner le résultat encodé
        pass


# ============================================================================
# DÉFI 5: OBFUSCATION BASIQUE
# ============================================================================

class Obfuscator:
    """Utilitaires d'obfuscation pour backdoors."""

    @staticmethod
    def xor_encode(data: str, key: int = 0x42) -> str:
        """
        Encode une string avec XOR.

        Args:
            data: Données à encoder
            key: Clé XOR

        Returns:
            Données encodées en Base64
        """
        # TODO: Appliquer XOR sur chaque byte
        # TODO: Encoder le résultat en Base64
        # TODO: Retourner la string encodée
        pass

    @staticmethod
    def xor_decode(encoded: str, key: int = 0x42) -> str:
        """
        Décode une string XOR.

        Args:
            encoded: Données encodées en Base64
            key: Clé XOR

        Returns:
            Données décodées
        """
        # TODO: Décoder le Base64
        # TODO: Appliquer XOR pour décoder
        # TODO: Retourner la string originale
        pass

    @staticmethod
    def detect_debugger() -> bool:
        """
        Détecte la présence d'un debugger.

        Returns:
            True si debugger détecté
        """
        # TODO: Vérifier sys.gettrace()
        # TODO: Vérifier les variables d'environnement
        # TODO: Timing checks (debugger ralentit l'exécution)
        # TODO: Retourner True si debugger détecté
        pass

    @staticmethod
    def detect_vm() -> bool:
        """
        Détecte l'exécution dans une VM.

        Returns:
            True si VM détectée
        """
        # TODO: Vérifier les processus suspects (VMware, VirtualBox)
        # TODO: Vérifier les fichiers système caractéristiques
        # TODO: Vérifier le hardware (faible RAM, CPU)
        # TODO: Retourner True si VM détectée
        pass


# ============================================================================
# DÉFI 6: MULTI-HANDLER C2
# ============================================================================

class MultiHandlerC2:
    """Gestionnaire de communication C2 avec multiples fallbacks."""

    def __init__(self, handlers_config: Dict):
        """
        Initialise avec configuration des handlers.

        Args:
            handlers_config: Configuration des handlers avec priorités
        """
        # TODO: Charger la configuration
        # TODO: Trier par priorité
        # TODO: Initialiser les handlers
        pass

    def test_connectivity(self, handler: Dict) -> bool:
        """
        Teste la connectivité d'un handler.

        Args:
            handler: Configuration du handler

        Returns:
            True si connectivité OK
        """
        # TODO: Tester selon le type (HTTP, DNS, ICMP, etc.)
        # TODO: Timeout court pour ne pas bloquer
        # TODO: Retourner le statut
        pass

    def send_via_http(self, data: str) -> Optional[str]:
        """Envoie des données via HTTP."""
        # TODO: Implémenter communication HTTP
        pass

    def send_via_dns(self, data: str) -> Optional[str]:
        """Envoie des données via DNS tunneling."""
        # TODO: Implémenter DNS tunneling basique
        # TODO: Encoder les données dans des requêtes DNS
        pass

    def send_via_icmp(self, data: str) -> Optional[str]:
        """Envoie des données via ICMP tunneling."""
        # TODO: Implémenter ICMP tunneling basique
        # TODO: Encoder les données dans des pings
        pass

    def send(self, data: str) -> Optional[str]:
        """
        Envoie des données via le premier handler disponible.

        Args:
            data: Données à envoyer

        Returns:
            Réponse du C2 ou None
        """
        # TODO: Itérer sur les handlers par priorité
        # TODO: Tester la connectivité
        # TODO: Envoyer via le premier disponible
        # TODO: Fallback si échec
        # TODO: Retourner la réponse
        pass


# ============================================================================
# DÉFI 7: STEALTH ET EVASION
# ============================================================================

class StealthManager:
    """Gestionnaire des techniques de stealth et d'évasion."""

    @staticmethod
    def hide_process():
        """Tente de masquer le processus actuel."""
        # TODO: Renommer le processus (setproctitle)
        # TODO: Process hollowing (avancé, Windows)
        # TODO: Masquer dans la liste des processus
        # NOTE: Très difficile en Python, concept démonstratif
        pass

    @staticmethod
    def clean_logs():
        """Nettoie les logs système de traces du backdoor."""
        # TODO: Identifier les logs à nettoyer selon l'OS
        # TODO: Supprimer les entrées pertinentes
        # TODO: Windows: Event Logs
        # TODO: Linux: /var/log/auth.log, syslog
        # TODO: Gérer les permissions
        pass

    @staticmethod
    def disable_av():
        """
        Tente de désactiver l'antivirus (concept démonstratif).

        ATTENTION: Extrêmement détectable et souvent impossible.
        """
        # TODO: Détecter l'AV installé
        # TODO: Tenter de stopper le service (requiert admin)
        # TODO: Alternative: exclusions ou bypass
        # NOTE: Pour éducation uniquement, très difficile en pratique
        pass


# ============================================================================
# DÉFI 8: KILL SWITCH ET AUTO-DESTRUCTION
# ============================================================================

class KillSwitch:
    """Gère l'auto-destruction et le kill switch."""

    def __init__(self, expiration_date: Optional[str] = None):
        """
        Initialise le kill switch.

        Args:
            expiration_date: Date d'expiration au format YYYY-MM-DD
        """
        # TODO: Stocker la date d'expiration
        # TODO: Initialiser les conditions d'auto-destruction
        pass

    def check_expiration(self) -> bool:
        """
        Vérifie si la date d'expiration est dépassée.

        Returns:
            True si expiré
        """
        # TODO: Comparer la date actuelle avec expiration
        # TODO: Retourner True si expiré
        pass

    def check_conditions(self) -> bool:
        """
        Vérifie toutes les conditions d'auto-destruction.

        Returns:
            True si conditions déclenchées
        """
        # TODO: Vérifier expiration
        # TODO: Vérifier debugger
        # TODO: Vérifier VM
        # TODO: Autres conditions custom
        # TODO: Retourner True si une condition vraie
        pass

    def self_destruct(self):
        """Effectue l'auto-destruction complète du backdoor."""
        # TODO: Supprimer la persistance
        # TODO: Supprimer les fichiers du backdoor
        # TODO: Nettoyer les logs
        # TODO: Effacer les traces réseau
        # TODO: Terminer le processus
        print("[!] AUTO-DESTRUCTION INITIÉE")
        # TODO: Implémenter la destruction
        pass


# ============================================================================
# FONCTION PRINCIPALE ET CLI
# ============================================================================

def main():
    """Fonction principale du backdoor (usage éducatif)."""

    # Afficher l'avertissement obligatoire
    afficher_avertissement()

    print("\n" + "="*70)
    print("EXERCICE 22: BACKDOOR PERSISTANT")
    print("="*70)
    print("\nUsage strictement éducatif et avec autorisation")
    print("\nDéfis disponibles:")
    print("  1. Reverse Shell")
    print("  2. Mécanisme de Persistance")
    print("  3. HTTP Beaconing")
    print("  4. Command Execution Engine")
    print("  5. Obfuscation Basique")
    print("  6. Multi-Handler C2")
    print("  7. Stealth et Evasion")
    print("  8. Kill Switch et Auto-Destruction")

    # TODO: Implémenter la logique selon les arguments CLI
    # TODO: Utiliser argparse pour parser les commandes
    # TODO: Appeler les classes appropriées selon le défi

    print("\n[*] Exercice terminé. Détruisez toutes les traces de test.")


if __name__ == "__main__":
    main()
