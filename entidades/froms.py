from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Vuelva a escribir su contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
