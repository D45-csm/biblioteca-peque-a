from django.contrib import admin
from django.urls import path
from .views import lista_libros, detalle_libro

urlpatterns = [
    path("Lista_libros/" , lista_libros, name="lista de libros"),
    path("<int:pk>/", detalle_libro, name="detalle_libro")
]