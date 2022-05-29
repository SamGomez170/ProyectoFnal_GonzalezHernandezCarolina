from django.urls import path
from . import views

urlpatterns = [
     path('lista/listas', views.ListaListas.as_view(), name='ListaListas'),
     path(r'^(?P<pk>\d+)$', views.ListaDetalle.as_view(), name='Detalle'),
     path(r'^nuevo$', views.ListaCreacion.as_view(), name='Nuevo'),
     path(r'^editar/(?P<pk>\d+)$', views.ListaUpdate.as_view(), name='Editar'),
     path(r'^borrar/(?P<pk>\d+)$', views.ListaDelete.as_view(), name='Borrar'),
     path("busqueda_lista/", views.busqueda_lista, name="busqueda_lista"),
     path("buscar_lista/", views.buscar_lista),
]

