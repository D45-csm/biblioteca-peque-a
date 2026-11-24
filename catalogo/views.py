from django.shortcuts import render, get_object_or_404
from .models import Libro

# Create your views here.
def lista_libros(request):
    libros= Libro.objects.all()

    return render(request, 'lista_libros.html', {'libros' : libros })

def detalle_libro(request, pk):
    libro= get_object_or_404(Libro, pk=pk)

    context= {'libro': libro}

    return render(request, 'detalle_libro.html', context)