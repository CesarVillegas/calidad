from django.shortcuts import render
from django.db.models import Prefetch, Count
from django.db import models
from .models import Banner, CategoriaIndicador, Indicador




def index(request):
    banners = Banner.objects.filter(publicado=True).order_by('orden')
    indicadores_destacados = (
        Indicador.objects
        .filter(
            publicado=True,
            destacado=True,
            categoria__publicado=True
        )
        .order_by('orden_destacado', 'id')
    )

    contexto = {
        'banners': banners,
        'indicadores_destacados': indicadores_destacados,
    }
    
    return render(request, 'home/index.html', contexto)


def somos(request):
    return render(request, 'home/quienes-somos.html')

def calidad_organizacion(request):
    return render(request, 'home/calidad_organizacion.html')

def calidad_definicion(request):
    return render(request, 'home/calidad_definicion.html')

def calidad_politica(request):
    return render(request, 'home/calidad_politica.html')

def calidad_politica(request):
    return render(request, 'home/calidad_politica.html')

def calidad_gestion(request):
    return render(request, 'home/calidad_gestion.html')

def ciclo_phva(request):
    return render(request, 'home/ciclo_phva.html')

def mecanismos_sgic(request):
    return render(request, 'home/mecanismos_sgic.html')

def formacion(request):
    return render(request, 'home/formacion.html')

def documentos(request):
    return render(request, 'home/documentos.html')


def indicadores(request):
    categorias = (
        CategoriaIndicador.objects
        .filter(publicado=True)
        .prefetch_related(
            Prefetch(
                'indicadores',
                queryset=Indicador.objects
                    .filter(publicado=True)
                    .order_by('orden', 'id')
            )
        )
        .order_by('orden', 'id')
    )



    categorias = (
        CategoriaIndicador.objects
        .filter(publicado=True)
        .annotate(
            total_indicadores=Count(
                'indicadores',
                filter=models.Q(indicadores__publicado=True)
            )
        )
        .filter(total_indicadores__gt=0) 
        .prefetch_related(
            Prefetch(
                'indicadores',
                queryset=Indicador.objects.filter(publicado=True).order_by('orden', 'id')
            )
        )
        .order_by('orden', 'id')
    )
    
    contexto = {
        'categorias': categorias
    }
    return render(request, 'home/indicadores.html', contexto)

def multimedia(request):
    return render(request, 'home/multimedia.html')
