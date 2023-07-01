from django.shortcuts import render


# Create your views here.

def repairs(request):
    return render(request, 'repairs/repairs.html')
