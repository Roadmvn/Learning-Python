"""
═══════════════════════════════════════════════════════════════════════════════
EXERCICE 12 : Gestion d'Exceptions
═══════════════════════════════════════════════════════════════════════════════

OBJECTIF :
- Maîtriser try/except/else/finally
- Gérer les types d'exceptions spécifiques
- Créer des exceptions personnalisées
- Appliquer aux contextes de cybersécurité et red teaming

EXÉCUTION : python main.py

═══════════════════════════════════════════════════════════════════════════════
"""

# ═════════════════════════════════════════════════════════════════════════════
# ÉTAPE 1 : try/except basique
# ═════════════════════════════════════════════════════════════════════════════

def etape1_try_except_basique():
    """Démonstration du bloc try/except basique."""

    print("═" * 79)
    print("ÉTAPE 1 : try/except basique")
    print("═" * 79)
    print()

    # EXEMPLE 1 : Conversion de chaîne en entier
    print("Exemple 1 : Conversion de chaîne en entier")
    print("-" * 40)

    # Sans gestion d'exception, le programme crash
    # numero = int("abc")  # Lève ValueError

    # Avec gestion d'exception, le programme continue
    try:
        numero = int("abc")  # Ceci lève une exception
    except ValueError:
        # Ce bloc s'exécute si ValueError est levée
        print("Erreur : la chaîne 'abc' ne peut pas être convertie en nombre")
        numero = 0

    print(f"Valeur finale : {numero}")
    print()

    # EXEMPLE 2 : Accès à une liste
    print("Exemple 2 : Accès à un index invalide")
    print("-" * 40)

    try:
        liste = [1, 2, 3]
        element = liste[10]  # Index invalide, lève IndexError
    except IndexError:
        print("Erreur : l'index 10 est en dehors de la liste")
        element = None

    print(f"Élément : {element}")
    print()

    # EXEMPLE 3 : Accès à un dictionnaire
    print("Exemple 3 : Accès à une clé manquante")
    print("-" * 40)

    try:
        utilisateurs = {"alice": "password123", "bob": "secret"}
        mot_passe = utilisateurs["charlie"]  # Clé manquante, lève KeyError
    except KeyError:
        print("Erreur : l'utilisateur 'charlie' n'existe pas")
        mot_passe = None

    print(f"Mot de passe : {mot_passe}")
    print()


# ═════════════════════════════════════════════════════════════════════════════
# ÉTAPE 2 : try/except avec capture du message d'erreur
# ═════════════════════════════════════════════════════════════════════════════

def etape2_capture_message_erreur():
    """Capture du message d'erreur avec 'as'."""

    print("═" * 79)
    print("ÉTAPE 2 : Capture du message d'erreur (as)")
    print("═" * 79)
    print()

    # EXEMPLE 1 : Afficher le message d'erreur
    print("Exemple 1 : Afficher le détail de l'erreur")
    print("-" * 40)

    try:
        resultat = 10 / 0  # ZeroDivisionError
    except ZeroDivisionError as erreur:
        # On capture l'objet exception dans 'erreur'
        print(f"Exception levée : {type(erreur).__name__}")
        print(f"Message : {erreur}")

    print()

    # EXEMPLE 2 : Parsing JSON (simulation)
    print("Exemple 2 : Parsing de données")
    print("-" * 40)

    def parser_entier(texte):
        try:
            return int(texte)
        except ValueError as e:
            print(f"Impossible de convertir '{texte}' : {e}")
            return None

    resultat = parser_entier("42")
    print(f"Succès : {resultat}")

    resultat = parser_entier("xyz")
    print(f"Échoué : {resultat}")

    print()


# ═════════════════════════════════════════════════════════════════════════════
# ÉTAPE 3 : Exceptions multiples
# ═════════════════════════════════════════════════════════════════════════════

def etape3_exceptions_multiples():
    """Gestion de plusieurs types d'exceptions."""

    print("═" * 79)
    print("ÉTAPE 3 : Exceptions multiples")
    print("═" * 79)
    print()

    # EXEMPLE 1 : Capturer avec un tuple
    print("Exemple 1 : Capturer plusieurs exceptions avec un tuple")
    print("-" * 40)

    def operation_risquee(operation):
        try:
            if operation == "division":
                resultat = 10 / 0  # ZeroDivisionError
            elif operation == "conversion":
                resultat = int("abc")  # ValueError
            elif operation == "index":
                resultat = [1, 2][10]  # IndexError
        except (ValueError, ZeroDivisionError, IndexError) as e:
            print(f"Erreur capturée : {e}")
            resultat = None

        return resultat

    print("Division :", operation_risquee("division"))
    print("Conversion :", operation_risquee("conversion"))
    print("Index :", operation_risquee("index"))
    print()

    # EXEMPLE 2 : Handlers différents pour chaque exception
    print("Exemple 2 : Handlers différents pour chaque exception")
    print("-" * 40)

    def traiter_donnees(donnees):
        try:
            # Étape 1 : Parser les données
            nombre = int(donnees)  # ValueError possible
            # Étape 2 : Calculer quelque chose
            resultat = 100 / nombre  # ZeroDivisionError possible
            # Étape 3 : Accéder à un index
            liste = [1, 2, 3]
            element = liste[nombre]  # IndexError possible
        except ValueError as e:
            print(f"Erreur de parsing : {e}")
        except ZeroDivisionError as e:
            print(f"Erreur de calcul : {e}")
        except IndexError as e:
            print(f"Erreur d'index : {e}")

    traiter_donnees("0")
    traiter_donnees("2")
    traiter_donnees("100")
    print()


# ═════════════════════════════════════════════════════════════════════════════
# ÉTAPE 4 : try/except/else
# ═════════════════════════════════════════════════════════════════════════════

def etape4_try_except_else():
    """Utiliser 'else' pour le code si aucune exception."""

    print("═" * 79)
    print("ÉTAPE 4 : try/except/else")
    print("═" * 79)
    print()

    print("Exemple : Traiter une conversion réussie différemment")
    print("-" * 40)

    def entrer_nombre(invite):
        try:
            # Tentative de conversion
            numero = int(input(invite))
        except ValueError:
            # Si la conversion échoue
            print("Erreur : Ce n'est pas un nombre valide")
            numero = None
        else:
            # Ce bloc s'exécute SEULEMENT si aucune exception
            print(f"Conversion réussie : {numero}")
            numero = numero * 2

        return numero

    # Simulation sans input réel
    print("Simulation 1 : Chaîne valide")
    try:
        numero = int("42")
        print(f"Conversion réussie : {numero}")
        numero = numero * 2
        print(f"Résultat après doublement : {numero}")
    except ValueError:
        print("Erreur : Ce n'est pas un nombre valide")
        numero = None

    print()

    print("Simulation 2 : Chaîne invalide")
    try:
        numero = int("abc")
        print(f"Conversion réussie : {numero}")
        numero = numero * 2
    except ValueError:
        print("Erreur : Ce n'est pas un nombre valide")
        numero = None

    print()


# ═════════════════════════════════════════════════════════════════════════════
# ÉTAPE 5 : try/except/finally
# ═════════════════════════════════════════════════════════════════════════════

def etape5_try_except_finally():
    """Le bloc 'finally' s'exécute toujours."""

    print("═" * 79)
    print("ÉTAPE 5 : try/except/finally")
    print("═" * 79)
    print()

    # EXEMPLE 1 : Fermer un fichier même en cas d'erreur
    print("Exemple 1 : Gestion de ressources (fichier)")
    print("-" * 40)

    def lire_fichier(chemin):
        fichier = None
        try:
            fichier = open(chemin, "r")
            print(f"Fichier '{chemin}' ouvert")
            contenu = fichier.read()
            print(f"Contenu lu : {len(contenu)} caractères")
        except FileNotFoundError:
            print(f"Erreur : Le fichier '{chemin}' n'existe pas")
            contenu = None
        except IOError as e:
            print(f"Erreur d'entrée/sortie : {e}")
            contenu = None
        finally:
            # Ce bloc s'exécute TOUJOURS, même en cas d'exception
            if fichier is not None and not fichier.closed:
                fichier.close()
                print(f"Fichier fermé correctement")

        return contenu

    # Tester avec un fichier inexistant
    resultat = lire_fichier("/tmp/fichier_inexistant_12345.txt")
    print()

    # EXEMPLE 2 : Bloc finally sans exception
    print("Exemple 2 : Finally même sans erreur")
    print("-" * 40)

    def operation_securisee():
        try:
            print("Début de l'opération")
            numero = int("42")
            resultat = numero * 2
            print(f"Résultat : {resultat}")
        except ValueError:
            print("Erreur de conversion")
        finally:
            print("Nettoyage des ressources (toujours exécuté)")

    operation_securisee()
    print()

    # EXEMPLE 3 : Utiliser une variable dans finally
    print("Exemple 3 : Utiliser les variables du try dans finally")
    print("-" * 40)

    def processus_complet():
        donnees = None
        try:
            donnees = {"utilisateur": "alice", "mot_passe": "secret"}
            print(f"Données chargées : {donnees}")
            # Simulation d'une erreur
            # raise ValueError("Erreur lors du traitement")
        except ValueError as e:
            print(f"Erreur : {e}")
        finally:
            if donnees:
                print(f"Nettoyage des données sensibles")
                donnees = None

    processus_complet()
    print()


# ═════════════════════════════════════════════════════════════════════════════
# ÉTAPE 6 : try/except/else/finally complet
# ═════════════════════════════════════════════════════════════════════════════

def etape6_try_except_else_finally():
    """Utiliser tous les blocs ensemble."""

    print("═" * 79)
    print("ÉTAPE 6 : try/except/else/finally (complet)")
    print("═" * 79)
    print()

    print("Exemple : Pipeline de traitement de données")
    print("-" * 40)

    def pipeline_donnees(donnees):
        resultat = None
        try:
            # Étape 1 : Parser les données
            print(f"Parsing de : {donnees}")
            numero = int(donnees)
        except ValueError as e:
            # Erreur lors du parsing
            print(f"Erreur de parsing : {e}")
        else:
            # Si le parsing réussit
            print(f"Parsing réussi : {numero}")
            try:
                # Étape 2 : Traiter les données
                resultat = 100 / numero
                print(f"Traitement réussi : {resultat}")
            except ZeroDivisionError:
                print("Erreur : Division par zéro")
        finally:
            # Toujours exécuté
            print("Fin du pipeline\n")

        return resultat

    # Tester différents cas
    pipeline_donnees("42")
    pipeline_donnees("0")
    pipeline_donnees("abc")
    print()


# ═════════════════════════════════════════════════════════════════════════════
# ÉTAPE 7 : Lever des exceptions avec 'raise'
# ═════════════════════════════════════════════════════════════════════════════

def etape7_lever_exceptions():
    """Lever volontairement des exceptions avec 'raise'."""

    print("═" * 79)
    print("ÉTAPE 7 : Lever des exceptions (raise)")
    print("═" * 79)
    print()

    # EXEMPLE 1 : Valider une entrée utilisateur
    print("Exemple 1 : Validation avec raise")
    print("-" * 40)

    def diviser(a, b):
        if b == 0:
            # Lever une exception si la division est impossible
            raise ValueError("Impossible de diviser par zéro")
        return a / b

    try:
        resultat = diviser(10, 2)
        print(f"10 / 2 = {resultat}")
    except ValueError as e:
        print(f"Erreur : {e}")

    try:
        resultat = diviser(10, 0)
        print(f"10 / 0 = {resultat}")
    except ValueError as e:
        print(f"Erreur : {e}")

    print()

    # EXEMPLE 2 : Validation de mot de passe
    print("Exemple 2 : Validation d'un mot de passe")
    print("-" * 40)

    def valider_mot_passe(mot_passe):
        if not mot_passe:
            raise ValueError("Le mot de passe ne peut pas être vide")
        if len(mot_passe) < 8:
            raise ValueError("Le mot de passe doit avoir au moins 8 caractères")
        if not any(c.isupper() for c in mot_passe):
            raise ValueError("Le mot de passe doit contenir une majuscule")
        if not any(c.isdigit() for c in mot_passe):
            raise ValueError("Le mot de passe doit contenir un chiffre")
        return True

    mots_passes = ["", "court", "SansMaj123", "SansChiffre", "ValidPassword123"]

    for mp in mots_passes:
        try:
            valider_mot_passe(mp)
            print(f"✓ Mot de passe valide : {mp}")
        except ValueError as e:
            print(f"✗ Mot de passe invalide ({mp}) : {e}")

    print()

    # EXEMPLE 3 : Vérifier les paramètres d'une fonction
    print("Exemple 3 : Vérifier les paramètres")
    print("-" * 40)

    def scanner_port(hote, port):
        if not isinstance(hote, str) or not hote:
            raise TypeError("hote doit être une chaîne non vide")
        if not isinstance(port, int) or not (1 <= port <= 65535):
            raise ValueError("port doit être un entier entre 1 et 65535")
        return f"Scan de {hote}:{port}"

    # Cas valides
    try:
        print(scanner_port("192.168.1.1", 22))
        print(scanner_port("example.com", 443))
    except (TypeError, ValueError) as e:
        print(f"Erreur : {e}")

    # Cas invalides
    try:
        print(scanner_port("", 22))
    except (TypeError, ValueError) as e:
        print(f"Erreur : {e}")

    try:
        print(scanner_port("localhost", 99999))
    except (TypeError, ValueError) as e:
        print(f"Erreur : {e}")

    print()


# ═════════════════════════════════════════════════════════════════════════════
# ÉTAPE 8 : Exceptions personnalisées
# ═════════════════════════════════════════════════════════════════════════════

def etape8_exceptions_personnalisees():
    """Créer ses propres exceptions."""

    print("═" * 79)
    print("ÉTAPE 8 : Exceptions personnalisées")
    print("═" * 79)
    print()

    # EXEMPLE 1 : Exception simple
    print("Exemple 1 : Exception personnalisée simple")
    print("-" * 40)

    class UtilisateurInvalide(Exception):
        """Exception levée quand un utilisateur est invalide."""
        pass

    def creer_utilisateur(nom, email):
        if not nom or len(nom) < 3:
            raise UtilisateurInvalide(
                f"Le nom '{nom}' doit avoir au moins 3 caractères"
            )
        if "@" not in email:
            raise UtilisateurInvalide(f"L'email '{email}' n'est pas valide")
        return {"nom": nom, "email": email}

    # Cas valides
    try:
        utilisateur = creer_utilisateur("Alice", "alice@example.com")
        print(f"Utilisateur créé : {utilisateur}")
    except UtilisateurInvalide as e:
        print(f"Erreur : {e}")

    # Cas invalides
    try:
        utilisateur = creer_utilisateur("Jo", "joe@example.com")
        print(f"Utilisateur créé : {utilisateur}")
    except UtilisateurInvalide as e:
        print(f"Erreur : {e}")

    try:
        utilisateur = creer_utilisateur("Bob", "bob_sans_arobase")
        print(f"Utilisateur créé : {utilisateur}")
    except UtilisateurInvalide as e:
        print(f"Erreur : {e}")

    print()

    # EXEMPLE 2 : Exception avec paramètres
    print("Exemple 2 : Exception personnalisée avec paramètres")
    print("-" * 40)

    class ErreurAuthentification(Exception):
        """Exception d'authentification avec détails."""
        def __init__(self, utilisateur, raison):
            self.utilisateur = utilisateur
            self.raison = raison
            super().__init__(
                f"Authentification échouée pour {utilisateur} : {raison}"
            )

    def authentifier(utilisateur, mot_passe):
        utilisateurs = {
            "alice": "password123",
            "bob": "secret456",
            "charlie": "secure789"
        }

        if utilisateur not in utilisateurs:
            raise ErreurAuthentification(
                utilisateur, "utilisateur inexistant"
            )

        if mot_passe != utilisateurs[utilisateur]:
            raise ErreurAuthentification(
                utilisateur, "mot de passe incorrect"
            )

        return f"Authentification réussie pour {utilisateur}"

    # Tests
    tentatives = [
        ("alice", "password123"),
        ("alice", "mauvais"),
        ("inconnu", "password123")
    ]

    for user, pwd in tentatives:
        try:
            resultat = authentifier(user, pwd)
            print(f"✓ {resultat}")
        except ErreurAuthentification as e:
            print(f"✗ {e}")

    print()

    # EXEMPLE 3 : Hiérarchie d'exceptions
    print("Exemple 3 : Hiérarchie d'exceptions personnalisées")
    print("-" * 40)

    class ErreurReseau(Exception):
        """Classe de base pour les erreurs réseau."""
        pass

    class ErreurConnexion(ErreurReseau):
        """Impossible de se connecter."""
        pass

    class ErreurTimeout(ErreurReseau):
        """Timeout de la connexion."""
        pass

    class ErreurSSL(ErreurReseau):
        """Erreur de certificat SSL."""
        pass

    def connecter_securise(adresse, timeout=5):
        import random
        scenario = random.choice(["ok", "timeout", "ssl", "autre"])

        if scenario == "timeout":
            raise ErreurTimeout(f"Timeout après {timeout}s sur {adresse}")
        elif scenario == "ssl":
            raise ErreurSSL(f"Certificat SSL invalide pour {adresse}")
        elif scenario == "autre":
            raise ErreurConnexion(f"Impossible de se connecter à {adresse}")

        return f"Connecté à {adresse}"

    # Tests
    for i in range(5):
        try:
            resultat = connecter_securise("api.example.com")
            print(f"✓ {resultat}")
        except ErreurTimeout as e:
            print(f"✗ Timeout : {e}")
        except ErreurSSL as e:
            print(f"✗ SSL : {e}")
        except ErreurConnexion as e:
            print(f"✗ Connexion : {e}")
        except ErreurReseau as e:
            print(f"✗ Erreur réseau générique : {e}")

    print()


# ═════════════════════════════════════════════════════════════════════════════
# ÉTAPE 9 : Red Teaming - Gestion d'erreurs avancée
# ═════════════════════════════════════════════════════════════════════════════

def etape9_red_teaming():
    """Gestion robuste des erreurs en contexte de red teaming."""

    print("═" * 79)
    print("ÉTAPE 9 : Red Teaming - Gestion d'erreurs avancée")
    print("═" * 79)
    print()

    # EXEMPLE 1 : Scanner de ports robuste
    print("Exemple 1 : Scanner de ports avec gestion d'erreurs")
    print("-" * 40)

    class ErreurScan(Exception):
        """Erreur générique de scan."""
        pass

    class CibleIndisponible(ErreurScan):
        """La cible n'est pas accessible."""
        pass

    class PortFerme(ErreurScan):
        """Le port est fermé."""
        pass

    def scanner_port_simple(hote, port, timeout=2):
        """Simule un scan de port avec gestion d'erreurs."""
        import random

        try:
            # Simuler la tentative de connexion
            if random.random() < 0.3:
                raise ConnectionRefusedError("Connexion refusée")
            elif random.random() < 0.2:
                raise TimeoutError(f"Timeout après {timeout}s")
            elif random.random() < 0.2:
                raise OSError("Impossible de résoudre le nom d'hôte")

            return {"hote": hote, "port": port, "statut": "ouvert"}

        except ConnectionRefusedError:
            return {"hote": hote, "port": port, "statut": "fermé"}
        except TimeoutError:
            return {"hote": hote, "port": port, "statut": "timeout"}
        except OSError as e:
            return {"hote": hote, "port": port, "statut": "erreur", "détail": str(e)}

    def scanner_multiple_ports(hote, ports):
        """Scanner multiple ports avec continuation sur erreur."""
        resultats = []

        for port in ports:
            try:
                resultat = scanner_port_simple(hote, port)
                resultats.append(resultat)
                print(f"[{hote}:{port}] {resultat['statut']}")

            except Exception as e:
                # Capturer toute erreur inattendue
                print(f"[{hote}:{port}] ERREUR INATTENDUE : {e}")
                resultats.append({
                    "hote": hote,
                    "port": port,
                    "statut": "erreur",
                    "détail": str(e)
                })

        return resultats

    # Tester le scanner
    resultats = scanner_multiple_ports("192.168.1.1", [22, 80, 443, 8080, 3306])
    print(f"\nRésultats : {len(resultats)} ports scannés")

    ports_ouverts = [r for r in resultats if r.get("statut") == "ouvert"]
    print(f"Ports ouverts : {[r['port'] for r in ports_ouverts]}")
    print()

    # EXEMPLE 2 : Parser de données avec validation
    print("Exemple 2 : Parser JSON robuste avec validation")
    print("-" * 40)

    class ErreurParsing(Exception):
        """Erreur lors du parsing."""
        pass

    def parser_donnees_json(texte):
        """Parser JSON avec gestion d'erreurs."""
        import json

        try:
            donnees = json.loads(texte)
            return donnees
        except json.JSONDecodeError as e:
            raise ErreurParsing(f"JSON invalide : {e}")
        except TypeError as e:
            raise ErreurParsing(f"Type invalide : {e}")

    def extraire_credentials(json_texte):
        """Extraire les credentials d'une réponse JSON."""
        try:
            donnees = parser_donnees_json(json_texte)

            # Valider la structure
            if "username" not in donnees:
                raise KeyError("Clé 'username' manquante")
            if "password" not in donnees:
                raise KeyError("Clé 'password' manquante")

            return {
                "username": donnees["username"],
                "password": donnees["password"]
            }

        except ErreurParsing as e:
            print(f"Erreur de parsing : {e}")
            return None
        except KeyError as e:
            print(f"Clé manquante : {e}")
            return None
        except Exception as e:
            print(f"Erreur inattendue : {e}")
            return None

    # Tester le parser
    json_valide = '{"username": "admin", "password": "secret123"}'
    json_invalide = '{"username": "admin" "password": "secret123"}'  # Syntaxe incorrecte
    json_incomplet = '{"username": "admin"}'

    print("Test 1 : JSON valide")
    resultat = extraire_credentials(json_valide)
    print(f"Résultat : {resultat}\n")

    print("Test 2 : JSON invalide (syntaxe)")
    resultat = extraire_credentials(json_invalide)
    print(f"Résultat : {resultat}\n")

    print("Test 3 : JSON incomplet")
    resultat = extraire_credentials(json_incomplet)
    print(f"Résultat : {resultat}\n")

    # EXEMPLE 3 : Retry avec backoff exponentiel
    print("Exemple 3 : Retry avec backoff exponentiel")
    print("-" * 40)

    def appel_api_avec_retry(url, max_retries=3):
        """Appeler une API avec retry et backoff exponentiel."""
        import time
        import random

        for tentative in range(max_retries):
            try:
                # Simuler un appel API qui peut échouer
                if random.random() < 0.5:
                    raise ConnectionError("Erreur de connexion")

                return f"Réponse de {url}"

            except ConnectionError as e:
                if tentative < max_retries - 1:
                    # Calculer le délai d'attente : 2^tentative secondes
                    delai = 2 ** tentative
                    print(f"Tentative {tentative + 1} échouée. Retry dans {delai}s...")
                    # time.sleep(delai)  # Ne pas vraiment attendre
                else:
                    print(f"Échec après {max_retries} tentatives")
                    raise

        return None

    try:
        resultat = appel_api_avec_retry("https://api.example.com", max_retries=3)
        print(f"Succès : {resultat}")
    except ConnectionError as e:
        print(f"Erreur finale : {e}")

    print()


# ═════════════════════════════════════════════════════════════════════════════
# ÉTAPE 10 : Réélever et chaîner des exceptions
# ═════════════════════════════════════════════════════════════════════════════

def etape10_relever_chainer():
    """Réélever et chaîner des exceptions."""

    print("═" * 79)
    print("ÉTAPE 10 : Réélever et chaîner des exceptions")
    print("═" * 79)
    print()

    # EXEMPLE 1 : Réélever une exception
    print("Exemple 1 : Réélever une exception")
    print("-" * 40)

    def fonction_bas_niveau():
        raise ValueError("Erreur au niveau bas")

    def fonction_niveau_intermediaire():
        try:
            fonction_bas_niveau()
        except ValueError as e:
            print(f"Erreur capturée au niveau intermédiaire : {e}")
            raise  # Relève la même exception

    try:
        fonction_niveau_intermediaire()
    except ValueError as e:
        print(f"Erreur finale : {e}")

    print()

    # EXEMPLE 2 : Transformer une exception
    print("Exemple 2 : Transformer une exception")
    print("-" * 40)

    def lire_donnees_sensibles(fichier):
        try:
            with open(fichier, "r") as f:
                return f.read()
        except FileNotFoundError as e:
            # Transformer en exception personnalisée
            raise ValueError(f"Fichier de configuration manquant : {fichier}") from e

    try:
        donnees = lire_donnees_sensibles("/etc/config_secret.conf")
    except ValueError as e:
        print(f"Erreur : {e}")
        if e.__cause__:
            print(f"Cause originale : {e.__cause__}")

    print()

    # EXEMPLE 3 : Chaîner des exceptions avec contexte
    print("Exemple 3 : Chaîner des exceptions")
    print("-" * 40)

    def connecter_et_authentifier(serveur, utilisateur, mot_passe):
        try:
            print(f"Connexion à {serveur}...")
            # Simuler une erreur de connexion
            raise ConnectionError(f"Impossible de se connecter à {serveur}")
        except ConnectionError as e:
            raise RuntimeError(
                f"Authentification échouée : {utilisateur}"
            ) from e

    try:
        connecter_et_authentifier("db.example.com", "admin", "secret")
    except RuntimeError as e:
        print(f"Erreur : {e}")
        print(f"Cause : {e.__cause__}")

    print()


# ═════════════════════════════════════════════════════════════════════════════
# FONCTION PRINCIPALE
# ═════════════════════════════════════════════════════════════════════════════

def main():
    """Fonction principale."""

    print("\n")
    print("╔" + "=" * 77 + "╗")
    print("║" + " " * 20 + "EXERCICE 12 : GESTION D'EXCEPTIONS" + " " * 24 + "║")
    print("╚" + "=" * 77 + "╝")
    print()

    # Exécuter chaque étape
    etape1_try_except_basique()
    etape2_capture_message_erreur()
    etape3_exceptions_multiples()
    etape4_try_except_else()
    etape5_try_except_finally()
    etape6_try_except_else_finally()
    etape7_lever_exceptions()
    etape8_exceptions_personnalisees()
    etape9_red_teaming()
    etape10_relever_chainer()

    print("=" * 79)
    print("Exercice complété ! Consultez exercice.txt pour les défis.")
    print("=" * 79)


if __name__ == "__main__":
    main()
