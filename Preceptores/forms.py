from .models import Preceptores, Graduacao, Mestrado, Doutorado
from django import forms
from django.forms import ModelForm

class DateInput(forms.DateInput):
    input_type = 'date'


class FormPreceptores(ModelForm):
    class Meta:
        model = Preceptores
        fields = '__all__'
        labels = {}
        widgets = {
            'preceptores.': DateInput(),
            'data_termino': DateInput(),
            'data_nascimento': DateInput(),
            'data_nascimento': DateInput(),
            'data_nascimento': DateInput(),
        }
class FormGraduacao(ModelForm):
    class Meta:
        model = Graduacao
        fields = '__all__'
        widgets = {
            'data_termino': DateInput()
        }
class FormMestrado():
    class Meta:
        model = Mestrado
        fields = '__all__'
        widgets = {
            'data_termino':
        }        