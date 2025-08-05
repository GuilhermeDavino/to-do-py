from django.urls import path 
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('listar-tarefas/', views.ListTasks.as_view(), name='task_list'),
    path('criar-tarefa/', views.TaskCreate.as_view(), name='task_create'),
    path('atualizar-tarefa/<int:pk>/', views.TaskUpdate.as_view(), name='task_update'),
    path('deletar-tarefa/<int:pk>/', views.TaskDelete.as_view(), name='task_delete'),
    path('completar-tarefa/<int:pk>/', views.CompleteTask.as_view(), name='task-complete'),
]