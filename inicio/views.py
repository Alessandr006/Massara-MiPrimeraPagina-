from django.shortcuts import render, redirect
from inicio.forms import creacion_publicacion
from inicio.models import publicacion

def inicio(request):
    return render(request, 'inicio/inicio.html')

def crear_publicacion(request):
    print("Estos son los datos del GET:" ,request.GET)
    print("Estos son los datos del POST:", request.POST)
    if request.method == "POST":
        formulario = creacion_publicacion(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            Publicacion = publicacion(nombre = info.get("nombre"), autor = info.get("autor"))
            Publicacion.save()
            return redirect("lista de publicaciones")
    else:
        formulario = creacion_publicacion()
    return render(request, 'inicio/crear_publicacion.html', {"formulario": formulario })

def lista_publicaciones(request):
    publicaciones = publicacion.objects.all()
    return render(request, 'inicio/lista_publicaciones.html', {'publicaciones': publicaciones})