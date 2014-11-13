#encoding:utf-8
from django import forms
from .models import Prestamo


class PrestamoForm(forms.ModelForm):

    class Meta:
            model = Prestamo
            fields = []
