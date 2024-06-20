from django.db import models

# Create your models here.

class Registro(models.Model):
    email = models.EmailField(primary_key=True, unique=True, max_length=100)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    contraseña = models.CharField(max_length=128, null=False)
    activo = models.IntegerField()

    def __str__(self):
        return str(self.email)+" "+ str(self.nombre)+" "+ str(self.apellido)