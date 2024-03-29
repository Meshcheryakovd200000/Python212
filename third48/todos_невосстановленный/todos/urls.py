"""
URL configuration for todos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('signup/', views.signupuser, name='signupuser'),  # первый путь для авторизации
    path('logout/', views.logoutuser, name='logoutuser'),  # первый путь для выхода
    path('login/', views.loginuser, name='loginuser'),  # первый путь для входа

    # Todos
    path('', views.home, name='home'),  # когда пользователь нажал на Выход то он переходит на главную страницу
    path('current/', views.currenttodos, name='currenttodos'),  # текущие задачи
]





























