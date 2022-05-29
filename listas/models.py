from django.db import models

class Lista(models.Model):
    def __str__(self):
        return f"Título: {self.titulo} - Genero: {self.genero} - Libros: {self.libros} - Posteador: {self.posteador}"

    titulo = models.CharField(max_length=255)
    genero = models.CharField(max_length=255)
    libros = models.TextField()
    posteador = models.CharField(max_length=255)
