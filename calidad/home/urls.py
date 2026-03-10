from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('quienes-somos/', views.somos, name='somos'),
]
