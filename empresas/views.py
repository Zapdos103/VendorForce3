from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Candidato, Empresa, Funcionario
from django.contrib.auth.models import User
import re
from hashlib import sha256
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import make_password, check_password
import logging

def cadastro_landing(request):
    if request.session.get('empresa'):
        return redirect('/painel/home_empresa')
    else:
        if request.method == 'GET':
            contexto = {'exibir_navbar': True,
                        'contexto_app:': 'auth',
                        'status': request.GET.get('status')}

            return render(request, 'cadastro_landing.html', contexto)

        elif request.method == 'POST':
            request.session.flush()
            razao_social = request.POST.get('razao_social')
            nome = request.POST.get('nome')
            cargo = request.POST.get('cargo')
            email = request.POST.get('email')
            telefone = request.POST.get('telefone')
            setor = request.POST.get('setor')
            segmento = request.POST.get('segmento')
            qtd_vendedores = request.POST.get('qtd_vendedores')
            senha = request.POST.get('senha')
            repetir_senha = request.POST.get('repetir_senha')

            # Validações do cadastro landing.
            def já_registrado():
                email2 = Empresa.objects.filter(email=email).first()
                telefone2 = Empresa.objects.filter(telefone=telefone).first()
                razao_social2 = Empresa.objects.filter(razao_social=razao_social).first()
                nome2 = Empresa.objects.filter(nome=nome).first()

                for campo in (email2, telefone2, razao_social2, nome2):
                    if campo:
                        return redirect('/auth/cadastro_landing/?status=3')
                return None  # Retorna None se não houver erro

            resultado_validação = já_registrado()
            if resultado_validação is not None:
                return resultado_validação

            def campo_vazio():
                field_list = (razao_social, nome, cargo, email, telefone, setor, segmento, qtd_vendedores, senha, repetir_senha)
                for campo in field_list:
                    if len(campo) == 0 or campo.isspace():
                        return redirect('/auth/cadastro_landing/?status=10')
                return None  # Retorna None se não houver erro

            resultado_validação = campo_vazio()
            if resultado_validação is not None:
                return resultado_validação

            def valida_senha():
                if senha != repetir_senha:
                    return redirect('/auth/cadastro_landing/?status=1')
                return None  # Retorna None se não houver erro

            resultado_validação = valida_senha()
            if resultado_validação is not None:
                return resultado_validação

            # ... Outras validações ...
            # Salvar a empresa no banco de dados
            try:
                empresa = Empresa(
                    razao_social=razao_social.strip(),
                    nome=nome.strip(),
                    cargo=cargo,
                    email=email,
                    telefone=''.join(filter(str.isdigit, telefone)),
                    setor=setor,
                    segmento=segmento,
                    qtd_vendedores=qtd_vendedores,
                    senha=make_password(senha),
                )
                # Empresa cadastrada com sucesso
                empresa.save()
            except Exception as e:
                # Erro inesperado
                print(f'Erro ao salvar a empresa: {str(e)}')
                return redirect('/auth/cadastro_landing/?status=11')
            return redirect('/auth/cadastro_landing/?status=0')

def cadastro_completo(request):
    if request.method == 'GET':
        contexto = {'exibir_navbar': True,
                    'contexto_app:': 'auth'}
        return render(request, 'cadastro_landing.html', contexto)

    #elif request.method == 'POST':
        # request.session.flush()
        #razao_social = request.POST.get('razao_social')
        #endereco = reques.POST.get('endereco')
        #CEP =
        #CNPJ =
        #nome = request.POST.get('nome')
        #cargo = request.POST.get('cargo')
        #email = request.POST.get('email')
        #telefone = request.POST.get('telefone')
        #setor = request.POST.get('setor')
        #segmento = request.POST.get('segmento')
        #qtd_vendedores = request.POST.get('qtd_vendedores')
        #senha = request.POST.get('senha')
        #repetir_senha = request.POST.get('repetir_senha')
        #endereco_cobranca =
        #contato_finanaceiro =
        #telefone_cobranca =
    pass

def cadastro_candidato(request):
        if request.method == 'GET':
            contexto = {'exibir_navbar': True,
                        'contexto_app:': 'auth',
                        'status': request.GET.get('status')}
            return render(request, 'cadastro_candidato.html', contexto)
        elif request.method == 'POST':
            request.session.flush()
            nome_completo = request.POST.get('nome_completo')
            data_de_nascimento = request.POST.get('data_de_nascimento')
            email = request.POST.get('email')
            senha = request.POST.get('senha')
            funcao = request.POST.get('funcao')
            telefone = request.POST.get('telefone')

            # Validações do cadastro de candidatos
            def já_registrado():
                email2 = Candidato.objects.filter(email=email).first()
                telefone2 = Candidato.objects.filter(telefone=telefone).first()
                for campo in (email2, telefone2):
                    if campo:
                        return redirect('/auth/cadastro_candidato/?status=1')
                return None  # Retorna None se não houver erro

            resultado_validação = já_registrado()
            if resultado_validação is not None:
                return resultado_validação

            def campo_vazio():
                for campo in (nome_completo, email, data_de_nascimento, funcao, telefone):
                    if len(campo) == 0 or campo.isspace():
                        return redirect('/auth/cadastro_candidato/?status=2')
                return None  # Retorna None se não houver erro

            resultado_validação = campo_vazio()
            if resultado_validação is not None:
                return resultado_validação

            def valida_email():
                padrao = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
                if not padrao.match(email):
                    return redirect('/auth/cadastro_funcionario/?status=3')
                return None  # Retorna None se não houver erro

            resultado_validação = valida_email()
            if resultado_validação is not None:
                return resultado_validação
            

            # ... Outras Validações ...
            # Salvar o candidato no banco de dados
            try:
                candidato = Candidato(
                    nome=nome_completo.strip(),
                    data_de_nascimento=data_de_nascimento,
                    email=email,
                    senha=make_password(senha),
                    funcao=funcao,
                    telefone=''.join(filter(str.isdigit, telefone)),
                )
                candidato.save()
                # Canditato cadastrado com sucesso
                return redirect('/auth/cadastro_candidato/?status=0')
            except Exception as e:
                # Erro inesperado
                print(f'Erro ao salvar o candidato: {str(e)}')
                return redirect('/auth/cadastro_candidato/?status=4')

def cadastro_funcionario(request):
    if request.method == 'GET':
        contexto = {'exibir_navbar': True,
                    'contexto_app:': 'auth',
                    'status': request.GET.get('status')}
        return render(request, 'cadastro_funcionario.html', contexto)
    elif request.method == 'POST':
        # Primeiro verificamos se a empresa está logada; se sim -> tentar salvar os dados; se não -> exibir status
        if request.session.get('empresa'):
            empresa_id = request.session['empresa']
            email = request.POST.get('email')
            # Agora, vamos verificar se o candidato existe; se sim -> tentar salvar o funcionário; se não -> exibir status
            try:
                funcionario1 = Candidato.objects.get(email=email)
                funcionario2 = Funcionario(
                    empresa=Empresa.objects.get(id=empresa_id),
                    nome=funcionario1.nome,
                    data_de_nascimento=funcionario1.data_de_nascimento,
                    email=funcionario1.email,
                    senha=funcionario1.senha,
                    funcao=funcionario1.funcao,
                    telefone=funcionario1.telefone,
                )
                funcionario2.save()
                # Funcionário cadastrado com sucesso
                return redirect('/auth/cadastro_funcionario/?status=0')
            except Candidato.DoesNotExist:
                # Lidar com o caso em que o candidato não é encontrado
                return redirect('/auth/cadastro_funcionario/?status=3')
            except Exception as e:
                # Erro inesperado
                print(f'Erro ao salvar o funcionário: {str(e)}')
                return redirect('/auth/cadastro_funcionario/?status=1')
        # Caso o usuário não esteja logado em nenhuma empresa
        return redirect('/auth/cadastro_funcionario/?status=2')

def login_empresa(request):
    if request.method == 'GET':
        contexto = {'exibir_navbar': True,
                    'contexto_app:': 'auth',
                    'status': request.GET.get('status')}
        return render(request, 'login_empresa.html', contexto)
    elif request.method == 'POST':
        request.session.flush()
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        # senha = sha256(senha.encode()).hexdigest()
        # empresa = Empresa.objects.get(email=email, senha=senha)
        try:
            empresa = Empresa.objects.filter(email=email)
            if not empresa:
                return redirect('/auth/login_empresa/?status=1')
            if check_password(senha, empresa.senha):
                # Login bem-sucedido, a empresa foi encontrada
                request.session['empresa'] = empresa[0].id # <-- Aqui é definida a session 'empresa'
                return redirect('/painel/home_empresa')
            else:
                # Email ou Senha incorretos
                return redirect('/auth/login_empresa/?status=1')
        except ObjectDoesNotExist:
            # Erro inesperado
            return redirect('/auth/login_empresa/?status=2')
        
def login_usuario(request):
    if request.method == 'GET':
        request.session.flush()
        contexto = {'exibir_navbar': True,
                    'contexto_app:': 'auth',
                    'status': request.GET.get('status')}
        return render(request, 'login_usuario.html', contexto)
    elif request.method == 'POST':
        request.session.flush()
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        try:
            funcionario = Funcionario.objects.filter(email=email)
            if not funcionario:
                return redirect('/auth/login_usuario/?status=1')
            if check_password(senha, funcionario.senha):
                # Login bem-sucedido, o candidato foi encontrado
                request.session['funcionario'] = funcionario[0].id  # <-- Aqui é definida a session 'funcionario'
                return redirect('/painel/home_usuario')
            else:
                # Email ou Senha incorretos
                return redirect('/auth/login_usuario/?status=1')
        except:
            try:
                candidato = Candidato.objects.filter(email=email).filter(senha=senha)
                if not candidato:
                    return redirect('/auth/login_usuario/?status=1')
                if check_password(senha, candidato.senha):
                    # Login bem-sucedido, o funcionário foi encontrado
                    request.session['candidato'] = candidato[0].id  # <-- Aqui é definida a session 'candidato'
                    return redirect('/painel/home_usuario')
                else:
                    # Email ou Senha incorretos
                    return redirect('/auth/login_usuario/?status=1')
                print(request.session)
            except ObjectDoesNotExist:
                # Erro inesperado
                return redirect('/auth/login_usuario/?status=2')
            
def logout_empresa(request):
    request.session.flush()
    return redirect('/auth/login_empresa')

def logout_usuario(request):
    request.session.flush()
    return redirect('/auth/login_usuario')