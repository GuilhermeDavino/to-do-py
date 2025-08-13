import datetime
from django import forms
from platform_app.choices import CategoryChoices, PriorityChoices, StatusChoices
from usuario.models import Usuario
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
        self.fields['deadline'].initial = datetime.date.today().strftime('%Y-%m-%d')



class UsuarioUpdateForm(forms.ModelForm):
    nova_senha = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua nova senha'
        }),
        label='Nova senha',
        required=False
    )
    confirmar_senha = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirme sua nova senha'
        }),
        label='Confirmar nova senha',
        required=False
    )

    class Meta:
        model = Usuario
        fields = ['email', 'nome', 'data_nascimento', 'sexo', 'endereco', 'cpf']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu e-mail'
            }),
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu nome'
            }),
            'data_nascimento': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
            'sexo': forms.Select(attrs={
                'class': 'form-select'
            }),
            'endereco': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Digite seu endereço'
            }),
            'cpf': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu CPF'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['data_nascimento'].input_formats = ['%Y-%m-%d'] # type: ignore



class TaskUpdateForm(forms.ModelForm):
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
            'deadline': forms.DateInput(format='%Y-%m-%d', attrs={
                'id': 'deadline',
                'class': 'form-control',
                'type': 'date',
                'required': True,
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.deadline:
            self.initial['deadline'] = self.instance.deadline.strftime('%Y-%m-%d')

       