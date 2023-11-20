from rest_framework import serializers
from .models import Administrador, Organizador, Atleta, Estado, Cidade, ContatoOrganizador, ContatoAtleta, Corrida

class AdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields = ('id', 'nome')

class OrganizadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizador
        fields = ('id', 'nome')

class AtletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atleta
        fields = ('id', 'nome', 'data_nascimento', 'genero', 'cidade')

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ('id', 'nome', 'uf')

class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cidade
        fields = ('id', 'nome', 'estado')

class ContatoOrganizadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContatoOrganizador
        fields = ('id', 'valor', 'observacao','tipo_contato', 'organizador')

class ContatoAtletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContatoAtleta
        fields = ('id', 'valor', 'observacao','tipo_contato', 'atleta')

class CorridaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corrida
        fields = ('id', 'nome', 'inicio_inscricao', 'fim_inscricao', 'data_largada', 'hora_largada', 'percurso', 'valor', 'site', 'cidade', 'organizador')