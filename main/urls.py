from django.urls import path
from . import views

urlpatterns = [
    path('student', views.index, name='home'),
    path('schedule', views.schedule, name='schedule'),
    path('tests', views.tests, name='tests'),
    path('history', views.history, name='history'),
    path('login', views.login, name='login'),
    path('teacher', views.teacher, name='teacher'),
    path('students', views.students, name='students')
]