from django import forms

class creacion_publicacion(forms.Form):
    nombre = forms.CharField(max_length= 50)
    autor = forms.CharField(max_length= 20)
