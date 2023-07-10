from django.shortcuts import render
from .models import Repair


# Create your views here.

def repairs(request):
    pr = Repair.objects.all()
    context = {
        'repairs': pr  # придумаем ключ
    }
    return render(request, 'repairs/repairs.html', context)


def repair(request, pk):
    project_obj = Repair.objects.get(id=pk)
    return render(request, 'repairs/single-repair.html', {'repair': project_obj})


























