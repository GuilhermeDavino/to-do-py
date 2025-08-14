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


class SexoChoices(models.TextChoices):
    MASCULINO = 'M', 'Masculino'
    FEMININO = 'F', 'Feminino'
    NAO_INFORMADO = 'N', 'Não informado'


class TipoUsuarioChoices(models.TextChoices):
    ADMIN = 'A', 'admin'
    COMUN = 'C', 'Comun'
