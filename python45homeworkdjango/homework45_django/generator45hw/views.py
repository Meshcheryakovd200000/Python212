from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("My first Django app.")
# Create your views here.
