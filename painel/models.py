

from django.db import models
# from empresas.models import Empresa, Funcionario


class Status(models.Model):
    nome = models.CharField(max_length=50)

    def Meta(self):
        verbose_name_plural = 'Status'

    def __str__(self):
        return self.nome