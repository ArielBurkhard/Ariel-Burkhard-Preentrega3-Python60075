from django.urls import path
from usuarios import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
            path("registrarse/", views.registrarse, name="registrarse"),
            path("ingresar/", views.ingresar, name="ingresar"),
            path("cerrar_sesion/", LogoutView.as_view(template_name="index.html"), name="cerrar_sesion"),
            path("editar_perfil/", views.editar_perfil, name="editar_perfil")

    
]