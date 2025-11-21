#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICE 23: PAYLOAD ENCODER
=============================

AVERTISSEMENT:
Ce code est fourni EXCLUSIVEMENT à des fins éducatives pour comprendre
les techniques d'évasion et améliorer la détection de malware.
Usage STRICTEMENT éducatif et avec autorisation.

Auteur: Formation Cybersécurité
Date: 2025
"""

import base64
import binascii
import random
import string
import json
import hashlib
from typing import List, Dict, Tuple, Optional, Union
from datetime import datetime


# ============================================================================
# AVERTISSEMENT ÉTHIQUE
# ============================================================================

def afficher_avertissement():
    """Affiche l'avertissement sur l'usage éthique."""
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║              ENCODEUR DE PAYLOADS - USAGE ÉDUCATIF           ║
    ║                                                              ║
    ║  Ces techniques sont pour COMPRENDRE et DÉTECTER les         ║
    ║  méthodes d'évasion d'antivirus.                             ║
    ║                                                              ║
    ║  NE JAMAIS utiliser pour:                                    ║
    ║  - Encoder des malwares réels                                ║
    ║  - Contourner des protections sans autorisation              ║
    ║  - Activités illégales                                       ║
    ║                                                              ║
    ║  Utilisez UNIQUEMENT pour:                                   ║
    ║  - Formation en détection de malware                         ║
    ║  - Tests de sécurité autorisés                               ║
    ║  - Recherche académique                                      ║
    ╚══════════════════════════════════════════════════════════════╝
    """)


# ============================================================================
# DÉFI 1: ENCODEURS BASIQUES
# ============================================================================

class BasicEncoders:
    """Collection d'encodeurs basiques réversibles."""

    @staticmethod
    def encode_base64(data: Union[str, bytes]) -> str:
        """
        Encode en Base64.

        Args:
            data: Données à encoder (string ou bytes)

        Returns:
            String Base64 encodée
        """
        # TODO: Convertir en bytes si nécessaire
        # TODO: Encoder en Base64
        # TODO: Retourner la string encodée
        pass

    @staticmethod
    def decode_base64(encoded: str) -> bytes:
        """
        Décode depuis Base64.

        Args:
            encoded: String Base64 encodée

        Returns:
            Données décodées en bytes
        """
        # TODO: Décoder le Base64
        # TODO: Gérer les erreurs de padding
        # TODO: Retourner les bytes décodés
        pass

    @staticmethod
    def encode_hex(data: Union[str, bytes]) -> str:
        """
        Encode en hexadécimal.

        Args:
            data: Données à encoder

        Returns:
            String hexadécimale
        """
        # TODO: Convertir en bytes si nécessaire
        # TODO: Encoder en hexadécimal
        # TODO: Retourner la string hex
        pass

    @staticmethod
    def decode_hex(encoded: str) -> bytes:
        """
        Décode depuis hexadécimal.

        Args:
            encoded: String hexadécimale

        Returns:
            Données décodées
        """
        # TODO: Décoder l'hexadécimal
        # TODO: Gérer les erreurs
        # TODO: Retourner les bytes
        pass

    @staticmethod
    def encode_rot13(data: str) -> str:
        """
        Encode avec ROT13 (lettres seulement).

        Args:
            data: String à encoder

        Returns:
            String ROT13 encodée
        """
        # TODO: Appliquer ROT13 sur les lettres
        # TODO: Préserver les non-lettres
        # TODO: Gérer majuscules et minuscules
        pass

    @staticmethod
    def decode_rot13(encoded: str) -> str:
        """
        Décode ROT13 (ROT13 est son propre inverse).

        Args:
            encoded: String ROT13 encodée

        Returns:
            String décodée
        """
        # TODO: Appliquer ROT13 (identique à encode)
        pass

    @staticmethod
    def encode_url(data: str) -> str:
        """
        Encode en URL encoding.

        Args:
            data: String à encoder

        Returns:
            String URL encodée
        """
        # TODO: Utiliser urllib.parse.quote
        # TODO: Encoder les caractères spéciaux
        pass

    @staticmethod
    def decode_url(encoded: str) -> str:
        """
        Décode URL encoding.

        Args:
            encoded: String URL encodée

        Returns:
            String décodée
        """
        # TODO: Utiliser urllib.parse.unquote
        pass


# ============================================================================
# DÉFI 2: ENCODEUR XOR
# ============================================================================

class XOREncoder:
    """Encodeur XOR avec support de clés multi-bytes."""

    @staticmethod
    def generate_random_key(length: int = 16) -> bytes:
        """
        Génère une clé XOR aléatoire.

        Args:
            length: Longueur de la clé en bytes

        Returns:
            Clé aléatoire
        """
        # TODO: Générer des bytes aléatoires
        # TODO: Retourner la clé
        pass

    @staticmethod
    def xor_encode(data: bytes, key: bytes) -> bytes:
        """
        Encode avec XOR.

        Args:
            data: Données à encoder
            key: Clé XOR (répétée si nécessaire)

        Returns:
            Données XOR encodées
        """
        # TODO: Appliquer XOR byte par byte
        # TODO: Répéter la clé si plus courte que les données
        # TODO: Retourner le résultat
        pass

    @staticmethod
    def xor_decode(encoded: bytes, key: bytes) -> bytes:
        """
        Décode XOR (identique à encode).

        Args:
            encoded: Données encodées
            key: Clé XOR

        Returns:
            Données décodées
        """
        # TODO: XOR est son propre inverse
        # TODO: Appeler xor_encode
        pass

    @staticmethod
    def encode_with_metadata(data: Union[str, bytes], key: Optional[bytes] = None) -> Dict:
        """
        Encode avec XOR et retourne métadonnées.

        Args:
            data: Données à encoder
            key: Clé optionnelle (générée si None)

        Returns:
            Dictionnaire avec données encodées et métadonnées
        """
        # TODO: Générer clé si non fournie
        # TODO: Convertir data en bytes si nécessaire
        # TODO: Encoder avec XOR
        # TODO: Retourner dict avec encoded data, key, taille, etc.
        pass


# ============================================================================
# DÉFI 3: ENCODAGE MULTI-COUCHES
# ============================================================================

class MultiLayerEncoder:
    """Système d'encodage multi-couches empilables."""

    AVAILABLE_ENCODERS = {
        'base64': (BasicEncoders.encode_base64, BasicEncoders.decode_base64),
        'hex': (BasicEncoders.encode_hex, BasicEncoders.decode_hex),
        'rot13': (BasicEncoders.encode_rot13, BasicEncoders.decode_rot13),
        'xor': (XOREncoder.xor_encode, XOREncoder.xor_decode),
    }

    def __init__(self):
        """Initialise l'encodeur multi-couches."""
        self.layers = []
        self.xor_keys = {}

    def add_layer(self, encoder_type: str, **kwargs):
        """
        Ajoute une couche d'encodage.

        Args:
            encoder_type: Type d'encodeur ('base64', 'xor', etc.)
            **kwargs: Arguments pour l'encodeur (ex: key pour XOR)
        """
        # TODO: Valider que l'encodeur existe
        # TODO: Ajouter la couche à la liste
        # TODO: Stocker les paramètres (comme clé XOR)
        pass

    def encode(self, data: Union[str, bytes]) -> Tuple[bytes, Dict]:
        """
        Encode avec toutes les couches empilées.

        Args:
            data: Données à encoder

        Returns:
            Tuple (données encodées, métadonnées de décodage)
        """
        # TODO: Convertir data en bytes si nécessaire
        # TODO: Appliquer chaque couche séquentiellement
        # TODO: Stocker les métadonnées de chaque couche
        # TODO: Retourner résultat final et métadonnées
        pass

    def decode(self, encoded_data: bytes, metadata: Dict) -> bytes:
        """
        Décode en inversant les couches.

        Args:
            encoded_data: Données encodées
            metadata: Métadonnées de décodage

        Returns:
            Données originales
        """
        # TODO: Lire les couches depuis métadonnées
        # TODO: Appliquer les decoders en ordre inverse
        # TODO: Retourner les données originales
        pass

    def get_encoding_metadata(self) -> Dict:
        """
        Retourne les métadonnées d'encodage.

        Returns:
            Dictionnaire de métadonnées
        """
        # TODO: Compiler info sur les couches
        # TODO: Inclure clés XOR si utilisées
        # TODO: Timestamp, ordre des couches, etc.
        pass


# ============================================================================
# DÉFI 4: GÉNÉRATEUR DE DECODER STUB
# ============================================================================

class DecoderStubGenerator:
    """Génère le code de décodage automatique."""

    @staticmethod
    def generate_python_decoder(metadata: Dict, encoded_payload: bytes) -> str:
        """
        Génère un script Python standalone pour décoder.

        Args:
            metadata: Métadonnées d'encodage
            encoded_payload: Payload encodé

        Returns:
            Code Python du decoder
        """
        # TODO: Générer les imports nécessaires
        # TODO: Inclure le payload encodé (en Base64 dans le code)
        # TODO: Générer le code de décodage selon les couches
        # TODO: Retourner le script complet
        pass

    @staticmethod
    def generate_python_oneliner(metadata: Dict, encoded_payload: bytes) -> str:
        """
        Génère un one-liner Python pour décoder et exécuter.

        Args:
            metadata: Métadonnées d'encodage
            encoded_payload: Payload encodé

        Returns:
            One-liner Python
        """
        # TODO: Créer une version compacte du decoder
        # TODO: Utiliser exec() pour exécution directe
        # TODO: Minimiser la taille
        pass

    @staticmethod
    def generate_powershell_decoder(metadata: Dict, encoded_payload: bytes) -> str:
        """
        Génère un script PowerShell pour décoder.

        Args:
            metadata: Métadonnées d'encodage
            encoded_payload: Payload encodé

        Returns:
            Script PowerShell du decoder
        """
        # TODO: Générer le code PowerShell
        # TODO: Utiliser [System.Convert]::FromBase64String pour décodage
        # TODO: Implémenter XOR si nécessaire
        # TODO: Exécuter le payload décodé
        pass


# ============================================================================
# DÉFI 5: OBFUSCATION DE DECODER
# ============================================================================

class DecoderObfuscator:
    """Obfusque le code du decoder pour éviter détection."""

    @staticmethod
    def randomize_variable_names(code: str) -> str:
        """
        Remplace les noms de variables par des noms aléatoires.

        Args:
            code: Code source à obfusquer

        Returns:
            Code avec variables renommées
        """
        # TODO: Identifier les variables dans le code
        # TODO: Générer des noms aléatoires
        # TODO: Remplacer dans le code
        # TODO: Retourner le code obfusqué
        pass

    @staticmethod
    def insert_junk_code(code: str) -> str:
        """
        Insère du dead code / junk code.

        Args:
            code: Code source

        Returns:
            Code avec junk code inséré
        """
        # TODO: Générer des lignes de code inutiles mais valides
        # TODO: Insérer à des endroits stratégiques
        # TODO: Préserver la fonctionnalité
        pass

    @staticmethod
    def split_strings(code: str) -> str:
        """
        Fragmente les strings suspectes.

        Args:
            code: Code source

        Returns:
            Code avec strings fragmentées
        """
        # TODO: Identifier les strings dans le code
        # TODO: Splitter et reconstituer avec concat
        # TODO: Ex: "exec" devient "ex" + "ec"
        pass

    @staticmethod
    def use_indirection(code: str) -> str:
        """
        Utilise l'indirection pour masquer les appels.

        Args:
            code: Code source

        Returns:
            Code avec indirection
        """
        # TODO: Remplacer exec() par getattr(__builtins__, 'exec')
        # TODO: Utiliser eval() de façon indirecte
        # TODO: Masquer les imports sensibles
        pass

    @staticmethod
    def obfuscate_full(code: str) -> str:
        """
        Applique toutes les techniques d'obfuscation.

        Args:
            code: Code source

        Returns:
            Code complètement obfusqué
        """
        # TODO: Appliquer toutes les techniques
        # TODO: Dans un ordre optimal
        # TODO: Retourner le résultat
        pass


# ============================================================================
# DÉFI 6: ENCODAGE POLYMORPHIQUE
# ============================================================================

class PolymorphicEncoder:
    """Génère des encodages uniques à chaque exécution."""

    @staticmethod
    def randomize_layer_order(layers: List[str]) -> List[str]:
        """
        Randomise l'ordre des couches d'encodage.

        Args:
            layers: Liste des couches à appliquer

        Returns:
            Liste randomisée
        """
        # TODO: Copier la liste
        # TODO: Randomiser l'ordre avec random.shuffle
        # TODO: S'assurer que l'ordre est valide
        pass

    @staticmethod
    def add_random_padding(data: bytes) -> Tuple[bytes, int]:
        """
        Ajoute du padding aléatoire.

        Args:
            data: Données à padder

        Returns:
            Tuple (données paddées, taille du padding)
        """
        # TODO: Générer padding aléatoire
        # TODO: Ajouter au début ou à la fin des données
        # TODO: Retourner données + taille padding pour suppression
        pass

    @staticmethod
    def generate_unique_encoding(payload: Union[str, bytes]) -> Dict:
        """
        Génère un encodage unique du payload.

        Args:
            payload: Payload à encoder

        Returns:
            Dictionnaire avec payload encodé et métadonnées
        """
        # TODO: Choisir aléatoirement 2-4 couches d'encodage
        # TODO: Randomiser l'ordre
        # TODO: Générer clés XOR aléatoires
        # TODO: Ajouter padding aléatoire
        # TODO: Encoder avec cette configuration unique
        # TODO: Retourner tout avec métadonnées
        pass

    @staticmethod
    def generate_multiple_variants(payload: Union[str, bytes], count: int = 5) -> List[Dict]:
        """
        Génère plusieurs variantes polymorphiques.

        Args:
            payload: Payload à encoder
            count: Nombre de variantes

        Returns:
            Liste de variantes encodées
        """
        # TODO: Générer count variantes uniques
        # TODO: Chacune avec configuration différente
        # TODO: Vérifier que signatures sont différentes
        pass


# ============================================================================
# DÉFI 7: TECHNIQUES ANTI-AV
# ============================================================================

class AntiAVTechniques:
    """Techniques d'évasion d'antivirus."""

    @staticmethod
    def fragment_payload(payload: bytes, chunk_size: int = 64) -> List[bytes]:
        """
        Fragmente le payload en chunks.

        Args:
            payload: Payload à fragmenter
            chunk_size: Taille des chunks

        Returns:
            Liste de chunks
        """
        # TODO: Diviser le payload en chunks
        # TODO: Retourner la liste de fragments
        pass

    @staticmethod
    def generate_reassembly_code(chunks: List[bytes]) -> str:
        """
        Génère le code pour réassembler les chunks.

        Args:
            chunks: Fragments du payload

        Returns:
            Code Python de réassemblage
        """
        # TODO: Générer code qui reconstitue le payload
        # TODO: Encoder chaque chunk
        # TODO: Créer code de reconstitution
        pass

    @staticmethod
    def add_time_delay(decoder_code: str, delay_seconds: int = 5) -> str:
        """
        Ajoute un délai avant décodage (anti-sandbox).

        Args:
            decoder_code: Code du decoder
            delay_seconds: Délai en secondes

        Returns:
            Code avec délai
        """
        # TODO: Insérer time.sleep() au début
        # TODO: Ou vérifier timestamp système
        # TODO: Retourner code modifié
        pass

    @staticmethod
    def add_environment_checks(decoder_code: str) -> str:
        """
        Ajoute des vérifications d'environnement.

        Args:
            decoder_code: Code du decoder

        Returns:
            Code avec checks anti-sandbox
        """
        # TODO: Ajouter vérifications:
        # - Nombre de processeurs (sandbox souvent < 2)
        # - RAM disponible (sandbox souvent < 4GB)
        # - Uptime système (sandbox souvent < 10 min)
        # - Présence de fichiers/processus VM
        # TODO: Sortir si environnement suspect
        pass

    @staticmethod
    def encrypt_payload(payload: bytes, password: str) -> Tuple[bytes, bytes]:
        """
        Chiffre le payload avec AES (concept).

        Args:
            payload: Payload à chiffrer
            password: Mot de passe

        Returns:
            Tuple (payload chiffré, salt/IV)
        """
        # TODO: Utiliser cryptography.fernet ou AES
        # TODO: Dériver clé depuis password
        # TODO: Chiffrer le payload
        # TODO: Retourner chiffré + métadonnées crypto
        pass


# ============================================================================
# DÉFI 8: FRAMEWORK COMPLET D'ENCODAGE
# ============================================================================

class EncodingFramework:
    """Framework complet intégrant tous les composants."""

    PROFILES = {
        'stealth': {
            'layers': ['base64', 'xor'],
            'obfuscation_level': 'low',
            'anti_av': ['delay'],
            'polymorphic': False
        },
        'balanced': {
            'layers': ['xor', 'base64', 'rot13'],
            'obfuscation_level': 'medium',
            'anti_av': ['delay', 'env_check'],
            'polymorphic': True
        },
        'aggressive': {
            'layers': ['xor', 'base64', 'hex', 'rot13', 'xor'],
            'obfuscation_level': 'high',
            'anti_av': ['fragment', 'delay', 'env_check', 'encrypt'],
            'polymorphic': True
        }
    }

    def __init__(self, profile: str = 'balanced'):
        """
        Initialise le framework avec un profil.

        Args:
            profile: Profil à utiliser (stealth/balanced/aggressive)
        """
        # TODO: Charger la configuration du profil
        # TODO: Initialiser les composants nécessaires
        pass

    def encode_payload(self, payload: Union[str, bytes], payload_type: str = 'python') -> Dict:
        """
        Encode un payload avec le profil configuré.

        Args:
            payload: Payload à encoder
            payload_type: Type (python/shellcode/powershell/bash)

        Returns:
            Dictionnaire avec résultats et métadonnées
        """
        # TODO: Appliquer les couches d'encodage du profil
        # TODO: Appliquer les techniques anti-AV
        # TODO: Générer le decoder approprié
        # TODO: Obfusquer selon le niveau
        # TODO: Appliquer polymorphisme si activé
        # TODO: Compiler tout et retourner
        pass

    def generate_report(self, encoding_result: Dict) -> str:
        """
        Génère un rapport sur l'encodage effectué.

        Args:
            encoding_result: Résultat de encode_payload

        Returns:
            Rapport textuel
        """
        # TODO: Lister les techniques appliquées
        # TODO: Tailles avant/après
        # TODO: Hash du payload encodé
        # TODO: Métadonnées utiles
        pass

    def save_output(self, encoding_result: Dict, output_path: str):
        """
        Sauvegarde le payload encodé et métadonnées.

        Args:
            encoding_result: Résultat de encode_payload
            output_path: Chemin de sortie
        """
        # TODO: Sauvegarder le payload encodé
        # TODO: Sauvegarder le decoder
        # TODO: Sauvegarder les métadonnées JSON
        # TODO: Sauvegarder le rapport
        pass


# ============================================================================
# FONCTION PRINCIPALE ET CLI
# ============================================================================

def main():
    """Fonction principale avec interface CLI."""

    afficher_avertissement()

    print("\n" + "="*70)
    print("EXERCICE 23: PAYLOAD ENCODER")
    print("="*70)
    print("\nUsage strictement éducatif pour comprendre les techniques d'évasion")
    print("\nDéfis disponibles:")
    print("  1. Encodeurs Basiques (Base64, Hex, ROT13, URL)")
    print("  2. Encodeur XOR avec clés")
    print("  3. Encodage Multi-Couches")
    print("  4. Générateur de Decoder Stub")
    print("  5. Obfuscation de Decoder")
    print("  6. Encodage Polymorphique")
    print("  7. Techniques Anti-AV")
    print("  8. Framework Complet d'Encodage")

    # TODO: Implémenter CLI avec argparse
    # TODO: Supporter toutes les commandes décrites dans exercice.txt
    # TODO: Exemples:
    #   - encode-base64, encode-xor, encode-multi
    #   - generate-decoder, obfuscate-decoder
    #   - encode-polymorphic, encode-antiv
    #   - encode (framework complet)

    # Exemple d'utilisation des classes
    print("\n[*] Exemple: Encodage Base64")
    test_payload = "print('Hello from encoded payload')"
    encoded = BasicEncoders.encode_base64(test_payload)
    print(f"Original: {test_payload}")
    print(f"Encodé: {encoded}")

    print("\n[*] Les implémentations complètes sont dans solution.txt")


if __name__ == "__main__":
    main()
