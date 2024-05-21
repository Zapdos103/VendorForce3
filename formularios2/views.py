from django.shortcuts import render, redirect
from django.http.response import HttpResponse, JsonResponse
from .models import *
from empresas.models import Candidato, Funcionario
import random
from django.http import HttpResponse, FileResponse
#from weasyprint import HTML
# import tempfile
from django.template.loader import render_to_string

"""Segunda tentativa de criar os invenários"""

def home(request):
    contexto = {
                'formularios': Formulario.objects.all(),
                'exibir_navbar': True,
                'contexto_app': 'formularios2'}
    if request.GET.get('formulario'):
        return redirect(f'/formularios2/formulario/?formulario={request.GET.get("formulario")}')

    return render(request, 'home.html', contexto)

def formulario(request):
    # formulario = Formulario.objects.get(id=formulario_id)
    # nome_formulario = formulario.nome
    contexto = {'categoria': request.GET.get('categoria'),
                'formulario': request.GET.get('formulario'),
                'exibir_navbar': True,
                'contexto_app': 'formularios2'}

    return render(request, 'formulario.html', contexto)

def get_formulario(request):
    try:
        questoes = Questao.objects.all()
        # formularios = Formulario.objects.all()
        if request.GET.get('formulario'):
            print(request.GET.get('formulario'))
            questoes = questoes.filter(formulario__nome__icontains=request.GET.get("formulario"))
        questoes = list(questoes)
        data = []
        random.shuffle(questoes)

        for q in questoes:
            data.append({
                'uid': q.uid,
                'nome': q.nome,
                'formulario': q.formulario.nome,
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

def gerenciar_formularios(request):
    exibir_navbar = True
    formularios = Formulario.objects.all()
    print(formularios)
    return render(request, 'gerenciar_formularios.html', {'exibir_navbar': exibir_navbar, 'formularios': formularios})
def resultado(request):
    contexto = {'exibir_navbar': False,
                'contexto_app': 'formularios2'}

    # Aplicar essa lógica ao formulario depois
    if not (request.session.get('candidato') or request.session.get('funcionario')):
        return HttpResponse('Faça seu Login.')

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
        categorias = ['Estilos de Vendas', 'Locus de Controle', 'Atitudes Profissionais', 'Técnicas de Vendas', 'Negociação', 'Matemática Básica']
        print(resultados)
        print(respostas_ids)
        # Renderização
        return render(request, 'resultado.html', {'resultados': resultados}) # passar o usuário

def resultado2(request):
    # Tratamento das respostas
    pontuacao = 0
    resultado = 0
    if request.session.get('candidato'):
            candidato = Candidato.objects.get(id=request.session['candidato'])
            funcionario = None
    elif request.session.get('funcionario'):
            funcionario = Funcionario.objects.get(id=request.session['funcionario'])
            candidato = None
    else:
        funcionario = None
        candidato = None
    if request.method == 'GET':
        return render(request, 'formulario.html')

    elif request.method == 'POST':

        respostasMarcadas = request.POST.get('respostasMarcadas') # <-- coletando as respostas do html do formulario

        """
        Aqui ficara todo o traramento dos resultados que o usuario obteve apos enviar o formulario
        """
        # Renderizar a página resultado_pdf.html como string
        #html_string = render_to_string('resultado_pdf.html', {'respostasMarcadas': respostasMarcadas})
        #pdf = HTML(string=html_string).write_pdf()

        resultado = Resultado(
            candidato=candidato,
            funcionario=funcionario,
            pontuacao=pontuacao,
            #resultado=pdf,
        )
        resultado.save()
        return render(request, 'resultado.html', {'respostasMarcadas': respostasMarcadas})

def resultado_pdf(request, resultado_id):

    return render(request, 'resultado_pdf.html')