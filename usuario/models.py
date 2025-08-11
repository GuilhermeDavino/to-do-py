from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import date
# Create your models here.

class Usuario(AbstractUser):

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
    data_nascimento = models.DateField(default=timezone.now)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    endereco =models.TextField(max_length=200)
    cpf = models.CharField(unique=True, max_length=16)
    tipo_usuario = models.CharField(max_length=1, choices=TIPO_USUARIO_CHOICES, default='C')
    username = models.CharField(max_length=10, default="username", unique=False)

    @property
    def idade(self):
        today = date.today()
        return today.year - self.data_nascimento.year - ((today.month, today.day) < (self.data_nascimento.month, self.data_nascimento.day))
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'data_nascimento', 'sexo', 'endereco', 'cpf', 'tipo_usuario']
