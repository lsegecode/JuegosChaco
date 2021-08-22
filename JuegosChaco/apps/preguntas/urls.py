from django.urls import path, include
from . import views

app_name = 'preguntas'

urlpatterns = [
    path('', views.IniciarPreguntas, name = 'jugar'),
]