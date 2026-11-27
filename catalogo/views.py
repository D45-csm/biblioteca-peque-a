from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Libro, Autor
from catalogo import forms

# Create your views here.
def lista_libros(request):
    libros= Libro.objects.all()

    return render(request, 'lista_libros.html', {'libros' : libros })

def detalle_libro(request, pk):
    libro= get_object_or_404(Libro, pk=pk)

    context= {'libro': libro}

    return render(request, 'detalle_libro.html', context)

def crear_libro(request):
    if request.method == 'POST' :
        form= forms.LibrosForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('crear-libro')

        else:
            print(form.errors)
            messages.success(request, 'hay campos incompletos o incorrectos')
    else:
        form= forms.LibrosForm(request.POST , request.FILES)
        messages.success(request, 'no se pudo crear el libro')
        return render(request , 'crear_libro.html' , {'form': form})

def editar_libro(request, pk):

    libro_editar= get_object_or_404(Libro, pk=pk)

    if request.method == 'POST' :
        form= forms.LibrosForm(request.POST , request.FILES, instance=libro_editar)
        if form.is_valid():
            form.save()
            return redirect('lista de libros')

        else:
            print(form.errors)
            messages.success(request, 'hay campos incompletos o incorrectos')
    else:
        form= forms.LibrosForm(instance=libro_editar)
        messages.success(request, 'no se pudo editar el libro')
        return render(request , 'editar_libro.html' , {'form': form , 'libro' : libro_editar})

def eliminar_libro(request, pk):
    libro= get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
    return redirect('lista de libros')


#CRUD autores 
def lista_autores(request):
    query= request.GET.get('q', '')
    autores= Autor.objects.all()
    if query != '':
        autores= Autor.objects.filter(Q(nombre__icontains=query) | Q(pais__icontains=query) )

    contexto= {
        'query': query ,
        'autores' : autores 
    }
    return render(request, 'lista_autores.html', contexto)



def detalle_autor(request, pk):
    autor= get_object_or_404(Autor, pk=pk)
    return render(request, 'detalle_autor.html', {'autor' : autor})

def crear_autor(request):
    if request.method == 'POST':
        form= forms.AutoresForm(request.POST, request.FILES)
        if form.is_valid() :
            form.save()
            return redirect('lista de autores')
    else:
        form= forms.AutoresForm(request.POST, request.FILES)
    return render(request, 'crear_autor.html', {'form': form})
    
def editar_autor(request, pk):
    autor_editar= get_object_or_404(Autor, pk=pk)

    if request.method == 'POST':
        form= forms.AutoresForm(request.POST, request.FILES, instance=autor_editar)

        if form.is_valid():
            form.save()
            return redirect('lista de autores')
    else:
        form= forms.AutoresForm( instance=autor_editar)
    return render(request, 'editar_autor.html', {'form': form , 'autor': autor_editar})

def eliminar_autor(request, pk):
    autor_eliminar= get_object_or_404(Autor, pk=pk)

    if request.method == 'POST':
        autor_eliminar.delete()

    return redirect('lista de autores')