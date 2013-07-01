from polls.models import Categoriasxproducto,Usuario,Producto,prueba
from django.contrib import admin

class CategoriasxproductoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['Descripcion']}),
    ]
    list_display = ('Descripcion')
    list_display_links =('Descripcion')

admin.site.register(Categoriasxproducto)

class UsuarioAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['Idusuario']}),
        (None,               {'fields': ['nombre']}),
        (None,               {'fields': ['apellido']}),
        ('Date information', {'fields': ['fechanacimiento'],'classes': ['collapse']}),
        (None,               {'fields': ['direccion']}),
        (None,               {'fields': ['contrasena']})

    ]
    list_display = ('Idusuario,nombre,apellido,fechanacimiento,direccion,contrasena')
    list_display_links =('Idusuario,nombre,apellido,fechanacimiento,direccion,contrasena')

admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(prueba)






