# Generated by Django 3.1.4 on 2020-12-13 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reserva',
            unique_together={('data', 'hora_inicial', 'hora_final')},
        ),
    ]
