from django.contrib import admin
from .models import Libro


class LibroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "editorial", "area", "disponible_fisico", "facultad")
    list_filter = ['disponible_fisico']
    search_fields = ['titulo']

admin.site.register(Libro, LibroAdmin)