from django.shortcuts import render

def Home(request):
    return render(request, 'home.html')

def Pri(request):
    return render(request, 'primera.html')

def Usuario(request):
    return render(request, 'usuario.html')