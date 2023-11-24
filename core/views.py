from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from .models import Administrador, Organizador, Atleta, Estado, Cidade, ContatoOrganizador, ContatoAtleta, Corrida
from .serializers import AdministradorSerializer, OrganizadorSerializer, AtletaSerializer, EstadoSerializer, CidadeSerializer, ContatoOrganizadorSerializer, ContatoAtletaSerializer, CorridaSerializer

class AdministradorViewSet(viewsets.ModelViewSet):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username','password']

class OrganizadorViewSet(viewsets.ModelViewSet):
    queryset = Organizador.objects.all()
    serializer_class = OrganizadorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username','password']

class AtletaViewSet(viewsets.ModelViewSet):
    queryset = Atleta.objects.all()
    serializer_class = AtletaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username','password']

class ContatoOrganizadorViewSet(viewsets.ModelViewSet):
    queryset = ContatoOrganizador.objects.all()
    serializer_class = ContatoOrganizadorSerializer

class ContatoAtletaViewSet(viewsets.ModelViewSet):
    queryset = ContatoAtleta.objects.all()
    serializer_class = ContatoAtletaSerializer

# Endpoints abertos ao público
class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

class CidadeViewSet(viewsets.ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['estado']

class CorridaViewSet(viewsets.ModelViewSet):
    queryset = Corrida.objects.all()
    serializer_class = CorridaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['organizador','cidade']
