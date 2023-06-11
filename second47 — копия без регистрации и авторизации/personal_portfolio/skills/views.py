from django.shortcuts import render
from .models import Skills


# Create your views here.

def index(request):
    projects = Skills.objects.all()  # достать из БД данные
    return render(request, 'skills/index.html', {'projects': projects})
