from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView

# Create your views here.

class Login(LoginView):
    template_name = 'login/login.html'
    redirect_authenticated_user = True

class Register(CreateView):
    form_class = UserCreationForm
    template_name = 'register/register.html'
    success_url = reverse_lazy('login')




