from django.urls import path  # чтобы мы могли указывать пути
from . import views

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
]























