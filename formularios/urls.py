from django.urls import path
from .views import(
    FormularioListView,
    formulario_view,
    formulario_data_view,
    salvar_formulario,
)

urlpatterns = [
    path('', FormularioListView.as_view(), name='FormularioListView'),
    path('<pk>/', formulario_view, name='formulario_view'),
    path('<pk>/data/', formulario_data_view, name='formulario_data_view'),
    path('<pk>/salvar/', salvar_formulario, name='salvar_formulario'),
]