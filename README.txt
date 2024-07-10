Proyecto: GimmeWok

Este proyecto es una especie de parodia al local de comida de un amigo, para que en un futuro pueda hacerle la pagina pero de manera mas trabajada. 
Como no tengo muchos conocimientos de base de datos, se me complico bastante todo lo relacionado a este, por otro lado, estoy muy corto de tiempo por el tema de los finales y parciales de la facultad, 
por consecuencia no pude hacer la pagina mas estetica. Pero toda la pagina funciona y es acorde a lo pedido para la entrega.
El objetivo es que los clientes puedan comprar sus comidas desde sus casas y que las personas que quieran buscar una pasantia lo hagan con facil acceso. 

Indicaciones:

Superusuario y Contraseña:
-Coco
-password

Usuario y Contraseña (Usuario "comun"):
-Coquito
-contrase;a

Hay 4 modelos:

Clientes (Son las personas que hicieron un pedido)
Empleados (Son los empleados y pasantes del local)
Comida (Es la comida disponible)
Tareas (Las tareas para los empleados y pasantes)

1- Index: En el index tenemos todo su contenido "home" y el nav.En todas estas opciones nos pedira iniciar sesion, si no tenemos una, podemos registrarnos. En su contenido "home" tenemos la opcion de comprar una de las comidas que se presentan, este nos llevara a un formulario, que al completarlo añadira una fila a la base de datos del modelo "Cliente".
Mas abajo esta la opcion de aplicar a una pasantia, al seleccionarlo se nos presentara un formulario que debemos completar y añadira una fila a la base de datos del modelo "Empleados" con todos los datos que pusimos.

2- Nav: Todas las funcionalidades del navegador estan bloqueados para que el usuario se registre e inicie sesion en la pagina. Tenemos 8 funcionalidades en el navegador (si estamos logeados).
	1- "Inicio": con este podemos volver al Index.
	2- "Acerca de mi": en este hablo brevemente de quien soy y porque decidi entrar a este curso
	3- "Buscador de comidas": en este hay un filtro que el usuario puede usar para ver si la comida que desea esta en el menu o no.(Filtra la Tabla de Comidas)
	4- "Pasantias": al seleccionarlo se nos presentara un formulario que debemos completar y añadira una fila a la base de datos del modelo "Empleados" con todos los datos que pusimos.
	5- "Tabla de comidas": en este se puede ver la tabla de todas las comidas disponibles. (la base de datos de el modelo "Comida")
	6- "Perfil": en este el usuario podra modificar sus datos (email, nombre, apellido y la contraseña)
	7- "Avatar": en este el usuario podra modificar su avatar
	8- "Salir": en este el usuario cierra sesion

3- Tablas y funcionalidades de "Admin": El agregar, modificar y eliminar datos de la tabla, solo lo podra hacer el "dueño" de la pagina apartir de unos URL especiales (aunque cualquier usuario logueado puede acceder a dichas funciones si tiene las urls), que no estan al alcance del cliente comun. Ahora a continuacion dejare todos los links de "Admin".

###Admin Clientes (Ingresar manualmente para Admin)
    'clientesAdmin/' (Tabla de clientes)
    'clientesCreate/' (Crear datos (Los usuarios acceden al formulario))
    'clientesUpdateAdmin/<int:pk>/' (Modificar datos)
    'clientesDeleteAdmin/<int:pk>/' (Borrar datos)

###Admin Empleados y Pasantias (Ingresar manualmente para Admin)
    'empleadosAdmin/' (Tabla de Empleados y Pasantes)
    'empleadosCreateAdmin/' (Crear datos)
    'empleadosUpdateAdmin/<int:pk>/' (Modificar datos)
    'empleadosDeleteAdmin/<int:pk>/' (Borrar datos)

###Admin Comidas (Ingresar manualmente para Admin)
    'comidasAdmin/' (Tabla de Comidas)
    'comidasCreateAdmin/' (Crear datos)
    'comidasUpdateAdmin/<int:pk>/' (Modificar datos)
    'comidasDeleteAdmin/<int:pk>/' (Borrar datos)

###Tareas (Ingresar manualmente para Admin)
    'tareasAdmin/' (Tabla de Tareas)
    'tareasCreateAdmin/' (Crear datos)
    'tareasUpdateAdmin/<int:pk>/' (Modificar datos)
    'tareasDeleteAdmin/<int:pk>/' (Borrar datos)

