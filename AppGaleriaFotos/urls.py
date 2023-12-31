from django.urls import path
from .views import lista_imagenes, cargar_imagen, eliminar_imagen
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', lista_imagenes, name='lista_imagenes'),
    path('cargar-imagen/', cargar_imagen, name='cargar_imagen'),
    path('eliminar/<int:imagen_id>/', eliminar_imagen, name='eliminar_imagen'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)