from django.shortcuts import render,redirect
#--->Importamos la Libreria de Permisos
from django.contrib.auth.decorators import login_required
#--->Importamos la Libreria de Logout
from django.contrib.auth import logout

from .models import *

from django.db.models import Q
# Create your views here.

def Home(request):
    return render(request,"index.html")
