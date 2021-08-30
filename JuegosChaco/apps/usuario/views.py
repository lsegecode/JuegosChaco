from apps.preguntas.models import PreguntaPartida
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Usuario
from .forms import SignUpForm


@login_required
def Perfil(request):
    preguntas_respondidas = list(PreguntaPartida.objects.filter(partida__usuario=request.user))
    total = len(preguntas_respondidas)
    correctas = len([p for p in preguntas_respondidas if p.correcta])
    incorrectas = len([p for p in preguntas_respondidas if not p.correcta])
    return render(request, 'usuario/perfil.html', context={
        'total': total,
        'correctas':correctas,
        'incorrectas': incorrectas,
    })

def Ranking(request):
    ranking = []
    for usuario in Usuario.objects.all():
        correctas = len([p for p in list(PreguntaPartida.objects.filter(partida__usuario=usuario)) if p.correcta])
        ranking.append({'username':usuario.username, 'correctas': correctas})
    ranking = sorted(ranking, key=lambda x: x['correctas'], reverse=True)[:10]
    return render(request, 'usuario/ranking.html', context={
        'ranking': ranking
    })

class RegistroUsuario(CreateView):
    model = Usuario
    template_name = 'usuario/registrar.html'
    form_class = SignUpForm
    success_url = reverse_lazy('home')