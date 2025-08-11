from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario

class UsuarioCreateForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = [
            'email', 'nome', 'data_nascimento', 'sexo',
            'endereco', 'cpf',  # Ignorando tipo_usuario
            'password1', 'password2',
        ]
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'sexo': forms.Select(),
            'endereco': forms.Textarea(attrs={'rows': 3}),
        }


class UsuarioUpdateForm(forms.ModelForm):
    nova_senha = forms.CharField(
        label="Nova senha",
        widget=forms.PasswordInput,
        required=False
    )
    confirmar_senha = forms.CharField(
        label="Confirmar nova senha",
        widget=forms.PasswordInput,
        required=False
    )

    class Meta:
        model = Usuario
        fields = [
            'email', 'nome', 'data_nascimento', 'sexo',
            'endereco', 'cpf',
        ]
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'sexo': forms.Select(),
            'endereco': forms.Textarea(attrs={'rows': 3}),
        }

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("nova_senha")
        confirmar = cleaned_data.get("confirmar_senha")

        if senha or confirmar:
            if senha != confirmar:
                raise forms.ValidationError("As senhas não coincidem.")
        return cleaned_data

    def save(self, commit=True):
        usuario = super().save(commit=False)
        nova_senha = self.cleaned_data.get("nova_senha")

        if nova_senha:
            usuario.set_password(nova_senha)

        if commit:
            usuario.save()
        return usuario