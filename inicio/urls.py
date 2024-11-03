from django.urls import path
from inicio import views

urlpatterns = [
    
    
path("", views.index, name="inicio"),
path("sobre_mi/", views.sobre_mi, name="sobre_mi"),




]