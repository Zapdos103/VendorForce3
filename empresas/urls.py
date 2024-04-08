from django.urls import path
from . import views

urlpatterns = [
    path('cadastro_landing/', views.cadastro_landing, name='cadastro_landing'),
    path('cadastro_funcionario/', views.cadastro_funcionario, name='cadastro_funcionario'),
    path('cadastro_completo/', views.cadastro_completo, name='cadastro_completo'),
    path('cadastro_candidato/', views.cadastro_candidato, name='cadastro_candidato'),
    path('login_empresa/', views.login_empresa, name='login_empresa'),
    path('login_funcionario/', views.login_funcionario, name='login_funcionario'),
    path('login_candidato/', views.login_candidato, name='login_candidato'),
    path('logout_empresa/', views.logout_empresa, name='logout_empresa'),
    path('logout_funcionario/', views.logout_funcionario, name='logout_funcionario'),
    path('logout_candidato', views.logout_candidato, name='logout_candidato')

]