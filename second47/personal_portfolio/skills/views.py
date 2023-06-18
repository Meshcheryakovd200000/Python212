from django.shortcuts import render, redirect
from .models import Skills

# ---------------
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    projects = Skills.objects.all()  # достать из БД данные
    return render(request, 'skills/index.html', {'projects': projects})


# -------------------------------------------

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:  # если пароль и подтверждение пароля совпадают,
            # то сохраняем введенные данные c формы
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)  # чтобы пользователь залогинился на сайте автоматически
                return redirect('currenttodos')  # перенаправление на страницу
            except IntegrityError:
                return render(request, 'todo/signupuser.html',
                              {'form': UserCreationForm(), 'error':
                                  'Такое имя пользователя уже существует. Задайте другое.'})  # если не удалось
                # зарегестрироваться то возвращаемся на страницу заполнения формы

        else:
            return render(request, 'todo/signupuser.html',
                          {'form': UserCreationForm(), 'error': 'Пароли не совпадают.'})  # если не удалось
            # зарегестрироваться то возвращаемся на страницу заполнения формы


@login_required  # эта страница не должна показываться незаавторизованным пользователям
def currenttodos(request):
    return render(request, 'todo/currenttodos.html')


# чтобы пользователь разлогинелся

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')


# чтобы залогинелся
def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todo/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'],
                            password=request.POST['password'])  # то что пользователь введет в поле
        # username и password, эти данные сохранили в переменную user
        if user is None:  # если пользователя нет в БД то возвращаемся на форму авторизации
            return render(request, 'todo/loginuser.html',
                          {'form': AuthenticationForm(), 'error': 'Неверные данные для входа'})
        else:  # если пользователь есть в БД то будет перенаправляться на страницу Задачи
            login(request, user)
            return redirect('currenttodos')
