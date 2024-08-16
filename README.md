# Sales Analysis App avec Docker

## Description

Ce projet analyse des données de ventes à partir d'un fichier CSV, génère des statistiques et crée des graphiques montrant les tendances des ventes. L'application est dockerisée pour faciliter son exécution.

## Prérequis

- Docker installé sur votre machine
- Un fichier CSV contenant des données de ventes

## Instructions

Pour construire l'image Docker, exécutez la commande suivante :

docker build -t sales-analysis-app .

Pour analyser les données et générer le rapport, utilisez la commande suivante :

docker run -v $(pwd)/output:/app/output sales-analysis-app


Le rapport et les graphiques seront générés dans le dossier output/.

### 1. Cloner le dépôt

```bash
git clone <URL_DU_REPOSITORY>
cd <NOM_DU_REPERTOIRE>


