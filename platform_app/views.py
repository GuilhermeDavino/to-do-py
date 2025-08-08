from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from platform_app.forms import TaskForm
from .models import Task
from django.urls import reverse_lazy


class TesteView(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'tasks'
    create_form = TaskForm

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by('-created_at')
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_form'] = TaskForm()
        context['update_form'] = TaskForm()
        return context


class ListTasks(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'list_task/list_task.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by('-created_at')
    

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task_teste')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    
class TaskUpdate(LoginRequiredMixin, View):
    def get(self, request, id):
        task = get_object_or_404(Task, id=id, user=request.user)
        return render(request, 'update_task/update_task.html', {'task': task})

    def post(self, request, id):
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        
        task = get_object_or_404(Task, id=id, user=request.user)
        
        if(title != '' and title != task.title):
            task.title = title
        
        if(description != '' and description != task.description):
            task.description = description

        task.priority = priority

        task.save()
        return redirect('task_teste')


class TaskDelete(LoginRequiredMixin, View):
    def get(self, request, id):
        task = get_object_or_404(Task, id=id, user=request.user)
        task.delete()
        return redirect('task_teste')




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






