from django.contrib import admin
from .models import Ciudad, Pais, Provincia

# Register your models here.
admin.site.register(Ciudad)
admin.site.register(Pais)
admin.site.register(Provincia)