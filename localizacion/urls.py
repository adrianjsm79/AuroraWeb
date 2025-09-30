from django.urls import path
from .views import mapa_view

urlpatterns = [
    path('', mapa_view, name='index'),  # Esta línea hace que / muestre el mapa
    path('mapa/', mapa_view, name='mapa'),
]