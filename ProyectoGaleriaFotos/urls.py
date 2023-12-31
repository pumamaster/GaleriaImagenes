from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AppGaleriaFotos.urls')),  # Ajusta 'mi_aplicacion' al nombre de tu aplicación
]