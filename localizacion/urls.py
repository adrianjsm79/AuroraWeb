from django.urls import path
from .views import mapa_view, index_redirect

urlpatterns = [
    path('', index_redirect, name='index'),  # Redirige / a /mapa/
    path('mapa/', mapa_view, name='mapa'),
]