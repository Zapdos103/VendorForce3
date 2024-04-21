from django.urls import path
from . import views



urlpatterns = [
    path('home/', views.home, name='home'),
    path('api/get_formulario/', views.get_formulario, name='get_formulario'),
    path('formulario/', views.formulario, name='formulario'),

]