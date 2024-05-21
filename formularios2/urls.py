from django.urls import path
from . import views



urlpatterns = [
    path('home/', views.home, name='home'),
    path('api/get_formulario/', views.get_formulario, name='get_formulario'),
    path('formulario/', views.formulario, name='formulario'),
    path('resultado/', views.resultado, name='resultado'),
    path('resultado2/', views.resultado2, name='resultado2'),
    path('gerenciar_formularios/', views.gerenciar_formularios, name='gerenciar_formularios'),
    path('resultado_pdf/<int:resultado_id>', views.resultado_pdf, name='resultado_pdf')

]