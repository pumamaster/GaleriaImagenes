from django.shortcuts import render, redirect
from .models import Imagen
from .forms import ImagenForm

def lista_imagenes(request):
    imagenes = Imagen.objects.all()
    return render(request, 'lista_imagenes.html', {'imagenes': imagenes})

def cargar_imagen(request):
    if request.method == 'POST':
        form = ImagenForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_imagenes')
    else:
        form = ImagenForm()
    return render(request, 'cargar_imagen.html', {'form': form})

def eliminar_imagen(request, imagen_id):
    archivo=Imagen.objects.get(pk=imagen_id)
    if archivo:
        archivo.delete()
    return redirect('lista_imagenes')