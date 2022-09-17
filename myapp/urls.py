from calendar import calendar
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('counter', views.counter, name = 'counter'),
    path('register', views.register, name = 'register'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name = 'logout'),
    path('post/<str:a>', views.post, name = 'post'),
    re_path(r'^calendar/$', views.CalendarView.as_view(), name='calendar')
]