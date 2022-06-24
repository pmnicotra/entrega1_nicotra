from django.db import models

# Create your models here.
class Jugador(models.Model):
    apellido = models.CharField(max_length=20)
    camiseta = models.IntegerField()

class Tecnico(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    club = models.CharField(max_length=20)

class Club(models.Model):
    club = models.CharField(max_length=20)
    ligas = models.IntegerField()
    descensos = models.BooleanField()


