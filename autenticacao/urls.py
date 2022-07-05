from django import views
from django.urls import path
from . import views


urlpatterns = [
    path('register/cadastro.html', views.register, name='cadastrar'),
    path('login/login.html', views.login, name='logar')
]