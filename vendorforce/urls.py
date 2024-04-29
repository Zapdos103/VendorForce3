from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('empresas.urls')),
    path('painel/', include('painel.urls')),
    path('formularios2/', include('formularios2.urls')),
    path('', lambda request: redirect('/auth/cadastro_completo')),
]