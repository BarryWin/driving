from django.db import models

# Create your models here.

class Individ(models.Model):
    name = models.CharField('Имя')
    fam = models.CharField('Фамилия')
    otch = models.CharField('Отчество')
    date_rogd = models.DateField('Дата Рождения')