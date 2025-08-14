from django.urls import path 
from . import views
from django.contrib.auth.views import LogoutView
from django.views.decorators.http import require_GET
from django.utils.decorators import method_decorator

urlpatterns = [
   path('logar/', views.Login.as_view(), name='login'),
   path('sair/', views.LogOut.as_view(), name='logout'),
   path('', views.home)

]