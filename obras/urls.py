from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.inicio, name="InicioObras"),
    
    path("nuevo_libro/", views.nuevo_libro, name="nuevo_libro"),
    path("lista_libros/", views.lista_libros, name="lista_libros"),
    path("libro/<id>", views.ver_libro, name="ver_libro"),
    path("eliminar_libro/<id>", views.borrar_libro, name="borrar_libro"),
    path("libro/editar/<id>", views.editar_libro, name="editar_libro"),
    path("busqueda_autor/", views.busqueda_autor, name="busqueda_autor"),
    path("buscar_libro/", views.buscar_libro),

    path('noticias/lista', views.ListaNoticias.as_view(), name='ListaNoticias'),
    path(r'^(?P<pk>\d+)$', views.NoticiaDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.NoticiaCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.NoticiaUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.NoticiaDelete.as_view(), name='Delete'),
    path("busqueda_titulo/", views.busqueda_titulo, name="busqueda_titulo"),
    path("buscar_noticia/", views.buscar_noticia),

    path('login', views.login_request, name = 'Login'),
    path('logout', LogoutView.as_view(template_name='obras/logout.html'), name='Logout'),
    path('register', views.register, name = 'Register'),
    path("editarUsuario", views.editarUsuario, name="EditarUsuario"),

    path('agregarImagen',views.agregarImagen, name='agregarImagen'),
    
    
]

