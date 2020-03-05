from django.shortcuts import render
from .forms import FormPreceptores, FormGraduacao, FormResidencia, FormMestrado, FormDoutorado
from .models import Preceptores, Graduacao, Residencia, Mestrado, Doutorado

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.

def RegistroPreceptor(request):
    form = FormPreceptores(request.POST or None)
    formG = FormGraduacao(request.POST or None)
    formR = FormResidencia(request.POST or None)
    formM = FormMestrado(request.POST or None)
    formD = FormDoutorado(request.POST or None)
    # print('>>>>>>', Preceptores.objects.last())
    #teste = Preceptores.objects.get(pk=1)
    #print(teste.nome)
    if(form.is_valid()):
        form.save()
        Graduacao.objects.create(
            g_preceptores=Preceptores.objects.get(
                pk=Preceptores.objects.last()
            ),
            g_curso="teste!",
            g_ano_termino=2019,
            g_instituicao="UFRN"
        ).save()

 
    # Graduacao.objects.create(
    #     formG.Meta.model.g_curso=""
    # )

    # Graduacao.objects.filter(id=Preceptores.objects.first())
    # print('---->', Graduacao.objects.filter(id=Preceptores.objects.first()))
    # graduacao.g_preceptores = Preceptores.objects.last()
    # graduacao.save()
    # formG.Meta.model.g_preceptores = Preceptores.objects.last()
    # print(formG.Meta.model.g_preceptores)

    # formR.Meta.model.r_preceptores = Preceptores.objects.last()
    # formM.Meta.model.m_preceptores = Preceptores.objects.last()
    # formD.Meta.model.d_preceptores = Preceptores.objects.last()

    #print(Graduacao.objects.id_g_preceptores)
    #print(formG.is_valid())
    if((formG.is_valid()) and (formR.is_valid()) and (formM.is_valid()) and (formD.is_valid())):
    # if(formG.is_valid()):
        # form.save()
        formG.save()
        formR.save()
        formM.save()
        formD.save()
        messages.success(request, 'Preceptor Registrado com Sucesso!')
        return redirect('../ListarPreceptores')    
    return render(
        request,
        'registroPreceptor/RegistrarPreceptor.html', {
            'form': form,
            'formG': formG,
            'formR': formR,
            'formM': formM,
            'formD': formD
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