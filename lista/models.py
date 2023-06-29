from django.db import models
from tiendas.models import Tienda
from productos.models import Producto

class Listas(models.Model):
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)
    # fecha = models.DateField()

    def __str__(self):
        return f"Lista de compras en {self.tienda.nombre} - {self.fecha}"




