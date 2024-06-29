from django import forms

class ClientesForm(forms.Form):
    nombre = forms.CharField(max_length=40, required=True)
    apellido = forms.CharField(max_length=40, required=True)
    direccion = forms.CharField(max_length=50, required=True)
    dni = forms.IntegerField(required=True)
    edad = forms.IntegerField(required=True)

class EmpleadosForm(forms.Form):
    nombre = forms.CharField(max_length=40, required=True)
    apellido = forms.CharField(max_length=40, required=True)
    direccion = forms.CharField(max_length=50, required=True)
    dni = forms.IntegerField(required=True)
    edad = forms.IntegerField(required=True)
    puesto = forms.CharField(max_length=20)

class ComidasForm(forms.Form):
    nombre = forms.CharField(max_length=40, required=True)
    ingredientes = forms.CharField(max_length=100, required=True)