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
from django.contrib.auth import views as auth_views
from autenticacion import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='registration/login.html')),
    path('crear_usuario/', views.crear_usuario, name="signup"),
    #path('profile/', auth_views.LoginView.as_view(template_name='templates/login.html')),
    #path('change-password/', auth_views.PasswordChangeView.as_view(template_name='templates/login.html')),
]

#urlpatterns = [
    # Add Django site authentication urls (for login, logout, password management)
    #^accounts/login/$ [name='login']
    #^accounts/logout/$ [name='logout']
    #^accounts/password_change/$ [name='password_change']
    #^accounts/password_change/done/$ [name='password_change_done']
    #^accounts/password_reset/$ [name='password_reset']
    #^accounts/password_reset/done/$ [name='password_reset_done']
    #^accounts/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$ [name='password_reset_confirm']
    #^accounts/reset/done/$ [name='password_reset_complete']



    #accounts/login/ [name='login']
    #accounts/logout/ [name='logout']
    #accounts/password_change/ [name='password_change']
    #accounts/password_change/done/ [name='password_change_done']
    #accounts/password_reset/ [name='password_reset']
    #accounts/password_reset/done/ [name='password_reset_done']
    #accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
    #accounts/reset/done/ [name='password_reset_complete']
#]
