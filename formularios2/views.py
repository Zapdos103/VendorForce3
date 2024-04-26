from django.shortcuts import render, redirect
from django.http.response import HttpResponse, JsonResponse
from .models import *
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
                'categoria': q.categoria.nome,
                'qtd_respostas': q.qtd_respostas,
                'respostas': q.get_respostas(),
            })
        payload = {'status': True, 'data': data}

        return JsonResponse(payload)

    except Exception as e:
        print(e)

    return HttpResponse('Erro inesperado.')
