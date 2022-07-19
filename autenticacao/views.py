from asyncio import constants
from .utils import password_is_valid
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants


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
    try:
        user = User.objects.create_user(
            username = usuario,
            password = senha,
            is_active = False
        )
        user.save()
        messages.add_message(request, constants.SUCCESS, 'Cadastro efetuado, verifique sua caixa de email para confirmar')
        return redirect("/auth/register")

    except:
        messages.add_message(request, constants.ERROR, 'Erro do sistema')
        return redirect("/auth/register")

def login(request):
    return HttpResponse('Bem vindo, faça login')