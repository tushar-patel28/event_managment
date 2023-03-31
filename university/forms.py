from django import forms
from .models import *
from register.models import *
#
#
# class EventForm(forms.ModelForm):
#     Event_Name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
#         'class': 'form-control',
#     }))
#     Event_Description = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
#         'class': 'form-control',
#     }))
#
#     Event_Date = forms.DateField(widget=forms.DateInput(attrs={
#         'type': 'date',
#         'class': 'form-control',
#     }))
#     Event_Time = forms.TimeField(widget=forms.TimeInput(attrs={
#         'type': 'time',
#         'class': 'form-control',
#     }))
#     Event_Type = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
#         'class': 'form-control',
#     }))
#
#     class Meta:
#         model = Event
#         exclude = ['user', 'volunteers']
#
#
# class SpeakerForm(forms.ModelForm):
#     Name = forms.CharField(max_length=80, widget=forms.TextInput(attrs={
#         'class': 'form-control',
#     }))
#     Gender = forms.CharField(max_length=12, widget=forms.TextInput(attrs={
#         'class': 'form-control',
#     }))
#     Email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={
#         'class': 'form-control',
#     }))
#     description =forms.CharField(max_length=120, widget=forms.TextInput(attrs={
#         'class': 'form-control',
#     }))
#     mobile_no = forms.CharField(max_length=10, widget=forms.TextInput(attrs={
#         'class': 'form-control',
#     }))
#
#     class Meta:
#         model = Speakers
#         fields = '__all__'
#         widgets = {
#             'event': forms.Select(attrs={
#                 'class': 'form-control'
#             })
#         }
#
#
# class ParticipantsForm(forms.ModelForm):
#     Name = forms.CharField(max_length=80, widget=forms.TextInput(attrs={
#         'class': 'form-control',
#     }))
#     Gender = forms.CharField(max_length=12, widget=forms.TextInput(attrs={
#         'class': 'form-control',
#     }))
#     Institute = forms.CharField(max_length=80, widget=forms.TextInput(attrs={
#         'class': 'form-control',
#     }))
#     Email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={
#         'class': 'form-control',
#     }))
#     mobile_no = forms.CharField(max_length=10, widget=forms.TextInput(attrs={
#         'class': 'form-control',
#     }))
#     field = forms.CharField(max_length=80, widget=forms.TextInput(attrs={
#         'class': 'form-control',
#     }))
#     semester = forms.IntegerField( widget=forms.NumberInput(attrs={
#         'class': 'form-control',
#     }))
#
#     class Meta:
#         model = Participants
#         fields = '__all__'
#         exclude = ['event']
#
#
class ESUserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ESRegisterForm(forms.ModelForm):
    mobile_no = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    gender = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    field = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    Department = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = CordinatorRegister
        exclude = ['user', 'is_cordinator']

#
# class VUserForm(forms.ModelForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control'
#     }))
#     first_name = forms.CharField(widget=forms.TextInput(
#         attrs={
#             'class': 'form-control'
#         }
#     ))
#     last_name = forms.CharField(widget=forms.TextInput(
#         attrs={
#             'class': 'form-control'
#         }
#     ))
#     email = forms.EmailField(widget=forms.EmailInput(attrs={
#         'class': 'form-control'
#     }))
#
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email')
#
#
# class VRegisterForm(forms.ModelForm):
#     mobile_no = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control'
#     }))
#     gender = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control'
#     }))
#     institute = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control'
#     }))
#     field = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control'
#     }))
#     semester = forms.IntegerField(widget=forms.NumberInput(attrs={
#         'class': 'form-control'
#     }))
#
#     class Meta:
#         model = VisitorRegister
#         exclude = ['user', 'is_visitor']
#
#
# class PastEventForm(forms.ModelForm):
#     Event_Name = forms.CharField(max_length=80, widget=forms.TextInput(attrs={
#         'class': 'form-control'
#     }))
#     Description = forms.CharField(max_length=120, widget=forms.TextInput(attrs={
#         'class': 'form-control'
#     }))
#     Place = forms.CharField(max_length=120, widget=forms.TextInput(attrs={
#         'class': 'form-control'
#     }))
#     DateAndTime = forms.DateTimeField(widget=forms.DateTimeInput(attrs={
#         'type': 'datetime-local',
#         'class': 'form-control',
#     }))
#     video = forms.FileField(widget=forms.FileInput(attrs={
#         'class': 'form-control'
#     }))
#
#     class Meta:
#         model = PastEvent
#         fields = '__all__'
#
#
# class ImageForm(forms.ModelForm):
#     image = forms.ImageField(label='Image', widget=forms.FileInput(attrs={
#         'class': 'form-control',
#     }))
#
#     class Meta:
#         model = Images
#         fields = ('image', )
