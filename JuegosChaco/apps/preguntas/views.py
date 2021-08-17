from django.shortcuts import render

# Create your views here.

def IniciarPreguntas(request):
    return render(request, 'productos/iniciar.html')