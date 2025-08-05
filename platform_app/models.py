from django.db import models
from django.conf import settings


class Task(models.Model):
    STATUS_CHOICES = (
        ('D', "Deletado"),
        ('P', "Pendente"),
        ('C', "Concluída"),
    )

    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    
