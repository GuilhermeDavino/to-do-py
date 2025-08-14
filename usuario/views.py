from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView,
)
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from platform_app.choices import SexoChoices
from .models import Usuario
from .forms import UsuarioCreateForm, UsuarioUpdateForm
from datetime import date
from django.db.models import Count
import json



class SuperUserRequiredMixin(UserPassesTestMixin):
   
    def test_func(self):
        return self.request.user.is_superuser # type: ignore

    def handle_no_permission(self):
        from django.shortcuts import redirect
        return redirect('login')




class UsuarioListView(SuperUserRequiredMixin, ListView):
    model = Usuario
    template_name = 'gerenciamento.html'
    context_object_name = 'usuarios'

    def get_queryset(self):
        return super().get_queryset()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuarios = context['usuarios']
        usuarios_forms = []
        for usuario in usuarios:
            form = UsuarioUpdateForm(instance=usuario)
            usuarios_forms.append((usuario, form))
        context['usuarios_forms'] = usuarios_forms
        context['form'] = UsuarioCreateForm()
        return context




class UsuarioDetailView(SuperUserRequiredMixin, DetailView):
    model = Usuario
    template_name = 'usuarios/detalhe.html'
    context_object_name = 'usuario'



class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioCreateForm
    template_name = 'cadastro.html'
    success_url = reverse_lazy('login')



class UsuarioUpdateView(SuperUserRequiredMixin, UpdateView):
    model = Usuario
    form_class = UsuarioUpdateForm
    template_name = 'usuarios/editar.html'
    success_url = reverse_lazy('gerenciamento')



class UsuarioDeleteView(SuperUserRequiredMixin, DeleteView):
    model = Usuario
    template_name = 'usuarios/deletar.html'
    success_url = reverse_lazy('gerenciamento')



class UsuarioDashBoardView(SuperUserRequiredMixin, ListView):
    model = Usuario
    template_name = 'dashboard.html'
    context_object_name = 'usuarios'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuarios_qs = self.get_queryset()

      
        usuarios_data = []
        for u in usuarios_qs:
            usuarios_data.append({
                'nome': u.nome,
                'email': u.email,
                'sexo': u.get_sexo_display(),
                'cpf': u.cpf,
                'data_nascimento': u.data_nascimento.strftime('%Y-%m-%d'),
                'idade': u.idade  
            })

       
        sexo_counts = usuarios_qs.values('sexo').annotate(count=Count('sexo'))
        sexo_labels = [SexoChoices(entry['sexo']).label if entry['sexo'] in SexoChoices.values else SexoChoices.NAO_INFORMADO.label for entry in sexo_counts]
        sexo_data = [entry['count'] for entry in sexo_counts]

        
        idade_dict = {}
        for u in usuarios_qs:
            idade = u.idade  
            idade_dict[idade] = idade_dict.get(idade, 0) + 1

        idade_chart_data = {
            'labels': list(idade_dict.keys()),
            'data': list(idade_dict.values())
        }

      
        context['usuarios_data'] = json.dumps(usuarios_data)
        context['sexo_data'] = json.dumps({
            'labels': sexo_labels,
            'data': sexo_data
        })
        context['idade_data'] = json.dumps(idade_chart_data)

        return context
