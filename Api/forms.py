from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

class FormularioProducto(forms.ModelForm):
    class Meta:
        model=Productos
        fields='__all__'

class CustomUserCreationForm(UserCreationForm):
    pass