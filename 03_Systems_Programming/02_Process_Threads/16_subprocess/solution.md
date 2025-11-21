========================================
SOLUTIONS - EXERCICE 16 : SUBPROCESS
========================================

========================================
## Solution Défi 1: Exécution de Commandes Basiques
========================================

#!/usr/bin/env python3
"""
Solution Défi 1: Exécution de commandes basiques avec subprocess
"""

```python
import subprocess
from typing import List, Dict

def execute_command(cmd: List[str]) -> Dict:
    """
    Exécute une commande et retourne un dictionnaire avec les résultats

    Args:
        cmd: Liste d'arguments de la commande

    Returns:
        Dict avec 'success', 'output', 'error', 'returncode'
    """
    result = {
        'success': False,
        'output': '',
        'error': '',
        'returncode': -1
    }

    try:
        # Exécution avec capture de stdout et stderr séparés
        completed = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            shell=False,  # IMPORTANT: Jamais shell=True avec entrée utilisateur
            timeout=10
        )

        result['output'] = completed.stdout.strip()
        result['error'] = completed.stderr.strip()
        result['returncode'] = completed.returncode
        result['success'] = (completed.returncode == 0)

    except FileNotFoundError as e:
        # Commande non trouvée
        result['error'] = f"Commande non trouvée: {e}"
        result['returncode'] = 127
    except subprocess.TimeoutExpired:
        # Timeout dépassé
        result['error'] = "Timeout dépassé (>10s)"
        result['returncode'] = 124
    except Exception as e:
        # Autres erreurs
        result['error'] = f"Erreur: {str(e)}"
        result['returncode'] = 1

    return result

def main():
    """
    Test de la fonction execute_command avec différents cas
    """
    print("\n=== SOLUTION DÉFI 1 : Exécution de Commandes ===\n")

    # Test 1 : Commande qui réussit
    print("Test 1: Commande réussie")
    result = execute_command(['echo', 'Success'])
    print(f"Exécution: echo Success")
    print(f"Succès: {result['success']}")
    print(f"Sortie: {result['output']}")
    print(f"Code retour: {result['returncode']}")
    print()

    # Test 2 : Commande qui échoue
    print("Test 2: Erreur - répertoire inexistant")
    result = execute_command(['ls', '/nonexistent'])
    print(f"Exécution: ls /nonexistent")
    print(f"Succès: {result['success']}")
    print(f"Erreur: {result['error'][:80]}...")
    print(f"Code retour: {result['returncode']}")
    print()

    # Test 3 : Commande inexistante
    print("Test 3: Commande inexistante")
    result = execute_command(['commande_bidon_xyz'])
    print(f"Exécution: commande_bidon_xyz")
    print(f"Succès: {result['success']}")
    print(f"Erreur: {result['error'][:80]}...")
    print(f"Code retour: {result['returncode']}")

if __name__ == "__main__":
    main()

```
========================================
## Solution Défi 2: Reconnaissance Système
========================================

#!/usr/bin/env python3
"""
Solution Défi 2: Reconnaissance système multi-plateforme
"""

```python
import subprocess
import sys
import os

def run_safe_command(cmd, timeout=2):
    """
    Exécute une commande de manière sûre avec timeout

    Returns: (success: bool, output: str)
    """
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            shell=False
        )
        if result.returncode == 0:
            return True, result.stdout.strip()
        return False, result.stderr.strip()
    except subprocess.TimeoutExpired:
        return False, "Timeout"
    except FileNotFoundError:
        return False, "Commande non trouvée"
    except Exception as e:
        return False, str(e)

def system_recon():
    """
    Effectue une reconnaissance système complète et multi-plateforme
    """
    print("\n=== RECONNAISSANCE SYSTÈME ===\n")

    # Déterminer l'OS
    os_type = sys.platform
    is_linux = os_type.startswith('linux')
    is_macos = os_type == 'darwin'
    is_windows = os_type == 'win32'

    # INFORMATIONS SYSTÈME
    print("[*] Système d'exploitation")

    if is_linux or is_macos:
        success, output = run_safe_command(['uname', '-s'])
        if success:
            print(f"Système: {output}")

        success, output = run_safe_command(['uname', '-a'])
        if success:
            print(f"Version: {output[:80]}...")
    elif is_windows:
        success, output = run_safe_command(['systeminfo'])
        if success:
            lines = output.split('\n')
            for line in lines[:5]:
                print(line)

    success, output = run_safe_command(['hostname'])
    if success:
        print(f"Hostname: {output}")
    print()

    # INFORMATIONS UTILISATEUR
    print("[*] Utilisateur")

    success, output = run_safe_command(['whoami'])
    if success:
        print(f"Utilisateur: {output}")

    if is_linux or is_macos:
        success, output = run_safe_command(['id'])
        if success:
            print(f"ID/Groupes: {output}")
    elif is_windows:
        success, output = run_safe_command(['whoami', '/groups'])
        if success:
            print(f"Groupes: {output[:80]}...")

    print(f"Répertoire home: {os.path.expanduser('~')}")
    print()

    # INFORMATIONS RÉSEAU
    print("[*] Réseau")

    if is_linux:
        success, output = run_safe_command(['ip', 'addr'])
        if success:
            lines = [l for l in output.split('\n') if 'inet' in l]
            print(f"Adresses IP: {len(lines)} trouvées")
            for line in lines[:2]:
                print(f"  {line.strip()}")
    elif is_macos:
        success, output = run_safe_command(['ifconfig'])
        if success:
            print(f"Configuration réseau: OK")
    elif is_windows:
        success, output = run_safe_command(['ipconfig'])
        if success:
            print(f"Configuration réseau: OK")

    print()

if __name__ == "__main__":
    system_recon()

```
========================================
## Solution Défi 3: Injection de Commandes
========================================

#!/usr/bin/env python3
"""
Solution Défi 3: Démonstration des risques d'injection et protections
"""

```python
import subprocess
import re
import shlex

def validate_hostname(hostname: str) -> bool:
    """
    Valide un hostname pour éviter les injections

    Accepte: alphanumériques, point, tiret (domaines valides)
    """
    # Regex pour valider un hostname/domaine
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, hostname) is not None

def vulnerable_ping(hostname: str):
    """
    VERSION VULNÉRABLE - Démo du risque (ne pas exécuter avec input non-vérifiée!)

    Cette fonction démontre comment une injection fonctionne.
    Ne pas utiliser en production!
    """
    print(f"\n[VULNÉRABLE] subprocess.run with shell=True")
    print(f"Hostname: {hostname}")
    print(f"Commande shell: ping {hostname}")

    # Simuler ce que ferait shell=True sans exécuter
    if ';' in hostname or '&' in hostname or '|' in hostname:
        print("\nRISQUE: Caractères de metacommande détectés!")
        print("Avec shell=True, cela exécuterait PLUSIEURS commandes:")
        parts = hostname.split(';')
        for i, part in enumerate(parts, 1):
            print(f"  {i}. {part.strip()}")
        print("\nCONSÉQUENCE: Exécution de commandes arbitraires!")
    else:
        # Exécution sûre (pas d'injection)
        subprocess.run(
            f"ping -c 1 {hostname}",
            shell=True,
            capture_output=True,
            timeout=3
        )

def secure_ping(hostname: str):
    """
    VERSION SÉCURISÉE - Approche recommandée
    """
    print(f"\n[SÉCURISÉE] subprocess.run with shell=False")
    print(f"Hostname: {hostname}")

    # Validation
    if not validate_hostname(hostname):
        print(f"REJETÉ: Hostname invalide - caractères non autorisés")
        return False

    print(f"Validation: OK")
    print(f"Commande: ['ping', '-c', '1', '{hostname}']")

    try:
        # Arguments séparés = pas d'interprétation shell
        result = subprocess.run(
            ['ping', '-c', '1', hostname],
            capture_output=True,
            text=True,
            timeout=3,
            shell=False  # Important!
        )

        if result.returncode == 0:
            print(f"SUCCÈS: {hostname} est accessible")
        else:
            print(f"ÉCHEC: {hostname} ne répond pas (mais sûr)")
        return True

    except subprocess.TimeoutExpired:
        print(f"TIMEOUT: Pas de réponse de {hostname}")
        return False
    except FileNotFoundError:
        print(f"ping non trouvé sur ce système")
        return False

def main():
    """
    Démonstration complète des risques et protections
    """
    print("\n=== SOLUTION DÉFI 3 : Injection de Commandes ===")

    # Entrée potentiellement malveillante
    malicious_input = "google.com; whoami"

    print(f"\nEntrée testée: {malicious_input}")
    print("\n" + "="*60)

    # Afficher le risque
    print("\nAPPROCHE VULNÉRABLE (DÉMONSTRATION - NE PAS EXÉCUTER):")
    vulnerable_ping(malicious_input)

    # Afficher la solution
    print("\n" + "="*60)
    print("\nAPPROCHE SÉCURISÉE (RECOMMANDÉE):")
    secure_ping(malicious_input)

    # Test avec une adresse valide
    print("\n" + "="*60)
    print("\nTest avec une adresse valide:")
    secure_ping("google.com")

    # Alternative avec shlex.quote()
    print("\n" + "="*60)
    print("\nAlternative: shlex.quote() pour shell=True")
    print(f"Avant: {malicious_input}")
    print(f"Après: {shlex.quote(malicious_input)}")
    print("(Mais shell=False reste préférable!)")

if __name__ == "__main__":
    main()

```
========================================
## Solution Défi 4: Énumération de Ports
========================================

#!/usr/bin/env python3
"""
Solution Défi 4: Scanner de ports avec gestion des timeouts
"""

```python
import subprocess
from typing import List, Tuple

def check_port(host: str, port: int, timeout: float = 1.0) -> bool:
    """
    Vérifie si un port est ouvert sur un hôte

    Args:
        host: Adresse IP ou hostname
        port: Numéro de port
        timeout: Délai maximum (secondes)

    Returns:
        True si le port est ouvert, False sinon
    """
    # Essayer avec netcat d'abord
    try:
        result = subprocess.run(
            ['nc', '-zv', host, str(port)],
            capture_output=True,
            timeout=timeout,
            shell=False
        )
        return result.returncode == 0
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass

    # Fallback: utiliser nmap si disponible
    try:
        result = subprocess.run(
            ['nmap', '-p', str(port), '-oG', '-', host],
            capture_output=True,
            timeout=timeout,
            shell=False
        )
        return 'open' in result.stdout.decode()
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass

    return False

def scan_ports(host: str, ports: List[int]) -> Tuple[List[int], int]:
    """
    Scanne une liste de ports

    Args:
        host: Hôte à scanner
        ports: Liste des ports

    Returns:
        (ports_ouverts, temps_total)
    """
    import time

    print(f"\nScanneur de ports de {host}")
    print("="*40)

    open_ports = []
    start_time = time.time()

    for port in ports:
        try:
            if check_port(host, port, timeout=1):
                open_ports.append(port)
                print(f"Port {port:5d} : OUVERT")
            else:
                print(f"Port {port:5d} : Fermé")
        except KeyboardInterrupt:
            print("\nScan interrompu")
            break
        except Exception as e:
            print(f"Port {port:5d} : Erreur ({type(e).__name__})")

    elapsed = time.time() - start_time

    print("="*40)
    print(f"\nRésultats:")
    print(f"Ports testés: {len(ports)}")
    print(f"Ports ouverts: {len(open_ports)}")
    if open_ports:
        print(f"Ports: {', '.join(map(str, open_ports))}")
    print(f"Temps: {elapsed:.2f}s")

    return open_ports, elapsed

def main():
    """
    Test du scanner de ports
    """
    print("\n=== SOLUTION DÉFI 4 : Énumération de Ports ===")

    # Ports courants à scanner
    ports = [22, 80, 443, 8080, 3306, 5432]

    # Scanner localhost
    scan_ports('127.0.0.1', ports)

if __name__ == "__main__":
    main()

```
========================================
## Solution Défi 5: Analyse de Processus
========================================

#!/usr/bin/env python3
"""
Solution Défi 5: Capture et parsing de processus
"""

```python
import subprocess
import sys

def analyze_processes():
    """
    Analyse les processus en cours avec parsing
    """
    print("\n=== ANALYSE PROCESSUS ===\n")

    # Déterminer la commande selon l'OS
    if sys.platform.startswith('linux') or sys.platform == 'darwin':
        cmd = ['ps', 'aux']
    else:
        cmd = ['tasklist']

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=5,
            shell=False
        )

        lines = result.stdout.strip().split('\n')

        print(f"Total processus: {len(lines) - 1}")  # -1 pour l'en-tête

        # Chercher les processus Python
        python_procs = [l for l in lines if 'python' in l.lower()]
        print(f"Processus Python: {len(python_procs)}")

        for proc in python_procs[:3]:
            print(f"  {proc[:80]}...")

        # Analyser l'utilisation CPU/mémoire (si ps aux)
        if 'ps' in str(cmd):
            print("\nTop 3 consommateurs mémoire:")
            # Indice 5 = %MEM, indice 10 = COMMAND
            try:
                procs_with_mem = []
                for line in lines[1:]:
                    parts = line.split()
                    if len(parts) >= 6:
                        try:
                            mem_percent = float(parts[3])
                            command = ' '.join(parts[10:]) if len(parts) > 10 else parts[-1]
                            procs_with_mem.append((mem_percent, command))
                        except ValueError:
                            continue

                # Trier par mémoire décroissante
                procs_with_mem.sort(reverse=True)
                for mem, cmd_name in procs_with_mem[:3]:
                    print(f"  {mem:5.1f}% - {cmd_name[:50]}")
            except Exception:
                pass

    except Exception as e:
        print(f"Erreur: {e}")

if __name__ == "__main__":
    analyze_processes()

```
========================================
## Solution Défi 6: Gestion des Signaux
========================================

#!/usr/bin/env python3
"""
Solution Défi 6: Gestion des signaux et termination
"""

```python
import subprocess
import time

def run_with_timeout(cmd, timeout):
    """
    Exécute une commande avec timeout géré (terminate -> kill)

    Returns: (success: bool, returncode: int, status: str)
    """
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    status = f"Processus {process.pid} lancé"

    try:
        # Attendre la fin du processus avec timeout
        returncode = process.wait(timeout=timeout)
        status += f"\nTerminé naturellement après {timeout}s"
        return True, returncode, status

    except subprocess.TimeoutExpired:
        # Timeout: essayer SIGTERM d'abord
        status += f"\nTimeout après {timeout}s"
        status += "\nEnvoi de SIGTERM..."

        process.terminate()

        try:
            # Attendre 1 seconde que SIGTERM fonctionne
            returncode = process.wait(timeout=1)
            status += "\nSIGTERM réussi"
            return True, returncode, status

        except subprocess.TimeoutExpired:
            # SIGTERM a échoué, forcer SIGKILL
            status += "\nSIGTERM timeout, envoi de SIGKILL..."
            process.kill()

            try:
                returncode = process.wait(timeout=1)
                status += "\nSIGKILL exécuté"
                return False, returncode, status
            except:
                status += "\nErreur lors du kill"
                return False, -1, status

def main():
    """
    Test avec différentes durées
    """
    print("\n=== SOLUTION DÉFI 6 : Gestion des Signaux ===\n")

    tests = [
        (['echo', 'test'], 5, "Commande rapide"),
        (['sleep', '2'], 5, "Commande moyenne"),
        (['sleep', '10'], 1, "Commande lente"),
    ]

    for cmd, timeout, description in tests:
        print(f"\nTest: {description}")
        print(f"Commande: {' '.join(cmd)}")
        print(f"Timeout: {timeout}s")

        success, returncode, status = run_with_timeout(cmd, timeout)

        print(status)
        print(f"Code de sortie: {returncode}")
        print("-"*50)

if __name__ == "__main__":
    main()

```
========================================
## Solution Défi 7: Redirection et Pipes
========================================

#!/usr/bin/env python3
"""
Solution Défi 7: Démonstration de PIPE et redirection
"""

```python
import subprocess

def demo_redirection():
    """
    Démonstration complète des redirections
    """
    print("\n=== REDIRECTION ET PIPES ===\n")

    # 1. Capture stdout
    print("1. Capture stdout:")
    result = subprocess.run(
        ['echo', 'Hello World'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    print(f"   Input: echo 'Hello World'")
    print(f"   Output: {result.stdout.strip()}")

    # 2. Capture stderr
    print("\n2. Capture stderr:")
    result = subprocess.run(
        ['ls', '/nonexistent'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    print(f"   Input: ls /nonexistent")
    print(f"   Error: {result.stderr.strip()[:60]}...")

    # 3. Combiner stdout et stderr
    print("\n3. Combiner stdout + stderr:")
    result = subprocess.run(
        ['ls', '/tmp', '/nonexistent'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,  # Combine stderr dans stdout
        text=True
    )
    lines = result.stdout.strip().split('\n')
    print(f"   Lignes: {len(lines)}")

    # 4. Communication stdin/stdout
    print("\n4. Communication bidirectionnelle (stdin -> cat -> stdout):")
    process = subprocess.Popen(
        ['cat'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    input_text = "Ligne 1\nLigne 2\nLigne 3\n"
    stdout, stderr = process.communicate(input=input_text)
    print(f"   Input: {repr(input_text)}")
    print(f"   Output: {repr(stdout)}")

    # 5. Suppression avec DEVNULL
    print("\n5. Suppression avec DEVNULL:")
    process = subprocess.Popen(
        ['echo', 'cette sortie est supprimée'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    process.wait()
    print(f"   Sortie supprimée pour exécution discrète")

if __name__ == "__main__":
    demo_redirection()

```
========================================
## Solution Défi 8: Challenge Final (Énumération Complète)
========================================

#!/usr/bin/env python3
"""
Solution Défi 8: Énumération automatisée complète et sécurisée
"""

```python
import subprocess
import sys
import os
from datetime import datetime
from typing import Dict, List

class Enumerator:
    """
    Classe pour effectuer une énumération système sécurisée et complète
    """

    def __init__(self, timeout=2):
        """Initialise l'énumérateur"""
        self.timeout = timeout
        self.os_type = sys.platform
        self.results = {}

    def _run_safe_command(self, cmd: List[str]) -> tuple:
        """
        Exécute une commande de manière sûre

        Returns: (success: bool, output: str)
        """
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=self.timeout,
                shell=False  # JAMAIS shell=True
            )
            if result.returncode == 0:
                return True, result.stdout.strip()
            return False, result.stderr.strip()
        except subprocess.TimeoutExpired:
            return False, "Timeout"
        except FileNotFoundError:
            return False, "Commande non trouvée"
        except Exception as e:
            return False, str(e)

    def enumerate_system(self):
        """Énumère les infos système"""
        section = {}

        # Système d'exploitation
        if self.os_type.startswith('linux'):
            success, output = self._run_safe_command(['uname', '-s'])
            section['OS'] = output if success else "Linux"

            success, output = self._run_safe_command(['uname', '-r'])
            section['Kernel'] = output if success else "N/A"
        else:
            section['OS'] = sys.platform
            section['Kernel'] = "N/A"

        # Hostname
        success, output = self._run_safe_command(['hostname'])
        section['Hostname'] = output if success else "N/A"

        self.results['System'] = section

    def enumerate_user(self):
        """Énumère les infos utilisateur"""
        section = {}

        # Utilisateur courant
        success, output = self._run_safe_command(['whoami'])
        section['User'] = output if success else "N/A"

        # ID
        if self.os_type.startswith('linux'):
            success, output = self._run_safe_command(['id'])
            section['UID/GID'] = output if success else "N/A"

        # Répertoire home
        section['Home'] = os.path.expanduser('~')

        self.results['User'] = section

    def enumerate_network(self):
        """Énumère les infos réseau"""
        section = {}

        if self.os_type.startswith('linux'):
            success, output = self._run_safe_command(['hostname', '-I'])
            if success:
                ips = output.split()
                section['IPs'] = ', '.join(ips[:3])
            else:
                section['IPs'] = "N/A"

        self.results['Network'] = section

    def enumerate_processes(self):
        """Énumère les processus"""
        section = {}

        if self.os_type.startswith('linux'):
            success, output = self._run_safe_command(['ps', 'aux'])
            if success:
                lines = output.split('\n')
                section['Total'] = len(lines) - 1

                python_procs = [l for l in lines if 'python' in l.lower()]
                section['Python'] = len(python_procs)
            else:
                section['Total'] = 0
                section['Python'] = 0

        self.results['Processes'] = section

    def generate_report(self) -> str:
        """Génère un rapport formaté"""
        report = "\n"
        report += "="*50 + "\n"
        report += "RAPPORT D'ÉNUMÉRATION\n"
        report += f"Généré: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        report += "="*50 + "\n"

        for section_name, section_data in self.results.items():
            report += f"\n[*] {section_name.upper()}\n"
            for key, value in section_data.items():
                report += f"{key}: {value}\n"

        report += "\n" + "="*50 + "\n"
        return report

    def run_full_enumeration(self):
        """Exécute l'énumération complète"""
        print("\n=== ÉNUMÉRATION SYSTÈME EN COURS ===\n")
        print("[*] Énumération système...", end=" ", flush=True)
        self.enumerate_system()
        print("OK")

        print("[*] Énumération utilisateur...", end=" ", flush=True)
        self.enumerate_user()
        print("OK")

        print("[*] Énumération réseau...", end=" ", flush=True)
        self.enumerate_network()
        print("OK")

        print("[*] Énumération processus...", end=" ", flush=True)
        self.enumerate_processes()
        print("OK")

        print("\n")
        return self.generate_report()

def main():
    """
    Fonction principale - Énumération complète
    """
    print("\n=== SOLUTION DÉFI 8 : Challenge Final ===")

    # Créer et lancer l'énumérateur
    enum = Enumerator(timeout=2)
    report = enum.run_full_enumeration()

    # Afficher le rapport
    print(report)

    # Afficher des notes de sécurité
    print("[*] Notes de Sécurité:")
    print("- Shell=False utilisé partout")
    print("- Timeouts implémentés")
    print("- Gestion d'erreurs complète")
    print("- Multi-plateforme compatible")

if __name__ == "__main__":
    main()

```
========================================
FIN DES SOLUTIONS
========================================

Les solutions ci-dessus démontrent:

1. Bases de subprocess (run, Popen, capture)
2. Multi-plateforme (sys.platform, commandes OS-spécifiques)
3. Sécurité (shell=False, validation, timeouts)
4. Gestion d'erreurs (try/except, TimeoutExpired)
5. Parsing de sortie (split, list comprehension)
6. Gestion avancée (signaux, PIPE, DEVNULL)
7. Conception orientée objet (classe Enumerator)
8. Intégration de tous les concepts

Points clés à retenir:
- JAMAIS shell=True avec input utilisateur
- TOUJOURS utiliser des listes d'arguments
- Implémenter des timeouts
- Valider et nettoyer les inputs
- Gérer les exceptions appropriées
- Capturer et analyser les erreurs
- Tester sur plusieurs plateformes
- Documenter le code en français
