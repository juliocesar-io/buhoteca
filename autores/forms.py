#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import Autor

class AutorForm(forms.ModelForm):

	nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Julio César'}))
    	class Meta:
        	model = Autor