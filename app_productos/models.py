from django.db import models

class Categorias(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2) 
    stock = models.IntegerField()
    foto_prod = models.ImageField(upload_to='img_productoss/', blank=True, null=True)
    
    categoria = models.ForeignKey(
        Categorias,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.nombre