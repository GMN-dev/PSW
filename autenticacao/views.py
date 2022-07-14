from .utils import password_is_valid
from django.shortcuts import redirect, render
from django.http import HttpResponse


# Create your views here.
def register(request):
    if request.method == 'GET': 
        return render(request, 'register.html')
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('password')
        confSenha = request.POST.get('confirm_password')
        if not password_is_valid(request, senha, confSenha):
            return redirect("/auth/register")
        return HttpResponse(f'Seja bem vindo {usuario}')
        
        
def login(request):
    return HttpResponse('Bem vindo, faça login')