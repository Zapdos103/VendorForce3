from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('empresas.urls')),
    path('painel/', include('painel.urls')),
    path('formularios/', include('formularios.urls')),
]