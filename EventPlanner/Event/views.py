from django.shortcuts import render, redirect
from .models import Events
from django.http import HttpResponse
from .forms import EventForm

def add_event(request):
    return render(request, 'Event/add_event.html')

def eventinfo(request, title):
    try:
        event = Events.objects.get(title__iexact=title)
        return render(request, 'Event/eventinfo.html', {'event': event})
    except Events.DoesNotExist:
        return HttpResponse("Event not found")


def errorpage(request):
    return HttpResponse("ERROR")

