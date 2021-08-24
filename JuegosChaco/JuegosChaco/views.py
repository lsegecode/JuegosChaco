from django.shortcuts import render

def Home(request):
    return render(request, 'home.html')

def Usuario(request):
    return render(request, 'usuario.html')

def Nosotros(request):
	return render(request, 'nosotros/nosotros.html')