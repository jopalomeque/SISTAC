"""SisMedico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    Este archivo es de la aplicacion cita_medica
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # RUTAS PARA EL CRUD DE LA CATEOGIRA PRODUCTONA#
    path('consultar_categoria_producto/', views.consultar_categoria_producto, name="consultar_categoria_producto"),
    path('crear_categoria_producto/', views.crear_categoria_producto, name="crear_categoria_producto"),
    path('eliminar_categoria_producto/<int:id>', views.eliminar_categoria_producto, name="eliminar_categoria_producto"),
    path('modificar_categoria_producto/<int:id>', views.modificar_categoria_producto, name="modificar_categoria_producto"),

    # RUTAS PARA EL CRUD DE PRODUCTONA#
    path('consultar_producto/', views.consultar_producto, name="consultar_producto"),
    path('crear_producto/', views.crear_producto, name="crear_producto"),
    path('eliminar_producto/<int:id>', views.eliminar_producto, name="eliminar_producto"),
    path('modificar_producto/<int:id>', views.modificar_producto, name="modificar_producto"),

    # RUTAS PARA EL CRUD DE CATEGORIA BODEGA#
    path('consultar_categoria_bodega/', views.consultar_categoria_bodega, name="consultar_categoria_bodega"),
    path('crear_categoria_bodega/', views.crear_categoria_bodega, name="crear_categoria_bodega"),
    path('eliminar_categoria_bodega/<int:id>', views.eliminar_categoria_bodega, name="eliminar_categoria_bodega"),
    path('modificar_categoria_bodega/<int:id>', views.modificar_categoria_bodega, name="modificar_categoria_bodega"),

    # RUTAS PARA EL CRUD DE BODEGA#
    path('consultar_bodega/', views.consultar_bodega, name="consultar_bodega"),
    path('crear_bodega/', views.crear_bodega, name="crear_bodega"),
    path('eliminar_bodega/<int:id>', views.eliminar_bodega, name="eliminar_bodega"),
    path('modificar_bodega/<int:id>', views.modificar_bodega, name="modificar_bodega"),

    # RUTAS PARA EL CRUD DE INGRESO A BODEGA#
    path('consultar_ingreso_bodega/', views.consultar_ingreso_bodega, name="consultar_ingreso_bodega"),
    path('crear_ingreso_bodega/', views.crear_ingreso_bodega, name="crear_ingreso_bodega"),
    path('eliminar_ingreso_bodega/<int:id>', views.eliminar_ingreso_bodega, name="eliminar_ingreso_bodega"),
    path('modificar_ingreso_bodega/<int:id>', views.modificar_ingreso_bodega, name="modificar_ingreso_bodega"),

]
