from django.db import models

class StatusChoices(models.TextChoices):
    ATRASADA = 'A', "Atrasada"
    PENDENTE = 'P', "Pendente"
    CONCLUIDA = 'C', "Concluída"

class PriorityChoices(models.TextChoices):
    BAIXA = 'Baixa', 'Baixa'
    MEDIA = 'Média', 'Média'
    ALTA = 'Alta', 'Alta'

class CategoryChoices(models.TextChoices):
    TRABALHO = 'T', "Trabalho"
    ESTUDO = 'E', "Estudos",
    PESSOAL = 'P', "Pessoal"