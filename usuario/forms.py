from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from usuario.models import info_extra

class formulario_registro(UserCreationForm):
    username = forms.CharField(label="Usuario")
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repertir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_text = {llave: "" for llave in fields}

class formulario_editar_perfil(UserChangeForm):
    password = None
    email = forms.EmailField(required=False)
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]

class formulario_info_extra(forms.ModelForm):
    hobbie = forms.CharField(label="hobbie")
    avatar = forms.ImageField(required=False)

    class Meta:
        model = info_extra
        fields = ['hobbie', 'avatar']
