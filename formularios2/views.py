from django.shortcuts import render, redirect
from django.http.response import HttpResponse, JsonResponse
from .models import *
from empresas.models import Candidato, Funcionario
import random


"""Segunda tentativa de criar os invenários"""

def home(request):
    contexto = {'categorias': Categoria.objects.all(),
               'exibir_navbar': True,
               'contexto_app': 'formularios2'}
    if request.GET.get('categoria'):
        return redirect(f'/formularios2/formulario/?categoria={request.GET.get("categoria")}')

    return render(request, 'home.html', contexto)

def formulario(request):
    contexto = {'categoria': request.GET.get('categoria'),
               'exibir_navbar': True,
               'contexto_app': 'formularios2'}

    return render(request, 'formulario.html', contexto)

def get_formulario(request):
    try:
        questoes = Questao.objects.all()
        formularios = Formulario.objects.all()

        if request.GET.get('categoria'):
            questoes = questoes.filter(categoria__nome__icontains=request.GET.get("categoria"))

        questoes = list(questoes)
        print(questoes)
        data = []
        random.shuffle(questoes)

        for q in questoes:
            data.append({
                'uid': q.uid,
                'nome': q.nome,
                'formulario': q.formulario.nome,
                'categoria': q.categoria.nome,
                'qtd_respostas': q.qtd_respostas,
                'respostas': q.get_respostas(),
            })
        payload = {'status': True, 'data': data}

        return JsonResponse(payload)

    except Exception as e:
        print(e)

    return HttpResponse('Erro inesperado.')

def resultado(request):
    contexto = {'exibir_navbar': False,
                'contexto_app': 'formularios2'}

    # Aplicar essa lógica ao formulario depois
    if request.session.get('candidato') or request.session.get('funcionario'):

        if request.session.get('candidato'):
            candidato = Candidato.objects.get(id=request.session['candidato'])
        if request.session.get('funcionario'):
            funcionario = Funcionario.objects.get(id=request.session['funcionario'])

        if request.method == 'GET':
            return render(request, 'formulario.html')

        elif request.method == 'POST':
            # Recuperar as respostas enviadas pelo usuário
            respostas_ids = request.POST.getlist('respostas')
            respostas = Resposta.objects.filter(pk__in=respostas_ids)
            # Calcular a porcentagem de acerto por categoria
            porcentagens = {}

            for resposta_id in respostas:
                resposta = Resposta.objects.get(pk=resposta_id)
                nome_categoria = resposta.questao.categoria.nome
                if nome_categoria not in porcentagens:
                    porcentagens[nome_categoria] = {'total': 0, 'corretas': 0}
                porcentagens[nome_categoria]['total'] += 1
                if resposta.resposta_correta:
                    porcentagens[nome_categoria]['corretas'] += 1

            resultados = {}

            for nome_categoria, dados in porcentagens.items():
                if dados > 0:
                    porcentagem_acerto = (dados['corretas']/dados['total'])*100
                else:
                    porcentagem_acerto = 0

                if porcentagem_acerto <= 20:
                    frase = 'frase 1'
                elif porcentagem_acerto <= 40:
                    frase = 'frase 2'
                elif porcentagem_acerto <= 60:
                    frase = 'frase 3'
                elif porcentagem_acerto <= 80:
                    frase = 'frase 4'
                else:
                    frase = 'frase 5'
                resultados[nome_categoria] = {'porcentagem_acerto': porcentagem_acerto,
                                              'frase': frase}

            print(resultados)
            print(respostas_ids)
            # Renderização
            return render(request, 'resultado.html', {'resultados': resultados}) # passar o usuário

    else:
        return HttpResponse('Faça seu Login.')

def resultado2(request):
    if request.session.get('candidato') or request.session.get('funcionario'):

        if request.session.get('candidato'):
            candidato = Candidato.objects.get(id=request.session['candidato'])
        if request.session.get('funcionario'):
            funcionario = Funcionario.objects.get(id=request.session['funcionario'])

        if request.method == 'GET':
            return render(request, 'formulario.html')

        elif request.method == 'POST':
            respostasMarcadas = request.POST.get('respostasMarcadas')
            print(respostasMarcadas)
            return render(request, 'resultado.html', {'respostasMarcadas': respostasMarcadas})

    return HttpResponse('Faça seu Login.')