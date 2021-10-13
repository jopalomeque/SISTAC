from django.contrib import admin
from .models import RolUsuario, Rol, User
# Register your models here.
admin.site.register(Rol)
admin.site.register(RolUsuario)
admin.site.register(User)
