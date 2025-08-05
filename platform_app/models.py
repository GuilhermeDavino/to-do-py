from django.db import models
from django.conf import settings


class Task(models.Model):
    choices = (('D', "deletado"), ('P', "pendente"), ('C', "concluida"))
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    status = choices
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODELS,
        on_delete=models.CASCADE,
        related_name='tasks')
    
