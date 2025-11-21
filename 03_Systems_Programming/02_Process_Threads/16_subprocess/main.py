#!/usr/bin/env python3
"""
Exercice 16 : Subprocess en Python
Démonstration complète du module subprocess avec applications en cybersécurité

AVERTISSEMENT SÉCURITÉ:
- Ces techniques sont destinées à l'apprentissage et aux tests autorisés uniquement
- L'utilisation sur des systèmes sans autorisation est ILLÉGALE
- JAMAIS utiliser shell=True avec entrées utilisateur
- TOUJOURS valider et nettoyer les inputs
"""

import subprocess
import time
import shlex
import signal
import os
from typing import List, Tuple, Optional

# =============================================================================
# PARTIE 1 : CONCEPTS DE BASE DE SUBPROCESS
# =============================================================================

def introduction_subprocess():
    """
    Introduction aux concepts de base de subprocess
    """
    print("\n" + "="*60)
    print("PARTIE 1 : CONCEPTS DE BASE DE SUBPROCESS")
    print("="*60)

    # 1. Exécution simple sans capture de sortie
    print("\n1. Exécution simple d'une commande:")
    print("   Commande: echo 'Hello Subprocess'")
    result = subprocess.run(['echo', 'Hello Subprocess'])
    print(f"   Code de retour: {result.returncode}")

    # 2. Exécution avec capture de sortie
    print("\n2. Capture de la sortie (capture_output=True):")
    result = subprocess.run(
        ['echo', 'Texte capturé'],
        capture_output=True,  # Capture stdout et stderr
        text=True             # Renvoie des strings au lieu de bytes
    )
    print(f"   Sortie: {result.stdout.strip()}")
    print(f"   Code de retour: {result.returncode}")

    # 3. Capture de stdout et stderr séparément
    print("\n3. Capture séparée de stdout et stderr:")
    result = subprocess.run(
        ['ls', '/tmp'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    lines = [l for l in result.stdout.split('\n') if l]
    print(f"   Fichiers trouvés: {len(lines)}")
    if lines:
        print(f"   Premier fichier: {lines[0]}")


def subprocess_run_vs_popen():
    """
    Comparaison entre subprocess.run() et subprocess.Popen()
    """
    print("\n" + "="*60)
    print("PARTIE 2 : subprocess.run() VS subprocess.Popen()")
    print("="*60)

    # subprocess.run() : Interface recommandée (simple et synchrone)
    print("\n1. subprocess.run() - Simple et synchrone:")
    print("   Avantages: Interface simple, attente automatique")
    result = subprocess.run(
        ['whoami'],
        capture_output=True,
        text=True
    )
    print(f"   Utilisateur courant: {result.stdout.strip()}")
    print(f"   Code de retour: {result.returncode}")

    # subprocess.Popen() : Contrôle avancé (plus de flexibilité)
    print("\n2. subprocess.Popen() - Contrôle avancé:")
    print("   Avantages: Plus de contrôle, interaction en temps réel")
    process = subprocess.Popen(
        ['echo', 'Texte avec Popen'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    # communicate() : envoie données et attend la fin
    stdout, stderr = process.communicate()
    print(f"   Sortie: {stdout.strip()}")
    print(f"   PID du processus: {process.pid}")
    print(f"   Code de retour: {process.returncode}")

    # Différence clé : Popen avec control asynchrone
    print("\n3. Popen avec polling (vérification non-bloquante):")
    process = subprocess.Popen(
        ['sleep', '1'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    print(f"   Processus lancé (PID {process.pid})")
    print(f"   Encore en cours? {process.poll() is None}")
    time.sleep(1.5)
    print(f"   Après 1.5s? {process.poll() is None}")
    print(f"   Code de retour: {process.returncode}")


def capture_output_demo():
    """
    Démonstration des différentes méthodes de capture de sortie
    """
    print("\n" + "="*60)
    print("PARTIE 3 : CAPTURE DE SORTIE")
    print("="*60)

    # Cas 1 : Pas de capture
    print("\n1. Sans capture (sortie directe):")
    print("   Commande: echo 'Affichage direct'")
    result = subprocess.run(['echo', 'Affichage direct'])
    print(f"   stdout capturé: {result.stdout}")

    # Cas 2 : capture_output=True (Python 3.7+)
    print("\n2. Avec capture_output=True (méthode moderne):")
    result = subprocess.run(
        ['whoami'],
        capture_output=True,
        text=True
    )
    print(f"   stdout: '{result.stdout.strip()}'")
    print(f"   stderr: '{result.stderr.strip()}'")

    # Cas 3 : PIPE pour plus de contrôle
    print("\n3. Avec subprocess.PIPE (méthode classique):")
    result = subprocess.run(
        ['ls', '-la', '/tmp'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    print(f"   Nombre de lignes stdout: {len(result.stdout.split(chr(10)))}")
    print(f"   Nombre de lignes stderr: {len(result.stderr.split(chr(10)))}")

    # Cas 4 : Combiner stdout et stderr
    print("\n4. Combiner stderr dans stdout (stderr=subprocess.STDOUT):")
    result = subprocess.run(
        ['ls', '/tmp', '/dossier_inexistant'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,  # Combine stderr dans stdout
        text=True
    )
    print(f"   Nombre total de lignes: {len(result.stdout.split(chr(10)))}")


def shell_true_vs_false():
    """
    CRITIQUE POUR LA SÉCURITÉ : Démonstration des risques de shell=True
    """
    print("\n" + "="*60)
    print("PARTIE 4 : shell=True vs shell=False (SÉCURITÉ CRITIQUE!)")
    print("="*60)

    # shell=False (RECOMMANDÉ)
    print("\n1. shell=False (SÛRE - Arguments séparés):")
    result = subprocess.run(
        ['echo', 'Argument 1', 'Argument 2'],
        capture_output=True,
        text=True
    )
    print(f"   Commande: ['echo', 'Argument 1', 'Argument 2']")
    print(f"   Sortie: {result.stdout.strip()}")
    print("   Sécurité: Les arguments ne sont pas interprétés par le shell")

    # shell=True (DANGEREUX!)
    print("\n2. shell=True (DANGEREUX - String interprétée):")
    print("   DANGER: Permet l'utilisation de pipes, wildcards, substitution")
    result = subprocess.run(
        'echo "Commande avec shell"',
        shell=True,
        capture_output=True,
        text=True
    )
    print(f"   Commande: 'echo \"Commande avec shell\"'")
    print(f"   Sortie: {result.stdout.strip()}")

    # Démonstration du risque d'injection
    print("\n3. RISQUE D'INJECTION AVEC shell=True:")
    print("   Simulation d'une entrée malveillante:")
    user_input = "test'; echo 'INJECTION RÉUSSIE'; echo '"
    # Cette commande dangeureuse montre le risque
    print(f"   Entrée malveillante: {user_input}")
    print("   Avec shell=True, cela exécuterait deux commandes!")
    print("   Avec shell=False, c'est traité comme simple argument")

    # Démonstration sûre avec shell=False
    print("\n4. APPROCHE SÛRE avec shell=False:")
    dangerous_input = "'; rm -rf /; echo '"
    # shell=False échappe naturellement
    result = subprocess.run(
        ['echo', dangerous_input],
        capture_output=True,
        text=True
    )
    print(f"   Entrée potentiellement malveillante: {dangerous_input}")
    print(f"   Sortie (safe): {result.stdout.strip()}")
    print("   Aucune injection possible car pas d'interprétation shell")


def command_injection_examples():
    """
    Exemples concrets d'attaques par injection de commandes
    """
    print("\n" + "="*60)
    print("PARTIE 5 : EXEMPLES D'INJECTION DE COMMANDES")
    print("="*60)

    # Exemple 1 : Injection via ping
    print("\n1. Injection via parameter ping (VULNÉRABLE):")
    print("   Code vulnérable:")
    print("   hostname = 'target.com; cat /etc/passwd'")
    print("   subprocess.run(f'ping {hostname}', shell=True)")
    print("   ")
    print("   Ce code exécuterait DEUX commandes:")
    print("   - ping target.com")
    print("   - cat /etc/passwd")
    print("   ")
    print("   Code sûr:")
    hostname = "target.com"
    result = subprocess.run(
        ['ping', '-c', '1', hostname],
        capture_output=True,
        text=True,
        timeout=2
    )
    print(f"   subprocess.run(['ping', '-c', '1', '{hostname}'])")
    print("   Les arguments ne peuvent pas être interprétés")

    # Exemple 2 : Protection avec validation
    print("\n2. Protection par validation d'entrée:")
    import re
    def validate_filename(filename):
        """Valider un nom de fichier"""
        # Accepter uniquement alphanumériques, point, tiret, underscore
        if not re.match(r'^[a-zA-Z0-9._-]+$', filename):
            raise ValueError(f"Nom de fichier invalide: {filename}")
        return filename

    try:
        filename = validate_filename("malicious; rm -rf /")
    except ValueError as e:
        print(f"   Validation rejetée: {e}")

    filename = validate_filename("document.txt")
    print(f"   Fichier valide: {filename}")

    # Exemple 3 : Utiliser shlex.quote()
    print("\n3. Protection avec shlex.quote():")
    user_input = "test; dangerous_command"
    escaped = shlex.quote(user_input)
    print(f"   Entrée brute: {user_input}")
    print(f"   Après shlex.quote(): {escaped}")
    print("   (Mais shell=False reste la meilleure approche)")


def timeout_and_signals():
    """
    Gestion des timeouts et signaux
    """
    print("\n" + "="*60)
    print("PARTIE 6 : GESTION DES TIMEOUTS ET SIGNAUX")
    print("="*60)

    # 1. Timeout avec subprocess.run()
    print("\n1. Timeout avec subprocess.run():")
    try:
        print("   Exécution de 'sleep 2' avec timeout=1")
        result = subprocess.run(
            ['sleep', '2'],
            timeout=1
        )
    except subprocess.TimeoutExpired:
        print("   TimeoutExpired levée après 1 seconde")
        print("   Le processus a été terminé")

    # 2. Timeout avec Popen et wait()
    print("\n2. Timeout avec Popen et wait():")
    process = subprocess.Popen(['sleep', '3'])
    print(f"   Processus lancé (PID {process.pid})")
    try:
        process.wait(timeout=1)
    except subprocess.TimeoutExpired:
        print("   Wait() timeout après 1 seconde")
        # Terminer gracieusement
        process.terminate()
        try:
            process.wait(timeout=1)
            print("   Processus terminé avec SIGTERM")
        except subprocess.TimeoutExpired:
            # Force kill si terminate() échoue
            process.kill()
            print("   Processus tué avec SIGKILL")

    # 3. Gestion complète avec timeout et retry
    print("\n3. Pattern complet: terminate -> wait -> kill:")
    process = subprocess.Popen(['sleep', '10'])
    print(f"   Processus lancé (PID {process.pid})")

    # Essayer terminate d'abord (gracieux)
    process.terminate()
    try:
        process.wait(timeout=2)
        print("   SIGTERM réussi")
    except subprocess.TimeoutExpired:
        # Si terminate échoue, force kill
        process.kill()
        process.wait()
        print("   SIGKILL exécuté")


def return_codes_demo():
    """
    Démonstration des codes de retour
    """
    print("\n" + "="*60)
    print("PARTIE 7 : CODES DE RETOUR ET GESTION D'ERREUR")
    print("="*60)

    # Code 0 : Succès
    print("\n1. Succès (returncode=0):")
    result = subprocess.run(['echo', 'Success'], capture_output=True)
    print(f"   echo 'Success' -> returncode: {result.returncode}")

    # Code 1 : Erreur générale
    print("\n2. Erreur générale (returncode=1):")
    result = subprocess.run(
        ['ls', '/dossier_inexistant'],
        capture_output=True
    )
    print(f"   ls /dossier_inexistant -> returncode: {result.returncode}")

    # Utiliser check=True pour lever exception
    print("\n3. Avec check=True (lève CalledProcessError):")
    try:
        result = subprocess.run(
            ['false'],  # Commande qui retourne 1
            check=True,
            capture_output=True
        )
    except subprocess.CalledProcessError as e:
        print(f"   CalledProcessError levée pour returncode {e.returncode}")

    # Codes spéciaux
    print("\n4. Codes de retour spéciaux:")
    print("   0   : Succès")
    print("   1   : Erreur générale")
    print("   2   : Mauvaise utilisation")
    print("   127 : Commande non trouvée")
    print("   137 : Tué par SIGKILL (9)")
    print("   143 : Tué par SIGTERM (15)")
    print("   128+N : Tué par signal N")


def red_teaming_examples():
    """
    Applications pratiques en cybersécurité et red teaming
    """
    print("\n" + "="*60)
    print("PARTIE 8 : APPLICATIONS EN CYBERSÉCURITÉ")
    print("="*60)

    # 1. Enumération système
    print("\n1. Énumération système (reconnaissance):")
    commands = [
        (['whoami'], 'Utilisateur courant'),
        (['id'], 'ID et groupes'),
        (['uname', '-a'], 'Information système'),
        (['hostname'], 'Hostname'),
    ]

    for cmd, desc in commands:
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=2
            )
            if result.returncode == 0:
                output = result.stdout.strip()
                # Afficher seulement les 50 premiers caractères
                display = output[:50] + "..." if len(output) > 50 else output
                print(f"   {desc}: {display}")
        except Exception as e:
            print(f"   {desc}: Erreur ({type(e).__name__})")

    # 2. Extraction d'informations réseau
    print("\n2. Informations réseau (si disponible):")
    net_commands = [
        (['ifconfig'], 'Configuration réseau'),
        (['netstat', '-an'], 'Connexions réseau'),
        (['ip', 'route'], 'Table de routage'),
    ]

    for cmd, desc in net_commands:
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=2
            )
            if result.returncode == 0:
                lines = result.stdout.strip().split('\n')
                print(f"   {desc}: {len(lines)} lignes")
            else:
                print(f"   {desc}: Commande non trouvée")
        except Exception:
            print(f"   {desc}: Non disponible")

    # 3. Parsing de sortie
    print("\n3. Parsing de sortie pour extraction d'infos:")
    result = subprocess.run(
        ['ps', 'aux'],
        capture_output=True,
        text=True,
        timeout=2
    )
    processes = result.stdout.strip().split('\n')
    print(f"   Processus actifs: {len(processes)}")
    # Afficher seulement les processus Python
    python_procs = [p for p in processes if 'python' in p.lower()]
    print(f"   Processus Python: {len(python_procs)}")
    if python_procs:
        print(f"   Exemple: {python_procs[0][:80]}...")


def security_best_practices():
    """
    Bonnes pratiques de sécurité avec subprocess
    """
    print("\n" + "="*60)
    print("PARTIE 9 : BONNES PRATIQUES DE SÉCURITÉ")
    print("="*60)

    # Bonne pratique 1 : Ne jamais utiliser shell=True avec input utilisateur
    print("\n1. JAMAIS shell=True avec entrées utilisateur:")
    print("   MAUVAIS CODE:")
    print("   user_input = input('Entrez hostname: ')")
    print("   subprocess.run(f'ping {user_input}', shell=True)")
    print("   ")
    print("   BON CODE:")
    print("   user_input = input('Entrez hostname: ')")
    print("   subprocess.run(['ping', '-c', '1', user_input])")

    # Bonne pratique 2 : Toujours utiliser liste d'arguments
    print("\n2. Utiliser des listes plutôt que strings:")
    print("   BON:")
    print("   subprocess.run(['ls', '-la', '/tmp'])")
    print("   ")
    print("   MAUVAIS:")
    print("   subprocess.run('ls -la /tmp', shell=True)")

    # Bonne pratique 3 : Implémenter des timeouts
    print("\n3. Toujours implémenter des timeouts:")
    print("   subprocess.run(['nmap', 'target'], timeout=300)")
    print("   Évite les blocages indéfinis")

    # Bonne pratique 4 : Valider les inputs
    print("\n4. Valider TOUS les inputs utilisateurs:")
    print("   import re")
    print("   if not re.match(r'^[a-zA-Z0-9.-]+$', hostname):")
    print("       raise ValueError('Hostname invalide')")

    # Bonne pratique 5 : Capturer et logger les erreurs
    print("\n5. Capturer et analyser les erreurs:")
    print("   result = subprocess.run(cmd, capture_output=True, text=True)")
    print("   if result.returncode != 0:")
    print("       log_error(result.stderr)")

    # Bonne pratique 6 : Limiter les privilèges
    print("\n6. Limiter les privilèges du processus enfant:")
    print("   Ne pas utiliser sudo ou exécution en root si possible")
    print("   Utiliser les droits minimum nécessaires")


def popen_advanced_control():
    """
    Contrôle avancé avec subprocess.Popen()
    """
    print("\n" + "="*60)
    print("PARTIE 10 : CONTRÔLE AVANCÉ AVEC POPEN")
    print("="*60)

    # 1. Popen avec stdin/stdout/stderr
    print("\n1. Communication bidirectionnelle avec communicate():")
    process = subprocess.Popen(
        ['cat'],  # cat lit stdin et le reproduit sur stdout
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    input_text = "Ligne 1\nLigne 2\nLigne 3\n"
    stdout, stderr = process.communicate(input=input_text, timeout=2)
    print(f"   Input: {repr(input_text)}")
    print(f"   Output: {repr(stdout)}")

    # 2. Vérification non-bloquante avec poll()
    print("\n2. Vérification non-bloquante avec poll():")
    process = subprocess.Popen(['sleep', '1'])
    print(f"   Après lancement: poll() = {process.poll()}")
    time.sleep(0.5)
    print(f"   Après 0.5s: poll() = {process.poll()}")
    time.sleep(0.7)
    print(f"   Après 1.2s: poll() = {process.returncode}")

    # 3. Termination gracieuse vs forcée
    print("\n3. Différentes méthodes de termination:")

    # terminate()
    process = subprocess.Popen(['sleep', '100'])
    process.terminate()  # SIGTERM
    try:
        process.wait(timeout=1)
        print(f"   terminate() réussi")
    except subprocess.TimeoutExpired:
        process.kill()  # SIGKILL
        print(f"   kill() nécessaire")

    # 4. Pipes avec DEVNULL
    print("\n4. Suppression de la sortie avec DEVNULL:")
    process = subprocess.Popen(
        ['echo', 'sortie supprimée'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    process.wait()
    print(f"   Sortie supprimée pour une exécution discrète")


def main():
    """
    Fonction principale - Exécution de tous les exemples
    """
    print("\n" + "="*60)
    print("EXERCICE 16 : SUBPROCESS EN PYTHON")
    print("Module complet avec focus cybersécurité")
    print("="*60)

    # Exécuter tous les exemples
    introduction_subprocess()
    subprocess_run_vs_popen()
    capture_output_demo()
    shell_true_vs_false()
    command_injection_examples()
    timeout_and_signals()
    return_codes_demo()
    red_teaming_examples()
    security_best_practices()
    popen_advanced_control()

    # Résumé final
    print("\n" + "="*60)
    print("RÉSUMÉ DES CONCEPTS CLÉS")
    print("="*60)
    print("""
1. subprocess.run() : Interface recommandée pour la plupart des cas
2. subprocess.Popen() : Contrôle avancé et interaction asynchrone
3. TOUJOURS shell=False (par défaut)
4. JAMAIS shell=True avec entrées non-vérifiées
5. Implémenter des timeouts pour éviter les blocages
6. Valider et nettoyer TOUS les inputs
7. Capturer stdout/stderr pour analyse
8. Gérer les exceptions (TimeoutExpired, CalledProcessError)
9. Implémenter les protections de sécurité
10. Utiliser shlex.quote() si shell=True est nécessaire

AVERTISSEMENT: L'utilisation non-autorisée est illégale.
Utilisez ces connaissances de manière responsable et éthique.
    """)


if __name__ == "__main__":
    main()
