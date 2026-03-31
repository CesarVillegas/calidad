from django.contrib import admin
from .models import Banner, Indicador

# Register your models here.
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display  = ['titulo', 'publicado', 'orden']
    list_editable = ['publicado', 'orden']
    ordering      = ['orden']


@admin.register(Indicador)
class IndicadorAdmin(admin.ModelAdmin):
    list_display  = ('titulo', 'valor', 'publicado', 'orden')
    list_editable = ('orden', 'publicado')
    list_filter   = ('publicado',)
    search_fields = ('titulo',)
    ordering      = ('orden',)