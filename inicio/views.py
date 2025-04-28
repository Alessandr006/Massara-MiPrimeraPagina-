from django.shortcuts import render, redirect
from inicio.forms import creacion_publicacion
from inicio.models import publicacion
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, 'inicio/inicio.html')

@login_required
def crear_publicacion(request):
    print("Estos son los datos del GET:" ,request.GET)
    print("Estos son los datos del POST:", request.POST)
    if request.method == "POST":
        formulario = creacion_publicacion(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            Publicacion = publicacion(titulo = info.get("titulo"), autor = info.get("autor"), fecha_publicacion = info.get("fecha_publicacion"))
            Publicacion.save()
            return redirect("lista de publicaciones")
    else:
        formulario = creacion_publicacion()
    return render(request, "inicio/crear_publicacion.html", {"formulario": formulario })

def lista_publicaciones(request):
    publicaciones = publicacion.objects.all()
    return render(request, "inicio/lista_publicaciones.html", {"publicaciones": publicaciones})

class detallePublicacion(DetailView):
    model = publicacion
    template_name = "inicio/detalle_publicacion.html"

class modificarPublicacion(LoginRequiredMixin, UpdateView):
    model = publicacion
    template_name = "inicio/modificar_publicacion.html"
    fields = ["titulo", "autor"]
    success_url = reverse_lazy("lista de publicaciones")

class eliminarPublicacion(LoginRequiredMixin, DeleteView):
    model = publicacion
    template_name = "inicio/eliminar_publicacion.html"
    success_url = reverse_lazy("lista de publicaciones")
