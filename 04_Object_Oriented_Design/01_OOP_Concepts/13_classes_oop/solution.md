# Exercice 13: Classes et Programmation Orientée Objet (OOP)
SOLUTIONS

## Solution Défi 1: Classe simple - Outil de scan de port

class PortScanner:
```python
    """Classe pour scanner les ports d'une adresse IP"""

    def __init__(self, ip):
        """Initialise le scanner avec une IP"""
        self.ip = ip
        self.ports_ouverts = []
        self.timestamp = "2024-11-07"

    def ajouter_port(self, port):
        """Ajoute un port à la liste des ports ouverts"""
        if port not in self.ports_ouverts:
            self.ports_ouverts.append(port)

    def afficher_ports(self):
        """Affiche tous les ports ouverts"""
        print(f"Ports ouverts sur {self.ip}: {self.ports_ouverts}")

    def nombre_ports(self):
        """Retourne le nombre de ports ouverts"""
        return len(self.ports_ouverts)

```
# Utilisation
scanner = PortScanner("192.168.1.1")
scanner.ajouter_port(22)
scanner.ajouter_port(80)
scanner.afficher_ports()
```python
print(f"Total: {scanner.nombre_ports()} ports")

```
Résultat :
Ports ouverts sur 192.168.1.1: [22, 80]
Total: 2 ports

## Solution Défi 2: Classe avec méthodes spéciales

class Vulnerabilite:
```python
    """Représente une vulnérabilité CVE"""

    def __init__(self, cve_id, severite, type_vuln):
        """Initialise une vulnérabilité"""
        self.cve_id = cve_id
        self.severite = severite
        self.type_vuln = type_vuln

    def __str__(self):
        """Retourne une chaîne lisible pour l'utilisateur"""
        return f"CVE-{self.cve_id}: Sévérité {self.severite}/10"

    def __repr__(self):
        """Retourne une représentation technique"""
        return f"Vulnerabilite('{self.cve_id}', {self.severite}, '{self.type_vuln}')"

    def __eq__(self, autre):
        """Compares deux vulnérabilités par CVE ID"""
        return self.cve_id == autre.cve_id

```
# Utilisation
vuln1 = Vulnerabilite("2024-1234", 9, "SQLi")
vuln2 = Vulnerabilite("2024-1234", 9, "SQLi")
```python
print(vuln1)  # CVE-2024-1234: Sévérité 9/10
print(repr(vuln1))  # Vulnerabilite('2024-1234', 9, 'SQLi')
print(vuln1 == vuln2)  # True

```
Résultat :
CVE-2024-1234: Sévérité 9/10
Vulnerabilite('2024-1234', 9, 'SQLi')
True

## Solution Défi 3: Héritage - Différents types d'attaques

class Attaque:
```python
    """Classe parente pour les attaques"""

    def __init__(self, nom, cible):
        """Initialise une attaque"""
        self.nom = nom
        self.cible = cible
        self.reussie = False

    def executer(self):
        """À implémenter dans les enfants"""
        raise NotImplementedError("executer() doit être implémentée")

    def rapport(self):
        """Génère un rapport"""
        print(f"[*] Rapport généré pour {self.nom}")

class SQLInjection(Attaque):
    """Classe enfant : SQL Injection"""

    def __init__(self, nom, cible, nom_table="users"):
        """Initialise une attaque SQL"""
        super().__init__(nom, cible)
        self.nom_table = nom_table
        self.donnees_extraites = []

    def executer(self):
        """Exécute l'injection SQL"""
        print(f"[!] Injection SQL sur {self.cible}...")
        self.reussie = True

    def extraire_donnees(self):
        """Extrait les données"""
        print(f"[+] Données extraites de {self.nom_table}")
        self.donnees_extraites.append(self.nom_table)

class BruteForce(Attaque):
    """Classe enfant : Force brute"""

    def __init__(self, nom, cible, nb_tentatives=1000):
        """Initialise une attaque brute force"""
        super().__init__(nom, cible)
        self.nb_tentatives = nb_tentatives
        self.tentative_actuelle = 0

    def executer(self):
        """Exécute la force brute"""
        print(f"[!] Force brute lancée sur {self.cible}")
        self.reussie = True

    def test_motdepasse(self, pwd):
        """Teste un mot de passe"""
        self.tentative_actuelle += 1
        print(f"[*] Test du mot de passe ({self.tentative_actuelle}/{ self.nb_tentatives}): {pwd}")

```
# Utilisation
sql = SQLInjection("Login_Form", "192.168.1.1")
sql.executer()
sql.rapport()
sql.extraire_donnees()

```python
print()

```
brute = BruteForce("Admin_Panel", "10.0.0.1")
brute.executer()
brute.test_motdepasse("admin")
brute.rapport()

Résultat :
[!] Injection SQL sur 192.168.1.1...
[*] Rapport généré pour Login_Form
[+] Données extraites de users

[!] Force brute lancée sur 10.0.0.1
[*] Test du mot de passe (1/1000): admin
[*] Rapport généré pour Admin_Panel

## Solution Défi 4: Encapsulation et modificateurs d'accès

```python
class ProjetSecurite:
    """Représente un projet de sécurité avec encapsulation"""

    def __init__(self, nom, deadline, budget):
        """Initialise un projet"""
        self.nom = nom
        self._deadline = deadline
        self.__budget = budget

    def get_budget(self):
        """Retourne le budget privé"""
        return self.__budget

    def set_budget(self, nouveau):
        """Change le budget avec validation"""
        if nouveau > 0:
            self.__budget = nouveau
            return True
        else:
            print("[-] Le budget doit être positif")
            return False

    def ajouter_depense(self, montant):
        """Soustrait une dépense du budget"""
        if montant > 0 and montant <= self.__budget:
            self.__budget -= montant
            print(f"[+] Dépense de {montant}€ enregistrée")
            return True
        else:
            print("[-] Montant invalide ou budget insuffisant")
            return False

    def afficher_info(self):
        """Affiche les informations du projet"""
        print(f"Projet: {self.nom}")
        print(f"  Deadline: {self._deadline}")
        print(f"  Budget: {self.__budget}")

```
# Utilisation
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

Résultat :
10000
[+] Dépense de 2500€ enregistrée
7500
Projet: PenTest-ACME
  Deadline: 2024-12-31
  Budget: 15000

## Solution Défi 5: Attributs et méthodes de classe

```python
import random

class Agent:
    """Représente un agent de sécurité"""

    nombre_agents = 0
    organisation = "SecTeam"

    def __init__(self, numero, nom, specialite):
        """Initialise un agent"""
        self.numero = numero
        self.nom = nom
        self.specialite = specialite
        Agent.nombre_agents += 1

    @classmethod
    def afficher_info_organisation(cls):
        """Affiche les infos de l'organisation"""
        print(f"[*] Organisation: {cls.organisation} - {cls.nombre_agents} agents")

    @classmethod
    def creer_agent_par_numero(cls, numero, nom, specialite):
        """Crée un agent (méthode de classe)"""
        return cls(numero, nom, specialite)

    @staticmethod
    def generer_id():
        """Génère un ID aléatoire"""
        return f"AGENT-{random.randint(10000, 99999)}"

    def profil(self):
        """Affiche le profil de l'agent"""
        print(f"[+] Agent #{self.numero}: {self.nom} ({self.specialite})")

```
# Utilisation
Agent.afficher_info_organisation()

agent1 = Agent(1, "Alice", "Pentesting")
agent2 = Agent(2, "Bob", "Forensics")
Agent.afficher_info_organisation()

```python
print(Agent.generer_id())
```
agent1.profil()

Résultat :
[*] Organisation: SecTeam - 0 agents
[*] Organisation: SecTeam - 2 agents
AGENT-75432
[+] Agent #1: Alice (Pentesting)

## Solution Défi 6: Polymorphisme - Différents outils de scan

class OutilScan:
```python
    """Classe parente pour les outils de scan"""

    def __init__(self, nom, cible):
        """Initialise un outil"""
        self.nom = nom
        self.cible = cible

    def executer(self):
        """À implémenter dans les enfants"""
        raise NotImplementedError("executer() doit être implémentée")

class NmapScan(OutilScan):
    """Outil de scan Nmap"""

    def executer(self):
        """Exécute un scan Nmap"""
        print(f"[*] Scan Nmap lancé sur {self.cible}")

class NessusScan(OutilScan):
    """Outil de scan Nessus"""

    def executer(self):
        """Exécute un scan Nessus"""
        print(f"[*] Scan Nessus lancé sur {self.cible}")

class BurpScan(OutilScan):
    """Outil de scan Burp"""

    def executer(self):
        """Exécute un scan Burp"""
        print(f"[*] Scan Burp lancé sur {self.cible}")

def executer_scans(outils):
    """Exécute une liste d'outils (polymorphisme)"""
    for outil in outils:
        outil.executer()

```
# Utilisation
outils = [
```python
    NmapScan("NetworkEnum", "192.168.1.0/24"),
    NessusScan("VulnScan", "192.168.1.1"),
    BurpScan("WebAppTest", "http://target.com")
```
]
executer_scans(outils)

Résultat :
[*] Scan Nmap lancé sur 192.168.1.0/24
[*] Scan Nessus lancé sur 192.168.1.1
[*] Scan Burp lancé sur http://target.com

## Solution Défi 7: Classe complexe - Système de rapports

```python
class RapportSecurite:
    """Représente un rapport de sécurité complet"""

    def __init__(self, titre, auteur, date):
        """Initialise un rapport"""
        self.__titre = titre
        self._auteur = auteur
        self.__date = date
        self.__vulnerabilites = []
        self.securite_score = 100

    def ajouter_vulnerabilite(self, cve, severite):
        """Ajoute une vulnérabilité au rapport"""
        self.__vulnerabilites.append({"cve": cve, "severite": severite})
        self.calculer_score()

    def supprimer_vulnerabilite(self, cve):
        """Supprime une vulnérabilité"""
        self.__vulnerabilites = [v for v in self.__vulnerabilites if v["cve"] != cve]
        self.calculer_score()

    def nombre_vulnerabilites(self, critiques_seulement=False):
        """Retourne le nombre de vulnérabilités"""
        if critiques_seulement:
            return sum(1 for v in self.__vulnerabilites if v["severite"] >= 8)
        return len(self.__vulnerabilites)

    def calculer_score(self):
        """Calcule le score de sécurité (0-100)"""
        if not self.__vulnerabilites:
            self.securite_score = 100
        else:
            penalite = sum(v["severite"] * 5 for v in self.__vulnerabilites)
            self.securite_score = max(0, 100 - penalite)

    def __str__(self):
        """Retourne une chaîne lisible"""
        return f"Rapport: {self.__titre} ({self.__date}) par {self._auteur}"

    def __lt__(self, autre):
        """Compare par score de sécurité"""
        return self.securite_score < autre.securite_score

    def export_dict(self):
        """Exporte le rapport sous forme de dictionnaire"""
        return {
            "titre": self.__titre,
            "auteur": self._auteur,
            "date": self.__date,
            "vulnerabilites": self.__vulnerabilites,
            "score": self.securite_score
        }

```
# Utilisation
rapport = RapportSecurite("Audit ACME", "Alice", "2024-11-07")
rapport.ajouter_vulnerabilite("2024-1111", 9)
rapport.ajouter_vulnerabilite("2024-2222", 5)
```python
print(rapport)
print(f"Score: {rapport.securite_score}")
print(f"Total: {rapport.nombre_vulnerabilites()} vulnérabilités")

```
Résultat :
Rapport: Audit ACME (2024-11-07) par Alice
Score: 30
Total: 2 vulnérabilités

## Solution Défi 8: Défi avancé - Gestionnaire de malwares

```python
from datetime import datetime

class Malware:
    """Représente un malware"""

    nombre_malwares = 0

    def __init__(self, hash_md5, nom, type_malware):
        """Initialise un malware"""
        self.hash_md5 = hash_md5
        self.nom = nom
        self.type_malware = type_malware
        self.__signature = f"sig_{hash_md5[:8]}"
        self.__date_decouverte = datetime.now().strftime("%Y-%m-%d")
        Malware.nombre_malwares += 1

    def __str__(self):
        """Chaîne lisible"""
        return f"Malware: {self.nom} ({self.type_malware})"

    def __repr__(self):
        """Représentation technique"""
        return f"Malware('{self.hash_md5}', '{self.nom}', '{self.type_malware}')"

    def __eq__(self, autre):
        """Compare par hash MD5"""
        return self.hash_md5 == autre.hash_md5

    def __lt__(self, autre):
        """Compare par date de découverte"""
        return self.__date_decouverte < autre.__date_decouverte

    def analyser(self):
        """Retourne un rapport d'analyse"""
        return f"[+] Malware analysé: {self.nom} - Signature: {self.__signature}"

class Echantillon:
    """Représente un échantillon de malware"""

    def __init__(self, malware, localisation):
        """Initialise un échantillon"""
        self.malware = malware
        self.localisation = localisation
        self.__source_infection = "Inconnue"
        self.__date_capture = datetime.now().strftime("%Y-%m-%d %H:%M")

    def obtenir_infos(self):
        """Retourne les infos de l'échantillon"""
        print(f"[*] Échantillon: {self.malware.nom}")
        print(f"    Localisation: {self.localisation}")
        print(f"    Date: {self.__date_capture}")

    def quarantainer(self):
        """Met en quarantaine"""
        print(f"[!] {self.malware.nom} mis en quarantaine")

class BaseDonneesMalware:
    """Gestionnaire de malwares"""

    def __init__(self):
        """Initialise la base"""
        self.base = []

    def ajouter_malware(self, malware):
        """Ajoute un malware"""
        if malware not in self.base:
            self.base.append(malware)

    def rechercher_par_hash(self, hash_md5):
        """Recherche un malware par hash"""
        for malware in self.base:
            if malware.hash_md5 == hash_md5:
                return malware
        return None

    def lister_par_type(self, type_malware):
        """Liste les malwares par type"""
        return [m for m in self.base if m.type_malware == type_malware]

    def compter_malwares(self):
        """Retourne le nombre de malwares"""
        return len(self.base)

    def afficher_tous(self):
        """Affiche tous les malwares"""
        for malware in self.base:
            print(f"[+] {malware}")

```
# Utilisation
malware1 = Malware("abc123def456", "Conficker", "worm")
malware2 = Malware("xyz789uvw012", "ZeroDay", "backdoor")

base = BaseDonneesMalware()
base.ajouter_malware(malware1)
base.ajouter_malware(malware2)

```python
print(f"{base.compter_malwares()} malwares dans la base")
```
base.afficher_tous()

resultat = base.rechercher_par_hash("abc123def456")
```python
if resultat:
    print(f"{resultat.nom} trouvé")

```
Résultat :
2 malwares dans la base
[+] Malware: Conficker (worm)
[+] Malware: ZeroDay (backdoor)
Conficker trouvé

POINTS IMPORTANTS À RETENIR :

1. CLASSES SIMPLES :
   - Définition avec 'class'
   - Constructeur __init__
   - Attributs et méthodes

2. HÉRITAGE :
   - super().__init__() pour appeler le parent
   - Polymorphisme automatique
   - Réutilisation du code parent

3. ENCAPSULATION :
   - _ pour les attributs protégés
   - __ pour les attributs privés (name mangling)
   - Méthodes get/set pour l'accès contrôlé

4. MÉTHODES SPÉCIALES :
   - __init__ : constructeur
   - __str__ : chaîne lisible (print)
   - __repr__ : représentation technique
   - __eq__ : comparaison ==
   - __lt__ : comparaison <
   - __len__ : longueur

5. MÉTHODES DE CLASSE :
   - @classmethod : accès à la classe
   - Attributs de classe : partagés

6. MÉTHODES STATIQUES :
   - @staticmethod : pas d'accès à self/cls
   - Utiles pour les fonctions utilitaires

7. POLYMORPHISME :
   - Différentes classes, même interface
   - Surcharge de méthodes dans les enfants
   - Traitement unifié de types différents

8. BONNES PRATIQUES :
   - Docstrings pour les classes et méthodes
   - Noms explicites pour attributs/méthodes
   - Encapsulation pour la sécurité
   - Utiliser l'héritage pour éviter la duplication
   - Implémenter les méthodes spéciales quand utile
