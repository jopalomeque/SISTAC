from django.db import models

# Create your models here.
class CategoriaBodega(models.Model):
    nombre = models.CharField(max_length=125)
    descripcion = models.CharField(max_length=250)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    estado = models.IntegerField()

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

    categoria = models.ForeignKey(CategoriaBodega, on_delete=models.CASCADE)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    estado = models.IntegerField()

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

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    estado = models.IntegerField()

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

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    estado = models.IntegerField()

    class Meta:
        db_table = "inv_producto"
        verbose_name = "producto"
        verbose_name_plural = "productos"
        ordering = ['fecha_creacion']

    def __str__(self):
        return '{}'.format(self.nombre)


class BodegaProducto(models.Model):
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_existencia = models.IntegerField()  #STOCK
    precio_compra = models.DecimalField(max_digits=16, decimal_places=4)
    precio_venta = models.DecimalField(max_digits=16, decimal_places=4)
    stock_maximo = models.IntegerField()
    stock_minimo = models.IntegerField()

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    estado = models.IntegerField()

    class Meta:
        db_table = "inv_bodegaproducto"
        verbose_name = "bodegaproducto"
        verbose_name_plural = "bodegaproductos"
        ordering = ['fecha_creacion']

    def __str__(self):
        return '{}'.format(self.bodega)



