from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.


class AdminRegister(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    mobile_no = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{9,10}$')])
    is_uni = models.BooleanField(default=True)
    profile_photo = models.ImageField(upload_to='profile_pic', null=True, blank=True)

    def __str__(self):
        return self.user.first_name


class CordinatorRegister(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    mobile_no = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{9,10}$')])
    field = models.CharField(max_length=20)
    Department = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    is_cordinator = models.BooleanField(default=True)
    profile_photo = models.ImageField(upload_to='profile_pic', null=True, blank=True)

    def __str__(self):
        return self.user.first_name


class StudentRegister(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    mobile_no = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{9,10}$')])
    field = models.CharField(max_length=20)
    semester = models.IntegerField()
    gender = models.CharField(max_length=10)
    is_student = models.BooleanField(default=True)
    profile_photo = models.ImageField(upload_to='profile_pic', null=True, blank=True)

    def __str__(self):
        return self.user.first_name


class VisitorRegister(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    mobile_no = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{9,10}$')])
    gender = models.CharField(max_length=10)
    institute = models.CharField(max_length=70)
    field = models.CharField(max_length=20)
    semester = models.IntegerField()
    is_visitor = models.BooleanField(default=True)
    profile_photo = models.ImageField(upload_to='profile_pic', null=True, blank=True)

    def __str__(self):
        return self.user.first_name
