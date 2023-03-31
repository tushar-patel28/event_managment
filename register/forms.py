from django import forms
from django.contrib.auth.models import User
from .models import *


class UserForm(forms.ModelForm):
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
    password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    Confirm_Password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'Confirm_Password')


class RegisterForm(forms.ModelForm):
    mobile_no = forms.CharField(max_length=10, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    class Meta:
        model = AdminRegister
        exclude = ['user', 'is_uni']


class CUserForm(forms.ModelForm):
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
    password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    Confirm_Password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'Confirm_Password')


class CRegisterForm(forms.ModelForm):
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
    password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    Confirm_Password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'Confirm_Password')

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


class VUserForm(forms.ModelForm):
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
    password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    Confirm_Password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'Confirm_Password')


class VRegisterForm(forms.ModelForm):
    mobile_no = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    gender = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    institute = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    field = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    semester = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = VisitorRegister
        exclude = ['user', 'is_visitor']
