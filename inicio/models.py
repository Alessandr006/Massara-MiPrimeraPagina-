from django.db import models

class publicacion(models.Model):
    nombre = models.CharField(max_length= 50)
    autor = models.CharField(max_length= 20)
    def __str__(self):
        return f'{self.nombre} - {self.autor}'
