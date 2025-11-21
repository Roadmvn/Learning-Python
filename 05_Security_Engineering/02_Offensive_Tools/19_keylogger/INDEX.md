EXERCICE 19 - KEYLOGGER
Capture et enregistrement de frappes clavier pour red teaming

FICHIERS DE L'EXERCICE
======================

1. README.md (172 lignes)
   └─ Objectifs pédagogiques, concepts clés
   └─ Architecture pynput (keyboard listener, callbacks)
   └─ Techniques: interception, logging, filtrage, stealth
   └─ Considérations éthiques et légales CRITIQUES
   └─ Références officielles

2. main.py (457 lignes)
   └─ Code exhaustif commenté en français
   └─ Classes principales:
```python
      • KeyloggerCallback: Gestion événements clavier
      • Keylogger: Orchestration principale
```
   └─ Fonctionnalités:
```python
      ✓ Capture frappes en temps réel
      ✓ Logging horodaté avec timestamps
      ✓ Filtrage données sensibles (password, etc.)
      ✓ Touches spéciales ([ENTER], [SHIFT], etc.)
      ✓ Buffer accumulation mots
      ✓ Gestion erreurs robuste
      ✓ Arrêt gracieux (Ctrl+C)
```
   └─ Utilitaires: affichage logs, effacement, vérification
   └─ USAGE:
```python
      python main.py              # Démarrer
      python main.py --logs       # Voir logs
      python main.py --path       # Chemin fichier log
      python main.py --clear      # Effacer logs

```
3. exercice.txt (421 lignes)
   └─ 8 défis progressifs:
```python
      ✓ Défi 1: Keylogger basique non-persistant (Basique)
      ✓ Défi 2: Logging fichier avec timestamps (Intermédiaire)
      ✓ Défi 3: Filtrage données sensibles (Intermédiaire)
      ✓ Défi 4: Détection application active (Avancé)
      ✓ Défi 5: Envoi logs par email SMTP (Avancé)
      ✓ Défi 6: Persistence système startup (Avancé)
      ✓ Défi 7: Encryption logs (Avancé+)
      ✓ Défi 8: Evasion antivirus obfuscation (Expert)
```
   └─ Guide progression recommandée
   └─ Considérations finales éthiques

4. solution.txt (1061 lignes)
   └─ Solutions complètes pour tous les défis
   └─ Code Python fonctionnel à adapter
   └─ Points clés apprentissage pour chaque solution
   └─ Détails implémentation techniques

PROGRESSION RECOMMANDÉE
=======================

Niveau BASIQUE (1-2 jours):
├─ Lire: README.md (concepts)
├─ Étudier: main.py (code exemple)
├─ Faire: Défi 1 (basique sans fichier)
└─ Faire: Défi 2 (logging fichier)

Niveau INTERMÉDIAIRE (3-5 jours):
├─ Faire: Défi 3 (filtrage sensibles)
├─ Faire: Défi 4 (détection app - optionnel)
├─ Faire: Défi 5 (email - optionnel)
└─ Créer: Version complète main.py

Niveau AVANCÉ (5-10 jours):
├─ Faire: Défi 6 (persistence startup)
├─ Faire: Défi 7 (encryption logs)
├─ Faire: Défi 8 (obfuscation evasion)
└─ Analyser: Techniques défense antivirus

AVERTISSEMENTS ÉTHIQUES CRITIQUES
==================================

⚠️  ILLÉGAL sans autorisation explicite du propriétaire du système
⚠️  Délit criminel: Violation grave de la vie privée
⚠️  Responsabilité civile et pénale en cas d'abus
⚠️  Usage personnel sur machines propres UNIQUEMENT
⚠️  JAMAIS sur systèmes tiers, production ou systèmes d'autrui
⚠️  Aucun déploiement, transmission ou partage
⚠️  Éducation red teaming personnel uniquement
⚠️  Non responsabilité: Usage aux risques de l'utilisateur

CODE DE CONDUITE
================

Avant d'implémenter chaque défi, demandez-vous:

1. ÉTHIQUE
   ✓ Est-ce sur ma machine personnelle?
   ✓ Puis-je justifier l'utilisation pédagogiquement?
   ✓ Ai-je intention claire et éducative?

2. LÉGALITÉ
   ✓ Conforme aux lois de ma juridiction?
   ✓ Non utilisation à fins criminel?
   ✓ Documentation pour fins éducatives?

3. SÉCURITÉ
   ✓ Code isolé/sandboxé?
   ✓ Traces effaçables facilement?
   ✓ Pas de transmission données réelles?

CONCEPTS CLÉS ABORDÉS
=====================

Techniques Capture:
├─ pynput.keyboard.Listener
├─ Callbacks on_press/on_release
├─ Distinction caractères/touches spéciales
└─ Threading pour monitoring parallèle

Logging et Persistance:
├─ Python logging module
├─ Timestamps précis (microseconde)
├─ Stockage fichier sécurisé
└─ Gestion erreurs I/O

Filtrage Sécurité:
├─ Détection patterns sensibles
├─ Buffer accumulation mots
├─ Remplacement données sensibles
└─ Logging warnings

Techniques Avancées:
├─ Détection application active (AppKit macOS)
├─ Exfiltration email (SMTP)
├─ Persistence système (LaunchAgent/Registry)
├─ Encryption logs (cryptography.fernet)
└─ Obfuscation evasion (AV detection)

RESSOURCES ADDITIONNELLES
=========================

Documentation:
├─ pynput: https://pynput.readthedocs.io/
├─ Python logging: https://docs.python.org/3/library/logging.html
├─ cryptography: https://cryptography.io/
└─ OWASP: https://owasp.org/

Défense et Détection:
├─ MITRE ATT&CK: https://attack.mitre.org/
├─ Elastic Detection: https://www.elastic.co/security
└─ NIST Cybersecurity: https://www.nist.gov/

## Conseils DE PROGRESSION
=======================

✓ Commencer simple: Défi 1-2 basiques
✓ Tester sur machine personnelle uniquement
✓ Documenter apprentissage pour chaque défi
✓ Comprendre POURQUOI chaque technologie fonctionne
✓ Étudier solutions après implémentation
✓ Progresser graduellement vers défis avancés
✓ Focus sur défense et détection: COMPRENDRE les attaques
✓ Supprimer complètement après tests

CONTACT ET SUPPORT
==================

Questions techniques:
└─ Consulter main.py et exercice.txt détails
└─ Vérifier solutions.txt pour approches

Questions éthiques/légales:
└─ Consult your local laws and regulations
└─ Parlez avec instructeur ou expert sécurité

---

Créé pour Learning-Python Exercise 19
Focus: Red teaming personnel, éducation sécurité
Format: Commentaires français, code exhaustif
