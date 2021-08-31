from apps.preguntas.models import Preguntas, ElegirRespuesta, Partida, PreguntaPartida
from django.http.response import HttpResponse, HttpResponseRedirect
from apps.categorias.models import Categoria
from django.shortcuts import redirect, render

# Create your views here.

def IniciarPreguntas(request):
    return render(request, 'preguntas/iniciar.html')

def Jugar(request):
    return render(request, 'preguntas/jugar.html', context = {
        'categorias': list(Categoria.objects.all().values_list('nombre', flat = True))
    })



def JugarCategoria(request, nombre_categoria):
    from random import randint
    preguntas_vista = []

    partida, _ = Partida.objects.get_or_create(
        usuario = request.user, 
        categoria=Categoria.objects.get(nombre=nombre_categoria) 
    )
    preguntas_categoria = list(Preguntas.objects.filter(categorias__nombre = nombre_categoria).exclude(
        id__in=[x.pregunta.id for x in PreguntaPartida.objects.filter(partida=partida)] #preguntas_contestadas
    ))
    if preguntas_categoria:
        pregunta = preguntas_categoria[randint(0,len(preguntas_categoria) -1 )]
        preguntas_vista.append({
            "consigna": pregunta.consigna,
            "opciones": [{
                "id": opcion.id,
                "pregunta": opcion.texto,
                "correcta": opcion.correcta
            } for opcion in ElegirRespuesta.objects.filter(pregunta = pregunta)]
        })
    return render(request, 'preguntas/jugar_categoria.html', context = {
        'preguntas': preguntas_vista,
        'todas_respondidas': len(preguntas_categoria) == 0,
        'preguntas_categoria':len(preguntas_categoria)
    })

def SeleccionarRespuesta(request, id):
    context = {
        'back':request.GET.get('back', '')
    }
    elegir_respuesta = ElegirRespuesta.objects.get(pk=id)
    pregunta = elegir_respuesta.pregunta
    # 1) ver si existe partida para esa categoria y usuario, sino crearla
    partida, _ = Partida.objects.get_or_create(
        usuario = request.user, 
        categoria = pregunta.categorias
    )
    PreguntaPartida.objects.create(
        partida=partida,
        pregunta=pregunta,
        correcta=elegir_respuesta.correcta
    )
    view = 'resultados/correcta.html' if elegir_respuesta.correcta else 'resultados/incorrecta.html'
    
    
    return render(request, view, context=context)

 

    
    