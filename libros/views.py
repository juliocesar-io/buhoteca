#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render
from .models import Libro
from autores.models import Autor
from .forms import LibroForm


def inicio(request):
    autores = Autor.objects.all()
    libros = Libro.objects.all()
    return render(request, 'inicio.html', {'autores': autores, 'libros': libros})


def nuevo_libro(request, template='libroForm.html'):
    form = LibroForm()
    if request.method == "POST":
        form = LibroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, 'libroNuevo.html')

    kwvars = {
        "form": form,
    }
    return render_to_response(template, kwvars, context_instance=RequestContext(request))


def listado_libros(request):
    autores = Autor.objects.all()
    libros = Libro.objects.all()
    return render(request, 'librosListado.html', {'autores': autores, 'libros': libros})


def detalle_libro(request, id_libro, template='libroDetalle.html'):
    libro = get_object_or_404(Libro, pk=id_libro)
    return render_to_response(template, {'libro': libro}, context_instance=RequestContext(request))

