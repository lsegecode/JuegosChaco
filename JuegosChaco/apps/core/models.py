from django.db import models

# Create your models here.

class TimeModel(models.Model):
    creado = models.DateTimeField(auto_now_add=True,
                                  verbose_name=u'creado',
                                  help_text=u'Fecha de creación')
    modificado = models.DateTimeField(auto_now=True,
                                      verbose_name=u'modificado',
                                      help_text=u'Fecha de modificación')

    class Meta:
        abstract = True
