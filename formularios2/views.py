from django.shortcuts import render, redirect
from django.http.response import HttpResponse, JsonResponse
from .models import *
from empresas.models import Candidato, Funcionario, Empresa
import random
from django.http import HttpResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime

"""Segunda tentativa de criar os invenários"""

def gerenciar_formularios(request):
    # print(request.session.keys())
    exibir_navbar = True
    formularios = Formulario.objects.all()
    if not (request.session.get('funcionario') or request.session.get('empresa')):
        return HttpResponse('Faça seu login.')
    try:
        funcionario = Funcionario.objects.get(id=request.session['funcionario'])
        print(funcionario.id)
        return render(request, 'gerenciar_formularios.html',
                      {'exibir_navbar': exibir_navbar, 'formularios': formularios, 'funcionario': funcionario})
    except:
        return render(request, 'gerenciar_formularios.html', {'exibir_navbar': exibir_navbar, 'formularios': formularios})

def formulario(request):
    if not (request.session.get('funcionario') or request.session.get('empresa')):
        return HttpResponse('Faça seu login.')
    formulario = request.GET.get('formulario')
    instancias = Formulario.objects.get(nome=formulario)
    formularios = Formulario.objects.all()
    nomes = [nome.nome for nome in formularios]
    # Verificar se o nome do formulário existe
    if formulario not in nomes:
        return HttpResponse(f'formulário "{formulario}" não encontrado.')
    contexto = {'categoria': request.GET.get('categoria'),
                'formulario': formulario,
                'instancias': instancias,
                'exibir_navbar': True,
                'contexto_app': 'formularios2'}
    # TO-DO: validacao apenas 1 vez!
    try:
        funcionario = request.session.get('funcionario')
        # lista dos resultados do funcionário em questão
        resultados = Resultado.objects.filter(funcionario=funcionario)
        # Vamos verificar se o formulário já foi realizado pelo usuário
        for resultado in resultados:
            if resultado.formulario.nome == formulario:
                # Formulário já realizado, redirecionando o usuário para o menu de formulários
                return redirect('/formularios2/gerenciar_formularios/?status=2')
        return render(request, 'formulario.html', contexto)
    except:
        return render(request, 'formulario.html', contexto)

def get_formulario(request):
    try:
        questoes = Questao.objects.all()
        if request.GET.get('formulario'):
            questoes = questoes.filter(formulario__nome__icontains=request.GET.get("formulario"))
        questoes = list(questoes)
        data = []
        random.shuffle(questoes)

        for q in questoes:
            data.append({
                'uid': q.uid,
                'nome': q.nome,
                'formulario': q.formulario.nome,
                'uid_formulario': q.formulario.uid,
                'tempo': q.formulario.tempo,
                'categoria': q.categoria.nome,
                'qtd_respostas': q.qtd_respostas,
                'respostas': q.get_respostas(),
            })
        payload = {'status': True, 'data': data}
        return JsonResponse(payload)
    except Exception as e:
        print(e)
    return HttpResponse('Erro inesperado.')

@csrf_exempt
def coletar_respostas(request):
    # Tratamento das respostas
    if not (request.session.get('funcionario') or request.session.get('empresa')):
        return HttpResponse('Faça seu login.')
    if request.method == 'GET':
        return render(request, 'formulario.html')
    elif request.method == 'POST':
        try:
            respostasMarcadas = json.loads(request.body.decode())
            print (respostasMarcadas)

            nome_formulario = respostasMarcadas['respostasMarcadas'][0]['formulario_da_resposta']
            uid_formulario = respostasMarcadas['respostasMarcadas'][0]['uid_formulario']
            acerto = 0
            erro = 0
            for resposta in respostasMarcadas['respostasMarcadas']:
                if resposta['resposta_correta']:
                    acerto += 1
                else:
                    erro += 1
            porcentagem_acerto = (acerto/(acerto + erro))*100
            print(f'Porcentagem de acerto de {nome_formulario}:', porcentagem_acerto)
            frase = 'texto'

            try:
                funcionario = Funcionario.objects.get(id=request.session['funcionario'])
                resultado = Resultado(funcionario = funcionario,
                                  formulario = Formulario.objects.get(uid=uid_formulario),
                                  nome_formulario = nome_formulario,
                                  pontuacao = porcentagem_acerto,
                                  frase = frase)
                resultado.save()
                funcionario.status_questionario += 1
                funcionario.save()
                #funcionario.ultimo_envio = datetime.now()
            except:
                pass
            return HttpResponse(json.dumps({'status': 1, 'funcionario': bool(funcionario)}))
        except Exception as e:
            return JsonResponse({'erro': str(e)}, status=500)
def resultado(request, funcionario_id):
    funcionario = Funcionario.objects.get(id=funcionario_id)
    # Verifica se o usuário tem permissão para visualizar a página
    if not (request.session.get('funcionario') or request.session.get('empresa')):
        return HttpResponse('Você não tem permissão para visualizar esta página.')
    # Verifica permissão para a empresa
    if request.session.get('empresa') and funcionario.empresa.id != request.session['empresa']:
        return HttpResponse('Você não tem permissão para visualizar esta página.')
    # Verifica permissão para o funcionário
    if request.session.get('funcionario') and funcionario_id != request.session['funcionario']:
        return HttpResponse('Você não tem permissão para visualizar esta página.')
    # Verifica se o funcionário concluiu todos os formulários
    if not funcionario.verificar_status:
        return redirect('/formularios2/gerenciar_formularios/?status=2')
    resultados = Resultado.objects.filter(funcionario=funcionario)
    contexto = {'funcionario': {'id': funcionario.id, 'nome': funcionario.nome},
                'idade': None,
                'data': None,
                'formacao': None,
                'resultados': resultados,
                }
    return render(request, 'resultado.html', contexto)

def coletar_resultado(request, funcionario_id):
    funcionario = Funcionario.objects.get(id=funcionario_id)
    resultados = Resultado.objects.filter(funcionario=funcionario)
    pontuacao = []
    frases = []
    labels = []
    for resultado in resultados:
        pontuacao.append(resultado.pontuacao)
        frases.append(resultado.frase)
        labels.append(resultado.nome_formulario)
    data_json = {
        'funcionario': {'id': funcionario.id, 'nome': funcionario.nome},
        'resultados': list(zip(labels, pontuacao, frases)),
        'pontuacao': pontuacao,
        'frases': frases,
        'labels': labels,
    }
    return JsonResponse(data_json)