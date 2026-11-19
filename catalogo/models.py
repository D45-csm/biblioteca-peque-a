from django.db import models
from django.db.models.signals import pre_save
# Create your models here.
class Categoria (models.Model):
    nombre= models.CharField(max_length=30, verbose_name="nombre categoria")
    slug= models.SlugField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nombre

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug= 'SLUG-categoria'


pre_save.connect(slug_generator, sender=Categoria)


class Autor (models.Model):
    nombre= models.CharField(max_length=30, verbose_name="nombre autor")
    pais= models.CharField(max_length=30,)

    def __str__(self):
        return self.nombre

class Libro (models.Model):
    titulo= models.CharField(max_length=30,)
    resumen= models.CharField(max_length=300 , verbose_name="resumen del libro")
    año= models.DateField(verbose_name="fecha del libro")
    portada= models.ImageField(upload_to="catalogo/", null=True, blank=True)
    disponible= models.BooleanField( default=True)
    autor= models.ForeignKey(Autor, on_delete=models.CASCADE ,null=False, blank=False)
    categoria= models.ForeignKey(Categoria, on_delete=models.CASCADE ,null=False, blank=False)

    def __str__(self):
        return self.titulo

class Prestamo(models.Model):
    nombre_solicitante= models.CharField(max_length=50 , verbose_name="nombre del solisitante")
    libro= models.ForeignKey(Libro, on_delete=models.CASCADE ,null=False, blank=False)
    fecha_prestamo= models.DateTimeField(auto_now_add=True)