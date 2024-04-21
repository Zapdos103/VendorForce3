from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('empresas.urls')),
    path('painel/', include('painel.urls')),
    path('formularios2/', include('formularios2.urls')),
]