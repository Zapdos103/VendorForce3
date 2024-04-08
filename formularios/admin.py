from django.contrib import admin
from .models import Resultado, Formulario, Questao, Resposta

admin.site.register(Resultado)
admin.site.register(Formulario)


class RespostaInLine(admin.TabularInline):
    model = Resposta

class QuestaoAdmin(admin.ModelAdmin):
    model = [RespostaInLine]

admin.site.register(Questao, QuestaoAdmin)
admin.site.register(Resposta)
