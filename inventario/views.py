from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import CategoriaProductoForm, ProductoForm, CategoriaBodegaForm, BodegaForm, CabeceraIngresoBodegaForm, DetalleIngresoBodegaForm, BuscarxRangoFechaForm
from .models import CategoriaProducto, Producto, Bodega, CategoriaBodega, CabeceraIngreso, DetalleIngreso


# Create your views here.

#### CRUD PARA LA ENTIDAD CATEGLORIA PRODUCTO ###


@login_required(None, "", 'login')
def consultar_categoria_producto(request):
    buscarxRangoFechaForm = BuscarxRangoFechaForm()
    categorias_productos = None
    if request.method == "POST":
        buscarxRangoFechaForm=BuscarxRangoFechaForm(request.POST or None)
        if buscarxRangoFechaForm.is_valid():
            edad = buscarxRangoFechaForm.cleaned_data['edad']
            categoria = buscarxRangoFechaForm.cleaned_data['categoria_producto']
            desde = buscarxRangoFechaForm.cleaned_data['desde']
            hasta = buscarxRangoFechaForm.cleaned_data['hasta']

            categorias_productos = CategoriaProducto.objects.filter(Q(nombre__startswith=categoria) & Q(fecha_creacion__range=(desde, hasta)) & Q(edad__gt=edad))

    #else:
        #categorias_productos = CategoriaProducto.objects.all()
    return render(request, "categoria_producto/consultar_categoria_producto.html", {'categorias_productos_ls': categorias_productos, 'buscarxRangoFechaForm':buscarxRangoFechaForm})

@login_required(None, "", 'login')
def crear_categoria_producto(request):
    if request.method == "POST":
        categoriaProductoForm = CategoriaProductoForm(request.POST)
        if categoriaProductoForm.is_valid():
            categoriaProductoForm.save()
            messages.add_message(request,  messages.SUCCESS, 'Grabado exitosamente.')
            return redirect('consultar_categoria_producto')
            #return render(request, "categoria_producto/consultar_categoria_producto.html")
        else:
            categoriaProductoForm = CategoriaProductoForm()
            messages.add_message(request, messages.ERROR, 'Registro No Guardado.')
    else:
        categoriaProductoForm = CategoriaProductoForm()
    return render(request, "categoria_producto/crear_categoria_producto.html", {'categoriaProductoForm': categoriaProductoForm})

@login_required(None, "", 'login')
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

@login_required(None, "", 'login')
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
@login_required(None, "", 'login')
def consultar_producto(request):
    buscarxRangoFechaForm = BuscarxRangoFechaForm()
    prodcutos = None
    if (request.method=="POST"):
        buscarxRangoFechaForm = BuscarxRangoFechaForm(request.POST or None)
        if buscarxRangoFechaForm.is_valid():
            desde = buscarxRangoFechaForm.cleaned_data['desde']
            hasta = buscarxRangoFechaForm.cleaned_data['hasta']

            prodcutos= Producto.objects.filter(fecha_creacion__range=(desde, hasta))

    else:
        prodcutos = Producto.objects.all()
    return render(request, "producto/consultar_producto.html", {'prodcutos_ls': prodcutos, 'buscarxRangoFechaForm': buscarxRangoFechaForm})

@login_required(None, "", 'login')
def crear_producto(request):
    if request.method == "POST":
        productoForm = ProductoForm(request.POST)
        if productoForm.is_valid():
            productoForm.save()
            messages.add_message(request, messages.SUCCESS, 'Grabado exitosamente.')
            return redirect('consultar_producto')
        else:
            messages.add_message(request, messages.INFO, 'Registro No Guardado.')
            productoForm = ProductoForm()
    else:
        productoForm = ProductoForm()
    return render(request, "producto/crear_producto.html", {'productoForm': productoForm})

@login_required(None, "", 'login')
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
    return render(request, "producto/eliminar_producto.html", {'productoForm':productoForm})

@login_required(None, "", 'login')
def modificar_producto(request, id):
    if request.method == "POST":
        producto = get_object_or_404(Producto, pk=id)
        productoForm = ProductoForm(request.POST or None, instance=producto)
        if productoForm.is_valid():
            productoForm.save()
            return redirect('consultar_producto')
        else:
            productoForm = ProductoForm(instance=producto)
    else:  ##GET
        producto = get_object_or_404(Producto, pk=id)
        productoForm = ProductoForm(instance=producto)
    return render(request, "producto/modificar_producto.html", {'productoForm': productoForm})


#### CRUD PARA LA ENTIDAD CATEGLORIA BODEGA ###
@login_required(None, "", 'login')
def consultar_categoria_bodega(request):
    buscarxRangoFechaForm = BuscarxRangoFechaForm()
    categorias_bodegas = None
    if (request.method == "POST"):
        buscarxRangoFechaForm = BuscarxRangoFechaForm(request.POST or None)
        if buscarxRangoFechaForm.is_valid():
            desde = buscarxRangoFechaForm.cleaned_data['desde']
            hasta = buscarxRangoFechaForm.cleaned_data['hasta']

            categorias_bodegas = CategoriaBodega.objects.filter(fecha_creacion__range=(desde, hasta))

    else:
        categorias_bodegas = CategoriaBodega.objects.all()
    return render(request, "categoria_bodega/consultar_categoria_bodega.html", {'categorias_bodegas_ls': categorias_bodegas, 'buscarxRangoFechaForm': buscarxRangoFechaForm})

@login_required(None, "", 'login')
def crear_categoria_bodega(request):
    if request.method == "POST":
        categoriaBodegaForm = CategoriaBodegaForm(request.POST)
        if categoriaBodegaForm.is_valid():
            categoriaBodegaForm.save()
            messages.add_message(request, messages.SUCCESS, "Grabado exitosamente")
            return redirect('consultar_categoria_bodega')
        else:
            categoriaBodegaForm = CategoriaBodegaForm()
    else:
        categoriaBodegaForm = CategoriaBodegaForm()
    return render(request, "categoria_bodega/crear_categoria_bodega.html", {'categoriaBodegaForm': categoriaBodegaForm})

@login_required(None, "", 'login')
def eliminar_categoria_bodega(request, id):
    if request.method == "POST":
        categoriaBodega= get_object_or_404(CategoriaBodega, pk=id)
        categoriaBodegaForm = CategoriaBodegaForm(request.POST or None, instance=categoriaBodega)
        if categoriaBodegaForm.is_valid():
            categoriaBodega.estado = 0
            categoriaBodega.save()
            ##personaForm.
            return redirect('consultar_categoria_bodega')
    else: ##GET
        categoriaBodega = get_object_or_404(CategoriaBodega, pk=id)
        categoriaBodegaForm = CategoriaBodegaForm(instance=categoriaBodega)
    return render(request, "categoria_bodega/eliminar_categoria_bodega.html", {'categoriaBodegaForm':categoriaBodegaForm})

@login_required(None, "", 'login')
def modificar_categoria_bodega(request, id):
    if request.method == "POST":
        categoriaBodega= get_object_or_404(CategoriaBodega, pk=id)
        categoriaBodegaForm = CategoriaBodegaForm(request.POST or None, instance=categoriaBodega)
        if categoriaBodegaForm.is_valid():
            categoriaBodega.save()
            ##personaForm.
            return redirect('consultar_categoria_bodega')
    else: ##GET
        categoriaBodega = get_object_or_404(CategoriaBodega, pk=id)
        categoriaBodegaForm = CategoriaBodegaForm(instance=categoriaBodega)
    return render(request, "categoria_bodega/modificar_categoria_bodega.html", {'categoriaBodegaForm':categoriaBodegaForm})

#### CRUD PARA LA ENTIDAD  BODEGA ###
@login_required(None, "", 'login')
def consultar_bodega(request):
    buscarxRangoFechaForm = BuscarxRangoFechaForm()
    bodegas = None
    if (request.method == "POST"):
        buscarxRangoFechaForm = BuscarxRangoFechaForm(request.POST or None)
        if buscarxRangoFechaForm.is_valid():
            desde = buscarxRangoFechaForm.cleaned_data['desde']
            hasta = buscarxRangoFechaForm.cleaned_data['hasta']

            bodegas = Bodega.objects.filter(fecha_creacion__range=(desde, hasta))

    else: # GET
        bodegas = Bodega.objects.all()
    return render(request, "bodega/consultar_bodega.html", {'bodegas_ls': bodegas, 'buscarxRangoFechaForm':buscarxRangoFechaForm})

@login_required(None, "", 'login')
def crear_bodega(request):
    if request.method == "POST":
        bodegaForm = BodegaForm(request.POST)
        if bodegaForm.is_valid():
            bodegaForm.save()
            messages.add_message(request, messages.SUCCESS, "Grabado Exitosamente")
            return redirect('consultar_bodega')
        else:
            messages.add_message(request, messages.WARNING, "NO se Grabo Exitosamente")
            bodegaForm = BodegaForm()
    else:
        bodegaForm = BodegaForm()
    return render(request, "bodega/crear_bodega.html", {'bodegaForm': bodegaForm})

@login_required(None, "", 'login')
def eliminar_bodega(request, id):
    if request.method=="POST":
        bodega= get_object_or_404(Bodega, pk=id)
        bodegaForm = BodegaForm(request.POST or None, instance=bodega)
        if bodegaForm.is_valid():
            bodega.estado = 0
            bodega.save()
            messages.add_message(request, messages.SUCCESS, "Registro Eliminado Exitosamente")
            ##personaForm.
            return redirect('consultar_bodega')
    else: ##GET
        bodega = get_object_or_404(Bodega, pk=id)
        bodegaForm = BodegaForm(instance=bodega)
    return render(request, "bodega/eliminar_bodega.html", {'bodegaForm':bodegaForm})

@login_required(None, "", 'login')
def modificar_bodega(request, id):
    if request.method=="POST":
        bodega= get_object_or_404(Bodega, pk=id)
        bodegaForm = BodegaForm(request.POST or None, instance=bodega)
        if bodegaForm.is_valid():
            bodega.save()
            ##personaForm.
            return redirect('consultar_bodega')
    else: ##GET
        bodega = get_object_or_404(Bodega, pk=id)
        bodegaForm = BodegaForm(instance=bodega)
    return render(request, "bodega/modificar_bodega.html", {'bodegaForm':bodegaForm})


#### CRUD PARA LA CABECERA INGRESO A BODEGA ###
@login_required(None, "", 'login')
def consultar_ingreso_bodega(request):
    buscarxRangoFechaForm = BuscarxRangoFechaForm()
    cabeceraIngreso = None
    if (request.method == "POST"):
        buscarxRangoFechaForm = BuscarxRangoFechaForm(request.POST or None)
        if buscarxRangoFechaForm.is_valid():
            desde = buscarxRangoFechaForm.cleaned_data['desde']
            hasta = buscarxRangoFechaForm.cleaned_data['hasta']

            cabeceraIngreso = CabeceraIngreso.objects.filter(fecha_creacion__range=(desde, hasta))


    return render(request, "ingreso_bodega/consultar_ingreso_bodega.html", {'cabeceraIngreso_ls': cabeceraIngreso, 'buscarxRangoFechaForm': buscarxRangoFechaForm})

@login_required(None, "", 'login')
def crear_ingreso_bodega(request):
    if request.method == "POST":
        cabeceraIngresoBodegaForm = CabeceraIngresoBodegaForm(request.POST)
        if cabeceraIngresoBodegaForm.is_valid():
            cabeceraIngresoBodegaForm.save()
            return redirect('consultar_ingreso_bodega')
        else:
            cabeceraIngresoBodegaForm = CabeceraIngresoBodegaForm()
    else:
        cabeceraIngresoBodegaForm = CabeceraIngresoBodegaForm()
        detalleIngresoBodegaForm = DetalleIngresoBodegaForm()
    return render(request, "ingreso_bodega/crear_ingreso_bodega.html", {'cabeceraIngresoBodegaForm': cabeceraIngresoBodegaForm, 'detalleIngresoBodegaForm': detalleIngresoBodegaForm})

@login_required(None, "", 'login')
def eliminar_ingreso_bodega(request, id):
    if request.method=="POST":
        cabeceraIngreso= get_object_or_404(CabeceraIngreso, pk=id)
        cabeceraIngresoBodegaForm = CabeceraIngresoBodegaForm(request.POST or None, instance=cabeceraIngreso)
        if cabeceraIngresoBodegaForm.is_valid():
            cabeceraIngreso.estado = 0
            cabeceraIngreso.save()
            ##personaForm.
            return redirect('consultar_ingreso_bodega')
    else: ##GET
        cabeceraIngreso = get_object_or_404(CabeceraIngreso, pk=id)
        cabeceraIngresoBodegaForm = CabeceraIngresoBodegaForm(instance=cabeceraIngreso)
    return render(request, "ingreso_bodega/eliminar_ingreso_bodega.html", {'cabeceraIngresoBodegaForm':cabeceraIngresoBodegaForm})

@login_required(None, "", 'login')
def modificar_ingreso_bodega(request, id):
    if request.method=="POST":
        cabeceraIngreso= get_object_or_404(CabeceraIngreso, pk=id)
        cabeceraIngresoBodegaForm = CabeceraIngresoBodegaForm(request.POST or None, instance=cabeceraIngreso)
        if cabeceraIngresoBodegaForm.is_valid():
            cabeceraIngreso.save()
            ##personaForm.
            return redirect('consultar_ingreso_bodega')
    else: ##GET
        cabeceraIngreso = get_object_or_404(CabeceraIngreso, pk=id)
        cabeceraIngresoBodegaForm = CabeceraIngresoBodegaForm(instance=cabeceraIngreso)
    return render(request, "ingreso_bodega/modificar_ingreso_bodega.html", {'cabeceraIngresoBodegaForm':cabeceraIngresoBodegaForm})



