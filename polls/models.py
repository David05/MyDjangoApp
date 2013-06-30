from django.db import models
#el polls es el app puedo tener n cantidad de app
class Categoriasxproducto(models.Model):
    Descripcion= models.CharField(max_length=200)
    def __unicode__(self):
        return self.Descripcion

class Usuario(models.Model):
    Idusuario=models.CharField(max_length=200)
    nombre=models.CharField(max_length=200)
    apellido=models.CharField(max_length=200)
    fechanacimiento=models.DateField('date published')
    direccion=models.CharField(max_length=200)
    contrasena=models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre

class Producto(models.Model):

    Codigo=models.CharField(max_length=200)
    Descripcion=models.CharField(max_length=200)
    Precio=models.IntegerField()
    Cantidad_actual=models.IntegerField()
    Imagen= models.ImageField(upload_to="C:/Users/torres/PycharmProjects/MyDjangoApp/MyDjangoApp/", null=True, blank=True)
    Cod_categoria_id=models.ForeignKey(Categoriasxproducto)
    def __unicode__(self):
        return self.Descripcion











