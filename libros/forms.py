#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import Libro
from autores.models import Autor

class LibroForm(forms.ModelForm):

	#autores = list(Autor.objects.values('nombres'))

	titulo = forms.CharField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Javascipt: The Good Parts'}))
	#autor = forms.ChoiceField(widget=forms.Select(attrs={'class': 'error'}), choices = autores)
	area = forms.CharField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Programación'}))
	editorial = forms.CharField(widget=forms.TextInput(attrs={'class': 'error','placeholder': "O'Reilly media"}))
    	class Meta:
        	model = Libro
        	fields = ['titulo','area','autor','editorial','cover_url','facultad','disponible_fisico','digital_url']