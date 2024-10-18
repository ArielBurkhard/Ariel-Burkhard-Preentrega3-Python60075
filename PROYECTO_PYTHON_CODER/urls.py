"""
URL configuration for PROYECTO_PYTHON_CODER project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicio.views import index, categorias, sobre_mi, lista_de_speedruns, insc_speedrun, registrate, ingresa


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="inicio"),
    path("categorias/", categorias, name="categorias"),
    path("sobre_mi/", sobre_mi, name="sobre_mi"),
    path("lista_de_speedrun/", lista_de_speedruns, name="lista_de_speedruns"),
    path('insc_speedrun/<str:juego>/<int:horas>/<int:minutos>/<int:segundos>/<str:link>/', insc_speedrun, name='insc_speedrun'),
    path("registrate/", registrate, name="registrate"),
    path("ingresa/", ingresa, name="ingresa"),

]
