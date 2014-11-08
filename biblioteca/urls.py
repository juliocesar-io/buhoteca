from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'libros.views.inicio', name='inicio'),
    url(r'^libros/nuevo/$','libros.views.nuevo_libro' , name='libros_nuevo'),
    url(r'^autores/nuevo/$','autores.views.nuevo_autor', name='autores_nuevo'),
    url(r'^admin/', include(admin.site.urls)),
)



if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))

    urlpatterns += staticfiles_urlpatterns()
	