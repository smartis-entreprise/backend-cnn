# Définir l'image de base
FROM tensorflow/tensorflow:latest

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers requis dans le répertoire de travail
COPY requirements.txt .
COPY app ./app
COPY model ./model
COPY image.jpg .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Définir les variables d'environnement
ENV PYTHONUNBUFFERED=1

# Définir le point d'entrée
ENTRYPOINT ["python", "./app/main.py"]
