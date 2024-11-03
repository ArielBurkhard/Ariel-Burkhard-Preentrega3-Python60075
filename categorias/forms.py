from django import forms

class Formulario_speedrun_base(forms.Form):
    juegos_opciones = [
        ('Dark souls', 'Dark souls'),
        ('Hollow Knigth', 'Hollow Knigth'),
        ('GTA SA', 'GTA SA'),
      
    ]

    juego = forms.ChoiceField(choices=juegos_opciones)

class Formulario_speedrun(Formulario_speedrun_base):

    tiempo = forms.RegexField(
        regex=r'^(?P<hours>\d{1,2}):(?P<minutes>\d{2}):(?P<seconds>\d{2})$',
        error_messages={
            'invalid': 'Ingrese el tiempo en formato Hor:Min:Seg (por ejemplo, 01:30:45)',
        }
    )
    link = forms.URLField(max_length=80)
    
class Formulario_buscar_speedrun(Formulario_speedrun_base): ...

class Formulario_editar_speedun(Formulario_speedrun_base): 
    
    tiempo = forms.RegexField(
        regex=r'^(?P<hours>\d{1,2}):(?P<minutes>\d{2}):(?P<seconds>\d{2})$',
        error_messages={
            'invalid': 'Ingrese el tiempo en formato Hor:Min:Seg (por ejemplo, 01:30:45)',
        } 
    )
    link = forms.URLField(max_length=80)