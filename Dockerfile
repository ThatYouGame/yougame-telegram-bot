FROM python:3.11-slim

# Dossier de travail
WORKDIR /app

# Installer les dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code
COPY . .

# Lancer le bot
CMD ["python", "main.py"]
