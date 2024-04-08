from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from empresas.models import Empresa, Funcionario, Candidato
from django.contrib.auth.models import User
import re
from empresas.views import logout_empresa, logout_funcionario, logout_candidato
from datetime import time


def home_empresa(request):
    if request.session.get('empresa'):
        empresa = Empresa.objects.get(id=request.session['empresa'])
        nome_empresa = empresa.nome
        funcionarios = Funcionario.objects.filter(empresa=empresa)
        # print(funcionarios)

        return render(request, 'home_empresa.html', {'nome_empresa': nome_empresa, 'funcionarios': funcionarios})

    else:
        return redirect('/auth/login_empresa/?status=2')

def candidatos_empresa(request):
    candidatos = Candidato.objects.all()
    return render(request, 'candidatos_empresa.html', {'candidatos': candidatos})

def relatorios_empresa(request):
    return render(request, 'relatorios_empresa.html')

def dashboard_empresa(request):

    pass

def config_empresa(request):
    return render(request, 'config_empresa.html')


def home_funcionario(request):
    if request.session.get('funcionario'):
        funcionario = Funcionario.objects.get(id=request.session['funcionario'])
        nome_funcionario = funcionario.nome

        return render(request, 'home_funcionario.html', {'nome_funcionario': nome_funcionario})

    else:
        return redirect('/auth/login_funcionario/?status=2')

def config_funcionario(request):
    pass

def home_candidato(request):
    if request.session.get('candidato'):
        candidato = Candidato.objects.get(id=request.session['candidato'])
        nome_candidato = candidato.nome

        return render(request, 'home_candidato.html', {'nome_candidato': nome_candidato})

    else:
        return redirect('/auth/login_candidato/?status=2')

def config_candidato(request):
    pass