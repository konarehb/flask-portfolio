# Utiliser l'image officielle de Python comme image de base
FROM python:3.12.4-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier des dépendances dans le conteneur
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code de l'application dans le conteneur
COPY . .

# Exposer le port 5000 pour les connexions entrantes
EXPOSE 5000

# Spécifier la commande pour exécuter l'application
# Forme exec
CMD ["python", "app.py"]
# ou
# Forme shell
# CMD python ./app.py