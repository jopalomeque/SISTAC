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
    path('saludo/', views.saludo, name="saludo"),
    path('ruta1/', views.miprimerfuncion, name="ruta1"),
    path('inicio/', views.inicio, name="inicio"),
    path('inicio2/', views.inicio2, name="inicio2"),

    # OPERACONES PARA CACULADORA #
    path('sumar/', views.sumar, name="sumar"),
    path('restar/', views.restar, name="restar"),

    # RUTAS PARA EL CRUD DE LA ENTIDAD CITA MEDICA#
    path('consultar_cita_medica/', views.consultar_cita_medica, name="consultar_cita_medica"),
    path('crear_cita_medica/', views.crear_cita_medica, name="crear_cita_medica"),
    path('eliminar_cita_medica/', views.eliminar_cita_medica, name="eliminar_cita_medica"),
    path('modificar_cita_medica/', views.modificar_cita_medica, name="modificar_cita_medica"),

    # RUTAS PARA EL CRUD DE LA ENTIDAD DOCTOR
    path('consultar_doctor/', views.consultar_doctor, name="consultar_doctor"),
    path('crear_doctor/', views.crear_doctor, name="crear_doctor"),
    path('eliminar_doctor/', views.eliminar_doctor, name="eliminar_doctor"),
    path('modificar_doctor/', views.modificar_doctor, name="modificar_doctor"),

    # RUTAS PARA EL CRUD DE LA ENTIDAD PERSONA#
    path('consultar_persona/', views.consultar_persona, name="consultar_persona"),
    path('crear_persona/', views.crear_persona, name="crear_persona"),
    path('eliminar_persona/<int:id>', views.eliminar_persona, name="eliminar_persona"),
    path('modificar_persona/<int:id>', views.modificar_persona, name="modificar_persona"),

]
