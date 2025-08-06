from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

class Login(View):
    
    def get(self, request):
        if request.user.is_authenticated: 
            return redirect('/tasks/listar-tarefas/')
        return render(request, 'login/login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username + " " + password)
        user = auth.authenticate(username=username, password=password)
        print(user)
        if not user:
            print("not")
            return redirect('/auth/logar')
        else:
            auth.login(request, user)
            print("sucesso")
            return redirect('/tasks/listar-tarefas')
    


class Register(View):

    def get(self, request):
        if request.user.is_authenticated: 
            return redirect('/tasks/listar-tarefas')
        return render(request, 'register/register.html')


    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
         
        if(len(username.strip()) == 0 or len(password.strip()) == 0):
            return redirect('/auth/cadastro')
         
        user = User.objects.filter(username=username)

        if user.exists():
            return redirect('/auth/cadastro')
        
        try:
            User.objects.create_user(username=username, password=password)
            return redirect('/tasks/listar-tarefas/')
        except:
            return redirect('/auth/cadastro')
        


class LogOut(View):
    def get(self, request):
        auth.logout(request)
        return redirect('/auth/logar')







