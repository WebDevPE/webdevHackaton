from django import forms
from django.forms import ModelForm
from .models import *

class FormHoja(forms.ModelForm):
    class Meta:
        model= Hoja
        fields='__all__'

