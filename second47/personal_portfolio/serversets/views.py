from django.shortcuts import render
from .models import Serversets
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required  # эта страница не должна показываться незаавторизованным пользователям
def serversets(request):
    projects = Serversets.objects.all()  # достать из БД данные
    return render(request, 'serverset/serversets.html', {'projects': projects})
