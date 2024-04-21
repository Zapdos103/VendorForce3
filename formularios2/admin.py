from django.contrib import admin
from .models import *

admin.site.register(Formulario)

class RespostaAdmin(admin.StackedInline):
    model = Resposta

class QuestaoAdmin(admin.ModelAdmin):
    inlines = [RespostaAdmin]

admin.site.register(Categoria)
admin.site.register(Questao, QuestaoAdmin)
admin.site.register(Resposta)