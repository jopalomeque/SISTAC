from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Column, Row, Submit
from django import forms
from crispy_bootstrap5.bootstrap5 import BS5Accordion


BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']

FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

class AsientosForm(forms.Form):
    CHOICES = [('1', 'Asiento 1'), ('2', 'Asiento 2')]
    Asientos = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

    Asientos_2 = forms.ChoiceField(widget=forms.CheckboxSelectMultiple, choices=CHOICES)

    asiento1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'btn-primary'}))
    asiento2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'btn-primary'}))

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'btn-primary'}))
    url = forms.URLField()
    comment = forms.CharField(widget=forms.TextInput(attrs={'size': '40'}))

    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))

    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )




STATES = (
    ('', 'Seleccione...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)

class AddressForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'size': '20'}))
    password = forms.CharField(widget=forms.PasswordInput())
    address_1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
    )
    address_2 = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'})
    )

    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)
    date_creation = forms.DateTimeField(label="Fecha de Documento", widget=forms.DateInput(format=('%Y-%m-%d'),
                                                                                     attrs={
                                                                                         'placeholder': 'Select a date',
                                                                                         'type': 'date', 'size': 30}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('email', css_class='form-group col-md-6 mb-0'),
                Column('password', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('address_1'),
                Column('address_2'),
            ),
            Row(
                Column('city', css_class='form-group col-md-6 mb-0'),
                Column('state', css_class='form-group col-md-4 mb-0'),
                Column('zip_code', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('check_me_out'),
                Column('date_creation'),
            ),
            Submit('submit', 'Sign in'),
        )
