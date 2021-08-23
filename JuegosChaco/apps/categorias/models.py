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
    
