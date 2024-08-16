# Utiliser une image Python de base
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier tous les fichiers dans le répertoire de travail du conteneur
COPY . .

# Installer les dépendances nécessaires
RUN pip install -r requirements.txt

# Exécuter l'application
CMD ["python", "app.py"]
