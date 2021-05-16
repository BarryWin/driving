from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def schedule(request):
    return render(request, 'main/schedule.html')


def tests(request):
    return render(request, 'main/tests.html')


def history(request):
    return render(request, 'main/history.html')


def login(request):
    return render(request, 'main/login.html')
# Create your views here.
