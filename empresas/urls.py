from django.urls import path
from . import views

urlpatterns = [
    path('cadastro_landing/', views.cadastro_landing, name='cadastro_landing'),
    path('cadastro_funcionario/', views.cadastro_funcionario, name='cadastro_funcionario'),
    path('cadastro_completo/', views.cadastro_completo, name='cadastro_completo'),
    path('cadastro_candidato/', views.cadastro_candidato, name='cadastro_candidato'),
    path('login_usuario/', views.login_usuario, name='login_usuario'),
    path('login_empresa/', views.login_empresa, name='login_empresa'),
    path('logout_empresa/', views.logout_empresa, name='logout_empresa'),
    path('logout_usuario/', views.logout_usuario, name='logout_usuario'),
]