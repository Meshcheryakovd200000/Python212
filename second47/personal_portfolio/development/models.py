from django.db import models


# Create your models here.

class Development(models.Model):
    title = models.CharField(max_length=100)  # CharField - тип данных
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='development/images/')  # для загрузки картинки
    url = models.URLField(blank=True)  # blank=True - не обязательное для заполнения поле

    def __str__(self):  # возвращает строковое значение, чтобы в админке показывались названия
        return self.title
