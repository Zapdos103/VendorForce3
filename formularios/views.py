from django.shortcuts import render
from .models import Formulario, Questao, Resposta, Resultado
from empresas.models import Empresa, Funcionario, Candidato
from django.views.generic import ListView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
import logging

logger = logging.getLogger(__name__)

class FormularioListView(ListView):
    model = Formulario
    template_name = 'main.html'

def formulario_view(request, pk):
    formulario = Formulario.objects.get(pk=pk)
    texto_formulario = formulario.texto
    return render(request, 'formulario.html', {'formulario': formulario, 'texto_formulario': texto_formulario})

def formulario_data_view(request, pk):
    formulario = Formulario.objects.get(pk=pk)
    questoes = []
    for q in formulario.questoes():
        respostas = []
        for r in q.respostas():
            respostas.append(r.texto)
        questoes.append({str(q): respostas})

    return JsonResponse({
        'data': questoes,
        'tempo': formulario.tempo,

    })

@csrf_protect
def salvar_formulario(request, pk):
    print(request.POST)

    if request.is_ajax():
        questoes = []
        data = request.POST
        data_ = dict(data.lists())
        data_.pop('csrfmiddlewaretoken')

        for k in data_.keys():
            print('key', k)
            questao = Questao.objects.get(texto=k)
            questoes.append(questao)

        # definir o tipo de usuário...
        if request.session.get('funcionario'):
            usuario = Funcionario.objects.get(id=request.session['funcionario'])
        elif request.session.get('candidato'):
            usuario = Candidato.objects.get(id=request.session['candidato'])
        elif request.session.get('empresa'):
            usuario = Empresa.objects.get(id=request.session['empresa'])
        else:
            usuario = None

        formulario = Formulario.objects.get(pk=pk)

        pontuacao = 0
        multiplicador = 100/formulario.qtd_questoes
        resultados = []
        resposta_correta = None

        for q in questoes:
            resposta_selecionada = request.POST.get(q.texto)

            if resposta_selecionada != "":
                questao_respostas = Resposta.objects.filter(questao=q)
                for r in questao_respostas:
                    if resposta_selecionada == r.texto:
                        if r.acerto:
                            pontuacao += 1
                            resposta_correta = r.texto
                        else:
                            if r.acerto:
                                resposta_correta = r.texto
                resultados.append({str(q): {'resposta_correta': resposta_correta, 'resposta_selecionada': resposta_selecionada}})

            else:
                resultados.append({str(q): {'Sem resposta'}})

        pontuacao_ = pontuacao*multiplicador
        Resultado.objects.create(formulario=formulario, usuario=usuario, pontuacao=pontuacao_)

        # Retornar as frases de acordo com a pontuacao do usuario
        if pontuacao_ >= formulario.qtd_acertos:
            frase = 'Frase para quem acertou 12 questoes ou mais'
            return JsonResponse({'pontuação': pontuacao_, 'resultados': resultados, 'frase': frase})
        else:
            frase = 'Frase para quem acertou menos de 12 questoes'
            return JsonResponse({'pontuação': pontuacao_, 'resultados': resultados, 'frase': frase})
