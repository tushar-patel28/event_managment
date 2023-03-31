from django.db import models
from register.models import *
from django.core.validators import RegexValidator
# Create your models here.


class Event(models.Model):
    user = models.ForeignKey(CordinatorRegister, on_delete=models.CASCADE)
    Event_Name = models.CharField(max_length=50)
    Event_Description = models.CharField(max_length=120, null=True, blank=True)
    Event_Date = models.DateField()
    Event_Time = models.TimeField()
    Event_Banner = models.ImageField(upload_to='event_banner', null=True, blank=True)
    for_visitors = models.BooleanField(default=False)
    volunteers = models.ManyToManyField(StudentRegister)
    Event_Type = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.Event_Name


class Speakers(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    Name = models.CharField(max_length=80)
    Gender = models.CharField(max_length=12)
    Email = models.EmailField()
    mobile_no = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{9,10}$')])
    description = models.CharField(max_length=120)

    def __str__(self):
        return self.Name


class Participants(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    Name = models.CharField(max_length=80)
    Gender = models.CharField(max_length=12)
    Institute = models.CharField(max_length=80)
    Email = models.EmailField()
    mobile_no = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{9,10}$')])
    field = models.CharField(max_length=80)
    semester = models.IntegerField()

    def __str__(self):
        return self.Name


class PastEvent(models.Model):
    Event_Name = models.CharField(max_length=80)
    Description = models.CharField(max_length=120)
    Place = models.CharField(max_length=120)
    DateAndTime = models.DateTimeField()
    video = models.FileField(upload_to='event_video/', blank=True, null=True)

    def __str__(self):
        return self.Event_Name


def get_image_filename(instance, filename):
    id = instance.event.id
    return "post_images/%s" % (id)


class Images(models.Model):
    event = models.ForeignKey(PastEvent, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_filename,
                              verbose_name='Image', blank=True, null=True)
from django.db import models

# Create your models here.
