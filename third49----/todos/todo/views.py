from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TodoForm
from .models import Todo


# Create your views here.
# Обработчики

def home(request):
    return render(request, 'todo/home.html')


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


def currenttodos(request):  # страница 'Актуальные'
    todos = Todo.objects.filter(user=request.user, date_completed__isnull=True)  # показывает что objects нету т.к.
    # не платная версия PyCharm. # выводим данные только этого пользователя
    return render(request, 'todo/currenttodos.html', {'todos': todos})


# чтобы пользователь разлогинелся

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


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


def createtodo(request):
    if request.method == 'GET':  # когда доступ к странице методом GET то
        return render(request, 'todo/createtodo.html', {'form': TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            new_todo = form.save(commit=False)
            new_todo.user = request.user
            new_todo.save()  # сохранение данных с формы в БД
            return redirect('currenttodos')  # после сохранения возвращаем на страницу "currenttodos" Актуальные задачи
        except ValueError:
            return render(request, 'todo/createtodo.html', {
                'form': TodoForm(),
                'error': 'Переданы неверные данные. Попробуйте ещё раз'})  # если данные не сохранились то
            # оставляем пользователя на той же странице


def viewtodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk)  # если запись есть по ключу pk то
    # появится запись, иначе вернется ошибка 404
    return render(request, 'todo/viewtodo.html', {'todo': todo})  # чтобы получить данные создаем {'todo': todo}
