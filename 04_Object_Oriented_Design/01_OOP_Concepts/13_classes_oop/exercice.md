# Exercice 13: Classes et Programmation Orientée Objet (OOP)

## Défi 1: Classe simple - Outil de scan de port

Créez une classe `PortScanner` qui :
1. Prend en paramètre une adresse IP dans __init__
2. A les attributs : ip, ports_ouverts (liste), timestamp (chaîne)
3. Implément une méthode `ajouter_port(port)` qui ajoute un port à la liste
4. Implémente une méthode `afficher_ports()` qui affiche tous les ports trouvés
5. Implémente une méthode `nombre_ports()` qui retourne le nombre de ports

Utilisation :
scanner = PortScanner("192.168.1.1")
scanner.ajouter_port(22)
scanner.ajouter_port(80)
scanner.afficher_ports()
```python
print(f"Total: {scanner.nombre_ports()} ports")

```
Attendu :
Ports ouverts sur 192.168.1.1: [22, 80]
Total: 2 ports

## Défi 2: Classe avec méthodes spéciales (__str__, __repr__)

Créez une classe `Vulnerabilite` qui :
1. Prend en paramètre : cve_id (chaîne), severite (1-10), type_vuln
2. Implémente __init__ pour initialiser les attributs
3. Implémente __str__() pour retourner: "CVE-XXXX: Sévérité X/10"
4. Implémente __repr__() pour retourner: "Vulnerabilite('CVE-XXXX', X, 'type')"
5. Implémente __eq__() pour comparer deux vulnérabilités par cve_id

Utilisation :
vuln1 = Vulnerabilite("2024-1234", 9, "SQLi")
vuln2 = Vulnerabilite("2024-1234", 9, "SQLi")
```python
print(vuln1)  # CVE-2024-1234: Sévérité 9/10
print(repr(vuln1))  # Vulnerabilite('2024-1234', 9, 'SQLi')
print(vuln1 == vuln2)  # True

```
Attendu :
CVE-2024-1234: Sévérité 9/10
Vulnerabilite('2024-1234', 9, 'SQLi')
True

## Défi 3: Héritage - Différents types d'attaques

Créez une classe parente `Attaque` et deux classes enfants :
1. Classe parente `Attaque` :
   - Attributs : nom, cible, reussie (False par défaut)
   - Méthode : executer() (à implémenter dans les enfants)
   - Méthode : rapport() qui affiche "[*] Rapport générér pour (nom)"

2. Classe `SQLInjection(Attaque)` :
   - Attribut additionnel : nom_table
   - Implémente executer() qui affiche "[!] Injection SQL sur (cible)..."
   - Méthode specifique : extraire_donnees() qui affiche "[+] Données extraites"

3. Classe `BruteForce(Attaque)` :
   - Attribut additionnel : nb_tentatives
   - Implémente executer() qui affiche "[!] Force brute lancée"
   - Méthode specifique : test_motdepasse(pwd) qui teste un mot de passe

Utilisation :
sql = SQLInjection("Login_Form", "192.168.1.1")
sql.executer()
sql.rapport()
sql.extraire_donnees()

brute = BruteForce("Admin_Panel", "10.0.0.1")
brute.executer()
brute.test_motdepasse("admin")
brute.rapport()

## Défi 4: Encapsulation et modificateurs d'accès

Créez une classe `ProjetSecurite` qui :
1. Attributs publics : nom (chaîne)
2. Attributs protégés : _deadline (chaîne - "YYYY-MM-DD")
3. Attributs privés : __budget (nombre)
4. Méthodes :
   - __init__(nom, deadline, budget)
   - get_budget() qui retourne le budget privé
   - set_budget(nouveau) qui change le budget avec validation (>0)
   - ajouter_depense(montant) qui soustrait du budget
   - afficher_info() qui affiche tous les détails

Utilisation :
projet = ProjetSecurite("PenTest-ACME", "2024-12-31", 10000)
```python
print(projet.get_budget())  # 10000
```
projet.ajouter_depense(2500)
```python
print(projet.get_budget())  # 7500
```
projet.set_budget(15000)
projet.afficher_info()

Attendu :
10000
7500
Projet: PenTest-ACME
  Deadline: 2024-12-31
  Budget: 15000

## Défi 5: Attributs et méthodes de classe

Créez une classe `Agent` qui :
1. Attribut de classe : nombre_agents = 0
2. Attribut de classe : organisation = "SecTeam"
3. Attributs d'instance : numero (unique), nom, specialite
4. __init__ increment number_agents
5. @classmethod : afficher_info_organisation() qui affiche les infos de classe
6. @classmethod : creer_agent_par_numero(numero, nom, specialite)
7. @staticmethod : generer_id() qui retourne un ID aléatoire
8. Méthode : profil() qui affiche les infos de l'agent

Utilisation :
Agent.afficher_info_organisation()

agent1 = Agent(1, "Alice", "Pentesting")
agent2 = Agent(2, "Bob", "Forensics")
Agent.afficher_info_organisation()

```python
print(Agent.generer_id())
```
agent1.profil()

Attendu :
[*] Organisation: SecTeam - 0 agents
[*] Organisation: SecTeam - 2 agents
[+] Agent #1: Alice (Pentesting)

## Défi 6: Polymorphisme - Différents outils de scan

Créez une classe abstraite `OutilScan` et plusieurs implémentations :
1. Classe parente `OutilScan` :
   - Attributs : nom, cible
   - Méthode abstraite : executer()

2. Classe `NmapScan(OutilScan)` :
   - Implémente executer() : "[*] Scan Nmap lancé..."

3. Classe `NessusScan(OutilScan)` :
   - Implémente executer() : "[*] Scan Nessus lancé..."

4. Classe `BurpScan(OutilScan)` :
   - Implémente executer() : "[*] Scan Burp lancé..."

Créez une fonction qui :
- Prend une liste d'outils
- Exécute chaque outil
- Affiche le résultat pour chaque

Utilisation :
outils = [
```python
    NmapScan("NetworkEnum", "192.168.1.0/24"),
    NessusScan("VulnScan", "192.168.1.1"),
    BurpScan("WebAppTest", "http://target.com")
```
]
executer_scans(outils)

Attendu :
[*] Scan Nmap lancé sur 192.168.1.0/24
[*] Scan Nessus lancé sur 192.168.1.1
[*] Scan Burp lancé sur http://target.com

## Défi 7: Classe complexe - Système de rapports

Créez une classe `RapportSecurite` qui :
1. Attributs :
   - __titre (privé)
   - __date (privé)
   - __vulnerabilites (privé - liste)
   - _auteur (protégé)
   - securite_score (public - 0-100)

2. Méthodes :
   - __init__(titre, auteur, date)
   - ajouter_vulnerabilite(cve, severite)
   - supprimer_vulnerabilite(cve)
   - nombre_vulnerabilites() (critiques en paramètre optionnel)
   - __str__() pour affichage lisible
   - __lt__() pour comparer par securite_score
   - export_dict() qui retourne un dictionnaire
   - calculer_score() qui calcule le score de sécurité

Utilisation :
rapport = RapportSecurite("Audit ACME", "Alice", "2024-11-07")
rapport.ajouter_vulnerabilite("2024-1111", 9)
rapport.ajouter_vulnerabilite("2024-2222", 5)
```python
print(rapport)
print(f"Score: {rapport.calculer_score()}")
print(f"Total: {rapport.nombre_vulnerabilites()} vulnérabilités")

```
Attendu :
Rapport: Audit ACME (2024-11-07) par Alice
Score: 45
Total: 2 vulnérabilités

## Défi 8: Défi avancé - Gestionnaire de malwares

Créez un système de gestion de malwares avec 3 classes :
1. Classe `Malware` :
   - Attributs : hash_md5, nom, type (trojan/worm/virus/backdoor)
   - Attributs privés : __signature, __date_decouverte
   - Attribut de classe : nombre_malwares
   - Méthodes spéciales : __str__, __repr__, __eq__, __lt__ (par date)
   - Méthode : analyser() qui retourne un rapport

2. Classe `Echantillon` :
   - Attributs : malware (objet Malware), localisation
   - Attributs privés : __source_infection, __date_capture
   - Méthodes : obtenir_infos(), quarantainer()

3. Classe `BaseDonneesMalware` :
   - Attribut de classe : base = []
   - Méthodes :
```python
     - ajouter_malware(malware)
     - rechercher_par_hash(hash)
     - lister_par_type(type)
     - compter_malwares()
     - afficher_tous()

```
Utilisation :
malware1 = Malware("abc123def456", "Conficker", "worm")
malware2 = Malware("xyz789uvw012", "ZeroDay", "backdoor")

base = BaseDonneesMalware()
base.ajouter_malware(malware1)
base.ajouter_malware(malware2)

```python
print(base.compter_malwares())  # 2
```
base.afficher_tous()
```python
print(base.rechercher_par_hash("abc123def456"))

```
Attendu :
2 malwares dans la base
[+] Malware: Conficker (worm)
[+] Malware: ZeroDay (backdoor)
Conficker trouvé

## Conseils :
1. Commencez par les défis 1 et 2 (classes simples)
2. Progressez vers l'héritage (défis 3)
3. Maîtrisez l'encapsulation (défi 4)
4. Explorez les méthodes de classe (défi 5)
5. Comprenez le polymorphisme (défi 6)
6. Intégrez tous les concepts (défis 7 et 8)

RESSOURCES :
- Lisez le main.py en détail
- Testez chaque exemple
- Modifiez le code pour comprendre
- Utilisez dir() et type() pour explorer les objets
- Écrivez des docstrings pour documenter votre code
