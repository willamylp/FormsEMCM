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
    # request.POST['CPF'] = 'XXXXXX'
    #print("Request >>>>", request.POST.get('CPF', False))
    #teste = Preceptores.objects.filter(CPF=234234)
    #print("PK >>>> ",  Preceptores.objects.get(pk=teste))

    if(form.is_valid()):
        form.save()
        if(request.POST['g_curso'] != ''):
            Graduacao.objects.create(
                g_preceptores=Preceptores.objects.get(
                    pk=Preceptores.objects.filter(CPF=request.POST['CPF'])[:1]
                ),
                g_curso=request.POST['g_curso'],
                g_ano_termino=request.POST['g_ano_termino'],
                g_instituicao=request.POST['g_instituicao']
            ).save()
        elif(request.POST['g_curso'] == ''):
            return render(
                request,
                'registroPreceptor/RegistrarPreceptor.html', {
                    'form': form, 'formG': formG, 'formR': formR, 'formM': formM, 'formD': formD
                }
            )
        #------------------------------------- 
        if((request.POST['r_area'] != '') or (request.POST['r_ano_termino'] != '') or (request.POST['r_instituicao'] != '')):
            if((request.POST['r_area'] == '') or (request.POST['r_ano_termino'] == '') or (request.POST['r_instituicao'] == '')):
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
            else:
                Residencia.objects.create(
                    r_preceptores=Preceptores.objects.get(
                        pk=Preceptores.objects.filter(CPF=request.POST['CPF'])[:1]
                    ),
                    r_area=request.POST['r_curso'],
                    r_ano_termino=request.POST['r_ano_termino'],
                    r_instituicao=request.POST['r_instituicao']
                ).save()
        #-------------------------------------

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