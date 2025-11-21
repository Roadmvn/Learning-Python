"""
═══════════════════════════════════════════════════════════════
EXERCICE 13 : Classes et Programmation Orientée Objet (OOP)
═══════════════════════════════════════════════════════════════

OBJECTIF :
- Maîtriser la définition de classes
- Comprendre __init__ et l'initialisation d'attributs
- Utiliser self pour accéder aux attributs et méthodes
- Créer des méthodes d'instance et des attributs de classe
- Implémenter l'héritage
- Comprendre l'encapsulation
- Utiliser les méthodes spéciales __str__, __repr__, __eq__
- Appliquer aux contextes de cybersécurité (scanning, exploits, payloads)

EXÉCUTION : python main.py

═══════════════════════════════════════════════════════════════
"""


def main():
    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 1 : Définition basique d'une classe
    # ═══════════════════════════════════════════════════════════

    print("=== Étape 1 : Définition basique d'une classe ===\n")

    # Une classe est un modèle pour créer des objets (instances)
    # Elle encapsule des attributs (données) et des méthodes (fonctions)
    #
    # Syntaxe :
    # class NomClasse:
    #     def __init__(self, ...):
    #         # Initialisation
    #     def methode(self):
    #         # Logique
    #
    # Création d'instance : objet = NomClasse(...)

    class Serveur:
        """Représente un serveur à scanner"""

        def __init__(self, adresse_ip):
            """
            Constructeur : appelé automatiquement lors de la création
            self fait référence à l'instance en cours de création
            """
            self.adresse_ip = adresse_ip
            self.ports_ouverts = []
            self.services = {}

        def ajouter_port_ouvert(self, port):
            """Méthode d'instance : accède à self"""
            self.ports_ouverts.append(port)
            print(f"[+] Port {port} ajouté pour {self.adresse_ip}")

        def afficher_info(self):
            """Affiche les informations du serveur"""
            print(f"\n[*] Serveur : {self.adresse_ip}")
            print(f"[*] Ports ouverts : {self.ports_ouverts}")

    # Créer deux instances (objets) de la classe Serveur
    serveur1 = Serveur("192.168.1.1")
    serveur2 = Serveur("10.0.0.1")

    # Utiliser les méthodes d'instance
    serveur1.ajouter_port_ouvert(22)
    serveur1.ajouter_port_ouvert(80)
    serveur1.ajouter_port_ouvert(443)
    serveur1.afficher_info()

    serveur2.ajouter_port_ouvert(3306)
    serveur2.afficher_info()

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 2 : Le constructeur __init__ et les attributs
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 2 : Le constructeur __init__ et les attributs ===\n")

    class Cible:
        """Représente une cible de penetration test"""

        def __init__(self, nom, systeme, difficulte):
            """
            __init__ est le constructeur.
            Il est appelé automatiquement lors de la création d'un objet.
            Il initialise les attributs d'instance.
            """
            # Les attributs d'instance sont uniques pour chaque objet
            self.nom = nom
            self.systeme = systeme
            self.difficulte = difficulte  # "Facile", "Moyen", "Difficile"
            self.exploites = False
            self.informations_recoltes = []

        def afficher_details(self):
            """Affiche les détails de la cible"""
            print(f"Cible: {self.nom}")
            print(f"  Système: {self.systeme}")
            print(f"  Difficulté: {self.difficulte}")
            print(f"  Exploitée: {'Oui' if self.exploites else 'Non'}")
            if self.informations_recoltes:
                print(f"  Infos: {', '.join(self.informations_recoltes)}")

    # Créer plusieurs cibles
    cible1 = Cible("WebApp1", "Linux", "Facile")
    cible2 = Cible("DBServer", "Windows", "Difficile")
    cible3 = Cible("FTP_Old", "Linux", "Moyen")

    print("[*] Cibles trouvées :\n")
    cible1.afficher_details()
    print()
    cible2.afficher_details()
    print()
    cible3.afficher_details()

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 3 : self - Référence à l'instance
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 3 : self - Référence à l'instance ===\n")

    class Payload:
        """Représente un payload d'exploitation"""

        def __init__(self, nom, type_attack, taille):
            """self fait référence à l'instance en cours"""
            self.nom = nom
            self.type_attack = type_attack  # "RCE", "SQLi", "XSS"
            self.taille = taille  # en octets
            self.exécuté = False

        def executer(self):
            """
            Les méthodes d'instance reçoivent self automatiquement.
            self permet d'accéder aux attributs et méthodes de l'instance.
            """
            self.exécuté = True
            print(f"[!] Exécution du payload {self.nom}...")
            print(f"[!] Type: {self.type_attack}")
            print(f"[!] Taille: {self.taille} bytes")

        def info_execution(self):
            """Affiche l'état d'exécution"""
            if self.exécuté:
                print(f"[+] {self.nom} a été exécuté avec succès")
            else:
                print(f"[-] {self.nom} n'a pas été exécuté")

    # Créer et exécuter des payloads
    payload1 = Payload("shell_reversh", "RCE", 256)
    payload2 = Payload("union_select", "SQLi", 128)

    payload1.executer()
    payload2.info_execution()  # N'a pas été exécuté
    print()
    payload2.executer()
    payload2.info_execution()  # Maintenant exécuté

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 4 : Attributs de classe vs Attributs d'instance
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 4 : Attributs de classe vs Attributs d'instance ===\n")

    class Exploit:
        """Représente un exploit - CVE"""

        # Attribut de classe : partagé par toutes les instances
        # Utile pour les constantes, compteurs, etc.
        nombre_exploits = 0
        version = "1.0"

        def __init__(self, cve_id, severite):
            """Attributs d'instance : uniques pour chaque objet"""
            self.cve_id = cve_id
            self.severite = severite  # "Critique", "Haute", "Moyenne"
            self.patche = False
            # Incrémenter le compteur de classe
            Exploit.nombre_exploits += 1

        def afficher_statut(self):
            print(f"CVE-{self.cve_id} (Sévérité: {self.severite})")
            print(f"  Patché: {'Oui' if self.patche else 'Non'}")

        @classmethod
        def afficher_nombre_exploits(cls):
            """Accès à la classe elle-même"""
            print(f"\n[*] Exploits connus: {cls.nombre_exploits}")
            print(f"[*] Version: {cls.version}")

    # Créer plusieurs exploits
    exploit1 = Exploit("2024-1234", "Critique")
    exploit2 = Exploit("2024-5678", "Haute")
    exploit3 = Exploit("2024-9999", "Moyenne")

    exploit1.afficher_statut()
    print()
    exploit2.afficher_statut()

    # Appeler une méthode de classe
    Exploit.afficher_nombre_exploits()

    # Accéder directement à un attribut de classe
    print(f"[*] Version globale: {Exploit.version}")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 5 : Héritage (Inheritance)
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 5 : Héritage (Inheritance) ===\n")

    class VecteurAttaque:
        """Classe parente : définit une interface commune"""

        def __init__(self, nom, plateforme):
            self.nom = nom
            self.plateforme = plateforme  # "Web", "Network", "Physical"
            self.reussi = False

        def executer(self):
            """Méthode à implémenter dans les classes enfants"""
            print(f"[*] Exécution du vecteur {self.nom}...")

    class SQLInjection(VecteurAttaque):
        """Classe enfant : hérite de VecteurAttaque"""

        def __init__(self, nom, plateforme, base_de_donnees):
            # super() appelle le constructeur de la classe parente
            super().__init__(nom, plateforme)
            # Attributs spécifiques à SQLInjection
            self.base_de_donnees = base_de_donnees
            self.donnees_extraites = []

        def extraire_donnees(self, table):
            """Méthode spécifique à SQLInjection"""
            print(f"[+] Extraction de la table {table}...")
            self.donnees_extraites.append(table)
            self.reussi = True

    class XSS(VecteurAttaque):
        """Une autre classe enfant"""

        def __init__(self, nom, plateforme, type_xss):
            super().__init__(nom, plateforme)
            self.type_xss = type_xss  # "Stored", "Reflected", "DOM"
            self.payload_injecte = False

        def injecter_payload(self, payload):
            print(f"[+] Injection du payload XSS {self.type_xss}: {payload}")
            self.payload_injecte = True
            self.reussi = True

    # Créer des instances des classes enfants
    sql_attack = SQLInjection("SQLi_DVWA", "Web", "MySQL")
    sql_attack.executer()
    sql_attack.extraire_donnees("users")
    sql_attack.extraire_donnees("passwords")
    print(f"  Tables extraites: {sql_attack.donnees_extraites}")

    print()

    xss_attack = XSS("XSS_OWASP", "Web", "Stored")
    xss_attack.executer()
    xss_attack.injecter_payload("<script>alert('pwned')</script>")
    print(f"  Payload injecté: {xss_attack.payload_injecte}")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 6 : Encapsulation et modificateurs d'accès
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 6 : Encapsulation et modificateurs d'accès ===\n")

    class Credentials:
        """Représente des identifiants avec encapsulation"""

        def __init__(self, username, password):
            # Attributs publics (convention : pas de préfixe)
            self.username = username

            # Attributs privés (convention : préfixe __)
            # Python applique le name mangling pour les protéger
            self.__password = password

            # Attributs protégés (convention : préfixe _)
            # Simple convention, accessible mais pas recommandé
            self._attempts = 0

        def verifier_password(self, tentative):
            """Méthode pour vérifier le mot de passe de manière sécurisée"""
            self._attempts += 1
            if tentative == self.__password:
                print(f"[+] Mot de passe correct après {self._attempts} tentative(s)")
                return True
            else:
                print(f"[-] Mot de passe incorrect (tentative {self._attempts})")
                if self._attempts >= 3:
                    print("[!] Compte verrouillé après 3 tentatives")
                return False

        def get_password(self):
            """Getter : permet l'accès contrôlé"""
            return self.__password

        def change_password(self, ancien, nouveau):
            """Setter : permet la modification contrôlée"""
            if ancien == self.__password:
                self.__password = nouveau
                print("[+] Mot de passe changé avec succès")
                return True
            else:
                print("[-] Ancien mot de passe incorrect")
                return False

    # Utiliser la classe avec encapsulation
    creds = Credentials("admin", "SuperSecret123")
    print(f"[*] Utilisateur: {creds.username}")

    # Vérifier le mot de passe
    creds.verifier_password("wrong")
    creds.verifier_password("wrong2")
    creds.verifier_password("SuperSecret123")

    # Changer le mot de passe
    print()
    creds.change_password("SuperSecret123", "NewPassword456")
    creds.change_password("wrong", "AnotherPassword")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 7 : Méthodes spéciales (__str__, __repr__, __eq__)
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 7 : Méthodes spéciales ===\n")

    class ScanResult:
        """Résultat d'un scan de sécurité"""

        def __init__(self, ip, ports_ouverts, risque_level):
            self.ip = ip
            self.ports_ouverts = ports_ouverts  # liste
            self.risque_level = risque_level  # 1-10
            self.timestamp = "2024-11-07"

        def __str__(self):
            """
            Méthode spéciale : retourne une chaîne lisible pour l'utilisateur.
            Utilisée par print() et str()
            """
            return f"Scan {self.ip}: {len(self.ports_ouverts)} ports, Risque: {self.risque_level}/10"

        def __repr__(self):
            """
            Méthode spéciale : retourne une représentation technique.
            Utile pour le débogage et les logs.
            """
            return f"ScanResult('{self.ip}', {self.ports_ouverts}, {self.risque_level})"

        def __eq__(self, autre):
            """
            Méthode spéciale : définit la comparaison avec ==.
            Permet de comparer deux objets ScanResult.
            """
            return (self.ip == autre.ip and
                    self.ports_ouverts == autre.ports_ouverts and
                    self.risque_level == autre.risque_level)

        def __lt__(self, autre):
            """
            Méthode spéciale : définit la comparaison < (inférieur à).
            Utile pour le tri basé sur le niveau de risque.
            """
            return self.risque_level < autre.risque_level

        def __len__(self):
            """Méthode spéciale : permet d'utiliser len()"""
            return len(self.ports_ouverts)

    # Créer plusieurs résultats de scan
    scan1 = ScanResult("192.168.1.1", [22, 80, 443], 7)
    scan2 = ScanResult("10.0.0.1", [3306, 5432], 9)
    scan3 = ScanResult("172.16.0.1", [22, 80, 443], 7)
    scan4 = ScanResult("10.1.1.1", [21, 25, 53], 8)

    # Utiliser __str__
    print("[*] Utilisation de __str__ (lisible pour l'utilisateur) :")
    print(f"  {scan1}")
    print(f"  {scan2}")

    # Utiliser __repr__
    print("\n[*] Utilisation de __repr__ (représentation technique) :")
    print(f"  repr(scan1): {repr(scan1)}")

    # Utiliser __eq__
    print("\n[*] Utilisation de __eq__ (comparaison) :")
    print(f"  scan1 == scan3: {scan1 == scan3}")
    print(f"  scan1 == scan2: {scan1 == scan2}")

    # Utiliser __lt__ et trier
    print("\n[*] Utilisation de __lt__ (tri par risque) :")
    scans = [scan1, scan2, scan3, scan4]
    print(f"  Avant tri: {[s.risque_level for s in scans]}")
    scans_tries = sorted(scans)
    print(f"  Après tri : {[s.risque_level for s in scans_tries]}")

    # Utiliser __len__
    print("\n[*] Utilisation de __len__ (nombre de ports) :")
    print(f"  len(scan1): {len(scan1)} ports")
    print(f"  len(scan2): {len(scan2)} ports")

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 8 : Polymorphisme (Polymorphism)
    # ═══════════════════════════════════════════════════════════

    print("\n=== Étape 8 : Polymorphisme (Polymorphism) ===\n")

    class TechniqueAttack:
        """Classe de base pour les techniques d'attaque"""

        def executer(self):
            """À surcharger dans les classes enfants"""
            raise NotImplementedError("execute() doit être implémentée")

        def rapport(self):
            """Méthode commune"""
            print("[*] Rapport d'attaque généré")

    class BruteForce(TechniqueAttack):
        """Attaque par force brute"""

        def __init__(self, target, wordlist_size):
            self.target = target
            self.wordlist_size = wordlist_size
            self.reussie = False

        def executer(self):
            """Implémentation spécifique"""
            print(f"[*] Lancement du brute force sur {self.target}")
            print(f"[*] Wordlist: {self.wordlist_size} entrées")
            print("[+] Mot de passe trouvé: password123")
            self.reussie = True

    class RainbowTable(TechniqueAttack):
        """Attaque par rainbow table"""

        def __init__(self, target, table_size):
            self.target = target
            self.table_size = table_size
            self.reussie = False

        def executer(self):
            """Implémentation spécifique"""
            print(f"[*] Requête dans la rainbow table pour {self.target}")
            print(f"[*] Taille de la table: {self.table_size} GB")
            print("[+] Hash trouvé dans la table: admin123")
            self.reussie = True

    class Wordlist(TechniqueAttack):
        """Attaque avec dictionnaire"""

        def __init__(self, target, wordlist_path):
            self.target = target
            self.wordlist_path = wordlist_path

        def executer(self):
            """Implémentation spécifique"""
            print(f"[*] Chargement du dictionnaire: {self.wordlist_path}")
            print(f"[*] Test des mots de passe sur {self.target}")
            print("[+] Accès obtenu avec le mot de passe: qwerty")

    # Polymorphisme : une fonction qui accepte n'importe quelle technique
    def lancer_attaque(technique):
        """
        Le polymorphisme permet d'utiliser une seule fonction
        avec différents types d'objets.
        """
        print("[!] ====== Lancement de l'attaque ======")
        technique.executer()
        technique.rapport()
        print()

    # Utiliser le polymorphisme
    brute = BruteForce("admin@localhost", 100000)
    rainbow = RainbowTable("admin@localhost", 50)
    wordlist = Wordlist("admin@localhost", "/usr/share/wordlists/rockyou.txt")

    lancer_attaque(brute)
    lancer_attaque(rainbow)
    lancer_attaque(wordlist)

    # ═══════════════════════════════════════════════════════════
    # ÉTAPE 9 : Méthodes statiques et de classe
    # ═══════════════════════════════════════════════════════════

    print("=== Étape 9 : Méthodes statiques et de classe ===\n")

    class UtilsSecurite:
        """Classe utilitaire avec méthodes statiques et de classe"""

        version = "2.0"
        outils_utilises = []

        @staticmethod
        def hacher_password(password):
            """
            Méthode statique : pas d'accès à self ou cls.
            Utile pour les fonctions utilitaires.
            """
            # Simulation d'un hachage (en vrai on utiliserait bcrypt)
            hache = f"hash_{password[:3]}_{len(password)}"
            return hache

        @staticmethod
        def valider_ip(ip):
            """Valide une adresse IP (simplifié)"""
            parties = ip.split(".")
            if len(parties) != 4:
                return False
            for partie in parties:
                try:
                    n = int(partie)
                    if not (0 <= n <= 255):
                        return False
                except ValueError:
                    return False
            return True

        @classmethod
        def ajouter_outil(cls, nom_outil):
            """
            Méthode de classe : accès à la classe elle-même.
            Utile pour modifier les attributs de classe.
            """
            cls.outils_utilises.append(nom_outil)
            print(f"[+] Outil '{nom_outil}' ajouté")

        @classmethod
        def afficher_infos(cls):
            """Affiche les informations de classe"""
            print(f"\n[*] Infos de sécurité :")
            print(f"  Version: {cls.version}")
            print(f"  Outils utilisés: {', '.join(cls.outils_utilises)}")

    # Utiliser les méthodes statiques (pas besoin d'instance)
    print("[*] Tests des méthodes statiques :")
    print(f"  hacher_password('secret123'): {UtilsSecurite.hacher_password('secret123')}")
    print(f"  valider_ip('192.168.1.1'): {UtilsSecurite.valider_ip('192.168.1.1')}")
    print(f"  valider_ip('256.1.1.1'): {UtilsSecurite.valider_ip('256.1.1.1')}")

    # Utiliser les méthodes de classe
    print("\n[*] Tests des méthodes de classe :")
    UtilsSecurite.ajouter_outil("Nmap")
    UtilsSecurite.ajouter_outil("Metasploit")
    UtilsSecurite.ajouter_outil("Burp Suite")
    UtilsSecurite.afficher_infos()

    # ═══════════════════════════════════════════════════════════
    # RÉSUMÉ ET CONCEPTS CLÉS
    # ═══════════════════════════════════════════════════════════

    print("\n" + "=" * 60)
    print("RÉSUMÉ : CONCEPTS CLÉS DE LA POO")
    print("=" * 60)

    resume = """
1. CLASSE : Modèle pour créer des objets
   - Syntax: class NomClasse:

2. __init__ : Constructeur appelé à la création
   - Initialise les attributs d'instance
   - Argument spécial : self

3. self : Référence à l'instance courante
   - Accès aux attributs : self.attribut
   - Appel de méthodes : self.methode()

4. ATTRIBUTS :
   - D'instance : uniques pour chaque objet
   - De classe : partagés par toutes les instances

5. MÉTHODES :
   - D'instance : reçoivent self
   - De classe : @classmethod, reçoivent cls
   - Statiques : @staticmethod, indépendantes

6. HÉRITAGE : Une classe hérite d'une autre
   - Syntax: class EnfantClass(ParentClass):
   - super() : appelle la méthode parente

7. ENCAPSULATION : Protection des données
   - Public : pas de préfixe
   - Protégé : préfixe _
   - Privé : préfixe __

8. MÉTHODES SPÉCIALES : Personnalisent le comportement
   - __str__() : chaîne lisible
   - __repr__() : représentation technique
   - __eq__() : comparaison ==
   - __lt__() : comparaison <

9. POLYMORPHISME : Méthodes différentes selon le type
   - Même interface, implémentations différentes
   - Permet de traiter différents types uniformément

10. AVANTAGES DE LA POO :
    - Modularité
    - Réutilisabilité
    - Maintenabilité
    - Flexibilité
    - Organisation du code
    """
    print(resume)


if __name__ == "__main__":
    main()
