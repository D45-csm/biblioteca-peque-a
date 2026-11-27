from django.contrib import admin
from django.urls import path
from catalogo import views

urlpatterns = [
    path("Lista_libros/" , views.lista_libros, name="lista de libros"),
    path("listar/<int:pk>/", views.detalle_libro, name="detalle_libro"),
    path('crear_libro/', views.crear_libro, name='crear-libro'),
    path('editar_libro/<int:pk>/', views.editar_libro, name='editar-libro'),
    path('eliminar_libro/<int:pk>/', views.eliminar_libro, name='eliminar-libro'),
    path('lista_autores//', views.lista_autores, name='lista de autores'),
    path('crear_autor/', views.crear_autor, name='crear-autor'),
    path('detalle_autor/<int:pk>', views.detalle_autor, name='detalle-autor'),
    path('editar_autor/<int:pk>', views.editar_autor, name='editar-autor'),
    path('eliminar_autor/<int:pk>/', views.eliminar_autor, name='eliminar-autor'),
]