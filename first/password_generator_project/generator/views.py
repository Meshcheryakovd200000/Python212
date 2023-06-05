from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    lst = list(range(6, 15))  # [6, 7, 8, 9, 10, 11, 12, 13, 14]
    return render(request, 'generator/home.html', {'lst': lst})


def password(request):
    char = [chr(i) for i in range(97, 123)]  # получаем список букв, берем из таблицы кодировки символов ASCII
    if request.GET.get('uppercase'):
        char.extend([chr(i) for i in range(65, 91)])  # буквы верхнего регистра
    if request.GET.get('numbers'):
        char.extend([chr(i) for i in range(48, 58)])  # к генерируему паролю добавляютя цифры
    if request.GET.get('special'):
        char.extend([chr(i) for i in range(33, 48)])  # к генерируему паролю добавляютя спецсимволы
    print(char)
    length = int(request.GET.get('length'))
    psw = ''
    for i in range(length):
        psw += random.choice(char)
    return render(request, 'generator/password.html', {'password': psw})


def work_rules(request):
    return render(request, 'generator/work_rules.html')

# Create your views here.
