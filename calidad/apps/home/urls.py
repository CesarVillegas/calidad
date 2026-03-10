from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('quienes-somos/', views.somos, name='somos'),

    path('calidad/organizacion/', views.calidad_organizacion, name='calidad_organizacion'),
    path('calidad/definicion/', views.calidad_definicion, name='calidad_definicion'),
    path('calidad/politica/', views.calidad_politica, name='calidad_politica'),
    path('calidad/ciclo-phva/', views.ciclo_phva, name='ciclo_phva'),
    path('calidad/mecanismos-sgic/', views.mecanismos_sgic, name='mecanismos_sgic'),

    path('formacion/', views.formacion, name='formacion'),
    path('documentos/', views.documentos, name='documentos'),
    path('multimedia/', views.multimedia, name='multimedia'),
]
