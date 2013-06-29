from django.db import models

class Categoriasxproducto(models.Model):
    Descripcion= models.CharField(max_length=200)
    def __unicode__(self):
        return self.Descripcion

class Usuarios(models.Model):
    Idusuario=models.CharField(max_length=200)
    nombre=models.CharField(max_length=200)
    apellido=models.CharField(max_length=200)
    fechanacimiento=models.DateField('date published')
    direccion=models.CharField(max_length=200)
    contrasena=models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre








