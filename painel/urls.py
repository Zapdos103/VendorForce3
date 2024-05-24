from django.urls import path
from . import views
# from empresas import views as views_empresa


urlpatterns = [
    # Empresa
    path('home_empresa/', views.home_empresa, name='home_empresa'),
    path('dashboard_empresa/', views.dashboard_empresa, name='dashboard_empresa'),
    path('candidatos_empresa/', views.candidatos_empresa, name='candidatos_empresa'),
    path('relatorios/', views.relatorios, name='relatorios'),
    path('config_empresa/', views.config_empresa, name='config_empresa'),
    path('gerenciar_funcionario/<int:funcionario_id>', views.gerenciar_funcionario, name='gerenciar_funcionario'),
    path('gerenciar_candidato/<int:candidato_id>', views.gerenciar_candidato, name='gerenciar_candidato'),
    # path('chamar_logout_empresa', views_empresa.logout_empresa, name='chamar_logout_empresa'),

    # Usuário -> 1) Candidato / 2) Funcionário
    path('home_usuario/', views.home_usuario, name='home_usuario'),
    path('perfil/<int:usuario_id>', views.perfil, name='perfil')
]