from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login
from usuario.forms import formulario_registro, formulario_editar_perfil
from django.contrib.auth.decorators import login_required
from usuario.models import info_extra

def login(request):
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            django_login(request, usuario)
            info_extra.objects.get_or_create(user = usuario)
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
    info_extra = request.user.info_extra
    if request.method == "POST":
        formulario = formulario_editar_perfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            if formulario.cleaned_data.get('avatar'):
                info_extra.avatar = formulario.cleaned_data.get('avatar')
            info_extra.save()
            formulario.save()
            return redirect("login")
    else:
        formulario = formulario_editar_perfil(initial={'avatar': info_extra.avatar}, instance=request.user)
    return render(request, "usuario/editar_perfil.html", {'formulario': formulario})