from django.db import models

# Create your models here.

class Tienda(models.Model):
    nombre = models.CharField(max_length=100)
    # direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
