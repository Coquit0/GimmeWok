from django.shortcuts import render, redirect
from .models import *
from .froms import *
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request, 'index.html')

def buscadordecomidas(request):
    return render(request, 'buscadordecomidas.html',)

@login_required
def encontrarcomidas(request):
    if request.GET ["buscar"]:
        patron = request.GET["buscar"]
        comida = Comida.objects.filter(nombre__icontains=patron)
        contexto = {"comidas": comida}
    else:
        contexto = {"comidas": Comida.objects.all()}

    return render(request, 'tabladecomidas.html', contexto)

def tabladecomidas(request):
    contexto = {"comidas": Comida.objects.all()}
    return render(request, 'tabladecomidas.html', contexto)


@login_required
def pasantias(request):
    return render(request, 'registerpasantias.html')

def exito(request):
        return render(request, 'exitocompra.html')

def exitopasantia(request):
        return render(request, 'exitopasantia.html')

#Formulario
@login_required
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


#Comidas

class ComidaList(LoginRequiredMixin, ListView):
    model = Comida
    template_name="comida_list.html"

class ComidaCreate(LoginRequiredMixin, CreateView):
    model = Comida
    fields = ["nombre", "ingredientes"]
    template_name="comidaCreate.html"
    success_url = reverse_lazy("comidas")

class ComidaUpdate(LoginRequiredMixin, UpdateView):
    model = Comida
    fields = ["nombre", "ingredientes"]
    template_name="comidaUpdate.html"
    success_url = reverse_lazy("comidas")

class ComidaDelete(LoginRequiredMixin, DeleteView):
    model = Comida
    template_name="comidaDelete.html"
    success_url = reverse_lazy("comidas")

class ComidaClienteList(LoginRequiredMixin, ListView):
    model = Comida
    template_name="comidacliente_list.html"

#Clientes

class ClienteList(LoginRequiredMixin, ListView):
    model = Clientes
    template_name="cliente_list.html"

class ClienteCreate(LoginRequiredMixin ,CreateView):
    model = Clientes
    fields = ["nombre", "apellido", "direccion", "dni", "edad"]
    template_name="clienteCreate.html"
    success_url = reverse_lazy("exito")

class ClienteUpdate(LoginRequiredMixin, UpdateView):
    model = Clientes
    fields = ["nombre", "apellido", "direccion", "dni", "edad"]
    template_name="clienteUpdate.html"
    success_url = reverse_lazy("clientes")

class ClienteDelete(LoginRequiredMixin, DeleteView):
    model = Clientes
    template_name="clienteDelete.html"
    success_url = reverse_lazy("clientes")

#Pasantia

class EmpleadosList(LoginRequiredMixin, ListView):
    model = Empleados
    template_name="empleado_list.html"

class EmpleadosCreate(LoginRequiredMixin ,CreateView):
    model = Empleados
    fields = ["nombre", "apellido", "direccion", "dni", "edad", "puesto"]
    template_name="empleadoCreate.html"
    success_url = reverse_lazy("empleados")

class EmpleadosUpdate(LoginRequiredMixin, UpdateView):
    model = Empleados
    fields = ["nombre", "apellido", "direccion", "dni", "edad", "puesto"]
    template_name="empleadoUpdate.html"
    success_url = reverse_lazy("empleados")

class EmpleadosDelete(LoginRequiredMixin, DeleteView):
    model = Empleados
    template_name="empleadoDelete.html"
    success_url = reverse_lazy("empleados")



#Login

def loginEntrar(request):
    if request.method == "POST":
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            return render(request, "index.html")
        else:
            return redirect(reverse_lazy('login'))
    else:
        miForm = AuthenticationForm()
    
    return render(request, "login.html",{"form": miForm})

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            miForm.save()

            return render(request, "index.html")
        else:
            return redirect(reverse_lazy('home'))
    else:
        miForm = RegistroForm()
    
    return render(request, "register.html",{"form": miForm}) 

def logout_view(request):
    logout(request) 
    return render(request, "index.html")


        