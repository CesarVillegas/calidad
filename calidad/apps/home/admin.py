from django.contrib import admin
from .models import Banner, Indicador

# Register your models here.
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display  = ['titulo', 'activo', 'orden', 'fecha_inicio', 'fecha_fin']
    list_editable = ['activo', 'orden']
    ordering      = ['orden']


@admin.register(Indicador)
class IndicadorAdmin(admin.ModelAdmin):
    list_display  = ('nombre', 'valor', 'activo', 'orden')
    list_editable = ('orden', 'activo')
    list_filter   = ('activo',)
    search_fields = ('nombre',)
    ordering      = ('orden',)