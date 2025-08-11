from django.utils import timezone
from django.db import models
from django.conf import settings


import datetime
from django.utils import timezone
from django.db import models
from django.conf import settings
from .choices import StatusChoices, PriorityChoices, CategoryChoices



class Task(models.Model):
    

    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=1, choices=StatusChoices.choices, default=StatusChoices.PENDENTE)
    priority = models.CharField(max_length=6, choices=PriorityChoices.choices, default=PriorityChoices.MEDIA)
    category = models.CharField(max_length=12, choices=CategoryChoices.choices, default=CategoryChoices.PESSOAL)
    created_at = models.DateTimeField(default=timezone.now)
    deadline = models.DateField(default=timezone.now)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
