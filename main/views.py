from django.shortcuts import render
from django.http import HttpResponse
from .models import Ucheniki
from .forms import ContactsForm

def index(request):
    students = Ucheniki.objects.all()
    form = ContactsForm()
    data = {
        'title': "Личный кабинет",
        'form': form
    }
    return render(request, 'main/index.html', {'students': students[:1], 'data': data})


def teacher(request):
    data = {
        'title': "Личный кабинет"
    }
    return render(request, 'main/teacher.html', data)


def schedule(request):
    data = {
        'title': "Расписание"
    }
    return render(request, 'main/schedule.html', data)


def tests(request):
    data = {
        'title': "Тестирование"
    }
    return render(request, 'main/tests.html', data)


def history(request):
    return render(request, 'main/history.html')


def login(request):
    return render(request, 'main/login.html')


def scheduleTeacher(request):
    return render(request, 'main/schedule-teacher.html')


def students(request):
    students = Ucheniki.objects.all()
    return render(request, 'main/students.html', {'students': students})


def chat(request):
    return render(request, 'main/chat.html')
# Create your views here.
