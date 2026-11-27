from django import forms
from .models import Libro, Autor

class LibrosForm(forms.ModelForm):
    class Meta:
        model= Libro
        fields= ['titulo', 'resumen', 'año', 'portada', 'disponible', 'autor', 'categoria']
        labels = {'año': 'fecha de publicación'}
        widgets = {
            'titulo': forms.TextInput(attrs= {'class' : 'form-control' , 'placeholder': 'eje: calculo integral'}),
            'resumen': forms.TextInput(attrs= { 'class' : 'form-control' , }),
            'año': forms.DateInput(format='%Y-%m-%d', attrs= { 'type': 'date' , 'class' : 'form-control' ,})
        }

class AutoresForm(forms.ModelForm):
    class Meta:
        model= Autor
        fields= ['nombre', 'pais']

        widgets = {
            'nombre': forms.TextInput(attrs= { 'class' : 'form-control' , }),
            'pais': forms.TextInput(attrs= { 'class' : 'form-control' , }),
        }