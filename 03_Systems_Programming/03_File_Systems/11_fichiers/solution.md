# Exercice 11: Gestion de Fichiers - Solutions

SOLUTION 1 : Créer et lire un fichier simple

"""
Créer un fichier avec du contenu et le lire avec 'with'
"""

# Créer et écrire
```python
print("Création du fichier notes.txt...")
```
with open('notes.txt', 'w') as f:
```python
    f.write("Première note\n")
    f.write("Deuxième note\n")
    f.write("Troisième note\n")
    f.write("Quatrième note\n")
    f.write("Cinquième note\n")

print("Fichier créé : notes.txt")

```
# Lire et afficher
```python
print("\nContenu du fichier :")
```
with open('notes.txt', 'r') as f:
```python
    lignes = f.readlines()
    for i, ligne in enumerate(lignes, 1):
        print(f"  {i}. {ligne.strip()}")

print(f"Total de lignes : {len(lignes)}")

```
# Nettoyer
import os
os.remove('notes.txt')

SOLUTION 2 : Modifier un fichier existant

"""
Créer un fichier, l'ajouter et afficher les modifications
"""

```python
import os

```
# Étape 1 : Créer avec le mode 'w'
```python
print("Création du fichier log.txt (3 lignes)...")
```
with open('log.txt', 'w') as f:
```python
    f.write("Ligne initiale 1\n")
    f.write("Ligne initiale 2\n")
    f.write("Ligne initiale 3\n")

```
# Compter les lignes initiales
with open('log.txt', 'r') as f:
```python
    lignes_avant = f.readlines()
    nombre_avant = len(lignes_avant)

print(f"Fichier initial : {nombre_avant} lignes")

```
# Étape 2 : Ajouter avec le mode 'a'
```python
print("Ajout de 2 lignes au fichier...")
```
with open('log.txt', 'a') as f:
```python
    f.write("Ligne ajoutée 1\n")
    f.write("Ligne ajoutée 2\n")

```
# Compter après modification
with open('log.txt', 'r') as f:
```python
    lignes_apres = f.readlines()
    nombre_apres = len(lignes_apres)

print(f"Fichier après ajout : {nombre_apres} lignes")

```
# Afficher le contenu final
```python
print("\nContenu final :")
for i, ligne in enumerate(lignes_apres, 1):
    print(f"  [{i}] {ligne.strip()}")

```
# Nettoyer
os.remove('log.txt')

SOLUTION 3 : Lire un fichier ligne par ligne et compter les mots

"""
Analyser un fichier pour compter les mots par ligne
"""

```python
import os

```
# Créer le fichier de test
```python
print("Création du fichier texte.txt...")
```
contenu = [
```python
    "Ceci est une phrase\n",
    "Cette ligne contient plus de mots\n",
    "Et celle-ci aussi\n",
    "Pour un total complet\n"
```
]

with open('texte.txt', 'w') as f:
```python
    f.writelines(contenu)

print("Analyse du fichier texte.txt\n")

```
# Analyser le fichier
total_mots = 0
with open('texte.txt', 'r') as f:
```python
    for num_ligne, ligne in enumerate(f, 1):
        # Compter les mots (split sur les espaces)
        mots = ligne.strip().split()
        nombre_mots = len(mots)
        total_mots += nombre_mots

        print(f"Ligne {num_ligne} ({nombre_mots} mots) : {ligne.strip()}")

print(f"\nTotal : {total_mots} mots")

```
# Nettoyer
os.remove('texte.txt')

SOLUTION 4 : Copier un fichier

"""
Copier le contenu d'un fichier à un autre
"""

```python
import os

```
# Créer le fichier source
```python
print("Création du fichier source.txt...")
```
contenu_source = "Ceci est le contenu du fichier source.\nDeuxième ligne du fichier source.\n"

with open('source.txt', 'w') as f:
```python
    f.write(contenu_source)

print("Fichier source créé : source.txt")

```
# Vérifier l'existence
existe_source = os.path.exists('source.txt')
```python
print(f"Fichier source existe : {existe_source}")

```
# Copier le fichier
```python
print("\nCopie en cours...")
```
with open('source.txt', 'r') as src:
```python
    contenu = src.read()

```
with open('destination.txt', 'w') as dst:
```python
    dst.write(contenu)

print("Fichier destination créé par copie")

```
# Vérifier l'existence
existe_destination = os.path.exists('destination.txt')
```python
print(f"Fichier destination existe : {existe_destination}")

```
# Vérifier que le contenu est identique
with open('source.txt', 'r') as src:
```python
    contenu_src = src.read()

```
with open('destination.txt', 'r') as dst:
```python
    contenu_dst = dst.read()

```
identique = contenu_src == contenu_dst
```python
print(f"Contenu identique : {identique}")
print(f"Nombre de caractères : {len(contenu_src)}")

```
# Afficher le contenu
```python
print("\nContenu du fichier source :")
```
with open('source.txt', 'r') as f:
```python
    print(f.read())

print("Contenu du fichier destination :")
```
with open('destination.txt', 'r') as f:
```python
    print(f.read())

```
# Nettoyer
os.remove('source.txt')
os.remove('destination.txt')

SOLUTION 5 : Travailler avec JSON - Configuration d'attaque

"""
Créer, charger et modifier une configuration en JSON
"""

```python
import json
import os

```
# Créer la configuration
```python
print("Création de la configuration d'attaque...")

```
config = {
```python
    "campagne": "Pentest XYZ",
    "cibles": ["192.168.1.1", "192.168.1.2"],
    "techniques": ["scan", "exploitation", "post-exploitation"],
    "resultats": {
        "ports_ouverts": [80, 443, 22],
        "vulnerabilites": []
    }
```
}

# Sauvegarder en JSON
with open('config.json', 'w') as f:
```python
    json.dump(config, f, indent=2)

print("Configuration créée et sauvegardée")

```
# Charger et afficher
with open('config.json', 'r') as f:
```python
    config_chargee = json.load(f)

print(f"\nCampagne : {config_chargee['campagne']}")
print(f"Cibles : {len(config_chargee['cibles'])}")
print(f"Techniques : {len(config_chargee['techniques'])}")
print(f"Vulnérabilités : {len(config_chargee['resultats']['vulnerabilites'])}")

```
# Ajouter une vulnérabilité
```python
print("\nAjout d'une vulnérabilité...")
```
config_chargee['resultats']['vulnerabilites'].append({
```python
    "id": "CVE-2024-1234",
    "severite": "CRITICAL"
```
})

# Sauvegarder à nouveau
with open('config.json', 'w') as f:
```python
    json.dump(config_chargee, f, indent=2)

print("Fichier mis à jour")
print(f"Vulnérabilités : {len(config_chargee['resultats']['vulnerabilites'])}")

```
# Afficher le JSON
```python
print("\nFichier config.json :")
```
with open('config.json', 'r') as f:
```python
    print(f.read())

```
# Nettoyer
os.remove('config.json')

SOLUTION 6 : Travailler avec les chemins (os.path et pathlib)

"""
Utiliser os.path et pathlib pour manipuler les chemins
"""

```python
import os
from pathlib import Path

```
# Afficher le répertoire courant
rep_courant = os.getcwd()
```python
print(f"Répertoire courant : {rep_courant}")

```
# Construire le chemin avec os.path.join()
chemin_os = os.path.join(rep_courant, 'data', 'fichier.txt')
```python
print(f"Chemin os.path : {chemin_os}")

```
# Construire le chemin avec pathlib
chemin_pathlib = Path(rep_courant) / 'data' / 'fichier.txt'
```python
print(f"Chemin pathlib : {chemin_pathlib}")

```
# Vérifier si c'est identique
identiques = str(chemin_pathlib) == chemin_os
```python
print(f"Chemins identiques : {identiques}")

```
# Extraire les composants avec os.path
```python
print(f"\nExtraits avec os.path :")
print(f"  Répertoire parent : {os.path.dirname(chemin_os)}")
print(f"  Nom du fichier : {os.path.basename(chemin_os)}")

```
# Extraire les composants avec pathlib
p = Path(chemin_os)
```python
print(f"\nExtraits avec pathlib :")
print(f"  Répertoire parent : {p.parent}")
print(f"  Nom du fichier : {p.name}")
print(f"  Extension : {p.suffix}")

```
SOLUTION 7 : Créer un gestionnaire de logs avec timestamps

"""
Créer un fichier de logs avec timestamps et filtrer les résultats
"""

```python
import os
from datetime import datetime, timedelta

```
# Créer le fichier de logs
```python
print("Création du fichier attack_log.txt...")

```
# Simulation de logs avec timestamps
logs = []
temps_base = datetime.now()

logs.append(f"[{(temps_base + timedelta(seconds=0)).strftime('%Y-%m-%d %H:%M:%S')}] [INFO] Démarrage du scanner")
logs.append(f"[{(temps_base + timedelta(seconds=15)).strftime('%Y-%m-%d %H:%M:%S')}] [INFO] Énumération en cours")
logs.append(f"[{(temps_base + timedelta(seconds=45)).strftime('%Y-%m-%d %H:%M:%S')}] [WARN] Port 22 : SSH détecté")
logs.append(f"[{(temps_base + timedelta(seconds=60)).strftime('%Y-%m-%d %H:%M:%S')}] [INFO] Scan des services")
logs.append(f"[{(temps_base + timedelta(seconds=90)).strftime('%Y-%m-%d %H:%M:%S')}] [ERROR] Erreur de connexion au port 3389")
logs.append(f"[{(temps_base + timedelta(seconds=120)).strftime('%Y-%m-%d %H:%M:%S')}] [WARN] Vulnérabilité détectée : OpenSSH outdated")
logs.append(f"[{(temps_base + timedelta(seconds=150)).strftime('%Y-%m-%d %H:%M:%S')}] [SUCCESS] Accès obtenu en SSH")
logs.append(f"[{(temps_base + timedelta(seconds=180)).strftime('%Y-%m-%d %H:%M:%S')}] [SUCCESS] Escalade de privilèges réussie")

# Écrire les logs
with open('attack_log.txt', 'w') as f:
    for log in logs:
```python
        f.write(log + '\n')

print(f"Log créé avec {len(logs)} entrées")

```
# Lire et afficher les logs
```python
print(f"\nLogs totaux : {len(logs)}")

```
# Lire le fichier
with open('attack_log.txt', 'r') as f:
```python
    contenu = f.read()

```
# Filtrer les logs [SUCCESS]
```python
print("\nLogs [SUCCESS] :")
for ligne in contenu.split('\n'):
    if '[SUCCESS]' in ligne:
        print(f"  {ligne}")

```
# Compter par type
```python
print("\nStatistiques :")
```
types_log = ['[INFO]', '[WARN]', '[ERROR]', '[SUCCESS]']
```python
for type_log in types_log:
    count = contenu.count(type_log)
    print(f"  {type_log} : {count}")

```
# Nettoyer
os.remove('attack_log.txt')

SOLUTION 8 : Red Teaming - Scanner complet avec résultats en JSON

"""
Scanner complet de red teaming avec logs, JSON et rapport
"""

```python
import json
import os
from datetime import datetime, timedelta

print("█" * 79)
print("█" + " " * 77 + "█")
print("█" + "  RED TEAMING SCANNER - RÉSULTATS COMPLETS".center(77) + "█")
print("█" + " " * 77 + "█")
print("█" * 79)
print()

```
# ═══════════════════════════════════════════════════════════════════════════
# 1. ÉNUMÉRATION SYSTÈME
# ═══════════════════════════════════════════════════════════════════════════

```python
print("[*] Énumération système")
print("-" * 79)

```
rep_courant = os.getcwd()
utilisateur = os.getenv('USER') or 'N/A'

```python
print(f"Répertoire : {rep_courant}")
print(f"Utilisateur : {utilisateur}")
print()

```
# ═══════════════════════════════════════════════════════════════════════════
# 2. LOGS D'ATTAQUE
# ═══════════════════════════════════════════════════════════════════════════

```python
print("[*] Logs d'attaque")
print("-" * 79)

```
temps_base = datetime.now()
logs_attaque = []

logs_attaque.append(f"[{temps_base.strftime('%Y-%m-%d %H:%M:%S')}] [INFO] Démarrage du scanner")
logs_attaque.append(f"[{(temps_base + timedelta(seconds=5)).strftime('%Y-%m-%d %H:%M:%S')}] [INFO] Énumération de 192.168.1.0/24")
logs_attaque.append(f"[{(temps_base + timedelta(seconds=10)).strftime('%Y-%m-%d %H:%M:%S')}] [SCAN] Host découvert : 192.168.1.1")
logs_attaque.append(f"[{(temps_base + timedelta(seconds=15)).strftime('%Y-%m-%d %H:%M:%S')}] [SCAN] Port 22 (SSH) ouvert sur 192.168.1.1")
logs_attaque.append(f"[{(temps_base + timedelta(seconds=20)).strftime('%Y-%m-%d %H:%M:%S')}] [SCAN] Port 80 (HTTP) ouvert sur 192.168.1.1")
logs_attaque.append(f"[{(temps_base + timedelta(seconds=25)).strftime('%Y-%m-%d %H:%M:%S')}] [SCAN] Port 443 (HTTPS) ouvert sur 192.168.1.1")
logs_attaque.append(f"[{(temps_base + timedelta(seconds=30)).strftime('%Y-%m-%d %H:%M:%S')}] [VULN] CVE-2024-0001 détectée (CRITICAL)")
logs_attaque.append(f"[{(temps_base + timedelta(seconds=35)).strftime('%Y-%m-%d %H:%M:%S')}] [VULN] CVE-2024-0002 détectée (HIGH)")
logs_attaque.append(f"[{(temps_base + timedelta(seconds=40)).strftime('%Y-%m-%d %H:%M:%S')}] [EXPLOIT] Exploitation réussie")
logs_attaque.append(f"[{(temps_base + timedelta(seconds=45)).strftime('%Y-%m-%d %H:%M:%S')}] [SUCCESS] Accès administrateur obtenu")

# Sauvegarder les logs
with open('scan_log.txt', 'w') as f:
```python
    for log in logs_attaque:
        f.write(log + '\n')

print(f"Fichier créé : scan_log.txt")
print(f"Entrées : {len(logs_attaque)}")
print()

```
# ═══════════════════════════════════════════════════════════════════════════
# 3. RÉSULTATS DE SCAN EN JSON
# ═══════════════════════════════════════════════════════════════════════════

```python
print("[*] Résultats de scan")
print("-" * 79)

```
resultats_scan = {
```python
    "scan_id": "SCAN-20241107-001",
    "timestamp": temps_base.isoformat(),
    "cible": "192.168.1.1",
    "hosts_decouverts": [
        {
            "ip": "192.168.1.1",
            "mac": "00:11:22:33:44:55",
            "os": "Linux",
            "ports_ouverts": [22, 80, 443]
        },
        {
            "ip": "192.168.1.100",
            "mac": "AA:BB:CC:DD:EE:FF",
            "os": "Windows",
            "ports_ouverts": [445, 3389]
        }
    ],
    "vulnerabilites": [
        {
            "cve": "CVE-2024-0001",
            "severite": "CRITICAL",
            "host": "192.168.1.1"
        },
        {
            "cve": "CVE-2024-0002",
            "severite": "HIGH",
            "host": "192.168.1.1"
        }
    ]
```
}

# Sauvegarder en JSON
with open('scan_results.json', 'w') as f:
```python
    json.dump(resultats_scan, f, indent=2)

print(f"Scan ID : {resultats_scan['scan_id']}")
print(f"Cible : {resultats_scan['cible']}")
print(f"Hosts découverts : {len(resultats_scan['hosts_decouverts'])}")

```
# Compter les ports
ports_totaux = sum(len(h['ports_ouverts']) for h in resultats_scan['hosts_decouverts'])
```python
print(f"Ports totaux : {ports_totaux}")
print(f"Vulnérabilités : {len(resultats_scan['vulnerabilites'])}")
print()

```
# ═══════════════════════════════════════════════════════════════════════════
# 4. ANALYSE DÉTAILLÉE
# ═══════════════════════════════════════════════════════════════════════════

```python
print("[*] Vulnérabilités par sévérité")
print("-" * 79)

```
severites = {}
```python
for vuln in resultats_scan['vulnerabilites']:
    sev = vuln['severite']
    severites[sev] = severites.get(sev, 0) + 1

for sev in ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW']:
    count = severites.get(sev, 0)
    if count > 0:
        print(f"{sev} : {count}")

print()

```
# ═══════════════════════════════════════════════════════════════════════════
# 5. RAPPORT TEXTE
# ═══════════════════════════════════════════════════════════════════════════

```python
print("[*] Génération du rapport")
print("-" * 79)

```
rapport = f"""
RAPPORT DE SCAN DE SÉCURITÉ - RED TEAMING

INFORMATIONS GÉNÉRALES
Scan ID : {resultats_scan['scan_id']}
Timestamp : {resultats_scan['timestamp']}
Cible principale : {resultats_scan['cible']}
Nombre de hosts : {len(resultats_scan['hosts_decouverts'])}

RÉSUMÉ DES DÉCOUVERTES
Ports ouverts : {ports_totaux}
Vulnérabilités : {len(resultats_scan['vulnerabilites'])}

HOSTS DÉCOUVERTS
"""

```python
for host in resultats_scan['hosts_decouverts']:
    rapport += f"""
```
Host : {host['ip']}
  MAC Address : {host['mac']}
  Système : {host['os']}
  Ports ouverts : {', '.join(map(str, host['ports_ouverts']))}
"""

rapport += f"""
VULNÉRABILITÉS
"""

```python
for vuln in resultats_scan['vulnerabilites']:
    rapport += f"""
```
{vuln['cve']} ({vuln['severite']})
  Host : {vuln['host']}
"""

rapport += """
CONCLUSION
Scan complété avec succès. Les résultats détaillés sont disponibles dans
scan_results.json.

"""

# Sauvegarder le rapport
with open('rapport.txt', 'w') as f:
```python
    f.write(rapport)

print("Rapport généré : rapport.txt")
print()

```
# ═══════════════════════════════════════════════════════════════════════════
# 6. FIN
# ═══════════════════════════════════════════════════════════════════════════

```python
print("[+] Scanner complété avec succès")
print("=" * 79)
print()
print("Fichiers générés :")
print("  - scan_log.txt (logs d'attaque)")
print("  - scan_results.json (résultats détaillés)")
print("  - rapport.txt (rapport textuel)")
print()

```
# Nettoyer
os.remove('scan_log.txt')
os.remove('scan_results.json')
os.remove('rapport.txt')

