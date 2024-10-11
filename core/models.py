from django.db import models
from django.db.models import TextChoices

class Estado(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

class Cidade(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
class Genero(TextChoices):
    FEMININO = 'F', 'Feminino'
    MASCULINO = 'M', 'Masculino'
    
class Administrador(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class Organizador(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Atleta(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    genero = models.CharField(max_length=1, choices=Genero.choices)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class TipoContato(TextChoices):
    CELULAR = 'Celular'
    FIXO = 'Fixo'
    EMAIL = 'Email'

class ContatoOrganizador(models.Model):
    id = models.AutoField(primary_key=True)
    valor = models.CharField(max_length=100)
    observacao = models.CharField(max_length=255, blank=True)
    tipo_contato = models.CharField(max_length=10, choices=TipoContato.choices)
    organizador = models.ForeignKey(Organizador, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.tipo_contato} - {self.valor}'
    
class ContatoAtleta(models.Model):
    id = models.AutoField(primary_key=True)
    valor = models.CharField(max_length=100)
    observacao = models.CharField(max_length=255, blank=True)
    tipo_contato = models.CharField(max_length=10, choices=TipoContato.choices)
    atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.tipo_contato} - {self.valor}'

class Corrida(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    inicio_inscricao = models.DateField()
    fim_inscricao = models.DateField()
    data_largada = models.DateField()
    hora_largada = models.TimeField()
    percurso = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    site = models.CharField(max_length=150)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    organizador = models.ForeignKey(Organizador, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome