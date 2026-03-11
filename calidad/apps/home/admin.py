from django.contrib import admin
from .models import Banner

# Register your models here.
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display  = ['titulo', 'activo', 'orden', 'fecha_inicio', 'fecha_fin']
    list_editable = ['activo', 'orden']
    ordering      = ['orden']