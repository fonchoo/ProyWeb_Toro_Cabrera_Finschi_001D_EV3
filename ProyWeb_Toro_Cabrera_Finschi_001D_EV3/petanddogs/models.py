from django.db import models

# Create your models here.

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    mail = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"