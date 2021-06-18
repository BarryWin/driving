from django.urls import path
from . import views

urlpatterns = [
    path('student', views.index, name='home'),
    path('schedule', views.schedule, name='schedule'),
    path('tests', views.tests, name='tests'),
    path('history', views.history, name='history'),
    path('login', views.login, name='login'),
    path('teacher', views.teacher, name='teacher'),
    path('schedule-teacher', views.scheduleTeacher, name='schedule-teacher'),
    path('students', views.students, name='students'),
    path('chat', views.chat, name='chat'),
    path('student/<int:pk>', views.StudentDetailView.as_view(), name='student-detail'),
    path('student/<int:pk>', views.StudentUpdateView.as_view(), name='student-update')
]