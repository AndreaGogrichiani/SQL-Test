from django.shortcuts import render, redirect
from .models import Events
from django.http import HttpResponse, HttpResponseRedirect
from .forms import EventForm


def add_event(request):
    submitted = False
    form = EventForm
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/events/submitted/')
    else:
        form = EventForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'Event/add_event.html', {'form': form, 'submitted': submitted})

def eventinfo(request, title):
    try:
        event = Events.objects.get(title__iexact=title)
        return render(request, 'Event/eventinfo.html', {'event': event})
    except Events.DoesNotExist:
        return redirect('/events/errorpage/')


def errorpage(request):
    return HttpResponse("ERROR")

def submitted(request):
    return HttpResponse("Submitted Successfully")
