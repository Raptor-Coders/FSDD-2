from django.db import models


# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=50, blank=False, help_text='Name of Course')
    description = models.TextField(max_length=1000, blank=True, default='')
    sessions = models.IntegerField(blank=True, help_text='Number of Sessions')
    session_duration = models.IntegerField(blank=True, help_text='Session duration in minutes')
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    tags = models.CharField(max_length=1000, blank=True)
    is_featured = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_hidden = models.BooleanField(default=False)
    image_url = models.CharField(max_length=1000, blank=True)
    max_students = models.IntegerField(blank=False, default=3)

    def __str__(self):
        return self.name
    
    