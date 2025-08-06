from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from django.urls import reverse_lazy


class ListTasks(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'list_task/list_task.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'create_task/create_task.html'
    success_url = reverse_lazy('task_list')
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'task_update'
    success_url = reverse_lazy('task_list')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_delete'
    success_url = reverse_lazy('task_list')

    def get_queryset(self):
        return Task.objects.filter(id=self.kwargs['pk'])



class CompleteTask(LoginRequiredMixin, View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user=request.user)
        if task.status != 'C':
            task.status = 'C'
            task.save()
        return redirect('task_list')




