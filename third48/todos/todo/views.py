from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TodoForm
from .models import Todo
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.
# Обработчики

def home(request):
    return render(request, 'todo/home.html')


def signupuser(request):  # форма регистрации
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
def currenttodos(request):  # страница 'Актуальные'
    todos = Todo.objects.filter(user=request.user, date_completed__isnull=True)  # показывает что objects нету т.к.
    # не платная версия PyCharm. # выводим данные только этого пользователя
    return render(request, 'todo/currenttodos.html', {'todos': todos})


# чтобы пользователь разлогинелся
@login_required()  # эта страница не должна показываться незаавторизованным пользователям
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


# чтобы залогинелся
def loginuser(request):  # Авторизация пользователя
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


@login_required()  # эта страница не должна показываться незаавторизованным пользователям
def createtodo(request):  # Создание задачи
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


@login_required()  # эта страница не должна показываться незаавторизованным пользователям
def viewtodo(request, todo_pk):  # редактирование записи
    todo = get_object_or_404(Todo, pk=todo_pk)  # если запись есть по ключу pk то
    # появится запись, иначе вернется ошибка 404
    if request.method == 'GET':
        form = TodoForm(instance=todo)  # "instance=todo" - на страницах /todo/x/ - то
        # что в title попадет в title а memo в memo
        return render(request, 'todo/viewtodo.html', {'todo': todo, 'form': form})  # чтобы получить
        # данные создаем {'todo': todo, 'form': form}
    else:
        try:
            form = TodoForm(request.POST, instance=todo)  # редактируем задачу и сохраняем, чтобы не создавалась
            # новая задача то instance=todo
            form.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'todo/viewtodo.html',
                          {'todo': todo,
                           'form': form,
                           'except': 'Неверные данные'})  # если пойдет сбой в БД


@login_required()  # эта страница не должна показываться незаавторизованным пользователям
def completetodo(request, todo_pk):  # выполненные задачи
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.date_completed = timezone.now()  # автоматически заполняет время в случае выполнения задачи
        todo.save()  # сохраняем в БД с измененным полем date_completed
        return redirect('currenttodos')  # переходим на страницу выполненные задачи


@login_required()  # эта страница не должна показываться незаавторизованным пользователям
def deletetodo(request, todo_pk):  # Удаление задач
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('currenttodos')  # после удаления преход на currenttodos


@login_required()  # эта страница не должна показываться незаавторизованным пользователям
def completedtodos(request):  # задачи выполнены
    todos = Todo.objects.filter(user=request.user,
                                date_completed__isnull=False).order_by('-date_completed')  # data_completed - не NULL
    return render(request, 'todo/completedtodos.html', {'todos': todos})
