from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')


def somos(request):
    return render(request, 'home/quienes-somos.html')
