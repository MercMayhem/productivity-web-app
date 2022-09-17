from asyncio import events
from multiprocessing import Event
from django.contrib import admin
from .models import feature, Event

# Register your models here.
admin.site.register(feature)
admin.site.register(Event)