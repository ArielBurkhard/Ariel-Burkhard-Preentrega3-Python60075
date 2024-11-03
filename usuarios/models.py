from django.db import models

class Usuario(models.Model):
    nick_name = models.CharField(max_length=40)
    e_mail = models.EmailField(max_length=254)  
    contrasenia = models.CharField(max_length=80)  
    def __str__(self):
        return f"{self.nick_name}"
