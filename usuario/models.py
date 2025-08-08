from django.db import models

# Create your models here.

class usuario(models.Model):

    SEXO_CHOICES = [
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('N', 'Não informado'),
] 
    
    TIPO_USUARIO_CHOICES = [
        ('A', 'admin'),
        ('C', 'Comun'),
    ]

    nome = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    endereco =models.TextField(max_length=200)
    cpf = models.CharField(unique=True, max_length=16)
    tipo_usuario = models.CharField(max_length=1, choices=TIPO_USUARIO_CHOICES)

