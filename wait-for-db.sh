#!/bin/sh

# Espera o banco de dados ficar disponível
echo "Aguardando o banco de dados..."

while ! nc -z $DB_HOST $DB_PORT; do
  sleep 1
done

echo "Banco de dados está pronto. Iniciando a aplicação..."
exec "$@"
