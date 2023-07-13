from django.shortcuts import render, redirect
from .models import Repair
from .forms import RepairForm


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


def create_repair(request):
    form = RepairForm()  # отрабатывает методом get

    # при нажатии на кнопку
    if request.method == 'POST':
        form = RepairForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # когда пользователь заполнит форму то перенаправим на главную страницу
            return redirect('repairs')

    context = {'form': form}
    return render(request, 'repairs/form-template.html', context)
