from django.urls import path  # чтобы мы могли указывать пути
from . import views

urlpatterns = [
    path('', views.development, name='development'),
    path('<int:development_id>/', views.detail, name='development'),
]
