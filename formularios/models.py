
from django.db import models
from empresas.models import Funcionario
from datetime import date
import random

class Formulario(models.Model):
    nome = models.CharField(max_length=120)
    topico = models.CharField(max_length=120)
    qtd_questoes = models.IntegerField()
    tempo = models.IntegerField(help_text='Duração do teste em minutos')
    qtd_acertos = models.IntegerField(help_text='Pontuação realizada pelo usuário %')
    texto = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.nome}--{self.topico}'

    def questoes(self):
        questoes = list(self.questao_set.all())
        random.shuffle(questoes)
        return questoes[:self.qtd_questoes]

class Questao(models.Model):
    texto = models.CharField(max_length=120)
    formulario = models.ForeignKey(Formulario, on_delete=models.CASCADE)
    data_criacao = models.DateField(default=date.today)

    def __str__(self):
        return str(self.texto)

    def respostas(self):
        return self.resposta_set.all()

class Resposta(models.Model):
    texto = models.CharField(max_length=120)
    acerto = models.BooleanField(default=False)
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
    data_criacao = models.DateField(default=date.today)

    def __str__(self):
        return f'questão: {self.questao.texto} resposta: {self.texto}, acerto: {self.acerto}'

class Resultado(models.Model):
    formulario = models.ForeignKey(Formulario, on_delete=models.CASCADE)
    usuario = models.CharField(max_length=200, default=None)
    pontuacao = models.FloatField()

    def __str__(self):
        return str(self.pk)