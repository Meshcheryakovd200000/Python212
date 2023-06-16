from django.shortcuts import render, get_object_or_404
from .models import Serversetup


# Create your views here.

def serversetup(request):
    serversetups = Serversetup.objects.all()  # достать из БД данные
    return render(request, 'serversetup/serversetup.html', {'serversetups': serversetups})


def detail(request, serversetup):
    serversetup = get_object_or_404(Serversetup,
                                    pk=serversetup)  # если данные существуют то будут попадать в переменную
    # serversetup, если не существуют то ошибка 404
    return render(request, 'serversetup/details.html', {'serversetup': serversetup})


















