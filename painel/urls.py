from django.urls import path
from . import views


urlpatterns = [
    # Empresa
    path('home_empresa/', views.home_empresa, name='home_empresa'),
    path('dashboard_empresa/', views.dashboard_empresa, name='dashboard_empresa'),
    path('candidatos_empresa/', views.candidatos_empresa, name='candidatos_empresa'),
    path('config_empresa/', views.config_empresa, name='config_empresa'),
    path('gerenciar_funcionario/<int:funcionario_id>', views.gerenciar_funcionario, name='gerenciar_funcionario'),
    path('gerenciar_candidato/<int:candidato_id>', views.gerenciar_candidato, name='gerenciar_candidato'),
    # Usuário -> 1) Candidato / 2) Funcionário
    path('home_usuario/', views.home_usuario, name='home_usuario'),
    path('perfil/<int:usuario_id>', views.perfil, name='perfil'),
]