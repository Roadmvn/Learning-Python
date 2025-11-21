# Exercice 20 : Password Cracker en Python

## Objectifs d'Apprentissage

- Comprendre les concepts de brute force et attaque par dictionnaire
- Maîtriser le calcul de hash avec `hashlib` (MD5, SHA256)
- Implémenter des crackers de mots de passe efficaces
- Utiliser le multi-threading pour accélérer les attaques
- Implémenter un rate limiting éthique
- Générer des listes de mots (wordlists)
- Mesurer les performances et statistiques d'attaque
- Appliquer les techniques de cybersécurité défensive

## Avertissement Éthique et Légal

**USAGE UNIQUEMENT AUTORISÉ** :
- Cracker uniquement vos propres mots de passe
- Utiliser uniquement dans un cadre éducatif
- Obtenir l'autorisation écrite avant test sur d'autres systèmes
- Respecter toutes les lois applicables

**USAGE INTERDIT** :
- Cracker les mots de passe d'autres personnes
- Utiliser sans autorisation sur des systèmes externes
- Utiliser à des fins malveillantes
- Dépasser les limites légales de votre juridiction

Violation = Responsabilité légale et poursuites criminelles.

## Concepts Clés

### Brute Force (Attaque Par Force Brute)

L'attaque brute force teste tous les mots de passe possibles jusqu'à trouver le bon.

```
Brute Force Attack:
├── Caractères disponibles: a-z, A-Z, 0-9, symboles
├── Longueur initiale: 1 caractère
│   ├── Test: a, b, c, ... z, A, B, ...
│   └── Complexité: 26 + 26 + 10 + n symboles
├── Longueur 2: aa, ab, ac, ... zz
│   └── Complexité: 62^2 = 3,844 (sans symboles)
├── Longueur 3: aaa, aab, ...
│   └── Complexité: 62^3 = 238,328
└── Longueur N: (62)^N - EXPLOSION EXPONENTIELLE!

Exemple (minuscules + majuscules + chiffres = 62 caractères):
├── Longueur 4: 62^4 = 14,776,336 tentatives
├── Longueur 6: 62^6 = 56,800,235,584 tentatives
├── Longueur 8: 62^8 = 218,340,105,584,896 tentatives (impraticable!)
└── Longueur 12: 62^12 = 475,920,314,814,253,376 (impossible)
```

**Avantages** :
- Fonctionne contre n'importe quel mot de passe
- Peut trouver des patterns faibles
- Pas besoin de ressources externes

**Inconvénients** :
- Exponentiellement lent pour les longs mots de passe
- Impraticable pour les mots de passe forts (8+ caractères aléatoires)
- Consomme énormément de ressources CPU

**Cas d'usage réel** :
- Cracker des mots de passe oubliés personnels
- Mots de passe très courts (3-4 caractères)
- Patterns connus (dates, suites numériques)

### Dictionary Attack (Attaque Par Dictionnaire)

L'attaque par dictionnaire utilise une liste prédéfinie de mots courants.

```
Dictionary Attack:
├── Source de mots: Dictionnaire (rockyou.txt, etc.)
├── Stratégie 1: Mots simples
│   ├── password, 123456, qwerty, admin
│   └── Très rapide (quelques secondes généralement)
├── Stratégie 2: Mots avec variations
│   ├── password → Password, PASSWORD, passw0rd, p@ssw0rd
│   ├── Variations: capitalization, l33t speak, ajout de chiffres
│   └── Plus lent mais très efficace
└── Stratégie 3: Combinaisons (hybride)
    ├── password + 123, password + 2024
    ├── Marque + chiffre courant
    └── Très efficace sur mots de passe "faibles"
```

**Efficacité réelle** :
```
rockyou.txt (14 millions de mots):
├── Sans variations: ~14M tests
├── Avec 1 variation par mot: ~28M tests
├── Avec 3 variations par mot: ~42M tests

Résultat empirique:
├── 80% des mots de passe trouvés avec les 1,000 premiers mots
├── 95% trouvés avec les 100,000 premiers mots
├── rockyou.txt craque ~98% des mots de passe faibles
```

**Avantages** :
- Très rapide (quelques minutes pour 14M mots)
- Efficace contre les mots de passe courants
- Peu de ressources nécessaires

**Inconvénients** :
- Ne fonctionne que si le mot de passe est dans la liste
- Nécessite une bonne wordlist
- Inefficace contre les mots de passe aléatoires

**Cas d'usage réal** :
- Attaques réalistes (80% success rate)
- Cracking de hashs d'archives ZIP, RAR, PDF
- Entrée par entrée en bases de données compromises

### Hashing Cryptographique

Le hashing transforme un mot de passe en une chaîne fixe de caractères.

```
Processus de Hashing:
├── Input (mot de passe): "password123"
├── Fonction hash (ex: SHA256)
├── Output (hash): "ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f"
│
└── Propriétés fondamentales:
    ├── Déterministe: même input → même output (toujours)
    ├── Rapide: calcul très rapide (problème!)
    ├── Non-réversible: impossible de retrouver le mot de passe du hash
    ├── Sensible au moindre changement: petit changement = hash complètement différent
    └── Collision rare: deux inputs différents = hash TRÈS rarement identique
```

**Hashes courants en cybersécurité** :
```
MD5 (DÉPRÉCIÉ - NE PLUS UTILISER):
├── Taille: 32 caractères hexadécimaux
├── "password" → "5f4dcc3b5aa765d61d8327deb882cf99"
├── Rapide: 1,000,000+ hashs/seconde
├── Problème: Collisions trouvées (non sûr)
└── Cas d'usage: Legacy uniquement, JAMAIS nouveau code

SHA1 (DÉPRÉCIÉ):
├── Taille: 40 caractères hexadécimaux
├── "password" → "5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8"
├── Problème: Collisions théoriques trouvées
└── Cas d'usage: Legacy, JAMAIS pour nouveaux systèmes

SHA256 (BON CHOIX):
├── Taille: 64 caractères hexadécimaux
├── "password" → "5e884898da28047151d0e56f8dc62927..."
├── Sûr et rapide (pour l'instant)
└── Cas d'usage: Bon choix pour les applications modernes

SHA512 (TRÈS SÛRE):
├── Taille: 128 caractères hexadécimaux
├── Très lent (bonne chose pour les attaques!)
├── Plus lent = plus difficile à cracker
└── Cas d'usage: Données très sensibles

bcrypt (EXCELLENT CHOIX):
├── Fonction d'hashing spécifique aux mots de passe
├── Inclut un "salt" (donnée aléatoire)
├── Delibérément lente (configurable)
├── Quasiment impossible à cracker (même avec GPU)
└── Cas d'usage: RECOMMANDÉ pour tous nouveaux systèmes

argon2 (MEILLEUR CHOIX):
├── Fonction d'hashing moderne (2015)
├── Résistant aux attaques par force brute
├── Résistant aux attaques GPU
├── Configurable en temps/mémoire
└── Cas d'usage: Systèmes haute-sécurité (2024+)
```

**Pourquoi cracker un hash** :
```
Workflow typique:
├── Attaquant obtient une liste de hashs compromis
├── Attaquant crée une table de hashs pré-calculés (rainbow table)
├── Attaquant compare les hashs compromis avec la table
├── Match trouvé = mot de passe retrouvé

Défense (salt):
├── Ajouter une donnée aléatoire avant hashing
├── "password" + salt "abc123" → hash unique
├── Rainbow tables deviennent inutiles
├── bcrypt/argon2 incluent le salt
```

### Multi-Threading pour Accélération

Le multi-threading permet de paralléliser les tests de mots de passe.

```
Mono-thread vs Multi-thread:
├── MONO-THREAD:
│   ├── CPU utilisation: ~10% (1 core sur 8+)
│   └── Lenteur: Énorme gaspillage de ressources
│
└── MULTI-THREAD (4 threads):
    ├── CPU utilisation: ~40% (4 cores utilisés)
    ├── Speedup: ~4x plus rapide
    └── Chaque thread = 25% des mots de passe
```

**Architecture multi-thread** :
```
Thread Manager:
├── Thread 1: Tests mots 0-100,000
├── Thread 2: Tests mots 100,000-200,000
├── Thread 3: Tests mots 200,000-300,000
├── Thread 4: Tests mots 300,000-400,000
│
└── Main thread: Attendre les résultats + afficher stats
    └── LOCK/SYNCHRONISATION: Pas de race conditions
```

**Performance réelle** :
```
Benchmark: Cracker rockyou.txt (14M mots) contre MD5:
├── 1 thread: ~45 secondes
├── 2 threads: ~23 secondes (2.0x speedup)
├── 4 threads: ~12 secondes (3.75x speedup)
├── 8 threads: ~7 secondes (6.4x speedup) ← Décrochage limité par I/O
└── 16 threads: ~6 secondes (7.5x speedup) ← Contention mémoire
```

**Pièges du multi-threading** :
```
Race Conditions (résultat imprévisible):
├── MAUVAIS: Deux threads modifient la même variable
├── Résultat: Corruption de données
│
Race-Free (bon):
├── Utiliser threading.Lock() pour synchronisation
├── Utiliser queue.Queue() pour thread-safe communication
└── Résultat: Comportement prévisible
```

### Rate Limiting Éthique

Le rate limiting limite les tentatives par seconde pour respecter les limites de sécurité.

```
Pourquoi rate limiting:
├── Les systèmes réels limitent les tentatives échouées
├── Après 3-5 tentatives: Compte verrouillé (anti-brute force)
├── Délai croissant: 1sec, 5sec, 1min, 1h
│
Rate limiting simulation:
├── Délai entre tentatives: 0.1 secondes
├── Tentatives par seconde: 10 max
├── Total pour 1 million mots: ~100,000 secondes = 27 heures
```

**Implémentation simple** :
```python
# Sans rate limiting: Trop rapide, irréaliste
for password in wordlist:
    test_password(password)  # Milliers par seconde

# Avec rate limiting: Réaliste et éthique
for password in wordlist:
    test_password(password)
    time.sleep(0.1)  # Max 10 tentatives/seconde
```

### Wordlist Generation

Générer des listes de mots pour les attaques par dictionnaire.

```
Sources de wordlists:
├── Listes publiques:
│   ├── rockyou.txt (14M mots, la plus célèbre)
│   ├── darkweb2017.txt (15M mots)
│   ├── darkweb2019.txt (800M mots)
│   ├── 1000-most-common-passwords.txt
│   └── passwords_curated.txt
│
└── Générées intelligemment:
    ├── Années courantes: 2020, 2021, ..., 2025
    ├── Saisons: Spring, Summer, Fall, Winter
    ├── Noms courants + chiffres: John123, Maria2024
    ├── Variantes: password, Password, PASSWORD, p@ssw0rd
    └── Combinaisons hybrides: admin + 1234
```

**Fichier wordlist typique** :
```
password
123456
12345678
qwerty
abc123
monkey
1234567
letmein
dragon
111111
123123
football
baseball
...
(des millions de mots)
```

**Génération simple** :
```
Années communes: 1990-2025 = 35 ans
Mois: 01-12 = 12 mois
Jours: 01-31 = 31 jours

Wordlist dates: 1990, 1991, ..., 2025
Avec variations: 19901, 1990!, 1990@, etc.
```

## Applications en Cybersécurité

### Pentesting Éthique

```
Workflow pentest autorisé:
├── Contrat signé avec client
├── Autorisation écrite explicit
├── Scope défini (IP, domaines, systèmes)
│
├── Test 1: Utiliser dictionary attack
│   └── 80% des mots de passe trouvés
├── Test 2: Brute force sur mots de passe oubliés
│   └── Retrouver les mots de passe d'admin temporaires
├── Test 3: Hash cracking (si breach simulée)
│   └── Démontrer la faiblesse du hashing simple
│
└── Rapport: Recommandations de sécurité
    ├── Implémenter bcrypt/argon2
    ├── Politique de mots de passe forts
    ├── Rate limiting et lockout
    └── MFA obligatoire
```

### Forensics et Incident Response

```
Scenario: Compte compromis trouvé
├── Attaquant a changé le mot de passe
├── Administrateur doit retrouver le compte
│
Processus:
├── Extraire le hash du compte (si possible)
├── Cracker le hash avec dictionary attack
├── Retrouver le mot de passe original
├── Vérifier les logs d'accès avec ce mot de passe
└── Déterminer le moment exact du compromise
```

### Recherche en Sécurité

```
Études de sécurité:
├── Analyser les mots de passe compromis publiquement
├── Identifier les patterns courants
├── Créer des wordlists optimisées
├── Proposer des politique de mots de passe meilleures
│
Résultats typiques:
├── 40% des mots de passe contiennent l'année courante
├── 30% contiennent le mois de naissance
├── 25% utiliseront des variantes (123, !)
└── Wordlist de 100K mots craque 95% des mots de passe "normaux"
```

## Bonnes Pratiques de Sécurité

### 1. JAMAIS cracker sans autorisation

```python
# ILLEGAL - Peut entraîner des poursuites criminelles
wordlist = load_wordlist('rockyou.txt')
for password in wordlist:
    test_against_external_service(password)  # CRIMINEL!

# LEGAL et ÉTHIQUE - Votre propre compte ou autorisé
wordlist = load_wordlist('rockyou.txt')
for password in wordlist:
    test_against_your_own_hash(password)  # OK
```

### 2. Hashing sûr: Utiliser bcrypt ou argon2

```python
# MAUVAIS - MD5 et SHA256 sont trop rapides à cracker
import hashlib
password = "mypassword"
hash = hashlib.sha256(password.encode()).hexdigest()

# BON - bcrypt est conçu pour résister aux attaques
import bcrypt
password = "mypassword"
hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
```

### 3. Implémenter le rate limiting

```python
# SANS rate limiting: 1,000,000 tentatives par seconde
# Cracker un million mots de passe en 1 seconde (trop puissant)

# AVEC rate limiting: 10 tentatives par seconde
time.sleep(0.1)  # Délai entre chaque tentative
# Cracker un million mots de passe en 100,000 secondes (27h)
```

### 4. Utiliser des salts

```python
# MAUVAIS: Pas de salt, vulnérable aux rainbow tables
hash = hashlib.sha256(password.encode()).hexdigest()

# BON: Ajouter un salt aléatoire
import secrets
salt = secrets.token_hex(16)
hash = hashlib.sha256((salt + password).encode()).hexdigest()
# Même mot de passe = hash différent à chaque fois
```

### 5. Implémenter un lockout

```python
# Simulation basique de lockout
failed_attempts = {}

def try_password(username, password):
    if failed_attempts.get(username, 0) >= 3:
        raise PermissionError(f"Account {username} locked (3 failed attempts)")

    if password != correct_password:
        failed_attempts[username] = failed_attempts.get(username, 0) + 1
        return False

    failed_attempts[username] = 0  # Reset on success
    return True
```

## Outils Utiles

### Python Modules

```python
import hashlib          # MD5, SHA1, SHA256, SHA512
import secrets          # Génération de tokens sécurisés
import string           # Chaînes de caractères (ascii_lowercase, etc.)
import itertools        # Combinaisons et permutations
import threading        # Multi-threading
import queue            # Thread-safe communication
import time             # Timing et delays
import getpass          # Entrée masquée de mot de passe
```

### Wordlist Sources

```
Communauté:
├── rockyou.txt (14M mots) - Disponible légalement
├── SecLists (GitHub) - Collection massive
├── Weakpass.com - Bases de données compilées
├── Have I Been Pwned (HIBP) - Données de breach
└── Wordlist Combinator - Générer des listes personnalisées
```

### External Tools

```
Hashcat:
├── GPU-accelerated password cracking
├── Support MD5, SHA256, bcrypt, argon2
├── Très rapide (millions de hashs/seconde avec GPU)
└── Usage: hashcat -a 0 -m 1400 hash.txt wordlist.txt

John the Ripper:
├── Outil classique de password cracking
├── Format auto-detection
├── Très flexible et extensible
└── Usage: john --wordlist=wordlist.txt hash.txt

Online Lookup Services (NO!):
├── Ne JAMAIS soumettre de hashs à des services online
├── Risque d'interception
├── Violation de confidentialité
└── Illégal dans certaines juridictions
```

## Avertissements Critiques de Sécurité

### Usage Autorisé Uniquement

1. **Vos propres comptes**: OK
   - Mot de passe oublié de votre propre compte
   - Test de votre propre système

2. **Tests autorisés**: OK avec contrat
   - Pentesting avec autorisation écrite
   - Red team exercices interne
   - Recherche académique avec consentement

3. **Everything else**: INTERDIT
   - Cracker les mots de passe d'autres personnes
   - Attaquer des systèmes sans autorisation
   - Tout usage malveillant

### Responsabilité Légale

```
Conséquences de l'usage non autorisé:
├── Pénal:
│   ├── Accès frauduleux à système informatique
│   ├── Vol d'identité
│   ├── Fraude informatique
│   └── Prison + amendes substantielles
│
├── Civil:
│   ├── Poursuites en dommages-intérêts
│   ├── Violation RGPD (Europe)
│   ├── Violation CFAA (États-Unis)
│   └── Responsabilité illimitée
│
└── Professionnel:
    ├── Antécédents judiciaires
    ├── Interdiction d'exercice
    ├── Blacklist de l'industrie
    └── Carrière terminée
```

## Ressources Pédagogiques

### Articles Techniques

- OWASP Password Storage Cheat Sheet
- CWE-307: Improper Restriction of Rendered UI Layers
- CWE-326: Inadequate Encryption Strength
- "Distributed Password Cracking" papers

### Livres Recommandés

- "The Web Application Hacker's Handbook"
- "Penetration Testing" (Georgia Weidman)
- "Cryptography Engineering" (Ferguson, Schneier, Kohno)

### Ressources Éthiques

- Hack The Box (plateforme légale)
- TryHackMe (apprentissage guidé)
- OWASP WebGoat (intentionnellement vulnérable)
- OverTheWire Wargames (CTF légitime)

### Hash Sources de Test

- HackTheBox
- TryHackMe
- CTFlearn
- OWASP Juice Shop
- Deliberately vulnerable applications

Utilisez UNIQUEMENT ces ressources légales pour l'apprentissage!

## Résumé des Techniques

```
Technique            Vitesse        Efficacité    Cas d'Usage
─────────────────────────────────────────────────────────────
Brute Force (full)   Très lent      Universelle   Mots courts
Dictionary Attack    Très rapide    Réaliste      Mots faibles
Hybrid (dict+brute)  Rapide         Très bonne    Variantes
Rainbow Tables       Instant        Excellente    Sans salt
GPU Cracking         Extrême        Excellent     Hash faible
Wordlist Combo       Très rapide    Très bonne    Mots courants
```

Choisir selon l'objectif et les contraintes!
