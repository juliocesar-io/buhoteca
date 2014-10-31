#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import Autor

class AutorForm(forms.ModelForm):

    class Meta:
        model = Autor