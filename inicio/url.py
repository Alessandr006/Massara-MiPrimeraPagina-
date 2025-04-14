from django.urls import path
from inicio.views import inicio, crear_publicacion, lista_publicaciones
urlpatterns = [
    path('', inicio, name ='inicio'),
    path('publicaciones/', lista_publicaciones, name = 'lista de publicaciones'),
    path('crear/publicación/', crear_publicacion, name ='crear publicación'),
]