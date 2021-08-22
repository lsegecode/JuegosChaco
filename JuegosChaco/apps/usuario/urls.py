from django.urls import path, include
from . import views

app_name = 'usuario'

urlpatterns = [
    path('', views.Perfil, name = 'perfil'),
]