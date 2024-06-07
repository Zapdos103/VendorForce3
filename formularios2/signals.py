from .models import Resultado
from empresas.models import Candidato, Funcionario
from django.db.models.signals import post_delete
from django.dispatch import receiver

@receiver(post_delete, sender=Resultado)
def update_status_questionario(sender, instance, **kwargs):
    funcionario = instance.funcionario
    if funcionario.status_questionario > 0:
        funcionario.status_questionario -= 1
        funcionario.save()