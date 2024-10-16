from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from empresas.models import Empresa, Funcionario, Candidato
from formularios2.models import Formulario, Resultado
from django.contrib.auth.models import User
import re
from empresas.views import logout_empresa, logout_usuario
from datetime import datetime

# Empresa

def home_empresa(request):
    exibir_navbar = True
    contexto_app = 'painel'
    if request.session.get('empresa'):
        empresa = Empresa.objects.get(id=request.session['empresa'])
        funcionarios = Funcionario.objects.filter(empresa=empresa)
        return render(request, 'home_empresa.html', {'empresa': empresa, 'funcionarios': funcionarios, 'exibir_navbar': exibir_navbar, 'contexto_app': contexto_app})
    else:
        return redirect('/auth/login_empresa/?status=2')

def candidatos_empresa(request): # Desnecessário? sim -> home dinâmica
    empresa = Empresa.objects.get(id=request.session['empresa'])
    funcionarios = Funcionario.objects.filter(empresa=empresa)
    emails = [funcionario.email for funcionario in funcionarios]
    candidatos = Candidato.objects.all()
    return render(request, 'candidatos_empresa.html', {'empresa': empresa, 'funcionarios': funcionarios, 'emails': emails, 'candidatos': candidatos})

def dashboard_empresa(request):
    return render(request, 'dashboard_empresa.html')

def config_empresa(request):
    return render(request, 'config_empresa.html')

def excluir_funcionario(request, funcionario_id):
    # TO-DO: adicionar modal ao botao de excluir funcionario
    funcionario = Funcionario.objects.get(id=funcionario_id)
    if request.session.get('empresa'):
        empresa = Empresa.objects.get(id=request.session['empresa'])
        print(empresa)
        if funcionario.empresa.id == empresa.id:
            funcionario.delete()
            return redirect(f'/painel/home_empresa/?status=1')
        return redirect(f'/painel/perfil_funcionario/?status=2')
    return redirect(f'/painel/perfil_funcionario/{funcionario_id}/?status=2')

def salvar_formularios(request, funcionario_id):
    funcionario = Funcionario.objects.get(id=funcionario_id).id
    if request.method == 'POST':
        ids = request.POST.getlist('formularios')
        formularios_marcados = Formulario.objects.filter(id__in=ids)
        todos_os_formularios = Formulario.objects.filter(empresa=funcionario.empresa)
        # Vamos adicionar o funcionário aos formularios selecionados
        for formulario in todos_os_formularios:
            if str(formulario.id) in ids:
                formulario.funcionarios.add(funcionario)
            # Devemos excluir os formularios nao marcados que estavam disponíveis para o usuário
            else:
                formulario.funcionarios.remove(funcionario)

        for formulario in todos_os_formularios:
            formulario.save()

    return redirect(f'/painel/perfil_funcionario/{funcionario_id}/?status=0')

# Usuário

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

def perfil_funcionario(request, funcionario_id):
    empresarial = False
    editar = False
    formularios = False
    funcionario = Funcionario.objects.get(id=funcionario_id)
    if request.session.get('empresa'):
        empresa = Empresa.objects.get(id=request.session['empresa'])
        if funcionario.empresa.id == empresa.id:
            empresarial = True
            formularios = Formulario.objects.filter(empresa=empresa)
    if request.session.get('funcionario'):
        if Funcionario.objects.get(id=request.session['funcionario']).id == funcionario_id:
            editar = True

    contexto = {
        'exibir_navbar': True,
        'contexto_app': 'painel',
        'funcionario': {'id': funcionario.id, 'nome': funcionario.nome, 'email': funcionario.email},
        'empresarial': empresarial,
        'editar': 'editar',
        'formularios': formularios
    }
    return render(request, 'perfil_funcionario.html', contexto)