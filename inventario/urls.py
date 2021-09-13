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

]
