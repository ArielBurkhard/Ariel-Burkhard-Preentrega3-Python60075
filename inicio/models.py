from django.db import models

class Speedrun(models.Model):
    juego = models.CharField(max_length=40)
    tiempo = models.DurationField()
    link = models.CharField(max_length=80)
    def __str__(self):
        return f"{self.juego} - {self.tiempo}"
