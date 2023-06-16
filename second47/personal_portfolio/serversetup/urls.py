from django.urls import path  # чтобы мы могли указывать пути
from . import views

urlpatterns = [
    path('', views.serversetup, name='serversetup'),
    path('<int:serversetup_id>/', views.detail, name='serversetup'),
]