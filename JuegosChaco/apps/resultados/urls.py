from django.urls import path, include
from . import views

app_name = 'resultados'

urlpatterns = [
    path('', views.VerResultados, name = 'resultados.html'),
]