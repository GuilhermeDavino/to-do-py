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
        return Task.objects.filter(user=self.request.user).order_by('-created_at')
    

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'create_task/create_task.html'
    success_url = reverse_lazy('task_list')
    fields = ['title', 'description']

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
        status = request.POST.get('status')
        
        task = get_object_or_404(Task, id=id, user=request.user)
        
        if(title != '' and title != task.title):
            task.title = title
        
        if(description != '' and description != task.description):
            task.description = description
        
        task.save()
        return redirect('task_list')


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
    

class PendenteTask(LoginRequiredMixin, View):
    def get(self, request, id):
        task = get_object_or_404(Task, id=id, user=request.user)
        if task.status != 'P':
            task.status = 'P'
            task.save()
        return redirect('task_list')






