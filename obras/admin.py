from django.contrib import admin
from .models import Libro, Noticia, Avatar
# Register your models here.

admin.site.register(Libro)
admin.site.register(Noticia)
admin.site.register(Avatar)