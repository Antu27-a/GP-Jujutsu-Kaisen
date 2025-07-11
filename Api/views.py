from django.shortcuts import render,redirect
#--->Importamos la Libreria de Permisos
from django.contrib.auth.decorators import login_required
#--->Importamos la Libreria de Logout
from django.contrib.auth import logout,login,authenticate

from .models import *

from django.db.models import Q
# Create your views here.
from .forms import *


def Home(request):
    query=Productos.objects.all()
    data={
        'furm':query
    }
    return render(request,"index.html",data)

def cata(request):
    query=Productos.objects.all()
    data={
        'cat':query
    }
    return render(request, "admin.html", data)

def salir(request):
    logout(request)
    return redirect('Inicio')

def Register(request):
    data = {
        'regi':CustomUserCreationForm()
    }
    query= CustomUserCreationForm(data=request.POST)
    if query.is_valid():
        query.save()
        user= authenticate(username=query.cleaned_data['username'],password=query.cleaned_data['password1'])
        login(request, user)
        data["mensaje"]="hola"
        return redirect('Inicio')
    data['form']=query
    return render(request, 'registration/login.html',data)

@login_required
def Rega(request):
    data={
        'forma':FormularioProducto()
    }
    
    if request.method=='POST':
        query=FormularioProducto(data=request.POST,files=request.FILES)
        if query.is_valid():
            query.save()
            data['mensaje']="Datos Registrados"
        else:
            data['forma']=FormularioProducto
    return render(request,"pages/cargar-producto.html",data)