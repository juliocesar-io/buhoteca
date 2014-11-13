from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import  HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from libros.models import Libro
from prestamo.models import Prestamo

def nuevo_prestamo(request, id_libro, template='prestamoForm.html'):

    libro = get_object_or_404(Libro, pk=id_libro)
    formulario = AuthenticationForm()


    if request.method == 'POST' :
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST ['username']
            clave = request.POST ['password']
            acceso = authenticate(username = usuario, password = clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    # Obtener usuario
                    usuario = request.user
                    # Insertar registro en "prestamo"
                    prestamo = Prestamo()
                    prestamo.lector = usuario
                    prestamo.libro = libro
                    prestamo.save()
                    # Cambiar la disponibilidad del libro
                    libro.disponible_fisico = False
                    libro.save()

                    return HttpResponseRedirect('/prestar')
                else :
                    return render_to_response ('noactivo.html', context_instance=RequestContext(request))
            else :
                return render_to_response ('nousuario.html', context_instance=RequestContext(request))
    else:
        formulario = AuthenticationForm()
        return render_to_response('ingresar.html', {'formulario':formulario}, context_instance=RequestContext(request))

