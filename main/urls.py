from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('schedule', views.schedule, name='schedule'),
    path('tests', views.tests, name='tests'),
    path('history', views.history, name='history')
]