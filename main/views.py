from django.shortcuts import render
from django.http import HttpResponse
from .models import Ucheniki
from .models import Documenti
from .forms import ContactsForm
from django.views.generic import DetailView, UpdateView


class StudentDetailView(DetailView):
    model = Ucheniki
    template_name = 'main/index.html'
    context_object_name = 'student'


class StudentUpdateView(UpdateView):
    model = Ucheniki, Documenti
    extra_context = {}
    template_name = 'main/index.html'
    context_object_name = 'student'
    form_class = ContactsForm()

    def get_queryset(self):
        return


def index(request):
    students = Ucheniki.objects.all()
    error = ''
    if request.method == 'POST':
        form = ContactsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = ContactsForm()
    data = {
        'title': "Личный кабинет",
        'form': form
    }
    return render(request, 'main/index.html/1', data)


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
