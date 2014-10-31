from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'libros.views.inicio', name='inicio'),
    url(r'^libros/nuevo/$','libros.views.nuevo_libro' , name='libros_nuevo'),
    url(r'^autores/nuevo/$','autores.views.nuevo_autor', name='autores_nuevo'),
    url(r'^docs/', 'libros.views.docs', name='docs'),
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()