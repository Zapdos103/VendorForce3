from .models import Candidato, Funcionario, Empresa
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404

def logout_usuario_por_email(email):
    pass
@receiver(post_save, sender=Funcionario)
def excluir_candidato(sender, instance, **kwargs):
    """
    Esta funcao irá excluir o candidato se este virar um funcionário.
    """
    try:
        email_funcionario = instance.email
        candidato = Candidato.objects.get(email=email_funcionario)
        candidato.delete()
        # TO-DO: adicionar a lógica da session
    except Candidato.DoesNotExist:
        HttpResponse(f'Erro: nenhum candidato com email {email_funcionario} encontrado.')


@receiver(post_delete, sender=Funcionario)
def excluir_funcionario(sender, instance, **kwargs):
    """
    Esta funcao irá transformar um funcionário em candidato caso este funcionário seja deletado.
    """
    try:
        # Criar o candidato
        candidato = Candidato(
            nome_completo = instance.nome,
            email = instance.email,
            senha = instance.senha,
            funcao = instance.funcao,
            telefone = instance.telefone,
        )
        candidato.save()
        # TO-DO: adicionar a lógica da session
        return redirect('/painel/home_empresa')
    except:
        return HttpResponse('Erro interno do sistema.')