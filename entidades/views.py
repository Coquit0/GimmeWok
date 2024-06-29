from django.shortcuts import render
from .models import *
from .froms import *

# Create your views here.
def home(request):
    return render(request, 'index.html')

def tabladecomidas(request):
    contexto = {"comidas": Comida.objects.all()}
    return render(request, 'tabladecomidas.html', contexto)

def buscadordecomidas(request):
    return render(request, 'buscadordecomidas.html',)



def encontrarcomidas(request):
    if request.GET ["buscar"]:
        patron = request.GET["buscar"]
        comida = Comida.objects.filter(nombre__icontains=patron)
        contexto = {"comidas": comida}
    else:
        contexto = {"comidas": Comida.objects.all()}

    return render(request, 'tabladecomidas.html', contexto)

def pasantias(request):
    return render(request, 'registerpasantias.html')

def exito(request):
        return render(request, 'exitocompra.html')

def exitopasantia(request):
        return render(request, 'exitopasantia.html')

#Formulario

def registerusuario(request):
    if request.method == "POST":
        miForm = ClientesForm(request.POST)
        if miForm.is_valid():
            cliente_nombre = miForm.cleaned_data.get("nombre")
            cliente_apellido = miForm.cleaned_data.get("apellido")
            cliente_direccion = miForm.cleaned_data.get("direccion")
            cliente_dni = miForm.cleaned_data.get("dni")
            cliente_edad = miForm.cleaned_data.get("edad")
            cliente = Clientes(nombre=cliente_nombre, apellido=cliente_apellido, direccion=cliente_direccion, dni=cliente_dni, edad=cliente_edad)
            cliente.save()
            return render(request, 'exitocompra.html')
    else:
        miForm = ClientesForm()

    return render(request, "registerusuario.html", {"form": miForm})

def registerpasantias(request):
    if request.method == "POST":
        miForm = EmpleadosForm(request.POST)
        if miForm.is_valid():
            pasante_nombre = miForm.cleaned_data.get("nombre")
            pasante_apellido = miForm.cleaned_data.get("apellido")
            pasante_direccion = miForm.cleaned_data.get("direccion")
            pasante_dni = miForm.cleaned_data.get("dni")
            pasante_edad = miForm.cleaned_data.get("edad")
            pasante_puesto = miForm.cleaned_data.get("puesto")
            pasante = Empleados(nombre=pasante_nombre, apellido=pasante_apellido, direccion=pasante_direccion, dni=pasante_dni, edad=pasante_edad, puesto=pasante_puesto)
            pasante.save()
            return render(request, 'exitopasantia.html')
    else:
        miForm = EmpleadosForm()

    return render(request, "registerpasantias.html", {"form": miForm})

def registercomidas(request):
    if request.method == "POST":
        miForm = ComidasForm(request.POST)
        if miForm.is_valid():
            comida_nombre = miForm.cleaned_data.get("nombre")
            comida_ingredientes = miForm.cleaned_data.get("ingredientes")
            comida = Comida(nombre=comida_nombre, ingredientes=comida_ingredientes)
            comida.save()
            return render(request, 'index.html')
    else:
        miForm = ComidasForm()

    return render(request, "registercomida.html", {"form": miForm})



        