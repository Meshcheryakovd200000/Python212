from django.shortcuts import render
from .models import Repair


# Create your views here.

def repairs(request):
    pr = Repair.objects.all()
    context = {
        'repairs': pr  # придумаем ключ
    }
    return render(request, 'repairs/repairs.html', context)


















