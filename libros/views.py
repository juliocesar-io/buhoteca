#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from .models import Libro
from autores.models import Autor
from .forms import LibroForm

def inicio(request):
	autores = Autor.objects.all()
	libros = Libro.objects.all()

    	return render(request,'home.html', {'autores':autores,'libros':libros})


def nuevo_libro(request, template='libroForm.html'):
    form = LibroForm()
    if request.method == "POST":
    	form = LibroForm(request.POST)
        if form.is_valid():
        	form.save()
		return render(request,'libroNuevo.html')

    kwvars = {
        "form": form,
    }
    return render_to_response(template, kwvars, context_instance=RequestContext(request))


def docs(request):
    return render(request,'docs.html')