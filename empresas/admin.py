from django.contrib import admin
from .models import Empresa, Funcionario, Candidato
from formularios2.models import Resultado
# Register your models here.

admin.site.register(Empresa)

class ResultadoAdmin(admin.StackedInline):
    model = Resultado

class FuncionarioAdmin(admin.ModelAdmin):
    inlines = [ResultadoAdmin]

admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Candidato)
