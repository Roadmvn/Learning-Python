# Exercice 09: Fonctions - Solutions

## Solution Défi 1: Fonction de conversion de température

```python
def celsius_to_fahrenheit(celsius):
    """
    Convertit une température de Celsius à Fahrenheit.

    Arguments:
        celsius (float): Température en Celsius

    Retour:
        float: Température en Fahrenheit

    Exemple:
        >>> celsius_to_fahrenheit(0)
        32.0
        >>> celsius_to_fahrenheit(100)
        212.0
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

```
# Tests
```python
print(celsius_to_fahrenheit(0))    # 32.0
print(celsius_to_fahrenheit(100))  # 212.0
print(celsius_to_fahrenheit(-40))  # -40.0

## Solution Défi 2: Calculatrice avec *args

def calculs(*nombres):
    """
    Effectue des calculs statistiques sur un ensemble de nombres.

    Paramètres:
        *nombres: Nombre variable de nombres

    Retour:
        tuple: (somme, moyenne, min, max) ou None si pas d'argument
    """
    if not nombres:
        return None, None, None, None

    somme = sum(nombres)
    moyenne = somme / len(nombres)
    minimum = min(nombres)
    maximum = max(nombres)

    return somme, moyenne, minimum, maximum

```
# Tests
resultat1 = calculs(1, 2, 3)
```python
print(resultat1)  # (6, 2.0, 1, 3)

```
resultat2 = calculs(10, 20, 30, 40, 50)
```python
print(resultat2)  # (150, 30.0, 10, 50)

```
somme, moyenne, mini, maxi = calculs(5, 10, 15)
```python
print(f"Somme: {somme}, Moyenne: {moyenne}, Min: {mini}, Max: {maxi}")

## Solution Défi 3: Configurateur d'outil de scan avec **kwargs

def configurer_scanner(**options):
    """
    Configure un scanner avec les options fournies.

    Paramètres:
        **options: Configuration personnalisée
    """
    # Configuration par défaut
    config_defaut = {
        "timeout": 5,
        "retries": 3,
        "verbose": False,
        "threads": 1
    }

    # Mettre à jour avec les options personnalisées
    config_defaut.update(options)

    # Afficher la configuration
    print("[*] Configuration du scanner :")
    for cle, valeur in config_defaut.items():
        print(f"    {cle}: {valeur}")

    return config_defaut

```
# Tests
```python
print("=== Configuration par défaut ===")
```
configurer_scanner()

```python
print("\n=== Configuration personnalisée ===")
```
configurer_scanner(timeout=10, verbose=True)

```python
print("\n=== Configuration partiellement personnalisée ===")
```
configurer_scanner(threads=4, timeout=15)

## Solution Défi 4: Vérificateur de force de mot de passe avancé

```python
def verifier_force_mdp(mdp):
    """
    Évalue la force d'un mot de passe.

    Arguments:
        mdp (str): Le mot de passe à vérifier

    Retour:
        int: Score de force (0-100)
    """
    score = 0

    # Critères de longueur
    if len(mdp) >= 8:
        score += 10
    if len(mdp) >= 12:
        score += 10
    if len(mdp) >= 16:
        score += 10

    # Critères de contenu
    if any(c.isupper() for c in mdp):
        score += 15
    if any(c.islower() for c in mdp):
        score += 15
    if any(c.isdigit() for c in mdp):
        score += 15

    # Caractères spéciaux
    caracteres_speciaux = "!@#$%^&*()_+-=[]{}|;:,.<>?/"
    if any(c in caracteres_speciaux for c in mdp):
        score += 15

    # Vérifier les caractères répétés
    if len(mdp) == len(set(mdp)):
        score += 10

    # Limiter le score à 100
    score = min(score, 100)

    # Générer le rapport
    print(f"[*] Analyse du mot de passe : {mdp[:3]}{'*' * (len(mdp)-3)}")
    print(f"    Longueur : {len(mdp)}")
    print(f"    Majuscules : {'✓' if any(c.isupper() for c in mdp) else '✗'}")
    print(f"    Minuscules : {'✓' if any(c.islower() for c in mdp) else '✗'}")
    print(f"    Chiffres : {'✓' if any(c.isdigit() for c in mdp) else '✗'}")
    print(f"    Caractères spéciaux : {'✓' if any(c in caracteres_speciaux for c in mdp) else '✗'}")
    print(f"    Score final : {score}/100")

    if score < 40:
        force = "FAIBLE"
    elif score < 70:
        force = "MOYEN"
    else:
        force = "FORT"

    print(f"    Force : {force}")

    return score

```
# Tests
verifier_force_mdp("password")
print()
verifier_force_mdp("MyPassword123")
print()
verifier_force_mdp("P@ssw0rd!Complex#2024")

## Solution Défi 5: Analyseur de logs avec filtrage

```python
def analyser_logs(logs, filtre_fonction):
    """
    Filtre une liste de logs selon une fonction de filtrage.

    Arguments:
        logs (list): Liste des logs
        filtre_fonction (function): Fonction lambda pour filtrer

    Retour:
        list: Logs filtrés
    """
    return list(filter(filtre_fonction, logs))

```
# Exemple de données
logs = [
```python
    "[INFO] Utilisateur Alice connecté",
    "[ERROR] Erreur de connexion",
    "[WARNING] Tentative d'accès non autorisé",
    "[INFO] Scan complété",
    "[ERROR] Service indisponible"
```
]

# Différents filtres
```python
print("[*] Logs d'erreur :")
```
logs_erreurs = analyser_logs(logs, lambda x: "[ERROR]" in x)
```python
for log in logs_erreurs:
    print(f"  {log}")

print("\n[*] Logs d'information :")
```
logs_info = analyser_logs(logs, lambda x: "[INFO]" in x)
```python
for log in logs_info:
    print(f"  {log}")

print("\n[*] Logs longs (> 30 caractères) :")
```
logs_longs = analyser_logs(logs, lambda x: len(x) > 30)
```python
for log in logs_longs:
    print(f"  {log}")

print("\n[*] Logs contenant 'connecté' :")
```
logs_connexion = analyser_logs(logs, lambda x: "connecté" in x.lower())
```python
for log in logs_connexion:
    print(f"  {log}")

## Solution Défi 6: Décorateur de fonction (advanced)

def executer_avec_log(fonction, *args, **kwargs):
    """
    Exécute une fonction en affichant des logs de début et fin.

    Arguments:
        fonction: La fonction à exécuter
        *args: Arguments positionnels
        **kwargs: Arguments nommés

    Retour:
        Le résultat de la fonction exécutée
    """
    nom_fonction = fonction.__name__

    print(f"[*] Exécution de {nom_fonction}")

    try:
        resultat = fonction(*args, **kwargs)
        print(f"[+] {nom_fonction} terminée")
        return resultat
    except Exception as e:
        print(f"[-] {nom_fonction} a échoué : {e}")
        return None

```
# Exemples
```python
def greet(nom):
    return f"Bonjour {nom}"

def additionner(a, b):
    return a + b

def calculer(x, y, operation="add"):
    if operation == "add":
        return x + y
    elif operation == "mul":
        return x * y
    else:
        raise ValueError("Opération inconnue")

```
# Tests
resultat1 = executer_avec_log(greet, "Alice")
```python
print(f"Résultat : {resultat1}\n")

```
resultat2 = executer_avec_log(additionner, 10, 20)
```python
print(f"Résultat : {resultat2}\n")

```
resultat3 = executer_avec_log(calculer, 5, 3, operation="mul")
```python
print(f"Résultat : {resultat3}\n")

## Solution Défi 7: Générateur de signatures de requête HTTP

def generer_signature(url, methode="GET", **headers):
    """
    Génère la signature d'une requête HTTP.

    Arguments:
        url (str): L'URL cible
        methode (str): La méthode HTTP (par défaut: GET)
        **headers: Headers personnalisés

    Retour:
        str: Signature formatée
    """
    signature = f"{methode} {url}\n"

    # Ajouter les headers personnalisés
    for cle, valeur in headers.items():
        # Remplacer les tirets par des tirets (format standard)
        cle_formate = cle.replace("_", "-").title()
        signature += f"{cle_formate}: {valeur}\n"

    return signature.rstrip()

```
# Tests
```python
print("[*] Signature GET simple :")
```
sig1 = generer_signature("http://example.com/api")
```python
print(sig1)

print("\n[*] Signature POST avec headers :")
```
sig2 = generer_signature(
```python
    "http://example.com/api",
    "POST",
    User_Agent="CustomBot/1.0",
    Authorization="Bearer token123",
    Content_Type="application/json"
```
)
```python
print(sig2)

print("\n[*] Signature avec custom headers :")
```
sig3 = generer_signature(
```python
    "https://api.target.com/v2/users",
    "DELETE",
    X_Custom_Header="value123",
    Authorization="Bearer token123"
```
)
```python
print(sig3)

## Solution Défi 8: Scanner de vulnérabilités avec red teaming

def scan_service(host, *ports, severity="CRITICAL", **options):
    """
    Scanne les services et vulnérabilités sur une cible.

    Arguments:
        host (str): L'adresse IP ou domaine à scanner
        *ports: Ports à scanner
        severity (str): Niveau de sévérité minimum à rapporter
        **options: Options de scan (timeout, verbose, etc.)

    Retour:
        dict: Rapport de scan
    """
    # Configuration par défaut
    timeout = options.get("timeout", 5)
    verbose = options.get("verbose", False)
    method = options.get("method", "SYN")

    # Mapping des ports aux services
    services_mapping = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        80: "HTTP",
        443: "HTTPS",
        3306: "MySQL",
        5432: "PostgreSQL",
        8080: "Tomcat"
    }

    # Mapping des vulnérabilités
    vulnerabilites_mapping = {
        21: {"id": "CVE-2010-4221", "score": 6.5, "nom": "FTP Bounce"},
        22: {"id": "CVE-2018-15473", "score": 5.3, "nom": "User enumeration"},
        80: {"id": "CVE-2021-28169", "score": 7.5, "nom": "HTTP Smuggling"},
        443: {"id": "CVE-2021-41773", "score": 7.5, "nom": "Path Traversal"},
        3306: {"id": "CVE-2021-2109", "score": 9.8, "nom": "Authentication Bypass"},
    }

    # Niveaux de sévérité
    niveaux_severite = {"CRITICAL": 7.0, "HIGH": 6.0, "MEDIUM": 4.0, "LOW": 2.0}
    seuil_severite = niveaux_severite.get(severity, 7.0)

    rapport = {
        "host": host,
        "ports_scannes": list(ports),
        "methode": method,
        "timeout": timeout,
        "services": {},
        "vulnerabilites": [],
        "risque_global": 0
    }

    # Affichage du scan
    if verbose:
        print(f"[*] SCAN DÉBUTÉ")
        print(f"    Cible : {host}")
        print(f"    Ports : {', '.join(map(str, ports))}")
        print(f"    Méthode : {method}")
        print(f"    Timeout : {timeout}s")
        print()

    max_score = 0

    # Scanner chaque port
    for port in ports:
        service = services_mapping.get(port, "Inconnu")
        rapport["services"][port] = {
            "nom": service,
            "statut": "OUVERT"
        }

        if verbose:
            print(f"[+] Port {port} : {service} (OUVERT)")

        # Vérifier les vulnérabilités
        if port in vulnerabilites_mapping:
            vuln = vulnerabilites_mapping[port]
            if vuln["score"] >= seuil_severite:
                vuln_info = {
                    "port": port,
                    "service": service,
                    "cve": vuln["id"],
                    "nom": vuln["nom"],
                    "score": vuln["score"]
                }
                rapport["vulnerabilites"].append(vuln_info)

                if verbose:
                    print(f"    [!] CVE trouvée : {vuln['id']} ({vuln['nom']})")
                    print(f"        Score : {vuln['score']}/10")

                max_score = max(max_score, vuln["score"])

    # Calculer le risque global
    if rapport["vulnerabilites"]:
        risque_global = max_score
    else:
        risque_global = 0

    rapport["risque_global"] = risque_global

    # Évaluation du risque
    if risque_global >= 7.0:
        evaluation = "CRITIQUE"
    elif risque_global >= 6.0:
        evaluation = "ÉLEVÉ"
    elif risque_global >= 4.0:
        evaluation = "MOYEN"
    else:
        evaluation = "FAIBLE"

    rapport["evaluation"] = evaluation

    if verbose:
        print()
        print(f"[*] RÉSULTATS DU SCAN")
        print(f"    Services trouvés : {len(rapport['services'])}")
        print(f"    Vulnérabilités : {len(rapport['vulnerabilites'])}")
        print(f"    Risque global : {evaluation} ({risque_global:.1f}/10)")

    return rapport

```
# Tests
```python
print("=" * 60)
print("SCAN 1 : Scan standard")
print("=" * 60)
```
resultat1 = scan_service(
    "192.168.1.100",
    22, 80, 443,
    severity="HIGH",
    verbose=True,
    timeout=10
)

```python
print("\n" + "=" * 60)
print("SCAN 2 : Scan complet")
print("=" * 60)
```
resultat2 = scan_service(
    "10.0.0.1",
```python
    21, 22, 80, 443, 3306,
    severity="MEDIUM",
    verbose=True,
    method="CONNECT",
    timeout=15
```
)

# Afficher le rapport en format JSON-like
```python
import json

print("\n" + "=" * 60)
print("RAPPORT DÉTAILLÉ - SCAN 1")
print("=" * 60)
print(json.dumps(resultat1, indent=2, ensure_ascii=False))

```