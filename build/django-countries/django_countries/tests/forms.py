from django import forms

from django_countries.tests import models


class PersonForm(forms.ModelForm):

    class Meta:
        model = models.Person
        fields = ['country']


class LegacyForm(forms.ModelForm):

    class Meta:
        model = models.Legacy
        fields = ['default', 'default_callable']
