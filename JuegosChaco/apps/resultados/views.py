from django.shortcuts import render

# Create your views here.

def VerResultados(request):
    return render(request, 'resultados/resultados.html')