# Generated by Django 3.0 on 2021-08-28 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0012_juegoschacousuario_preguntasrespondidas_preguntas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preguntasrespondidas_preguntas',
            name='juegoschacoUser',
        ),
        migrations.RemoveField(
            model_name='preguntasrespondidas_preguntas',
            name='pregunta',
        ),
        migrations.RemoveField(
            model_name='preguntasrespondidas_preguntas',
            name='respuesta',
        ),
        migrations.AddField(
            model_name='preguntas',
            name='max_puntaje',
            field=models.DecimalField(decimal_places=2, default=3, max_digits=6, verbose_name='Maximo Puntaje'),
        ),
        migrations.DeleteModel(
            name='JuegosChacoUsuario',
        ),
        migrations.DeleteModel(
            name='PreguntasRespondidas_preguntas',
        ),
    ]