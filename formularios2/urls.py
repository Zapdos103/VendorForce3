from django.urls import path
from . import views



urlpatterns = [
    path('api/get_formulario/', views.get_formulario, name='get_formulario'),
    path('formulario/', views.formulario, name='formulario'),
    path('coletar_respostas/', views.coletar_respostas, name='coletar_respostas'),
    path('gerenciar_formularios/', views.gerenciar_formularios, name='gerenciar_formularios'),
    path('resultado/<int:funcionario_id>', views.resultado, name='resultado'),
    path('coletar_resultado/<int:funcionario_id>', views.coletar_resultado, name='coletar_resultado'),
    path('gerar_pdf/<int:funcionario_id>', views.gerar_pdf, name='gerar_pdf'),
]