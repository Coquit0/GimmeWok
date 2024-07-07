from django.urls import path, include
from entidades.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    #Index
    path('', home, name='home'),

    
    ###formularios###

    #Clientes

    ###Admin Clientes (Ingresar manualmente)
    path('clientesAdmin/', ClienteList.as_view(), name='clientes'),
    path('clientesUpdate/<int:pk>/', ClienteUpdate.as_view(), name='clientesupdate'),
    path('clientesDelete/<int:pk>/', ClienteDelete.as_view(), name='clientesdelete'),

    ###Clientes Clientes 
    path('clientesCreate/', ClienteCreate.as_view(), name='clientescreate'),
    path('exitoso/', exito, name='exito'),

    #pasantias
    path('empleadosAdmin/', EmpleadosList.as_view(), name='empleados'),
    path('empleadosCreateAdmin/', EmpleadosCreate.as_view(), name='empleadoscreate'),
    path('empleadosUpdateAdmin/<int:pk>/', EmpleadosUpdate.as_view(), name='empleadosupdate'),
    path('empleadosDeleteAdmin/<int:pk>/', EmpleadosDelete.as_view(), name='empleadosdelete'),
    path('exitosopasantia/', exitopasantia, name='exitopasantia'),
    path('pasantias/', registerpasantias, name='registerpasantias'), 

    ###Admin URL Comidas (Ingresar manualmente)
    path('comidasAdmin/', ComidaList.as_view(), name='comidas'),
    path('comidasCreateAdmin/', ComidaCreate.as_view(), name='comidascreate'),
    path('comidasUpdateAdmin/<int:pk>/', ComidaUpdate.as_view(), name='comidasupdate'),
    path('comidasDeleteAdmin/<int:pk>/', ComidaDelete.as_view(), name='comidasdelete'),

    ###Cliente Comidas
    path('comidascliente/', ComidaClienteList.as_view(), name='comidascliente'),
    path('buscadordecomidas/', buscadordecomidas, name='buscadordecomidas'), 
    path('encontrarcomidas/', encontrarcomidas, name='encontrarcomidas'), 
    path('comidaseleccionada/', tabladecomidas, name='tabladecomidas'),

    ###Login
    path('login/', loginEntrar, name='login'),
    path('logout/', logout_view, name='logout'),
    path('registrar/', register, name='register'),


]
