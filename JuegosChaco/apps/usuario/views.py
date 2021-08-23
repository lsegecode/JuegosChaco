from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Usuario

@login_required
def Perfil(request):
    return render(request, 'usuario/perfil.html')


class RegistroUsuario(CreateView):
    model = Usuario
    template_name = 'usuario/registrar.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    