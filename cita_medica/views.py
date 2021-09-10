from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import PersonaForm, ValoresForm
from .models import Persona


# Create your views here.

def saludo(request):
    return HttpResponse("Hola Mundo!!")


def inicio(request):
    return render(request, "inicio.html")

def inicio2(request):
    return render(request, "inicio2.html")


def miprimerfuncion(request):
    return render(request, "base.html")


### FUNCIONES PARA CALCULADORA ###
def sumar(request):
    if request.method == "POST":
        valoresform = ValoresForm(request.POST)
        if (valoresform.is_valid()):
            valor1 = valoresform.cleaned_data['valor1']
            valor2 = valoresform.cleaned_data['valor2']
            total = valor1 + valor2
            # return redirect("sumar")
    else:
        valoresform = ValoresForm()
        total = 0
    return render(request, "sumar.html", {'formulario': valoresform, 'suma': total})


### FUNCIONES PARA CALCULADORA ###
def restar(request):
    if request.method == "POST":
        valoresform = ValoresForm(request.POST)
        if (valoresform.is_valid()):
            valor1 = valoresform.cleaned_data['valor1']
            valor2 = valoresform.cleaned_data['valor2']
            total = valor1 - valor2
            # return redirect("sumar")
    else:
        valoresform = ValoresForm()
        total = 0
    return render(request, "restar.html", {'formulario': valoresform, 'resta': total})


#### CRUD PARA LA ENTIDAD CITA MEDICA ###

def consultar_cita_medica(request):
    return render(request, "cita_medica/consultar_cita_medica.html")


def crear_cita_medica(request):
    return render(request, "cita_medica/crear_cita_medica.html")


def eliminar_cita_medica(request):
    return render(request, "cita_medica/eliminar_cita_medica.html")


def modificar_cita_medica(request):
    return render(request, "cita_medica/modificar_cita_medica.html")


#### CRUD PARA LA ENTIDAD DOCTOR ###

def consultar_doctor(request):
    return render(request, "doctor/consultar_doctor.html")


def crear_doctor(request):
    return render(request, "doctor/crear_doctor.html")


def eliminar_doctor(request):
    return render(request, "doctor/eliminar_doctor.html")


def modificar_doctor(request):
    return render(request, "doctor/modificar_doctor.html")


#### CRUD PARA LA ENTIDAD PERSONA ###

def consultar_persona(request):
    personas = Persona.objects.all()
    return render(request, "persona/consultar_persona.html", {'personas_ls': personas})


def crear_persona(request):
    if request.method == "POST":
        personaForm = PersonaForm(request.POST)
        if personaForm.is_valid():
            personaForm.save()
            return redirect('consultar_persona')
        else:
            personaForm = PersonaForm()
    else:
        personaForm = PersonaForm()
    return render(request, "persona/crear_persona.html", {'personaForm': personaForm})


def eliminar_persona(request, id):
    if request.method=="POST":
        persona = get_object_or_404(Persona, pk=id)
        personaForm = PersonaForm(request.POST or None, instance=persona)
        if personaForm.is_valid():
            persona.estado = 0
            persona.save()
            ##personaForm.
            return redirect('consultar_persona')
    else: ##GET
        persona = get_object_or_404(Persona, pk=id)
        personaForm = PersonaForm(instance=persona)
    return render(request, "persona/eliminar_persona.html", {'personaForm':personaForm})


def modificar_persona(request, id):
    if request.method == "POST":
        persona = get_object_or_404(Persona, pk=id)
        personaForm = PersonaForm(request.POST or None, instance=persona)
        if personaForm.is_valid():
            personaForm.save()
            return redirect('consultar_persona')
        else:
            personaForm = PersonaForm(instance=persona)
    else:  ##GET
        persona = get_object_or_404(Persona, pk=id)
        personaForm = PersonaForm(instance=persona)
    return render(request, "persona/modificar_persona.html", {'personaForm': personaForm})
