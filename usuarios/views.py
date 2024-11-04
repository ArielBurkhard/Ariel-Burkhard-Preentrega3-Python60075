from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from usuarios.models import Usuario
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from usuarios.forms import Formulario_Registrarse

def registrarse(request):
    formulario = Formulario_Registrarse()
    if request.method == "POST":
        formulario = Formulario_Registrarse(request.POST) 
        if formulario.is_valid():
            formulario.save()
            return redirect("ingresar")
    return render(request, "registrarse.html", {"form": formulario})

def ingresar(request):
    
    formulario = AuthenticationForm()
    
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            nick_name = formulario.cleaned_data.get("username")
            contrasenia = formulario.cleaned_data.get("password")
            usuario = authenticate(username=nick_name, password=contrasenia) 
            login(request, usuario)
            return redirect("categorias")           
    return render(request, "ingresar.html", {"form": formulario})