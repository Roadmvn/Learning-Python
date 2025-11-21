# Exercice 18 : Reverse Shell en Python

## Objectifs d'Apprentissage

- Comprendre l'architecture et les principes d'une reverse shell
- Maîtriser les communications socket bidirectionnelles
- Implémenter un handler (serveur écouteur) et un payload (client)
- Exécuter des commandes système via une connexion réseau
- Transmettre l'output (stdout/stderr) via le réseau
- Comprendre les techniques de persistance basique
- Implémenter l'obfuscation et le masquage de processus
- Appliquer les concepts au red teaming et test de pénétration
- Comprendre les implications de sécurité et les mécanismes de défense

## Avertissement Éthique Majeur

**ÉDUCATIF UNIQUEMENT - ENVIRONNEMENTS AUTORISÉS UNIQUEMENT**

Cette matière couvre des techniques avancées de cybersécurité offensives. Les reverse shells sont utilisées pour:
- Le red teaming autorisé et les tests de pénétration
- L'évaluation de sécurité avec consentement explicite
- L'apprentissage en environnement contrôlé/sandbox

**INTERDICTIONS ABSOLUES**:
- JAMAIS utiliser sur des systèmes sans autorisation écrite
- JAMAIS sur des réseaux ou données d'autres personnes
- JAMAIS pour l'accès non autorisé (c'est CRIMINEL)
- JAMAIS pour le vol de données ou sabotage
- Comprendre que l'utilisation non autorisée peut entraîner:
  - Poursuites judiciaires criminelles graves
  - Prison jusqu'à plusieurs années
  - Amendes substantielles
  - Antécédents judiciaires permanents

## Concepts Clés

### Reverse Shell Concept

Une reverse shell est une technique offensiv où le système cible établit une connexion **sortante** vers un attaquant, plutôt que d'attendre une connexion entrante. C'est l'inverse de la ssh/telnet traditionnelle.

```
Architecture Reverse Shell:

Attaquant (Handler)          Système Cible (Payload)
├── Socket écoute              ├── Exécution payload
├── Port X ouvert              ├── Établit connexion TCP
├── Attend connexion           ├── Se connecte à attaquant:X
├── [Client branché!]<---------|-- Connexion établie
├── Interprète commandes       ├── Reçoit commandes
└── Envoie résultats    ------->-- Exécute + retourne output
```

**Pourquoi c'est puissant**:
- Contourne les pare-feu (connexion sortante souvent autorisée)
- Pas d'écoute sur le système cible (discret)
- Attaquant gardient le contrôle complet
- Communication bidirectionnelle temps réel

### Client/Serveur Inversé

Contrairement au modèle traditionnel client-serveur:

```
Modèle Traditionnel:              Reverse Shell:
Client → Initie connexion         Attaquant (Handler) → Écoute
Server → Écoute                   Cible (Payload) → Initie connexion
```

**Concept clé**: Le "serveur" inversé (attaquant) écoute, tandis que le "client" inversé (cible) établit la connexion.

### Exécution de Commandes

Les commandes sont exécutées via:
1. Réception de commandes sur la socket
2. Exécution via `subprocess` ou `os.system()`
3. Capture de stdout/stderr
4. Transmission des résultats via la socket

```python
Flux Exécution:
1. Attaquant envoie: "whoami"
2. Payload reçoit "whoami"
3. subprocess.Popen() exécute la commande
4. Capture stdout + stderr
5. Envoie résultats à l'attaquant
6. Boucle jusqu'à "exit"
```

### Transmission Output

L'output doit être sérialisé pour transmission réseau:

```
Données → Encodage UTF-8 → Transmission TCP → Décodage → Affichage

Gestion:
- Timeouts (commande qui ne répond pas)
- Caractères spéciaux (encodage/décodage)
- Lignes longues (buffering)
- Erreurs vs sortie standard
```

### Handler (Listener)

Le handler est le serveur d'écoute côté attaquant:

```
Handler Responsabilités:
├── Créer socket serveur
├── Écouter sur port spécifique
├── Accepter connexions (payload)
├── Boucle interactive:
│   ├── Lire input utilisateur (commande)
│   ├── Envoyer via socket
│   ├── Attendre réponse
│   ├── Afficher résultats
│   └── Repeat
└── Gestion d'erreurs et fermeture
```

### Payload (Client)

Le payload est le client exécuté sur le système cible:

```
Payload Responsabilités:
├── Établir connexion TCP à attaquant
├── Boucle infinie:
│   ├── Attendre commande depuis socket
│   ├── Exécuter commande (subprocess)
│   ├── Capturer stdout + stderr
│   ├── Envoyer résultats via socket
│   └── Repeat
├── Gestion d'erreurs silencieuse
└── Persistance (optionnel)
```

### Amélioration 1 : Persistance Basique

Faire persister le payload après redémarrage:

```
Techniques de Persistance:
├── Planificateur (cron/task scheduler)
│   └── Redémarrer payload à intervals réguliers
├── Répertoires de démarrage
│   └── Placer dans ~/.bashrc, ~/.profile, etc.
├── Tâches planifiées système
│   └── Windows: Task Scheduler, Linux: cron
├── Variables d'environnement
│   └── Injecter dans profils shell
└── Reconnaissance de démarrage
    └── Attendre reconnexion si déconnecté
```

### Amélioration 2 : Obfuscation

Masquer le payload pour éviter la détection:

```
Techniques d'Obfuscation:
├── Compression
│   └── Réduire taille pour éviter détection signature
├── Encodage (Base64, ROT13, XOR)
│   └── Obscurcir code source
├── Chiffrement
│   └── Chiffrer communication pour IDS/DLP
├── Multilignes/Lignes longues
│   └── Masquer patterns pattern reconnus
├── Masquage de processus
│   └── Renommer processus python → nom légitime
└── Anti-analyse
    └── Détecter sandboxes, debuggers, analyse statique
```

## Architecture Détaillée

```
Système Cible:
┌─────────────────────────────────────────┐
│ Payload (Exécution)                     │
├─────────────────────────────────────────┤
│ 1. Connexion TCP à attaquant:4444       │
│ 2. Boucle Réception de Commandes:       │
│    ├── Attendre données sur socket      │
│    ├── Décoder (UTF-8)                  │
│    ├── Valider commande                 │
│    ├── Exécuter subprocess.Popen()      │
│    ├── Capturer stdout + stderr         │
│    ├── Encoder résultats                │
│    └── Envoyer via socket               │
│ 3. Gestion d'erreurs silencieuse        │
│ 4. Persistance (optionnel)              │
│ 5. Obfuscation (optionnel)              │
└─────────────────────────────────────────┘
           Socket TCP
             ↕ (bidirectionnel)
           4444
┌─────────────────────────────────────────┐
│ Handler/Listener (Attaquant)            │
├─────────────────────────────────────────┤
│ 1. Socket serveur port 4444             │
│ 2. Accepter connexion (bloquer)         │
│ 3. Boucle Interactive:                  │
│    ├── Afficher prompt                  │
│    ├── Lire commande utilisateur        │
│    ├── Envoyer via socket               │
│    ├── Attendre réponse                 │
│    ├── Afficher résultats               │
│    └── Repeat                           │
│ 4. Gestion Ctrl+C                       │
│ 5. Logs (optionnel)                     │
└─────────────────────────────────────────┘
```

## Cas d'Usage Légal

- Red teaming autorisé dans contrats
- Tests de pénétration avec ROE (Rules of Engagement)
- Éducation en environnement sandbox/VM
- Recherche en cybersécurité
- Évaluation de défenses

## Défenses Contre Reverse Shells

- Bloquage des connexions sortantes (pare-feu)
- EDR (Endpoint Detection and Response)
- Monitoring de comportement anormal
- Segmentation réseau
- Application whitelisting
- Logs centralisés
- Détection de patterns réseau
- IDS/IPS pour détection de signatures
