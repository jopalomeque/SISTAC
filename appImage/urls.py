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
    Este archivo es de la aplicacion CORE del proyecto
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('crear_imagen_producto/', views.crear_imagen_producto, name="crear_imagen_producto"),
    path('modificar_imagen_producto/<int:id>', views.modificar_imagen_producto, name="modificar_imagen_producto"),
    path('eliminar_imagen_producto/<int:id>', views.eliminar_imagen_producto, name="eliminar_imagen_producto"),
    path('consulta_producto_imagenes/', views.consulta_producto_imagenes, name="consulta_producto_imagenes"),

]


