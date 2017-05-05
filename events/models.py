from django.db import models
from datetime import datetime

timezones = (('America/Bogota', 'America/Bogota'),('(UTC-0800) America/Los_Angeles', 'America/Los_Angeles',))

class Event(models.Model):
    # date_start = models.DateTimeField(auto_now=False, auto_now_add=False,)
    # date_end = models.DateTimeField(auto_now=False, auto_now_add=False,)
    title = models.CharField(max_length=100)
    date_start = models.DateTimeField(default=datetime.now)
    date_end = models.DateTimeField(default=datetime.now)
    description = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    timezone = models.CharField(default='America/Bogota', choices=timezones, max_length=255)
    organizer = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ('id',)
