from django.db import models
from apps.usuario.models import Usuario, PuntajeUsuario
from apps.preguntas.models import Preguntas, ElegirRespuesta

# Create your models here.
class PreguntasRespondidas(models.Model):
    usuario = models.ForeignKey(PuntajeUsuario, on_delete = models.CASCADE)
    preguntas = models.ForeignKey(Preguntas, on_delete = models.CASCADE)
    respuesta = models.ForeignKey(ElegirRespuesta, on_delete = models.CASCADE, related_name = 'intentos')
    correcta = models.BooleanField(verbose_name = '¿Es esta la respuesta correcta?', default = False, null = False)
    puntaje_obtenido = models.DecimalField(verbose_name = 'Puntaje Obtenido', default = 0, decimal_places = 2, max_digits = 6)