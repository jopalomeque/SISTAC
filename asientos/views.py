from django.shortcuts import render
from .forms import AsientosForm, AddressForm

# Create your views here.
def viewAsientos(request):
    if request.method == "POST":
        asientos = AsientosForm(request.POST or None)
        if asientos.is_valid():
            asiento1 = asientos.cleaned_data['asiento1']
            asiento2 = asientos.cleaned_data['asiento2']
    else:
        asientos = AsientosForm()
        addresForm = AddressForm()
    return render(request, "asientos.html", {'asientos':asientos, 'addresForm':addresForm})

