from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    TIPO = (
        (0, 'Professor'),
        (1, 'Técnico')
    )

    matricula = models.CharField(max_length=11, unique=True)
    tipo = models.IntegerField(choices=TIPO, null=True)
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

class Reserva(models.Model):
    professor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    turma = models.CharField(max_length=50)
    data = models.DateField(blank=False, null=False)
    hora_inicial = models.TimeField(auto_now=False)
    hora_final = models.TimeField(auto_now=False)
    class Meta:
        unique_together = [['data', 'hora_inicial', 'hora_final']]

