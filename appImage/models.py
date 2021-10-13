from django.db import models
from inventario.models import Producto
from autenticacion.models import User

# Create your models here.
class ProductoImagen(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=25)
    imagen = models.ImageField(upload_to='img', blank=True, null=True)
    descripcion = models.CharField(max_length=255)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    usuario_creacion = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name="usuario_creacion")
    usuario_modificacion = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name="usuario_modificacion")
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = "producto_imagen"
        verbose_name = "producto_imagen"
        verbose_name_plural = "producto_imagenes"
        ordering = ['fecha_creacion']

    def __str__(self):
        return '{}'.format(self.nombre)



