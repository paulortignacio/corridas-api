# Use uma imagem base do Python
FROM python:3.8-slim

# Instale as dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    libmariadb-dev \
    pkg-config \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo de requisitos para o contêiner
COPY requirements.txt .

# Copiar o script wait-for-db para o contêiner
COPY wait-for-db.sh /app/wait-for-db.sh


# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código para o contêiner
COPY . .

# Expõe a porta da aplicação
EXPOSE 8000

# Comando para iniciar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

