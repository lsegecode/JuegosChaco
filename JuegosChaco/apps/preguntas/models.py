from apps.categorias.models import Categoria
from django.db import models
from django.conf import settings
#from apps.usuario.models import Usuario, PuntajeUsuario

class Preguntas(models.Model):
     NUMERO_DE_RESPUESTAS_PERMITIDAS = 1
     
     consigna = models.TextField(verbose_name = 'Texto de la pregunta')
     categorias = models.ForeignKey(Categoria, related_name = 'la_categoria', on_delete = models.CASCADE)
    
     def __str__(self):
     	return self.consigna


class ElegirRespuesta(models.Model):

    MAXIMO_RESPUESTA = 3
    pregunta = models.ForeignKey(Preguntas, related_name = 'preguntas', on_delete = models.CASCADE)
    correcta = models.BooleanField(verbose_name = '¿Es esta la respuesta correcta?', default = False, null = False)
    texto = models.TextField(verbose_name = 'Texto de la respuesta')

    def __str__(self):
    	return self.texto

"""class Usuario (models.Model):
    usuario = models.OneToOneField(Usuario, on_delete= models.CASCADE)
    puntaje_total = models.DecimalField(verbose_name='Puntaje Total', default=0, decimal_places=2, max_digits=10)"""


"""class PreguntasRespondidas(models.Model):
    usuario = models.ForeignKey(PuntajeUsuario, on_delete=models.CASCADE)
    preguntas = models.ForeignKey(Preguntas, on_delete=models.CASCADE)
    respuesta = models.ForeignKey(ElegirRespuesta, on_delete=models.CASCADE, related_name = 'intentos')
    correcta = models.BooleanField(verbose_name='¿Es esta la respuesta correcta?',default=False, null= False)
    puntaje_obtenido = models.DecimalField(verbose_name='Puntaje Obtenido', default =0, decimal_places=2, max_digits=6)"""


# Create your models here.
