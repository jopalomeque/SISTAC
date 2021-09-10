from django.db import models

# Create your models here.
class Pais(models.Model):
    nombre = models.CharField(max_length=100)
    localidad = models.CharField(max_length=100)
    numero_habitantes = models.IntegerField()

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = "co_pais"
        verbose_name = "Pais"
        verbose_name_plural = "Paises"

    def __str__(self):
        return "{}".format(self.nombre)

class Provincia(models.Model):
    INSULAR = "AM"
    SIERRA = "EU"
    ORIENTE = "AS"
    COSTA = "AF"

    REGIONES = [(INSULAR,"INSULAR"), (SIERRA, "SIERRA") , (ORIENTE, "ORIENTE") , (COSTA, "COSTA")]

    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    numero_habitantes = models.IntegerField()
    zona_region = models.CharField(max_length=50, choices=REGIONES, default=COSTA)
    limites = models.CharField(max_length=200)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table="co_provincia"
        verbose_name = "Provincia"
        verbose_name_plural = "Provincias"

    def __str__(self):
        return "{}".format(self.nombre)

class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)
    numero_habitantes = models.IntegerField()

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)

    class Meta:
        db_table = "co_ciudad"
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"

    def __str__(self):
        return "{}".format(self.nombre)






