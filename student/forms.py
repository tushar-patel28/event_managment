from django import forms
from django.contrib.auth.models import User
from register.models import *


class SUserForm(forms.ModelForm):
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


class SRegisterForm(forms.ModelForm):
    mobile_no = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    gender = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    field = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    semester = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = StudentRegister
        exclude = ['user', 'is_student']
