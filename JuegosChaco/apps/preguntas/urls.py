from django.urls import path, include
from . import views

app_name = 'preguntas'

urlpatterns = [
    path('categoria/<str:categoria>/', views.JugarCategoria, name = 'jugar_categoria'),
    path('', views.IniciarPreguntas, name = 'jugar'),
    path('iniciar/', views.Jugar, name = 'iniciar'),
    path('seleccionar_respuesta/<int:id>', views.SeleccionarRespuesta, name = 'seleccionar_respuesta'),
]