#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
	titulo = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Javascipt: The Good Parts'}))
	
    	class Meta:
        	model = Libro