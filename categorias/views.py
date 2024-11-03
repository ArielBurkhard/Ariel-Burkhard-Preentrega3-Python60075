from django.shortcuts import render, redirect
from django.template import Template
from .models import Speedrun
from categorias.forms import Formulario_speedrun, Formulario_buscar_speedrun, Formulario_editar_speedun

def categorias(request):
    return render(request, "categorias.html")

def ver_speedrun(request, id):
    run = Speedrun.objects.get(id=id)
    return render(request, "categorias/ver_speedrun.html", {"run":run})

def eliminar_speedrun(request, id):
    run = Speedrun.objects.get(id=id)
    run.delete()
    return redirect("lista_de_speedruns")

def editar_speedrun(request, id):
    run = Speedrun.objects.get(id=id)
    formulario = Formulario_editar_speedun(initial={"juego": run.juego, "tiempo": run.tiempo, "link": run.link})
    if request.method == "POST":
        formulario = Formulario_editar_speedun(request.POST)
        if formulario.is_valid():
            run.juego = formulario.cleaned_data.get("juego")
            run.tiempo = formulario.cleaned_data.get("tiempo")
            run.link = formulario.cleaned_data.get("link")

            run.save()
            return redirect("lista_de_speedruns")
    return render(request, "categorias/editar_speedrun.html", {"run": run, "form": formulario})


def lista_de_speedruns(request):
    formulario = Formulario_buscar_speedrun(request.GET)
    run = Speedrun.objects.all()
    if formulario.is_valid():
        juego = formulario.cleaned_data.get("juego")
        run = Speedrun.objects.filter(juego=juego)
    else:
        run = Speedrun.objects.all()
    return render(request, "categorias/lista_de_speedruns.html", {"run": run, "form": formulario})

def speedrun(request):
    formulario = Formulario_speedrun()
    if request.method == "POST":
      formulario = Formulario_speedrun(request.POST)
      if formulario.is_valid():
          data = formulario.cleaned_data
          run = Speedrun(juego=data.get("juego"), tiempo=data.get("tiempo"), link=data.get("link"))
          run.save()
          return redirect("lista_de_speedruns")
    return render(request, "categorias/speedrun.html", {"form" : formulario})

def fighting_games(request):
    return render(request, "categorias/fighting_games.html")

def el_gamer_definitivo(request):
    return render(request, "categorias/el_gamer_definitivo.html")

def dragon_ball_bt3(request):
    return render(request, "lista_de_juegos/dragon_ball_bt3.html")

def mortal_kombat(request):
    return render(request, "lista_de_juegos/mortal_kombat.html")

def tekken(request):
    return render(request, "lista_de_juegos/tekken.html")


