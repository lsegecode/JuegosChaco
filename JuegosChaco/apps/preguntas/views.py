from apps.preguntas.models import Preguntas, ElegirRespuesta
from django.http.response import HttpResponse
from apps.categorias.models import Categoria
from django.shortcuts import render

# Create your views here.

def IniciarPreguntas(request):
    return render(request, 'preguntas/iniciar.html')

def Jugar(request):
    return render(request, 'preguntas/jugar.html', context={
        'categorias': list(Categoria.objects.all().values_list('nombre', flat=True))
    })

def JugarCategoria(request, categoria):
    # return render(request, 'preguntas/jugar_categoria.html', context={
    #     'preguntas': Preguntas.objects.filter(categorias__nombre=categoria)
    # })
    preguntas = []
    for pregunta in Preguntas.objects.filter(categorias__nombre=categoria):
        preguntas.append({
            "consigna": pregunta.consigna,
            "opciones": [{
                "id": opcion.id,
                "pregunta": opcion.texto,
                "correcta": opcion.correcta
            } for opcion in ElegirRespuesta.objects.filter(pregunta=pregunta)]
        })
    return render(request, 'preguntas/jugar_categoria.html', context={
        'preguntas': preguntas
    })

def SeleccionarRespuesta(request, id):
    back = request.GET.get('back', '')
    correcta = 'Correcto!!' if ElegirRespuesta.objects.get(pk=id).correcta else 'Incorrecto!!'
    return HttpResponse(f'{correcta}<br><a href="{back}">Volver</a>')