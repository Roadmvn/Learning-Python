# Exercice 24 - Privilege Escalation

## Objectifs d'apprentissage
- Comprendre les vecteurs d'escalade de privilèges
- Énumération système pour identifier les vulnérabilités
- Exploitation de misconfigurations courantes
- Techniques d'escalade sur Linux et Windows
- Développement de scripts d'énumération automatisés

## Avertissement Éthique

**ATTENTION: TECHNIQUES SENSIBLES - USAGE STRICTEMENT CONTRÔLÉ**

L'escalade de privilèges sans autorisation est illégale et constitue une violation grave de la sécurité. Ces techniques sont présentées EXCLUSIVEMENT pour:
- Formation en tests de pénétration autorisés
- Hardening et sécurisation de systèmes
- Compréhension des vecteurs d'attaque pour défense
- Certification professionnelle en sécurité (OSCP, CEH)

**INTERDIT:**
- Escalade sur systèmes sans autorisation explicite
- Exploitation de systèmes de production
- Utilisation en dehors du cadre légal
- Bypass de contrôles de sécurité sans permission

**AUTORISÉ UNIQUEMENT:**
- Environnements de laboratoire personnels
- Tests de pénétration avec contrat signé
- Plateformes CTF et HackTheBox
- Recherche académique avec approbation

## Concepts Clés

### Vecteurs d'Escalade de Privilèges

```
Privilege Escalation Vectors:
├── Kernel Exploits
│   ├── CVE exploitables
│   ├── Versions vulnérables
│   └── Module kernel bugs
├── SUID/SGID Binaries
│   ├── Binaires avec permissions élevées
│   ├── Path hijacking
│   └── Library injection
├── Sudo Misconfigurations
│   ├── NOPASSWD entries
│   ├── Wildcards exploitation
│   ├── Version-specific bugs
│   └── GTFOBins techniques
├── Scheduled Tasks/Cron
│   ├── World-writable scripts
│   ├── Path exploitation
│   └── Command injection
├── Service Misconfigurations
│   ├── Unquoted service paths
│   ├── Weak permissions
│   └── DLL hijacking
└── Credentials & Secrets
    ├── Config files
    ├── History files
    ├── Environment variables
    └── Memory dumps
```

### Méthodologie d'Énumération

#### Phase 1: Collecte d'informations
```bash
# Informations système
uname -a
cat /etc/os-release
cat /proc/version

# Utilisateur actuel et groupes
id
whoami
groups

# Autres utilisateurs
cat /etc/passwd
cat /etc/group

# Variables d'environnement
env
echo $PATH
```

#### Phase 2: Recherche de vulnérabilités
```bash
# SUID binaries
find / -perm -4000 -type f 2>/dev/null

# Writable files/directories
find / -writable -type f 2>/dev/null
find / -writable -type d 2>/dev/null

# Sudo permissions
sudo -l

# Cron jobs
cat /etc/crontab
ls -la /etc/cron.*
crontab -l
```

#### Phase 3: Exploitation
- Identifier le vecteur le plus prometteur
- Rechercher exploits ou techniques
- Tester l'exploitation
- Obtenir privilèges élevés

## Techniques Spécifiques

### Linux Privilege Escalation

#### SUID Exploitation
```python
# Recherche de binaires SUID exploitables
import subprocess
import os

def find_suid_binaries():
    result = subprocess.run(
        ['find', '/', '-perm', '-4000', '-type', 'f'],
        capture_output=True,
        text=True
    )
    return result.stdout.splitlines()

# GTFOBins: binaires exploitables
gtfobins = [
    'nmap', 'vim', 'find', 'bash', 'more', 'less',
    'nano', 'cp', 'mv', 'python', 'perl', 'ruby'
]
```

#### Sudo Exploitation
```bash
# Exemples de sudo misconfigurations

# 1. NOPASSWD avec wildcards
user ALL=(ALL) NOPASSWD: /bin/cp /tmp/* /root/

# Exploitation: créer fichier malveillant
echo '#!/bin/bash\nbash -i' > /tmp/exploit.sh
sudo /bin/cp /tmp/* /root/

# 2. PATH manipulation
user ALL=(ALL) NOPASSWD: /usr/bin/script.sh

# Créer faux binary dans PATH
export PATH=/tmp:$PATH
```

### Windows Privilege Escalation

#### Unquoted Service Paths
```powershell
# Recherche de services avec chemins non-quotés
wmic service get name,displayname,pathname,startmode | findstr /i "auto" | findstr /i /v "c:\windows\\" | findstr /i /v """

# Exploitation: placer binaire malveillant dans chemin
# C:\Program Files\Vulnerable App\app.exe
# Devient: C:\Program.exe si non-quoté
```

#### Weak Service Permissions
```powershell
# Vérifier permissions des services
accesschk.exe -uwcqv "Users" *

# Modifier config si permissions faibles
sc config ServiceName binpath= "C:\malicious.exe"
sc start ServiceName
```

## Structure du Projet

```
24_privilege_escalation/
├── README.md
├── main.py
├── exercice.txt
└── solution.txt
```

## Prérequis
- Python 3.8+
- Modules: subprocess, os, pathlib
- Accès à environnement Linux/Windows de test
- Connaissance des permissions Unix
- Compréhension des services Windows

## Outils d'Énumération

### Linux
- LinPEAS (Linux Privilege Escalation Awesome Script)
- LinEnum
- Unix-privesc-check
- pspy (process monitoring)

### Windows
- WinPEAS
- PowerUp.ps1
- SharpUp
- Seatbelt
- accesschk.exe (Sysinternals)

## Ressources

### Documentation
- Python subprocess: https://docs.python.org/3/library/subprocess.html
- Linux file permissions: man chmod
- Windows services: Microsoft Docs

### Références Techniques
- GTFOBins: https://gtfobins.github.io/
- LOLBAS (Living Off The Land Binaries): https://lolbas-project.github.io/
- PayloadsAllTheThings: Privilege Escalation
- HackTricks: Privilege Escalation guides

### Plateformes de Pratique
- HackTheBox machines
- TryHackMe privilege escalation rooms
- VulnHub vulnerable VMs
- OSCP labs

## Défense et Détection

### Hardening Linux
```bash
# Limiter SUID binaries
find / -perm -4000 -exec chmod u-s {} \;

# Auditer sudo configuration
visudo  # Vérifier NOPASSWD entries

# Monitoring avec auditd
auditctl -w /etc/sudoers -p wa -k sudoers_changes

# Désactiver kernel modules non nécessaires
echo "install usb-storage /bin/true" >> /etc/modprobe.d/disable-usb.conf
```

### Hardening Windows
```powershell
# Vérifier services avec permissions faibles
sc sdshow ServiceName

# Quoter tous les chemins de services
sc config ServiceName binpath= "\"C:\Program Files\App\app.exe\""

# Activer AppLocker
Set-AppLockerPolicy -PolicyObject $policy

# Auditer changements de privilèges
auditpol /set /subcategory:"User Account Management" /success:enable /failure:enable
```

### Indicateurs de Détection
- Utilisation suspecte de sudo
- Modifications de fichiers SUID
- Exécution de binaires depuis /tmp ou /dev/shm
- Changements de permissions inhabituels
- Élévation de privilèges anormale

## Considérations Légales

**RAPPEL CRITIQUE:**

L'escalade de privilèges sans autorisation est un crime grave. Conséquences possibles:
- Poursuites pénales sévères
- Amendes importantes
- Emprisonnement
- Interdiction professionnelle
- Responsabilité civile

**TOUJOURS:**
- Obtenir autorisation écrite
- Respecter le périmètre défini
- Documenter toutes les actions
- Rapporter les vulnérabilités trouvées
- Nettoyer après tests

## Support et Formation

Pour approfondir vos connaissances en escalade de privilèges:
- OSCP (Offensive Security Certified Professional)
- CEH (Certified Ethical Hacker)
- GPEN (GIAC Penetration Tester)
- Cours spécialisés sur Offensive Security
- Communautés de sécurité éthique
