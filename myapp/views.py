from typing import AsyncContextManager
from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import django.contrib.auth as auth
from django.contrib.auth import authenticate
from django.contrib import messages
from .models import feature
from datetime import datetime, timedelta, date
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe

from .models import *
from .utils import Calendar
# Create your views here.

def index(request):
    features = feature.objects.all()
    return render(request, 'index.html', {'features' : features})

def counter(request):
    posts = [1, 12, 'aman', 24, 133, 'tim']
    return render(request, 'counter.html', {'posts' : posts})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email = email).exists():
                messages.info(request, 'Email already used!')
                return redirect('register')

            elif User.objects.filter(username = username).exists():
                messages.info(request, 'Username already used!')
                return redirect('register')

            else:
                user = User.objects.create_user(username = username, email = email, password = password)
                user.save();
                return redirect('login')

        else:
            messages.info(request, 'Password not the same')
            return redirect('register')

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'credentials invalid')
            return redirect('login')
    
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/' )

def post(request, a):
    return render(request, 'post.html', {'value': a})

def calendar(request):
    return render(request, 'calendar.html')

class CalendarView(generic.ListView):
    model = Event
    template_name = r'C:\Users\amanr\OneDrive\Documents\Coding projects\mysite\templates\calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        id = self.request.user.id
        html_cal = cal.formatmonth(withyear=True, id=id)
        context['calendar'] = mark_safe(html_cal)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()