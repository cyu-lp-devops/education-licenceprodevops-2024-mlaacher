# Sales Analysis App avec Docker

## Description

Ce projet analyse des données de ventes à partir d'un fichier CSV, génère des statistiques et crée des graphiques montrant les tendances des ventes. L'application est dockerisée pour faciliter son exécution.

## Prérequis

- Docker installé sur votre machine
- Un fichier CSV contenant des données de ventes

## Instructions

### 1. Cloner le dépôt


    git clone https://github.com/Koundidjo/sale_analysis.git

Une fois le dépôt cloné, accédez au répertoire du projet :

    cd <NOM_DU_REPERTOIRE>.


### 2. Structure des fichiers

Le projet devrait contenir les fichiers suivants :

    Dockerfile : Le fichier de configuration pour Docker.
    requirements.txt : Liste des dépendances Python nécessaires.
    app.py : Le script principal de l'application qui traite les données et génère les rapports.
    sales_data.csv : Le fichier CSV contenant les données de ventes à analyser.
    
### 3. Construire l'image Docker
Pour préparer l'environnement d'exécution, vous devez d'abord construire l'image Docker en utilisant le Dockerfile fourni. Exécutez la commande suivante dans le terminal :

    docker build -t sales-analysis-app .

Cette commande crée une image Docker nommée sales-analysis-app qui contient toutes les dépendances nécessaires, telles que pandas, numpy et matplotlib.

### 4. Exécuter l'application dans un conteneur Docker

Pour exécuter l'application et générer les rapports, utilisez la commande suivante :

Sur Windows (dans PowerShell) :
    
    docker run -v ${PWD}/output:/app/output sales-analysis-app

sur Window (dans Command Prompt) : 

    docker run -v "C:\<NOM_DU_REPERTOIRE>\output:/app/output" sales-analysis-app

Sur macOS ou Linux :

    docker run -v $(pwd)/output:/app/output sales-analysis-app

### 5. Vérifier les résultats

Une fois l'application exécutée, vous trouverez les fichiers suivants dans le dossier output qui a été crée  :

report.txt : Un fichier texte contenant le résumé statistique des ventes.
monthly_sales.png : Un graphique montrant les tendances des ventes mensuelles.

### 6. Nettoyer les ressources Docker (optionnel)
Pour libérer de l'espace sur votre machine, vous pouvez nettoyer les conteneurs et images Docker créés. Voici comment faire :

Lister les conteneurs Docker :

    docker ps -a

Supprimer un conteneur spécifique :

    docker rm <ID_DU_CONTENEUR>

Supprimer l'image Docker :

    docker rmi sales-analysis-app

### 7. Résolution des problèmes
Problèmes de compatibilité
Si vous rencontrez des erreurs liées aux versions de pandas ou numpy, vous pouvez ajuster les versions dans le fichier requirements.txt puis reconstruire l'image Docker.

Problèmes liés aux chemins
Si vous utilisez Windows et que vous avez des problèmes avec les chemins contenant des espaces, assurez-vous d'utiliser des guillemets doubles autour du chemin complet dans la commande docker run.

### 8. Contribuer
Si vous souhaitez contribuer à ce projet, n'hésitez pas à soumettre des pull requests. Toute suggestion d'amélioration est la bienvenue !



