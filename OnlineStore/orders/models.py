import email
from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre del Cliente") # Verbose es para cambiar la vista del nombre en el panel de Admin
    direccion = models.CharField(max_length=50, blank=True, null=True) # Permite dejar en blanco al agregar nuevo en el panel de Admin
    email = models.EmailField(verbose_name='Correo')
    tfno = models.CharField(max_length=7, verbose_name='Teléfono')

class Articulos(models.Model):
    nombre = models.CharField(max_length=30, verbose_name='Articulo')
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()

    # def __str__(self):    # Para cambiar el formato de la vista en el panel admin
    #     return f'Nombre: {self.nombre} | Seccion: {self.seccion} | Precio: {self.precio}'

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()