from django.shortcuts import render
from django.views.generic.edit import CreateView
from usuarios.models import Usuario
from django.urls import reverse_lazy

class Registrarse(CreateView):
    model = Usuario
    template_name = "registrarse.html"
    success_url = reverse_lazy("categorias")
    fields = ("nick_name", "e_mail", "contrasenia") 


def ingresar(request):
    return render(request, "ingresar.html")