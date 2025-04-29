from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

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
    fecha_nacimiento = forms.DateField(widget= forms.DateInput(attrs={'type': 'date'}))
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "fecha_nacimiento", "avatar"]