# Exercice 19 - Keylogger

## AVERTISSEMENT ÉTHIQUE CRITIQUE

**Ce code est ILLÉGAL à utiliser sans autorisation explicite du propriétaire du système.**

- Utilisation uniquement sur vos propres machines personnelles à des fins éducatives
- Violation de la vie privée : **Délit criminel** dans la plupart des juridictions
- Utilisation non autorisée : **Cybercriminalité**, responsabilité civile et pénale
- Non responsabilité : Ces matériaux sont fournis à titre pédagogique uniquement

**Red teaming personnel uniquement. Aucun déploiement sur systèmes tiers.**

---

## Objectifs Pédagogiques

### Concepts Clés
1. **Interception clavier** - Capture bas niveau des frappes clavier
2. **Monitoring système** - Surveillance d'événements système en temps réel
3. **Persistence de données** - Logging structuré dans des fichiers
4. **Techniques de dissimulation** - Exécution discrète, absence de fenêtres visibles
5. **Gestion d'erreurs robuste** - Continuation malgré exceptions
6. **Considérations éthiques et légales** - Implications de sécurité

---

## Bibliothèque Clé : pynput

### Installation
```bash
pip install pynput
```

### Architecture de pynput
```
pynput
├── keyboard
│   ├── Listener → Écouteur d'événements clavier
│   ├── on_press() → Callback lors appui touche
│   ├── on_release() → Callback lors relâchement
│   └── Key → Énumération touches spéciales
├── mouse
│   ├── Listener → Écouteur d'événements souris
│   └── Position tracking
└── Controller → Contrôle programmatique clavier/souris
```

---

## Concepts Techniques

### 1. Capture de Frappes Clavier
```python
from pynput import keyboard

def on_press(key):
    # Appelé lors de chaque appui
    try:
        char = key.char  # Touche alphanumérique
    except AttributeError:
        char = str(key)  # Touche spéciale (Shift, Ctrl, etc.)

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()  # Bloque indéfiniment
```

### 2. Logging dans Fichier
- Enregistrement horodaté des frappes
- Séparation des touches spéciales
- Format structuré pour analyse
- Gestion des exceptions (fichier verrouillé, permissions)

### 3. Filtrage des Données Sensibles
- Mots clés à filtrer (mots de passe, données sensibles)
- Distinction majuscules/minuscules
- Remplacement par placeholders

### 4. Techniques de Stealth Basique
- Exécution sans console (`.pyw` sur Windows)
- Pas de fenêtres visibles
- Processus discret en arrière-plan
- Noms de fichiers logs discrets
- Répertoires cachés

### 5. Considérations de Détection
- Monitoring des processus en arrière-plan
- Utilisation RAM/CPU
- Fichiers logs visibles dans système de fichiers
- Antivirus détectant pynput
- Audits de contrôle d'accès fichiers

---

## Structure du Code

### Composants Principaux
1. **Initialisation logging** - Création fichier log sécurisé
2. **Callback clavier** - Traitement chaque frappe
3. **Listener** - Boucle d'écoute infinie
4. **Gestion signaux** - Arrêt gracieux (Ctrl+C)

### Workflow
```
Démarrage
    ↓
Initialiser logging (horodatage, fichier)
    ↓
Créer Listener pynput
    ↓
Attendre événements clavier
    ↓
Pour chaque frappe:
    • Capturer caractère/touche
    • Appliquer filtrage
    • Enregistrer horodaté
    • Écrire dans fichier log
    ↓
Gestion arrêt gracieux (exceptions, signaux)
    ↓
Fermer fichier log
```

---

## Défis Progressifs

Voir `exercice.txt` pour 6-8 défis couvrant:
- Keylogger basique non persistant
- Logging fichier avec timestamps
- Filtrage mots-clés sensibles
- Détection application active
- Envoi logs par email
- Persistence système (startup)
- Encryption logs
- Évasion antivirus

---

## Risques de Sécurité Abordés

### Détection par Défenseurs
- Monitoring processus
- Détection fichiers logs
- Antivirus signatures
- Behavioral analysis
- Anomalies réseau (email logs)

### Mitigations Possibles
- Obfuscation code
- Encryption fichiers
- Délai aléatoire avant envoi
- Communication discrète

---

## Références Officielles
- [pynput Documentation](https://pynput.readthedocs.io/)
- [Python logging](https://docs.python.org/3/library/logging.html)
- [Threading Python](https://docs.python.org/3/library/threading.html)

---

## Considérations Finales

Ce matériel est fourni à titre **éducatif uniquement** pour comprendre:
- Techniques de cyberattaque réelles
- Importance de la sécurité système
- Bonnes pratiques défensives
- Implications éthiques et légales

**Responsabilité du développeur** : Utilisation éthique et légale uniquement.
