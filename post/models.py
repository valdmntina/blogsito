from django.db import models
from datetime import date

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=20)
    correo = models.EmailField(max_length=20)

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    cuerpo = models.TextField()
    fecha = models.DateField(default= date.today)
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE, null=True, blank=True, related_name="posteo") #blank false no almacena valores vacios 

