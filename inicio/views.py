from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import Template
from datetime import timedelta



def index(request):
    return render(request, "index.html")

def sobre_mi(request):
    return render(request, "sobre_mi.html")


