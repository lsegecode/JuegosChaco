from django.db import models

# Create your models here.
'''
1.  CULTURA Y ARTE
2.	HISTORIA 
3.	DEPORTE
4.	GEOGRAFÍA 
5.	ECONOMÍA
6.	CIENCIA Y EDUCACIÓN 
7.	ENTRETENIMIENTO
'''

class Categoria(models.Model):
    nombre = models.CharField(max_length = 50)

    def __str__(self):
        return self.nombre
    def crear_intentos(self, pregunta):
        intento = PreguntasRespondidas(pregunta=pregunta, juegoschacoUser=self)
        intento.save()

    def obtener_nuevas_preguntas(self):
        respondidas = PreguntasRespondidas.objects.filter(juegoschacoUser=self).values_list('pregunta__pk', flat=True)
        preguntas_restantes = Pregunta.objects.exclude(pk__in=respondidas)
        if not preguntas_restantes.exists():
            return None
        return random.choice(preguntas_restantes)


    def validar_intento(self, pregunta_respondida, respuesta_selecionada):
        if pregunta_respondida.pregunta_id != respuesta_selecionada.pregunta_id:
            return

        pregunta_respondida.respuesta_selecionada = respuesta_selecionada
        if respuesta_selecionada.correcta is True:
            pregunta_respondida.correcta = True
            pregunta_respondida.puntaje_obtenido = respuesta_selecionada.pregunta.max_puntaje
            pregunta_respondida.respuesta = respuesta_selecionada

        else:
            pregunta_respondida.respuesta = respuesta_selecionada

        pregunta_respondida.save()

        self.actualizar_puntaje()

    def actualizar_puntaje(self):
        puntaje_actualizado = self.intentos.filter(correcta=True).aggregate(
            models.Sum('puntaje_obtenido'))['puntaje_obtenido__sum']

        self.puntaje_total = puntaje_actualizado
        self.save()
