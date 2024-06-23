from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from empresas.models import Empresa, Funcionario, Candidato
from formularios2.models import Resultado
from django.contrib.auth.models import User
import re
from empresas.views import logout_empresa, logout_funcionario, logout_candidato
from datetime import datetime

def home_empresa(request):
    exibir_navbar = True
    contexto_app = 'painel'
    if request.session.get('empresa'):
        empresa = Empresa.objects.get(id=request.session['empresa'])
        funcionarios = Funcionario.objects.filter(empresa=empresa)
        return render(request, 'home_empresa.html', {'empresa': empresa, 'funcionarios': funcionarios, 'exibir_navbar': exibir_navbar, 'contexto_app': contexto_app})
    else:
        return redirect('/painel/login_empresa/?status=2')

def candidatos_empresa(request): # Desnecessário? sim -> home dinâmica
    empresa = Empresa.objects.get(id=request.session['empresa'])
    funcionarios = Funcionario.objects.filter(empresa=empresa)
    emails = [funcionario.email for funcionario in funcionarios]
    candidatos = Candidato.objects.all()
    return render(request, 'candidatos_empresa.html', {'empresa': empresa, 'funcionarios': funcionarios, 'emails': emails, 'candidatos': candidatos})

def gerenciar_funcionario(request, funcionario_id): # Desnecessário? sim -> gerenciar pela home
    funcionario = Funcionario.objects.get(id=funcionario_id)
    return render(request, 'perfil_usuario.html', {'funcionario': funcionario})
def gerenciar_candidato(request, candidato_id): # Desnecessário? sim -> gerenciar pela home
    candidato = Candidato.objects.get(id=candidato_id)
    return render(request, 'perfil_usuario.html', {'candidato': candidato})

def dashboard_empresa(request):
    return render(request, 'dashboard_empresa.html')

def config_empresa(request):
    return render(request, 'config_empresa.html')

def home_usuario(request):
    exibir_navbar = True
    contexto_app = 'painel'
    if request.session.get('funcionario'):
        usuario = Funcionario.objects.get(id=request.session['funcionario'])
    elif request.session.get('candidato'):
        usuario = Candidato.objects.get(id=request.session['candidato'])
    else:
        return redirect('/auth/login_candidato/?status=2')
    return render(request, 'home_usuario.html',
                  {'usuario': usuario, 'exibir_navbar': exibir_navbar, 'contexto_app': contexto_app})

def perfil(request, usuario_id):
    exibir_navbar = True
    contexto_app = 'painel'
    if request.session.get('funcionario'):
        usuario = Funcionario.objects.get(id=request.session['funcionario'])
    elif request.session.get('candidato'):
        usuario = Candidato.objects.get(id=request.session['candidato'])
    else:
        return redirect('/auth/login_candidato/?status=2')
    return render(request, 'perfil_usuario.html')