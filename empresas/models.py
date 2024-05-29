
from django.db import models
from django.utils.safestring import mark_safe
from datetime import datetime
from datetime import timedelta

# Create your models here.

SETOR_CHOICES = (
    ('V', 'Varejo'),
    ('A', 'Atacado'),
    ('S', 'Serviço'),
    ('T', 'Tecnologia'),
    ('I', 'Industria'),
    ('Outro', 'Outro')
)

VENDEDORES_CHOICES = (
    ('1-5', 'De 01 a 05'),
    ('6-10', 'De 06 a 10'),
    ('11-15', 'De 11 a 15'),
    ('16-30', 'De 16 a 30'),
    ('30+', 'Acima de 30')
)

CARGO_CHOICES = (
    ('S', 'Sócio/Proprietário'),
    ('CEO', 'CEO'),
    ('GC', 'Gestor Comercial'),
    ('GR', 'Gestor RH'),
    ('BP', 'Bussiness Partner RH'),
    ('V', 'Vendedor')
)

SEGMENTO_CHOICES = (
    ('A', 'Alimentação'),
    ('T', 'Transporte'),
    ('Cons', 'Consultoria'),
    ('V', 'Vestuário'),
    ('PE', 'Peças e Equipamentos'),
    ('M', 'Manutenção'),
    ('Q', 'Química'),
    ('F', 'Farmaceutica'),
    ('Cosm', 'Cosmético'),
    ('E', 'Educação'),
    ('O', 'Outro')
)

FUNCAO_CHOICES = (
    ('', ''),
)

class Empresa(models.Model):
    premium = models.BooleanField(default=False)
    razao_social = models.CharField(max_length=100, blank=False)
    nome = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    setor = models.CharField(max_length=10, choices=SETOR_CHOICES)
    qtd_vendedores = models.CharField(max_length=10, choices=VENDEDORES_CHOICES)
    cargo = models.CharField(max_length=10, choices=CARGO_CHOICES)
    telefone = models.CharField(max_length=11, blank=False)
    segmento = models.CharField(max_length=10,choices=SEGMENTO_CHOICES)
    senha = models.CharField(max_length=100, blank=False)
    repetir_senha = models.CharField(max_length=100, blank=False)
    CEP = models.CharField(max_length=8)
    CNPJ = models.CharField(max_length=11)
    endereco_cobranca = models.CharField(max_length=100)
    contato_financeiro = models.CharField(max_length=100)
    telefone_financeiro = models.CharField(max_length=11)

    def __str__(self):
        return self.nome

    def badge_template(self):
        pass

class Funcionario(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    senha = models.CharField(max_length=100)
    funcao = models.CharField(max_length=10, blank=False)
    telefone = models.CharField(max_length=11, blank=False)
    # nascimento = models.DateField()
    # formacao academica
    status_questionario = models.IntegerField(default=0)
    # ultimo_envio = models.DateField(null=True)


    def __str__(self):
        return self.email

    @property
    def verificar_status(self):
        # TO-DO: malear de acordo com o número de formulários
        return True if self.status_questionario == 6 else False
    @property
    def idade(self):
        # return timezone.now() - self.nascimento
        pass

    def badge_template(self):
        if self.status_questionario == 6:
            classes = 'success'
            texto = 'Finalizado'
        elif 0 < self.status_questionario < 6:
            classes = 'warning'
            texto = 'Em andamento'
        else:
            classes = 'secondary'
            texto = 'Pedente'
        return mark_safe(f'<span class="badge rounded-pill bg-{classes}">{texto}</span>')

class Candidato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=100)
    funcao = models.CharField(max_length=10)
    telefone = models.CharField(max_length=11)
    # nascimento = models.DateField()
    # formacao academica
    status_questionario = models.IntegerField(default=0)
    # ultimo_envio = models.DateField(null=True)

    def __str__(self):
        return self.email

    @property
    def verificar_status(self):
        pass

    @property
    def idade(self):
        pass

    def badge_template(self):
        pass