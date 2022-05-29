from django.shortcuts import render, redirect
from django.http import HttpResponse

from listas.models import Lista
from .forms import FormLista
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio(request):
    return HttpResponse("Hola mundo")



def busqueda_lista(request):
    return render(request, "listas/busqueda_lista.html")

def buscar_lista(request):

    if request.GET['genero']:
        genero = request.GET['genero']      #almacenar el nombre 
        listas = Lista.objects.filter(genero__icontains=genero)
        return render(request, "listas/resultado_buscar.html", {"listas":listas, "genero":genero})
    else:
        respuesta="No enviaste datos."
    return HttpResponse(respuesta)


class ListaListas(LoginRequiredMixin, ListView):

    model = Lista
    template_name = "listas/leer.html"

class ListaDetalle(DetailView):

    model = Lista
    template_name = "listas/listaDetalle.html"

class ListaCreacion(CreateView):

    model = Lista
    success_url = "/listas/lista/listas"
    fields = ['titulo', 'genero', 'libros', 'posteador']

class ListaUpdate(UpdateView):

    model = Lista
    success_url = "/listas/lista/listas"
    fields = ['titulo', 'genero', 'libros', 'posteador']

class ListaDelete(DeleteView):

    model = Lista
    success_url = "/listas/lista/listas"