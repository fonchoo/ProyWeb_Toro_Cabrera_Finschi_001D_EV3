from django.db import models
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

User = get_user_model()


class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id de categoria")
    nombreCategoria=models.CharField(max_length=50, blank=True, verbose_name="Nombre de Categoria")

    def __str__(self):
        return self.nombreCategoria
    
    
class Producto(models.Model):
    id_producto              = models.CharField(primary_key=True, max_length=10)
    nombre           = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=5000)
    imagen=models.ImageField(upload_to="imagenes", null=True, blank=True, verbose_name="Imagen")
    precio=models.IntegerField(blank=True, null=True, verbose_name="Precio")
    stock = models.IntegerField(verbose_name="Stock")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoría")

    def __str__(self):
        return self.nombre 
    
class Registro(models.Model):
    email = models.EmailField(primary_key=True, unique=True, max_length=100)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    contraseña = models.CharField(max_length=128, null=False)
    activo = models.IntegerField()

    def __str__(self):
        return str(self.email)+" "+ str(self.nombre)+" "+ str(self.apellido)
    
class EmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None