from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    tiendas = models.ManyToManyField('Tienda', through='ProductoTienda')

    def __str__(self):
        return self.nombre

class ProductoTienda(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tienda = models.ForeignKey('Tienda', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.producto} - {self.tienda}"

class Tienda(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
