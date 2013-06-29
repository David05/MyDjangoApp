from polls.models import Poll,Choice,Categoriasxproducto,Usuarios
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'],'classes': ['collapse']})
    ]
    inlines = [ChoiceInline]
admin.site.register(Poll, PollAdmin)

class CategoriasxproductoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['Descripcion']}),
    ]
    list_display = ('Descripcion')
    list_display_links =('Descripcion')

admin.site.register(Categoriasxproducto)

class UsuariosAdmin(admin.ModelAdmin):
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

admin.site.register(Usuarios)





