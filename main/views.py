from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def schedule(request):
    return render(request, 'main/schedule.html')

# Create your views here.
