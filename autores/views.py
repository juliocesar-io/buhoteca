from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render, redirect
from .forms import AutorForm
from autores.models import Autor

def nuevo_autor(request, template='autorForm.html'):
    form = AutorForm()
    if request.method == "POST":
    	form = AutorForm(request.POST)
        if form.is_valid():
        	form.save()
		return redirect('/libros/nuevo/')

    kwvars = {
        "form": form,
    }
    return render_to_response(template, kwvars, context_instance=RequestContext(request))

def listado_autores(request):
    autores = Autor.objects.all()
    return render(request,'autoresListado.html', {'autores':autores})