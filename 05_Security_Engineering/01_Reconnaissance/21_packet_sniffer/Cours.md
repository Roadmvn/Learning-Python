# Exercice 21 - Packet Sniffer

## Objectifs

Maîtriser la capture et l'analyse de paquets réseau en utilisant Scapy, une bibliothèque Python puissante pour la manipulation et l'analyse de protocoles réseau.

- Capturez des paquets réseau en temps réel
- Analysez les couches TCP/IP (Ethernet, IP, TCP, UDP)
- Filtrez les paquets selon des critères spécifiques
- Extraites et décortifiez les données utiles (adresses IP, ports, protocoles)
- Inspectez les requêtes HTTP pour comprendre les en-têtes et données applicatives
- Utilisez les filtres BPF (Berkeley Packet Filter) pour ciblage précis
- Implémentez l'analyse des protocoles avec décodage de données

## Concepts Clés

### Scapy Library
Bibliothèque Python pour la manipulation interactive et l'analyse des paquets réseau. Permet de construire, envoyer, capturer et analyser les paquets.

### Capture de Paquets
Utilisation de `sniff()` pour intercepter les paquets qui transitent sur l'interface réseau. Nécessite des privilèges root/administrateur pour accéder aux interfaces réseau brutes.

### Couches Réseau (OSI)
- **Couche 2 (Liaison)** : Ethernet - adresses MAC
- **Couche 3 (Réseau)** : IP - adresses IPv4/IPv6
- **Couche 4 (Transport)** : TCP/UDP - ports et numéros de séquence
- **Couche 7 (Application)** : HTTP, DNS, etc.

### Filtrage BPF
Syntaxe de filtrage pour cibler les paquets (ex: "tcp port 80", "ip src 192.168.1.1")

### Analyse Protocole
Extraction et interprétation des champs de chaque couche pour reconstuire les communications.

### Extraction de Données
Récupération des informations pertinentes : adresses IP, ports, flags TCP, données applicatives.

### Captur en Direct
Analyse en temps réel avec callbacks sur chaque paquet capturé.

## Avertissements Critiques

AVERTISSEMENT LÉGAL: Ce type de code nécessite des considérations légales importantes :

- **Privilèges Root/Admin** : Seul un administrateur système peut capturer les paquets
- **Usage Légal Uniquement** : Capturer le trafic d'autres utilisateurs sans consentement est illégal
- **Propre Réseau** : Utilisez cette technique UNIQUEMENT sur votre propre réseau ou avec permission explicite
- **Responsabilité** : L'utilisateur assume 100% de la responsabilité des actions et conséquences légales
- **Éthique** : À ne pas utiliser pour l'espionnage, l'interception de données sensibles ou le vol d'information

## Installation

```bash
# Installer Scapy
pip install scapy

# Sur macOS avec Homebrew pour compatibilité complète
brew install libpcap
```

## Notes de Sécurité

Ce code démontre les principes du red teaming et de la sécurité réseau à des fins éducatives. Les techniques présentées peuvent être utilisées pour :

- Diagnostiquer les problèmes réseau
- Apprendre comment les protocoles fonctionnent
- Détecter les menaces sur votre propre réseau
- Développer des défenses contre les attaques réseau

Ne les utilisez JAMAIS pour :

- Intercepter les données d'autres utilisateurs
- Voler des credentials ou informations sensibles
- Perturber les communications réseau
- Violer la vie privée ou la loi
