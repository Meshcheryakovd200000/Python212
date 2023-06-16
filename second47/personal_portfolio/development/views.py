from django.shortcuts import render, get_object_or_404
from .models import Development
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required  # эта страница не должна показываться незаавторизованным пользователям
def development(request):
    developments = Development.objects.all()  # достать из БД данные
    return render(request, 'development/developments.html', {'developments': developments})


def detail(request, development):
    development = get_object_or_404(Development,
                                    pk=development)  # если данные существуют то будут попадать в переменную
    # development, если не существуют то ошибка 404
    return render(request, 'development/details.html', {'development': development})
