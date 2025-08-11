from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView,
)
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Usuario
from .forms import UsuarioCreateForm, UsuarioUpdateForm



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



class UsuarioCreateView(SuperUserRequiredMixin, CreateView):
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
    
