
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastro/', views.UsuarioCreateView.as_view(), name="usuario_create"),
    path('gerenciamento/', views.UsuarioListView.as_view(), name='gerenciamento'),
    path('atualizar/<int:pk>', views.UsuarioUpdateView.as_view(), name="usuario_update"),
    path('deletar/<int:pk>/', views.UsuarioDeleteView.as_view(), name="usuario_delete"),
    path('dashboard/', views.UsuarioDashBoardView.as_view(), name='usuario_dashboard'),
]
