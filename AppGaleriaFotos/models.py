from django.db import models

class Imagen(models.Model):
    nombre = models.CharField(max_length=255)
    archivo = models.ImageField(upload_to='imagenes/')
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre