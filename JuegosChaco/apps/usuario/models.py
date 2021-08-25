from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Usuario(AbstractUser):
	pass
	
class PuntajeUsuario (models.Model):
    usuario = models.OneToOneField(Usuario, on_delete= models.CASCADE)
    puntaje_total = models.DecimalField(verbose_name='Puntaje Total', default=0, decimal_places=2, max_digits=10)
