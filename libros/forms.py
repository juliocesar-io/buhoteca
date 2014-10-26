#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import Autor, Libro

class LibroForm(forms.ModelForm):
	titulo = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Titulo'}))
	
    	class Meta:
        	model = Libro
