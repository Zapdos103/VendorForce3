from django.urls import path
from . import views
# from empresas import views as views_empresa

urlpatterns = [
    # Empresa
    path('home_empresa/', views.home_empresa, name='home_empresa'),
    path('dashboard_empresa/', views.dashboard_empresa, name='dashboard_empresa'),
    path('candidatos_empresa/', views.candidatos_empresa, name='candidatos_empresa'),
    path('relatorios_empresa/', views.relatorios_empresa, name='relatorios_empresa'),
    path('config_empresa/', views.config_empresa, name='config_empresa'),
    # path('chamar_logout_empresa', views_empresa.logout_empresa, name='chamar_logout_empresa'),

    # Funcionário
    path('home_funcionario/', views.home_funcionario, name='home_funcionario'),
    path('home_candidato/', views.home_candidato, name='home_candidato'),

    # Candidato
]