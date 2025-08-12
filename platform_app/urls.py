from django.urls import path 
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('nothing/', views.ListTasks.as_view(), name='task_list'),
    path('criar-tarefa/', views.TaskCreate.as_view(), name='task_create'),
    path('atualizar-tarefa/<int:id>/', views.TaskUpdate.as_view(), name='task_update'),
    path('deletar-tarefa/<int:id>/', views.TaskDelete.as_view(), name='task_delete'),
    path('completar-tarefa/<int:id>/', views.CompleteTask.as_view(), name='task_complete'),
    path('pendenciar-tarefa/<int:id>/', views.PendingTask.as_view(), name='task_pending'),
    path('listar-tarefas/', views.TesteView.as_view(), name='task_list')
]