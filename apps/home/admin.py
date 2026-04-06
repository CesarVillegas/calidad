from django.contrib import admin
from .models import Banner, Indicador, CategoriaIndicador

# Register your models here.
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display  = ['titulo', 'publicado', 'orden']
    list_editable = ['publicado', 'orden']
    ordering      = ['orden']


@admin.register(CategoriaIndicador)
class CategoriaIndicadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'orden', 'publicado')
    list_editable = ('orden', 'publicado')
    ordering = ('orden',)


@admin.register(Indicador)
class IndicadorAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'categoria',
        'orden',
        'destacado',
        'orden_destacado',
        'publicado'
    )

    list_editable = (
        'orden',
        'destacado',
        'orden_destacado',
        'publicado'
    )

    list_filter = ('categoria', 'destacado', 'publicado')
    search_fields = ('titulo', 'descripcion')

    ordering = ('categoria__orden', 'orden')

    fieldsets = (
        ('Contenido', {
            'fields': ('categoria', 'titulo', 'descripcion', 'subtitulo')
        }),
        ('Valor', {
            'fields': ('valor', 'sufijo')
        }),
        ('Visual', {
            'fields': ('icono',)
        }),
        ('Configuración', {
            'fields': ('orden', 'publicado')
        }),
        ('Home (Destacados)', {
            'fields': (
                'destacado',
                'orden_destacado',
                'icono_gif',
            )
        }),
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        # Si ya es destacado → exigir GIF
        if obj and obj.destacado:
            form.base_fields['icono_gif'].required = True
            form.base_fields['orden_destacado'].required = True

        return form

