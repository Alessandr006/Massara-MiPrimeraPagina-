from django.db import models

class publicacion(models.Model):
    titulo = models.CharField(max_length= 50)
    autor = models.CharField(max_length= 20)
    fecha_publicacion = models.DateField(null= True)
    imagen = models.ImageField(upload_to= "imagenes", null=True, blank=True)
    def __str__(self):
        return f'{self.titulo} - {self.autor} - {self.fecha_publicacion}'
