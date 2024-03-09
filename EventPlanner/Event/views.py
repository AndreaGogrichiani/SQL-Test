from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Events


def eventinfo(request, title):
    # Retrieve the event(s) based on the provided title (you'll need to adjust this)
    event_list = Events.objects.filter(title=title)

    # You can pass the event_list to a template for rendering
    return render(request, 'EventPlanner/eventinfo.html', {'event_list': event_list})

def errorpage(request):
    return HttpResponse("ERROR")

