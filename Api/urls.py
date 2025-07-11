from django.urls import path
from .views import *

urlpatterns = [
    path('',Home,name='Inicio'),
    path('logouts/',salir,name='logouts'),
    path('registrar/',Rega,name='regis'),
    path('catalogo/',cata,name='Catalogo'),
]