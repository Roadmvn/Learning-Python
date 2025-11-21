#!/bin/bash

# ═══════════════════════════════════════════════════════════════
# Script d'installation automatique
# Learning-Python : De Zéro au Red Teaming
# ═══════════════════════════════════════════════════════════════

set -e  # Arrêt en cas d'erreur

echo "═══════════════════════════════════════════════════════════════"
echo "  Installation Learning-Python Red Team"
echo "═══════════════════════════════════════════════════════════════"
echo ""

# ═══════════════════════════════════════════════════════════════
# 1. Vérification de Python
# ═══════════════════════════════════════════════════════════════

echo "[1/5] Vérification de Python..."

if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 n'est pas installé"
    echo "   Installez Python 3.10 ou supérieur depuis https://www.python.org/"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
REQUIRED_VERSION="3.10"

if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then
    echo "❌ Python $PYTHON_VERSION détecté. Python 3.10+ requis."
    exit 1
fi

echo "✅ Python $PYTHON_VERSION détecté"
echo ""

# ═══════════════════════════════════════════════════════════════
# 2. Création de l'environnement virtuel
# ═══════════════════════════════════════════════════════════════

echo "[2/5] Création de l'environnement virtuel..."

if [ -d "venv" ]; then
    echo "⚠️  L'environnement virtuel existe déjà"
    read -p "   Voulez-vous le recréer ? (y/N) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        rm -rf venv
        python3 -m venv venv
        echo "✅ Environnement virtuel recréé"
    else
        echo "✅ Environnement existant conservé"
    fi
else
    python3 -m venv venv
    echo "✅ Environnement virtuel créé"
fi
echo ""

# ═══════════════════════════════════════════════════════════════
# 3. Activation de l'environnement virtuel
# ═══════════════════════════════════════════════════════════════

echo "[3/5] Activation de l'environnement virtuel..."

source venv/bin/activate

echo "✅ Environnement activé"
echo ""

# ═══════════════════════════════════════════════════════════════
# 4. Mise à jour de pip
# ═══════════════════════════════════════════════════════════════

echo "[4/5] Mise à jour de pip..."

pip install --upgrade pip --quiet

echo "✅ Pip mis à jour"
echo ""

# ═══════════════════════════════════════════════════════════════
# 5. Installation des dépendances
# ═══════════════════════════════════════════════════════════════

echo "[5/5] Installation des dépendances..."

if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt --quiet
    echo "✅ Dépendances installées"
else
    echo "⚠️  requirements.txt non trouvé"
fi
echo ""

# ═══════════════════════════════════════════════════════════════
# Vérifications post-installation
# ═══════════════════════════════════════════════════════════════

echo "═══════════════════════════════════════════════════════════════"
echo "  Vérifications"
echo "═══════════════════════════════════════════════════════════════"
echo ""

echo "Python : $(python --version)"
echo "Pip    : $(pip --version | cut -d' ' -f1,2)"
echo ""

echo "Packages installés :"
pip list --format=columns | grep -E "pynput|scapy|requests" || echo "  Aucun package spécifique"
echo ""

# ═══════════════════════════════════════════════════════════════
# Instructions finales
# ═══════════════════════════════════════════════════════════════

echo "═══════════════════════════════════════════════════════════════"
echo "  Installation terminée !"
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "Prochaines étapes :"
echo ""
echo "1. Activer l'environnement virtuel :"
echo "   source venv/bin/activate"
echo ""
echo "2. Lire la documentation :"
echo "   cat README.md"
echo "   cat PROGRESSION.md"
echo ""
echo "3. Commencer l'exercice 01 :"
echo "   cd exercices/01_hello_print"
echo "   cat README.md"
echo "   python main.py"
echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "  ⚠️  AVERTISSEMENT ÉTHIQUE"
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "Les outils développés dans ce projet sont à des fins"
echo "pédagogiques UNIQUEMENT."
echo ""
echo "Utilisation autorisée :"
echo "  ✅ Environnements de test personnels"
echo "  ✅ Machines virtuelles isolées"
echo "  ✅ Avec autorisation écrite explicite"
echo ""
echo "Utilisation interdite :"
echo "  ❌ Systèmes sans autorisation"
echo "  ❌ Activités malveillantes"
echo "  ❌ Violation de la vie privée"
echo ""
echo "Vous êtes seul responsable de vos actions."
echo ""
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "Bon apprentissage ! 🐍"
echo ""
