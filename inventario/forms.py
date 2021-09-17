from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from django import forms
from .models import CategoriaProducto, Producto, CategoriaBodega, Bodega, CabeceraIngreso, DetalleIngreso


class BuscarCategoriaProductoForm(forms.Form):
    desde = forms.DateTimeField(label="Desde", required=True, widget=forms.DateInput(format=('%Y-%m-%d'),
                                                                                     attrs={
                                                                                         'placeholder': 'Select a date',
                                                                                         'type': 'date', 'size': 30}))

    hasta = forms.DateTimeField(label="Hasta", required=True, widget=forms.DateInput(format=('%Y-%m-%d'),
                                                                                     attrs={
                                                                                         'placeholder': 'Select a date',
                                                                                         'type': 'date', 'size': 30}))


class CategoriaProductoForm(forms.ModelForm):
    class Meta:
        model = CategoriaProducto
        fields = ['nombre', 'descripcion']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'class': 'form-control'})
        self.fields['descripcion'].widget.attrs.update(size='40')


class BuscarProductoForm(forms.Form):
    desde = forms.DateTimeField(label="Desde", required=True, widget=forms.DateInput(format=('%Y-%m-%d'),
                                                                                     attrs={
                                                                                         'placeholder': 'Select a date',
                                                                                         'type': 'date', 'size': 30}))

    hasta = forms.DateTimeField(label="Hasta", required=True, widget=forms.DateInput(format=('%Y-%m-%d'),
                                                                                     attrs={
                                                                                         'placeholder': 'Select a date',
                                                                                         'type': 'date', 'size': 30}))



class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo', 'nombre', 'descripcion', 'categoria_producto']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['nombre'].widget.attrs.update({'class': 'form-control'})
        # self.fields['apellido'].widget.attrs.update({'class': 'form-control'})
        self.fields['nombre'].widget.attrs.update(size='80')


class CategoriaBodegaForm(forms.ModelForm):
    class Meta:
        model = CategoriaBodega
        fields = ['nombre', 'descripcion']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'class': 'form-control'})
        self.fields['descripcion'].widget.attrs.update(size='5')
        self.helper = FormHelper(self)



class BodegaForm(forms.ModelForm):
    class Meta:
        model = Bodega
        fields = ['nombre', 'descripcion', 'categoria']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['nombre'].widget.attrs.update({'class': 'form-control'})
        # self.fields['apellido'].widget.attrs.update({'class': 'form-control'})
        self.fields['nombre'].widget.attrs.update(size='80')


class CabeceraIngresoBodegaForm(forms.ModelForm):
    class Meta:
        model = CabeceraIngreso
        fields = ['codigo_documento', 'fecha_documento', 'usuario_recibe', 'usuario_entrega', 'total_ingreso']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['nombre'].widget.attrs.update({'class': 'form-control'})
        # self.fields['apellido'].widget.attrs.update({'class': 'form-control'})
        self.fields['nombre'].widget.attrs.update(size='80')


class DetalleIngresoBodegaForm(forms.ModelForm):
    class Meta:
        model = DetalleIngreso
        fields = ['cabecera_ingreso', 'producto', 'cantidad_ingreso', 'precio_ingreso', 'sub_total']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['nombre'].widget.attrs.update({'class': 'form-control'})
        # self.fields['apellido'].widget.attrs.update({'class': 'form-control'})
        self.fields['nombre'].widget.attrs.update(size='80')
