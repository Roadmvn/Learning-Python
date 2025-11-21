# Exercice 11: Gestion de Fichiers - Défis

## Défi 1: Créer et lire un fichier simple

Créez un programme qui :
1. Crée un fichier nommé "notes.txt"
2. Écrit 5 lignes de contenu dans le fichier
3. Lit le fichier et affiche chaque ligne avec son numéro
4. Affiche le nombre total de lignes
5. Utilise obligatoirement 'with' pour ouvrir le fichier

Exemple de sortie :
  Fichier créé : notes.txt
  Contenu du fichier :
    1. Première note
    2. Deuxième note
```python
    3. Troisième note
    4. Quatrième note
    5. Cinquième note
```
  Total de lignes : 5

## Défi 2: Modifier un fichier existant

Créez un programme qui :
1. Crée un fichier "log.txt" avec 3 lignes initiales
2. Ajoute 2 nouvelles lignes au fichier (mode append)
3. Lit le fichier et affiche toutes les lignes
4. Affiche le nombre de lignes avant et après modification

Étapes :
1. Écrire les 3 lignes initiales avec le mode 'w'
2. Ajouter 2 lignes avec le mode 'a'
3. Lire le fichier et afficher les résultats

Exemple de sortie :
  Fichier initial : 3 lignes
  Fichier après ajout : 5 lignes
  Contenu final :
```python
    [1] Ligne initiale 1
    [2] Ligne initiale 2
    [3] Ligne initiale 3
    [4] Ligne ajoutée 1
    [5] Ligne ajoutée 2

## Défi 3: Lire un fichier ligne par ligne et compter les mots

```
Créez un programme qui :
1. Crée un fichier "texte.txt" avec 4 phrases différentes
2. Lit le fichier ligne par ligne
3. Pour chaque ligne, compte le nombre de mots
4. Affiche :
   - Le numéro de la ligne
   - La ligne
   - Le nombre de mots dans cette ligne
5. Affiche le nombre total de mots dans le fichier

Exemple de sortie :
  Analyse du fichier texte.txt
  Ligne 1 (4 mots) : Ceci est une phrase
  Ligne 2 (5 mots) : Cette ligne contient plus de mots
  Ligne 3 (3 mots) : Et celle-ci aussi
  Ligne 4 (4 mots) : Pour un total complet
  Total : 16 mots

## Défi 4: Copier un fichier

Créez un programme qui :
1. Crée un fichier source "source.txt" avec du contenu
2. Copie le contenu dans un fichier "destination.txt"
3. Vérifie que les deux fichiers existent
4. Affiche le contenu des deux fichiers
5. Vérifies que le contenu est identique

Approche :
1. Ouvrir le fichier source en lecture
2. Ouvrir le fichier destination en écriture
3. Copier le contenu
4. Fermer les deux fichiers

Exemple de sortie :
  Fichier source créé : source.txt
  Fichier source existe : True
  Fichier destination créé par copie
  Fichier destination existe : True
  Contenu identique : True
  Nombre de caractères : 45

## Défi 5: Travailler avec JSON - Configuration d'attaque

Créez un programme qui :
1. Crée un dictionnaire de configuration d'attaque avec :
   - Nom de la campagne
   - Cibles (liste d'adresses IP)
   - Techniques utilisées (liste)
   - Résultats (ports ouverts, vulnérabilités)
2. Sauvegarde cette configuration en JSON dans un fichier
3. Charge le JSON et affiche les informations
4. Ajoute une nouvelle vulnérabilité à la configuration
5. Sauvegarde à nouveau le fichier mis à jour

Structures JSON :
{
  "campagne": "Pentest XYZ",
  "cibles": ["192.168.1.1", "192.168.1.2"],
  "techniques": ["scan", "exploitation"],
  "resultats": {
```python
    "ports_ouverts": [80, 443],
    "vulnerabilites": []
```
  }
}

Exemple de sortie :
  Configuration créée et sauvegardée
  Campagne : Pentest XYZ
  Cibles : 2
  Vulnérabilités : 0
  Ajout d'une vulnérabilité...
  Vulnérabilités : 1
  Fichier mis à jour

## Défi 6: Travailler avec les chemins (os.path et pathlib)

Créez un programme qui :
1. Affiche le répertoire courant
2. Crée un chemin vers un fichier dans un dossier "data"
3. Utilise os.path.join() pour construire le chemin
4. Utilise pathlib.Path pour construire le même chemin
5. Vérifie que les deux méthodes donnent le même résultat
6. Affiche les composants du chemin (répertoire, nom, extension)

Utiliser :
- os.getcwd()
- os.path.join()
- os.path.dirname(), os.path.basename()
- pathlib.Path
- Path.parent, Path.name, Path.suffix

Exemple de sortie :
  Répertoire courant : /Users/tudygbaguidi/Desktop/Learning-Python
  Chemin os.path : /Users/tudygbaguidi/Desktop/Learning-Python/data/fichier.txt
  Chemin pathlib : /Users/tudygbaguidi/Desktop/Learning-Python/data/fichier.txt
  Chemins identiques : True
  Nom du fichier : fichier.txt
  Extension : .txt
  Répertoire parent : /Users/tudygbaguidi/Desktop/Learning-Python/data

## Défi 7: Créer un gestionnaire de logs avec timestamps

Créez un programme qui :
1. Crée un fichier "attack_log.txt"
2. Écrit au moins 8 entrées de log avec timestamps
3. Chaque log inclut :
   - Timestamp (utiliser datetime)
   - Niveau ([INFO], [WARN], [ERROR], [SUCCESS])
   - Message
4. Lit le fichier et affiche les logs
5. Filtre et affiche uniquement les logs [SUCCESS]
6. Compte le nombre de logs par type

Format du log :
  [YYYY-MM-DD HH:MM:SS] [LEVEL] Message du log

Exemple de sortie :
  Log créé avec 8 entrées
  Logs totaux : 8

  Logs [SUCCESS] :
```python
    [2024-11-07 14:30:45] [SUCCESS] Accès obtenu
    [2024-11-07 14:31:12] [SUCCESS] Exploit réussi

```
  Statistiques :
    [INFO] : 3
    [WARN] : 2
    [ERROR] : 1
```python
    [SUCCESS] : 2

## Défi 8: Red Teaming - Scanner complet avec résultats en JSON

```
Créez un programme complet de red teaming qui :

1. ÉNUMÉRATION SYSTÈME
   - Afficher le répertoire courant
   - Afficher l'utilisateur actuel (os.getenv('USER'))

2. CRÉATION DE LOGS D'ATTAQUE
   - Créer un fichier "scan_log.txt"
   - Écrire au moins 10 entrées de log avec timestamps
   - Inclure : énumération, scan, vulnérabilités trouvées

3. RÉSULTATS DE SCAN EN JSON
   - Créer une structure JSON avec :
     * scan_id
     * timestamp
     * cible
```python
     * hosts_decouverts (liste avec IP, ports ouverts)
     * vulnerabilites_trouvees
```
   - Sauvegarder dans "scan_results.json"

4. RAPPORT TEXTE
   - Créer un fichier "rapport.txt"
   - Lire le JSON et générer un rapport formaté
   - Inclure résumé et statistiques

5. ANALYSE ET STATISTIQUES
   - Compter les vulnérabilités par sévérité
   - Compter les ports ouverts
   - Calculer le nombre de hosts découverts

Structure JSON attendue :
{
  "scan_id": "SCAN-20241107-001",
  "timestamp": "2024-11-07T14:30:45",
  "cible": "192.168.1.1",
  "hosts_decouverts": [
```python
    {"ip": "192.168.1.1", "ports_ouverts": [22, 80, 443]},
    {"ip": "192.168.1.100", "ports_ouverts": [445, 3389]}
```
  ],
  "vulnerabilites": [
```python
    {"cve": "CVE-2024-0001", "severite": "CRITICAL"},
    {"cve": "CVE-2024-0002", "severite": "HIGH"}
```
  ]
}

Exemple de sortie :
  ═══════════════════════════════════════════════════════════════════════════
  RED TEAMING SCANNER - RÉSULTATS COMPLETS
  ═══════════════════════════════════════════════════════════════════════════

  [*] Énumération système
  Répertoire : /Users/tudygbaguidi/Desktop/Learning-Python
  Utilisateur : tudygbaguidi

  [*] Logs d'attaque
  Fichier créé : scan_log.txt
  Entrées : 10

  [*] Résultats de scan
  Scan ID : SCAN-20241107-001
  Cible : 192.168.1.1
  Hosts découverts : 2
  Ports totaux : 5
  Vulnérabilités : 2

  [*] Vulnérabilités par sévérité
  CRITICAL : 1
  HIGH : 1

  [*] Rapport généré : rapport.txt

  [+] Scanner complété avec succès
  ═══════════════════════════════════════════════════════════════════════════

## Conseils DE RÉSOLUTION

1. Lisez les sections concernées dans main.py
2. Utilisez TOUJOURS 'with' pour les fichiers
3. Testez chaque défi indépendamment
4. Pour JSON, utilisez json.dump() et json.load()
5. Pour chemins, préférez pathlib si possible
6. Utilisez try/except pour les opérations fichiers
7. Nettoyez les fichiers temporaires après les tests
8. Pour le défi 8, combinez tous les concepts

