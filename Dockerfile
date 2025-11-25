FROM python:3.11-slim

# Dossier de travail dans le conteneur
WORKDIR /app

# Installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code
COPY . .

# Commande de démarrage (la même que sur Railway)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
