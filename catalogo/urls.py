from django.contrib import admin
from django.urls import path
from .views import lista_libros

urlpatterns = [
    path("Lista_libros/" , lista_libros, name="lista de libros"),
]