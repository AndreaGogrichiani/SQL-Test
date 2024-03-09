from django.shortcuts import render, redirect
from .models import Events
from django.http import HttpResponse

def eventinfo(request, title):

    event_list = Events.objects.all()

    titles = [event.title for event in event_list]

    return render(request, 'Event/eventinfo.html', {'titles': titles})

def errorpage(request):
    return HttpResponse("ERROR")

