from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()  # поле без ограничения колличества символов
    date = models.DateField()

    def __str__(self):  # возвращает строковое значение, чтобы в админке показывались названия блогов
        return self.title
























