from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    tiendas = models.ManyToManyField('productos.Tienda')

    def __str__(self):
        return self.nombre


class Tienda(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre




