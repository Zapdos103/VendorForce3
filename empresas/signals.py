from .models import Candidato, Funcionario
from django.db.models.signals import pre_init
from django.dispatch import receiver

#@receiver(pre_init, sender=Funcionario)
#def excluir_candidato(sender, instance, **kwargs):
"""
    Esta funcao irá excluir o candidato se este virar um funcionário.
    Atualmente ela não está sendo utilizada.
    """
    # Candidato.objects.get(email=instance.email).delete()