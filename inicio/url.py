from django.urls import path
from inicio.views import inicio, crear_publicacion, lista_publicaciones, detallePublicacion, modificarPublicacion, eliminarPublicacion 
urlpatterns = [
    path('', inicio, name ='inicio'),
    path('publicación/', lista_publicaciones, name = 'lista de publicaciones'),
    path('publicación/crear/', crear_publicacion, name ='crear publicación'),
    path('publicación/<int:pk>/', detallePublicacion.as_view(), name ='detalles de publicación'),
    path('publicación/<int:pk>/modificar', modificarPublicacion.as_view(), name ='modificar publicación'),
    path('publicación/<int:pk>/eliminar', eliminarPublicacion.as_view(), name ='eliminar publicación'),
]