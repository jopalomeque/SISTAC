from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=100)
    edad = models.CharField(max_length=3)
    direccion = models.CharField(max_length=255)
    cedula = models.CharField(max_length=10)
    correo = models.EmailField(null=True, blank=True)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = "tr_persona"

    def __str__(self):
        return "{}{}{}".format(self.apellido, " ", self.nombre)

