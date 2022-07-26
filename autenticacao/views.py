from .utils import password_is_valid
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth


# Create your views here.
def register(request):
    # Verifica o tipo de método da requisição 
    # Caso o método for Get
    if request.method == 'GET':
        # verificando se o usuário ja esta autenticado antes para não precisar fazer cadastro
        if request.user.is_authenticated:
            return redirect('/')
        # Retornando a página de cadastro 
        return render(request, 'register.html')

    # Caso o método for Post
    if request.method == 'POST':

        # Coletando informções do Form
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('password')
        confSenha = request.POST.get('confirm_password')

        # Verificando se a senha corresponde aos padrões estabelecidos
        # função password_is_valid esta dentro de utils.py
        if not password_is_valid(request, senha, confSenha):
            # se a senha não corresponder aos padrões, retorna a página com a mensagem específica
            return redirect("/auth/register")

    # se a senha estiver correspondendo, tentar criar objeto no banco de dados
    try:
        user = User.objects.create_user(
            username = usuario,
            password = senha,
            is_active = False
        )
        # salvando alteraçoes no banco
        user.save()

        # informando ao usuário para ativar a conta por meio da caixa de email
        messages.add_message(request, constants.SUCCESS, 'Cadastro efetuado, verifique sua caixa de email para confirmar')
        return redirect("/auth/register")

    except:
        # caso algum erro para criar o objeto, infomando erro do sistema
        messages.add_message(request, constants.ERROR, 'Erro do sistema')
        return redirect("/auth/register")



def login(request):
    # Verifica o tipo de método da requisição 
    # Caso o método for Get
    if request.method == 'GET':
        # verificando se o usuário ja esta autenticado antes para não precisar fazer cadastro
        if request.user.is_authenticated:
            return redirect('/')
            
        # Retorna a página de login
        return render(request, 'login.html')
    
    # Caso o método for Post
    elif request.method == 'POST':
        # coleta dados do form
        username = request.POST.get('usuario')
        password = request.POST.get('senha')

        # coloca dentro de uma variável se o usuário tem registro dentro do banco
        # essa função verifica se o usuario existe no banco 
        loginUser = auth.authenticate(username=username, password=password)

        # se não existir o usuário
        if not (loginUser):
            # retorna a página com a mensagem de erro 
            messages.add_message(request, constants.ERROR, 'Verifique nome de usuário e senha, algo está errado')
            return redirect('/auth/login')

        # se existir
        else:
            # essa função autentica o usuario quando retornado da função auth.authenticate
            auth.login(request, loginUser)
            return redirect('/')
