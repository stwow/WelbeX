from django.db import models


class Table(models.Model):
    date = models.DateField('Дата')
    title = models.CharField('Название', max_length=35)
    number = models.PositiveIntegerField('Количество')
    distance = models.PositiveIntegerField('Расстояние')

    def __str__(self):
        return self.title




