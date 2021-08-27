from django.db.models.fields.related import ForeignKey
from apps.categorias.models import Categoria
from django.db import models
from django.conf import settings
from apps.usuario.models import Usuario, PuntajeUsuario

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


class Partida(models.Model):
    usuario = models.ForeignKey(Usuario, related_name = 'usuario', on_delete = models.CASCADE)
    categoria = models.ForeignKey(Categoria, related_name = 'categoria', on_delete = models.CASCADE)


class PreguntaPartida(models.Model):
    pregunta = models.ForeignKey(Preguntas, related_name = 'pregunta', on_delete = models.CASCADE)
    partida = models.ForeignKey(Partida, related_name = 'partida', on_delete = models.CASCADE)
    correcta = models.BooleanField(verbose_name = '¿Es esta la respuesta correcta?', default = False, null = False)


'''
#    [
# {
# "id":id_pregunta,
# "respuesta correctas":int
# "total contestadas": int
# }
# ]
'''
"""
en el endpoint de elegir respuesta
0) si la respuesta ya estaba contestada (verificar en metadata) redireccionar a las preguntas
1) ver si existe partida para esa categoria y usuario, sino crearla
2) verificar si la respuesta es correcta y agregar a metadata(lista) el diccionao
# {
# "id":id_pregunta,
# "respuesta correcta":bool
# }
3) guardar


"""

"""class Usuario (models.Model):
    usuario = models.OneToOneField(Usuario, on_delete= models.CASCADE)
    puntaje_total = models.DecimalField(verbose_name='Puntaje Total', default=0, decimal_places=2, max_digits=10)"""


"""class PreguntasRespondidas(models.Model):
    usuario = models.ForeignKey(PuntajeUsuario, on_delete=models.CASCADE)
    preguntas = models.ForeignKey(Preguntas, on_delete=models.CASCADE)
    respuesta = models.ForeignKey(ElegirRespuesta, on_delete=models.CASCADE, related_name = 'intentos')
    correcta = models.BooleanField(verbose_name='¿Es esta la respuesta correcta?',default=False, null= False)
    puntaje_obtenido = models.DecimalField(verbose_name='Puntaje Obtenido', default =0, decimal_places=2, max_digits=6)"""
