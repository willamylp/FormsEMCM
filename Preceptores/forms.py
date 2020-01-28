from .models import Preceptores
from django import forms
from django.forms import ModelForm

class FormPreceptores(ModelForm):
    class Meta:
        model = Preceptores
        fields = '__all__'
        labels = {}