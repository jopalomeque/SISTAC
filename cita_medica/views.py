from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import PersonaForm, ValoresForm, SearchPersonaForm
from .models import Persona

import io
from django.http import FileResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, inch
from reportlab.pdfgen import canvas

from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from reportlab.platypus import TableStyle, Table, SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.enums import TA_JUSTIFY, TA_RIGHT, TA_CENTER, TA_LEFT


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
    if request.method == "POST":
        searchPersonaForm = SearchPersonaForm(request.POST or None)
        if searchPersonaForm.is_valid():
            cedula = searchPersonaForm.cleaned_data['cedula']
            apellido = searchPersonaForm.cleaned_data['apellido']
            personas = Persona.objects.filter(Q(cedula__icontains=cedula) | Q(apellido__icontains=apellido))
    else :
        personas = Persona.objects.all()
        searchPersonaForm = SearchPersonaForm(request.POST or None)
    return render(request, "persona/consultar_persona.html", {'personas_ls':personas, 'searchPersonaForm':searchPersonaForm})


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



@login_required(None, "", 'login')
def exportarListaPersonaPdf(request):
    # Create a file-like buffer to receive PDF data.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="lista_personas.pdf"'

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer,
                            rightMargin=inch / 4,
                            leftMargin=inch / 4,
                            topMargin=inch / 2,
                            bottomMargin=inch / 4,
                            pagesize=A4)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='RightAlign', fontName='Arial', align=TA_RIGHT))

    personas = []
    styles = getSampleStyleSheet()
    header = Paragraph("     Reporte de Personas", styles['Heading1'])
    personas.append(header)


    headings = ('Id', 'Nombre', 'Apellido', 'Edad', 'Direccion', 'Cedula', 'Correo')
    allpersonas = [(c.id, c.nombre, c.apellido, c.edad, c.direccion, c.cedula, c.correo) for c in Persona.objects.all()
]
    print
    allpersonas

    t = Table([headings] + allpersonas)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (9, -1), 1, colors.springgreen),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.springgreen),
            ('BACKGROUND', (0, 0), (-1, 0), colors.springgreen)
        ]
    ))
    personas.append(t)
    doc.build(personas)
    response.write(buffer.getvalue())
    buffer.close()
    return response

