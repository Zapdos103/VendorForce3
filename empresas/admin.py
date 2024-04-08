from django.contrib import admin
from .models import Empresa, Funcionario, Candidato
from painel.models import Status
# Register your models here.

admin.site.register(Empresa)
admin.site.register(Funcionario)
admin.site.register(Candidato)
admin.site.register(Status)