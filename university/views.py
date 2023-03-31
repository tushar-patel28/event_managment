from django.contrib import messages
from django.forms import modelformset_factory
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.template import RequestContext
from django.urls import reverse
import datetime
from .forms import *
from register.models import *
from coedinator.models import *
from .models import *
# Create your views here.


# def add_event(request):
#     u = AdminRegister.objects.get(user_id=request.user)
#     if request.method == 'POST':
#
#         form = EventForm(request.POST, request.FILES)
#
#         if form.is_valid():
#
#             form_r = form.save(commit=False)
#             form_r.user = u
#             form_r.save()
#             return redirect('university:event_list')
#         else:
#             print(form.errors)
#     else:
#         form = EventForm()
#     return render(request, 'university/add_event.html', {'form': form})


def event_list(request):
    eve_list = Event.objects.all()
    return render(request, 'university/events.html', {'events': eve_list})


def event_details(request, id):
    eve_list = Event.objects.get(id=id)
    participant_list = Participants.objects.filter(event_id=id)
    speaker = Speakers.objects.filter(event_id=id)
    return render(request, 'university/event_details.html', {'events': eve_list, 'part': participant_list, 'speaker': speaker})


def event_edit(request, id):
    instance = get_object_or_404(Event, id=id)

    form = EventForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()

        return redirect('university:event_list')
    else:
        print(form.errors)
    return render(request, 'university/edite_event.html', {'form': form})


def event_delete(request, id):
    user2 = Event.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('university:event_list'))


def add_speaker(request):
    if request.method == 'POST':
        form = SpeakerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('university:event_list')
        else:
            print(form.errors)
    else:
        form = SpeakerForm()
    return render(request, 'university/add_speaker.html', {'form': form})


def visitors_list(request):
    visitors = VisitorRegister.objects.all()
    return render(request, 'university/visitors_list.html', {'visitors': visitors})

def visitors_delete(request, id):
    user2 = VisitorRegister.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('university:visitors_list'))


def edit_visitors(request, id):
    instance2 = VisitorRegister.objects.get(id=id)
    instance = User.objects.get(id=instance2.user.id)
    form_p = VUserForm(request.POST or None, instance=instance)
    form = VRegisterForm(request.POST or None, request.FILES or None, instance=instance2)
    if form.is_valid() and form_p.is_valid():

        form_p.save()
        # here connected OneToOneField with user table
        form.save()

        return redirect('university:visitors_list')
    else:
        print(form.errors)
    return render(request, 'university/edite_visitors.html', {'form': form, 'form_p': form_p})


def students_list(request):
    student = StudentRegister.objects.all()
    return render(request, 'university/student_list.html', {'student': student})


def cordinator_list(request):
    cordinator = CordinatorRegister.objects.all()

    return render(request, 'university/cordinator_list.html', {'cordinator': cordinator})


def edit_cordinator(request, id):
    instance2 = CordinatorRegister.objects.get(id=id)
    instance = User.objects.get(id=instance2.user.id)
    form_p = ESUserForm(request.POST or None, instance=instance)
    form = ESRegisterForm(request.POST or None, request.FILES or None, instance=instance2)
    if form.is_valid() and form_p.is_valid():

        form_p.save()
        # here connected OneToOneField with user table
        form.save()

        return redirect('university:cordinator_list')
    else:
        print(form.errors)
    return render(request, 'university/edite_cordinator.html', {'form': form, 'form_p': form_p})

def cordinator_delete(request, id):
    user2 = CordinatorRegister.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('university:cordinator_list'))

# def post(request):
#
#     ImageFormSet = modelformset_factory(Images,
#                                         form=ImageForm, extra=6)
#
#     if request.method == 'POST':
#
#         postForm = PastEventForm(request.POST, request.FILES)
#         formset = ImageFormSet(request.POST, request.FILES,
#                                queryset=Images.objects.none())
#
#         if postForm.is_valid() and formset.is_valid():
#             post_form = postForm.save(commit=False)
#
#             post_form.save()
#
#             for form in formset:
#                 data = form.cleaned_data
#                 image = data.get('image')
#                 print(image)
#                 if image:
#                     photo = Images(event=post_form, image=image)
#                     photo.save()
#                 else:
#                     break
#             messages.success(request,
#                              "Posted!")
#             return HttpResponseRedirect(reverse('university:event_list'))
#         else:
#             print(postForm.errors, formset.errors)
#     else:
#         postForm = PastEventForm()
#         formset = ImageFormSet(queryset=Images.objects.none())
#     return render(request, 'university/past_evnt.html', {'postForm': postForm, 'formset': formset})


def past_events(request):
    e_list = PastEvent.objects.all()
    return render(request, 'university/p_event_list.html', {'e_list': e_list})


def past_details(request, id):
    e_list = PastEvent.objects.get(id=id)
    im = Images.objects.filter(event_id=e_list.id)
    return render(request, 'university/p_event_det.html', {'e_list': e_list, 'im': im})
