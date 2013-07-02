from django.conf.urls.defaults import patterns, include,url
import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^polls/$', 'polls.views.producto_view'),
    #url(r'^polls/$', 'polls.views.Contatcto_view'),


    url(r'^menu/$','polls.views.menu_view',name="menu"),
    url(r'^productos/$', 'polls.views.add_producto_view',name="addproductos"),
    url(r'^contactos/','polls.views.Contatcto_view',name="contactos"),
    url(r'^inicial/','polls.views.index',name="index"),
    url(r'^ver_productos/','polls.views.producto_view',name="ver_productos"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
)
