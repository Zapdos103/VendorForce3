from django.contrib import admin
from .models import *

class QuestaoFormulario(admin.StackedInline):
    model = Questao

class FormularioAdmin(admin.ModelAdmin):
    inlines = [QuestaoFormulario]

admin.site.register(Formulario, FormularioAdmin)

class RespostaQuestao(admin.StackedInline):
    model = Resposta

class QuestaoAdmin(admin.ModelAdmin):
    inlines = [RespostaQuestao]

admin.site.register(Categoria)
admin.site.register(Questao, QuestaoAdmin)
admin.site.register(Resposta)
admin.site.register(Resultado)