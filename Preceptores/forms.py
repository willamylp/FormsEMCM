from .models import Preceptores, Graduacao, Residencia, Mestrado, Doutorado, Vinculo_Profissional

from django import forms
from django.forms import ModelForm

class DateInput(forms.DateInput):
    input_type = 'date'

class FormPreceptores(ModelForm):
    class Meta:
        model = Preceptores
        fields = '__all__'
        labels = {}
        widgets = {}
class FormGraduacao(ModelForm):
    class Meta:
        model = Graduacao
        fields = '__all__'
        labels = {}
        widgets = {}
class FormResidencia(ModelForm):
    class Meta:
        model = Residencia
        fields = '__all__'
        labels = {}
        widgets = {}        
class FormMestrado(ModelForm):
    class Meta:
        model = Mestrado
        fields = '__all__'
        labels = {}
        widgets = {}
class FormDoutorado(ModelForm):
    class Meta:
        model = Doutorado
        fields = '__all__'
        widgets = {}

class FormVinculo(ModelForm):
    class Meta:
        model = Vinculo_Profissional
        fields = '__all__'
        widgets = {}   