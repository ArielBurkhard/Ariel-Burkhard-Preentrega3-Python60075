from django.urls import path
from usuarios import views

urlpatterns = [
    
            path("registrarse/", views.Registrarse.as_view(), name="registrarse"),
            path("ingresa/", views.ingresar, name="ingresar"),

    
]