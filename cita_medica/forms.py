from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'edad', 'direccion', 'cedula', 'correo' ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['nombre'].widget.attrs.update({'class': 'form-control'})
        #self.fields['apellido'].widget.attrs.update({'class': 'form-control'})
        self.fields['apellido'].widget.attrs.update(size='80')


class ValoresForm(forms.Form):
    valor1 = forms.IntegerField()
    valor2 = forms.IntegerField()
    total = forms.IntegerField()

