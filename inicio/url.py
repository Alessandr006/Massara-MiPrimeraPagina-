from django.urls import path
from inicio.views import inicio, crear_publicacion, lista_publicaciones, detalle_publicacion
urlpatterns = [
    path('', inicio, name ='inicio'),
    path('publicación/', lista_publicaciones, name = 'lista de publicaciones'),
    path('publicación/crear/', crear_publicacion, name ='crear publicación'),
    path('publicación/<int:publicacion_especifica>/', detalle_publicacion, name ='detalles de publicacion'),
]