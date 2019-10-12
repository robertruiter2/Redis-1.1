from django.db import models

# Create your models here.

class Heroi(models.Model):
    nome = models.CharField('Nome', max_length=100)
    universo = models.CharField('Universo', max_length=100)
    habilidade = models.CharField('Habilidade', max_length=100)

    def __str__(self):
        return self.nome