EXERCICE 19 - KEYLOGGER
Capture et enregistrement de frappes clavier

AVERTISSEMENT ÉTHIQUE CRITIQUE
================================
- ILLÉGAL sans autorisation explicite du propriétaire du système
- Violation grave de la vie privée (délit criminel dans la plupart des juridictions)
- Utilisation personnelle sur machines propres UNIQUEMENT, à titre éducatif
- Aucun déploiement, transmission ou partage sur systèmes tiers
- Responsabilité personnelle et légale de l'utilisateur
- Non responsabilité : matériel fourni à titre pédagogique uniquement

Red teaming personnel uniquement. Respect scrupuleux des lois.

---

DÉFI 1: KEYLOGGER BASIQUE NON-PERSISTANT (Basique)
===================================================

Objectif:
Créer un keylogger simple qui capture et affiche les frappes clavier
en temps réel dans la console, sans sauvegarder dans un fichier.

Spécifications:
- Capturer chaque frappe du clavier
- Afficher le caractère dans le terminal en temps réel
- Afficher les touches spéciales ([ENTER], [SHIFT], etc.)
- Durée: 10 secondes maximum
- Arrêt gracieux après timeout

Fonctionnalités requises:
✓ Utilisation de pynput.keyboard.Listener
✓ Callback on_press pour chaque frappe
✓ Affichage console
✓ Gestion du timeout
✓ Arrêt gracieux (try/except)

Exemple de sortie:
[*] Keylogger basique - 10 secondes
h e l l o [SPACE] w o r l d [ENTER]
S[SHIFT] h i f t [SHIFT]

Points d'apprentissage:
- Structure basique pynput
- Événements clavier en temps réel
- Gestion des touches spéciales
- Architecture callback

---

DÉFI 2: LOGGING FICHIER AVEC TIMESTAMPS (Intermédiaire)
==========================================================

Objectif:
Ajouter la persistance fichier avec horodatage précis et
méta-informations sur la session.

Spécifications:
- Créer fichier logs/keylog_SESSION.txt (SESSION = datetime)
- Enregistrer chaque frappe avec TIMESTAMP exact
- Format: [HH:MM:SS.mmm] CHAR: 'x' ou [HH:MM:SS.mmm] SPECIAL: [ENTER]
- Enregistrer timestamp démarrage/arrêt session
- Inclure timing entre frappes (ms)
- Gestion erreurs fichier (permission, espace disque)

Fonctionnalités requises:
✓ Module datetime pour timestamps microseconde
✓ Gestion fichiers avec pathlib.Path
✓ Format structured logging
✓ Try/except pour I/O errors
✓ Nom fichier unique par session

Exemple de fichier log:
---
[14:23:45.123] START_SESSION: macOS, Python 3.9.7
[14:23:47.456] CHAR: 'h'
[14:23:47.612] CHAR: 'e' (timing: 156ms depuis dernière frappe)
[14:23:48.234] SPECIAL: [SPACE]
[14:23:50.789] END_SESSION: 5 secondes, 8 caractères
---

Points d'apprentissage:
- Timing précis avec time.perf_counter()
- Gestion fichiers robuste
- Formatage logs structurés
- Métadonnées sessions

---

DÉFI 3: FILTRAGE DE DONNÉES SENSIBLES (Intermédiaire)
=======================================================

Objectif:
Détecter et filtrer les mots-clés sensibles pour éviter
enregistrer données critiques.

Spécifications:
- Liste mots-clés sensibles: password, secret, credit card, ssn, etc.
- Détection case-insensitive
- Remplacer par [DONNÉES SENSIBLES - N chars]
- Enregistrer alert WARNING dans logs avec timestamp
- Filtrage après détection complet du mot (pas caractère par caractère)

Filtres obligatoires:
✓ password, passwd, pwd
✓ secret, key, token
✓ credit, card, ssn
✓ bitcoin, crypto, ethereum
✓ Versions françaises: motdepasse, clé, clé_api

Fonctionnalités requises:
✓ Buffer stockage mot en cours
✓ Détection fin mot (espace, entrée, ponctuation)
✓ Vérification case-insensitive
✓ Logging warnings sécurité
✓ Statistiques sessions (mots filtrés)

Exemple:
[14:23:45.123] WORD: 'username'
[14:23:46.234] CHAR: 'p', 'a', 's', 's'
[14:23:46.890] SPECIAL: [SPACE]
[14:23:47.001] WARNING: [DONNÉES SENSIBLES DÉTECTÉES - 8 chars]

Points d'apprentissage:
- Patterns de sécurité
- Buffering et parsing
- Gestion patterns sensibles

---

DÉFI 4: DÉTECTION APPLICATION ACTIVE (Avancé)
==============================================

Objectif:
Enregistrer quelle application a le focus du clavier pour
contextualiser les frappes capturées.

Spécifications:
- Intégrer module platform-spécifique:
  * Linux: utiliser wmctrl ou xdotool
  * macOS: utiliser AppKit (Cocoa)
  * Windows: utiliser ctypes + GetForegroundWindow()
- Enregistrer changement application active dans logs
- Format: [14:23:45.123] APP_CHANGE: VS Code → Slack
- Inclure dans header logs application courante
- Timing changement application (délai avant prochaines frappes)

Fonctionnalités requises:
✓ Détection OS (sys.platform)
✓ Code platform-spécifique approprié
✓ Thread dédié pour vérification périodique
✓ Cache pour éviter re-détection constante
✓ Gestion erreurs (app fermée, system changes)
✓ Clean shutdown du thread

Implémentation macOS (recommandée pour tests):
- Utiliser AppKit via PyObjC: pip install pyobjc
- NSWorkspace.sharedWorkspace().frontmostApplication

Points d'apprentissage:
- Intégration système d'exploitation
- Code platform-spécifique
- Threading pour monitoring parallèle
- Architecture modulaire

---

DÉFI 5: ENVOI LOGS PAR EMAIL (Avancé)
======================================

Objectif:
Ajouter capacité d'exfiltration données via email
pour simulating command & control.

Spécifications:
- Envoyer logs par email SMTP (Gmail recommandé)
- Trigger automatique:
  * Après N frappes (ex: tous les 100 caractères)
  * Tous les T secondes (ex: toutes les 5 minutes)
  * À heure spécifique (ex: 22:00:00 quotidien)
- Authentification sécurisée (tokens d'app, pas mots de passe)
- Logs compressés en ZIP avant envoi
- Préserver anonymat (headers modifiés?)
- Confirmation envoi dans logs

Fonctionnalités requises:
✓ Module smtplib et email.mime
✓ Configuration SMTP (Gmail/Outlook)
✓ Authentication tokens (pas credentials fichier)
✓ Compression ZIP des logs
✓ Threading pour envoi asynchrone
✓ Error handling (network, auth, disk)
✓ Gestion multi-sessions (plusieurs logs)
✓ Clean shutdown avant envoi partiel

Sécurité CRITIQUE:
✓ JAMAIS hardcoder credentials
✓ Utiliser variables d'environnement ou fichier config chiffré
✓ Tokens d'app seulement
✓ Logs temporaires effacés après succès
✓ Retry logic avec backoff exponentiel

Exemple:
[14:23:45.123] EMAIL: Envoi logs (2.3KB)...
[14:23:48.567] EMAIL: Succès (ID: mail-2024-11-07-142345)
[14:23:50.123] EMAIL: Prochainement à 14:28:50

Points d'apprentissage:
- Exfiltration données
- SMTP/email infrastructure
- Gestion secrets (tokens)
- Threading asynchrone

---

DÉFI 6: PERSISTENCE SYSTÈME - STARTUP AUTOMATIQUE (Avancé)
===========================================================

Objectif:
Configurer keylogger pour démarrage automatique au boot système.

Spécifications selon OS:

Linux (systemd):
- Créer service systemd utilisateur
- Fichier: ~/.config/systemd/user/keylogger.service
- EnableUnitFromBootup: oui
- Redémarrage automatique si crash
- Logs dans ~/.cache/keylogger/

macOS (LaunchAgent):
- Créer plist dans ~/Library/LaunchAgents/
- Propriété: Label: com.user.keylogger
- Program: path complet Python + script
- RunAtLoad: true
- KeepAlive: true
- StandardErrorPath/StandardOutPath configurés

Windows (Registry + Scheduled Task):
- Ajouter clé registry: HKCU\Software\Microsoft\Windows\CurrentVersion\Run
- Scheduled Task en arrière-plan sans fenêtre
- Trigger: On System Startup
- Hidden: Oui

Fonctionnalités requises:
✓ Détection OS automatique
✓ Création fichiers config appropriés
✓ Vérification permissions
✓ Installation avec confirmation utilisateur
✓ Logs startup/shutdown dans logs système
✓ Uninstall réversible
✓ Détection déjà installé

Défi supplémentaire:
- Masquer dans liste processus (difficile - voir défi 7)
- Ofuscation nom script
- Répertoires cachés appropriés à OS

Points d'apprentissage:
- Persistence techniques réelles
- Configuration système OS
- Autoruns et startup folders
- Architecture kernel/user space

---

DÉFI 7: ENCRYPTION LOGS (Avancé+)
==================================

Objectif:
Chiffrer les fichiers logs avec clé pour éviter lecture accidentelle.

Spécifications:
- Utiliser cryptography.fernet (symétrique, simple)
- Clé: stockée séparément ou dérivée de seed
- Chiffrer nouveau log automatiquement
- Déchiffrer à la demande avec clé
- Mode opération:
  * LOG mode: enregistrement clair en temps réel
  * ENCRYPT mode: chiffrer tous les N jours/heures
  * READ mode: déchiffrer logs pour vérification

Fonctionnalités requises:
✓ cryptography.fernet pour AES-128-CBC
✓ Génération/rotation clés
✓ Chiffrement fichier complet
✓ Déchiffrement partiel pour vérification
✓ Key management sécurisé
✓ Gestion erreurs (clé perdue, corruption)
✓ Benchmarking performance (impact CPU/IO)

Bonus:
- Chiffrement streaming pour gros logs
- Compression + chiffrement
- Authenticated encryption (HMAC vérification)
- Dual encryption (clé + password)

Points d'apprentissage:
- Cryptographie symétrique
- Gestion clés en production
- Chiffrement fichier vs en-mémoire
- Performance vs sécurité

---

DÉFI 8: EVASION ANTIVIRUS - OBFUSCATION (Expert)
================================================

Objectif:
Analyser et contourner détections antivirus courantes
pour démonstration red teaming personnel.

Contexte:
Antivirus détecte pynput + logging fichier + patterns keyboard listening.
Défi: contourner détections de signature et comportement.

Approches (à explorer):
1. Obfuscation code:
   - Renommer variables: logger → log_mgr, callback → evt_handler
   - Strings sensibles encodées: base64, ROT13, XOR
   - Code dynamique: compile(), exec()
   - Lazy imports: importer seulement si exécution

2. Anti-reverse engineering:
   - Supprimer symboles débug
   - Checksum/validation intégrité code
   - Détection débogueur/VM
   - Jitter et timing random

3. Détection antivirus:
   - Vérifier processus antivirus en exécution
   - Tester accès fichier log
   - Scanner système de fichiers
   - Vérifier connexions réseau bloquées

4. Stealth comportement:
   - Délai aléatoire avant démarrage (jitter)
   - Logs fragmentés (plusieurs fichiers)
   - Compression logs avant écriture
   - Pas d'activité réseau pendant hours
   - Arrêt lors détection threat

Spécifications minimales:
✓ Obfuscation strings critiques (pynput, logging, path)
✓ Détection antivirus/malware scanning
✓ Jitter timing (délai 0-30s avant démarrage)
✓ Logs fragmentés (rotate toutes heures)
✓ Gestion erreurs gracieuse

Spécifications avancées:
✓ Analyse système avant démarrage
✓ Code polymorphe (changement signature à runtime)
✓ Anti-debugging (détection gdb, lldb, WinDbg)
✓ Checksum validation
✓ Communication chiffrement pour C&C
✓ Nettoyage traces disque (secure delete)

Limitations éthiques:
⚠ Obfuscation seulement sur machines personnelles
⚠ Jamais sur systèmes production/tiers
⚠ Documentation claire intentions
⚠ Suppression complète après tests

Points d'apprentissage:
- Evasion techniques réelles
- Reverse engineering défenses
- Malware analysis perspective
- Advanced persistence

---

GUIDE DE DIFFICULTÉ ET PROGRESSION
===================================

Basique (1-2 jours):
├─ Défi 1: Keylogger basique non-persistant
└─ Défi 2: Logging fichier timestamps

Intermédiaire (3-5 jours):
├─ Défi 3: Filtrage sensibles
├─ Défi 4: Détection application active
└─ Défi 5: Envoi email (optionnel)

Avancé (5-10 jours):
├─ Défi 6: Persistence startup
├─ Défi 7: Encryption logs
└─ Défi 8: Evasion antivirus

ROADMAP RECOMMANDÉE:
1. Commencer Défi 1-2 pour bases pynput
2. Ajouter Défi 3 pour sécurité
3. Défi 4-5 pour features intermédiaires
4. Défi 6 pour persistence (red teaming)
5. Défi 7-8 pour advanced (recherche)

---

CONSIDÉRATIONS FINALES
======================

Avant d'implémenter chaque défi, demandez-vous:

1. ÉTHIQUE
   - Est-ce sur ma machine personnelle?
   - Puis-je justifier l'utilisation?
   - Ai-je intention pédagogique claire?

2. LÉGALITÉ
   - Conforme lois pays?
   - Non utilisation à d'autres fins?
   - Documentation autorisée?

3. SÉCURITÉ
   - Code isolation / sandboxing?
   - Trace effaçable facilement?
   - Pas de transmission données réelles?

Rappel: Ces défis sont pour comprendre DEFENSES cyberattaques,
pas pour les exécuter en réalité. Responsabilité personnelle.

Bonne progression!
