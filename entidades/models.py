from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    direccion = models.CharField(max_length=50)
    dni = models.IntegerField()
    edad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Empleados(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    direccion = models.CharField(max_length=50)
    dni = models.IntegerField()
    edad = models.IntegerField()
    puesto = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Comida(models.Model):
    nombre = models.CharField(max_length=40)
    ingredientes = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre}"
    
class Tareas(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.nombre}"

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"
    
    
