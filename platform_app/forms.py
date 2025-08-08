import datetime
from django import forms
from platform_app.choices import CategoryChoices, PriorityChoices, StatusChoices
from .models import Task
import datetime
from django import forms
from .models import Task, StatusChoices, PriorityChoices, CategoryChoices

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'priority', 'category', 'deadline']

        widgets = {
            'title': forms.TextInput(attrs={
                'id': 'title',
                'maxlength': 20,
                'class': 'form-control',
                'required': True,
            }),
            'description': forms.Textarea(attrs={
                'id': 'description',
                'maxlength': 100,
                'class': 'form-control',
                'rows': 2,
                'required': True,
            }),
            'status': forms.Select(attrs={
                'id': 'status',
                'class': 'form-select',
                'required': True,
            }),
            'priority': forms.Select(attrs={
                'id': 'priority',
                'class': 'form-select',
                'required': True,
            }),
            'category': forms.Select(attrs={
                'id': 'category',
                'class': 'form-select',
                'required': True,
            }),
            'deadline': forms.DateInput(attrs={
                'id': 'deadline',
                'class': 'form-control',
                'type': 'date',
                'required': True,
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].initial = 'Nova tarefa'
        self.fields['description'].initial = 'Descrição da tarefa'
        self.fields['status'].initial = StatusChoices.PENDENTE
        self.fields['priority'].initial = PriorityChoices.MEDIA
        self.fields['category'].initial = CategoryChoices.PESSOAL
        self.fields['deadline'].initial = datetime.date.today()