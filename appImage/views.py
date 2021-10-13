from django.shortcuts import render, redirect, get_object_or_404
from autenticacion.models import User



from .forms import ProductoImagenForm
from .models import ProductoImagen
# Create your views here.
def crear_imagen_producto(request):
    if request.method == "POST":
        productoImagenForm = ProductoImagenForm(request.POST or None, request.FILES)
        if productoImagenForm.is_valid():
            productoImagen = productoImagenForm.save(commit=False)
            #user = get_object_or_404(User, username=request.user.username)
            productoImagen.usuario_creacion = request.user
            #productoImagen.usuario_modificacion = request.user
            productoImagenForm.save(commit=True)
            return redirect('consulta_producto_imagenes')
    else: #GET
        productoImagenForm = ProductoImagenForm()
    return render(request, "crear_imagen_producto.html", {'productoImagenForm':productoImagenForm})

def modificar_imagen_producto(request, id):
    if request.method == "POST":
        productoIamgen = get_object_or_404(ProductoImagen, pk=id)
        productoImagenForm = ProductoImagenForm(request.POST or None, instance=productoIamgen)
        if productoImagenForm.is_valid():
            productoImagen = productoImagenForm.save(commit=False)
            #user = get_object_or_404(User, username=request.user.username)
            #productoImagen.usuario_creacion = request.user
            productoImagen.usuario_modificacion = request.user
            productoImagenForm.save(commit=True)
            return redirect('consulta_producto_imagenes')
    else: #GET
        productoIamgen = get_object_or_404(ProductoImagen, pk=id)
        productoImagenForm = ProductoImagenForm(instance=productoIamgen, initial={'imagen': productoIamgen.imagen})
    return render(request, "modificar_imagen_producto.html", {'productoImagenForm':productoImagenForm})


def eliminar_imagen_producto(request, id):
    if request.method == "POST":
        productoIamgen = get_object_or_404(ProductoImagen, pk=id)
        productoImagenForm = ProductoImagenForm(request.POST or None, instance=productoIamgen)
        if productoImagenForm.is_valid():
            productoImagen = productoImagenForm.save(commit=False)
            #user = get_object_or_404(User, username=request.user.username)
            #productoImagen.usuario_creacion = request.user
            productoImagen.usuario_modificacion = request.user
            productoImagen.estado = 0
            productoImagenForm.save(commit=True)
            return redirect('consulta_producto_imagenes')
    else: #GET
        productoIamgen = get_object_or_404(ProductoImagen, pk=id)
        productoImagenForm = ProductoImagenForm(instance=productoIamgen, initial={'imagen': productoIamgen.imagen})
    return render(request, "eliminar_imagen_producto.html", {'productoImagenForm':productoImagenForm})


def consulta_producto_imagenes(request):
    imagenes_producto = ProductoImagen.objects.all()
    return render(request, "consulta_producto_imagenes.html", {'imagenes_producto':imagenes_producto})