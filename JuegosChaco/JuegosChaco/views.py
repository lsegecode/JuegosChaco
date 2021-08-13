from django.shortcuts import render

def Home(request):

    return render(request, 'home.html')

def Pri(request):

    return render(request, 'primera.html')


def Carpincho(request): 

	return render(request, 'carpincho.html')
