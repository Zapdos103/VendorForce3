from django.urls import path
from . import views


urlpatterns = [
    # Empresa
    path('home_empresa/', views.home_empresa, name='home_empresa'),
    path('dashboard_empresa/', views.dashboard_empresa, name='dashboard_empresa'),
    path('candidatos_empresa/', views.candidatos_empresa, name='candidatos_empresa'),
    path('config_empresa/', views.config_empresa, name='config_empresa'),
    path('excluir_funcionario/<int:funcionario_id>', views.excluir_funcionario, name='excluir_funcionario'),
    path('salvar_formularios/<int:funcionario_id>', views.salvar_formularios, name='salvar_formularios'),
    # Usuário -> 1) Candidato / 2) Funcionário
    path('home_usuario/', views.home_usuario, name='home_usuario'),
    path('perfil_funcionario/<int:funcionario_id>', views.perfil_funcionario, name='perfil_funcionario'),
]