from django import views
from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='cadastrar'),
    path('login/', views.login, name='logar')
]