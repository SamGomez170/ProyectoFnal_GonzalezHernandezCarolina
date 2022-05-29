from django.shortcuts import render, redirect
from django.http import HttpResponse

from obras.models import Libro, Noticia, Avatar
from .forms import FormLibro, FormNoticia, RegistroFormulario, AvatarFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

#Vista para registrarse
def register(request):
    if request.method == 'POST':    #cuando le haga click al botón
        form = RegistroFormulario(request.POST)   #leer los datos   llenados en el formulario
        if form.is_valid():
            user=form.cleaned_data['username']
            form.save()
            return render(request, "obras/Autenticar/inicio.html", {'mensaje':"Usuario Creado"})
    else:
        form = RegistroFormulario()   #formulario de django que nos permite crear usuarios.
    return render(request, "obras/Autenticar/registro.html", {'form':form})

def agregarImagen(request):
    if request.method == 'POST':
        miFormulario=AvatarFormulario(request.POST, request.FILES)
        if miFormulario.is_valid():
             informacion = miFormulario.cleaned_data
             avatar = Avatar(user=request.user, imagen=informacion['imagen'])
             avatar.save()
             return render(request, 'obras/Autenticar/inicio.html')
    else:
        miFormulario=AvatarFormulario()
    return render(request, 'obras/agregarImagen.html', {'form':miFormulario})


#Vista para iniciar sesión
def login_request(request):

    if request.method == 'POST': #al presionar el botón "Iniciar Sesión"

        form = AuthenticationForm(request, data = request.POST) #leer la data del formulario de inicio de sesión

        if form.is_valid():
            
            usuario=form.cleaned_data.get('username')   #leer el usuario ingresado
            contra=form.cleaned_data.get('password')    #leer la contraseña ingresada

            user=authenticate(username=usuario, password=contra)    #buscar al usuario con los datos ingresados

            if user:    #si ha encontrado un usuario con eso datos

                login(request, user)   #hacemos login

                #mostramos la página de inicio con un mensaje de bienvenida.
                return render(request, "obras/Autenticar/inicio.html", {'mensaje':f"Bienvenido {user}"}) 

        else:   #si el formulario no es valido (no encuentra usuario)

            #mostramos la página de inicio junto a un mensaje de error.
    
            return render(request, "obras/Autenticar/inicio.html", {'mensaje':"Error. Datos incorrectos"})

    else:
            
        form = AuthenticationForm() #mostrar el formulario

    return render(request, "obras/Autenticar/login.html", {'form':form})    #vincular la vista con la plantilla de html
    

def editarUsuario(request):
    usuario = request.user #usuario activo (el que ha iniciado sesión)
    if request.method == "POST":    #al presionar el botón
        miFormulario = RegistroFormulario(request.POST) #el formulario es el del usuario
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data     #info en modo diccionario
            #actualizar la info del usuario activo
            usuario.username = informacion['username']
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password1']

            usuario.save()
            return render(request, "obras/Autenticar/inicio.html")
    else:
        miFormulario= RegistroFormulario(initial={'username':usuario.username, 'email':usuario.email})
    return render(request, "obras/Autenticar/editarUsuario.html",{'miFormulario':miFormulario, 'usuario':usuario.username})


def inicio(request):
    return render(request, 'obras/Autenticar/inicio.html')


#Noticias 
class ListaNoticias(LoginRequiredMixin, ListView):

    model = Noticia
    template_name = "obras/leerNoticias.html"

class NoticiaDetalle(DetailView):

    model = Noticia
    template_name = "obras/noticiaDetalle.html"

class NoticiaCreacion(CreateView):

    model = Noticia
    success_url = "/obras/noticias/lista"
    fields = ['titulo', 'autor', 'descripcion', 'fecha']

class NoticiaUpdate(UpdateView):

    model = Noticia
    success_url = "/obras/noticias/lista"
    fields = ['titulo', 'autor', 'descripcion', 'fecha']

class NoticiaDelete(DeleteView):

    model = Noticia
    success_url = "/obras/noticias/lista"

def busqueda_titulo(request):
    return render(request, "obras/busqueda_titulo.html")

def buscar_noticia(request):

    if request.GET['titulo']:
        titulo = request.GET['titulo']      #almacenar el nombre 
        noticias = Noticia.objects.filter(titulo__icontains=titulo)
        return render(request, "obras/resultados_busqueda_noticia.html", {"noticias":noticias, "titulo":titulo})
    else:
        respuesta="No enviaste datos."
    return HttpResponse(respuesta)

#Libros 
def lista_libros(request):

    libros = Libro.objects.all() #almacenamos todos los libros registrados en la base de datos
    contexto = {"libros":libros}
    return render(request, "obras/Libros/leerLibros.html",contexto)

def ver_libro(request, id):
    libro = Libro.objects.get(id=id)
    return render(request, "obras/Libros/libroDetalle.html", {"libro": libro})


def editar_libro(request, id):
    libro = Libro.objects.get(id=id)
    if request.method == "POST":
        mi_form = FormLibro(request.POST, request.FILES)
        if mi_form.is_valid():
            info = mi_form.cleaned_data
            libro.titulo = info["titulo"]
            libro.autor = info["autor"]
            libro.descripcion = info["descripcion"]
            libro.año = info["año"]
            libro.portada = info["portada"]
            libro.save()
            return redirect("lista_libros")
    else:

        mi_form= FormLibro(initial={'titulo':libro.titulo, 'autor':libro.autor, 
        'portada':libro.portada})
    return render(request, "obras/Libros/formLibros.html",{'mi_form':mi_form})

def nuevo_libro(request):
    if request.method == "POST":
       # libro = Libro.objects.get(id=id)
        mi_form = FormLibro(request.POST, request.FILES)
        if mi_form.is_valid():
            info = mi_form.cleaned_data
            libro = Libro(
                titulo=info["titulo"],
                autor=info["autor"],
                descripcion=info["descripcion"],
                año=info["año"],
                portada=info["portada"],
            )
            libro.save()
            #return render(request, 'obras/inicio.html')
            return redirect("lista_libros")
    else:
        mi_form=FormLibro()
    return render(request, "obras/Libros/nuevoLibro.html", {"form": mi_form})

def borrar_libro(request, id):
    
    libro = Libro.objects.get(id=id)
    libro.delete()
    libros = Libro.objects.all()
    contexto={"libros":libros}
    return render(request, "obras/Libros/leerLibros.html",contexto)

def busqueda_autor(request):
    return render(request, "obras/Libros/busqueda_autor.html")

def buscar_libro(request):
    if request.GET['autor']:
        autor = request.GET['autor']      #almacenar el nombre autor
        libros = Libro.objects.filter(autor__iexact=autor)
        return render(request, "obras/Libros/resultados_busqueda_libro.html", {"libros":libros, "autor":autor})
    else:
        respuesta="No enviaste datos."
    return HttpResponse(respuesta)

