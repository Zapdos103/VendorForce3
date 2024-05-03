from django.db import models
import uuid
import random

# Classe base com atributos de data
class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    data_criacao = models.DateField(auto_now=True)
    update = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class Formulario(BaseModel):
    nome = models.CharField(max_length=100)
    topico = models.CharField(max_length=100)
    qtd_perguntas = models.IntegerField()
    qtd_acertos = models.IntegerField(help_text='Pontuação realizada pelo usuário')
    tempo = models.IntegerField(help_text='Duração do teste em minutos')
    texto = models.CharField(max_length=300)

    def __str__(self):
        return str(self.nome)

    def get_questoes(self):
        questoes = Questao.objects.filter(formulario=self)
        data = []
        for q in questoes:
            data.append({
                'questao': q.nome,
                'qtd_respostas': q.qtd_resposta
            })
        return data

class Categoria(BaseModel):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return str(self.nome)

class Questao(BaseModel):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    formulario = models.ForeignKey(Formulario, on_delete=models.CASCADE)
    qtd_respostas = models.IntegerField(default=4)

    def __str__(self):
        return str(self.nome)

    def get_respostas(self):
        respostas = list(Resposta.objects.filter(questao=self))
        random.shuffle(respostas)
        data = []
        for r in respostas:
            data.append({
                'resposta': r.nome,
                'resposta_correta': r.resposta_correta,

            })

        return data

class Resposta(BaseModel):
    nome = models.CharField(max_length=100)
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
    resposta_correta = models.BooleanField(default=False)

    def __str__(self):
        return str(self.nome)
