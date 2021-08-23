from django.urls import path, include
from . import views
from apps.usuario.views import RegistroUsuario

app_name = 'usuario'

urlpatterns = [
    path('', views.Perfil, name = 'perfil'),
    path('registrar/', RegistroUsuario.as_view(), name = 'registrar'),
]