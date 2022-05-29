from django.db import models
from django.contrib.auth.models import User

class Libro(models.Model):
    #def __str__(self):
     #   return f"Título: {self.titulo} - Autor: {self.autor} - descripcion: {self.descripcion} - Año: {self.año}"

    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    descripcion = models.TextField()
    año = models.IntegerField()
    portada = models.ImageField(upload_to = 'avatares', null=True)

class Noticia(models.Model):
    def __str__(self):
        return f"Título: {self.titulo} - Autor: {self.autor} - descripción: {self.descripcion} - Fecha: {self.fecha}"

    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha = models.DateField()

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to = 'avatares', null=True, blank=True)

    class Meta:
        verbose_name = "Avatar"
        verbose_name_plural = "Avatares"


    