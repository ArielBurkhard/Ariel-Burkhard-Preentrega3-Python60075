from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import Template
from .models import Speedrun
from datetime import timedelta



def index(request):
    return render(request, "index.html")

def categorias(request):
    return render(request, "categorias.html")

def sobre_mi(request):
    return render(request, "sobre_mi.html")

def insc_speedrun(request, juego, horas, minutos, segundos, link):
    tiempo = timedelta(hours=horas, minutes=minutos, seconds=segundos)
    nuevo_speedrun = Speedrun(juego=juego, tiempo=tiempo, link=link)
    nuevo_speedrun.save()
    return redirect("lista_de_speedrruns")

def lista_de_speedruns(request):
    return render(request, "lista_de_speedruns.html")

def registrate(request):
    return render(request, "registrate.html")

def ingresa(request):
    return render(request, "ingresa.html")