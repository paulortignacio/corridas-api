#!/bin/bash
echo "Parando a api"
docker stop corridas-api

echo "Removendo a api"
docker rm corridas-api

echo "Limpando as imagens"
docker image prune -a -f

echo "Rebuildando uma nova imagem"
docker build -t corridas-api .

echo "Rodando a api"
docker run -d --name corridas-api -p 8000:8000 corridas-api

