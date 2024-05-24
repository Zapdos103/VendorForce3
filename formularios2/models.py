from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from empresas.models import Candidato, Funcionario
import uuid
import random

class BaseModel(models.Model):
    # Classe base com atributos de data e uid
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    data_criacao = models.DateField(auto_now=True)
    update = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class Formulario(BaseModel):
    nome = models.CharField(max_length=100)
    topico = models.CharField(max_length=100)
    qtd_perguntas = models.IntegerField()
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

class Categoria(BaseModel): # depois trocar para models.Model (exclua o banco de dados)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return str(self.nome)

class Questao(BaseModel):
    nome = models.CharField(max_length=100)
    formulario = models.ForeignKey(Formulario, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
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

class Resultado(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    formulario = models.ForeignKey(Formulario, on_delete=models.CASCADE)
    pontuacao = models.FloatField()
    frase = models.CharField(max_length=500)

    def __str__(self):
        return str(self.pk)

    def gerar_pdf(self):
        pass
@receiver(post_delete, sender=Resultado)
def update_status_questionario(sender, instance, **kwargs):
    funcionario = instance.funcionario
    if funcionario.status_questionario > 0:
        funcionario.status_questionario -= 1
        funcionario.save()