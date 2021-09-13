from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import CategoriaProductoForm, ProductoForm
from .models import CategoriaProducto, Producto


# Create your views here.

#### CRUD PARA LA ENTIDAD CATEGLORIA PRODUCTO ###

def consultar_categoria_producto(request):
    categorias_prodcutos = CategoriaProducto.objects.all()
    return render(request, "categoria_producto/consultar_categoria_producto.html", {'categorias_prodcutos_ls': categorias_prodcutos})


def crear_categoria_producto(request):
    if request.method == "POST":
        categoriaProductoForm = CategoriaProductoForm(request.POST)
        if categoriaProductoForm.is_valid():
            categoriaProductoForm.save()
            return redirect('consultar_categoria_producto')
        else:
            categoriaProductoForm = CategoriaProductoForm()
    else:
        categoriaProductoForm = CategoriaProductoForm()
    return render(request, "categoria_producto/crear_categoria_producto.html", {'categoriaProductoForm': categoriaProductoForm})


def eliminar_categoria_producto(request, id):
    if request.method=="POST":
        categoriaProducto= get_object_or_404(CategoriaProducto, pk=id)
        categoriaProductoForm = CategoriaProductoForm(request.POST or None, instance=categoriaProducto)
        if categoriaProductoForm.is_valid():
            categoriaProducto.estado = 0
            categoriaProducto.save()
            ##personaForm.
            return redirect('consultar_categoria_producto')
    else: ##GET
        categoriaProducto = get_object_or_404(CategoriaProducto, pk=id)
        categoriaProductoForm = CategoriaProductoForm(instance=categoriaProducto)
    return render(request, "categoria_producto/eliminar_categoria_producto.html", {'categoriaProductoForm':categoriaProductoForm})


def modificar_categoria_producto(request, id):
    if request.method == "POST":
        categoriaProducto = get_object_or_404(CategoriaProducto, pk=id)
        categoriaProductoForm = CategoriaProductoForm(request.POST or None, instance=categoriaProducto)
        if categoriaProductoForm.is_valid():
            categoriaProductoForm.save()
            return redirect('consultar_categoria_producto')
        else:
            categoriaProductoForm = CategoriaProductoForm(instance=categoriaProducto)
    else:  ##GET
        categoriaProducto = get_object_or_404(CategoriaProducto, pk=id)
        categoriaProductoForm = CategoriaProductoForm(instance=categoriaProducto)
    return render(request, "categoria_producto/modificar_categoria_producto.html", {'categoriaProductoForm': categoriaProductoForm})


#### CRUD PARA LA ENTIDAD  PRODUCTO ###

def consultar_producto(request):
    prodcutos = Producto.objects.all()
    return render(request, "producto/consultar_producto.html", {'prodcutos_ls': prodcutos})


def crear_producto(request):
    if request.method == "POST":
        productoForm = ProductoForm(request.POST)
        if productoForm.is_valid():
            productoForm.save()
            return redirect('consultar_producto')
        else:
            productoForm = ProductoForm()
    else:
        productoForm = ProductoForm()
    return render(request, "producto/crear_producto.html", {'productoForm': productoForm})


def eliminar_producto(request, id):
    if request.method=="POST":
        producto= get_object_or_404(Producto, pk=id)
        productoForm = ProductoForm(request.POST or None, instance=producto)
        if productoForm.is_valid():
            producto.estado = 0
            producto.save()
            ##personaForm.
            return redirect('consultar_producto')
    else: ##GET
        producto = get_object_or_404(Producto, pk=id)
        productoForm = ProductoForm(instance=producto)
    return render(request, "categoria_producto/eliminar_categoria_producto.html", {'productoForm':productoForm})


def modificar_producto(request, id):
    if request.method == "POST":
        producto = get_object_or_404(Producto, pk=id)
        productoForm = ProductoForm(request.POST or None, instance=producto)
        if productoForm.is_valid():
            productoForm.save()
            return redirect('consultar_producto')
        else:
            productoForm = CategoriaProductoForm(instance=producto)
    else:  ##GET
        producto = get_object_or_404(Producto, pk=id)
        productoForm = CategoriaProductoForm(instance=producto)
    return render(request, "categoria_producto/modificar_categoria_producto.html", {'productoForm': productoForm})
