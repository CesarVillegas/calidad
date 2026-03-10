from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def somos(request):
    return render(request, 'home/quienes-somos.html')

def calidad_organizacion(request):
    return render(request, 'home/calidad_organizacion.html')

def calidad_definicion(request):
    return render(request, 'home/calidad_definicion.html')

def calidad_politica(request):
    return render(request, 'home/calidad_politica.html')

def ciclo_phva(request):
    return render(request, 'home/ciclo_phva.html')

def mecanismos_sgic(request):
    return render(request, 'home/mecanismos_sgic.html')

def formacion(request):
    return render(request, 'home/formacion.html')

def documentos(request):
    return render(request, 'home/documentos.html')

def multimedia(request):
    return render(request, 'home/multimedia.html')
