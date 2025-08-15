from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from platform_app.forms import TaskForm
from platform_app.forms import TaskUpdateForm, UsuarioUpdateForm
from usuario.models import Usuario
from .models import Task
from django.urls import reverse_lazy


class ListTasksView(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'tasks'
    create_form = TaskForm
    update_form = TaskUpdateForm

    def get_queryset(self):
        hoje = timezone.now().date()
        qs = Task.objects.filter(user=self.request.user).order_by('-created_at')

        for task in qs:
            if task.deadline < hoje and task.status != 'C' and task.status != 'A':
                task.status = 'A'
                task.save() 
        return qs
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = context['tasks']
        tasks_forms = []
        for task in tasks:
            form = TaskUpdateForm(instance=task)
            tasks_forms.append((task, form))
        context['tasks_forms'] = tasks_forms
        context['create_form'] = TaskForm()
        context['update_form'] = TaskUpdateForm()
        context['usuario'] = self.request.user
        return context


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskUpdateForm
    success_url = reverse_lazy('task_list')


class TaskDelete(LoginRequiredMixin, View):
    def get(self, request, id):
        task = get_object_or_404(Task, id=id, user=request.user)
        task.delete()
        return redirect('task_list')




class CompleteTask(LoginRequiredMixin, View):
    def get(self, request, id):
        task = get_object_or_404(Task, id=id, user=request.user)
        if task.status != 'C':
            task.status = 'C'
            task.save()
        return redirect('task_list')
    

class PendingTask(LoginRequiredMixin, View):
    def get(self, request, id):
        task = get_object_or_404(Task, id=id, user=request.user)
        if task.status != 'P':
            task.status = 'P'
            task.save()
        return redirect('task_list')


class PerfilView(LoginRequiredMixin, UpdateView):
    model = Usuario
    form_class = UsuarioUpdateForm
    template_name = 'perfil.html'
    success_url = reverse_lazy('perfil')

    def get_object(self, queryset=None):
        return self.request.user

def LogadoView(request):
    return HttpResponse(request.user.id)


class TaskDetailJsonView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user=request.user)
        data = {
            'title': task.title,
            'description': task.description,
            'status': task.status,
            'priority': task.priority,
            'category': task.category,
            'deadline': task.deadline.strftime('%Y-%m-%d'),
        }
        return JsonResponse(data)




