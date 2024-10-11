from rest_framework import serializers
from .models import Administrador, Organizador, Atleta, Estado, Cidade, ContatoOrganizador, ContatoAtleta, Corrida

class AdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields = ('id', 'nome', 'username', 'password')

class OrganizadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizador
        fields = ('id', 'nome', 'username', 'password')

class AtletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atleta
        fields = ('id', 'nome', 'data_nascimento', 'genero', 'cidade', 'username', 'password')

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ('id', 'nome', 'uf')

class CidadeSerializer(serializers.ModelSerializer):
    estado = EstadoSerializer()
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

#class CorridaSerializer(serializers.ModelSerializer):
#    cidade = CidadeSerializer()
#    class Meta:
#        model = Corrida
#        fields = ('id', 'nome', 'inicio_inscricao', 'fim_inscricao', 'data_largada', 'hora_largada', 'percurso', 'valor', 'site', 'cidade', 'organizador')

class CorridaSerializer(serializers.ModelSerializer):
    cidade = CidadeSerializer()

    class Meta:
        model = Corrida
        fields = ('id', 'nome', 'inicio_inscricao', 'fim_inscricao', 'data_largada', 'hora_largada', 'percurso', 'valor', 'site', 'cidade', 'organizador')

    def create(self, validated_data):
        cidade_data = validated_data.pop('cidade')
        estado_data = cidade_data.pop('estado')

        # Crie o estado se ele não existir
        estado, created = Estado.objects.get_or_create(**estado_data)

        # Crie a cidade com o estado que você acabou de criar ou obter
        cidade = Cidade.objects.create(estado=estado, **cidade_data)

        # Agora, crie a corrida
        corrida = Corrida.objects.create(cidade=cidade, **validated_data)
        return corrida

    def update(self, instance, validated_data):
        cidade_data = validated_data.pop('cidade')
        
        # Atualiza o estado
        estado_data = cidade_data.pop('estado')
        estado, created = Estado.objects.get_or_create(**estado_data)
        
        # Atualiza a cidade
        instance.cidade.estado = estado
        instance.cidade.nome = cidade_data.get('nome', instance.cidade.nome)
        instance.cidade.save()

        # Atualiza os outros campos da corrida
        instance.nome = validated_data.get('nome', instance.nome)
        instance.inicio_inscricao = validated_data.get('inicio_inscricao', instance.inicio_inscricao)
        instance.fim_inscricao = validated_data.get('fim_inscricao', instance.fim_inscricao)
        instance.data_largada = validated_data.get('data_largada', instance.data_largada)
        instance.hora_largada = validated_data.get('hora_largada', instance.hora_largada)
        instance.percurso = validated_data.get('percurso', instance.percurso)
        instance.valor = validated_data.get('valor', instance.valor)
        instance.site = validated_data.get('site', instance.site)
        instance.save()
        
        return instance
