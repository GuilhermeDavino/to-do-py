from django.utils import timezone
from django.db import models
from django.conf import settings


import datetime
from django.utils import timezone
from django.db import models
from django.conf import settings

from usuario.models import Usuario
from .choices import StatusChoices, PriorityChoices, CategoryChoices



class Task(models.Model):
    

    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=1, choices=StatusChoices.choices, default=StatusChoices.PENDENTE)
    priority = models.CharField(max_length=6, choices=PriorityChoices.choices, default=PriorityChoices.MEDIA)
    category = models.CharField(max_length=12, choices=CategoryChoices.choices, default=CategoryChoices.PESSOAL)
    created_at = models.DateTimeField(default=timezone.now)
    deadline = models.DateField(default=timezone.now)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='tasks')

    def save(self, *args, **kwargs):
        if self.deadline < timezone.now().date() and self.status != 'C':
            self.status = 'A'
        super().save(*args, **kwargs)

    
    def status_css_class(self):
       if self.status == 'C':
            return 'status-concluida'
       elif self.status == 'A':
            return 'status-atrasada'
       return ''
    
