from typing import Any
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Entidad(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30, default="Default")
    administrador = models.ForeignKey(User,on_delete=models.CASCADE, null=True)


    def __str__(self) -> str:
        return self.nombre
    
class Comunicador(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=30)
    detalle = models.CharField(max_length=400)
    detallecorto = models.CharField(max_length=30, default="Hola")
    TIPO_CHOICES = (
    ("S","Suspensión de actividades"),
    ("C","Suspensión de clases"),
    ("I","Información"),
    )
    tipo = models.CharField(max_length=10,choices=TIPO_CHOICES,default="I")
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE,editable=False, null=True)
    visible = models.BooleanField(default=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    fecha_ultima_modificacion = models.DateTimeField(auto_now=True)
    publicado_por = models.ForeignKey(User,on_delete=models.CASCADE, editable=False, null=True)
    modificado_por = models.ForeignKey(User,on_delete=models.CASCADE,related_name="modificado_por", editable=False, null=True)
    
    def __str__(self) -> str:
        return self.titulo