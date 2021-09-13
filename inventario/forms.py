from django import forms
from .models import CategoriaProducto, Producto

class CategoriaProductoForm(forms.ModelForm):
    class Meta:
        model = CategoriaProducto
        fields = ['nombre', 'descripcion']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['nombre'].widget.attrs.update({'class': 'form-control'})
        #self.fields['apellido'].widget.attrs.update({'class': 'form-control'})
        self.fields['nombre'].widget.attrs.update(size='80')

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo', 'nombre', 'descripcion']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['nombre'].widget.attrs.update({'class': 'form-control'})
        #self.fields['apellido'].widget.attrs.update({'class': 'form-control'})
        self.fields['nombre'].widget.attrs.update(size='80')


