from django.db import models
from django.contrib.auth.models import User


# Create your models here. БД

class Todo(models.Model):  # это куда будут сохраняться данные задачи
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)  # чтобы сделать поле не обязательное для заполнения 'blank=True'
    created = models.DateTimeField(auto_now_add=True)  # когда поставили задачу
    date_completed = models.DateTimeField(blank=True, null=True)  # когда выполнили задачу, поле может быть пустое
    important = models.BooleanField(default=False)  # задача важная или нет
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # внешний ключ,

    def __str__(self):
        return self.title
