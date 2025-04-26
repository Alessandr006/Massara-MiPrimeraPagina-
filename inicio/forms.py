from django import forms

class creacion_publicacion(forms.Form):
    titulo = forms.CharField(max_length= 50)
    autor = forms.CharField(max_length= 20)
    fecha_publicacion = forms.DateField(widget= forms.DateInput(attrs={'type': 'date'}))
