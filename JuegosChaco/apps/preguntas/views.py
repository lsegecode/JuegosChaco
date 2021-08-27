from apps.preguntas.models import Preguntas, ElegirRespuesta, Partida, PreguntaPartida
from django.http.response import HttpResponse
from apps.categorias.models import Categoria
from django.shortcuts import render

# Create your views here.

def IniciarPreguntas(request):
    return render(request, 'preguntas/iniciar.html')

def Jugar(request):
    return render(request, 'preguntas/jugar.html', context = {
        'categorias': list(Categoria.objects.all().values_list('nombre', flat = True))
    })

def JugarCategoria(request, categoria):
    # return render(request, 'preguntas/jugar_categoria.html', context={
    #     'preguntas': Preguntas.objects.filter(categorias__nombre=categoria)
    # })
    preguntas = []
    for pregunta in Preguntas.objects.filter(categorias__nombre = categoria):
        preguntas.append({
            "consigna": pregunta.consigna,
            "opciones": [{
                "id": opcion.id,
                "pregunta": opcion.texto,
                "correcta": opcion.correcta
            } for opcion in ElegirRespuesta.objects.filter(pregunta = pregunta)]
        })
    return render(request, 'preguntas/jugar_categoria.html', context = {
        'preguntas': preguntas
    })

def SeleccionarRespuesta(request, id):
    back = request.GET.get('back', '')
    elegir_respuesta = ElegirRespuesta.objects.get(pk=id)
    pregunta = elegir_respuesta.pregunta
    # 1) ver si existe partida para esa categoria y usuario, sino crearla
    partida, _ = Partida.objects.get_or_create(
        usuario = request.user, 
        categoria = pregunta.categorias
    )
    # 0) si la respuesta ya estaba contestada (verificar en metadata) redireccionar a las preguntas
    
    pregunta_match = list(PreguntaPartida.objects.filter(partida=partida,pregunta=pregunta))
    if pregunta_match:
        return HttpResponse(f'Esta pregunta ya se contestó pruebe con otra<br><a href="{back}">Volver</a>')
    else:
        # 2) verificar si la respuesta es correcta y agregar a metadata(lista) el diccionao
        correcta = 'Correcto!!' if elegir_respuesta.correcta else 'Incorrecto!!'
        
        PreguntaPartida.objects.create(
            partida=partida,
            pregunta=pregunta,
            correcta=elegir_respuesta.correcta
        )
        return HttpResponse(f'{correcta}<br><a href="{back}">Volver</a>')
    
    