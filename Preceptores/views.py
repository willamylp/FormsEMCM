from django.shortcuts import render
from .forms import FormPreceptores, FormGraduacao, FormResidencia, FormMestrado, FormDoutorado
from .models import Preceptores, Graduacao, Residencia, Mestrado, Doutorado

from django.contrib import messages

from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.

def RegistroPreceptor(request):
    formG = FormGraduacao(request.POST or None)
    formR = FormResidencia(request.POST or None)
    formM = FormMestrado(request.POST or None)
    formD = FormDoutorado(request.POST or None)
    form = FormPreceptores(request.POST or None)
    if((formG.is_valid()) and (formR.is_valid()) and (formM.is_valid()) and (formD.is_valid()) and (form.is_valid())):
        formG.save()
        formR.save()
        formM.save()
        formD.save()
        form.save()
        messages.success(request, 'Preceptor Registrado com Sucesso!')
        return redirect('../ListarPreceptores')    
    return render(
        request,
        'registroPreceptor/RegistrarPreceptor.html', {
            'formG': formG,
            'formR': formR,
            'formM': formM,
            'formD': formD,
            'form': form
        }
    )

def ListarPreceptores(request):
    preceptores = Preceptores.objects.all().values()
    graduacao = Graduacao.objects.all().values()
    residencia = Residencia.objects.all().values()
    mestrado = Mestrado.objects.all().values()
    doutorado = Doutorado.objects.all().values()

    return render(
        request,
        'listagemPreceptores/ListarPreceptores.html', {
            'preceptores': preceptores,
            'graduacao': graduacao, 
            'residencia': residencia,
            'mestrado': mestrado,
            'doutorado': doutorado
        }
    )