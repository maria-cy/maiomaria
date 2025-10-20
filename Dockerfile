# använd lightweight Python image
FROM python:3.11-slim

# Lägg till etiketter för att koppla bilden till ditt GitHub-repo (viktigt för GHCR)
LABEL org.opencontainers.image.source="https://github.com/fikafredrik/maio3"
LABEL org.opencontainers.image.description="Virtual Diabetes Clinic ML service"
LABEL org.opencontainers.image.licenses="MIT"


WORKDIR /app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiera source code
COPY app/ ./app
COPY train.py .
COPY CHANGELOG.md .


EXPOSE 8000

# Starta FastAPI app med hjälp av Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
