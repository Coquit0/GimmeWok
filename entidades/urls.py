from django.urls import path, include
from entidades.views import *

urlpatterns = [
    path('', home, name='home'),
    path('registerusuario/', registerusuario, name='registerusuario'),
    path('pasantias/', registerpasantias, name='registerpasantias'), 
    #formularios
    path('exitoso/', exito, name='exito'),
    path('exitosopasantia/', exitopasantia, name='exitopasantia'),
    path('adminregistercomidas/', registercomidas, name='registercomidas'),
    path('buscadordecomidas/', buscadordecomidas, name='buscadordecomidas'),
    path('tabladecomidas/', tabladecomidas, name='tabladecomidas'),
    path('encontrarcomidas/', encontrarcomidas, name='encontrarcomidas'),
]
