from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone
from datetime import date

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O campo Email é obrigatório')
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('tipo_usuario', 'A')
        extra_fields.setdefault('is_active', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('Superusuário precisa ter is_staff=True.')
        if not extra_fields.get('is_superuser'):
            raise ValueError('Superusuário precisa ter is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

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

    username = None 
    nome = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField(default=timezone.now)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    endereco = models.TextField(max_length=200)
    cpf = models.CharField(unique=True, max_length=16)
    tipo_usuario = models.CharField(max_length=1, choices=TIPO_USUARIO_CHOICES, default='C')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'data_nascimento', 'sexo', 'endereco', 'cpf', 'tipo_usuario']

    objects = UsuarioManager() # type: ignore

    def __str__(self):
        return self.email

    @property
    def idade(self):
        today = date.today()
        return today.year - self.data_nascimento.year - (
            (today.month, today.day) < (self.data_nascimento.month, self.data_nascimento.day)
        )
