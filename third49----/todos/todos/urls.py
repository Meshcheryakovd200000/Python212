from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('signup/', views.signupuser, name='signupuser'),  # первый путь для авторизации
    path('logout/', views.logoutuser, name='logoutuser'),  # первый путь для выхода
    path('login/', views.loginuser, name='loginuser'),  # первый путь для входа

    # Todos Задачи
    path('', views.home, name='home'),  # когда пользователь нажал на Выход то он переходит на главную страницу
    path('current/', views.currenttodos, name='currenttodos'),  # текущие задачи
    path('create/', views.createtodo, name='createtodo'),
    path('todo/<int:todo_pk>/', views.viewtodo, name='viewtodo'),
]
