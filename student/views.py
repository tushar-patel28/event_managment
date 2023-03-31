from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from university.models import *
from coedinator.models import *
from register.models import *
from django.contrib import messages
from .forms import *
from university.forms import *
from coedinator.forms import *
import datetime
# Create your views here.


def event_list(request):
    eve_list = Event.objects.filter(Event_Date__range=[datetime.date.today(), '2222-12-31'])
    return render(request, 'student/events.html', {'events': eve_list})


def event_details(request, id):
    eve_list = Event.objects.get(id=id)
    speaker = Speakers.objects.filter(event_id=id)
    return render(request, 'student/event_details.html', {'events': eve_list, 'speaker': speaker})


def participate(request, id):
    u = Event.objects.get(id=id)
    if request.method == 'POST':
        form = ParticipantsForm(request.POST)

        if form.is_valid():
            form_r = form.save(commit=False)
            form_r.event = u
            form.save()
            return redirect('student:events')
        else:
            print(form.errors)
    else:
        form = ParticipantsForm()
    return render(request, 'student/participants.html', {'form': form})


def volunteer(request, id):
    u = Event.objects.get(id=id)
    user = StudentRegister.objects.get(user_id=request.user)
    u.volunteers.add(user)
    return redirect('student:events')


def manage_profile(request):

    instance2 = StudentRegister.objects.get(user_id=request.user)
    instance = User.objects.get(id=instance2.user.id)
    form_p = SUserForm(request.POST or None, instance=instance)
    form = SRegisterForm(request.POST or None, request.FILES or None, instance=instance2)
    if form.is_valid() and form_p.is_valid():

        form_p.save()
        # here connected OneToOneField with user table
        form.save()

        return redirect('student:events')
    else:
        print(form.errors)
    return render(request, 'student/s_register.html', {'form': form, 'form_p': form_p})


def change_password(request):
    user = StudentRegister.objects.get(user_id=request.user)
    if request.method == 'POST':

        u = User.objects.get(id=user.user.id)

        form = PasswordChangeForm(u, request.POST)
        if form.is_valid():
            user = form.save()

            messages.success(request, 'Your password was successfully updated!')
            return redirect('student:events')
        else:
            messages.error(request, 'Please correct the error below.')
            print(form.errors)
            return redirect('student:change_password')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'student/change_password.html', {'form': form, 'user': user})


def past_events(request):
    e_list = PastEvent.objects.all()
    return render(request, 'student/p_event_list.html', {'e_list': e_list})


def past_details(request, id):
    e_list = PastEvent.objects.get(id=id)
    im = Images.objects.filter(event_id=e_list.id)

    return render(request, 'student/p_event_det.html', {'e_list': e_list, 'im': im})
