from django.urls import path   
from categorias.views import (categorias,
                              lista_de_speedruns,
                              dragon_ball_bt3,
                              mortal_kombat,
                              speedrun,
                              fighting_games,
                              el_gamer_definitivo,
                              tekken,
                              ver_speedrun,
                              eliminar_speedrun,
                              editar_speedrun
                            )
   
urlpatterns = [   
   
    path("categorias/", categorias, name="categorias"),
    path("speedrun/", speedrun, name="speedrun"),
    path("lista_de_speedruns/", lista_de_speedruns, name="lista_de_speedruns"),
    path("ver_speedrun/<int:id>/", ver_speedrun, name="ver_speedrun"),
    path("eliminar_speedrun/<int:id>/", eliminar_speedrun, name="eliminar_speedrun"),
    path("editar_speedrun/<int:id>/", editar_speedrun, name="editar_speedrun"),
    path("fighting_games/", fighting_games, name="fighting_games"),
    path("dragon_ball_bt3/", dragon_ball_bt3, name="dragon_ball_bt3"),
    path("mortal_kombat/", mortal_kombat, name="mortal_kombat"),
    path("tekken/", tekken, name="tekken"),
    path("el_gamer_definitivo/", el_gamer_definitivo, name="el_gamer_definitivo"),
]