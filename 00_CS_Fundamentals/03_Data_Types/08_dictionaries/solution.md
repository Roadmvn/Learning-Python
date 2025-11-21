# Exercice 08: Dictionnaires - Solutions

## Solution Défi 1: Créateur de profil utilisateur

"""
Créateur de profil utilisateur
"""

# Créer le profil initial
profil = {
    "nom": "Alice",
```python
    "email": "alice@example.com",
    "age": 30,
    "username": "alice_dev"
```
}

```python
print("Profil initial :")
print(profil)
print()

```
# Ajouter une clé
profil["actif"] = True

# Modifier une clé
profil["age"] = 31

```python
print("Profil mis à jour :")
print(profil)
print()

```
# Affichage détaillé
```python
print("Informations du profil :")
for cle, valeur in profil.items():
    print(f"  {cle}: {valeur}")

## Solution Défi 2: Gestionnaire d'inventaire simple

```
"""
Gestionnaire d'inventaire simple
"""

# Initialiser l'inventaire
inventaire = {
    "laptop": 5,
    "souris": 20,
    "clavier": 15,
    "moniteur": 8
}

```python
print("Inventaire initial :")
print(inventaire)
print()

```
# Nombre total d'articles (somme des quantités)
total = sum(inventaire.values())
```python
print(f"Nombre total d'articles : {total}")
print()

```
# Utiliser get() pour afficher les quantités
articles_a_chercher = ["laptop", "souris", "cable"]

```python
for article in articles_a_chercher:
    quantite = inventaire.get(article, "Article introuvable")
    print(f"{article}: {quantite}")
print()

```
# Ajouter un nouvel article
inventaire["cable_usb"] = 50
```python
print(f"Après ajout de cable_usb : {inventaire}")
print()

```
# Supprimer un article
del inventaire["laptop"]
# ou : inventaire.pop("laptop")
```python
print(f"Après suppression de laptop : {inventaire}")
print()

```
# Afficher l'inventaire final
```python
print("Inventaire final :")
for article, quantite in inventaire.items():
    print(f"  {article}: {quantite} unités")

## Solution Défi 3: Analyseur de résultats d'examen

```
"""
Analyseur de résultats d'examen
"""

scores = {
    "alice": 95,
    "bob": 78,
    "charlie": 88,
    "diana": 92,
    "eve": 85
}

# Afficher tous les étudiants et leurs scores
```python
print("Résultats de l'examen :")
for etudiant, score in scores.items():
    print(f"  {etudiant}: {score}")
print()

```
# Score max et min
score_max = max(scores.values())
score_min = min(scores.values())
etudiant_max = max(scores, key=scores.get)
etudiant_min = min(scores, key=scores.get)

```python
print(f"Score maximum : {score_max} ({etudiant_max})")
print(f"Score minimum : {score_min} ({etudiant_min})")
print()

```
# Moyenne
moyenne = sum(scores.values()) / len(scores)
```python
print(f"Moyenne : {moyenne:.2f}")
print()

```
# Compter les étudiants avec score >= 85
reussis = sum(1 for score in scores.values() if score >= 85)
```python
print(f"Étudiants avec score >= 85 : {reussis}")
print()

```
# Afficher ceux qui ont échoué (< 50)
echoues = [etudiant for etudiant, score in scores.items() if score < 50]
```python
if echoues:
    print(f"Étudiants qui ont échoué : {', '.join(echoues)}")
else:
    print("Aucun étudiant n'a échoué (tous >= 50)")
print()

```
# Affichage des résultats par catégorie
```python
print("Résultats détaillés :")
print(f"Excellents (>= 90) :")
for etudiant, score in scores.items():
    if score >= 90:
        print(f"  {etudiant}: {score}")

print(f"Bons (80-89) :")
for etudiant, score in scores.items():
    if 80 <= score < 90:
        print(f"  {etudiant}: {score}")

print(f"Acceptables (70-79) :")
for etudiant, score in scores.items():
    if 70 <= score < 80:
        print(f"  {etudiant}: {score}")

print(f"À travailler (< 70) :")
for etudiant, score in scores.items():
    if score < 70:
        print(f"  {etudiant}: {score}")

## Solution Défi 4: Dict comprehension - Table de multiplication

```
"""
Dict comprehension - Générateur de table de multiplication
"""

# Créer la table de multiplication avec dict comprehension
table_multi = {
```python
    f"{i}x{j}": i * j
    for i in range(1, 11)
    for j in range(1, 11)
```
}

```python
print("Table de multiplication (1-10) :")
print(f"Nombre total d'entrées : {len(table_multi)}")
print()

```
# Afficher quelques entrées
```python
print("Aperçu des premiers résultats :")
```
compte = 0
```python
for operation, resultat in table_multi.items():
    if compte < 20:
        print(f"  {operation} = {resultat}")
        compte += 1
    else:
        break
print("...")
print()

```
# Rechercher toutes les multiplications qui donnent 12
```python
print("Opérations qui donnent 12 :")
```
mult_12 = {op: result for op, result in table_multi.items() if result == 12}
```python
for operation in mult_12:
    print(f"  {operation} = 12")
print()

```
# Créer un dict avec uniquement les multiplications >= 50
mult_sup_50 = {op: result for op, result in table_multi.items() if result >= 50}
```python
print(f"Nombre de résultats >= 50 : {len(mult_sup_50)}")
print("Quelques exemples :")
```
compte = 0
```python
for operation, resultat in mult_sup_50.items():
    if compte < 10:
        print(f"  {operation} = {resultat}")
        compte += 1
print()

## Solution Défi 5: Scanner de ports (cybersécurité)

```
"""
Scanner de ports
"""

# Dictionnaire des services
services = {
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
```python
    5432: "PostgreSQL"
```
}

# Résultats du scan
resultats_scan = {
    22: "open",
    80: "open",
    443: "closed",
```python
    3306: "filtered",
    5432: "closed"
```
}

```python
print("═══ Résultats du scan de ports ═══\n")

```
# Afficher le statut avec le service
```python
print("Rapport détaillé :")
for port, statut in resultats_scan.items():
    service = services.get(port, "Inconnu")
    print(f"  Port {port} ({service}) : {statut}")
print()

```
# Ports ouverts uniquement
```python
print("Ports ouverts :")
```
ports_ouverts = [
```python
    (port, services.get(port))
    for port, statut in resultats_scan.items()
    if statut == "open"
```
]
```python
for port, service in ports_ouverts:
    print(f"  Port {port} ({service})")
print()

```
# Statistiques
ouverts = sum(1 for s in resultats_scan.values() if s == "open")
fermes = sum(1 for s in resultats_scan.values() if s == "closed")
filtres = sum(1 for s in resultats_scan.values() if s == "filtered")

```python
print("Statistiques :")
print(f"  Ports ouverts : {ouverts}")
print(f"  Ports fermés : {fermes}")
print(f"  Ports filtrés : {filtres}")
print(f"  Total scanné : {len(resultats_scan)}")

## Solution Défi 6: Base de données d'utilisateurs imbriquée

```
"""
Base de données d'utilisateurs imbriquée
"""

utilisateurs = {
    "user1": {
```python
        "nom": "Alice",
        "role": "admin",
        "email": "alice@example.com"
    },
    "user2": {
        "nom": "Bob",
        "role": "user",
        "email": "bob@example.com"
    },
    "user3": {
        "nom": "Charlie",
        "role": "user",
        "email": "charlie@example.com"
    }
```
}

```python
print("═══ Base de données utilisateurs ═══\n")

```
# Afficher les informations de chaque utilisateur
```python
print("Tous les utilisateurs :")
for user_id, infos in utilisateurs.items():
    print(f"\n{user_id}:")
    for cle, valeur in infos.items():
        print(f"  {cle}: {valeur}")
print()

```
# Afficher uniquement les administrateurs
```python
print("\nAdministrateurs :")
for user_id, infos in utilisateurs.items():
    if infos["role"] == "admin":
        print(f"  {user_id}: {infos['nom']} ({infos['email']})")
print()

```
# Ajouter un nouvel utilisateur
utilisateurs["user4"] = {
    "nom": "Diana",
    "role": "user",
```python
    "email": "diana@example.com"
```
}
```python
print("Ajout de user4 effectué")
print()

```
# Modifier le rôle de user2
utilisateurs["user2"]["role"] = "admin"
```python
print("user2 promu en administrateur")
print()

```
# Afficher la base mise à jour
```python
print("Base mise à jour :")
for user_id, infos in utilisateurs.items():
    role_info = f"({infos['role']})"
    print(f"  {user_id}: {infos['nom']} {role_info}")

## Solution Défi 7: Configuration d'application avancée

```
"""
Configuration d'application avancée
"""

# Configuration par défaut
config_defaut = {
    "app": {
```python
        "nom": "MyApp",
        "version": "1.0.0",
        "debug": False
    },
    "serveur": {
        "host": "localhost",
        "port": 5000,
        "ssl": False
    },
    "base_donnees": {
        "type": "sqlite",
        "nom": "app.db"
    }
```
}

# Configuration utilisateur
config_utilisateur = {
```python
    "app": {"debug": True},
    "serveur": {"port": 8080}
```
}

```python
print("═══ Configuration d'application ═══\n")

print("Configuration par défaut :")
print(config_defaut)
print()

print("Configuration utilisateur :")
print(config_utilisateur)
print()

```
# Fusionner les configurations (IMPORTANT : fusion simple, pas profonde)
# Pour une fusion profonde, il faudrait le faire manuellement ou utiliser deepcopy

# Fusion simple (écrase les clés existantes)
config_finale = config_defaut.copy()

# Fusion manuelle pour les dictionnaires imbriqués
```python
for section, valeurs in config_utilisateur.items():
    if section in config_finale:
        config_finale[section].update(valeurs)
    else:
        config_finale[section] = valeurs

print("Configuration finale (après fusion) :")
print(config_finale)
print()

```
# Afficher uniquement les paramètres du serveur
```python
print("Paramètres du serveur :")
for param, valeur in config_finale["serveur"].items():
    print(f"  {param}: {valeur}")
print()

```
# Modifier le port du serveur
config_finale["serveur"]["port"] = 9000
```python
print("Port du serveur modifié à 9000")
print()

```
# Configuration finale
```python
print("Configuration finale :")
for section, valeurs in config_finale.items():
    print(f"\n[{section}]")
    for cle, valeur in valeurs.items():
        print(f"  {cle}: {valeur}")

## Solution Défi 8: Rapport de vulnérabilités (red teaming)

```
"""
Rapport de vulnérabilités
"""

vulnerabilites = {
```python
    "CVE-2024-1234": {
        "description": "RCE in WebApp",
        "severite": "critique",
        "cvss_score": 9.8,
        "patch": True
    },
    "CVE-2024-5678": {
        "description": "SQL Injection",
        "severite": "haute",
        "cvss_score": 8.9,
        "patch": False
    },
    "CVE-2024-9999": {
        "description": "XSS",
        "severite": "moyenne",
        "cvss_score": 6.1,
        "patch": True
    }
```
}

```python
print("═══════════════════════════════════════════════════════════")
print("RAPPORT DE VULNÉRABILITÉS")
print("═══════════════════════════════════════════════════════════\n")

```
# Afficher toutes les vulnérabilités
```python
print("Toutes les vulnérabilités détectées :")
print()
for cve, infos in vulnerabilites.items():
    print(f"{cve}: {infos['description']}")
    print(f"  Sévérité : {infos['severite']}")
    print(f"  CVSS Score : {infos['cvss_score']}")
    print(f"  Patch disponible : {'Oui' if infos['patch'] else 'Non'}")
    print()

```
# Générer des statistiques
```python
print("═" * 60)
print("STATISTIQUES")
print("═" * 60\n")

```
# Nombre par sévérité
severites = {}
```python
for info in vulnerabilites.values():
    sev = info["severite"]
    severites[sev] = severites.get(sev, 0) + 1

print("Vulnérabilités par sévérité :")
for sev, count in sorted(severites.items()):
    print(f"  {sev}: {count}")
print()

```
# Score CVSS moyen
scores = [info["cvss_score"] for info in vulnerabilites.values()]
score_moyen = sum(scores) / len(scores)
```python
print(f"Score CVSS moyen : {score_moyen:.2f}")
print()

```
# Avec/sans patch
avec_patch = sum(1 for info in vulnerabilites.values() if info["patch"])
sans_patch = sum(1 for info in vulnerabilites.values() if not info["patch"])
```python
print(f"Vulnérabilités avec patch : {avec_patch}")
print(f"Vulnérabilités sans patch : {sans_patch}")
print()

```
# Afficher les vulnérabilités critiques
```python
print("═" * 60)
print("VULNÉRABILITÉS CRITIQUES")
print("═" * 60\n")

```
critiques = {cve: info for cve, info in vulnerabilites.items()
```python
             if info["severite"] == "critique"}

if critiques:
    for cve, infos in critiques.items():
        print(f"[CRITIQUE] {cve}: {infos['description']}")
        print(f"  CVSS Score : {infos['cvss_score']}")
else:
    print("Aucune vulnérabilité critique détectée")
print()

```
# Vulnérabilités sans patch (à corriger en priorité)
```python
print("═" * 60)
print("VULNÉRABILITÉS SANS PATCH (À CORRIGER EN PRIORITÉ)")
print("═" * 60\n")

```
sans_patch_dict = {cve: info for cve, info in vulnerabilites.items()
```python
                   if not info["patch"]}

if sans_patch_dict:
    for cve, infos in sans_patch_dict.items():
        print(f"[{infos['severite'].upper()}] {cve}: {infos['description']}")
        print(f"  CVSS Score : {infos['cvss_score']}")
else:
    print("Tous les vulnérabilités ont des patchs disponibles")
print()

```
# Trier par score CVSS (décroissant)
```python
print("═" * 60)
print("TOP 3 VULNÉRABILITÉS (par score CVSS)")
print("═" * 60\n")

```
vulns_triees = sorted(vulnerabilites.items(),
```python
                      key=lambda x: x[1]["cvss_score"],
                      reverse=True)

for i, (cve, infos) in enumerate(vulns_triees[:3], 1):
    print(f"{i}. {cve} - Score: {infos['cvss_score']}")
    print(f"   {infos['description']}")
    print(f"   Sévérité : {infos['severite']}")
    print()

```