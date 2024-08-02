# suivi_medicamenteux

# Projet : Alarme de Rappel de Prise de Médicaments et de Doses
Ce projet consiste à concevoir une alarme de rappel pour la prise de médicaments et de doses, en utilisant MicroPython et une carte ESP32. L'alarme utilise une LED, un buzzer, un écran pour afficher les informations, et inclut un serveur web ainsi qu'un point d'accès fonctionnel pour la configuration et le suivi à distance.

# Fonctionnalités
Alarme de rappel : LED et buzzer pour alerter l'utilisateur.
Affichage des informations : Écran pour afficher les informations sur les médicaments et les doses.
Serveur Web : Interface web pour configurer les rappels et surveiller les prises de médicaments.
Point d'accès : ESP32 configuré comme point d'accès pour une connexion facile au serveur web.
# Matériel Requis
ESP32
LED
Buzzer
Écran (OLED ou LCD)
Résistances et fils de connexion
Alimentation (batterie ou adaptateur secteur)
# Installation
1. Configuration de l'Environnement de Développement
Installer les outils nécessaires :

MicroPython
Thonny IDE ou tout autre IDE compatible avec MicroPython.
Flasher MicroPython sur l'ESP32 :

Télécharger l'image MicroPython pour ESP32.
Utiliser un outil comme esptool.py pour flasher l'image sur l'ESP32.
2. Déploiement du Code
Cloner le dépôt GitHub :

bash
Copier le code
git clone https://github.com/votre-utilisateur/alarme-medication.git
cd alarme-medication
Téléverser les scripts MicroPython sur l'ESP32 :

Utiliser Thonny IDE ou tout autre outil pour transférer les fichiers .py vers l'ESP32.
3. Connexion et Configuration
Allumer l'ESP32 et se connecter au point d'accès créé par l'ESP32 :

SSID : **********
Mot de passe : ********
Accéder à l'interface web :

Ouvrir un navigateur web et aller à l'adresse http://192.168.4.1.
Configurer les rappels de médicaments et de doses via l'interface web.

# Utilisation
Ajouter des rappels : Utiliser l'interface web pour ajouter ou modifier des rappels.
Vérification des alertes : Lorsque l'alarme se déclenche, la LED clignote et le buzzer émet un son.
Confirmation de prise de médicament : Confirmer la prise du médicament via l'interface web ou un bouton physique connecté à l'ESP32.
Contribuer
Les contributions sont les bienvenues ! Merci de suivre les étapes ci-dessous pour contribuer :

# Forker le dépôt
Créer une branche de fonctionnalité (git checkout -b fonctionnalite/ma-nouvelle-fonctionnalite)
Commiter les modifications (git commit -am 'Ajoute une nouvelle fonctionnalité')
Pousser vers la branche (git push origin fonctionnalite/ma-nouvelle-fonctionnalite)
Créer une Pull Request

Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus d'informations.

Acknowledgements
Merci à tous les contributeurs et aux projets open-source qui ont rendu ce projet possible.

Pour toute question ou suggestion, n'hésitez pas à ouvrir une issue sur le dépôt GitHub.

