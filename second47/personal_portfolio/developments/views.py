from django.shortcuts import render
from .models import Developments
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required  # эта страница не должна показываться незаавторизованным пользователям
def developments(request):
    projects = Developments.objects.all()  # достать из БД данные
    return render(request, 'development/developments.html', {'projects': projects})
