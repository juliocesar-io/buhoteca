from django.contrib import admin
from .models import Autor

class AutorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "nacionalidad")
    list_filter = ['nacionalidad']
    search_fields = ['nombre']

admin.site.register(Autor, AutorAdmin)