from django.shortcuts import render, redirect
from .models import Repair
from .forms import RepairForm
from django.contrib.auth.decorators import login_required


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


@login_required(login_url="login")
def create_repair(request):
    profile = request.user.profile
    form = RepairForm()  # отрабатывает методом get

    # при нажатии на кнопку
    if request.method == 'POST':
        form = RepairForm(request.POST, request.FILES)
        if form.is_valid():
            repair = form.save(commit=False)
            repair.owner = profile
            form.save()
            # когда пользователь заполнит форму то перенаправим на главную страницу
            return redirect('account')

    context = {'form': form}
    return render(request, 'repairs/form-template.html', context)


@login_required(login_url="login")
def update_repair(request, pk):
    profile = request.user.profile
    repair = profile.repair_set.get(id=pk)
    form = RepairForm(instance=repair)

    if request.method == "POST":
        form = RepairForm(request.POST, request.FILES, instance=repair)
        if form.is_valid():
            repair = form.save()
            return redirect('account')

    context = {'form': form}
    return render(request, 'repairs/form-template.html', context)


@login_required(login_url="login")
def delete_repair(request, pk):
    profile = request.user.profile
    repair = profile.repair_set.get(id=pk)

    if request.method == "POST":
        repair.delete()
        return redirect('repairs')

    context = {'object': repair}
    return render(request, 'repairs/delete.html', context)


















