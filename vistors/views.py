from django.shortcuts import render, redirect
from university.models import *
from coedinator.models import *
from register.models import *
from university.forms import *
from coedinator.forms import *
from django.contrib import messages
import datetime

# Create your views here.


def event_list(request):
    eve_list = Event.objects.filter(for_visitors=True, Event_Date__range=[datetime.date.today(), '2222-12-31'])
    return render(request, 'visitor/events.html', {'events': eve_list})


def event_details(request, id):
    eve_list = Event.objects.get(id=id)
    speaker = Speakers.objects.filter(event_id=id)
    return render(request, 'visitor/event_details.html', {'events': eve_list, 'speaker': speaker})


def participate(request, id):
    u = Event.objects.get(id=id)
    if request.method == 'POST':
        form = ParticipantsForm(request.POST)

        if form.is_valid():
            form_r = form.save(commit=False)
            form_r.event = u
            form.save()
            return redirect('visitors:event_list')

        else:
            print(form.errors)
    else:
        form = ParticipantsForm()
    return render(request, 'visitor/participants.html', {'form': form})
