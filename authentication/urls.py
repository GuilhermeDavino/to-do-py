from django.urls import path 
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
   path('logar/', views.Login.as_view(), name='login'),
   path('cadastro/', views.Register.as_view(), name='register'),
   path('sair/', LogoutView.as_view(), name='logout')

]