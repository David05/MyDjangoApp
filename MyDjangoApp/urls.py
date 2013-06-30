from django.conf.urls import patterns, include, url
import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^polls/$', 'polls.views.producto_view'),
    url(r'^admin/', include(admin.site.urls)),
       (r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    )
