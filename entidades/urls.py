from django.urls import path, include
from entidades.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    #Index y Acerca de mi
    path('', home, name='home'),
    path('acercademi/', acercademi, name='acercademi'),

    
    ###formularios###

    ###Admin Clientes (Ingresar manualmente para Admin)
    path('clientesAdmin/', ClienteList.as_view(), name='clientes'),
    path('clientesUpdateAdmin/<int:pk>/', ClienteUpdate.as_view(), name='clientesupdate'),
    path('clientesDeleteAdmin/<int:pk>/', ClienteDelete.as_view(), name='clientesdelete'),

    ###Clientes (Para usuarios) 
    path('clientesCreate/', ClienteCreate.as_view(), name='clientescreate'),
    path('exitoso/', exito, name='exito'),

    #Admin Empleados y Pasantias (Ingresar manualmente para Admin)
    path('empleadosAdmin/', EmpleadosList.as_view(), name='empleados'),
    path('empleadosCreateAdmin/', EmpleadosCreate.as_view(), name='empleadoscreate'),
    path('empleadosUpdateAdmin/<int:pk>/', EmpleadosUpdate.as_view(), name='empleadosupdate'),
    path('empleadosDeleteAdmin/<int:pk>/', EmpleadosDelete.as_view(), name='empleadosdelete'),
    path('exitosopasantia/', exitopasantia, name='exitopasantia'),

    ###Pasantias (Para usuarios) 
    path('pasantias/', registerpasantias, name='registerpasantias'), 

    ###Admin Comidas (Ingresar manualmente para Admin)
    path('comidasAdmin/', ComidaList.as_view(), name='comidas'),
    path('comidasCreateAdmin/', ComidaCreate.as_view(), name='comidascreate'),
    path('comidasUpdateAdmin/<int:pk>/', ComidaUpdate.as_view(), name='comidasupdate'),
    path('comidasDeleteAdmin/<int:pk>/', ComidaDelete.as_view(), name='comidasdelete'),

    ###Cliente Comidas (Para usuarios)
    path('comidascliente/', ComidaClienteList.as_view(), name='comidascliente'),
    path('buscadordecomidas/', buscadordecomidas, name='buscadordecomidas'), 
    path('encontrarcomidas/', encontrarcomidas, name='encontrarcomidas'), 
    path('comidaseleccionada/', tabladecomidas, name='tabladecomidas'),

    ###Tareas (Ingresar manualmente para Admin)
    path('tareasAdmin/', TareasList.as_view(), name='tareas'),
    path('tareasCreateAdmin/', TareasCreate.as_view(), name='tareascreate'),
    path('tareasUpdateAdmin/<int:pk>/', TareasUpdate.as_view(), name='tareasupdate'),
    path('tareasDeleteAdmin/<int:pk>/', TareasDelete.as_view(), name='tareasdelete'),

    ###Login (Para usuarios) 
    path('login/', loginEntrar, name='login'),
    path('logout/', logout_view, name='logout'),
    path('registrar/', register, name='register'),
    path('perfil/', editarPerfil, name='editarperfil'),
    path('<int:pk>/password/', CambiarClave.as_view(), name='cambiarclave'),
    path('avatar/', agregarAvatar, name='agregaravatar'),



]
