from django.shortcuts import render
from .forms import FormPreceptores, FormGraduacao, FormResidencia, FormMestrado, FormDoutorado, FormVinculo
from .models import Preceptores, Graduacao, Residencia, Mestrado, Doutorado, Vinculo_Profissional

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render


def RegistroPreceptor(request):
    form = FormPreceptores(request.POST or None)
    formG = FormGraduacao(request.POST or None)
    formR = FormResidencia(request.POST or None)
    formM = FormMestrado(request.POST or None)
    formD = FormDoutorado(request.POST or None)
    formV = FormVinculo(request.POST or None)

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
                    'form': form, 'formG': formG, 'formR': formR, 'formM': formM, 'formD': formD, 'formV': formV
                }
            )
        #------------------------------------- 
        if((request.POST['r_area'] != '') or (request.POST['r_ano_termino'] != '') or (request.POST['r_instituicao'] != '')):
            Residencia.objects.create(
                r_preceptores=Preceptores.objects.get(
                    pk=Preceptores.objects.filter(CPF=request.POST['CPF'])[:1]
                ),
                r_area=request.POST['r_area'],
                r_ano_termino=request.POST['r_ano_termino'],
                r_instituicao=request.POST['r_instituicao']
            ).save()
        #------------------------------------- 
        if((request.POST['m_area'] != '') or (request.POST['m_ano_termino'] != '') or (request.POST['m_instituicao'] != '')):
            Mestrado.objects.create(
                m_preceptores=Preceptores.objects.get(
                    pk=Preceptores.objects.filter(CPF=request.POST['CPF'])[:1]
                ),
                m_area=request.POST['m_area'],
                m_ano_termino=request.POST['m_ano_termino'],
                m_instituicao=request.POST['m_instituicao']
            ).save()
        #------------------------------------- 
        if((request.POST['d_area'] != '') or (request.POST['d_ano_termino'] != '') or (request.POST['d_instituicao'] != '')):
            Doutorado.objects.create(
                d_preceptores=Preceptores.objects.get(
                    pk=Preceptores.objects.filter(CPF=request.POST['CPF'])[:1]
                ),
                d_area=request.POST['d_area'],
                d_ano_termino=request.POST['d_ano_termino'],
                d_instituicao=request.POST['d_instituicao']
            ).save()
        #-------------------------------------
        dic = dict(request.POST)
        if('vinculo' in dic.keys()):
            vAux = dic['vinculo']
            Vinculo_Profissional.objects.create(
                v_preceptores=Preceptores.objects.get(
                    pk=Preceptores.objects.filter(
                        CPF=request.POST['CPF']
                    )[:1]
                ),
                vinculo=vAux[:],
                sesap_outro=request.POST['sesap_outro'],
                outro_vinculo=request.POST['outro_vinculo']
            ).save()
        #-------------------------------------

        # return redirect('../ListarPreceptores')
    return render(
        request,
        'registroPreceptor/RegistrarPreceptor.html', {
            'form': form,
            'formG': formG,
            'formR': formR,
            'formM': formM,
            'formD': formD,
            'formV': formV
        }
    )

def ListarPreceptores(request):
    preceptores = Preceptores.objects.all().values()
    graduacao = Graduacao.objects.all().values()
    residencia = Residencia.objects.all().values()
    mestrado = Mestrado.objects.all().values()
    doutorado = Doutorado.objects.all().values()
    vinculo = Vinculo_Profissional.objects.all().values()
    return render(
        request,
        'listagemPreceptores/ListarPreceptores.html', {
            'preceptores': preceptores,
            'graduacao': graduacao, 
            'residencia': residencia,
            'mestrado': mestrado,
            'doutorado': doutorado,
            'vinculo': vinculo
        }
    )