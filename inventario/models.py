from django.contrib.postgres.constraints import ExclusionConstraint
from django.contrib.postgres.fields import RangeOperators
from django.core.exceptions import ValidationError
from django.db import models
from autenticacion.models import User

# Create your models here.
class CategoriaBodega(models.Model):
    nombre = models.CharField(max_length=125)
    descripcion = models.CharField(max_length=250)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = "inv_catbodega"
        verbose_name = "categoria_bodega"
        verbose_name_plural = "categorias_bodegas"
        ordering = ['fecha_creacion']

    def __str__(self):
        return '{}'.format(self.nombre)

class Bodega(models.Model):
    nombre = models.CharField(max_length=125)
    descripcion = models.CharField(max_length=250)

    categoria = models.OneToOneField(CategoriaBodega, on_delete=models.CASCADE)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = "inv_bodega"
        verbose_name = "bodega"
        verbose_name_plural = "bodegas"
        ordering = ['fecha_creacion']

    def __str__(self):
        return '{}'.format(self.nombre)


class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=250)
    edad = models.IntegerField(blank=True, null=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = "inv_catproducto"
        verbose_name = "catproducto"
        verbose_name_plural = "catproductos"
        ordering = ['fecha_creacion']

    def __str__(self):
        return '{}'.format(self.nombre)



class Producto(models.Model):
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=250)
    categoria_producto = models.ManyToManyField(CategoriaProducto)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = "inv_producto"
        verbose_name = "producto"
        verbose_name_plural = "productos"
        ordering = ['fecha_creacion']


    def __str__(self):
        return '{}'.format(self.nombre)



class CabeceraIngreso(models.Model):
    codigo_documento = models.CharField(max_length=15)
    fecha_documento = models.DateTimeField()
    usuario_recibe = models.CharField(max_length=15)
    usuario_entrega = models.CharField(max_length=15)
    total_ingreso = models.DecimalField(max_digits=16, decimal_places=4)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = "inv_cabecera_ingreso"
        verbose_name = "cabecera_ingreso"
        verbose_name_plural = "cabecera_ingresos"
        ordering = ['fecha_creacion']

    def __str__(self):
        return '{}'.format(self.codigo_documento)


class DetalleIngreso(models.Model):
    cabecera_ingreso = models.OneToOneField(CabeceraIngreso, on_delete=models.CASCADE)
    secuencia = models.IntegerField(default=None)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_ingreso = models.IntegerField()
    precio_ingreso = models.DecimalField(max_digits=16, decimal_places=4)
    sub_total = models.DecimalField(max_digits=16, decimal_places=4)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = "inv_detalle_ingreso"
        verbose_name = "detalle_ingreso"
        verbose_name_plural = "detalle_ingresos"
        ordering = ['fecha_creacion']

    def __str__(self):
        return '{}'.format(self.cabecera_ingreso)


class BodegaProducto(models.Model):
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE, related_name="bodegas")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='productos')
    cantidad_existencia = models.IntegerField()  #STOCK
    precio_compra = models.DecimalField(max_digits=16, decimal_places=4)
    precio_venta = models.DecimalField(max_digits=16, decimal_places=4)
    stock_maximo = models.IntegerField()
    stock_minimo = models.IntegerField()

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    usuario_creacion = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="usuario_creacion_bp")
    usuario_modificacion = models.ForeignKey(User, null=True, blank=True,  on_delete=models.CASCADE,  related_name="usuario_modificacion_bp")
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = "inv_bodegaproducto"
        verbose_name = "bodegaproducto"
        verbose_name_plural = "bodegaproductos"
        ordering = ['fecha_creacion']

    def __str__(self):
        return '{}'.format(self.bodega)


class CabeceraEgreso(models.Model):
    codigo = models.CharField(max_length=15)
    fecha_entrega = models.DateTimeField(auto_now_add=True)
    bodeguero = models.ForeignKey(User, on_delete=models.CASCADE)
    recibe = models.CharField(max_length=255)
    total_egreso = models.DecimalField(max_digits=16, decimal_places=4)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    usuario_creacion = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE,
                                         related_name="usuario_creacion_cbe")
    usuario_modificacion = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE,
                                             related_name="usuario_modificacion_cbe")
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = "cabecera_egreso"
        verbose_name = "cabecera_egreso"
        verbose_name_plural = "cabeceras_egreso"
        ordering = ['fecha_entrega']

    def __str__(self):
        return '{}'.format(self.codigo)

class DetalleEgreso(models.Model):
    cabecera_egreso = models.OneToOneField(CabeceraEgreso, on_delete=models.CASCADE, related_name="cabecera_egreso")
    secuencia = models.IntegerField(default=None)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_egreso = models.IntegerField()
    precio_egreso = models.DecimalField(max_digits=16, decimal_places=4)
    total_egreso = models.DecimalField(max_digits=16, decimal_places=4)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    usuario_creacion = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE,
                                         related_name="usuario_creacion_dbe")
    usuario_modificacion = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE,
                                             related_name="usuario_modificacion_dbe")
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = "detalle_egreso"
        verbose_name = "detalle_egresos"
        verbose_name_plural = "detalles_egreso"
        ordering = ['producto']

    def __str__(self):
        return '{}{}{}()()'.format(self.cabecera_egreso.codigo, " ", self.secuencia, " ", self.producto.nombre)







