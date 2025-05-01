from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login
from usuario.forms import formulario_registro, formulario_editar_perfil, formulario_info_extra
from django.contrib.auth.decorators import login_required
from usuario.models import info_extra

def login(request):
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            django_login(request, usuario)
            info_extra.objects.get_or_create(user=usuario)
            return redirect("inicio")
    else:
        formulario = AuthenticationForm()
    return render(request, "usuario/login.html", {'formulario': formulario})

def registro(request):
    if request.method == "POST":
        formulario = formulario_registro(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("login")
    else:
        formulario = formulario_registro()
    return render(request, "usuario/registro.html", {'formulario': formulario})

@login_required
def editar_perfil(request):
    user = request.user
    informacion_extra, created = info_extra.objects.get_or_create(user=user)
    if request.method == "POST":
        formulario = formulario_editar_perfil(request.POST, instance=request.user)
        formulario_informacion = formulario_info_extra(request.POST, request.FILES, instance=informacion_extra)
        if formulario.is_valid() and formulario_informacion.is_valid(): 
            informacion_extra.save()
            formulario_informacion.save()
            formulario.save()
            return redirect("detalle perfil")
    else:
        formulario = formulario_editar_perfil( instance=request.user)
        formulario_informacion = formulario_info_extra(instance=informacion_extra)
    return render(request, "usuario/editar_perfil.html", {
        'formulario': formulario,
        'formulario_informacion': formulario_informacion
    })

def detalle_perfil(request):
    user = request.user
    informacion_extra = info_extra.objects.get(user=user)
    return render(request, "usuario/detalle_perfil.html", {
        'usuario': user,
        'informacion_extra': informacion_extra
    })