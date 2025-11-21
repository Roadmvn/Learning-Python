# Exercice 02: Variables et Types - Défis

## Défi 1: Profil de pentester

Créez des variables pour un profil de pentester :
- pseudo (str)
- annees_experience (int)
- taux_reussite (float) - entre 0 et 1
- certification_oscp (bool)
- specialite (str)

Affichez toutes ces informations avec des f-strings.

## Défi 2: Configuration de scan

Créez des variables pour configurer un scan de réseau :
- ip_debut (str) - ex: "192.168.1.1"
- ip_fin (str) - ex: "192.168.1.254"
- port_debut (int)
- port_fin (int)
- timeout (float) - en secondes
- scan_agressif (bool)

Affichez un résumé de la configuration.

## Défi 3: Conversions de types

Effectuez les conversions suivantes :

1. Convertir "443" (str) en int
2. Convertir 3.14159 (float) en int (quelle valeur obtenez-vous ?)
3. Convertir 192 (int) en str
4. Convertir "True" (str) en bool (piège !)
5. Convertir 0 (int) en bool

Affichez les résultats et les types avec type().

## Défi 4: Calculs avec variables

Créez des variables :
- nombre_cibles = 50
- pourcentage_vulnerable = 0.35

Calculez :
- nombre_cibles_vulnerables (nombre × pourcentage)
- Arrondir le résultat en entier
- Afficher un message type : "17 cibles sur 50 sont vulnérables (35%)"

## Défi 5: Rapport de scan

Créez un rapport de scan avec ces variables :
- date_scan (str)
- heure_debut (str)
- heure_fin (str)
- hotes_scannes (int)
- hotes_up (int)
- ports_ouverts (int)
- vulnerabilites_trouvees (int)

Format attendu :
╔═══════════════════════════════════════╗
║      RAPPORT DE SCAN DE RÉSEAU        ║
╠═══════════════════════════════════════╣
║ Date : 2024-01-15                     ║
║ Début : 14:30:00                      ║
║ Fin : 15:45:00                        ║
║                                       ║
║ Hôtes scannés : 254                   ║
║ Hôtes actifs : 42                     ║
║ Ports ouverts : 187                   ║
║ Vulnérabilités : 12                   ║
╚═══════════════════════════════════════╝

## Défi 6: Types de données avancés

Explorez les types de données :

1. Créez une variable avec None
2. Vérifiez son type avec type()
3. Créez un nombre hexadécimal : 0xFF
4. Créez un nombre binaire : 0b1010
5. Créez un nombre avec notation scientifique : 1.5e3
6. Affichez tous ces nombres et leurs types

DÉFI BONUS : Simulateur de bruteforce

Créez des variables simulant une attaque par force brute :
- mot_de_passe_cible = "admin123"
- tentative_actuelle = 15847
- tentatives_max = 1000000
- tentatives_par_seconde = 1500
- temps_ecoule = 10.56 (secondes)

Calculez et affichez :
- Pourcentage de progression
- Temps restant estimé
- Vitesse moyenne

Utilisez des f-strings pour un affichage professionnel.

